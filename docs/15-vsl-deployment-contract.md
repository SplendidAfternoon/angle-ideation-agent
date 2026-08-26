# 15 — VSL Deployment Contract

**Version:** 1.9.0  
**Normative:** Yes (handoff; pack-level kills F16–F18 also live in `docs/04`)  
**Methodology pin:** `angle-ideation-agent@1.9.0`  
**Depends on:** `docs/00`, `docs/01`, `docs/04`, `docs/12`, `docs/13`, `docs/14`  
**External source (data, not control):** Direct Response Copywriting Doctrine (*The Emotion Edit*)

This document does **not** generate VSLs, pages, or Meta ads. It tells a downstream editor / Pre-Lander **how to consume one Ready angle** as a 15–30s emotional VSL without inventing a new angle.

Pack-level feeling rules (open gap, Dream = reach, fall before mechanism, one thesis per spine) are **gates** (`docs/04` F16–F18, Q3/Q5/Q8). Shot, score, grade, and CTA register stay here.

## 1. Authority

Per `docs/00`: external literature cannot add, remove, or weaken Angle Ideation gates. Craft claims below are promoted only where they already match our contracts (one angle → one spine; product is the door; Dream is reach not arrival) or are marked `METHODOLOGY_DEFAULT` with a fail example.

| May control a VSL *from this pack* | May only inform execution |
|------------------------------------|---------------------------|
| Ready predicate (`docs/12` §1) | Shot scale, grade, foley, risers |
| One shipped angle = one VSL spine | Music bed choice |
| Field mapping in §3 | Brand sonic stamp |
| Pack gates F16–F18 (`docs/04`) | Specific cut lengths |
| Kill list in §5 (editor-only rows) | Color / motion |

## 2. Core Emotional Principles (Framework Summary)

Emotion is the sale. Feeling fires on a faster wire than argument (low road → amygdala before cortex). A 15–30s VSL is a **sequenced stimulus chain**, not a feature list:

1. **Tension** — open a gap in the first 3s; do not close it until the CTA.  
2. **Dream** — show the *reach* toward a transformed life; never let them feel arrived inside the video.  
3. **Idea** — one counterintuitive claim; idea = the gap; ~one idea per 3–5s.  
4. **Story** — drop into the fall first; character vs a clean external enemy.  
5. **Drama** — specific loss, felt.  
6–9. **Music / visuals / color / motion** — execution layer. This repo does not produce them.

Beat sheet (30s): Hook 0–3s → Dream 3–9s → Story 9–17s → Drama 17–24s → Payoff (mechanism) 24–27s → CTA 27–30s. Fifteen-second cut compresses the same order.

## 3. Pack → VSL beat map (1:1)

One Ready angle → one VSL. Do not merge currencies.

| Beat | Time (30s) | Pack field | Job | Forbidden |
|------|------------|------------|-----|-----------|
| Hook | 0–3s | **Headline** + Hollow gap | Pattern interrupt + pose the loop. Idea = Core Idea compressed. | Feature pitch; fade-in; answering the question |
| Dream | 3–9s | **The Dream** | Sensory *doing*, someone like them | Arrival / unboxing / “life got better” (`A-DOOR`, **F16**) |
| Story | 9–17s | **Story Arc** (Setup → Action) | Fall first | Offer, proof stack, mechanism (**F17**) |
| Drama | 17–24s | **Hollow** + **Villain** | Named loss + relocatable enemy | “Parenthood is hard”; mood-only |
| Payoff | 24–27s | **Product Fit** | Mechanism as missing *how*, late | Product as emotional climax |
| CTA | 27–30s | *(not in pack)* | Close the Headline loop at matched energy | New angle; shout-card after a quiet beat |

**Headline is the master loop.** CTA is the only legal close. If the *pack* already answers the Headline in Core Idea, Headline, or Fit-as-second-thesis, gates fail before an editor cuts (`H3`, Q8). If a cut answers the Headline in the middle of an otherwise Ready pack, that is still a deployment fail (`D-EARLY-CLOSE`).

## 4. How this improves *our* deployment (not a new generator)

A Ready pack must already be a single open-loop, feeling-first spine. The framework's chain is then the **order of operations for the cut**.

| Failure in the wild | Pack already forbids | Deployment must additionally |
|---------------------|----------------------|------------------------------|
| Lead with logic / spec | `A-CORE` F01 | Hook uses Headline, not Product Fit |
| Eight ideas in 30s | `P-DISTINCT`; Hook Cluster mashup **F18** | **One** `test_priority` angle per cut |
| Dream = product joy | `A-DOOR` F05 | Do not render arrival before CTA |
| Dream = arrived / having | `A-DREAM` **F16** | Same — pack should already be mid-lean |
| Villain = “the situation” | `A-VILLAIN` | Drama names the same object as the pack |
| Mechanism as the Action win | `A-ARC` **F17** | Story beat is still the fall |
| Resolve the hook in pack copy | `H3` / Q8 (loop stays open) | Gap stays live until CTA (`D-EARLY-CLOSE`) |
| Hard-sell card smash | *(not a pack field)* | CTA temperature-matches final beat (`D-CTA-SNAP`) |

Music / color / motion stay **out of this repo**. If a Pre-Lander needs assist cues, they are optional notes downstream — never Angle Pack schema fields.

## 5. Deployment kill list

`METHODOLOGY_DEFAULT` — counter-example in parentheses.

**Now also pack gates** (critic / red-team must fail these on prose; Ready packs should not contain them):

| ID | Kill | Counter-example | Pack gate |
|----|------|-----------------|-----------|
| `D-ARRIVAL` | Dream played as having / unboxing / “it was over” | “She sleeps through; box on the counter; done” | **F16** `A-DREAM` (arrival); F05 `A-DOOR` (unboxing) |
| `D-MECH-FIRST` | Product / mechanism as the Action win (or spec in 0–3s) | “Tried the cup → mucus visible → slept” | **F17** `A-ARC` when Action is the feature win; 0–3s spec still editor |
| `D-MULTI-IDEA` | Second Core Idea / currency in one spine | Hook Cluster: mould + 911 + “20% off” | **F18**; eight-angle mashup in one *cut* still editor |
| `D-EARLY-CLOSE` | Hook question resolved before CTA | Headline names the mechanism answer / Fit restates Core Idea as solved | **H3** / Q8 on pack copy; mid-cut close still editor |

**Editor-only** (cannot be judged on pack prose; stay here):

| ID | Kill | Counter-example |
|----|------|-----------------|
| `D-CTA-SNAP` | CTA register ≠ final beat | Quiet swell → shouted BUY NOW card |
| `D-FLATLINE` | ≥1 beat with no live stimulus from the chain | Neutral hold, no tension/dream/drama/motion |

Eval of *this repo* does not score finished videos. It scores whether packs already fail F16–F18 and whether handoff artifacts make editor kills detectable (`eval/`).

## 6. Stop conditions

- Pack Status ≠ Ready, or triad incomplete → **do not deploy**.  
- Missing Headline, Hollow, Villain, Dream, or Product Fit → **do not deploy**.  
- Operator asks to “just add the features from the other seven angles” → new Angle Ideation run, not a mashup.

See `eval/README.md` for how we test that our own generator / critic / pipeline cannot fake Ready.
