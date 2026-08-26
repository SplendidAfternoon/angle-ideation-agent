# 06 — Quality Self-Audit (Research-Engineering Bar)

**Version:** 1.9.0  
**Methodology pin:** `angle-ideation-agent@1.9.0`  
**Purpose:** Explicitly check this methodology pack against a high research-engineering standard.

## 1. Quality bar (criteria)

| ID | Criterion | What “excellent” means |
|----|-----------|------------------------|
| Q1 | Precise definitions | Operational definitions + negatives |
| Q2 | Testable predicates | Gates fail for clear reasons |
| Q3 | Deterministic structure | Stable schema |
| Q4 | Observability | Intermediate artifacts required |
| Q5 | Fail-closed behavior | Missing inputs stop the run |
| Q6 | Separated concerns | Angle ≠ hook/claim/offer/concept |
| Q7 | Grounding | Beliefs/mechanisms labeled |
| Q8 | Adversarial robustness | Docs cannot rewrite process |
| Q9 | Calibrated uncertainty | Label enum |
| Q10 | Worked evaluation path | L2 executed with artifacts |
| Q11 | Non-overfit | Anti-cheat on gold |
| Q12 | Honest limits | Gaps stated |
| Q13 | Agentic judgment split | Generator ≠ Critic; scripts ≠ creative gates |

## 2. Audit results (v1.6.1)

| ID | Result | Evidence | Residual risk |
|----|--------|----------|---------------|
| Q1 | **PASS** | Schema + failure catalog | — |
| Q2 | **PASS** | H5/H6/P-FEELS-REAL + A-VILLAIN/A-DREAM | Human cold-read still valuable |
| Q3 | **PASS** | `schemas/angle_fuel.schema.json`, `angle_pack.schema.json`, `gate_report.schema.json` | — |
| Q4 | **PASS** | Full run artifacts 00–06 (+ assist audit when used) | — |
| Q5 | **PASS** | Input contracts + preflight scripts | — |
| Q6 | **PASS** | C11 / non-angle table + full negative-control pack FAIL | — |
| Q7 | **PASS** | Labeled fuel | Scenario B still inference-heavy |
| Q8 | **PASS** | docs/00 + P0 | — |
| Q9 | **PASS** | Labels in fuel | — |
| Q10 | **PASS** | L2 + L3 + assisted + StrideForm + negative-control FAIL | — |
| Q11 | **PASS** | L2 similarity + L3 leak check | — |
| Q12 | **PASS** | Scenario B product / deferred Pre-Lander page gen stated | — |
| Q13 | **PASS** | Chain judge before prose + independent red-team; scripts ≠ Ready | Critic/adversary still LLMs |

## 3. Residual risks accepted

- `P-FEELS-REAL` benefits from a cold human read even after critic PASS.  
- Critic agent can sycophant; mitigated by evidence quotes + anti-sycophancy + dual cold-read on H*, A-VILLAIN, A-DREAM, P-DISTINCT.  
- Brand/mechanism naming bridge (Baby Bubble vs dossier “Safe-Suction”) is documented in L2 fuel gaps.  
- L3 product `Rootline Serum` is a transfer stand-in, not a live SKU claim.  
- Generality: three niches proven (aspirator, hair loss, orthotics); still not a category encyclopedia.  
- Cursor scheduled Automations remain deferred (`docs/14`).  
- Negative control: [`docs/validation/negative-control.md`](validation/negative-control.md).
