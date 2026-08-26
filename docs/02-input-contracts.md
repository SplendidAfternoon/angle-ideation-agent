# 02 — Input Contracts and AngleFuel

**Version:** 1.9.0  
**Normative:** Yes
**Methodology pin:** `angle-ideation-agent@1.9.0`

## 1. Decision tree (deterministic)

```
Has a detailed research dossier available?
│
├─ YES → Scenario A
│         1. Validate dossier minimum (§3)
│         2. Map dossier → AngleFuel (§5) with EVIDENCED/DERIVED labels
│         3. Do NOT run mini-brief generation
│
└─ NO  → Scenario B
          1. Validate thin fields (§2) — fail closed if any required missing
          2. Run Mini-Research Brief master prompt (§4)
          3. Validate mini-brief (§4.2)
          4. Treat mini-brief JSON as AngleFuel (label PLAUSIBLE_INFERENCE)
```

**Rule:** Never mix “half dossier + invented mini-brief” without labeling. If a dossier exists but is incomplete, either (a) map what is evidenced and mark gaps `UNKNOWN`, or (b) fall back to Scenario B *only* after human confirmation.

## 2. Scenario B — thin input contract

### 2.1 Required fields

| Field | Type | Example | Reject if |
|-------|------|---------|-----------|
| `avatar_description` | non-empty string | “Mothers of newborns struggling with congestion” | Missing, placeholder (“TBD”), or demographic-only with no struggle |
| `product_description` | non-empty string | “A nasal aspirator with a clear collection cup” | Missing; brand name alone without mechanism hints |
| `problem_statement` | non-empty string | “Baby nasal congestion prevents sleep and feeding” | Missing; product pitch disguised as problem |

### 2.2 Optional fields

| Field | Type | Use |
|-------|------|-----|
| `competitor_names` | string[] | Seeds competitor dislike/love mining in mini-brief |
| `product_name` | string | For pack title / Product Fit naming |
| `constraints` | string | Legal/tone limits (never overrides gates) |

### 2.3 Fail-closed response

If any required field is missing, **stop**. Emit:

```json
{
  "status": "BLOCKED",
  "reason_code": "MISSING_REQUIRED_INPUT",
  "missing_fields": ["avatar_description"]
}
```

Do not generate angles. Do not “assume reasonable defaults.”

## 3. Scenario A — dossier minimum

A dossier is acceptable if it contains **enough fuel** to populate AngleFuel without fabrication. Minimum viable set:

| Fuel need | Acceptable evidence |
|-----------|---------------------|
| Avatar psychographics | Who they are + life stage + emotional state |
| Pain clusters | ≥3 distinct pains with concrete descriptions or quotes |
| Failed attempts | ≥2 tried solutions + why they failed / are hated |
| Voice | ≥5 multi-word verbatim phrases *or* clearly labeled derived voice |
| Product mechanism | How the product works + how it addresses the core problem |
| Competitor landscape | Named alternatives with at least hated traits *or* category flaws |

**Canonical example structure** (Comprehensive avatar dossier pattern): base avatar → emotional condition → pain drivers → verbatim voices → awareness levels → market sophistication → loved/hated competitor traits → mechanism implications.

Incomplete dossiers: map what exists; set `UNKNOWN` on gaps; if `product_fit.mechanism` is `UNKNOWN`, Status cannot become Ready.

## 4. Mini-Research Brief (Scenario B only)

### 4.1 Master prompt (verbatim contract)

Use the standard master prompt with fields substituted. Do not alter output schema keys.

**Output keys (required):**

- `avatar` (`name`, `description`)
- `pain_points[]` (`cluster`, `description`, `examples[]`)
- `failed_attempts[]` (`attempt`, `why_it_failed`)
- `emotional_effects[]`
- `exact_vocabulary[]` (multi-word phrases)
- `future_fears[]`
- `product_fit` (`mechanism`, `how_it_resolves`)
- `competitors[]` (`name`, `loved`, `hated`)
- `psychosocial_currencies[]` (`currency`, `why_it_applies`)

### 4.2 Mini-brief validation gates

| ID | Check |
|----|-------|
| `MB1` | JSON parses; all required keys present |
| `MB2` | Avatar description is specific (not “busy moms who want better”) |
| `MB3` | ≥3 pain points; each has ≥1 concrete example phrase |
| `MB4` | ≥2 failed attempts with distinct failure modes |
| `MB5` | Vocabulary entries are multi-word, avatar-voice |
| `MB6` | Product fit mechanism is concrete and tied to problem |
| `MB7` | Internal consistency: mechanism can plausibly address named pains |
| `MB8` | No fabricated URLs; if a source is cited it must be real *or* removed |

On any MB fail → revise mini-brief once; if still failing → `BLOCKED` / `MINI_BRIEF_QUALITY`.

## 5. AngleFuel — canonical intermediate

All paths converge on **AngleFuel**. Generation must not read raw dossier prose after mapping; it reads AngleFuel + run config. This is the observability spine.

