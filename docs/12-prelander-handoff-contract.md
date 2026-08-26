# 12 — Pre-Lander Handoff Contract

**Version:** 1.9.0  
**Normative:** Yes  
**Methodology pin:** `angle-ideation-agent@1.9.0`  
**Depends on:** `docs/01`, `docs/04`, `docs/13`  
**Purpose:** Freeze what the Pre-Lander agent may read from an Angle Pack. This document does **not** write pages, VSLs, or Meta creatives.

## 1. Readiness predicate

Pre-Lander may consume a run **only if all** are true:

1. `05_angle_pack.md` exists and matches the skeleton in `docs/01`.  
2. Pack header **Status** = `Ready for Pre-Lander Agent`.  
3. `06_gate_report.json` exists, validates against `schemas/gate_report.schema.json`, and every **required** gate is `PASS`.  
4. `06_chain_judge.json` `result: PASS`.  
5. `06_gold_scores.json` `pack_pass: true`.  
6. `07_adversary.json` `material_hits` is empty.  
7. Critic pin + `cold_reread.completed: true`.  
8. Lexical preflight recorded (not a substitute for 3–6).  
9. Supporting artifacts `01_angle_fuel.json` and `04_reasoning_chains.json` exist.

If any fail → Pre-Lander **must not** start; treat as Blocked upstream.

## 2. Fields Pre-Lander may read

1:1 with `docs/01` pack components. No invented fields.

### 2.1 Pack header

| Field | Source | Use |
|-------|--------|-----|
| `product_name` | Title / header | Product naming consistency |
| `run_id` | Header | Traceability |
| `scenario` | Header | A vs B confidence context |
| `methodology` | Header | Pin check |
| `status` | Header | Must be Ready |
| `contains` | Header | Expected angle count |

### 2.2 Per-angle story inputs

| Pack field | Pre-Lander story role |
|------------|----------------------|
| Angle Name | Internal label / section title seed |
| Psychosocial Currency (Currency ID) | Theme / Andromeda congruency key |
| Core Idea | Belief spine of the page |
| Headline | Opening confession / hook line (may adapt later; do not invent a new angle) |
| The Hollow | Loss scene the story must make felt |
| The Villain | Blame object the story relocates to |
| The Dream | Sensory resolution moment (not product climax) |
| Story Arc | Setup → Action → Twist → Verdict beat sheet |
| Product Fit | Mechanism doorway only — product enters late |
| Awareness stage (assist) | Cold-traffic message stage; default `problem_aware`; do not invent offer ads |
| Test priority (assist) | Concept test order (1 first); not bids or placements |

### 2.3 Pack-level tables

| Section | Use |
|---------|-----|
| Headline Rules Applied | Compliance audit |
| Summary Table | Index of shipped angles |
| Headline Refinement Summary | Rejected alternatives (optional reference) |
| Testing order | Which distinct concepts to try first (not ad copy) |

## 3. Fields Pre-Lander must not invent from silence

- New psychosocial currencies not in the pack  
- New villains / mechanisms absent from pack + fuel  
- Medical claims beyond Product Fit / fuel  
- Offers, pricing, scarcity, “doctor recommends” unless separately supplied  
- Bias names as page thesis (`docs/10` assist is upstream-only)

## 4. Mapping rule (angle → page)

One shipped angle → one primary Pre-Lander narrative spine.  
Do not merge two currencies into one page without a new Angle Ideation run.

```text
Angle.CoreIdea     → belief frame
Angle.Hollow       → problem world
Angle.Villain      → wrong-enemy reveal
Angle.Dream        → earned sensory close
Angle.StoryArc     → beat order
Angle.ProductFit   → late doorway (product is door, not hero)
Angle.Headline     → candidate open; may be refined for medium, not replaced with a feature pitch
Angle.Awareness    → keep page cold-problem unless tagged solution_aware
Angle.TestPriority → if producing multiple pages, start with priority 1
```

Short-form VSL beat order (hook → dream → story → drama → payoff → CTA): [`docs/15-vsl-deployment-contract.md`](15-vsl-deployment-contract.md). Still one angle per cut.

## 5. Machine mirror

JSON shape: `schemas/angle_pack.schema.json` (mirrors `docs/01` §7).  
Markdown pack remains the human handoff; JSON may be emitted by future automation. Both must agree on predicates.

## 6. Non-goals

- Writing HTML/advertorial/VSL  
- Selecting Meta placements or bids  
- Re-running Angle Ideation inside Pre-Lander
