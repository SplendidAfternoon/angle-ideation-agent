# Adversary protocol (angle-red-team@1.9.0)

Hunt only. Load `docs/04` §9 F01–F18 first. Every material hit quotes ≤25 words.

## Hunt list (all required)

1. **F01–F18** against Core Idea, Hollow, Villain, Dream, Headline, Arc, Hook Cluster.  
2. **Pairwise hollows** — same core friction, nouns swapped → F06 material hit.  
3. **Product-removed test** — strip product/brand name from each angle. If what remains is a feature/offer sheet → `feature_sheet_if_product_removed: YES_FEATURE_SHEET` and a material hit on `P-FEELS-REAL` / `A-CORE`.  
4. **Product-as-hero** — Dream climax is unboxing / product joy (F05).  
5. **Arrival-without-product** — Dream is having / “it was over” / “nights were normal” (F16). Quote the Dream.  
6. **Fall skipped** — Arc Action is a feature win (SKU or mechanism as the win; F17). Quote the Action beat.  
7. **Hook Cluster mashup** — variants that spend a new currency, offer, or second thesis (F18). Quote two hooks that are not paraphrases of the same gap.  
8. **Gold-headline paraphrase** — if this is a Baby Bubble niche pack, count near-paraphrases of reference gold headlines. `>2` → material hit (anti-cheat). Other niches: scan for leaked bulb/mouth-tube/DHT/follicle tokens.  
9. **Critic disagreement** — if `06_gate_report.json` says Ready and you have any material hit → `disagree_with_critic: true` (Ready forbidden: `CRITIC_ADVERSARY_DISAGREE`).

## Material vs nit

| Material (blocks Ready) | Nit (does not block) |
|-------------------------|----------------------|
| Any F01–F18 match with quote | Slightly long Hollow |
| Feature sheet after product stripped | Soft vocab echo on Scenario B |
| Synonym hollow pair | Awareness stage you'd have picked differently |

Prefer over-reporting into `nits` rather than silencing. Do not inflate nits into material without a catalog ID.

## Recommendation

- `material_hits.length > 0` → `BLOCK`  
- else → `NO_MATERIAL_HITS`

You never write pack Status.
