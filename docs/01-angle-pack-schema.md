# 01 — Angle Pack Schema

**Version:** 1.9.0
**Normative:** Yes
**Methodology pin:** `angle-ideation-agent@1.9.0`

## 1. What an angle is

**Definition (operational):** An angle is a **belief-shifting (or belief-proving) frame** that the entire creative/pre-lander story is built on. It is the foundation, not the decoration.

Formally, a valid angle must simultaneously specify:

1. **Emotional register** (psychosocial currency) — the core consumer friction or aspiration it addresses  
2. **Belief move** — prove a held belief *or* shift a ready-to-accept belief  
3. **Named loss / friction** (Hollow) — concrete, scene-level tension  
4. **Relocatable obstacle** (Villain) — a specific tool, conventional habit, or flawed assumption (not “life is hard”)  
5. **Rendered reach** (Dream) — sensory *doing / leaning*, not arrival or a benefit summary  
6. **Causal bridge** (Product Fit) — how *this* product resolves *this* tension  

If any of (1)–(6) is missing or generic, it is not shippable as an angle.

### 1.1 What an angle is *not*

| Not an angle | Why | Example |
|--------------|-----|---------|
| Hook | Attention device; can serve many angles | “Don’t scroll.” |
| Claim | Assertion without emotional frame | “Clears congestion in 60 seconds.” |
| Feature | Product attribute | “Transparent collection cup.” |
| Offer | Commercial terms | “20% off today.” |
| Ad concept | Creative *execution* of an angle (UGC vs doctor vs listicle) | “Mom films bathroom night routine.” |
| Competitor template | Copied structure from another brand’s winning ad | Swiped script with nouns swapped |
| Benefit list | Outcome stack without belief move | “Sleep better, feed better, less stress.” |

**Test:** If removing the product name still leaves a coherent emotional story with a villain and a hollow, you likely have an angle. If what remains is a feature sheet, you do not.

## 2. Pack document structure

Emit markdown matching this skeleton (field order is mandatory):

```markdown
# Emotional Angle Pack — [Product Name]

**Version:** v1.0
**Date:** [ISO date]
**Methodology:** angle-ideation-agent@1.9.0
**Status:** Ready for Pre-Lander Agent | Blocked
**Contains:** [N] angles
**Scenario:** A | B
**Run ID:** [opaque id]
**Style Controls:** Intensity [N], Darkness [N], Formality [N], Distance [N]
**Trace ID:** [opaque id]
**Model:** [model_version]
**Temperature:** [0.0 - 2.0]
**Tokens In/Out:** [N] / [N]

**Inference ceiling:** EVIDENCED | PLAUSIBLE_INFERENCE (Scenario B required)

---


## Headline Rules Applied

| Rule ID | Rule | Pass? |
|---------|------|-------|

---

## Angle Component Definitions

[Short definitions — copy from §3]

---

## Angles

### 1. The [Angle Name] Angle
...

---

## Summary Table

| # | Angle Name | Currency | Headline |
|---|------------|----------|----------|

---

## Testing order

| Priority | # | Angle Name | Awareness stage | S (E×M×W) |
|----------|---|------------|-----------------|-----------|

(Priority 1 = test first as a distinct concept. Assist only — not ads.)

---

## Headline Refinement Summary

[Why these headlines; what was rejected]

---

## Gate Report

[See docs/04 — required before Status = Ready]
```

## 3. Angle archetypes [v1.7.0]

Not every angle must follow the same emotional contour. The **archetype** defines the structural template an angle uses. As this is a strict Direct Response pipeline, **ALL archetypes must use past-tense headlines** and **ALL archetypes must use the Hollow and Villain components**.

| Archetype ID | Label | Structure | When to use | Hollow req? | Villain req? |
|-------------|-------|-----------|-------------|-------------|-------------|
| `confessional` | Confessional | Hollow → Villain → Dream | DTC problem-solution, health, wellness, high-pain categories | **Yes** | **Yes** |
| `contrarian` | Contrarian / Reframe | Held belief → Evidence it's wrong → New frame | Education, expertise, authority-challenging | **Yes** | **Yes** |
| `aspirational` | Aspirational / Identity | Current self → Desired self → Bridge | Luxury, lifestyle, identity-upgrade, positive-pursuit | **Yes** | **Yes** |
| `curiosity` | Curiosity / Open-Loop | Surprising fact → "Wait, what?" → Reveal | Viral, shareable, top-of-funnel engagement | **Yes** | **Yes** |
| `social_proof` | Social Proof / Belonging | Outsider → Discovery → Tribe | Community products, subscriptions, movements | **Yes** | **Yes** |

