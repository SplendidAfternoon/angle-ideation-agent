# Validation — StrideForm L3 live demo (third niche)

**Run:** [`runs/20260814-strideform-l3/`](../../runs/20260814-strideform-l3/)  
**Methodology:** angle-ideation-agent@1.6.0  
**Scenario:** B (thin inputs)  
**Product:** StrideForm Insoles (illustrative SKU; plantar-pressure redistribution)  
**Result:** Ready under v1.6 triad — chain PASS; gold mean 4.42 pack_pass; adversary `NO_MATERIAL_HITS`; leak check PASS  

## Purpose

Prove Generator → chain judge → pack → critic/gold → red-team on a **new niche**.

## Evidence

| Check | Result |
|-------|--------|
| `06_chain_judge.json` | PASS |
| `06_gold_scores.json` | pack_pass true (mean 4.42) |
| `07_adversary.json` | material_hits [] |
| `validate_headlines.py --product StrideForm` | 8/8 PASS (lexical) |
| `08_leak_check.json` | PASS |

## Notes

- Assist notes used on mining candidates only (Present bias / Sunk cost / Authority); Core Ideas are core friction insights, not bias names.
- Clinical diagnosis left UNKNOWN in fuel gaps; mechanism language only.
