# 04 — Quality Gates

**Version:** 1.9.0  
**Normative:** Yes  
**Rule:** Pack Status may be `Ready for Pre-Lander Agent` only if **chain judge PASS**, **all required gates PASS**, **gold-class pack_pass**, and **adversary material_hits empty**.
**Methodology pin:** `angle-ideation-agent@1.9.0`

## 1. How to run gates

**Owner (v1.6.0):** Chain + pack judgment = **critic**. Failure hunting = **red-team**. Lexical scripts never Ready. Generator never authors `06_*` / `07_*`. See `docs/13`.

1. Critic Pass A: chain-judge `04` → `06_chain_judge.json` (before `05`).  
2. Lexical preflight on `05`.  
3. Critic Pass B: gates in ID order → `06_gate_report.json` + `06_gold_scores.json`.  
4. Red-team → `07_adversary.json`.  
5. Evidence: quote ≤25 words. Missing evidence → FAIL `CRITIC_NO_EVIDENCE`.  
6. Adversary hits while critic said Ready → FAIL `CRITIC_ADVERSARY_DISAGREE`.

## 2. Input validation gates

| ID | Gate | Required | Pass criterion |
|----|------|----------|----------------|
| `I-AVATAR` | Avatar present | Yes | Scenario B field or fuel.avatar.description non-empty & specific |
| `I-PRODUCT` | Product present | Yes | Product description/mechanism present |
| `I-PROBLEM` | Problem present | Yes | Problem statement or evidenced core problem |
| `I-FUEL` | AngleFuel valid | Yes | Schema populated; `product_fit.mechanism` not `UNKNOWN` |
| `I-VOICE` | Avatar voice | Yes | ≥5 multi-word vocabulary items OR evidenced quotes mapped |
| `I-BRIEF` | Mini-brief quality | Scenario B only | All `MB1–MB8` from `docs/02` |

## 3. Headline gates (per angle)

| ID | Gate | Pass criterion |
|----|------|----------------|
| `H1` | Word budget | ≤12 words |
| `H2` | Past consequence | Past / past-perfect framing of event or discovery |
| `H3` | Stake named | Consequence or villain named; Headline **opens** the gap and does **not** contain the mechanism answer / “and then we slept” close |
| `H4` | No product | No product/brand token |
| `H5` | No weak preamble | First three tokens not in `docs/01` §5.1 reject list; stake without throat-clear |
| `H6` | Confessable | Passes `docs/01` §5.2 checklist; zero ad-ese ban tokens |

## 4. Angle component gates (per angle)

| ID | Gate | Pass criterion | Fail examples |
|----|------|----------------|---------------|
| `A-CURRENCY` | Currency set | Exactly one allowed Currency ID | “Fear + guilt mix” |
| `A-CORE` | Core idea | One sentence; core friction + escalation; belief move clear; **is the unanswered Headline gap** (not a second thesis, not the mechanism answer) | Feature claim; Core Idea restates Product Fit |
| `A-HOLLOW` | Hollow specificity | Named loss in a scene; not mood-only | “She was exhausted and sad” |
| `A-VILLAIN` | Villain concreteness | **Required for ALL archetypes.** Specific thing/advice/tool/category flaw as the **subject**; not “the loop/situation/lack of sleep/unfinished loops/blockage that never ends” even with a tool nearby | “Parenthood is hard”; “the night loop”; “unfinished clear-out loops” |
| `A-DREAM` | Dream rendered | Sensory *reach* (doing / leaning) with ≥1 concrete anchor; not benefit summary; **not arrival** (“it was over”, “nights were normal”, problem gone) | “Life got better”; “felt more human” alone; “She finally slept through; it was over.” |
| `A-ARC` | Four beats | Setup, Action, Twist, Verdict all present. **Action = fall** (failed attempts). Product/mechanism only in Verdict + Product Fit | Twist missing; Action is a feature win |
| `A-FIT` | Product fit | Causal bridge from mechanism → this hollow/dream | Generic praise |
| `A-DOOR` | Product as door | Product is not the emotional climax of Dream | Dream is unboxing joy; Dream peak is inspecting the cup/chamber |
| `A-BELIEF` | Belief grounded | Belief proved/shifted appears in fuel held/ready_to_shift or evidenced pains | Invented cosmology |
| `A-VOICE` | Voice match | Uses register consistent with fuel vocabulary | Corporate tone |

