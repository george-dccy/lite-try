#!/usr/bin/env python3
"""Validate the local handoff layer for the Notion-led restructure.

Notion content is intentionally not fetched over HTTP here. Live readability is
proved by the Notion MCP caller, which passes the URLs it just fetched through
--notion-ok-url. Without that evidence this script fails closed.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

OWNED_SKILLS = [
    ".agents/skills/relationship-content/SKILL.md",
    ".agents/skills/yuguang-sticker-bridge/SKILL.md",
    ".agents/skills/yuguang-handoff/SKILL.md",
    ".agents/skills/jiejie-illustrations/SKILL.md",
    ".agents/skills/wm-mechanism-explorer/SKILL.md",
    ".agents/skills/wm-research-agent/SKILL.md",
    ".agents/skills/wm-creative-director/SKILL.md",
    ".agents/skills/wm-video-producer/SKILL.md",
    "world-mechanism/skills/wm-mechanism-explorer/SKILL.md",
    "world-mechanism/skills/wm-research-agent/SKILL.md",
    "world-mechanism/skills/wm-creative-director/SKILL.md",
    "world-mechanism/skills/wm-video-producer/SKILL.md",
]

REQUIRED_PATHS = [
    "AGENTS.md",
    "world-mechanism/AGENTS.md",
    "notes/BRAND_POSITIONING.md",
    "notes/NOTION_HANDOFF.md",
    "notes/REPOSITORY_EXECUTION.md",
    "engine/video-kit/README.md",
    "engine/video-kit/run.sh",
    "engine/video-kit/cues.json",
    "engine/video-kit/scene.html",
    "engine/video-kit/render.cjs",
    "engine/video-kit/audio.py",
    "engine/video-kit/master.py",
    "productions/README.md",
    "world-mechanism/renderers/art-motion/README.md",
    "world-mechanism/engine/production-orchestrator/template-production.yaml",
]

AGENT_FILES = ["AGENTS.md", "world-mechanism/AGENTS.md"]

NOTION_URL_RE = re.compile(
    r"(?:https://app\.notion\.com/(?:p|[a-z-]+)/(?:[A-Za-z0-9_-]+)|collection://[A-Za-z0-9-]+)"
)

REQUIRED_NOTION_URLS = {
    "https://app.notion.com/p/3d527110f8d581b3b3c2f53574559f94",
    "https://app.notion.com/p/3f727110f8d5813e9b22dbeff5ebdd9c",
    "https://app.notion.com/p/3d727110f8d5816dbed0f5360d37014b",
    "https://app.notion.com/p/3f727110f8d5812da32dd21d59e30131",
    "https://app.notion.com/p/3f727110f8d581409fc6efb83e348eb0",
    "https://app.notion.com/p/3f627110f8d581918bf3de93e837a339",
    "https://app.notion.com/p/3da27110f8d5819b835ac3154cec5e3a",
    "https://app.notion.com/p/9c7806bb654d4829b5f83bbe85969194",
    "https://app.notion.com/p/604c871889e84c7db58eb58e11d9cd74",
    "https://app.notion.com/p/fea502f01f484cefa0d83d7686ad2b63",
    "collection://2172cbcb-6c94-4836-a266-5601ef730bbe",
    "collection://5049912e-16d6-4754-af52-05622859c116",
    "collection://b10d972d-cdda-4b95-98ab-a6d4354a7439",
}

IGNORED_NOTION_URLS = {
    "https://app.notion.com/p/3f727110f8d5810599c1e0fa6aedc761",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def current_files() -> list[Path]:
    files: list[Path] = [ROOT / "AGENTS.md"]
    files.extend((ROOT / "notes").glob("*.md"))
    files.extend((ROOT / ".agents" / "skills").glob("*/SKILL.md"))
    return [path for path in files if path.exists()]


def instruction_files() -> list[Path]:
    paths = [ROOT / rel for rel in AGENT_FILES]
    paths.extend(ROOT / rel for rel in OWNED_SKILLS)
    return [path for path in paths if path.exists()]


def referenced_local_paths(path: Path) -> set[Path]:
    """Return concrete backtick paths from an instruction file.

    Dynamic examples such as productions/<date-slug> are intentionally skipped;
    concrete paths are checked so a renamed local dependency fails early.
    """

    candidates: set[Path] = set()
    text = read_text(path)
    for token in re.findall(r"`([^`]+)`", text):
        token = token.strip().rstrip(".,;:)")
        if (
            not token
            or token.startswith(("http://", "https://"))
            or "<" in token
            or " " in token
            or "|" in token
            or "→" in token
            or "..." in token
            or token.startswith(("python ", "node ", "sh "))
        ):
            continue
        if not token.startswith((
            ".agents/",
            "engine/",
            "episodes/",
            "notes/",
            "outputs/",
            "productions/",
            "research/",
            "scripts/",
            "world-mechanism/",
            "AGENTS.md",
            "skills-lock.json",
        )):
            continue
        normalized = token.replace("\\", "/").rstrip("/")
        candidates.add(ROOT / normalized)
    return candidates


def notion_urls() -> set[str]:
    urls: set[str] = set()
    for path in current_files():
        urls.update(NOTION_URL_RE.findall(read_text(path)))
    return urls


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--notion-ok-url",
        action="append",
        default=[],
        help="A URL freshly fetched and verified through Notion MCP; repeat per URL.",
    )
    args = parser.parse_args()

    failures: list[str] = []
    for rel in REQUIRED_PATHS + OWNED_SKILLS:
        if not (ROOT / rel).is_file():
            failures.append(f"missing local path: {rel}")

    for path in current_files():
        text = read_text(path)
        if path.name == "SKILL.md" and not text.startswith("---\n"):
            failures.append(f"skill missing front matter: {path.relative_to(ROOT)}")

    for instruction in instruction_files():
        for referenced in referenced_local_paths(instruction):
            if not referenced.exists():
                failures.append(
                    f"missing referenced local path: {referenced.relative_to(ROOT)} "
                    f"(from {instruction.relative_to(ROOT)})"
                )

    expected_urls = (notion_urls() | REQUIRED_NOTION_URLS) - IGNORED_NOTION_URLS
    verified_urls = set(args.notion_ok_url)
    if not args.notion_ok_url:
        failures.append("Notion MCP evidence missing: pass --notion-ok-url for every current URL")
    else:
        for url in sorted(expected_urls - verified_urls):
            failures.append(f"Notion URL was not verified through MCP: {url}")

    for url in sorted(expected_urls):
        if not (
            url.startswith("https://app.notion.com/")
            or url.startswith("collection://")
        ):
            failures.append(f"unexpected Notion URL form: {url}")

    for url in sorted(expected_urls):
        print(f"NOTION {url}: {'OK' if url in verified_urls else 'MISSING_MCP_EVIDENCE'}")

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 1

    print(f"PASS local paths and {len(expected_urls)} Notion URLs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
