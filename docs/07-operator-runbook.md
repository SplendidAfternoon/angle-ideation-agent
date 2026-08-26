# Operator Runbook (Manual Execution)

**Version:** 1.9.0  
**Methodology pin:** `angle-ideation-agent@1.9.0`  
**Use:** Human runs the methodology end-to-end before automation exists.

## Preconditions

- Read `docs/00` (trust) once.  
- Have either a dossier (Scenario A) or thin fields (Scenario B).  
- Create a run folder: `runs/YYYYMMDD-HHMM-<slug>/`

## Steps

1. **Route**  
   - Dossier? → Scenario A  
   - Else → Scenario B  
   - Write `00_route.json` with decision + rationale.

2. **Validate inputs**  
   - Scenario B: avatar, product, problem present → else STOP.  
   - Scenario A: dossier minimum from `docs/02` §3.

3. **Build AngleFuel**  
   - A: map dossier → `01_angle_fuel.json`  
   - B: run mini-brief master prompt → validate MB1–MB8 → save as fuel  
   - Label EVIDENCED / DERIVED / PLAUSIBLE_INFERENCE / UNKNOWN

4. **Mine candidates** → `02_candidates.json`

5. **Filter F1–F3** + score `E×M×W` → `03_filter_score_log.json`

6. **Select 6–8 unique currencies** (greedy by score)

7. **Reason Q1–Q8** per selected → `04_reasoning_chains.json`  
   - Do not draft final prose before Q1–Q8 exist.

8. **Draft pack** → `05_angle_pack.md` using `docs/01` skeleton (Status not Ready yet)

9. **Lexical preflight**  
   - `validate_headlines.py` + `validate_pack_preflight.py`  
   - Fix FAIL before critic (`docs/13`)

10. **Critic gates** → `06_gate_report.json` via `angle-gate-critic` (`docs/04`)  
    - Evidence quotes required; cold reread H*, A-VILLAIN, A-DREAM, P-DISTINCT  
    - On FAIL: revise ≤2 loops (`docs/03` §10), then re-run critic

11. **Set Status**  
    - Critic recommends Ready + all required PASS → `Ready for Pre-Lander Agent`  
    - Else → `Blocked` with reason codes  
    - Pre-Lander may consume only per `docs/12`

## Timebox guidance

| Stage | Typical care level |
|-------|--------------------|
| Fuel | Slow — errors here poison all angles |
| Mining/scoring | Medium — be ruthless on duplicates |
| Reasoning chains | Slow — this is the quality lever |
| Prose draft | Medium — compress to gold density |
| Preflight | Fast — lexical only |
| Critic + cold reread | Slow — judgment gates |

## Do not

- Start from competitor ads  
- Invent mechanism traits  
- Ship without artifacts  
- Ready-stamp without critic report  
- Treat preflight PASS as quality  
- “Borrow” Baby Bubble headlines for other niches