## 5. Pack-level gates

| ID | Gate | Pass criterion |
|----|------|----------------|
| `P-COUNT` | Count | 6–8 angles (or explicit Blocked with reason if research cannot support 6) |
| `P-DISTINCT` | Distinct territories | Unique Currency IDs **and** pairwise hollows are not noun-swapped synonyms (Andromeda same-concept) |
| `P-FEELS-REAL` | Realism | Passes §5.1 realism checklist |
| `P-CONSISTENCY` | Internal consistency | Mechanisms, villains, and product claims don’t contradict fuel |
| `P-ARTIFACTS` | Observability | Reasoning chains + score log exist for every shipped angle |
| `P-HEADLINES-TABLE` | Headline rules table | Present and accurate |
| `P-SUMMARY` | Summary table | Present; matches body |
| `P-CURRENCY-RULES` | Disambiguation | Near-collision currencies obey `docs/01` §4.1 |
| `P-CHAIN-JUDGE` | Chain before prose | `06_chain_judge.json` PASS |
| `P-GOLD` | Gold-class scores | `06_gold_scores.json` pack_pass (mean ≥ 4.0; no dim avg < 3.5) |
| `P-ADVERSARY` | Red-team clean | `07_adversary.json` material_hits empty |
| `P-ARCHETYPE-DIVERSITY` | Archetype diversity | ≥2 distinct archetypes used across pack angles, but ALL must adhere to core DR rules (Past-tense headlines, Hollow/Villain mandatory) |
| `P-HEADLINE-DIVERSITY` | Headline format diversity | ≥2 distinct syntactic structures across headlines, but ALL must remain strictly past-tense. |
| `P-AWARENESS-DIVERSITY` | Awareness stage diversity | ≥1 angle at `solution_aware` or `product_aware` |
| `P-PROMOTION` | Regulatory focus diversity | ≥1 angle tagged `promotion_focus` (aspirational/identity-upgrade framing) |
| `P-BIAS-ACTIVATION` | Bias assist activation | ≥3 angles carry explicit `assist_notes.bias_id` from docs/10 catalog |

### 5.1 P-FEELS-REAL checklist (all required)

1. ≥3 angles contain a multi-word echo from fuel `exact_vocabulary` (stem match OK).  
2. Zero angles read as feature sheets if product name is removed.  
3. Cold reader can name each angle’s villain object in ≤6 words.  
4. No pack-wide repeated metaphor that makes angles feel like synonyms.  
5. Failed attempts in arcs match fuel `failed_attempts` / competitor hates (no exotic villains from nowhere).
6. Pack contains angles at different emotional intensities — not all at maximum gut-punch level.

## 6. Automatic lexical checks (assistive)

These do not replace human/LLM judgment but catch cheap errors:

- Product name / brand string search in all headlines → fail `H4`  
- Currency ID uniqueness → fail `P-DISTINCT`  
- Word count per headline → fail `H1`  
- Dream contains product name as subject of the emotional peak → fail `A-DOOR`  
- Hollow shares >60% token overlap with Dream → fail rewrite (hollow≠dream)

## 7. Gate report schema

```json
{
  "run_id": "string",
  "methodology": "angle-ideation-agent@1.9.0",
  "critic": "angle-gate-critic@1.9.0",
  "pack_status_recommendation": "Ready for Pre-Lander Agent | Blocked",
  "gates": [
    {
      "gate_id": "H1",
      "scope": "angle:3",
      "result": "PASS",
      "evidence": "word_count=9",
      "notes": ""
    }
  ],
  "cold_reread": {
    "completed": true,
    "failures_found": []
  },
  "preflight": {
    "validate_headlines": "PASS|FAIL",
    "validate_pack_preflight": "PASS|FAIL"
  }
}

Machine schema: `schemas/gate_report.schema.json`.
```

