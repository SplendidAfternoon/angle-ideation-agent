# Eval harness & LLM ops

**Pin:** `angle-ideation-agent@1.9.0`  
**Purpose:** Prove the generator → critic → red-team **loop is real**, not a self-stamp. Lexical `validate_run.py` is necessary and not sufficient.

## Why this exists

`scripts/run_pipeline.py` previously wrote Ready-looking `06_gate_report.json` / `06_gold_scores.json` / `07_adversary.json` **without judging the pack** (hardcoded PASS). Naive single-pass generation can also rubber-stamp loop-villains. Harness + cases catch both classes:

| Class | Symptom | Catch |
|-------|---------|--------|
| **Stub triad** | Gate `gates` is a dict; gold lacks dimensions; adversary empty by construction | `OPS-*` flags in `eval/harness.py` |
| **Schema lie** | Artifact fails `schemas/*.schema.json` | jsonschema in harness + `validate_run` |
| **Sycophancy** | Pretty feature pack marked Ready | Negative-control case must `expect: FAIL` |
| **Collapsed roles** | Same prompt writes `05` and `06_*` | Trace requires distinct `role` per stage (`eval/llm_ops.md`) |
| **VSL doctrine** | Emotional-looking copy that arrives, sells in Action, or mashes Hook Cluster | `F16-ARRIVAL` / `F17-MECH-ACTION` / `F18-HOOK-CLUSTER` |

## Run

```text
python eval/harness.py
python eval/harness.py --case collapsed-triad-must-fail
python eval/harness.py --case vsl-doctrine-must-fail
python -m unittest tests.test_eval_harness tests.test_runs
```

Exit 0 only if every case’s actual PASS/FAIL matches `eval/cases/manifest.json`.

## Layout

| Path | Role |
|------|------|
| `eval/cases/manifest.json` | Expected labels |
| `eval/fixtures/collapsed-triad/` | Synthetic stub triad (must FAIL) |
| `eval/fixtures/vsl-doctrine-fail/` | Emotional-looking F16–F18 pack (must FAIL) |
| `eval/harness.py` | Runner |
| `eval/llm_ops.md` | Trace + role isolation protocol |
| `schemas/eval_case.schema.json` | Case file shape |
| `schemas/llm_trace.schema.json` | Per-run `09_llm_trace.json` |

Live Ready/Blocked packs stay under `runs/`. Fixtures here are **eval-only** and must never be handed to Pre-Lander.
