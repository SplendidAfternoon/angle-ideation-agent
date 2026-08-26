# 05 — Validation Protocol

**Version:** 1.9.0  
**Normative:** Yes  
**Methodology pin:** `angle-ideation-agent@1.9.0`

## 1. Purpose

Quality is not “sounds good.” Quality is **reproducible passage of gates** plus **parity with the gold-standard bar** without plagiarism of the gold pack into new contexts. False positives (bad pack Ready) block release as much as false negatives.

## 2. Validation levels

| Level | Name | When | Pass means | Status (v1.5.0) |
|------:|------|------|------------|-----------------|
| L0 | Contract lint | Every run | Schema + required artifacts present | Required every run |
| L0b | Eval harness | Every methodology / pipeline change | `eval/harness.py` cases match expected PASS/FAIL (incl. stub-triad FAIL + VSL-doctrine FAIL) | Required — `eval/README.md` |
| L1 | Gate suite | Every run | Chain judge PASS + pack gates PASS + gold pack_pass + adversary material_hits empty | Required every run |
| L2 | Gold-bar reconstruction | Methodology changes; first ship | Method can produce Baby Bubble–class components from fuel (see §3) | **Done** — `runs/20260813-bb-l2/` |
| L3 | Transfer test | Before claiming generality | Second (and later) niche packs pass L0–L1 without reusing Baby Bubble villains/headlines | **Done** — hair-loss + StrideForm |
| L4 | Downstream smoke | Optional with Pre-Lander team | Pre-Lander agent can consume pack without schema questions | **Blocked** until a Pre-Lander agent exists (`docs/12`, `docs/14`) |

Negative control: feature-as-angle pack must fail chain judge, critic, gold, **and** adversary — [`docs/validation/negative-control.md`](validation/negative-control.md).

## 3. L2 — Baby Bubble reconstruction test

### 3.1 Intent

Prove the methodology reaches Section 5 quality **from fuel**, not from memory of the finished pack.

### 3.2 Inputs allowed

- Scenario A: Full avatar research dossier (and/or other market research trackers) mapped to AngleFuel  
- **Or** Scenario B: thin fields from benchmark input examples  
- Reference gold exemplar pack used **only as a hidden grading rubric**, not as a drafting source during the blind pass

### 3.3 Blind procedure

1. Build AngleFuel **without** opening the gold pack.  
2. Run Stages A–F (`docs/03`).  
3. Run full gates (`docs/04`) via critic (`docs/13`).  
4. **Then** open the gold pack and score with the rubric below.  
5. Record gaps → tighten methodology (version bump) if gaps are systemic.

### 3.4 Rubric (per angle vs gold class)

Score 1–5 each:

| Dimension | 5 looks like |
|-----------|--------------|
| Specificity of Hollow | Named interpersonal/identity loss, not fatigue adjectives |
| Villain concreteness | Tool/advice/category object you can point at |
| Dream render | Cinematic *reach* (doing / leaning mid-scene); not consumption, unboxing, or “it was over” |
| Belief move | Clear prove/shift; not a feature |
| Headline punch | Consequence-first, ≤12, past, confessable |
| Mechanism honesty | Fit uses real mechanism traits |

**Pack pass (required every Ready, not only first L2):** mean ≥ 4.0 across shipped angles, no dimension average < 3.5, emit `06_gold_scores.json`. Binary specification checklist is not sufficient.

### 3.5 Anti-cheating rules

- No copying gold headlines or arcs during blind draft.  
- After reveal, copying is still forbidden for “fixing” scores; only methodology rules may change, then re-blind.  
- Similarity check: if >2 headlines are near-paraphrases of gold, the run is invalid for L2.

## 4. L3 — Transfer test (done)

Records:

- Hair loss: `runs/20260813-hairloss-l3/` + `docs/validation/hairloss-l3-transfer.md`  
- Orthotics (third niche): `runs/20260814-strideform-l3/` + `docs/validation/strideform-l3-live-demo.md`

Pass requires:

- Distinct currencies grounded in that niche’s fuel  
- No Baby Bubble villains (bulb syringe, mouth tube) leaking in  
- Same artifacts + gates  

## 5. Regression suite (lightweight)

When methodology changes, re-run:

1. Scenario B thin input for nasal aspirator (benchmark examples) — `runs/20260814-bb-assisted/`  
2. Scenario A full dossier mapping sanity (fuel completeness) — `runs/20260813-bb-l2/`  
3. One intentional bad pack (feature-as-angle) and confirm gates **FAIL** — `runs/20260814-negcontrol-feature/`
4. Eval harness including VSL-doctrine FAIL — `eval/harness.py` (`eval/fixtures/vsl-doctrine-fail/`)

False negatives (good pack fails) and false positives (bad pack passes) both block release.

## 6. Recording template

See `docs/validation/baby-bubble-reconstruction.md` for the L2 record format. Negative control: `docs/validation/negative-control.md`.