## 8. Mapping from specification quality checklist

| Specification checklist item | Gate IDs |
|---------------------------|----------|
| Avatar / product / problem present | `I-AVATAR`, `I-PRODUCT`, `I-PROBLEM` |
| Mini-brief plausible + voice | `I-BRIEF`, `I-VOICE` |
| Headline rules | `H1`–`H6` |
| Distinct currency | `A-CURRENCY`, `P-DISTINCT` |
| Hollow / Villain / Dream / Arc / Fit quality | `A-HOLLOW`, `A-VILLAIN`, `A-DREAM`, `A-ARC`, `A-FIT` |
| 6–8 angles | `P-COUNT` |
| Feels like real stories | `P-FEELS-REAL` |
| Product as door | `A-DOOR` |
| Archetype diversity | `P-ARCHETYPE-DIVERSITY` |
| Headline variety | `P-HEADLINE-DIVERSITY` |
| Funnel coverage | `P-AWARENESS-DIVERSITY` |
| Bias utilization | `P-BIAS-ACTIVATION` |

## 9. Failure catalog (annotated negatives)

Use these as unit tests: methodology/gates **must reject**. F01–F12 = original failure classes. F13–F15 = pack diversity. **F16–F18 = VSL doctrine** (Dream = reach, fall-first Action, one-gap Hook Cluster).

| ID | Bad fragment | Why it fails | Gate IDs |
|----|--------------|--------------|----------|
| F01 | Core Idea: “Hospital-grade suction clears mucus in seconds.” | Claim/feature, no core friction | `A-CORE` |
| F02 | Hollow: “She was exhausted and everything felt so heavy.” | Mood-only, no named scene loss | `A-HOLLOW` |
| F03 | Villain: “The situation where sleep never came.” | Abstract situation, not relocatable | `A-VILLAIN` |
| F04 | Villain: “The bulb syringe had a slight design issue.” | Too soft, doesn't carry the blame | `A-VILLAIN` |
| F05 | Dream: “She opened the Baby Bubble box and smiled at the parts.” | Product-joy / arrival, not user reach | `A-DOOR` |
| F06 | Hollow: Two angles describe identical partner resentment with synonyms | Duplicate core concept | `P-DISTINCT` |
| F07 | Headline: “At 3 a.m., I realized the bulb syringe was failing.” | Banned time-setting preamble | `H5` |
| F08 | Headline: “Baby Bubble changed our entire nighttime routine.” | Product name in headline | `H1` |
| F09 | Headline: “The hospital-grade secret that saved our nights.” | Ad-ese buzzwords | `H6` |
| F10 | Arc: Twist reveals the product instead of the mechanism/villain | Premature pitch | `A-ARC` |
| F11 | Physical risk written as tool betrayal (or reverse) without primary-friction test | Currency misfile | `P-CURRENCY-RULES` |
| F12 | Offer-as-angle: “20% off the aspirator moms swear by.” | Offer + social proof, not angle | non-angle (`docs/01` §1.1), `A-CORE` |
| F13 | All 6 angles are confessional gut-punch at intensity 5 | Tonal monotony; audience fatigue on same frequency | `P-ARCHETYPE-DIVERSITY` |
| F14 | All headlines follow "I [verb] [location] [feeling]" pattern | Headline homogeneity; reduces testing matrix value | `P-HEADLINE-DIVERSITY` |
| F15 | All angles tagged `problem_aware` | Funnel flatness; no mid/bottom funnel coverage | `P-AWARENESS-DIVERSITY` |
| F16 | Dream: “She finally slept through; it was over.” / “Nights were normal again.” | Arrival / having — SEEKING collapse; VSL has nothing left to lean toward | `A-DREAM` |
| F17 | Arc Action: “Tried the cup → mucus visible → slept” with no fall | Mechanism as the Action win; fall-first violated | `A-ARC` |
| F18 | Hook Cluster: mould hook + 911 hook + “20% off” | Competing theses / currencies in one spine | Hook Cluster (`docs/01` §4.3), `A-CORE` |
