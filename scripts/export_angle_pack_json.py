#!/usr/bin/env python3
"""Export Angle Pack Markdown (05_angle_pack.md) to validated JSON matching schemas/angle_pack.schema.json.

Usage:
  python scripts/export_angle_pack_json.py runs/20260814-bb-benchmark/05_angle_pack.md
  python scripts/export_angle_pack_json.py runs/20260814-bb-benchmark/05_angle_pack.md -o runs/20260814-bb-benchmark/05_angle_pack.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import jsonschema
except ImportError:
    jsonschema = None

CURRENCY_MAP = {
    "relational equity": "RELATIONAL_EQUITY",
    "relational_equity": "RELATIONAL_EQUITY",
    "identity / selfhood": "IDENTITY_SELFHOOD",
    "identity/selfhood": "IDENTITY_SELFHOOD",
    "identity_selfhood": "IDENTITY_SELFHOOD",
    "identity": "IDENTITY_SELFHOOD",
    "safety / security": "SAFETY_SECURITY",
    "safety/security": "SAFETY_SECURITY",
    "safety_security": "SAFETY_SECURITY",
    "safety": "SAFETY_SECURITY",
    "trust / safety": "TRUST_SAFETY",
    "trust/safety": "TRUST_SAFETY",
    "trust_safety": "TRUST_SAFETY",
    "trust": "TRUST_SAFETY",
    "social status / competence": "SOCIAL_STATUS",
    "social status": "SOCIAL_STATUS",
    "social_status": "SOCIAL_STATUS",
    "agency / control": "AGENCY_CONTROL",
    "agency/control": "AGENCY_CONTROL",
    "agency_control": "AGENCY_CONTROL",
    "guilt / regret": "GUILT_REGRET",
    "guilt/regret": "GUILT_REGRET",
    "guilt_regret": "GUILT_REGRET",
    "guilt": "GUILT_REGRET",
    "bodily autonomy": "BODILY_AUTONOMY",
    "bodily_autonomy": "BODILY_AUTONOMY",
    "gentleness": "GENTLENESS",
    "authority": "AUTHORITY",
    "future security": "FUTURE_SECURITY",
    "future_security": "FUTURE_SECURITY",
    "agency / partnership": "AGENCY_PARTNERSHIP",
    "agency/partnership": "AGENCY_PARTNERSHIP",
    "agency_partnership": "AGENCY_PARTNERSHIP",
}


def normalize_currency(curr_text: str) -> str:
    raw = curr_text.strip().strip("*").strip()
    # Check if direct ID
    upper = raw.upper().replace("-", "_").replace(" ", "_")
    if upper in CURRENCY_MAP.values():
        return upper
    clean = raw.lower()
    for k, v in CURRENCY_MAP.items():
        if k in clean:
            return v
    return raw.upper().replace(" ", "_")


def parse_markdown_pack(text: str) -> Dict[str, Any]:
    # Extract Title / Product Name
    title_m = re.search(r"^#\s+Emotional Angle Pack\s*[—–-]\s*(.+)$", text, re.M)
    product_name = title_m.group(1).strip() if title_m else "Unknown Product"

    # Extract Header fields
    version_m = re.search(r"\*\*Version:\*\*\s*(.+)$", text, re.M)
    version = version_m.group(1).strip() if version_m else "v1.0"

    date_m = re.search(r"\*\*Date:\*\*\s*(\d{4}-\d{2}-\d{2})", text, re.M)
    date_val = date_m.group(1).strip() if date_m else "2026-08-14"

    methodology_m = re.search(r"\*\*Methodology:\*\*\s*(.+)$", text, re.M)
    methodology = methodology_m.group(1).strip() if methodology_m else "angle-ideation-agent@1.6.1"

    status_m = re.search(r"\*\*Status:\*\*\s*(.+)$", text, re.M)
    status_val = status_m.group(1).strip() if status_m else "Blocked"
    # Normalize status enum
    if "Ready" in status_val:
        status_clean = "Ready for Pre-Lander Agent"
    else:
        status_clean = "Blocked"

    scenario_m = re.search(r"\*\*Scenario:\*\*\s*([AB])", text, re.M)
    scenario = scenario_m.group(1).strip() if scenario_m else "B"

    run_id_m = re.search(r"\*\*Run ID:\*\*\s*(.+)$", text, re.M)
    run_id = run_id_m.group(1).strip() if run_id_m else "unknown_run"

    style_m = re.search(r"\*\*Style Controls:\*\*\s*Intensity (\d), Darkness (\d), Formality (\d), Distance (\d)", text, re.M)
    style_controls = None
    if style_m:
        style_controls = {
            "intensity": int(style_m.group(1)),
            "darkness": int(style_m.group(2)),
            "formality": int(style_m.group(3)),
            "distance": int(style_m.group(4))
        }

    trace_m = re.search(r"\*\*Trace ID:\*\*\s*(.+)$", text, re.M)
    model_m = re.search(r"\*\*Model:\*\*\s*(.+)$", text, re.M)
    temp_m = re.search(r"\*\*Temperature:\*\*\s*([\d.]+)", text, re.M)
    tokens_m = re.search(r"\*\*Tokens In/Out:\*\*\s*(\d+)\s*/\s*(\d+)", text, re.M)
    
    telemetry = None
    if trace_m or model_m or temp_m or tokens_m:
        telemetry = {}
        if trace_m: telemetry["trace_id"] = trace_m.group(1).strip()
        if model_m: telemetry["model_version"] = model_m.group(1).strip()
        if temp_m: telemetry["temperature"] = float(temp_m.group(1))
        if tokens_m:
            telemetry["tokens_in"] = int(tokens_m.group(1))
            telemetry["tokens_out"] = int(tokens_m.group(2))

    # Split angles
    angles_data: List[Dict[str, Any]] = []
    blocks = re.split(r"^###\s+(\d+)\.\s+The\s+(.+?)\s+Angle", text, flags=re.M)
    
    # re.split with groups returns: [pre, ord1, name1, body1, ord2, name2, body2, ...]
    if len(blocks) > 1:
        for i in range(1, len(blocks), 3):
            ordinal = int(blocks[i])
            name = f"The {blocks[i+1].strip()} Angle"
            body = blocks[i+2]

            curr_m = re.search(r"\*\*Psychosocial Currency:\*\*\s*(.+)$", body, re.M)
            raw_curr = curr_m.group(1).strip() if curr_m else ""
            currency_id = normalize_currency(raw_curr)

            core_m = re.search(r"\*\*Core Idea:\*\*\s*(.+)$", body, re.M)
            core_idea = core_m.group(1).strip() if core_m else ""

            headline_m = re.search(r"\*\*Headline:\*\*\s*\*?(.+?)\*?\s*$", body, re.M)
            headline = headline_m.group(1).strip().strip("*").strip() if headline_m else ""

            hollow_m = re.search(r"\*\*The Hollow:\*\*\s*(.+?)(?=\n\s*\*\*|\Z)", body, re.S)
            hollow = re.sub(r"\s+", " ", hollow_m.group(1).strip()) if hollow_m else ""

            villain_m = re.search(r"\*\*The Villain:\*\*\s*(.+?)(?=\n\s*\*\*|\Z)", body, re.S)
            villain = re.sub(r"\s+", " ", villain_m.group(1).strip()) if villain_m else ""

            dream_m = re.search(r"\*\*The Dream:\*\*\s*(.+?)(?=\n\s*\*\*|\Z)", body, re.S)
            dream = re.sub(r"\s+", " ", dream_m.group(1).strip()) if dream_m else ""

            arc_m = re.search(r"\*\*Story Arc:\*\*\s*(.+?)(?=\n\s*\*\*|\Z)", body, re.S)
            story_arc = re.sub(r"\s+", " ", arc_m.group(1).strip()) if arc_m else ""

            fit_m = re.search(r"\*\*Product Fit:\*\*\s*(.+?)(?=\n\s*\*\*|\Z)", body, re.S)
            product_fit = re.sub(r"\s+", " ", fit_m.group(1).strip()) if fit_m else ""

            aware_m = re.search(r"\*\*Awareness stage:\*\*\s*(problem_aware|solution_aware|product_aware)", body, re.M)
            awareness = aware_m.group(1).strip() if aware_m else "problem_aware"

            prio_m = re.search(r"\*\*Test priority:\*\*\s*(\d+)", body, re.M)
            test_priority = int(prio_m.group(1)) if prio_m else ordinal

            variants_block_m = re.search(r"\*\*Variants:\*\*(.+?)(?=\n\s*### |\Z)", body, re.S)
            variants = {}
            if variants_block_m:
                v_text = variants_block_m.group(1)
                comp_m = re.search(r"-\s*\*\*Compressed Story:\*\*\s*(.+?)(?=\n\s*-|\Z)", v_text, re.S)
                if comp_m:
                    variants["compressed_story"] = re.sub(r"\s+", " ", comp_m.group(1).strip())
                
                flip_m = re.search(r"-\s*\*\*Objection Flip:\*\*\s*(.+?)(?=\n\s*-|\Z)", v_text, re.S)
                if flip_m:
                    variants["objection_flip"] = re.sub(r"\s+", " ", flip_m.group(1).strip())
                
                hook_m = re.search(r"-\s*\*\*Hook Cluster:\*\*(.+?)(?=\n\s*- \*\*|\Z)", v_text, re.S)
                if hook_m:
                    hooks_raw = hook_m.group(1)
                    hooks = [h.strip() for h in re.findall(r"^\s*-\s+(.+)$", hooks_raw, re.M) if h.strip()]
                    if hooks:
                        variants["hook_cluster"] = hooks

            angle_obj = {
                "ordinal": ordinal,
                "name": name,
                "currency_id": currency_id,
                "core_idea": core_idea,
                "headline": headline,
                "hollow": hollow,
                "villain": villain,
                "dream": dream,
                "story_arc": story_arc,
                "product_fit": product_fit,
                "awareness_stage": awareness,
                "test_priority": test_priority,
            }
            if variants:
                angle_obj["variants"] = variants
            angles_data.append(angle_obj)

    pack_data = {
        "pack": {
            "product_name": product_name,
            "version": version,
            "date": date_val,
            "methodology": methodology,
            "status": status_clean,
            "scenario": scenario,
            "run_id": run_id,
            "contains": len(angles_data),
            "angles": angles_data,
        }
    }
    if style_controls:
        pack_data["pack"]["style_controls"] = style_controls
    if telemetry:
        pack_data["pack"]["telemetry"] = telemetry
    return pack_data


def main() -> int:
    parser = argparse.ArgumentParser(description="Export 05_angle_pack.md to JSON")
    parser.add_argument("pack_md", help="Path to 05_angle_pack.md")
    parser.add_argument("-o", "--output", help="Optional output JSON path (defaults to stdout or sidecar)")
    parser.add_argument("--schema", help="Path to schemas/angle_pack.schema.json", default=None)
    args = parser.parse_args()

    md_path = Path(args.pack_md)
    if not md_path.is_file():
        print(f"Error: file not found: {md_path}", file=sys.stderr)
        return 1

    text = md_path.read_text(encoding="utf-8")
    data = parse_markdown_pack(text)

    # Validate against schema if available
    repo_root = Path(__file__).resolve().parent.parent
    schema_path = Path(args.schema) if args.schema else repo_root / "schemas" / "angle_pack.schema.json"
    if jsonschema and schema_path.is_file():
        try:
            with open(schema_path, "r", encoding="utf-8") as f:
                schema_json = json.load(f)
            jsonschema.validate(instance=data, schema=schema_json)
            print(f"Validated exported JSON against {schema_path.name} [PASS]", file=sys.stderr)
        except Exception as e:
            print(f"Validation error against schema: {e}", file=sys.stderr)
            return 1

    json_str = json.dumps(data, indent=2, ensure_ascii=False)

    if args.output:
        out_path = Path(args.output)
        out_path.write_text(json_str, encoding="utf-8")
        print(f"Exported JSON saved to: {out_path}", file=sys.stderr)
    else:
        print(json_str)

    return 0


if __name__ == "__main__":
    sys.exit(main())