### 3.0.1 Archetype-specific field definitions

| Field | Replaces | Used by archetypes | Definition |
|-------|----------|-------------------|------------|
| **The Hollow** | — | All archetypes (required) | Specific named loss in a scene |
| **The Villain** | — | All archetypes (required) | Concrete relocatable blame object |
| **The Dream** | — | All archetypes (required) | Sensory *reach* (doing / leaning), not arrival |

### 3.0.2 Regulatory focus tag [v1.7.0]

Every angle must carry a regulatory focus tag from Higgins' Regulatory Focus Theory:

| Tag | Definition | Typical archetypes |
|-----|-----------|-------------------|
| `prevention_focus` | Angle frames the product as resolving a core friction, risk, or frustration | `confessional`, `contrarian` |
| `promotion_focus` | Angle frames the product as enabling a gain, aspiration, or identity upgrade | `aspirational`, `curiosity`, `social_proof` |

**Pack rule:** At least 1 angle per pack must be `promotion_focus`. This prevents tonal monotony.

### 3.0.3 Pack archetype diversity rule [v1.7.0]

**Pack rule:** A pack must contain angles from **≥2 distinct archetypes**. A pack of 6 confessional angles fails `P-ARCHETYPE-DIVERSITY`. Recommended mix for a 6-angle pack:
- 2–3 confessional
- 1 contrarian
- 1 aspirational or curiosity
- 1 of any type

## 4. Per-angle required components

| Component | Cardinality | Constraints | Failure modes |
|-----------|-------------|-------------|----------------|
| **Archetype** | exactly 1 | From allowed set (§3) | Missing or unlisted archetype |
| **Strategy Fingerprint** | exactly 1 | 4-part string (Sophistication, Culture, Primal, Tone) | Missing or invalid |
| **Angle Name** | 1 | Short label (“Relationship”, “Betrayal”) | Vague (“Emotional Angle 3”) |
| **Psychosocial Currency** | exactly 1 | From allowed set (§5); unique within pack | Duplicate currency / vague blend |
| **Core Idea** | 1 sentence | Names the core friction/aspiration + escalation | Feature claim; multi-thesis sentence |
| **Headline** | 1–2 lines | §6 headline predicates | Product name; preamble; mechanism answer / “then we slept” close |
| **The Hollow** | exactly 1 | 2-3 sentences. Mandatory for all angles. | “She felt sad / stressed” |
| **The Villain** | exactly 1 | 2-3 sentences. Mandatory for all angles. | “Parenthood”, “society”, “stress” |
| **The Dream** | 1–2 sentences | Sensory *reach* (doing / leaning), not arrival | Abstract (“finally happy again”); “nights were normal”; problem gone |
| **Story Arc** | 2–4 sentences | Beats vary by archetype (see §4.2) | Missing twist or verdict |
| **Product Fit** | 1–2 sentences | Product resolves hollow → dream | Generic “our product helps” |
| **Regulatory focus** (assist) | 1 | `prevention_focus` \| `promotion_focus` | Missing |
| **Awareness stage** (assist) | 1 | `problem_aware` \| `solution_aware` \| `product_aware` | All angles same stage |
| **Test priority** (assist) | 1 | Integer 1–8 from `S = E×M×W` rank | Random order |
| **Bias assist** (assist) | 0–1 | `bias_id` from `docs/10`; ≥3 per pack total | Bias salad or none used |

### 4.1 Component definitions (canonical)

