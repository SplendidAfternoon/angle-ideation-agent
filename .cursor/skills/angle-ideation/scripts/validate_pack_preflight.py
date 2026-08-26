#!/usr/bin/env python3
"""Lexical / skeleton preflight for an Angle Ideation run folder.

Does NOT judge Hollow/Dream/Villain quality — that is the critic skill.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Add repo root to path to allow importing unified validator if present
repo_root = Path(__file__).resolve().parent.parent.parent.parent
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

try:
    from scripts.validate_run import validate_run
except ImportError:
    validate_run = None

REQUIRED_SECTIONS = (
    "## Headline Rules Applied",
    "## Angle Component Definitions",
    "## Angles",
    "## Summary Table",
)

REQUIRED_ARTIFACTS = (
    "00_route.json",
    "01_angle_fuel.json",
    "02_candidates.json",
    "03_filter_score_log.json",
    "04_reasoning_chains.json",
    "05_angle_pack.md",
)

BIAS_ID_RE = re.compile(r"\bBIAS_[A-Z0-9_]+\b")
ANGLE_HEADER_RE = re.compile(r"^###\s+\d+\.\s+", re.M)
CORE_IDEA_RE = re.compile(r"\*\*Core Idea:\*\*\s*(.+)$", re.M)
CURRENCY_RE = re.compile(r"\*\*Psychosocial Currency:\*\*\s*(.+)$", re.M)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dir", help="Path to runs/<slug>/")
    parser.add_argument("--product", default=None, help="Product brand name")
    args = parser.parse_args()
    run = Path(args.run_dir)
    if not run.is_dir():
        print(f"FAIL: not a directory: {run}")
        return 1

    if validate_run:
        success, errors = validate_run(run_dir=run, repo_root=repo_root, product_name=args.product, verbose=True)
        if success:
            print("RESULT: preflight PASS (lexical/skeleton only - critic still required)")
            return 0
        else:
            print(f"RESULT: {len(errors)} preflight failure(s)")
            return 1

    # Fallback standalone if imported without repo context
    failed = 0
    for name in REQUIRED_ARTIFACTS:
        p = run / name
        if not p.is_file():
            print(f"FAIL: missing artifact {name}")
            failed += 1
        else:
            print(f"PASS: artifact {name}")

    pack_path = run / "05_angle_pack.md"
    if not pack_path.is_file():
        print("RESULT: blocked (no pack)")
        return 1

    text = pack_path.read_text(encoding="utf-8")
    for sec in REQUIRED_SECTIONS:
        if sec not in text:
            print(f"FAIL: missing section {sec}")
            failed += 1
        else:
            print(f"PASS: section {sec}")

    angle_count = len(ANGLE_HEADER_RE.findall(text))
    if angle_count < 6 or angle_count > 8:
        if "**Status:** Blocked" in text or "Status:** Blocked" in text:
            print(f"PASS: angle_count={angle_count} with Status Blocked")
        else:
            print(f"FAIL: angle_count={angle_count} not in 6–8")
            failed += 1
    else:
        print(f"PASS: angle_count={angle_count}")

    currencies = [m.group(1).strip() for m in CURRENCY_RE.finditer(text)]
    if len(currencies) != angle_count and angle_count > 0:
        print(f"FAIL: currency lines={len(currencies)} != angle_count={angle_count}")
        failed += 1
    if len(currencies) != len(set(c.lower() for c in currencies)):
        print("FAIL: duplicate psychosocial currency labels")
        failed += 1
    else:
        if currencies:
            print(f"PASS: unique currencies={len(currencies)}")

    if failed:
        print(f"RESULT: {failed} preflight failure(s)")
        return 1
    print("RESULT: preflight PASS (lexical/skeleton only - critic still required)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
