"""Check gns3client/models.py against gns3openapi.json.

Compares, for every component schema in the OpenAPI document:
  * that a generated type exists for it (by name, or reused by value),
  * wire field names, required/optional, defaults,
  * field types, including nullability, enums, $refs and constraints,
by exporting the generated models back to JSON Schema with msgspec and
normalising both sides into a comparable form.

Usage: python scripts/check_models.py [openapi.json] [models.py]
Exit code is non-zero when any mismatch is found.
"""

from __future__ import annotations

import datetime as dt
import enum
import importlib.util
import inspect
import json
import re
import sys
import types
import typing
import uuid
from pathlib import Path

import msgspec

SPEC_PATH = Path(sys.argv[1] if len(sys.argv) > 1 else "gns3openapi.json")
MODELS_PATH = Path(sys.argv[2] if len(sys.argv) > 2 else "gns3client/models.py")
_spec = importlib.util.spec_from_file_location("gns3_models_under_test", MODELS_PATH)
models = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = models
_spec.loader.exec_module(models)
spec = json.loads(SPEC_PATH.read_text())
SPEC = spec["components"]["schemas"]

# Generated types (structs and enums) defined in the models module.
GEN = {
    name: obj
    for name, obj in vars(models).items()
    if inspect.isclass(obj)
    and obj.__module__ == models.__name__
    and (issubclass(obj, msgspec.Struct) or issubclass(obj, enum.Enum))
}

# Deviations introduced on purpose by scripts/postprocess_models.py.
ACCEPTED = {
    # untagged anyOf of structs, chosen by the sibling template_type field
    "TemplateSetting.template_properties",
}

# String formats msgspec has no native type for; generated as plain str.
STR_FORMATS = {"uri", "email", "password"}

problems: list[str] = []


def problem(msg: str) -> None:
    problems.append(msg)


STR_LIKE = (str, uuid.UUID, dt.datetime, dt.date, dt.time, bytes)


def str_like_members(hint) -> list:
    """Members of a union msgspec would treat as strings (it merges them)."""
    out = []
    stack = [hint]
    while stack:
        t = stack.pop()
        if isinstance(t, typing.TypeAliasType):
            stack.append(t.__value__)
        elif typing.get_origin(t) is typing.Annotated:
            stack.append(typing.get_args(t)[0])
        elif typing.get_origin(t) in (typing.Union, types.UnionType):
            stack.extend(typing.get_args(t))
        elif typing.get_origin(t) is typing.Literal:
            if any(isinstance(a, str) for a in typing.get_args(t)):
                out.append(t)
        elif isinstance(t, type) and issubclass(t, STR_LIKE + (enum.StrEnum,)):
            out.append(t)
    return out


# Every field type must be accepted by msgspec, otherwise no decoder can be
# built for the struct (or anything that contains it).
for gname, cls in GEN.items():
    if not issubclass(cls, msgspec.Struct):
        continue
    for fname, hint in typing.get_type_hints(cls, include_extras=True).items():
        try:
            msgspec.json.Decoder(hint)
        except TypeError as exc:
            problem(f"msgspec rejects {gname}.{fname}: {str(exc)[:160]}")
            continue
        # Two constrained str aliases in one union are silently merged into
        # one str with both constraints, which can reject every value.
        if len(str_like_members(hint)) > 1:
            problem(
                f"{gname}.{fname}: union of str-like types {str_like_members(hint)}"
            )

if problems:
    print(f"{len(problems)} problem(s):")
    for p in problems:
        print(" -", p)
    print("(structural comparison skipped: msgspec cannot export these models)")
    sys.exit(1)

# msgspec only emits `format: date-time` for tz-aware datetimes; emit it for
# any datetime so str and datetime fields can be told apart.
import msgspec._json_schema as _js

_orig_to_schema = _js._SchemaGenerator.to_schema


