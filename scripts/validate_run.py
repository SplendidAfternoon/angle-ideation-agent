#!/usr/bin/env python3
"""Unified Validation Runner for Angle Ideation Agent runs.

Validates:
1. Presence of required run artifacts.
2. JSON Schema conformance of all JSON artifacts against Draft 2020-12 schemas.
3. Structural and lexical rules of 05_angle_pack.md (H1–H6, A-DOOR, Hollow/Dream overlap, Currency uniqueness).
4. Agentic Triad Ready predicates (docs/13) if pack Status is Ready.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

try:
    import jsonschema
except ImportError:
    jsonschema = None

# Banned headline prefixes (case-insensitive)
H5_PREFIXES = (
    "at ",
    "at 3",
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

# Ad-ese banned phrases (case-insensitive whole-word / phrase)
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

SCHEMA_MAPPING = {
    "01_angle_fuel.json": "schemas/angle_fuel.schema.json",
    "06_chain_judge.json": "schemas/chain_judge.schema.json",
    "06_gate_report.json": "schemas/gate_report.schema.json",
    "06_gold_scores.json": "schemas/gold_scores.schema.json",
    "07_adversary.json": "schemas/adversary.schema.json",
}

ALLOWED_CURRENCIES = {
    "RELATIONAL_EQUITY",
    "IDENTITY_SELFHOOD",
    "SAFETY_SECURITY",
    "TRUST_SAFETY",
    "SOCIAL_STATUS",
    "AGENCY_CONTROL",
    "GUILT_REGRET",
    "BODILY_AUTONOMY",
    "GENTLENESS",
    "AUTHORITY",
    "FUTURE_SECURITY",
    "AGENCY_PARTNERSHIP",
}

# Regex patterns
BIAS_ID_RE = re.compile(r"\bBIAS_[A-Z0-9_]+\b")
ANGLE_HEADER_RE = re.compile(r"^###\s+(\d+)\.\s+The\s+(.+?)\s+Angle", re.M)


def tokenize_words(text: str) -> List[str]:
    return [t for t in re.split(r"\s+", text.strip()) if t]


def tokenize_words_clean(text: str) -> Set[str]:
    words = re.findall(r"\b[a-zA-Z]{3,}\b", text.lower())
    return set(words)


def jaccard_similarity(set_a: Set[str], set_b: Set[str]) -> float:
    if not set_a or not set_b:
        return 0.0
    intersection = len(set_a.intersection(set_b))
    union = len(set_a.union(set_b))
    return intersection / union if union > 0 else 0.0


def load_schema(schema_rel_path: str, repo_root: Path) -> Optional[Dict[str, Any]]:
    schema_path = repo_root / schema_rel_path
    if not schema_path.is_file():
        return None
    with open(schema_path, "r", encoding="utf-8") as f:
        return json.load(f)


def parse_angle_pack_sections(text: str) -> List[Dict[str, Any]]:
    """Parse each angle block from markdown text."""
    angles: List[Dict[str, Any]] = []
    blocks = re.split(r"^###\s+\d+\.\s+", text, flags=re.M)
    # The first block is header material before angle 1
    for block in blocks[1:]:
        angle: Dict[str, Any] = {}
        lines = block.strip().splitlines()
        if not lines:
            continue
        angle["title_line"] = lines[0].strip()

        # Extract fields with regex
        fields = [
            ("currency", r"\*\*Psychosocial Currency:\*\*\s*(.+)$"),
            ("core_idea", r"\*\*Core Idea:\*\*\s*(.+)$"),
            ("headline", r"\*\*Headline:\*\*\s*\*?(.+?)\*?\s*$"),
            ("hollow", r"\*\*The Hollow:\*\*\s*(.+?)(?=\n\s*\*\*|\Z)"),
            ("villain", r"\*\*The Villain:\*\*\s*(.+?)(?=\n\s*\*\*|\Z)"),
            ("dream", r"\*\*The Dream:\*\*\s*(.+?)(?=\n\s*\*\*|\Z)"),
            ("story_arc", r"\*\*Story Arc:\*\*\s*(.+?)(?=\n\s*\*\*|\Z)"),
            ("product_fit", r"\*\*Product Fit:\*\*\s*(.+?)(?=\n\s*\*\*|\Z)"),
            ("awareness_stage", r"\*\*Awareness stage:\*\*\s*(.+)$"),
            ("test_priority", r"\*\*Test priority:\*\*\s*(\d+)"),
        ]

        for key, pat in fields:
            m = re.search(pat, block, flags=re.M | re.S)
            if m:
                val = m.group(1).strip().strip("*").strip()
                # Clean multi-line whitespace
                val = re.sub(r"\s+", " ", val)
                angle[key] = val
            else:
                angle[key] = ""

        angles.append(angle)
    return angles


def validate_run(
    run_dir: Path,
    repo_root: Optional[Path] = None,
    product_name: Optional[str] = None,
    verbose: bool = True,
) -> Tuple[bool, List[str]]:
    errors: List[str] = []
    notes: List[str] = []

    if repo_root is None:
        # Resolve repo root from this script's location or run_dir
        repo_root = Path(__file__).resolve().parent.parent

    if not run_dir.is_dir():
        return False, [f"Run directory does not exist: {run_dir}"]

    # 1. Artifacts check
    for art in REQUIRED_ARTIFACTS:
        p = run_dir / art
        if not p.is_file():
            errors.append(f"Missing required artifact: {art}")
        else:
            notes.append(f"Found artifact: {art}")

    # 2. JSON Schema Validation
    if jsonschema:
        for fname, schema_rel in SCHEMA_MAPPING.items():
            fpath = run_dir / fname
            if fpath.is_file():
                schema = load_schema(schema_rel, repo_root)
                if schema:
                    try:
                        with open(fpath, "r", encoding="utf-8") as f:
                            data = json.load(f)
                        jsonschema.validate(instance=data, schema=schema)
                        notes.append(f"Schema PASS: {fname} matches {schema_rel}")
                    except jsonschema.ValidationError as ve:
                        errors.append(f"Schema FAIL: {fname} -> {ve.message} (path: {list(ve.path)})")
                    except json.JSONDecodeError as je:
                        errors.append(f"JSON invalid: {fname} -> {je}")
                else:
                    errors.append(f"Schema file not found: {schema_rel}")
    else:
        notes.append("jsonschema not installed; skipping deep schema validation")

    # 3. AngleFuel check
    fuel_path = run_dir / "01_angle_fuel.json"
    detected_product = product_name
    if fuel_path.is_file():
        try:
            with open(fuel_path, "r", encoding="utf-8") as f:
                fuel_data = json.load(f)
            if not detected_product:
                detected_product = fuel_data.get("meta", {}).get("product_name", "")
            mech = (
                fuel_data.get("product_fit", {}).get("mechanism")
                or fuel_data.get("product_fit", {}).get("mechanism_label")
            )
            labels = fuel_data.get("product_fit", {}).get("labels") or {}
            if labels.get("mechanism") == "UNKNOWN" or mech == "UNKNOWN":
                errors.append("AngleFuel product_fit.mechanism is UNKNOWN")
        except Exception as e:
            errors.append(f"Failed parsing fuel JSON: {e}")

    # 4. Angle Pack Markdown Validation
    pack_path = run_dir / "05_angle_pack.md"
    if pack_path.is_file():
        pack_text = pack_path.read_text(encoding="utf-8")

        # Sections check
        for sec in REQUIRED_SECTIONS:
            if sec not in pack_text:
                errors.append(f"Missing required markdown section: {sec}")

        # Status check
        status_m = re.search(r"\*\*Status:\*\*\s*(.+)$", pack_text, re.M)
        pack_status = status_m.group(1).strip() if status_m else "UNKNOWN"

        # Angles extraction
        angles = parse_angle_pack_sections(pack_text)
        angle_count = len(angles)

        if angle_count < 6 or angle_count > 8:
            if "Blocked" in pack_status:
                notes.append(f"Angle count {angle_count} with Blocked status accepted")
            else:
                errors.append(f"Angle count={angle_count} not in allowed range [6, 8]")

        # Unique currencies
        currencies = [a["currency"] for a in angles if a["currency"]]
        if len(currencies) != len(set(c.lower() for c in currencies)):
            errors.append(f"Duplicate psychosocial currencies found: {currencies}")

        for i, a in enumerate(angles, 1):
            h = a["headline"]
            core = a["core_idea"]
            hollow = a["hollow"]
            dream = a["dream"]
            villain = a["villain"]
            curr = a["currency"]

            # Check headline length H1
            words = tokenize_words(h)
            if len(words) > 12:
                errors.append(f"Angle {i} H1 fail: headline word count {len(words)} > 12 ({h})")

            # Check headline product name H4
            if detected_product and detected_product.strip().lower() in h.lower():
                errors.append(f"Angle {i} H4 fail: product '{detected_product}' found in headline: {h}")

            # Check headline preamble H5
            low_h = h.lower()
            if any(low_h.startswith(p) for p in H5_PREFIXES):
                errors.append(f"Angle {i} H5 fail: preamble opening in headline: {h}")

            # Check headline ad-ese H6
            for ban in AD_ESE:
                if ban in low_h:
                    errors.append(f"Angle {i} H6 fail: ad-ese term '{ban}' in headline: {h}")

            # Check Core Idea bias tokens
            if BIAS_ID_RE.search(core):
                errors.append(f"Angle {i} A-CORE fail: Core Idea contains bias ID ({core})")
            if re.search(r"\bwe use\b.*\bbias\b", core, re.I):
                errors.append(f"Angle {i} A-CORE fail: Core Idea uses bias as thesis ({core})")

            # Check Hollow vs Dream overlap
            hollow_words = tokenize_words_clean(hollow)
            dream_words = tokenize_words_clean(dream)
            overlap = jaccard_similarity(hollow_words, dream_words)
            if overlap > 0.60:
                errors.append(f"Angle {i} Hollow/Dream overlap {overlap:.2f} > 0.60 (hollow and dream too similar)")

            # Check A-DOOR (product name in Dream emotional climax)
            if detected_product:
                prod_clean = detected_product.strip().lower()
                if prod_clean and prod_clean in dream.lower():
                    errors.append(f"Angle {i} A-DOOR warning/fail: product name '{detected_product}' in Dream text: {dream}")

        # 5. Triad Ready Predicate Checks (docs/13)
        if "Ready" in pack_status:
            # Check 06_chain_judge.json
            cj_path = run_dir / "06_chain_judge.json"
            if not cj_path.is_file():
                errors.append("Status is Ready but 06_chain_judge.json is missing")
            else:
                try:
                    cj_data = json.loads(cj_path.read_text(encoding="utf-8"))
                    if cj_data.get("result") != "PASS":
                        errors.append(f"Status is Ready but 06_chain_judge.json result is {cj_data.get('result')}")
                except Exception as e:
                    errors.append(f"Error reading 06_chain_judge.json: {e}")

            # Check 06_gate_report.json
            gr_path = run_dir / "06_gate_report.json"
            if not gr_path.is_file():
                errors.append("Status is Ready but 06_gate_report.json is missing")
            else:
                try:
                    gr_data = json.loads(gr_path.read_text(encoding="utf-8"))
                    if gr_data.get("pack_status_recommendation") != "Ready for Pre-Lander Agent":
                        errors.append(f"Status is Ready but gate report recommendation is {gr_data.get('pack_status_recommendation')}")
                    gates = gr_data.get("gates", [])
                    failed_gates = [g.get("gate_id") for g in gates if g.get("result") == "FAIL"]
                    if failed_gates:
                        errors.append(f"Status is Ready but gate report contains failed gates: {failed_gates}")
                except Exception as e:
                    errors.append(f"Error reading 06_gate_report.json: {e}")

            # Check 06_gold_scores.json
            gs_path = run_dir / "06_gold_scores.json"
            if not gs_path.is_file():
                errors.append("Status is Ready but 06_gold_scores.json is missing")
            else:
                try:
                    gs_data = json.loads(gs_path.read_text(encoding="utf-8"))
                    if not gs_data.get("pack_pass"):
                        errors.append("Status is Ready but 06_gold_scores.json pack_pass is false")
                    if gs_data.get("pack_mean", 0) < 4.0:
                        errors.append(f"Status is Ready but gold score pack_mean {gs_data.get('pack_mean')} < 4.0")
                except Exception as e:
                    errors.append(f"Error reading 06_gold_scores.json: {e}")

            # Check 07_adversary.json
            adv_path = run_dir / "07_adversary.json"
            if not adv_path.is_file():
                errors.append("Status is Ready but 07_adversary.json is missing")
            else:
                try:
                    adv_data = json.loads(adv_path.read_text(encoding="utf-8"))
                    hits = adv_data.get("material_hits", [])
                    if hits:
                        errors.append(f"Status is Ready but 07_adversary.json has {len(hits)} material hits (recommendation={adv_data.get('recommendation')})")
                    if adv_data.get("recommendation") != "NO_MATERIAL_HITS":
                        errors.append(f"Status is Ready but adversary recommendation is {adv_data.get('recommendation')}")
                except Exception as e:
                    errors.append(f"Error reading 07_adversary.json: {e}")

    if verbose:
        for n in notes:
            print(f"  [PASS] {n}")
        for e in errors:
            print(f"  [FAIL] {e}")

    success = len(errors) == 0
    return success, errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an Angle Ideation run folder")
    parser.add_argument("run_dir", help="Path to runs/<slug>/ directory")
    parser.add_argument("--product", default=None, help="Product brand name to ban in headlines")
    parser.add_argument("--quiet", action="store_true", help="Suppress passing logs")
    args = parser.parse_args()

    run_path = Path(args.run_dir)
    print(f"=== Validating Run: {run_path.name} ===")
    success, errors = validate_run(
        run_dir=run_path,
        product_name=args.product,
        verbose=not args.quiet,
    )

    if success:
        print(f"\nRESULT: ALL CHECKS PASSED for {run_path.name}")
        return 0
    else:
        print(f"\nRESULT: {len(errors)} FAILURES for {run_path.name}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
