set shell := ["bash", "-eu", "-o", "pipefail", "-c"]

_default:
    @just --list --unsorted --list-submodules

[group('dev')]
generate:
  uv run datamodel-codegen --input gns3openapi.json --input-file-type openapi --output gns3client/models.py --output-model-type msgspec.Struct --target-python-version 3.12 --snake-case-field --use-double-quotes --field-constraints --use-standard-primitive-types --output-datetime-class datetime --formatters ruff-check ruff-format --collapse-root-models --naming-strategy parent-prefixed --disable-timestamp

[group('test')]
fmt:
    uv run ruff format .

[group('test')]
lint:
    uv run ruff check .

[group('test')]
test: fmt lint