def _to_schema(self, t, check_ref=True):
    out = _orig_to_schema(self, t, check_ref)
    inner = t
    while isinstance(inner, msgspec.inspect.Metadata):
        inner = inner.type
    if isinstance(inner, msgspec.inspect.DateTimeType):
        out["format"] = "date-time"
    return out


_js._SchemaGenerator.to_schema = _to_schema

_, GEN_SCHEMAS = msgspec.json.schema_components(
    list(GEN.values()), ref_template="#/$gen/{name}"
)

IGNORED_KEYS = {"title", "description", "examples", "example", "writeOnly", "readOnly"}
CONSTRAINT_KEYS = (
    "format",
    "pattern",
    "minimum",
    "maximum",
    "exclusiveMinimum",
    "exclusiveMaximum",
    "minLength",
    "maxLength",
    "minItems",
    "maxItems",
)


def camel(name: str) -> str:
    """Approximate datamodel-codegen's class naming for a component name."""
    parts = re.split(r"[^0-9a-zA-Z]+", name)
    return "".join(p[:1].upper() + p[1:] for p in parts if p)


def enum_values(schema: dict) -> frozenset | None:
    if "enum" in schema:
        return frozenset(schema["enum"])
    if "const" in schema:
        return frozenset([schema["const"]])
    return None


# ---------------------------------------------------------------- name mapping
spec_to_gen: dict[str, str] = {}
for sname, sschema in SPEC.items():
    for cand in (sname, camel(sname)):
        if cand in GEN:
            spec_to_gen[sname] = cand
            break
    else:
        # --reuse-model: an identical enum may have been merged into another.
        vals = enum_values(sschema)
        if vals is not None:
            same = [
                g
                for g, cls in GEN.items()
                if issubclass(cls, enum.Enum)
                and frozenset(m.value for m in cls) == vals
            ]
            if same:
                spec_to_gen[sname] = same[0]
                print(f"note: {sname} reused as {same[0]}")
                continue
        problem(f"{sname}: no generated type")

unclaimed = set(GEN) - set(spec_to_gen.values())
for g in sorted(unclaimed):
    print(f"note: generated type {g} has no component schema of that name")


# --------------------------------------------------------------- normalisation
def norm(schema: dict, side: str, seen=()) -> frozenset:
    """Turn a (sub)schema into a frozenset of hashable 'atoms'.

    side is 'spec' or 'gen' and decides how $refs are resolved.
    """
    schema = {k: v for k, v in schema.items() if k not in IGNORED_KEYS}
    schema.pop("default", None)
    if "$ref" in schema:
        ref = schema["$ref"]
        if side == "spec":
            name = ref.rsplit("/", 1)[1]
            target = SPEC[name]
            label = spec_to_gen.get(name, name)
        else:
            label = ref.rsplit("/", 1)[1]
            target = GEN_SCHEMAS[label]
        vals = enum_values(target)
        if vals is not None:
            return frozenset([("enum", vals)])
        if target.get("type") == "object" and "properties" in target:
            # Generated structs may be renamed (e.g. Foo2); compare by the
            # spec->gen mapping on the spec side and by name on the gen side.
            return frozenset([("struct", label)])
        if label in seen:
            return frozenset([("recursive", label)])
        return norm(target, side, seen + (label,))
    for key in ("anyOf", "oneOf"):
        if key in schema:
            out = set()
            for sub in schema[key]:
                out |= norm(sub, side, seen)
            rest = {k: v for k, v in schema.items() if k != key}
            if rest.keys() - {"format"}:
                out |= norm(rest, side, seen)
            # `non-empty str | empty str` is any string.
            strs = {a for a in out if a[0] == "string"}
            if len(strs) > 1 and any(("maxLength", 0) in a[1] for a in strs):
                out = (out - strs) | {("string", ())}
            # `uuid | string` accepts any string; that is what str means.
            if ("string", ()) in out:
                out = {
                    a
                    for a in out
                    if not (a[0] == "string" and a[1] == (("format", "uuid"),))
                }
            return frozenset(out)
    vals = enum_values(schema)
    if vals is not None:
        return frozenset([("enum", vals)])
    typ = schema.get("type")
    if isinstance(typ, list):
        out = set()
        for t in typ:
            out |= norm({**schema, "type": t}, side, seen)
        return frozenset(out)
    if schema.get("format") in STR_FORMATS:
        schema.pop("format")
    cons = tuple((k, schema[k]) for k in CONSTRAINT_KEYS if k in schema)
    if typ == "array":
        if "prefixItems" in schema:
            items = tuple(norm(i, side, seen) for i in schema["prefixItems"])
            return frozenset([("tuple", items, cons)])
        items = norm(schema.get("items", {}), side, seen)
        return frozenset([("array", items, cons)])
    if typ == "object":
        if schema.get("properties"):
            return frozenset([("inline-object", json.dumps(schema, sort_keys=True))])
        ap = schema.get("additionalProperties", True)
        vals = norm(ap, side, seen) if isinstance(ap, dict) else frozenset([("any",)])
        return frozenset([("dict", vals, cons)])
    if typ is None:
        return frozenset([("any",)])
    if typ == "integer" or typ == "number":
        # msgspec exports float constraints for number; keep int/number distinct.
        pass
    return frozenset([(typ, cons)])


