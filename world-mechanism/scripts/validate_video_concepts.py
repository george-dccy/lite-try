#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "video-concept.schema.json"
CONCEPT_DIR = ROOT / "examples" / "video-concepts"

def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    paths = sorted(CONCEPT_DIR.glob("*.yaml"))
    if not paths:
        print("No video concept examples found.", file=sys.stderr)
        return 1

    failed = False
    for path in paths:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
        if errors:
            failed = True
            print(f"FAIL {path.relative_to(ROOT)}")
            for error in errors:
                location = ".".join(str(x) for x in error.path) or "<root>"
                print(f"  - {location}: {error.message}")
        else:
            print(f"PASS {path.relative_to(ROOT)}")

    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
