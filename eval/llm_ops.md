# LLM ops protocol

**Pin:** `angle-ideation-agent@1.9.0`  
**Normative for** `scripts/run_pipeline.py` and any future Automation wrapper.

## 1. Roles (must not collapse)

| `role` in trace | Writes | Must not write | Temperature |
|-----------------|--------|----------------|-------------|
| `generator` | `00`–`05` | `06_*`, `07_adversary.json` | 0.4–0.7 |
| `critic` | `06_chain_judge.json`, `06_gate_report.json`, `06_gold_scores.json` | `05_angle_pack.md` | ≤0.2 |
| `red_team` | `07_adversary.json` | pack Status, angles | ≤0.2 |
| `preflight` | stdout / `preflight` object on gate report | creative verdicts | n/a (scripts) |

Same model **may** be used across roles only if traces show **separate calls** with distinct `system` hashes and the critic/red-team prompts contain no “return PASS”. Hardcoding JSON in Python is a **harness FAIL** (`OPS-STUB-*`).

## 2. Loop (accurate)

```text
generator 00–04
    → critic Pass A (chain judge). FAIL → revise Qs ≤2, do not polish 05 as Ready
generator 05 Status=Blocked
    → preflight scripts
    → critic Pass B (schema-valid gates + gold)
    → red-team (schema-valid adversary)
    → if all four Ready predicates true: generator updates Status line only
```

If Pass A `result != PASS`, the pipeline **stops** or regenerates chains. It does not invent `06_gate_report.json`.

## 3. Trace file

Every automated run writes `09_llm_trace.json` (`schemas/llm_trace.schema.json`):

- one object per LLM call: `role`, `stage`, `model`, `provider`, `temperature`, `tokens_in`, `tokens_out`, `artifact_written`, `ended_ok`
- `collapsed_roles: false` required
- `ready_stamped_by` must be `generator_header_after_triad` — never `critic` or `pipeline_default`

Missing trace on an automated run → `OPS-NO-TRACE`.

## 4. Stub signatures the harness hunts

- `gates` is an object/map instead of an array of `{gate_id, scope, result, evidence}`  
- Gold angles lack `hollow_specificity` … `mechanism_honesty`  
- Evidence strings in the generic stub set (see `eval/harness.py` `STUB_EVIDENCE`)  
- `07_adversary.json` with `material_hits: []` **and** no `nits` / no pack quotes when Status is Ready and pack contains F01-class Core Ideas  
- Pack Status Ready written in the **generator** prompt before Pass B exists

## 5. Disagreement

If critic recommends Ready and adversary has `material_hits` → `CRITIC_ADVERSARY_DISAGREE` (Blocked). The harness treats Ready + nonempty hits as FAIL regardless of recommendation string.
