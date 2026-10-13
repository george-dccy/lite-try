#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "creative-blueprint.schema.json"
BLUEPRINT_DIR = ROOT / "examples" / "blueprints"


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)

    paths = sorted(BLUEPRINT_DIR.glob("*.yaml"))
    if not paths:
        print("No blueprint examples found.", file=sys.stderr)
        return 1

    failed = False
    seen_ids: set[str] = set()

    for path in paths:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))

        blueprint_id = data.get("id") if isinstance(data, dict) else None
        if blueprint_id in seen_ids:
            errors.append(ValueError(f"duplicate blueprint id: {blueprint_id}"))
        elif blueprint_id:
            seen_ids.add(blueprint_id)

        if errors:
            failed = True
            print(f"FAIL {path.relative_to(ROOT)}")
            for error in errors:
                if hasattr(error, "path"):
                    location = ".".join(str(x) for x in error.path) or "<root>"
                    message = error.message
                else:
                    location = "<root>"
                    message = str(error)
                print(f"  - {location}: {message}")
        else:
            print(f"PASS {path.relative_to(ROOT)}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
