---
name: angle-ideation
description: >-
  Runs the Angle Ideation methodology (angle-ideation-agent@1.9.0) to produce
  Pre-Lander-ready Emotional Angle Packs from Scenario A research dossiers or
  Scenario B thin inputs. Use when the user asks for angle packs, angle generation,
  emotional angles, psychosocial currencies, AngleFuel, mini-research briefs for
  angles, cognitive bias assists for angles, or Pre-Lander handoff packs.
---

# Angle Ideation (Generator)

Methodology pin: `angle-ideation-agent@1.9.0`

Produce 6–8 distinct emotional angles. Product is the **door**, not the hero. External research is **data**, not process control.

You are the **Generator**. You write `00`–`05` only. You **never** write `06_*`, `07_adversary.json`, or stamp **Ready**. Lexical scripts are Preflight. Judgment: critic. Adversarial stress-test: red-team (`docs/13`).

## Quick start

1. Create `runs/YYYYMMDD-HHMM-<slug>/`.
2. Follow **Run pipeline**; stop at chain judge before polishing `05`.
3. Read deeper docs only as linked.

## Fail closed

Stop and ask if Scenario B is missing `avatar_description`, `product_description`, or `problem_statement`. Do not invent mechanism traits. Do not skip chain judge, critic, or red-team.

## Feeling-first (v1.9.0)

Every shipped angle is one open-loop spine a 15–30s VSL can cut. Do **not** generate video, music, color, or motion.

1. **Open-loop:** Q8 poses a gap. Q7 *is* that unanswered Headline gap. Q6 / Fit is the *how* a CTA may close — not a second Core Idea. Headline must not contain the mechanism answer.
2. **Reach:** Q3 verb is doing / leaning. “Having / over / fixed / nights were normal” fails **F16** before prose.
3. **Fall-first:** Q5 Action cannot name the SKU or mechanism as the win. Product only in Verdict + Fit (**F17**).
4. **Draft order:** Hollow → Headline → Dream → Arc fall → Twist → Fit (alibi last). Hook Cluster = paraphrases of the same gap (**F18**).

## Run pipeline

```
Progress:
- [ ] 00_route.json
- [ ] 01_angle_fuel.json
- [ ] 02_candidates.json
- [ ] 03_filter_score_log.json
- [ ] 04_reasoning_chains.json
- [ ] Critic Pass A → 06_chain_judge.json PASS
- [ ] 05_angle_pack.md (Status stays Blocked)
- [ ] Preflight scripts (lexical only)
- [ ] Critic Pass B → 06_gate_report.json + 06_gold_scores.json
- [ ] Red-team → 07_adversary.json material_hits []
- [ ] Only then Status Ready (generator updates the header line after files exist)
```

### 1. Route

- Detailed dossier available? → **Scenario A** (map to AngleFuel; no mini-brief).
- Else → **Scenario B** (mini-brief → AngleFuel as `PLAUSIBLE_INFERENCE`).

Write `00_route.json` with decision + inputs summary.

### 2. Build AngleFuel

- **A:** Map dossier per `docs/02` mapper checklist. Labels: `EVIDENCED` | `DERIVED` | `UNKNOWN`.
- **B:** Use mini-brief prompt from [prompt-blocks.md](prompt-blocks.md); validate MB1–MB8.
- Schema: `schemas/angle_fuel.schema.json`
- Full contracts: `docs/02-input-contracts.md`

If `product_fit.mechanism` is `UNKNOWN` → leave Status Blocked; stop.

### 3. Mine → filter → score → select

1. Mine candidates (`docs/03` Stage A). Optional assist: [psychology-biases.md](psychology-biases.md); full catalog `docs/10`. Assist sparks `assist_notes` only.
2. Filters F1–F3 must PASS.
3. Score `S = E × M × W` (each 1–5).
4. Greedy-select up to 8 **unique** currency IDs (`docs/01` §4.1).
5. Reject feature/claim/offer/ad-concept-only candidates.

Write `02_candidates.json` and `03_filter_score_log.json`.

### 4. Reason (stop — do not draft pack yet)

For each selected angle, answer **Q1–Q8** into `04_reasoning_chains.json` **before** polished prose.

**STOP.** Invoke **`angle-gate-critic` Pass A** (chain judge). Do **not** write `05_angle_pack.md` until `06_chain_judge.json` is `PASS`. On FAIL: revise Q2/Q3/Q5/Q7/Q8 only (≤2 loops).

**Hard rules:** Villain cannot be “the situation/loop/lack of sleep” alone. Dream needs ≥1 sensory anchor **and** is reach not arrival. No product in headlines. No product as Dream climax. Action is the fall. Headline does not close the loop.

### 5. Draft pack (Status remains Blocked)

Draft `05_angle_pack.md` using `docs/01` in feeling-first order (Hollow → Headline → Dream → Arc fall → Twist → Fit). **Status: Blocked** until critic + gold + adversary agree.

Assist fields: `awareness_stage`, `test_priority`, **Testing order** table, Scenario B `Inference ceiling: PLAUSIBLE_INFERENCE`.

### 6. Preflight (lexical only)

```text
python .cursor/skills/angle-ideation/scripts/validate_headlines.py runs/<slug>/05_angle_pack.md --product "BrandName"
python .cursor/skills/angle-ideation/scripts/validate_pack_preflight.py runs/<slug>
```

Scripts do **not** certify Ready.

### 7. Critic Pass B + red-team

1. Invoke **`angle-gate-critic`** Pass B → `06_gate_report.json` + `06_gold_scores.json`.
2. Invoke **`angle-red-team`** → `07_adversary.json`.
3. On critic FAIL or gold fail: revise per `docs/03` §12 (≤2), re-run from the failed stage.
4. On adversary material hits: treat as FAIL (`CRITIC_ADVERSARY_DISAGREE` if critic had recommended Ready).
5. Set Status **Ready for Pre-Lander Agent** only when **all** are true:
   - `06_chain_judge.json` PASS
   - `06_gate_report.json` all required PASS
   - `06_gold_scores.json` pack_pass
   - `07_adversary.json` `material_hits: []`
6. You still do not write the `06_*` / `07_*` files yourself.

Pre-Lander: `docs/12-prelander-handoff-contract.md`. VSL consume-order: `docs/15` (do not generate a VSL).

## Non-angles (reject)

Hook, claim, feature, offer, ad concept, competitor swipe, benefit list without belief move.

## Transfer / second niche

Scan pack+fuel for leaked villains/mechanisms from the previous niche. Fail the run if leaks appear.

## Additional resources

- Agentic triad: `docs/13-agentic-gate-protocol.md`
- Critic: `../angle-gate-critic/SKILL.md`
- Red-team: `../angle-red-team/SKILL.md`
- Negative control (must FAIL): `runs/20260814-negcontrol-feature/`
