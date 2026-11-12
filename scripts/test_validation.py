#!/usr/bin/env python3
"""Smoke-test rejection of malformed records and invalid relationships."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

root = Path(__file__).resolve().parents[1]
schema = json.loads((root / "schema/format.schema.json").read_text())
assert schema["required"] == ["id", "name", "status"]

def check(files, expect_success):
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        (base / "formats").mkdir()
        (base / "schema").mkdir()
        (base / "scripts").mkdir()
        shutil.copy(root / "schema/format.schema.json", base / "schema/format.schema.json")
        shutil.copy(root / "scripts/validate.py", base / "scripts/validate.py")
        for name, content in files.items():
            (base / "formats" / name).write_text(content)
        result = subprocess.run([sys.executable, str(base / "scripts/validate.py")],
                                capture_output=True, text=True)
        assert (result.returncode == 0) == expect_success, (
            result.stdout + result.stderr)

base = 'id: 1\nname: Test\nstatus: provisional\n'
check({"0001.yaml": base}, True)
check({"0001.yaml": base + "id: 2\n"}, False)  # duplicate YAML key
check({"0002.yaml": base}, False)                 # filename mismatch
check({"0001.yaml": base + "related_formats:\n  - id: 2\n    relationship: variant\n"}, False)
check({"0001.yaml": base + "related_formats:\n  - id: 2\n    relationship: variant\n",
       "0002.yaml": 'id: 2\nname: Other\nstatus: provisional\n'}, False)
check({"0001.yaml": base + "related_formats:\n  - id: 2\n    relationship: derived_from\n",
       "0002.yaml": 'id: 2\nname: Other\nstatus: provisional\nrelated_formats:\n  - id: 1\n    relationship: derived_into\n'}, True)
check({"0001.yaml": 'id: 1\nname: Retired\nstatus: retired\n'}, False)
print("PASS: validator negative tests")
