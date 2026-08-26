# Critic protocol (angle-gate-critic@1.9.0)

Evaluate in order. For each gate emit `{gate_id, scope, result, evidence, notes, fix_hint?}`.

**Evidence rule:** Quote ≤25 words from pack, fuel, or chain field. Judgment without evidence → FAIL `CRITIC_NO_EVIDENCE`.

**Anti-sycophancy:** If A-VILLAIN / A-DREAM / A-HOLLOW are borderline, FAIL.

**Ready is not yours alone:** gates PASS + gold pack_pass is a *recommendation*. Pack Status Ready only after `07_adversary.json` has `material_hits: []`.

## Pass A — Chain judge (`06_chain_judge.json`)

Required **before** shipping `05`. Input: `04_reasoning_chains.json` + `01_angle_fuel.json`.

Per chain, FAIL if:

| Q | Fail when |
|---|-----------|
| Q2 | Villain is situation/loop/lack of sleep/parenthood alone |
| Q3 | Dream has no sight/sound/place/body anchor **or** is arrival / having (“it was over”, “nights were normal”, problem gone) — **F16** |
| Q5 | Action beat is a feature win (SKU / mechanism as the win; fall missing) — **F17** |
| Q7 | Core is feature/claim/offer (F01/F12) **or** restates Product Fit as a second thesis |
| Q8 | Headline would fail H4/H6 **or** contains the mechanism answer / closes the loop (“and then we slept”) |

Any chain FAIL → `result: FAIL`; generator revises Qs (≤2), does not pretty-print `05` yet.

## Few-shot negatives (required before pack scoring)

Load `docs/04` §9 **F01–F18**. If a shipped field matches a failure class, FAIL the mapped gate(s) and cite the catalog ID in `notes`.

| ID | Match if you see | Fail |
|----|------------------|------|
| F01 | Core Idea is a spec/claim (“clears in seconds”, hospital-grade) | `A-CORE` |
| F02 | Hollow is mood-only (stressed/sad/overwhelmed) | `A-HOLLOW` |
| F03 | Villain is situation (“parenthood”, “the loop”, “lack of sleep”) | `A-VILLAIN` |
| F04 | Dream is benefit summary (“life got better”) | `A-DREAM` |
| F05 | Dream climax is unboxing / product joy | `A-DOOR` |
| F06 | Two hollows are the same core friction with nouns swapped | `P-DISTINCT` |
| F07 | Belief/cosmology absent from fuel | `A-BELIEF` |
| F08 | Headline starts with At / For weeks / Today… | `H5` |
| F09 | Product name or ad-ese in headline | `H4`, `H6` |
| F10 | Arc is try → buy → slept with no twist | `A-ARC` |
| F11 | Currency pair violates `docs/01` §4.1 | `P-CURRENCY-RULES` |
| F12 | Offer / discount / “moms swear by” as Core Idea or headline | `A-CORE` |
| F13 | All angles same archetype / max gut-punch | `P-ARCHETYPE-DIVERSITY` |
| F14 | All headlines the same syntactic stencil | `P-HEADLINE-DIVERSITY` |
| F15 | All angles `problem_aware` | `P-AWARENESS-DIVERSITY` |
| F16 | Dream is arrived / having (“She finally slept through; it was over.”) | `A-DREAM` |
| F17 | Arc Action is a feature win (“Tried the cup → mucus visible → slept”) | `A-ARC` |
| F18 | Hook Cluster is competing theses/currencies (mould / 911 / 20% off) | `A-CORE`, Hook Cluster |

Reference pack that must Block: `runs/20260814-negcontrol-feature/`. VSL-doctrine fixture that must FAIL: `eval/fixtures/vsl-doctrine-fail/`.

## Input / headline / component / pack gates

Unchanged tests from `docs/04` plus:

| ID | Test |
|----|------|
| P-CHAIN-JUDGE | `06_chain_judge.json` exists and `result: PASS` |
| P-GOLD | `06_gold_scores.json` pack_pass true |
| P-ADVERSARY | `07_adversary.json` material_hits empty |

Pairwise P-DISTINCT: unique currencies are not enough; noun-swapped hollows FAIL (F06).

Dream render 5 (`docs/05` §3.4) is cinematic *reach*, not consumption.

## Gold-class scores (`06_gold_scores.json`)

Every Ready run. Dimensions (`docs/05` §3.4): hollow_specificity, villain_concreteness, dream_render, belief_move, headline_punch, mechanism_honesty (1–5) with a quote per angle.

**dream_render = 5** only if the moment is mid-lean *doing*. Arrival / unboxing / “nights were normal” cannot score 5 (and should have failed F16/F05 already).

Pack pass: mean ≥ 4.0 across shipped angles; no dimension average < 3.5. Else Blocked even if binary gates PASS.

## Recommendation

- Gates PASS + gold pack_pass + chain PASS → recommend Ready **pending adversary**
- Else → `Blocked`

Generator may set pack Status Ready **only after** adversary `NO_MATERIAL_HITS`.
