# 03 — Angle Generation Methodology

**Version:** 1.9.0  
**Normative:** Yes  
**Depends on:** `docs/00`, `docs/01`, `docs/02` (assist: `docs/10`)  
**Validated by:** `docs/04`, `docs/05`  
**Methodology pin:** `angle-ideation-agent@1.9.0`

## 1. Goal

Translate `AngleFuel` into an Emotional Angle Pack that is:

- **Plausible** and internally consistent  
- **Distinct** across psychosocial currencies (Meta/Andromeda congruency: distinct themes)  
- **Story-complete** (Hollow, Villain, Dream, Arc, Product Fit)  
- **Mechanism-honest** (product is the door, not the hero)  
- **Observable** (every selection decision logged)

## 2. Pipeline overview

```text
[Validate inputs] → [Build AngleFuel] → [Mine candidates]
        → [Triple filter] → [Score & select 6–8]
        → [Per-angle reasoning chain] → [Draft components]
        → [Lexical preflight] → [Critic gates] → [Pack Ready] or [Revise ≤2]
```

**Agentic split (v1.4.0):** Generator drafts the pack; thin Python does lexical/schema preflight only; a separate **critic** skill owns judgment gates (`docs/04`, `docs/13`). Do not self-stamp Ready inside the generator pass without a critic report.

Maximum revise loops: **2** generator revisions on failed gate IDs only (using `P10 — Revision Loop` in `docs/08`). 
**Graceful Degradation (v1.6.3):** If the generator fails 2 revision loops, the pipeline must degrade gracefully by automatically dropping the LLM `temperature` to 0.1 and requesting a restricted generation of only 4 angles to reduce hallucination risk, rather than failing the run immediately. If this fallback fails, Status = Blocked / human review.

## 3. Preflight — Safety & Moderation Gate (v1.6.3)

Before generating candidates, `AngleFuel` must pass a zero-shot moderation check to ensure production safety and alignment.

**Checklist:**
1. **PII Leakage:** Ensure `AngleFuel` contains no real names, emails, or identifying patient data in `exact_vocabulary`.
2. **Toxicity/Brand Safety:** Ensure no unsanctioned toxic language or brand-damaging assertions exist.
3. **Policy Violations:** Ensure the product mechanism doesn't violate platform policies (e.g., prohibited medical claims).

If any check fails, the run is immediately `BLOCKED` with `SAFETY_VIOLATION`.

## 4. Stage A0 — Creative Strategy Diagnosis [v1.8.0]

Before generating angles, the agent must define the strategic parameters of the market and product using the framework in `docs/12-creative-strategy-engine.md`.
The agent outputs a **Strategy Fingerprint** determining:
- Market Sophistication (L1 to L5)
- Cultural Position (Amplifier, Subverter, Oasis, Micro-Culture)
- Primal Desire (One of the 8 evolutionary drives)
- Target Tonal Palette

This fingerprint constrains all subsequent candidate mining.

## 5. Stage A — Mine angle candidates

From AngleFuel, produce a candidate list. A candidate is a short object:

```json
{
  "candidate_id": "C01",
  "archetype": "confessional | contrarian | aspirational | curiosity | social_proof",
  "working_title": "string",
  "currency_id": "RELATIONAL_EQUITY",
  "belief_move": "prove | shift",
  "belief_statement": "string",
  "pain_refs": ["pain_points[0]"],
  "villain_seed": "string",
  "mechanism_bridge": "string",
  "confession_seed": "string",
  "assist_notes": {
    "bias_id": "BIAS_LOSS_AVERSION",
    "attach_to": "Hollow"
  }
}
```

`assist_notes` is **optional and non-normative for gates**. If present, `bias_id` must exist in [`docs/10`](10-cognitive-biases-heuristics-catalog.md), bind to fuel evidence, and follow assist binding rules (max one dominant assist per shipped angle; Core Idea must not be the bias name).

### 5.1 Mining heuristics (ordered)

