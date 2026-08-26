#!/usr/bin/env python3
"""Validate headlines in an Angle Pack markdown file (H1/H4/H5 assist)."""

from __future__ import annotations

import argparse
import re
import sys

H5_PREFIXES = (
    "at ",
    "for weeks",
    "for months",
    "for days",
    "when i",
    "after i",
    "before i",
    "one night",
    "last night",
    "today,",
    "tonight,",
    "suddenly,",
    "finally,",
)

AD_ESE = {
    "game-changer",
    "hack",
    "must-have",
    "literally obsessed",
    "link in bio",
    "hospital-grade",
    "miracle",
    "secret trick",
    "order now",
}


def extract_headlines(text: str) -> list[str]:
    headlines: list[str] = []
    for line in text.splitlines():
        m = re.match(r"\*\*Headline:\*\*\s*\*?(.+?)\*?\s*$", line.strip())
        if m:
            h = m.group(1).strip().strip("*").strip()
            headlines.append(h)
    return headlines


def word_count(headline: str) -> int:
    return len([t for t in re.split(r"\s+", headline.strip()) if t])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pack_md", help="Path to 05_angle_pack.md")
    parser.add_argument("--product", default="", help="Product/brand name to ban in headlines")
    args = parser.parse_args()

    text = open(args.pack_md, encoding="utf-8").read()
    headlines = extract_headlines(text)
    if not headlines:
        print("FAIL: no headlines found (expected **Headline:** lines)")
        return 1

    failed = 0
    product = args.product.strip().lower()
    for i, h in enumerate(headlines, 1):
        problems: list[str] = []
        wc = word_count(h)
        if wc > 12:
            problems.append(f"H1 word_count={wc}>12")
        low = h.lower()
        if product and product in low:
            problems.append("H4 product token present")
        if any(low.startswith(p) for p in H5_PREFIXES):
            problems.append("H5 preamble opening")
        for ban in AD_ESE:
            if ban in low:
                problems.append(f"H6 ad-ese:{ban}")
                break
        if problems:
            failed += 1
            print(f"FAIL angle@{i}: {h}")
            for p in problems:
                print(f"  - {p}")
        else:
            print(f"PASS angle@{i} words={wc}: {h}")

    if failed:
        print(f"RESULT: {failed}/{len(headlines)} failed")
        return 1
    print(f"RESULT: {len(headlines)}/{len(headlines)} passed assist checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
