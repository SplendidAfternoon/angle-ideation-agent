#!/usr/bin/env python3
"""Eval harness: compare live runs + fixtures to expected PASS/FAIL.

Catches stub triads (hardcoded critic/red-team) that lexical Ready checks miss
if schemas are skipped. See eval/README.md and eval/llm_ops.md.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.validate_run import parse_angle_pack_sections, validate_run

try:
    import jsonschema
except ImportError:
    jsonschema = None

STUB_EVIDENCE = {
    "scene-level emotional loss",
    "concrete tool/advice pattern",
    "sensory resolution moment",
    "product is mechanism doorway",
    "clear belief shift",
    "distinct psychosocial currencies",
    "4-beat story arcs complete",
    "audited with fresh eye; passes all criteria",
}

GOLD_DIMS = (
    "hollow_specificity",
    "villain_concreteness",
    "dream_render",
    "belief_move",
    "headline_punch",
    "mechanism_honesty",
)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def ops_flags(run_dir: Path) -> List[str]:
    """Hunt collapsed / stubbed triad signatures."""
    flags: List[str] = []
    gr = run_dir / "06_gate_report.json"
    gs = run_dir / "06_gold_scores.json"
    adv = run_dir / "07_adversary.json"
    pack = run_dir / "05_angle_pack.md"
    trace = run_dir / "09_llm_trace.json"

    status_ready = False
    if pack.is_file():
        text = pack.read_text(encoding="utf-8")
        status_ready = "Ready for Pre-Lander Agent" in text

    if gr.is_file():
        data = load_json(gr)
        gates = data.get("gates")
        if isinstance(gates, dict):
            flags.append("OPS-STUB-GATES")
        elif isinstance(gates, list):
            stub_hits = 0
            empty_ev = 0
            for g in gates:
                ev = str(g.get("evidence") or "").strip().lower()
                if not ev:
                    empty_ev += 1
                if ev in STUB_EVIDENCE:
                    stub_hits += 1
            if stub_hits >= 3:
                flags.append("OPS-STUB-GATES")
            if empty_ev and status_ready:
                flags.append("OPS-EMPTY-EVIDENCE")
            if "pack_status_recommendation" not in data:
                flags.append("OPS-STUB-GATES")
        else:
            flags.append("OPS-STUB-GATES")
        cr = data.get("cold_reread") or {}
        notes = str(cr.get("notes") or "").strip().lower()
        if notes in STUB_EVIDENCE:
            flags.append("OPS-STUB-GATES")

    if gs.is_file():
        data = load_json(gs)
        angles = data.get("angles") or []
        missing_dims = False
        if not angles:
            missing_dims = True
        for a in angles:
            if any(k not in a for k in GOLD_DIMS):
                missing_dims = True
                break
            if "critic" not in data and "methodology" not in data:
                missing_dims = True
        if missing_dims:
            flags.append("OPS-STUB-GOLD")
        if jsonschema:
            schema = json.loads(
                (REPO_ROOT / "schemas/gold_scores.schema.json").read_text(encoding="utf-8")
            )
            try:
                jsonschema.validate(instance=data, schema=schema)
            except jsonschema.ValidationError:
                if "OPS-STUB-GOLD" not in flags:
                    flags.append("OPS-STUB-GOLD")

    if adv.is_file():
        data = load_json(adv)
        if "nits" not in data and "minor_notes" in data:
            flags.append("OPS-STUB-ADVERSARY")
        if "recommendation" not in data and data.get("result") == "NO_MATERIAL_HITS":
            flags.append("OPS-STUB-ADVERSARY")
        if jsonschema:
            schema = json.loads(
                (REPO_ROOT / "schemas/adversary.schema.json").read_text(encoding="utf-8")
            )
            try:
                jsonschema.validate(instance=data, schema=schema)
            except jsonschema.ValidationError:
                if "OPS-STUB-ADVERSARY" not in flags:
                    flags.append("OPS-STUB-ADVERSARY")
        if status_ready and pack.is_file():
            pack_l = pack.read_text(encoding="utf-8").lower()
            f01ish = "hospital-grade" in pack_l or "20% off" in pack_l or "game-changer" in pack_l
            if f01ish and not data.get("material_hits"):
                flags.append("OPS-STUB-ADVERSARY")

    if status_ready and not trace.is_file() and (run_dir / "00_route.json").is_file():
        route = load_json(run_dir / "00_route.json")
        if route.get("decision", "").startswith("Eval fixture") or "auto" in str(
            route.get("run_id", "")
        ):
            flags.append("OPS-NO-TRACE")

    if trace.is_file() and jsonschema:
        schema = json.loads(
            (REPO_ROOT / "schemas/llm_trace.schema.json").read_text(encoding="utf-8")
        )
        tdata = load_json(trace)
        try:
            jsonschema.validate(instance=tdata, schema=schema)
        except jsonschema.ValidationError:
            flags.append("OPS-BAD-TRACE")
        if tdata.get("collapsed_roles") is True:
            flags.append("OPS-COLLAPSED-ROLES")
        if tdata.get("ready_stamped_by") == "pipeline_default":
            flags.append("OPS-READY-DEFAULT")

    return sorted(set(flags))


ARRIVAL_MARKERS = (
    "it was over",
    "nights were normal",
    "finally slept through",
    "she finally slept through",
    "problem gone",
    "life was normal again",
)

HOOK_CLUSTER_RE = re.compile(
    r"\*\*Hook Cluster:\*\*\s*(.+?)(?=\n\s*\*\*|\Z)", re.S | re.I
)


def vsl_flags(run_dir: Path) -> List[str]:
    """Cheap lexical hunts for docs/04 F16–F18 (VSL doctrine)."""
    pack = run_dir / "05_angle_pack.md"
    if not pack.is_file():
        return []
    text = pack.read_text(encoding="utf-8")
    flags: List[str] = []
    for angle in parse_angle_pack_sections(text):
        dream = (angle.get("dream") or "").lower()
        if any(m in dream for m in ARRIVAL_MARKERS):
            flags.append("F16-ARRIVAL")
        arc = (angle.get("story_arc") or "").lower()
        if "tried the cup" in arc and "slept" in arc:
            flags.append("F17-MECH-ACTION")
        elif "mucus visible" in arc and "slept" in arc and "fail" not in arc:
            flags.append("F17-MECH-ACTION")
    for match in HOOK_CLUSTER_RE.finditer(text):
        cluster = match.group(1).lower()
        has_offer = "20% off" in cluster or "20 percent off" in cluster
        has_911 = "911" in cluster
        has_mould = "mould" in cluster or "mold" in cluster
        if has_offer or (has_911 and has_mould):
            flags.append("F18-HOOK-CLUSTER")
    return sorted(set(flags))


def evaluate_case(case: Dict[str, Any], repo_root: Path) -> Dict[str, Any]:
    run_dir = repo_root / case["run_dir"]
    product = case.get("product")
    ok, errors = validate_run(
        run_dir=run_dir, repo_root=repo_root, product_name=product, verbose=False
    )
    flags = sorted(set(ops_flags(run_dir) + vsl_flags(run_dir)))
    actual = "PASS" if (ok and not flags) else "FAIL"
    expected = case["expect"]
    missing_must = []
    for flag in case.get("must_flag") or []:
        if flag not in flags:
            missing_must.append(flag)
    matched = actual == expected and not missing_must
    return {
        "id": case["id"],
        "expected": expected,
        "actual": actual,
        "validate_ok": ok,
        "validate_errors": errors[:12],
        "ops_flags": flags,
        "missing_must_flag": missing_must,
        "matched": matched,
        "kind": case["kind"],
    }


def run_harness(case_id: str | None = None) -> Tuple[bool, List[Dict[str, Any]]]:
    manifest_path = REPO_ROOT / "eval/cases/manifest.json"
    manifest = load_json(manifest_path)
    if jsonschema:
        schema = load_json(REPO_ROOT / "schemas/eval_case.schema.json")
        jsonschema.validate(instance=manifest, schema=schema)
    cases = manifest["cases"]
    if case_id:
        cases = [c for c in cases if c["id"] == case_id]
        if not cases:
            raise SystemExit(f"Unknown case id: {case_id}")
    results = [evaluate_case(c, REPO_ROOT) for c in cases]
    return all(r["matched"] for r in results), results


def main() -> int:
    parser = argparse.ArgumentParser(description="Angle Ideation eval harness")
    parser.add_argument("--case", default=None, help="Run a single case id")
    parser.add_argument("--json", action="store_true", help="Print JSON results")
    args = parser.parse_args()
    ok, results = run_harness(args.case)
    if args.json:
        print(json.dumps({"ok": ok, "results": results}, indent=2))
        return 0 if ok else 1
    print("=== Eval harness ===")
    for r in results:
        mark = "PASS" if r["matched"] else "MISS"
        print(
            f"[{mark}] {r['id']}  expect={r['expected']} actual={r['actual']}  "
            f"kind={r['kind']}"
        )
        if r["ops_flags"]:
            print(f"       ops_flags={r['ops_flags']}")
        if r["missing_must_flag"]:
            print(f"       missing_must_flag={r['missing_must_flag']}")
        if not r["matched"] and r["validate_errors"] and r["expected"] == "PASS":
            for e in r["validate_errors"][:6]:
                print(f"       {e}")
    print()
    print("RESULT: ALL CASES MATCHED" if ok else "RESULT: CASE MISMATCH")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
