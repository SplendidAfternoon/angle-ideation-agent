#!/usr/bin/env python3
"""Standalone End-to-End Orchestration Pipeline for Angle Ideation Agent.

Executes the full Triad workflow (Generator -> Critic -> Red-Team)
using Gemini, OpenAI, or Anthropic APIs to produce verified Angle Packs.

Usage:
    python scripts/run_pipeline.py --avatar "Mothers of newborns" \
                                   --product "Baby Bubble" \
                                   --problem "Nasal congestion blocks feeding and sleep" \
                                   --competitors "NoseFrida, Braun, bulb syringe"
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

import urllib.error
import urllib.request

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMAS_DIR = REPO_ROOT / "schemas"
RUNS_DIR = REPO_ROOT / "runs"
METHODOLOGY = "angle-ideation-agent@1.9.0"

if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.llm_ops import (  # noqa: E402
    adversary_prompt,
    append_call,
    critic_prompt_pass_a,
    critic_prompt_pass_b,
    gold_prompt,
    new_trace,
    validate_against_schema,
    write_trace,
)
from scripts.validate_run import validate_run  # noqa: E402


# ==============================================================================
# LLM Provider Callers
# ==============================================================================

def call_gemini(
    prompt: str,
    system_instruction: str = "",
    model: str = "gemini-1.5-pro",
    api_key: Optional[str] = None,
    temperature: float = 0.7,
    json_mode: bool = False,
) -> Tuple[str, Dict[str, Any]]:
    """Call Google Gemini REST API."""
    key = api_key or os.getenv("GEMINI_API_KEY")
    if not key:
        raise ValueError("GEMINI_API_KEY is not set in environment or arguments.")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
    
    contents = []
    if system_instruction:
        contents.append({"role": "user", "parts": [{"text": f"System Instructions:\n{system_instruction}\n\nUser Request:\n{prompt}"}]})
    else:
        contents.append({"role": "user", "parts": [{"text": prompt}]})

    generation_config: Dict[str, Any] = {
        "temperature": temperature,
    }
    if json_mode:
        generation_config["responseMimeType"] = "application/json"

    payload = {
        "contents": contents,
        "generationConfig": generation_config,
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            candidate = data.get("candidates", [{}])[0]
            text = candidate.get("content", {}).get("parts", [{}])[0].get("text", "")
            usage = data.get("usageMetadata", {})
            meta = {
                "tokens_in": usage.get("promptTokenCount", 0),
                "tokens_out": usage.get("candidatesTokenCount", 0),
                "model": model,
                "provider": "gemini"
            }
            return text, meta
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Gemini API error ({e.code}): {err_body}") from e


def call_openai(
    prompt: str,
    system_instruction: str = "",
    model: str = "gpt-4o",
    api_key: Optional[str] = None,
    temperature: float = 0.7,
    json_mode: bool = False,
) -> Tuple[str, Dict[str, Any]]:
    """Call OpenAI Chat Completions API."""
    key = api_key or os.getenv("OPENAI_API_KEY")
    if not key:
        raise ValueError("OPENAI_API_KEY is not set in environment or arguments.")

    url = "https://api.openai.com/v1/chat/completions"
    messages = []
    if system_instruction:
        messages.append({"role": "system", "content": system_instruction})
    messages.append({"role": "user", "content": prompt})

    payload: Dict[str, Any] = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }
    if json_mode:
        payload["response_format"] = {"type": "json_object"}

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            text = data["choices"][0]["message"]["content"]
            usage = data.get("usage", {})
            meta = {
                "tokens_in": usage.get("prompt_tokens", 0),
                "tokens_out": usage.get("completion_tokens", 0),
                "model": model,
                "provider": "openai"
            }
            return text, meta
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"OpenAI API error ({e.code}): {err_body}") from e


def call_anthropic(
    prompt: str,
    system_instruction: str = "",
    model: str = "claude-3-5-sonnet-20241022",
    api_key: Optional[str] = None,
    temperature: float = 0.7,
    json_mode: bool = False,
) -> Tuple[str, Dict[str, Any]]:
    """Call Anthropic Messages API."""
    key = api_key or os.getenv("ANTHROPIC_API_KEY")
    if not key:
        raise ValueError("ANTHROPIC_API_KEY is not set in environment or arguments.")

    url = "https://api.anthropic.com/v1/messages"
    payload: Dict[str, Any] = {
        "model": model,
        "max_tokens": 4096,
        "temperature": temperature,
        "messages": [{"role": "user", "content": prompt}]
    }
    if system_instruction:
        payload["system"] = system_instruction

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "x-api-key": key,
            "anthropic-version": "2023-06-01"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            text = "".join(b["text"] for b in data.get("content", []) if b.get("type") == "text")
            usage = data.get("usage", {})
            meta = {
                "tokens_in": usage.get("input_tokens", 0),
                "tokens_out": usage.get("output_tokens", 0),
                "model": model,
                "provider": "anthropic"
            }
            return text, meta
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Anthropic API error ({e.code}): {err_body}") from e


def dispatch_llm(
    prompt: str,
    system_instruction: str = "",
    provider: str = "gemini",
    model: Optional[str] = None,
    temperature: float = 0.7,
    json_mode: bool = False,
) -> Tuple[str, Dict[str, Any]]:
    """Route LLM call to appropriate provider."""
    prov = provider.lower()
    if prov == "gemini":
        mdl = model or os.getenv("LLM_MODEL") or "gemini-1.5-pro"
        return call_gemini(prompt, system_instruction, mdl, temperature=temperature, json_mode=json_mode)
    elif prov == "openai":
        mdl = model or os.getenv("LLM_MODEL") or "gpt-4o"
        return call_openai(prompt, system_instruction, mdl, temperature=temperature, json_mode=json_mode)
    elif prov == "anthropic":
        mdl = model or os.getenv("LLM_MODEL") or "claude-3-5-sonnet-20241022"
        return call_anthropic(prompt, system_instruction, mdl, temperature=temperature, json_mode=json_mode)
    else:
        raise ValueError(f"Unknown LLM provider: {provider}")


def clean_json_response(text: str) -> Any:
    """Extract and parse JSON from markdown code block or raw string."""
    cleaned = text.strip()
    if cleaned.startswith("```json"):
        cleaned = cleaned[7:]
    elif cleaned.startswith("```"):
        cleaned = cleaned[3:]
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]
    cleaned = cleaned.strip()
    return json.loads(cleaned)


# ==============================================================================
# Pipeline Execution
# ==============================================================================

def execute_pipeline(
    avatar: str,
    product: str,
    problem: str,
    competitors: str = "",
    scenario: str = "B",
    provider: str = "gemini",
    model: Optional[str] = None,
    style_intensity: int = 4,
    style_darkness: int = 0,
    style_formality: int = 2,
    style_distance: int = 1,
    output_dir: Optional[Path] = None,
) -> Path:
    """Run full automated generation and validation pipeline."""
    slug_date = datetime.datetime.now().strftime("%Y%m%d")
    slug_name = re.sub(r"[^a-z0-9]+", "-", product.lower()).strip("-")
    run_id = f"{slug_date}-{slug_name}-auto"
    run_dir = output_dir or (RUNS_DIR / run_id)
    run_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n================================================================================")
    print(f"Angle Ideation Agent  Automated Pipeline")
    print(f"Run ID:    {run_id}")
    print(f"Product:   {product}")
    print(f"Provider:  {provider} ({model or 'default'})")
    print(f"Directory: {run_dir}")
    print(f"================================================================================\n")

    trace = new_trace(run_id, METHODOLOGY)
    provider_name = provider
    model_name = model or provider

    # Step 0: Route
    route_data = {
        "scenario": scenario,
        "run_id": run_id,
        "product_name": product,
        "inputs": {
            "avatar": avatar,
            "product": product,
            "problem": problem,
            "competitors": competitors
        },
        "style_controls": {
            "intensity": style_intensity,
            "darkness": style_darkness,
            "formality": style_formality,
            "distance": style_distance
        }
    }
    (run_dir / "00_route.json").write_text(json.dumps(route_data, indent=2), encoding="utf-8")
    print("[OK] [00_route.json] Initialized run context.")

    # Step 1: Mini-Brief & Fuel
    print(" [Stage 1] Generating Mini-Research Brief & AngleFuel...")
    p1_prompt = f"""You are a Research Agent generating a mini-research brief.