1. **Strategy adherence:** Candidates must adhere to the Strategy Fingerprint established in Stage A0.
2. **Confession mining:** Prefer `exact_vocabulary` and pain examples that sound like something whispered to a friend (high emotional voltage).
3. **Failure pattern mining:** Cluster `failed_attempts` + competitor `hated` into relocatable villains (tool design, advice myths, category sameness).
4. **Identity / relationship / safety spillover:** For each functional pain (e.g. congestion), ask what secondary life system it damages (marriage, selfhood, competence, agency).
5. **Mechanism whitespace:** List mechanism traits the product uniquely owns; ask which pains those traits unlock emotionally.
6. **Currency coverage:** Ensure candidates span distinct currency IDs; drop near-duplicates early.
7. **Optional bias assist:** After fuel-bound candidates exist, optionally attach one `assist_notes.bias_id` from `docs/10` (see skill psychology protocol). Never mine from the catalog alone.
8. **Archetype diversity [v1.7.0]:** Ensure candidates span at least 2 distinct archetypes. Mine at least 1 non-confessional candidate (contrarian, aspirational, curiosity, or social_proof).
9. **Regulatory focus coverage [v1.7.0]:** Ensure at least 1 candidate is `promotion_focus` (aspirational, identity-upgrade, mastery). Not every angle should be about escaping pain.

**Hard ban:** Candidates whose only content is a feature, discount, authority flex, competitor swipe, or a bare bias/heuristic label.

## 6. Stage B — Triple filter (all must pass)

Adapted from training craft; made testable.

### Filter F1 — Emotional voltage

Ask *as the avatar*: “If I were living this, would my chest tighten? Would this feel like reading my own diary?”

| Pass | Fail |
|------|------|
| Specific event/confession energy | Generic desire (“I want healthier X”) |
| Body-level recognition possible | Abstract wellness language |

### Filter F2 — Problem → mechanism line

Ask: “Can the avatar draw a straight line from this pain to our unique fix, including why prior attempts failed?”

| Pass | Fail |
|------|------|
| Villain explains prior failure; mechanism addresses villain | Pain unrelated to mechanism |
| Product Fit can be said in one causal sentence | “It just works better” |

### Filter F3 — White space / non-saturation

Ask: “Have they already heard this *frame* a hundred times as the same story?”

| Pass | Fail |
|------|------|
| Frame is underused *or* reframed via dossier-specific confession | Commodity claim every competitor runs |
| Owns a conversation gap found in research | Pure “grow thicker / clear faster” |

Log pass/fail per candidate with one-line reasons.

## 7. Stage C — Scoring and selection

Score each surviving candidate 1–5 on:

| Dimension | 1 | 3 | 5 |
|-----------|---|---|---|
| **Emotional voltage (E)** | Flat | Mild recognition | Gut punch |
| **Mechanism alignment (M)** | Weak link | Partial | Direct unique fix |
| **White space (W)** | Saturated | Some overlap | Fresh frame |

**Priority score:** `S = E × M × W`  
(Range 1–125.)

### Selection algorithm

1. Sort by `S` descending.  
2. Greedily pick candidates with **unique `currency_id`**.  
2a. Verify ≥2 distinct archetypes are represented. If not, replace the lowest-scoring confessional with the highest-scoring non-confessional candidate.
2b. Verify ≥1 promotion_focus candidate is selected. If not, swap the lowest-scoring prevention_focus for the best promotion_focus candidate.
3. Stop at `target_angle_count` (default 8) or when next candidate would be `< 27` (i.e. worse than 3×3×3) **and** you already have `min_angle_count`.  
4. If fewer than `min_angle_count` survive, return to Stage A mining (different currency), not score inflation.  
5. Emit `selection_log` with chosen/rejected IDs and scores.

**Do not** select two angles that explore the same emotional territory under different names.

## 8. Stage D — Per-angle reasoning chain (mandatory)

For each selected candidate, answer **in writing** before drafting prose. This is the reasoning log; automation must persist it.

