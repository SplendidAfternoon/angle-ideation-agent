# Assist audit — 20260814-bb-assisted

**Methodology:** angle-ideation-agent@1.3.1  
**Result:** PASS

## Binding rules checked

| Rule | Result |
|------|--------|
| Assist only after AngleFuel | PASS |
| Max one `assist_notes` per shipped angle | PASS |
| Each `bias_id` exists in docs/10 | PASS |
| Assist binds to fuel pain/failure | PASS |
| Core Ideas are not bias names | PASS |
| Invalid assist path rejected (A09 + HEUR_SCARCITY on claim) | PASS |

## Mapping (shipped)

| Angle | Currency | bias_id | attach_to | Core Idea is bias name? |
|------:|----------|---------|-----------|-------------------------|
| 1 | SAFETY_SECURITY | `BIAS_ATTENTIONAL` | Hollow | No |
| 2 | TRUST_SAFETY | `BIAS_DISGUST` | Villain | No |
| 3 | AGENCY_PARTNERSHIP | `BIAS_DISGUST` | Villain | No |
| 4 | GUILT_REGRET | `DEBATE_NON_ID_BLAME` | Twist | No |
| 5 | AGENCY_CONTROL | `BIAS_SUNK_COST` | Action | No |
| 6 | AUTHORITY | `BIAS_AMBIGUITY_AVERSION` | Hollow | No |
| 7 | RELATIONAL_EQUITY | `BIAS_LOSS_AVERSION` | Hollow | No |
| 8 | IDENTITY_SELFHOOD | `BIAS_PROJECTION` | Hollow | No |

Note: `BIAS_DISGUST` appears on two angles with different currencies/primary wounds (contamination vs mouth-suction handoff). Allowed — uniqueness is per-angle assist, not pack-wide bias exclusivity.

## Headline validator

`validate_headlines.py --product "Baby Bubble"` → **8/8 PASS**

## Gates

`06_gate_report.json` → **Ready for Pre-Lander Agent**  
No methodology patch required.
