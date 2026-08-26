# Angle Ideation Agent (Technical Reference)

> A multi-agent creative strategy and evaluation pipeline that transforms qualitative market research, consumer psychology, and product mechanics into curiosity-led narrative angles, open-loop hooks, and validated creative briefs.

**Note:** This repository serves as a production-grade methodology and architectural blueprint for creative strategy ideation (`angle-ideation-agent@1.9.0`). It implements strict Creator–Verifier role isolation and zero-sycophancy evaluation gates to produce pre-lander-ready emotional angle packs without generic marketing hype or hallucinated claims.

## System Architecture

The pipeline implements a specialized three-node agentic topology to process, ground, generate, and evaluate narrative angles at scale:

### 1. Market Research & Fuel Plane (AngleFuel)
- **Structured VOC Mining:** Extracts qualitative customer insights, belief barriers, and category habits from thin inputs (Scenario B: avatar, product, problem, competitors) or rich dossiers (Scenario A) without fabricating claims.
- **Psychosocial Register Tagging:** Maps avatar motivations across 12 distinct psychosocial currencies (`Identity`, `Agency`, `Trust`, `Relational Equity`, `Mastery`, `Delight`) to guarantee emotional breadth across a pack.
- **Fail-Closed Input Routing:** Rejects underspecified or repetitive input data (`Blocked`) rather than generating generic or sycophantic copy.

### 2. Creative Ideation & Mining (Generator Node)
- **Curiosity-First Hypothesis Mining:** Scores candidates across emotional charge, market proof, and novelty ($S = E \times M \times W$) to filter out superficial feature lists.
- **Deterministic Reasoning Chains:** Executes structured Q1–Q8 reasoning paths to build a 4-beat narrative progression (Setup → Action → Twist → Verdict).
- **Open-Loop Headline Craft:** Generates pattern-interrupt headlines constrained by machine-checkable lexical predicates (past tense, under 12 words, named villain/consequence, zero ad-ese buzzwords, zero product names).
- **Product-as-Door Rule:** Enforces that the product functions strictly as the functional mechanism/doorway, never as the emotional hero or unboxing climax.

### 3. Verification & Quality Gates (Critic Node)
- **Pre-Prose Chain Judge:** Audits reasoning chains (`06_chain_judge.json`) for concrete villain objects and sensory dreams before drafting prose, catching structural flaws upstream.
- **Automated Quality Checklist:** Enforces F01–F18 failure detection (e.g., product-as-hero, premature arrival, territory collisions, ad-ese buzzwords, ungrounded cosmologies).
- **Gold Rubric Calibration:** Grades angle packs against strict multi-dimensional criteria (mean score $\ge 4.0$) across emotional tension, villain relocatability, and belief shift.

### 4. Adversarial Red-Team (Adversary Node)
- **Creator–Verifier Invariant:** An isolated red-team agent independently stress-tests the draft (`07_adversary.json`) without shared memory or sycophantic bias.
- **Pairwise Collision Hunting:** Detects near-duplicate angles with swapped nouns to ensure true diversity across testing angles.
- **Ready Predicate Gate:** Angle packs are stamped `Ready for Pre-Lander Agent` only when all gate reports, gold scores, and adversary audits pass unanimously.

## Multi-Niche Validation

The methodology is product-agnostic and validated across diverse consumer and wellness verticals:

| Vertical | Product / Domain | Core Insight & Curiosity Focus | Benchmark Run |
|----------|-----------------|--------------------------------|---------------|
| **Athletic Biomechanics** | `StrideForm` | Foot strike misconceptions vs joint loading mechanics | [`runs/20260814-strideform-l3/`](runs/20260814-strideform-l3/05_angle_pack.md) |
| **Pet Behavioral Wellness** | `Pawsitive Calm` | Separation anxiety triggers vs routine sensory regulation | [`runs/20260816-pawsitive-calm/`](runs/20260816-pawsitive-calm/05_angle_pack.md) |
| **Follicular Health** | `FolliRoot` | Topical scalp nutrition vs internal DHT pathway awareness | [`runs/20260814-folliroot/`](runs/20260814-folliroot/05_angle_pack.md) |
| **Pediatric Airway Care** | `Baby Bubble` | Nighttime congestion support & clear airway ergonomics | [`runs/20260814-bb-benchmark/`](runs/20260814-bb-benchmark/05_angle_pack.md) |

## Tooling & Automation

```bash
# 1. Automated Generation Pipeline (Requires GEMINI_API_KEY, OPENAI_API_KEY, or ANTHROPIC_API_KEY)
cp .env.example .env
python scripts/run_pipeline.py --avatar "Distance runners managing recurring shin discomfort" \
                               --product "StrideForm Dynamic Insoles" \
                               --problem "Impact fatigue on asphalt runs above 5 miles" \
                               --competitors "Generic foam inserts, custom rigid orthotics"

# 2. Run Comprehensive Eval Harness (live runs + synthetic fault injections)
python eval/harness.py

# 3. Validate Run Against Schemas and Triad Predicates
python scripts/validate_run.py runs/20260814-strideform-l3 --product "StrideForm"

# 4. Export Markdown Pack to Validated JSON Schema (docs/12)
python scripts/export_angle_pack_json.py runs/20260814-strideform-l3/05_angle_pack.md -o runs/20260814-strideform-l3/05_angle_pack.json

# 5. Execute Automated Test Suite
python -m unittest tests.test_runs tests.test_eval_harness
```

## Repository Architecture & Contracts

| Layer | Path | Description |
|-------|------|-------------|
| **Trust Hierarchy** | [docs/00](docs/00-source-hierarchy-and-trust.md) | Source hierarchy and prompt-injection defense |
| **Angle Pack Schema** | [docs/01](docs/01-angle-pack-schema.md) | Structural angle components, headline predicates, currency catalog |
| **Input Specifications** | [docs/02](docs/02-input-contracts.md) | Scenario A (rich research dossiers) & Scenario B (thin inputs) |
| **Generation Engine** | [docs/03](docs/03-angle-generation-methodology.md) | Candidate mining, scoring ($S = E \times M \times W$), 8-question reasoning chains |
| **Quality Gates** | [docs/04](docs/04-quality-gates.md) | F01–F18 failure detection catalog and lexical constraints |
| **Validation Protocol** | [docs/05](docs/05-validation-protocol.md) | Blind rubric scoring, cross-niche transfer tests, anti-cheating rules |
| **Agentic Triad Protocol** | [docs/13](docs/13-agentic-gate-protocol.md) | Creator–Verifier invariant, role isolation, and Ready predicates |
| **Downstream Contracts** | [docs/12](docs/12-prelander-handoff-contract.md), [docs/15](docs/15-vsl-deployment-contract.md) | Pre-lander and video sales letter deployment contracts |
| **System Overview** | [docs/11](docs/11-stakeholder-handoff.md) | Technical and creative team handoff documentation |