| # | Question | Output field |
|---|----------|--------------|
| Q0 | What **archetype** best fits this angle's emotional logic? | → Archetype ID (locked; apply `docs/01` §3) |
| Q1 | What is the **specific loss** (named, scene-level)? | → Hollow draft |
| Q2 | Who/what is the **villain** (relocatable, concrete)? | → Villain draft |
| Q3 | What does **reach** look like as one sensory moment (doing / leaning, not arrived)? | → Dream draft |
| Q4 | What **psychosocial currency** is this spending? | → Currency ID (locked; apply `docs/01` §4.1) |
| Q5 | What is the **4-beat story** (Setup/Action = fall; Twist; Verdict may doorway)? | → Story Arc draft |
| Q6 | How does the **product mechanism** resolve this hollow into this dream? | → Product Fit draft |
| Q7 | What **belief** is proved or shifted? (This *is* the unanswered Headline gap.) | → Core Idea draft |
| Q8 | What **headline** names consequence or villain in ≤12 past-tense words **without answering the gap**? | → Headline candidates (≤3) |

**Consistency checks inside the chain:**

- Villain must appear in Twist.  
- **Villain binding rule (v1.1.1 / v1.6.1):** The villain’s grammatical subject must be a concrete tool, advice line, or category flaw from `failed_attempts` / `competitors`. Never “the situation,” “the loop,” “lack of sleep,” “the blockage that never ends,” or “unfinished [X] loops” — even if a tool is named in the same sentence. Gate `A-VILLAIN` fails otherwise.  
- Product Fit must reference mechanism traits from `AngleFuel.product_fit`, not invented specs.  
- Dream must not mention the product brand as the emotional climax (product may appear only in Product Fit / light Verdict doorway).  
- **Dream render rule (v1.1.1 / v1.6.1):** Dream must include at least one concrete sensory anchor (sight, sound, place, body sensation). “Felt better / more human” alone fails `A-DREAM`. The anchor must **not** be solely the product or its chamber/cup — inspecting the mechanism is Product Fit, not Dream. That fails `A-DOOR`.  
- **Reach rule (v1.9.0):** Q3 verb is doing / leaning. Arrival, “having,” “over,” “fixed,” “nights were normal,” sleep-through-as-done fails `A-DREAM` (**F16**) before prose. Distinct from F05 (product as climax).  
- **Fall-first rule (v1.9.0):** Q5 Action cannot name the SKU or mechanism as the win. Setup/Action = the fall. Product/mechanism only in Verdict + Product Fit. Mechanism-as-Action fails `A-ARC` (**F17**).  
- **Open-loop rule (v1.9.0):** Q8 poses a gap; Q7 *is* that unanswered gap. Q6 / Product Fit is the *how* the CTA may close — not a second Core Idea. A Headline or Core Idea that contains the mechanism answer fails `H3` / `A-CORE`.  
- **Hook Cluster rule (v1.9.0):** Variants are paraphrases of the *same* gap, not new currencies or theses (**F18**).  
- Hollow must not be restated as Dream.

## 9. Stage E — Drafting rules (prose and Graceful Degradation)

For the top 6–8 candidates (or 4 if in Graceful Degradation mode), draft the components into prose.

**Feeling-first draft order (v1.9.0):** write Hollow → Headline → Dream → Arc fall → Twist → Fit (alibi last). Do not start from Product Fit and reverse-engineer feeling. Matches the VSL chain (gap → reach → fall → late mechanism).

### 7.1 Voice

- Prefer avatar first person or intimate second person consistently within an angle.  
- Prefer dossier vocabulary over marketer vocabulary.  
- Specific > clever. Clever without specificity fails gates.

### 7.2 Component length targets

Follow `docs/01` lengths. If tempted to write essays, compress; denser gold-pack style beats padded prose.

### 7.3 Product-as-door rule

Product Fit pattern:

> Because [mechanism trait], [hollow resolves] → [dream becomes possible].

Anti-pattern:

> [Product] is the best [category] with [feature list].

### 7.4 Headline drafting procedure