- **Archetype:** The structural template governing this angle's emotional contour (§3).
- **Strategy Fingerprint:** The specific strategic parameters from `docs/12` (Sophistication, Cultural Position, Primal Desire, Tone) guiding this angle.
- **Psychosocial Currency:** The emotional register the angle spends against (what the avatar is looking to protect, resolve, or achieve).
- **Core Idea:** The one-sentence core insight / belief move the angle exists to explore. It **is** the unanswered Headline gap — not a second thesis and not the Product Fit answer.
- **Headline:** Past tense. Under 12 words. Names consequence or villain. No product name. **Opens** a loop; must not contain the mechanism answer or a “then we slept” close (`H3`).
- **Hollow:** The specific loss *inside the scene*, not mood adjectives.
- **Villain:** Where blame is relocated. Must be a concrete mechanism, tool, advice pattern, or category flaw.
- **Dream:** One moment of *reach* the avatar can almost see/hear/feel — doing / leaning, not having / “it was over.” Not a benefit list. Not product climax (`A-DOOR`).
- **Story Arc:** Mini-narrative with beats appropriate to archetype (§4.2).
- **Product Fit:** How the product’s mechanism opens the door from hollow → dream for *this* angle only. Should address both *why it works* (mechanism) and *how easy it is* (ability).
- **Regulatory focus (assist):** Higgins-style tag. `prevention_focus` = escaping loss; `promotion_focus` = pursuing gain.
- **Awareness stage (assist):** Schwartz-style traffic tag for downstream. Pack must include ≥1 angle at `solution_aware` or `product_aware`.
- **Test priority (assist):** Rank for *concept* testing order from existing scores.
- **Bias assist (assist):** Optional `bias_id` from `docs/10`. ≥3 per pack required for `P-BIAS-ACTIVATION`.

### 4.2 Story arc beats by archetype [v1.7.0]

| Archetype | Beat 1 | Beat 2 | Beat 3 | Beat 4 |
|-----------|--------|--------|--------|--------|
| `confessional` | **Setup** — Pre-crisis identity | **Action** — Failed attempts | **Twist** — Villain revealed | **Verdict** — Product as door |
| `contrarian` | **Consensus** — What everyone believes | **Evidence** — Why that's wrong | **Reframe** — The real cause | **Verdict** — New understanding + product |
| `aspirational` | **Current** — Where you are now | **Vision** — Who you could become | **Villain** — What's been in the way | **Bridge** — Product enables the leap |
| `curiosity` | **Hook** — Surprising/counterintuitive fact | **Tension** — “Wait, but then why...” | **Reveal** — The hidden mechanism | **Implication** — What this means for you |
| `social_proof` | **Outsider** — Feeling alone in the struggle | **Discovery** — Others went through this | **Tribe** — The community that formed | **Belonging** — You're one of us + product |

### 4.3 Variants (Micro-formats) [v1.6.2]

Each angle must also include structural variants for downstream IDE consumption:
- **Compressed Story:** Short, 2-beat arc + Hollow + Product Fit (e.g., for email copy).
- **Hook Cluster:** 3–5 short headlines that are **paraphrases of the same Core Idea / Headline gap** for rapid ad testing. New currencies, offers, or a second thesis fail **F18**.
- **Objection Flip:** The core idea + named objection + reversal moment (FAQ style).

### 4.4 Per-angle markdown (assist lines)

After Product Fit, emit the assist tags and variants:

```markdown
**Archetype:** confessional
**Strategy Fingerprint:** L3 | The Subverter | Freedom from pain | Clinical
**Regulatory focus:** prevention_focus
**Awareness stage:** problem_aware
**Test priority:** 1
**Bias assist:** BIAS_LOSS_AVERSION → Hollow

**Variants:**
- **Compressed Story:** [Text]
- **Hook Cluster:**
  - [Hook 1]
  - [Hook 2]
  - [Hook 3]
- **Objection Flip:** [Text]
```

## 5. Allowed psychosocial currencies

Use these labels exactly (aliases in parentheses are for mapping only):

### 5.1 Prevention-focused currencies (friction/relief)

