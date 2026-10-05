"""Post-process datamodel-codegen output so every model is usable by msgspec.

datamodel-codegen emits a few annotations that are valid Python but that
msgspec refuses to build a decoder for. Run after regenerating:

    python scripts/postprocess_models.py gns3client/models.py

Each rewrite must match at least once; a rewrite that stops matching means
the generator or the spec changed and this script needs a look.
"""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

REWRITES: list[tuple[str, str, str]] = [
    (
        # msgspec does not allow two str-like types in one union. The spec
        # says `uuid | string` (compute ids are a UUID or "local"), so the
        # only lossless type is str.
        "compute_id: UUID | str -> str",
        r"Annotated\[(?:UUID \| str|str \| UUID), ",
        "Annotated[str, ",
    ),
    (
        # A fixed-length tuple already encodes its length; msgspec rejects
        # min_length/max_length on tuple types.
        "ControlOffset: drop length constraints on tuple[float, float]",
        r"tuple\[float, float\], Meta\(max_length=2, min_length=2, ",
        "tuple[float, float], Meta(",
    ),
    (
        # The spec has an untagged anyOf of four structs; the variant is
        # chosen by the sibling `template_type` field, which msgspec cannot
        # use as a tag. Keep the raw mapping and convert it by template_type
        # in hand-written code.
        "TemplateSetting.template_properties: untagged struct union -> dict",
        r"QemuPropertiesV8 \| DynamipsPropertiesV8 \| IouPropertiesV8 \| DockerPropertiesV8,",
        "dict[str, Any],",
    ),
]


def collapse_empty_string_unions(text: str) -> tuple[str, int]:
    """Replace `Url | Url1` (minLength 1 | maxLength 0) unions with str.

    The spec allows "a non-empty URL or the empty string", i.e. any string.
    msgspec merges the constraints of str-like union members instead, so the
    generated field rejects every string.
    """
    empties = re.findall(
        r"^type (\w+) = Annotated\[\s*str,\s*Meta\(\s*max_length=0,", text, re.MULTILINE
    )
    total = 0
    for name in empties:
        text, n = re.subn(rf"\b(?:\w+|str) \| {name}\b", "str", text)
        total += n
    return text, total


def unset_update_defaults(text: str) -> tuple[str, int]:
    """Make every optional field of *Update models default to UNSET.

    The server applies updates with exclude_unset, so only fields the caller
    sets may be sent. A spec default such as NodeUpdate.x = 0 would otherwise
    be encoded on every update and move the node back to the origin.
    """
    # ast column offsets count UTF-8 bytes, so edit the encoded text.
    data = text.encode()
    lines = data.splitlines(keepends=True)
    offsets = [0]
    for line in lines:
        offsets.append(offsets[-1] + len(line))

    def span(node: ast.AST) -> tuple[int, int]:
        return (
            offsets[node.lineno - 1] + node.col_offset,
            offsets[node.end_lineno - 1] + node.end_col_offset,
        )

    edits: list[tuple[int, int]] = []
    for cls in ast.parse(text).body:
        if not (isinstance(cls, ast.ClassDef) and cls.name.endswith("Update")):
            continue
        for stmt in cls.body:
            value = getattr(stmt, "value", None)
            if not isinstance(stmt, ast.AnnAssign) or value is None:
                continue
            if isinstance(value, ast.Call):  # field(name=..., default=...)
                value = next(
                    (k.value for k in value.keywords if k.arg == "default"), None
                )
            if value is None or (isinstance(value, ast.Name) and value.id == "UNSET"):
                continue
            edits.append(span(value))
    for start, end in sorted(edits, reverse=True):
        data = data[:start] + b"UNSET" + data[end:]
    return data.decode(), len(edits)


def main(path: Path) -> int:
    text = path.read_text()
    failed = False
    for label, pattern, repl in REWRITES:
        text, n = re.subn(pattern, repl, text)
        print(f"{n:3d}x {label}")
        if n == 0:
            failed = True
    text, n = collapse_empty_string_unions(text)
    print(f"{n:3d}x Url | Url1 (non-empty | empty string) -> str")
    if n == 0:
        failed = True
    text, n = unset_update_defaults(text)
    print(f"{n:3d}x *Update models: spec defaults -> UNSET")
    if n == 0:
        failed = True
    path.write_text(text)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1] if len(sys.argv) > 1 else "gns3client/models.py")))