def fmt(atoms: frozenset) -> str:
    return " | ".join(sorted(map(repr, atoms)))


# --------------------------------------------------------------- comparisons
for sname, sschema in SPEC.items():
    gname = spec_to_gen.get(sname)
    if gname is None:
        continue
    gschema = GEN_SCHEMAS[gname]
    svals, gvals = enum_values(sschema), enum_values(gschema)
    if svals is not None or gvals is not None:
        if svals != gvals:
            problem(f"{sname}: enum values {svals} != generated {gvals}")
        continue
    sprops = sschema.get("properties", {})
    gprops = gschema.get("properties", {})
    if set(sprops) != set(gprops):
        problem(
            f"{sname}: wire fields differ; missing={sorted(set(sprops) - set(gprops))}"
            f" extra={sorted(set(gprops) - set(sprops))}"
        )
    sreq = set(sschema.get("required", []))
    greq = set(gschema.get("required", []))
    if sreq != greq:
        problem(f"{sname}: required differ; spec={sorted(sreq)} gen={sorted(greq)}")

    cls = GEN[gname]
    gfields = {f.encode_name: f for f in msgspec.structs.fields(cls)}
    for prop, ps in sprops.items():
        if prop not in gprops:
            continue
        a, b = norm(ps, "spec"), norm(gprops[prop], "gen")
        # Optional fields are typed `X | None | UnsetType`; the None is only
        # legitimate when the spec allows null.
        if a != b and f"{sname}.{prop}" not in ACCEPTED:
            problem(
                f"{sname}.{prop}: type differs\n    spec: {fmt(a)}\n    gen:  {fmt(b)}"
            )
        f = gfields[prop]
        if gname.endswith("Update"):
            # postprocess_models.py: update models only send what is set.
            if f.default is not msgspec.UNSET and prop not in sreq:
                problem(
                    f"{sname}.{prop}: update field defaults to {f.default!r}, not UNSET"
                )
        elif "default" in ps:
            dflt = f.default
            if f.default_factory is not msgspec.NODEFAULT:
                dflt = f.default_factory()
            enc = (
                json.loads(msgspec.json.encode(dflt))
                if dflt is not msgspec.UNSET
                else "<UNSET>"
            )
            if enc != ps["default"]:
                problem(f"{sname}.{prop}: default spec={ps['default']!r} gen={enc!r}")
        elif prop not in sreq and f.default is not msgspec.UNSET:
            problem(f"{sname}.{prop}: spec has no default, gen default={f.default!r}")

print()
if problems:
    print(f"{len(problems)} problem(s):")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print("OK: all component schemas match")
