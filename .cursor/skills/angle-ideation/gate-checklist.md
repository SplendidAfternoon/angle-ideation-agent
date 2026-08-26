# Gate checklist (angle-ideation-agent@1.9.0)

**Owner:** Critic writes `06_chain_judge.json`, `06_gate_report.json`, `06_gold_scores.json`. Red-team writes `07_adversary.json`. Generator must not Ready-stamp without all four.

Ready only if chain PASS + required gates PASS + gold pack_pass + adversary material_hits empty. Lexical assist: `scripts/validate_headlines.py`, `scripts/validate_pack_preflight.py`.

## Input

| ID | Pass if |
|----|---------|
| I-AVATAR | Avatar specific and present |
| I-PRODUCT | Product/mechanism present |
| I-PROBLEM | Problem present |
| I-FUEL | AngleFuel valid; mechanism not UNKNOWN |
| I-VOICE | ≥5 multi-word vocab items or evidenced quotes |
| I-BRIEF | Scenario B only: mini-brief MB1–MB8 |

## Headlines (each angle)

| ID | Pass if |
|----|---------|
| H1 | ≤12 words |
| H2 | Past / past-perfect consequence |
| H3 | Consequence or villain named; Headline opens the gap (no mechanism answer / “then we slept”) |
| H4 | No product/brand token |
| H5 | Does not start with: At / For weeks|months|days / When I / After I / Before I / One night / Last night / Today / Tonight / Suddenly / Finally |
| H6 | Confessable; no ad-ese: game-changer, hack, must-have, literally obsessed, link in bio, hospital-grade (headline), miracle, secret trick, order now |

## Components (each angle)

| ID | Pass if |
|----|---------|
| A-CURRENCY | Exactly one allowlisted currency |
| A-CORE | One sentence; core friction + escalation; belief move |
| A-HOLLOW | Named scene loss (not mood-only) |
| A-VILLAIN | Concrete tool/advice/category flaw (not situation/loop alone) |
| A-DREAM | Sensory *reach* (doing / leaning); not arrival / “nights were normal” (F16) |
| A-ARC | Setup, Action = fall, Twist, Verdict; Action is not a feature win (F17) |
| A-FIT | Causal mechanism → this hollow/dream |
| A-DOOR | Product not Dream climax |
| A-BELIEF | Belief in fuel held/ready_to_shift or evidenced pains |
| A-VOICE | Matches fuel vocabulary register |

## Pack

| ID | Pass if |
|----|---------|
| P-COUNT | 6–8 (or Blocked with reason) |
| P-DISTINCT | Unique currencies **and** pairwise hollows not noun-swapped synonyms |
| P-FEELS-REAL | ≥3 vocab echoes; villains nameable in ≤6 words; no synonym pack |
| P-CONSISTENCY | Matches fuel |
| P-ARTIFACTS | Reasoning + score log present |
| P-HEADLINES-TABLE | Present/accurate |
| P-SUMMARY | Matches body |
| P-CURRENCY-RULES | docs/01 §4.1 obeyed |
| P-CHAIN-JUDGE | 06_chain_judge.json PASS |
| P-GOLD | 06_gold_scores.json pack_pass |
| P-ADVERSARY | 07_adversary.json material_hits empty |