Inputs:
- Avatar: {avatar}
- Product: {product}
- Problem: {problem}
- Competitors: {competitors or 'Standard category alternatives'}

Task: Generate a structured mini-research brief JSON with avatar, pain_points, failed_attempts, emotional_effects, exact_vocabulary, future_fears, product_fit, competitors, psychosocial_currencies_candidates.
Return ONLY valid JSON.
"""
    raw_brief, meta = dispatch_llm(p1_prompt, provider=provider, model=model, temperature=0.5, json_mode=True)
    append_call(
        trace,
        role="generator",
        stage="mini_brief",
        ended_ok=True,
        model=meta.get("model", ""),
        provider=meta.get("provider", provider_name),
        temperature=0.5,
        tokens_in=int(meta.get("tokens_in") or 0),
        tokens_out=int(meta.get("tokens_out") or 0),
        artifact_written="01_mini_brief.json",
    )
    brief_data = clean_json_response(raw_brief)
    (run_dir / "01_mini_brief.json").write_text(json.dumps(brief_data, indent=2), encoding="utf-8")

    # Create AngleFuel
    fuel_data = {
        "meta": {
            "scenario": scenario,
            "methodology": METHODOLOGY,
            "product_name": product,
            "style_controls": {
                "intensity": style_intensity,
                "darkness": style_darkness,
                "formality": style_formality,
                "distance": style_distance
            }
        },
        "avatar": brief_data.get("avatar", {}),
        "pain_points": brief_data.get("pain_points", []),
        "failed_attempts": brief_data.get("failed_attempts", []),
        "emotional_effects": brief_data.get("emotional_effects", []),
        "exact_vocabulary": brief_data.get("exact_vocabulary", []),
        "future_fears": brief_data.get("future_fears", []),
        "product_fit": brief_data.get("product_fit", {}),
        "competitors": brief_data.get("competitors", []),
        "psychosocial_currencies_candidates": brief_data.get("psychosocial_currencies_candidates", []),
        "beliefs": {
            "held": ["I must solve this with willpower/standard tools"],
            "ready_to_shift": ["Standard tools fail because of physiological lock"]
        },
        "gaps": []
    }
    (run_dir / "01_angle_fuel.json").write_text(json.dumps(fuel_data, indent=2), encoding="utf-8")
    print("[OK] [01_mini_brief.json & 01_angle_fuel.json] Fuel prepared.")

    # Step 2: Mine Candidates
    print(" [Stage 2] Mining Angle Candidates across 8 Currencies...")
    p3_prompt = f"""Given AngleFuel JSON:
{json.dumps(fuel_data, indent=2)}

