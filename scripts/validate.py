#!/usr/bin/env python3
"""Validate YAML records against JSON Schema and catalogue-wide invariants.

Requires: pip install pyyaml jsonschema
"""
import json
from pathlib import Path
import sys
import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schema/format.schema.json").read_text())
REVERSE = {"derived_from": "derived_into", "derived_into": "derived_from"}
errors = []
records = {}

for path in sorted((ROOT / "formats").glob("*.yaml")):
    try:
        # Reject duplicate YAML keys rather than silently overwriting them.
        class UniqueLoader(yaml.SafeLoader):
            pass
        def unique_map(loader, node):
            result = {}
            for key_node, value_node in node.value:
                key = loader.construct_object(key_node)
                if key in result:
                    raise ValueError(f"Duplicate YAML key: {key}")
                result[key] = loader.construct_object(value_node)
            return result
        UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_map)
        record = yaml.load(path.read_text(), Loader=UniqueLoader)
        for err in Draft202012Validator(SCHEMA).iter_errors(record):
            errors.append(f"{path.name}: {err.message}")
        if not isinstance(record, dict) or not isinstance(record.get("id"), int):
            continue
        ident = record["id"]
        if path.stem != f"{ident:04d}":
            errors.append(f"{path.name}: filename does not match ID {ident}")
        if ident in records:
            errors.append(f"{path.name}: duplicate ID {ident}")
        records[ident] = record
    except Exception as exc:
        errors.append(f"{path.name}: {exc}")

for ident, record in records.items():
    for rel in record.get("related_formats", []):
        target = rel["id"]
        if target == ident:
            errors.append(f"{ident}: self-reference")
        if target not in records:
            errors.append(f"{ident}: missing related format {target}")
            continue
        expected = REVERSE.get(rel["relationship"], rel["relationship"])
        if not any(x.get("id") == ident and x.get("relationship") == expected
                   for x in records[target].get("related_formats", [])):
            errors.append(f"{ident}: nonreciprocal relation to {target}")
    successor = record.get("retirement", {}).get("successor_id")
    if successor is not None and successor not in records:
        errors.append(f"{ident}: missing retirement successor {successor}")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"PASS: {len(records)} format records")
