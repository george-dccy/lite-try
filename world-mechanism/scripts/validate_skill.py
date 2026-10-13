#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKILLS = {
    "wm-mechanism-explorer": {
        "required": [
            "references/question-ladder.md",
            "references/mechanism-map-template.md",
            "references/counterfactual-protocol.md",
            "references/output-contract.md",
            "tests/evals.md",
        ],
        "must_contain": [
            "F — Fact",
            "R — Fictional Rule",
            "Stop before production",
            "Operationalize ambiguous concepts",
        ],
    },
    "wm-research-agent": {
        "required": [
            "references/source-hierarchy.md",
            "references/claim-ledger.md",
            "references/two-pass-workflow.md",
            "tests/evals.md",
        ],
        "must_contain": [
            "Pass A — Premise Check",
            "Pass B — Evidence Pack",
            "Do Not Strengthen",
            "F — Fact",
            "R — Fictional Rule",
        ],
    },
    "wm-creative-director": {
        "required": [
            "references/candidate-template.md",
            "tests/evals.md",
        ],
        "must_contain": [
            "China-first, World-second",
            "First Association Test",
            "Cognitive Surprise",
            "Wish Fulfillment Stress Test",
            "Audience Distance Test",
            "Form Fit Test",
            "Author Fit Test",
        ],
    },
    "wm-video-producer": {
        "required": [
            "references/production-continuation.md",
            "tests/evals.md",
        ],
        "must_contain": [
            "Codex-first",
            "The correct number of styles is 1..N",
            "Do not make a provider such as MiniMax H3 the default full-film renderer",
            "Resume protocol",
            "Production Manifest",
        ],
    },
}

def validate(name: str, spec: dict) -> list[str]:
    skill_dir = ROOT / "skills" / name
    skill_file = skill_dir / "SKILL.md"
    problems: list[str] = []
    if not skill_file.exists():
        return [f"missing {skill_file.relative_to(ROOT)}"]
    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        problems.append("SKILL.md must start with YAML front matter")
    front = text.split("---", 2)[1] if text.count("---") >= 2 else ""
    if not re.search(rf"(?m)^name:\s*{re.escape(name)}\s*$", front):
        problems.append(f"front matter name must be {name}")
    if not re.search(r"(?m)^description:\s*.+$", front):
        problems.append("front matter must contain a description")
    for rel in spec["required"]:
        path = skill_dir / rel
        if not path.exists():
            problems.append(f"missing skill file: {path.relative_to(ROOT)}")
    for phrase in spec["must_contain"]:
        if phrase not in text:
            problems.append(f"SKILL.md must preserve phrase/contract: {phrase}")
    return problems

def main() -> int:
    failed = False
    for name, spec in SKILLS.items():
        problems = validate(name, spec)
        if problems:
            failed = True
            print(f"FAIL skills/{name}")
            for problem in problems:
                print(f"  - {problem}")
        else:
            print(f"PASS skills/{name}")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