Mine 810 distinct angle candidates across distinct psychosocial currencies.
Return JSON array of objects:
[{{"candidate_id": "C01", "working_title": "...", "currency_id": "...", "belief_move": "shift", "belief_statement": "...", "pain_refs": [...], "villain_seed": "...", "mechanism_bridge": "...", "confession_seed": "..."}}]
Villain seed MUST be a concrete tool, advice pattern, or category flaw.
"""
    raw_cand, meta = dispatch_llm(p3_prompt, provider=provider, model=model, temperature=0.7, json_mode=True)
    append_call(
        trace,
        role="generator",
        stage="mine_candidates",
        ended_ok=True,
        model=meta.get("model", ""),
        provider=meta.get("provider", provider_name),
        temperature=0.7,
        tokens_in=int(meta.get("tokens_in") or 0),
        tokens_out=int(meta.get("tokens_out") or 0),
        artifact_written="02_candidates.json",
    )
    cand_data = clean_json_response(raw_cand)
    (run_dir / "02_candidates.json").write_text(json.dumps(cand_data, indent=2), encoding="utf-8")
    print("[OK] [02_candidates.json] Candidates mined.")

    # Step 3: Filter & Score
    print(" [Stage 3] Triple-Filtering & Scoring (E  M  W)...")
    p4_prompt = f"""Given candidates:
{json.dumps(cand_data, indent=2)}

