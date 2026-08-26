#!/usr/bin/env python3
"""LLM-ops helpers: traces, schema checks, refuse stub critic artifacts."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import jsonschema
except ImportError:
    jsonschema = None


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def new_trace(run_id: str, methodology: str) -> Dict[str, Any]:
    return {
        "run_id": run_id,
        "methodology": methodology,
        "collapsed_roles": False,
        "ready_stamped_by": "not_ready",
        "started_at": utc_now(),
        "calls": [],
    }


def append_call(
    trace: Dict[str, Any],
    *,
    role: str,
    stage: str,
    ended_ok: bool,
    model: str = "",
    provider: str = "",
    temperature: float = 0.0,
    tokens_in: int = 0,
    tokens_out: int = 0,
    artifact_written: str = "",
    notes: str = "",
) -> None:
    trace["calls"].append(
        {
            "role": role,
            "stage": stage,
            "model": model,
            "provider": provider,
            "temperature": temperature,
            "tokens_in": tokens_in,
            "tokens_out": tokens_out,
            "artifact_written": artifact_written,
            "ended_ok": ended_ok,
            "notes": notes,
        }
    )


def write_trace(run_dir: Path, trace: Dict[str, Any]) -> None:
    (run_dir / "09_llm_trace.json").write_text(
        json.dumps(trace, indent=2), encoding="utf-8"
    )


def validate_against_schema(
    instance: Dict[str, Any], schema_path: Path
) -> List[str]:
    if not jsonschema:
        return ["jsonschema not installed"]
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    try:
        jsonschema.validate(instance=instance, schema=schema)
        return []
    except jsonschema.ValidationError as e:
        return [e.message]


def critic_prompt_pass_a(run_id: str, methodology: str, chains: Any) -> str:
    return f"""You are angle-gate-critic. Judge Q1–Q8 chains only. Do not draft pack prose.
Do not default to PASS. If Q2 is situational (loop/parenthood/lack of sleep), FAIL.
If Q3 has no sensory anchor, is product climax, or is arrival/having (F16), FAIL.
If Q5 Action is a feature win / mechanism before the fall (F17), FAIL.
If Q7 is feature/claim/offer, FAIL.
If Q8 would fail H4/H6 or closes the loop with the mechanism answer, FAIL.

run_id={run_id}
methodology={methodology}

chains:
{json.dumps(chains, indent=2)}

Return ONLY JSON matching schemas/chain_judge.schema.json with required fields
run_id, methodology, critic (angle-gate-critic@…), result (PASS|FAIL), chains[].
Each chain needs angle_ordinal, Q2_villain, Q3_dream, Q7_core, Q8_headline, result, evidence (quote).
"""


def critic_prompt_pass_b(run_id: str, methodology: str, pack_md: str, fuel: Any) -> str:
    return f"""You are angle-gate-critic Pass B. Prefer FAIL when uncertain.
gates MUST be an array of objects {{gate_id, scope, result, evidence}} — never a map.
evidence must quote ≤25 words from the pack. Do not use generic phrases like
"Scene-level emotional loss". Fail F16 arrival Dream, F17 mechanism-in-Action,
and F18 Hook Cluster mashup.

run_id={run_id}
methodology={methodology}
fuel.product_fit={json.dumps((fuel or {{}}).get("product_fit", {{}}))}

PACK:
{pack_md[:24000]}

Return ONLY JSON with:
run_id, methodology, critic, pack_status_recommendation (Ready for Pre-Lander Agent|Blocked),
gates (array), cold_reread {{completed, failures_found}}.
Also return a sibling object is forbidden — just the gate report JSON.
"""


def gold_prompt(run_id: str, methodology: str, pack_md: str) -> str:
    return f"""Score each shipped angle 1–5 on hollow_specificity, villain_concreteness,
dream_render, belief_move, headline_punch, mechanism_honesty. Include mean and evidence quote.
dream_render 5 is cinematic reach (doing/leaning), not consumption or arrival.
pack_pass true only if pack_mean >= 4.0 and no dimension average < 3.5.
Do not invent 4.5 for feature sheets.

run_id={run_id}
methodology={methodology}

PACK:
{pack_md[:24000]}

Return ONLY JSON matching schemas/gold_scores.schema.json (critic field required).
"""


def adversary_prompt(run_id: str, methodology: str, pack_md: str) -> str:
    return f"""You are angle-red-team. Hunt F01–F18. Prefer over-reporting nits.
If Core Idea is a spec/claim, that is a material_hit. F16 arrival Dream, F17
mechanism-in-Action, and F18 Hook Cluster mashup are material_hits. Empty
material_hits only if truly clean.
Required keys: run_id, methodology, adversary, material_hits, nits, recommendation
(NO_MATERIAL_HITS|BLOCK). Do not use key "result" instead of recommendation.

run_id={run_id}
methodology={methodology}

PACK:
{pack_md[:24000]}

Return ONLY JSON matching schemas/adversary.schema.json.
"""
