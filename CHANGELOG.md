# CHANGELOG

## 1.9.0 — 2026-08-20

### VSL doctrine in generation + gates (not a video generator)

Emotion-First VSL doctrine is now pack law: feeling first, one idea = the unanswered gap, Dream = *reach* not arrival, fall before mechanism, loop closes only at CTA.

- Catalog: **F16–F18** (`docs/04` §9). Plan names F13–F15 collided with existing diversity IDs (archetype / headline / awareness); those stay F13–F15.
- Q3 reach, Q5 fall-first, Q7/Q8 open-loop (`docs/03`). Feeling-first draft order: Hollow → Headline → Dream → Arc fall → Twist → Fit.
- Gold Dream render **5** = cinematic reach, not consumption (`docs/05` §3.4). No new score dimension.
- `docs/15`: F16–F18 / H3 are pack gates; `D-CTA-SNAP` and `D-FLATLINE` stay editor-only.
- Skills: generator, critic Pass A (Q3 arrival, Q5 mechanism-in-Action, Q8 loop-closed), red-team hunts F16–F18.
- Eval: `eval/fixtures/vsl-doctrine-fail/` must FAIL (`F16-ARRIVAL`, `F17-MECH-ACTION`, `F18-HOOK-CLUSTER`). Benchmark pack `runs/20260814-bb-benchmark/` already mid-lean / fall-first / open headlines — **not regenerated**.

Pin: `angle-ideation-agent@1.9.0` on touched normative docs and skills. Historical run folders keep their pins.

## 1.7.0 — 2026-08-20

### VSL deployment contract + eval/LLM-ops harness

- Emotion-first direct response doctrine treated as **data**, not process control (`docs/00`). Handoff beat map: [`docs/15-vsl-deployment-contract.md`](docs/15-vsl-deployment-contract.md). Still no VSL generator (`docs/14`).
- Eval harness [`eval/harness.py`](eval/harness.py) labels live Ready runs, negative control, and a **collapsed-triad fixture** that must FAIL (hardcoded critic/gold/adversary signatures).
- LLM ops: [`eval/llm_ops.md`](eval/llm_ops.md), `09_llm_trace.json` schema, `scripts/llm_ops.py`.
- `scripts/run_pipeline.py` no longer writes stub PASS gates/gold/adversary. Status stays Blocked until schema-valid triad; Ready only after critic + red-team. Validator import fixed (`validate_run`).

## 1.6.1 — 2026-08-14


### Benchmark loop closed (after one iterate)

- First benchmark pack Ready stamp failed an honest red-team pass: F03 loop-villains, F05 Dream peaking on the cup.
- Patched `docs/03` villain/dream rules and `docs/04` `A-VILLAIN` / `A-DOOR` / F03 / F05. Regenerated Q2/Q3 on the benchmark pack.
- [`runs/20260814-bb-benchmark/05_angle_pack.md`](runs/20260814-bb-benchmark/05_angle_pack.md) Ready after revision_loop 1 (gold mean 4.48; adversary `material_hits` empty). Reference gold pack unused as copy source.
- README + [`docs/11`](docs/11-stakeholder-handoff.md) rewritten as pack → iterate → finished methodology. Pin: **complete**. No further methodology expansion unless asked.

## 1.6.0 — 2026-08-14

### LLM-native quality bar

- Ready requires **four** LLM artifacts: `06_chain_judge.json` PASS, `06_gate_report.json` PASS, `06_gold_scores.json` pack_pass (mean ≥ 4.0), `07_adversary.json` material_hits empty.
- Generator skill no longer authors judge files or stamps Ready without the triad (`docs/13`).
- New red-team skill [`.cursor/skills/angle-red-team/`](.cursor/skills/angle-red-team/) — hunts F01–F12 in prose even when Python already failed headlines.
- Chain judge blocks weak Q2/Q3/Q7/Q8 **before** pack prose.
- Proof: negcontrol chain FAIL + adversary BLOCK; StrideForm chain PASS, gold mean 4.42, adversary `NO_MATERIAL_HITS`.

## 1.5.0 — 2026-08-14

### Spec completeness + industry upgrades

- Negative control: [`runs/20260814-negcontrol-feature/`](runs/20260814-negcontrol-feature/) — feature/claim/offer pack; critic **Blocked**; headlines 6/6 FAIL. Record: [`docs/validation/negative-control.md`](docs/validation/negative-control.md).
- Critic 1.5.0: few-shot F01–F12 + pairwise `P-DISTINCT` (hollow noun-swap = same Andromeda concept). Protocol: `.cursor/skills/angle-gate-critic/critic-protocol.md`.
- StrideForm stays Ready under calibrated critic: [`runs/20260814-strideform-l3/06_gate_report.v15-calibrate.json`](runs/20260814-strideform-l3/06_gate_report.v15-calibrate.json).
- Pack assist fields: `awareness_stage`, `test_priority`, **Testing order** table (`docs/01`, `docs/12`, generator skill). Scenario B inference ceiling on pack header.
- `docs/05` L2/L3 marked done; L4 still blocked on Pre-Lander.