Apply Triple Filters (F1 Voltage, F2 Mechanism line, F3 Whitespace).
Score survivors E, M, W (1-5); S = E*M*W. Select top 6-8 candidates with unique currency_id.
Return JSON:
{{"scored_candidates": [{{"candidate_id": "...", "F1": "PASS", "F2": "PASS", "F3": "PASS", "E": 5, "M": 4, "W": 5, "S": 100, "selected": true}}], "selected_ids": [...]}}
"""
    raw_score, meta = dispatch_llm(p4_prompt, provider=provider, model=model, temperature=0.2, json_mode=True)
    append_call(
        trace,
        role="generator",
        stage="filter_score",
        ended_ok=True,
        model=meta.get("model", ""),
        provider=meta.get("provider", provider_name),
        temperature=0.2,
        tokens_in=int(meta.get("tokens_in") or 0),
        tokens_out=int(meta.get("tokens_out") or 0),
        artifact_written="03_filter_score_log.json",
    )
    score_data = clean_json_response(raw_score)
    (run_dir / "03_filter_score_log.json").write_text(json.dumps(score_data, indent=2), encoding="utf-8")
    print("[OK] [03_filter_score_log.json] Candidates filtered and prioritized.")

    # Step 4: Reasoning Chains
    print(" [Stage 4] Building Per-Angle Q1Q8 Reasoning Chains...")
    p5_prompt = f"""For AngleFuel and Selected Candidates:
AngleFuel: {json.dumps(fuel_data, indent=2)}
Selected Candidate IDs: {json.dumps(score_data.get('selected_ids', []), indent=2)}

For each selected candidate, answer Q1 through Q8 in writing.
Q1: specific loss (Hollow)
Q2: villain (concrete tool/advice pattern)
Q3: dream (sensory relief anchor)
Q4: currency_id
Q5: 4-beat story arc
Q6: product mechanism fit
Q7: belief shift (Core Idea)
Q8: headline candidates (past tense <=12 words)

Return JSON array of reasoning chain objects.
"""
    raw_chains, meta = dispatch_llm(p5_prompt, provider=provider, model=model, temperature=0.4, json_mode=True)
    append_call(
        trace,
        role="generator",
        stage="reasoning_chains",
        ended_ok=True,
        model=meta.get("model", ""),
        provider=meta.get("provider", provider_name),
        temperature=0.4,
        tokens_in=int(meta.get("tokens_in") or 0),
        tokens_out=int(meta.get("tokens_out") or 0),
        artifact_written="04_reasoning_chains.json",
    )
    chains_data = clean_json_response(raw_chains)
    (run_dir / "04_reasoning_chains.json").write_text(json.dumps(chains_data, indent=2), encoding="utf-8")
    print("[OK] [04_reasoning_chains.json] Reasoning chains drafted.")

    # Step 5: Chain Critic (Pass A) — real judge, never default PASS
    print(" [Stage 5] Critic Pass A (Chain Judge)...")
    p6_prompt = critic_prompt_pass_a(run_id, METHODOLOGY, chains_data)
    raw_judge, meta = dispatch_llm(
        p6_prompt, provider=provider, model=model, temperature=0.1, json_mode=True
    )
    judge_data = clean_json_response(raw_judge)
    if isinstance(judge_data, list):
        judge_data = {
            "run_id": run_id,
            "methodology": METHODOLOGY,
            "critic": "angle-gate-critic@1.9.0",
            "result": "FAIL",
            "chains": judge_data,
        }
    judge_data.setdefault("run_id", run_id)
    judge_data.setdefault("methodology", METHODOLOGY)
    judge_data.setdefault("critic", "angle-gate-critic@1.9.0")
    judge_errs = validate_against_schema(judge_data, SCHEMAS_DIR / "chain_judge.schema.json")
    chain_ok = judge_data.get("result") == "PASS" and not judge_errs
    append_call(
        trace,
        role="critic",
        stage="chain_judge",
        ended_ok=chain_ok,
        model=meta.get("model", ""),
        provider=meta.get("provider", provider_name),
        temperature=0.1,
        tokens_in=int(meta.get("tokens_in") or 0),
        tokens_out=int(meta.get("tokens_out") or 0),
        artifact_written="06_chain_judge.json",
        notes="; ".join(judge_errs) if judge_errs else "",
    )
    (run_dir / "06_chain_judge.json").write_text(json.dumps(judge_data, indent=2), encoding="utf-8")
    if not chain_ok:
        print("[BLOCKED] Chain judge FAIL or schema invalid. Not drafting Ready pack; no stub gates.")
        write_trace(run_dir, trace)
        return run_dir
    print("[OK] [06_chain_judge.json] Pass A PASS.")

    # Step 6: Draft pack — Status stays Blocked until triad exists
    print(" [Stage 6] Generator drafting 05_angle_pack.md (Status=Blocked)...")
    p7_prompt = f"""You are the Angle Ideation Generator. You do NOT stamp Ready.
