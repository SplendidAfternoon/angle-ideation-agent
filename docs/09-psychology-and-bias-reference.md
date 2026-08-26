# 09 — Psychology & Bias Reference (Policy)

**Version:** 1.9.0  
**Methodology pin:** `angle-ideation-agent@1.9.0`  
**Normative role:** Assistive only (not a gate source)

## Canonical vs runtime

| Artifact | Role |
|----------|------|
| [`docs/10-cognitive-biases-heuristics-catalog.md`](10-cognitive-biases-heuristics-catalog.md) | **Canonical** comprehensive catalog (biases, heuristics, debate) |
| [`.cursor/skills/angle-ideation/psychology-biases.md`](../.cursor/skills/angle-ideation/psychology-biases.md) | **Runtime protocol** + top-leverage quick table for the skill |

## When to use

- Optional fetch during candidate mining / scoring (after AngleFuel)  
- Map at most one dominant `bias_id` into `assist_notes`  
- Debate heuristics for Twist/Verdict reframe — never to strawman the avatar  

## When not to use

- As the primary angle generator  
- To invent pains/beliefs absent from AngleFuel  
- To justify dark patterns (see bans in docs/10 §0)  
- As Core Idea text (“we use loss aversion”) — fails `A-CORE`  

Agents running `angle-ideation` should load the skill protocol first; open **docs/10** when they need full lookup or debate/fallacy coverage.

## Foundational Frameworks

### Regulatory Focus Theory (Higgins)
Promotion focus (gains, aspirations, ideals) vs Prevention focus (losses, safety, oughts). The current system is 100% prevention-focused; v1.7.0 adds promotion-focused angle support.

### Information Gap Theory (Loewenstein)
Curiosity is triggered by a gap between what you know and what you want to know. This theory enables open-loop and curiosity headline formats.

### Fogg Behavior Model (B=MAP)
Behavior = Motivation × Ability × Prompt. The system currently only addresses Motivation (pain/relief) and v1.7.0 adds Ability (ease/simplicity in Product Fit) consideration.

### Narrative Transportation (Green & Brock)
Being absorbed in a story reduces counterarguing. Archetype diversity supports deeper transportation.

### Elaboration Likelihood Model (Petty & Cacioppo)
Central vs peripheral processing. This links to awareness stage diversity.