| Currency ID | Label | Typical friction / dilemma |
|-------------|-------|----------------------------|
| `RELATIONAL_EQUITY` | Relational Equity | Partnership eroded into logistics |
| `IDENTITY_SELFHOOD` | Identity / Selfhood | “I don’t recognize myself” |
| `SAFETY_SECURITY` | Safety / Security | Concern over unaddressed physical discomfort or risk |
| `TRUST_SAFETY` | Trust / Safety | Trusted tool/advice betrays or fails silently |
| `SOCIAL_STATUS` | Social Status / Competence | Public embarrassment / looking incompetent |
| `AGENCY_CONTROL` | Agency / Control | Tried everything; feeling powerless |
| `GUILT_REGRET` | Guilt / Regret | Self-blame for preventable mistakes |
| `BODILY_AUTONOMY` | Bodily Autonomy | Loss of bodily ownership / forced discomfort with tool |
| `GENTLENESS` | Gentleness | Forced to be rough / clumsy to help |
| `AUTHORITY` | Authority | Loss of knowing what to do / contradictory advice |
| `FUTURE_SECURITY` | Future Security | Concern over long-term habit / milestone disruption |
| `AGENCY_PARTNERSHIP` | Agency / Partnership | Care routine isn’t shareable; solo burden |

### 5.2 Promotion-focused currencies (aspiration/gain) [v1.7.0]

| Currency ID | Label | Typical aspiration |
|-------------|-------|-------------------|
| `MASTERY` | Mastery / Competence | Becoming skilled, knowledgeable, capable in a domain |
| `BELONGING` | Belonging / Community | Being part of a group that gets it; not alone |
| `DELIGHT` | Delight / Joy | The simple pleasure of something working beautifully |
| `SELF_ACTUALIZATION` | Self-Actualization | Becoming the version of yourself you've always wanted to be |
| `FREEDOM` | Freedom / Liberation | Gaining back time, mobility, or bandwidth |

### 5.3 Currency usage rules

**Pack rule:** No two angles may share the same Currency ID. Prefer 6–8 angles. If research cannot support 6 distinct currencies without fabrication, emit fewer and set Status = `Blocked` with reason `INSUFFICIENT_DISTINCT_CURRENCIES` *or* gather more fuel — never fake a currency.

**Focus mix rule [v1.7.0]:** A pack may use currencies from both §5.1 and §5.2. At least 1 angle should use a promotion-focused currency when the product category supports aspiration (most consumer products do). Prevention-only packs are permitted only when explicitly justified by the avatar’s awareness stage (e.g., acute medical/safety contexts).

### 5.4 Currency disambiguation (pairwise)

When two currencies could apply, pick using the **primary friction**, not secondary spillover.

| Pair | Choose A when | Choose B when | Forced-fail (wrong pick) |
|------|---------------|---------------|--------------------------|
| `SAFETY_SECURITY` vs `TRUST_SAFETY` | Concern over **unaddressed physical discomfort or risk** (under/over-reacting) | A **trusted tool/advice** actively betrays (mould, false reassurance, hidden chamber) | Calling mould-in-bulb “medical concern” without betrayal of trust |
| `AGENCY_CONTROL` vs `AGENCY_PARTNERSHIP` | “I tried everything / bought four versions / control is gone” (solo competence collapse) | Help exists but **cannot be handed off**; isolation inside the couple | Framing mouth-tube disgust as “tried everything shopping” |
| `AGENCY_PARTNERSHIP` vs `BODILY_AUTONOMY` | The loss is **shared caregiving / handoff** | The loss is **body boundary / forced intimate contact** with the tool | Using bodily autonomy when the beat is “I said no when he offered to help” *only* as partnership isolation |
| `GUILT_REGRET` vs `IDENTITY_SELFHOOD` | “I am a bad parent / I should have known” (moral self-blame) | “I don’t recognise who I am” (self erased), even if guilt co-occurs | Identity angle that never leaves the mirror and only moralizes |
| `SOCIAL_STATUS` vs `GENTLENESS` | Audience / public competence failure | Forced to be rough/cruel to help, even alone | Social angle with no witness/audience pressure |
| `AUTHORITY` vs `SAFETY_SECURITY` | Loss of **knowing what to do** / expertise collapse | Fear of **physical risk** outcome | Authority angle that is only physical risk with no know-how hollow |
| `FUTURE_SECURITY` vs `SAFETY_SECURITY` | Milestone / future disruption (recurring habit, long-term impact) | Immediate tonight tension | Future angle that is only tonight’s acute issue |