Draft 05_angle_pack.md from the passed reasoning chains and AngleFuel.

Header (exact Status line):
# Emotional Angle Pack — {product}
**Version:** v1.0
**Date:** {datetime.date.today().isoformat()}
**Methodology:** {METHODOLOGY}
**Status:** Blocked
**Contains:** [N] angles
**Scenario:** {scenario}
**Run ID:** {run_id}
**Inference ceiling:** PLAUSIBLE_INFERENCE (Scenario B required)

Include: Headline Rules Applied, Angle Component Definitions, Angles (6–8 unique currencies),
Summary Table, Testing order.
Per angle: Psychosocial Currency, Core Idea, Headline, The Hollow, The Villain, The Dream,
Story Arc, Product Fit, Awareness stage, Test priority.
Product is the door, not the hero. No product token in headlines. Villain cannot be
"the loop/situation/parenthood". Dream cannot climax on the product.

Emit ONLY the complete Markdown.
"""
    pack_md, meta = dispatch_llm(
        p7_prompt, provider=provider, model=model, temperature=0.7, json_mode=False
    )
    if pack_md.strip().startswith("```markdown"):
        pack_md = pack_md.strip()[11:]
    elif pack_md.strip().startswith("```"):
        pack_md = pack_md.strip()[3:]
    if pack_md.strip().endswith("```"):
        pack_md = pack_md.strip()[:-3]
    pack_md = pack_md.strip() + "\n"
    if "**Status:** Ready" in pack_md:
        pack_md = re.sub(
            r"\*\*Status:\*\*\s*.+",
            "**Status:** Blocked",
            pack_md,
            count=1,
        )
    (run_dir / "05_angle_pack.md").write_text(pack_md, encoding="utf-8")
    append_call(
        trace,
        role="generator",
        stage="draft_pack",
        ended_ok=True,
        model=meta.get("model", ""),
        provider=meta.get("provider", provider_name),
        temperature=0.7,
        tokens_in=int(meta.get("tokens_in") or 0),
        tokens_out=int(meta.get("tokens_out") or 0),
        artifact_written="05_angle_pack.md",
    )
    print("[OK] [05_angle_pack.md] drafted Blocked.")

    pack_text = (run_dir / "05_angle_pack.md").read_text(encoding="utf-8")

    # Step 7: Critic Pass B + gold — LLM, schema-valid, never hardcoded
    print(" [Stage 7] Critic Pass B (gates + gold)...")
    raw_gates, meta = dispatch_llm(
        critic_prompt_pass_b(run_id, METHODOLOGY, pack_text, fuel_data),
        provider=provider,
        model=model,
        temperature=0.1,
        json_mode=True,
    )
    gate_report_data = clean_json_response(raw_gates)
    gate_report_data.setdefault("run_id", run_id)
    gate_report_data.setdefault("methodology", METHODOLOGY)
    gate_report_data.setdefault("critic", "angle-gate-critic@1.9.0")
    gate_errs = validate_against_schema(gate_report_data, SCHEMAS_DIR / "gate_report.schema.json")
    append_call(
        trace,
        role="critic",
        stage="pack_gates",
        ended_ok=not gate_errs,
        model=meta.get("model", ""),
        provider=meta.get("provider", provider_name),
        temperature=0.1,
        tokens_in=int(meta.get("tokens_in") or 0),
        tokens_out=int(meta.get("tokens_out") or 0),
        artifact_written="06_gate_report.json",
        notes="; ".join(gate_errs) if gate_errs else "",
    )
    (run_dir / "06_gate_report.json").write_text(
        json.dumps(gate_report_data, indent=2), encoding="utf-8"
    )

    raw_gold, meta = dispatch_llm(
        gold_prompt(run_id, METHODOLOGY, pack_text),
        provider=provider,
        model=model,
        temperature=0.1,
        json_mode=True,
    )
    gold_scores_data = clean_json_response(raw_gold)
    gold_scores_data.setdefault("run_id", run_id)
    gold_scores_data.setdefault("methodology", METHODOLOGY)
    gold_scores_data.setdefault("critic", "angle-gate-critic@1.9.0")
    gold_errs = validate_against_schema(gold_scores_data, SCHEMAS_DIR / "gold_scores.schema.json")
    append_call(
        trace,
        role="critic",
        stage="gold_scores",
        ended_ok=not gold_errs,
        model=meta.get("model", ""),
        provider=meta.get("provider", provider_name),
        temperature=0.1,
        tokens_in=int(meta.get("tokens_in") or 0),
        tokens_out=int(meta.get("tokens_out") or 0),
        artifact_written="06_gold_scores.json",
        notes="; ".join(gold_errs) if gold_errs else "",
    )
    (run_dir / "06_gold_scores.json").write_text(
        json.dumps(gold_scores_data, indent=2), encoding="utf-8"
    )

    # Step 8: Red-team — LLM, never empty-by-construction
    print(" [Stage 8] Red-Team Adversary...")
    raw_adv, meta = dispatch_llm(
        adversary_prompt(run_id, METHODOLOGY, pack_text),
        provider=provider,
        model=model,
        temperature=0.1,
        json_mode=True,
    )
    adv_data = clean_json_response(raw_adv)
    adv_data.setdefault("run_id", run_id)
    adv_data.setdefault("methodology", METHODOLOGY)
    adv_data.setdefault("adversary", "angle-red-team@1.9.0")
    if "nits" not in adv_data:
        adv_data["nits"] = adv_data.pop("minor_notes", []) or []
    if "recommendation" not in adv_data and adv_data.get("result"):
        adv_data["recommendation"] = adv_data["result"]
    adv_errs = validate_against_schema(adv_data, SCHEMAS_DIR / "adversary.schema.json")
    append_call(
        trace,
        role="red_team",
        stage="adversary",
        ended_ok=not adv_errs,
        model=meta.get("model", ""),
        provider=meta.get("provider", provider_name),
        temperature=0.1,
        tokens_in=int(meta.get("tokens_in") or 0),
        tokens_out=int(meta.get("tokens_out") or 0),
        artifact_written="07_adversary.json",
        notes="; ".join(adv_errs) if adv_errs else "",
    )
    (run_dir / "07_adversary.json").write_text(json.dumps(adv_data, indent=2), encoding="utf-8")

    gates_list = gate_report_data.get("gates") if isinstance(gate_report_data.get("gates"), list) else []
    gates_ok = (
        not gate_errs
        and gate_report_data.get("pack_status_recommendation") == "Ready for Pre-Lander Agent"
        and all(g.get("result") == "PASS" for g in gates_list)
        and (gate_report_data.get("cold_reread") or {}).get("completed") is True
    )
    gold_ok = not gold_errs and gold_scores_data.get("pack_pass") is True
    adv_ok = (
        not adv_errs
        and not adv_data.get("material_hits")
        and adv_data.get("recommendation") == "NO_MATERIAL_HITS"
        and not adv_data.get("disagree_with_critic")
    )
    triad_ok = chain_ok and gates_ok and gold_ok and adv_ok
    status_line = "Ready for Pre-Lander Agent" if triad_ok else "Blocked"
    pack_text = re.sub(
        r"\*\*Status:\*\*\s*.+",
        f"**Status:** {status_line}",
        pack_text,
        count=1,
        flags=re.M,
    )
    (run_dir / "05_angle_pack.md").write_text(pack_text, encoding="utf-8")
    trace["ready_stamped_by"] = (
        "generator_header_after_triad" if triad_ok else "not_ready"
    )
    append_call(
        trace,
        role="generator",
        stage="stamp_status",
        ended_ok=True,
        model=model_name,
        provider=provider_name,
        artifact_written="05_angle_pack.md",
        notes=status_line,
    )
    write_trace(run_dir, trace)
    print(f"[OK] Status set to {status_line} after triad (no hardcoded PASS).")

    # Step 9: Export JSON
    print(" [Stage 9] Exporting 05_angle_pack.json...")
    try:
        from scripts.export_angle_pack_json import parse_markdown_pack

        pack_json_data = parse_markdown_pack(pack_text)
        (run_dir / "05_angle_pack.json").write_text(
            json.dumps(pack_json_data, indent=2), encoding="utf-8"
        )
        print("[OK] [05_angle_pack.json] exported.")
    except Exception as e:
        print(f" Warning during JSON export: {e}")

    # Step 10: Unified validator
    print(" [Stage 10] Running validate_run...")
    all_passed, errs = validate_run(
        run_dir=run_dir, repo_root=REPO_ROOT, product_name=product, verbose=True
    )
    if all_passed:
        print("\nALL VALIDATION CHECKS PASSED")
    else:
        print(f"\n{len(errs)} validation failure(s) — pack remains inspectable.")

    print(f"\n================================================================================")
    print(f"Run Complete: {run_dir}")
    print(f"Markdown:     {run_dir / '05_angle_pack.md'}")
    print(f"Trace:        {run_dir / '09_llm_trace.json'}")
    print(f"================================================================================\n")
    return run_dir


# ==============================================================================
# CLI Entrypoint
# ==============================================================================

def main() -> int:
    parser = argparse.ArgumentParser(description="Angle Ideation Agent  Automated Standalone Runner")
    parser.add_argument("--avatar", help="Avatar description / target audience", default=None)
    parser.add_argument("--product", help="Product name and short description", default=None)
    parser.add_argument("--problem", help="Core pain point or problem statement", default=None)
    parser.add_argument("--competitors", help="Competitor brands/alternatives", default="")
    parser.add_argument("--brief", help="Path to a JSON file containing avatar/product/problem", default=None)
    parser.add_argument("--provider", help="LLM Provider: gemini | openai | anthropic", default="gemini")
    parser.add_argument("--model", help="Specific model name", default=None)
    parser.add_argument("--intensity", type=int, help="Style Intensity (1-5)", default=4)
    parser.add_argument("--darkness", type=int, help="Style Darkness (0-1)", default=0)
    parser.add_argument("--formality", type=int, help="Style Formality (1-5)", default=2)
    parser.add_argument("--distance", type=int, help="Style Distance (1-5)", default=1)
    parser.add_argument("-o", "--output-dir", help="Custom output directory path", default=None)
    args = parser.parse_args()

    avatar = args.avatar
    product = args.product
    problem = args.problem
    competitors = args.competitors

    # If brief file is supplied
    if args.brief:
        brief_path = Path(args.brief)
        if not brief_path.is_file():
            print(f"Error: Brief file not found: {brief_path}", file=sys.stderr)
            return 1
        data = json.loads(brief_path.read_text(encoding="utf-8"))
        avatar = avatar or data.get("avatar", "")
        product = product or data.get("product", "")
        problem = problem or data.get("problem", "")
        competitors = competitors or data.get("competitors", "")

    # Default fallback demo if none provided
    if not (avatar and product and problem):
        print("No input arguments provided. You can run with:")
        print("  python scripts/run_pipeline.py --avatar \"Mothers of congested newborns\" \\")
        print("                                 --product \"Baby Bubble\" \\")
        print("                                 --problem \"Nasal congestion blocks feeding and sleep\" \\")
        print("                                 --competitors \"NoseFrida, Braun, bulb syringe\"\n")
        return 1

    out_path = Path(args.output_dir) if args.output_dir else None

    try:
        execute_pipeline(
            avatar=avatar,
            product=product,
            problem=problem,
            competitors=competitors,
            provider=args.provider,
            model=args.model,
            style_intensity=args.intensity,
            style_darkness=args.darkness,
            style_formality=args.formality,
            style_distance=args.distance,
            output_dir=out_path
        )
        return 0
    except Exception as e:
        print(f"\n Pipeline Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
