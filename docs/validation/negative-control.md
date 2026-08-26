# Validation — Negative control (feature-as-angle)

**Run:** [`runs/20260814-negcontrol-feature/`](../../runs/20260814-negcontrol-feature/)  
**Methodology:** angle-ideation-agent@1.6.0  
**Purpose:** `docs/05` regression — a bad pack must **not** Ready (false-positive check).  
**Result:** **PASS as a negative control** — chain FAIL, gold fail, critic Blocked, adversary BLOCK with quoted F-class hits (not only Python H4).

## v1.6 triad

| Artifact | Result |
|----------|--------|
| `06_chain_judge.json` | FAIL (would have blocked `05`) |
| `06_gold_scores.json` | pack_pass false (mean ~1.4) |
| `06_gate_report.json` | Blocked |
| `07_adversary.json` | BLOCK; F01/F02/F03/F04/F05/F06/F10/F12 quoted from prose |
| `validate_headlines.py` | 6/6 FAIL (lexical only) |
| `validate_pack_preflight.py` | PASS (skeleton ≠ quality) |

Adversary quotes Hollow/Dream/Core failures even though scripts already failed headlines — judgment is LLM-native.
