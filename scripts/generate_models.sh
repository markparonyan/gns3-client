#!/usr/bin/env sh
# Regenerate gns3client/models.py from gns3openapi.json, then check it.
set -eu
cd "$(dirname "$0")/.."

uvx --from "datamodel-code-generator[black,isort]==0.83.0" datamodel-codegen \
    --input gns3openapi.json \
    --input-file-type openapi \
    --output gns3client/models.py \
    --output-model-type msgspec.Struct \
    --target-python-version 3.12 \
    --snake-case-field \
    --use-double-quotes \
    --field-constraints \
    --use-standard-primitive-types \
    --output-datetime-class datetime \
    --formatters black isort \
    --collapse-root-models \
    --naming-strategy parent-prefixed \
    --disable-timestamp

uv run python scripts/postprocess_models.py gns3client/models.py
uvx -p 3.12 black -q gns3client/models.py
uv run python scripts/check_models.py gns3openapi.json gns3client/models.py