1. Generate 3 candidates from Q8.  
2. Apply `H1–H6` from `docs/01`.  
3. Prefer the line that maximizes consequence specificity without preamble.  
4. Record rejected headlines in pack “Headline Refinement Summary.”

## 10. Stage F — Pack assembly

1. Order angles by descending score `S` (or by narrative diversity if scores tie).  
2. Fill Summary Table.  
3. Fill Headline Rules Applied table (all true).  
4. Attach Gate Report (`docs/04`).  
5. Set Status only after all required gates pass.

## 11. Observability — required run artifacts

Every run must produce (files or structured log):

| Artifact | Purpose |
|----------|----------|
| `00b_strategy_diagnosis.json` | The Stage A0 Strategy Fingerprint |
| `01_angle_fuel.json` | Normalized fuel |
| `02_candidates.json` | All mined candidates with archetype tags |
| `03_filter_score_log.json` | F1–F3 + E/M/W + S |
| `04_reasoning_chains.json` | Q1–Q8 per selected angle |
| `05_angle_pack.md` | Final pack |
| `06_gate_report.json` | Gate IDs pass/fail + notes |

If any artifact is missing, the run is incomplete even if prose “looks good.”

## 12. Revision policy

| Failure class | Action |
|---------------|--------|
| Headline predicates | Rewrite headline only; keep chain |
| Weak Hollow/Dream | Re-answer Q1/Q3; rewrite those fields |
| Dream arrival / having (F16) | Re-answer Q3 as mid-lean *doing*; do not add product joy |
| Mechanism-in-Action (F17) | Re-answer Q5; move SKU/mechanism to Verdict + Fit |
| Hook Cluster mashup (F18) | Rewrite cluster as paraphrases of the same Headline gap |
| Villain too situational | Re-answer Q2 with concrete object from failed_attempts/competitors |
| Currency collision | Replace lower-scoring angle’s currency or swap candidate |
| Mechanism hallucination | Revert to AngleFuel.product_fit; rewrite Product Fit |
| Pack feels samey | Re-run Stage A for missing currencies; do not synonym-swap |
| Tonal monotony | Re-mine for missing archetype; do not synonym-swap existing confessionals |

## 13. Worked micro-example (pattern only)

**Fuel fragment:** failed bulb syringe (sealed, uncleanable); verbatim fear of night breathing; partner becoming “shift worker.”

| Q | Answer sketch |
|---|---------------|
| Q1 | Partnership replaced by night logistics |
| Q2 | Sealed bulb + “it’s just a phase” advice |
| Q3 | Same kitchen, same person, quiet morning (leaning — not “nights were normal”) |
| Q4 | `RELATIONAL_EQUITY` |
| Q5 | Happy couple → failed bulb/steam (fall) → wrong enemy (tool/advice) → doorway, not “then we slept” |
| Q6 | Clearable/visible mechanism ends congestion fights that were misread as relationship failure |
| Q7 | Congestion isn’t only stealing sleep — it’s stealing the marriage |
| Q8 | “My husband almost left because our baby couldn’t breathe.” |

This mirrors gold-pack *structure*, not a license to copy gold-pack text into unrelated niches.

## 14. Automation mapping (v1.5.0 agentic)

| Methodology stage | Owner |
|-------------------|-------|
| Scenario router → draft pack | Generator skill `angle-ideation` |
| Assist fields | `awareness_stage`, `test_priority`, Testing order table (`docs/01`) |
| Lexical / skeleton checks | Preflight scripts (`validate_headlines.py`, `validate_pack_preflight.py`) |
| Judgment gates + Ready stamp | Critic skill `angle-gate-critic` (few-shot F01–F18 + pairwise P-DISTINCT) |
| Revise on FAIL (≤2) | Generator, scoped to failed gate IDs (`§10`) |
| Negative control | `runs/20260814-negcontrol-feature/` must stay Blocked |

Canonical architecture: `docs/13-agentic-gate-protocol.md`. Do not collapse generator + critic into one opaque prompt; collapsed prompts destroy observability and honesty.
