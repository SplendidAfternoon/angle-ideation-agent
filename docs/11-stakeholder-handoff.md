# 11 — System Handoff & Architecture Overview

**Audience:** Technical Reviewers, Growth Engineers & Copywriters  
**Project:** Angle Ideation Agent  
**Methodology pin:** `angle-ideation-agent@1.9.0` — **complete**  

This is a **finished methodology** (generation logic + quality gates) plus skills and tooling to execute and validate it. Not a Pre-Lander page generator and not a product app.

---

## 1. The Angle Pack

The reference benchmark pack:

**[runs/20260814-bb-benchmark/05_angle_pack.md](../runs/20260814-bb-benchmark/05_angle_pack.md)**

Scenario B thin inputs only (mothers of congested newborns; nasal aspirator with a clear collection cup; congestion blocks sleep and feeding; NoseFrida / Braun / bulb). Reference gold exemplar was not used as a copy source.

| Artifact | Result |
|----------|--------|
| `06_chain_judge.json` | PASS (revision_loop 1) |
| `06_gate_report.json` | all required PASS |
| `06_gold_scores.json` | pack_mean **4.48**, pack_pass |
| `07_adversary.json` | `material_hits: []` |
| Pack Status | **Ready for Pre-Lander Agent** |

---

## 2. How we iterate

Gates fail → change the methodology (`docs/03` or `docs/04`) → generate again. Do not patch by copying gold headlines or arcs.

```text
00–04 → chain judge → 05 (Blocked) → preflight → critic gates + gold → red-team → Ready | Blocked
```

**This loop ran once.** First Ready stamp failed honest F03/F05 (loop-villains; Dream peaking on the cup). v1.6.1 tightened those rules; affected Q2/Q3 fields were regenerated; second triad PASS.

Ready only if all four of `docs/13` are true. Max 2 revise loops.

---

## 3. Finished methodology

| Piece | Location |
|-------|----------|
| Design (contracts, generation, checklist) | `docs/00`–`docs/08` |
| How to rerun | `.cursor/skills/angle-ideation/` (generator), `angle-gate-critic`, `angle-red-team` |
| Quality bar | `docs/04` gates + `docs/05` gold rubric (mean ≥ 4.0) |

**Run:** Open this project in Cursor. Ask for an Angle Pack. Scenario B needs avatar, product, problem (competitors optional). Fail closed if any of those three is missing.

**Automation & validation tools:**

```bash
# Automated regression test suite
python -m unittest tests/test_runs.py

# Unified run validator (schemas + preflight + triad predicates)
python scripts/validate_run.py runs/<slug> --product "Brand"

# Export pack to validated JSON (docs/12)
python scripts/export_angle_pack_json.py runs/<slug>/05_angle_pack.md -o runs/<slug>/05_angle_pack.json

# Skill-local lexical preflight
python .cursor/skills/angle-ideation/scripts/validate_headlines.py runs/<slug>/05_angle_pack.md --product "Brand"
python .cursor/skills/angle-ideation/scripts/validate_pack_preflight.py runs/<slug>
```

**No further methodology expansion unless asked.**

---

## Artifact contract

| File | Required |
|------|----------|
| `00_route.json` | Scenario decision + inputs |
| `01_angle_fuel.json` | Normalized fuel |
| `01_mini_brief.json` | Scenario B only (MB1–MB8) |
| `02_candidates.json` | Mined candidates |
| `03_filter_score_log.json` | F1–F3 + `S = E×M×W` |
| `04_reasoning_chains.json` | Q1–Q8 per selected angle |
| `05_angle_pack.md` | Handoff pack (`docs/01`) |
| `06_chain_judge.json` | Q2/Q3/Q7/Q8 before prose |
| `06_gate_report.json` | Gate PASS/FAIL + cold reread |
| `06_gold_scores.json` | L2 rubric every Ready |
| `07_adversary.json` | Red-team; empty `material_hits` for Ready |

Bias catalog (`docs/10`) is **assist only**. Core Idea must never be a bias name.

---

## Non-goals

- Pre-lander / advertorial / VSL generation  
- Meta performance prediction  
- Deployed app or research pipelines  
- More skills or catalog expansion  

Downstream: [`docs/14-downstream-deferrals.md`](14-downstream-deferrals.md).
