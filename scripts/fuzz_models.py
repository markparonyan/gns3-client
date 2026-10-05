"""Decode spec-valid payloads with the generated models.

For every object schema in the OpenAPI document, hypothesis generates JSON
instances that are valid against the spec; each must decode with msgspec
into the matching Struct and encode back to the same JSON. Then each
required field is dropped in turn and the decode must fail.

Usage: python scripts/fuzz_models.py [openapi.json] [models.py] [examples]
Needs: hypothesis-jsonschema (dev only).
"""

from __future__ import annotations

import datetime as dt
import importlib.util
import json
import re
import sys
import warnings
from pathlib import Path

import msgspec
from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st
from hypothesis.errors import NonInteractiveExampleWarning
from hypothesis_jsonschema import from_schema

warnings.simplefilter("ignore", NonInteractiveExampleWarning)

SPEC_PATH = Path(sys.argv[1] if len(sys.argv) > 1 else "gns3openapi.json")
MODELS_PATH = Path(sys.argv[2] if len(sys.argv) > 2 else "gns3client/models.py")
EXAMPLES = int(sys.argv[3]) if len(sys.argv) > 3 else 50

_spec = importlib.util.spec_from_file_location("gns3_models_under_test", MODELS_PATH)
models = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = models
_spec.loader.exec_module(models)

SCHEMAS = json.loads(SPEC_PATH.read_text())["components"]["schemas"]
KNOWN_FORMATS = {"date-time", "uuid", "email", "uri"}
# hypothesis-jsonschema has no uuid strategy and would emit any string.
FORMATS = {
    "uuid": st.uuids().map(str),
    # RFC 3339: offsets are whole minutes; the server emits naive or UTC.
    "date-time": st.datetimes(timezones=st.none() | st.just(dt.UTC)).map(
        lambda d: d.isoformat()
    ),
}


def clean(node):
    """Make an OpenAPI 3.1 component usable as a standalone JSON Schema."""
    if isinstance(node, dict):
        out = {}
        for k, v in node.items():
            if k == "$ref":
                out[k] = v.replace("#/components/schemas/", "#/$defs/")
            elif (
                k == "format"
                and v not in KNOWN_FORMATS
                or k
                in ("example", "examples", "writeOnly", "readOnly", "discriminator")
            ):
                continue
            elif k == "properties":
                out[k] = {p: clean(s) for p, s in v.items()}
            else:
                out[k] = clean(v)
        return out
    if isinstance(node, list):
        return [clean(i) for i in node]
    return node


DEFS = {name: clean(s) for name, s in SCHEMAS.items()}


def camel(name: str) -> str:
    parts = re.split(r"[^0-9a-zA-Z]+", name)
    return "".join(p[:1].upper() + p[1:] for p in parts if p)


def gen_class(name: str):
    for cand in (name, camel(name)):
        cls = getattr(models, cand, None)
        if isinstance(cls, type) and issubclass(cls, msgspec.Struct):
            return cls
    return None


def canon(value):
    """Normalise JSON for comparison (datetimes may be re-formatted)."""
    if isinstance(value, dict):
        return {k: canon(v) for k, v in value.items()}
    if isinstance(value, list):
        return [canon(v) for v in value]
    if isinstance(value, str):
        try:
            d = dt.datetime.fromisoformat(value)
            if "T" in value or " " in value:
                return ("datetime", d)
        except ValueError:
            pass
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value


def first_difference(a, b, path="$"):
    if isinstance(a, dict) and isinstance(b, dict):
        for k in a.keys() & b.keys():
            if d := first_difference(a[k], b[k], f"{path}.{k}"):
                return d
        return None
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return f"{path}: length {len(a)} != {len(b)}"
        for i, (x, y) in enumerate(zip(a, b)):
            if d := first_difference(x, y, f"{path}[{i}]"):
                return d
        return None
    return None if a == b else f"{path}: {a!r} != {b!r}"


def check_schema(name: str, schema: dict, decoder: msgspec.json.Decoder) -> list[str]:
    props = schema["properties"]
    strategy = from_schema({**DEFS[name], "$defs": DEFS}, custom_formats=FORMATS)
    errors: list[str] = []

    @settings(
        max_examples=EXAMPLES,
        deadline=None,
        database=None,
        suppress_health_check=list(HealthCheck),
    )
    @given(strategy)
    def roundtrip(instance):
        raw = json.dumps(instance).encode()
        try:
            obj = decoder.decode(raw)
        except msgspec.ValidationError as exc:
            errors.append(f"rejects valid payload: {exc}\n      {raw[:300]!r}")
            return
        back = json.loads(msgspec.json.encode(obj))
        # Fields absent from the input come back only as their spec default.
        for key, value in back.items():
            if (
                key not in instance
                and props.get(key, {}).get("default", object()) != value
            ):
                errors.append(f"encode adds {key}={value!r} not in input/default")
        # Every known top-level key survives; nested values must agree
        # wherever both sides have a key (unknown keys are dropped and
        # defaults filled in on decode, both intended).
        known = {k: v for k, v in instance.items() if k in props}
        lost = known.keys() - back.keys()
        diff = first_difference(canon(known), canon(back))
        if lost or diff:
            errors.append(
                f"round-trip changed payload: lost={sorted(lost)} {diff or ''}"
            )

    roundtrip()

    # Required fields must really be required.
    sample = strategy.example()
    for req in schema.get("required", []):
        bad = {k: v for k, v in sample.items() if k != req}
        try:
            decoder.decode(json.dumps(bad).encode())
            errors.append(f"accepts payload missing required {req!r}")
        except msgspec.ValidationError:
            pass
    return errors


failures: list[str] = []
checked = 0

for name, schema in SCHEMAS.items():
    if schema.get("type") != "object" or "properties" not in schema:
        continue
    cls = gen_class(name)
    if cls is None:
        failures.append(f"{name}: no generated struct")
        continue
    try:
        decoder = msgspec.json.Decoder(cls)
    except TypeError as exc:
        failures.append(f"{name}: msgspec cannot build a decoder: {str(exc)[:160]}")
        continue
    errors = check_schema(name, schema, decoder)
    checked += 1
    if errors:
        failures.append(f"{name}:\n    " + "\n    ".join(dict.fromkeys(errors)))

print(f"checked {checked} object schemas, {EXAMPLES} examples each")
if failures:
    print(f"{len(failures)} schema(s) with failures:")
    for f in failures:
        print(" -", f)
    sys.exit(1)
print("OK: every spec-valid payload decoded and round-tripped")
