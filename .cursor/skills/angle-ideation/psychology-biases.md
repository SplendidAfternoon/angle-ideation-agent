# Psychology & bias protocol (assist only)

**Role:** Optional fetch during **candidate mining / scoring**.  
**Canonical catalog:** [`docs/10-cognitive-biases-heuristics-catalog.md`](../../../docs/10-cognitive-biases-heuristics-catalog.md)  
**Not** a substitute for AngleFuel, psychosocial currencies, or gates.  
**Ban:** Core Idea = “we use [bias name]” (fails `A-CORE`).

Methodology pin: `angle-ideation-agent@1.6.1`

## How to use

1. After AngleFuel exists, optionally set on a candidate:
   ```json
   "assist_notes": { "bias_id": "BIAS_LOSS_AVERSION", "attach_to": "Hollow" }
   ```
2. Max **one dominant** assist per shipped angle.  
3. Must bind to fuel evidence — else drop.  
4. Spine remains Currency + Hollow + Villain + Dream + belief move.  
5. For full families / A–Z lookup → read **docs/10**.

## Top-leverage quick table (DTC / angles)

| id | Name | Currency hints | Attach | Reject |
|----|------|----------------|--------|--------|
| `BIAS_LOSS_AVERSION` | Loss aversion | `RELATIONAL_EQUITY` `IDENTITY_SELFHOOD` `FUTURE_SECURITY` `SAFETY_SECURITY` | Hollow | Generic FOMO Core Idea |
| `BIAS_SUNK_COST` | Sunk cost | `AGENCY_CONTROL` `GUILT_REGRET` | Action | Mocking the avatar |
| `BIAS_STATUS_QUO` | Status quo | `TRUST_SAFETY` `AGENCY_CONTROL` | Villain | Shaming non-switchers |
| `BIAS_AUTHORITY` | Authority | `TRUST_SAFETY` `AUTHORITY` | Villain | Fake doctors |
| `BIAS_SOCIAL_PROOF` | Social proof | `SOCIAL_STATUS` | Hollow | Forged “everyone loves X” |
| `BIAS_COMMITMENT` | Commitment/consistency | `IDENTITY_SELFHOOD` `GUILT_REGRET` | Hollow | “You already agreed to buy” |
| `BIAS_AVAILABILITY` | Availability | `SAFETY_SECURITY` | Hollow | Invented catastrophe |
| `BIAS_DISGUST` | Disgust/contamination | `TRUST_SAFETY` `AGENCY_PARTNERSHIP` `BODILY_AUTONOMY` | Villain | Gross-out sans mechanism |
| `BIAS_LEARNED_HELPLESS` | Learned helplessness | `AGENCY_CONTROL` | Hollow/Twist | Hopeless ending |
| `BIAS_AMBIGUITY_AVERSION` | Ambiguity aversion | `AUTHORITY` `AGENCY_CONTROL` | Villain | Fearmongering off-fuel |
| `BIAS_PRESENT` | Present bias | `FUTURE_SECURITY` | Twist | Fake timers |
| `BIAS_IDENTITY_PROTECTIVE` | Identity-protective | `IDENTITY_SELFHOOD` | tone/Twist | Ego threat / defensiveness |
| `BIAS_ENDOWMENT` | Endowment / default cling | `TRUST_SAFETY` | Villain | Shaming ownership |
| `BIAS_SPOTLIGHT` | Spotlight effect | `SOCIAL_STATUS` | Hollow | Invented mockery |
| `BIAS_REACTANCE` | Reactance | tone | Verdict tone | Hard-sell Verdict |

## Debate heuristics (allowed vs reject)

**Allowed (Twist/Verdict/tone):**  
`DEBATE_WRONG_ENEMY`, `DEBATE_REFRAME`, `DEBATE_STEELMAN`, `DEBATE_DISTINCTION`, `DEBATE_REDUCTIO_CAT`, `DEBATE_CONCESSIVE`, `DEBATE_NON_ID_BLAME`, `DEBATE_CRITERIA`

**Reject as method / expose only as villain:**  
`FALLACY_STRAWMAN` (never on avatar), `FALLACY_MOTTE_BAILEY`, `FALLACY_AD_HOMINEM`, `FALLACY_FALSE_DILEMMA` (don’t create to sell), `HEUR_SCARCITY` as Core Idea

## Dark-pattern bans (never)

Fake timers, forged testimonials/stats, scarcity-as-Core-Idea, strawmanning the avatar, motte-and-bailey selling, clinical diagnosis copy, bias salad (3+ stacked as the story).

Full ban table + complete catalog: **docs/10**.