```json
{
  "meta": {
    "scenario": "A",
    "methodology": "angle-ideation-agent@1.9.0",
    "product_name": "string",
    "source_refs": ["string"],
    "style_controls": {
      "intensity": 4,
      "darkness": 0,
      "formality": 2,
      "distance": 1
    }
  },
  "avatar": {
    "name": "string",
    "description": "string",
    "awareness_notes": "string",
    "labels": { "description": "EVIDENCED" }
  },
  "pain_points": [
    {
      "cluster": "string",
      "description": "string",
      "examples": ["string"],
      "label": "EVIDENCED"
    }
  ],
  "failed_attempts": [
    {
      "attempt": "string",
      "why_it_failed": "string",
      "label": "EVIDENCED"
    }
  ],
  "emotional_effects": ["string"],
  "exact_vocabulary": ["string"],
  "future_fears": ["string"],
  "product_fit": {
    "mechanism": "string",
    "how_it_resolves": "string",
    "label": "EVIDENCED"
  },
  "competitors": [
    {
      "name": "string",
      "loved": "string",
      "hated": "string",
      "label": "DERIVED"
    }
  ],
  "psychosocial_currencies_candidates": [
    {
      "currency_id": "IDENTITY_SELFHOOD",
      "why_it_applies": "string",
      "evidence_refs": ["pain_points[1]", "exact_vocabulary[0]"],
      "label": "DERIVED"
    }
  ],
  "beliefs": {
    "held": ["string"],
    "ready_to_shift": ["string"],
    "label": "DERIVED"
  },
  "gaps": [
    { "field": "string", "status": "UNKNOWN", "impact": "string" }
  ]
}
```

### 5.1 Mapping rules (Scenario A → AngleFuel)

| Dossier region | AngleFuel target |
|----------------|------------------|
| Demographics + life stage + emotional condition | `avatar` |
| Emotional pain points / drivers | `pain_points` |
| Verbatim parent voices | `exact_vocabulary` (+ examples under pains) |
| Tried tools / competitor complaints | `failed_attempts`, `competitors` |
| Fear / panic / future worry language | `future_fears`, `emotional_effects` |
| Unique mechanism / hygiene / control claims | `product_fit` |
| Awareness + sophistication notes | `avatar.awareness_notes`, `beliefs` |

Do not discard uncomfortable quotes. High-voltage confessions are priority fuel (see `docs/03` filters).

### 5.2 Belief extraction

From AngleFuel, derive:

- **Held beliefs:** what the avatar already accepts (e.g. “congestion destroys sleep/feeding”).
- **Ready-to-shift beliefs:** where old solutions failed and a new mechanism explanation is acceptable (e.g. “the category is sealed/uncleanable or uncontrolled”).

Angles must attach to one of these. Do not invent a belief war the avatar is not ready for unless the dossier shows high education willingness.

### 5.3 Dossier → AngleFuel mapper checklist (Comprehensive Dossier pattern)

Execute in order; tick each row. Skip inventing.

| Step | Extract from dossier region | Write to AngleFuel | Label |
|------|----------------------------|--------------------|-------|
| M1 | Title / target avatar / demographics / life stage | `avatar.name`, `avatar.description` | EVIDENCED |
| M2 | Emotional condition / PPA / hypervigilance | `avatar.description` append; `emotional_effects` | EVIDENCED |
| M3 | Pain driver table | `pain_points[]` (one cluster per driver) | EVIDENCED |
| M4 | Verbatim voices + vocabulary glossary | `exact_vocabulary[]` + pain `examples` | EVIDENCED |
| M5 | Awareness levels | `avatar.awareness_notes` | EVIDENCED |
| M6 | Market sophistication / cynicism | `beliefs.ready_to_shift` | DERIVED from EVIDENCED |
| M7 | Loved competitor qualities | `competitors[].loved` | EVIDENCED |
| M8 | Hated objections + why alternatives fail | `competitors[].hated`, `failed_attempts[]` | EVIDENCED |
| M9 | Root cause (physiological) | supports problem; may inform Core Ideas | EVIDENCED |
| M10 | Unique mechanism section | `product_fit.mechanism`, `how_it_resolves` | EVIDENCED (or DERIVED if “proposed”) |
| M11 | “I want” statements / future fears | `future_fears`, belief/desire lines | EVIDENCED |
| M12 | Direct response hooks (optional seeds) | candidate confession seeds only — **not** final headlines | EVIDENCED as seeds |
| M13 | Currency candidates | ≥6 `psychosocial_currencies_candidates` with `evidence_refs` | DERIVED |
| M14 | Gaps | any missing mechanism/competitor/voice → `gaps[]` | UNKNOWN |

**Stop conditions:** If M10 cannot be completed, do not proceed to angle drafting (`I-FUEL` fail).

## 6. Run configuration object

```json
{
  "target_angle_count": 8,
  "min_angle_count": 6,
  "currency_allowlist": null,
  "tone_constraints": [],
  "forbid_product_in_headline": true
}
```

Defaults: aim 8, accept 6–8 if quality holds; never pad with weak duplicates.