## 1.4.1 — 2026-08-14

### Pipeline next steps

- Git baseline commit freezing `angle-ideation-agent@1.4.0` on `master`.
- Third-niche live demo: [`runs/20260814-strideform-l3/`](runs/20260814-strideform-l3/) (Generator → Preflight → Critic Ready; leak check PASS).
- Reviewer demo walk record: [`docs/validation/stakeholder-demo-walk-20260814.md`](docs/validation/stakeholder-demo-walk-20260814.md).
- Explicit downstream deferrals: [`docs/14-downstream-deferrals.md`](docs/14-downstream-deferrals.md) (Pre-Lander separate project; Automations after push).

## 1.4.0 — 2026-08-14

### Release readiness + agentic gates

- Normalized methodology pin to `angle-ideation-agent@1.4.0` across normative docs and skills.
- Added Pre-Lander handoff contract [`docs/12-prelander-handoff-contract.md`](docs/12-prelander-handoff-contract.md) + [`schemas/angle_pack.schema.json`](schemas/angle_pack.schema.json).
- Added agentic gate protocol [`docs/13-agentic-gate-protocol.md`](docs/13-agentic-gate-protocol.md): Generator / Preflight / Critic split.
- Added critic skill [`.cursor/skills/angle-gate-critic/`](.cursor/skills/angle-gate-critic/) (`SKILL.md`, `critic-protocol.md`) and [`schemas/gate_report.schema.json`](schemas/gate_report.schema.json).
- Generator skill wires preflight → critic → max-2 revise; Ready only after critic PASS.
- Added lexical [`validate_pack_preflight.py`](.cursor/skills/angle-ideation/scripts/validate_pack_preflight.py) (skeleton/count only — not creative quality).
- Critic smoke: [`runs/20260814-bb-assisted/06_gate_report.critic-smoke.json`](runs/20260814-bb-assisted/06_gate_report.critic-smoke.json) (preflight PASS; Ready recommendation).
- Refreshed [`docs/06-quality-self-audit.md`](docs/06-quality-self-audit.md) with Q13 agentic split.

## 1.3.1 — 2026-08-14

### Handoff + assisted proof

- Added [`docs/11-stakeholder-handoff.md`](docs/11-stakeholder-handoff.md) (how to run, artifacts, demo script).
- Completed Scenario B assisted proof run [`runs/20260814-bb-assisted/`](runs/20260814-bb-assisted/) with docs/10 `assist_notes` on all shipped angles; headline validator 8/8; gates Ready.
- Assist audit: [`runs/20260814-bb-assisted/07_assist_audit.md`](runs/20260814-bb-assisted/07_assist_audit.md).

## 1.3.0 — 2026-08-14

### Bias & heuristics catalog (assist layer)

- Added canonical [`docs/10-cognitive-biases-heuristics-catalog.md`](docs/10-cognitive-biases-heuristics-catalog.md): cognitive biases, judgment heuristics, debate/rhetorical heuristics, dark-pattern bans, A–Z index.
- Slimmed skill [`psychology-biases.md`](.cursor/skills/angle-ideation/psychology-biases.md) to protocol + top-leverage table; progressive disclosure into docs/10.
- `docs/03` Stage A: optional `assist_notes` on candidates (non-normative for gates).
- Rewrote `docs/09` as policy pointer (canonical = docs/10).

## 1.2.0 — 2026-08-13

### Runnable skill

- Added project skill `.cursor/skills/angle-ideation/` (`SKILL.md`, gate checklist, prompt blocks, psychology assist, `scripts/validate_headlines.py`).
- Added `docs/09-psychology-and-bias-reference.md` (pointer + policy: assist only, not primary engine).

## 1.1.1 — 2026-08-13

### Patches from Blind L2 (`runs/20260813-bb-l2`)

- Added **villain binding rule** for thin relational/identity fuel (`docs/03`).
- Tightened `A-VILLAIN` / `A-DREAM` predicates (no “loop/situation”; dream needs sensory anchor).
- Rewrote L2 angles 7–8 villains/dreams; L2 closed as PASS after patch.

### L3 transfer

- Completed Scenario B hair-loss pack (`runs/20260813-hairloss-l3/`) with leak check PASS.
- Added `docs/validation/hairloss-l3-transfer.md`.

## 1.1.0 — 2026-08-13

### Stricter / clearer

- Added **currency disambiguation** pairwise rules (`docs/01` §4.1).
- Replaced fuzzy `H5` / `H6` / `P-FEELS-REAL` with reject patterns, ad-ese ban list, and confessable checklist (`docs/01`, `docs/04`).
- Added **failure catalog** with gate mappings (`docs/04` §9).
- Added **dossier→AngleFuel mapper checklist** (`docs/02` §5.3).
- Added **prompt appendix** (`docs/08-prompt-appendix.md`).
- Added machine JSON schema file `schemas/angle_fuel.schema.json`.
- Methodology pin bumped to `angle-ideation-agent@1.1.0` across normative docs.

### Intent

Close soft spots before Blind L2 so validation tests a sharper contract, not vibes.
