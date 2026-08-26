# 13 — Agentic Gate Protocol

**Version:** 1.9.0  
**Normative:** Yes  
**Methodology pin:** `angle-ideation-agent@1.9.0`  
**Depends on:** `docs/03`, `docs/04`, `docs/12`  
**Purpose:** Lock Generator / Preflight / Critic / Red-team so quality is LLM-native, not a Python checklist.

## 1. Why scripts are not enough

Lexical Python can check word counts, product tokens, and section presence. It **cannot** judge Hollow, Dream, Villain, or “feels real.” One chat self-grading `05` in the same pass is also not enough.

## 2. Four roles (triad + preflight)

| Role | Skill / tool | Writes | Must not |
|------|--------------|--------|----------|
| **Generator** | `angle-ideation` | `00`–`05` | `06_*`, `07_adversary.json`, Ready without files |
| **Preflight** | `validate_headlines.py`, `validate_pack_preflight.py` | stdout | Creative gates |
| **Critic** | `angle-gate-critic` | `06_chain_judge.json`, `06_gate_report.json`, `06_gold_scores.json` | Drafting angles |
| **Red-team** | `angle-red-team` | `07_adversary.json` | Passing anything; rewriting pack |

```text
Generator 00-04 → Critic chain-judge → Generator 05 (Blocked)
  → Preflight → Critic pack+gold → Red-team → Ready | Blocked
```

## 3. Ready predicate (all required)

Pack Status may be `Ready for Pre-Lander Agent` only if:

1. `06_chain_judge.json` `result: PASS`  
2. `06_gate_report.json` all required gates PASS + cold reread  
3. `06_gold_scores.json` `pack_pass: true` (mean ≥ 4.0; no dimension avg < 3.5)  
4. `07_adversary.json` `material_hits: []`  
5. If critic recommended Ready and adversary has hits → FAIL `CRITIC_ADVERSARY_DISAGREE`

Generator updates the Status **line** only after those files exist. Generator does not author the judge files.

## 4. Chain judge (1.5x vs single-pass generation)

Single-pass generation inspects finished copy only. We inspect **Q1–Q8** first so weak villains/dreams never become pretty prose.

## 5. Known limits

Critic and red-team are still LLMs. Split passes + evidence quotes + gold scores + adversary disagreement mitigate sycophancy. Not unit-test certainty.

## 6. Out of scope

Pre-Lander pages, Meta, scheduled Automations, quality regex.