If still ambiguous: prefer the currency whose Hollow sentence remains true after deleting the other friction's nouns.

## 6. Headline predicates (machine-checkable)

A headline **passes** only if all are true:

| ID | Predicate |
|----|-----------|
| `H1` | Word count ≤ 12 (whitespace-separated tokens) |
| `H2` | Primary tense is past (or past-perfect consequence); not a present-tense pitch. All archetypes must use past-tense headlines. |
| `H3` | Names a **consequence** or **villain** (not only a vague feeling). Opens the gap; does **not** contain the mechanism answer or a “then we slept” close |
| `H4` | Contains no product/brand name |
| `H5` | First three tokens are **not** in the preamble reject list below; stake appears in the line without a time-setting throat-clear |
| `H6` | Passes confessable checklist (§6.1) |
| `H7` | **Pack-level [v1.7.0]:** ≥2 distinct syntactic headline structures across the pack (e.g., not all "I [verb] [location]") |

### 6.1 H5 reject openings (case-insensitive)

Reject if headline **starts with** any of:

`At `, `At 3`, `For weeks`, `For months`, `For days`, `When I`, `After I`, `Before I`, `One night,`, `Last night,`, `Today,`, `Tonight,`, `Suddenly,`, `Finally,`

Prefer consequence-first, villain-first, or curiosity-first openings.

### 6.2 H6 confessable checklist (all required)

1. Could be said aloud to a friend without sounding like an ad read.  
2. Contains at least one **concrete noun** from the scene (person, tool, body part, place) — not only abstractions ("struggle", "journey", "wellness").  
3. Contains **zero** ad-ese ban tokens (case-insensitive whole-word / phrase): `game-changer`, `hack`, `must-have`, `literally obsessed`, `link in bio`, `hospital-grade` (in headline), `miracle`, `secret trick`, `order now`.  
4. Prefer ≥1 echo of fuel `exact_vocabulary` stem when available (soft preference; hard-fail only if voice is corporate).

### 6.3 Headline format examples by archetype [v1.7.0]

| Archetype | Format | Example |
|-----------|--------|---------|
| `confessional` | Past-tense confession: "I [verb] [scene]" | *I sat on the bathroom floor wishing I never got a puppy.* |
| `contrarian` | Villain-forward declaration: "[Authority/tool] [past-tense action]" | *Your dog trainer made separation anxiety worse.* |
| `curiosity` | Open-loop: "The moment [surprising claim]" | *The moment I realized puppy screams had nothing to do with training.* |
| `aspirational` | Future-self moment: "[Positive identity shift]" | *The morning I stopped dreading the front door.* |
| `social_proof` | Tribe statement: "[Shared past experience]" | *When every first-time puppy owner felt this at 3 AM.* |

## 7. Story arc beats

| Beat | Function | Must include |
|------|----------|--------------|
| **Setup** | Who they were / baseline | Relatable pre-crisis identity |
| **Action** | What they tried — **the fall** | Failed attempts or trusted ritual. **Must not** name the SKU or mechanism as the win (**F17**) |
| **Twist** | Reframe | Villain revealed / wrong enemy named |
| **Verdict** | New belief + doorway | Why the product mechanism now makes sense — mechanism belongs here, not in Action |

## 8. JSON mirror (for future automation)

```json
{
  "pack": {
    "product_name": "string",
    "version": "v1.0",
    "date": "YYYY-MM-DD",
    "methodology": "angle-ideation-agent@1.9.0",
    "status": "Ready for Pre-Lander Agent | Blocked",
    "scenario": "A | B",
    "run_id": "string",
    "angles": [
      {
        "ordinal": 1,
        "name": "string",
        "currency_id": "RELATIONAL_EQUITY",
        "core_idea": "string",
        "headline": "string",
        "hollow": "string",
        "villain": "string",
        "dream": "string",
        "story_arc": "string",
        "product_fit": "string",
        "awareness_stage": "problem_aware | solution_aware | product_aware",
        "test_priority": 1
      }
    ]
  }
}
```

Markdown remains the human handoff format; JSON is the automation mirror. Both must validate against the same predicates.
