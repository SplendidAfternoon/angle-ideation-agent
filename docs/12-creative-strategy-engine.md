# 12 — Creative Strategy Engine

**Version:** 1.9.0
**Normative:** Yes
**Methodology pin:** `angle-ideation-agent@1.9.0`

## 1. The Purpose of the Strategy Engine

Basic copywriting matches a product feature to a consumer pain point. Elite D2C creative strategy goes deeper: it maps a product to a biological drive, diagnoses the market's awareness/sophistication, and deliberately positions the brand against (or with) macroscopic cultural currents. 

Before generating any angles, the agent must define the **Strategy Fingerprint** using the four pillars below.

---

## 2. Pillar 1: Market Sophistication (Eugene Schwartz)

Angles must match how saturated the market is. Selling a "new mechanism" to a Level 1 market causes confusion; selling a "basic claim" to a Level 5 market causes ad blindness.

| Level | State of the Market | Strategy & Angle Approach |
|-------|---------------------|---------------------------|
| **L1: New** | They have the problem but have never seen a solution like yours. | **The Promise:** Make a direct, massive claim. No need to explain the deep mechanics yet. |
| **L2: Growing** | Competitors have entered. The basic claim isn't enough. | **The Expansion:** Enlarge the claim. "Faster, easier, lasts longer." |
| **L3: Crowded** | Market is jaded by big claims. They need proof. | **The New Mechanism:** Introduce the unique mechanism. Focus on *how* it works (the secret sauce) rather than just what it does. |
| **L4: Saturated** | Competitors have copied your mechanism. | **The Expanded Mechanism:** Make the mechanism faster/better, or combine it with another benefit. |
| **L5: Jaded** | The market no longer believes any product claims. | **Identity & Emotion:** Abandon feature claims entirely. Shift 100% to brand, identity, status, or absurdist entertainment. |

---

## 3. Pillar 2: Cultural Positioning Matrix

How does this angle relate to the current cultural zeitgeist? The brand cannot always be the "rebel"—it must choose a deliberate cultural stance.

| Position | The Play | When to use | Angle Vibe |
|----------|----------|-------------|------------|
| **The Amplifier** | Riding the zeitgeist. Validating what people already want to be part of. | When a trend is highly aspirational (e.g., Quiet Luxury, Gut Health, Clean Aesthetic). | "This is your shortcut to the lifestyle you're obsessed with." (Aspirational) |
| **The Subverter** | Fighting the zeitgeist. Calling out a toxic cultural norm. | When the audience is exhausted by a trend (e.g., Anti-hustle, toxic beauty standards). | "You don't need to do *more*. The industry lied to you." (Contrarian/Rebel) |
| **The Oasis** | Escaping the zeitgeist. Providing analog joy and simplicity. | Comfort products, nostalgia, offline hobbies, simple single-ingredient items. | "Put the phone down. Remember what this felt like?" (Relief/Nostalgia) |
| **The Micro-Culture** | Creating a new zeitgeist. Ignoring the mainstream for an IYKYK club. | High-end streetwear, hype drops, hyper-niche enthusiast gear. | "Not for everyone. And that's the point." (Exclusivity/Status) |

---

## 4. Pillar 3: Evolutionary Primal Desires

Every angle must anchor its psychological currency to one of the fundamental human biological drives (adapted from Drew Eric Whitman's Life-Force 8). Superficial benefits must map to these primal imperatives.

1. **Survival, enjoyment of life, life extension** (Health, biohacking, safety)
2. **Enjoyment of food and beverage** (Sensory pleasure, taste, cravings)
3. **Freedom from fear, pain, and danger** (Anxiety relief, security, predictability)
4. **Sexual companionship / Mating** (Attraction, confidence, beauty, vitality)
5. **Comfortable living conditions** (Aesthetics, coziness, frictionless environment)
6. **To be superior, winning, keeping up with the Joneses** (Status, luxury, exclusivity, competence)
7. **Care and protection of loved ones** (Parenting, pet care, family safety)
8. **Social approval / Belonging** (Community, fitting in, avoiding embarrassment)

---

## 5. Pillar 4: The Tonal Palette

An angle's tone is the vehicle that bypasses ad fatigue. The agent must select a tone that matches the strategy.

| Tone | Description | Best paired with |
|------|-------------|------------------|
| **Absurdist / Satirical** | Self-aware hyperbole. Uses melodrama to make a mundane problem funny. Shatters the 4th wall. | L4/L5 Sophistication, Low-stakes products, The Subverter. |
| **Confessional / Raw** | High emotional intensity. Vulnerable, "3 AM" thoughts. Visceral language. | L2/L3 Sophistication, High-pain products (health, relationships). |
| **Clinical / Authoritative** | Expert breakdown. Objective, precise, dismantling myths. | L3 Sophistication (New Mechanism), The Subverter. |
| **Prestige / Understated** | Effortless, minimal, "IYKYK". Doesn't try too hard to sell. | L5 Sophistication, The Amplifier, The Micro-Culture. |
| **Warm / Nostalgic** | Gentle, comforting, familiar, analog. | The Oasis, Comfort products. |

---

## 6. The Strategy Fingerprint (Output Schema)

When drafting angles, the agent must output a Strategy Fingerprint combining these elements. This replaces relying purely on "biases."

**Example Strategy Fingerprint for a high-end Matcha whisk:**
*   **Demographic:** High-Income Millennials
*   **Sophistication:** L5 (Jaded - everyone sells matcha)
*   **Cultural Position:** The Amplifier (Riding the "Slow Morning / Aesthetic" trend)
*   **Primal Desire:** Comfortable living conditions & Social approval
*   **Tone:** Prestige / Understated
*   **Cognitive Load:** Low (Frictionless - aesthetic visual focus)
*   **Bias Route:** Social/Identity biases
*   **Resulting Angle:** Focuses on the ritual and the aesthetic proof of having your life together, not the "pain" of clumpy tea.

---

## 7. Pillar 5: The Smart Bias Router & Persona Fluency

To prevent the agent from blindly applying random biases from `docs/10`, the agent must now route cognitive science pragmatically based on the demographic.

1. **Target Demographic:** Define the core avatar (e.g., Affluent Boomers, Stressed Millennials).
2. **Persona-Matched Cognitive Load:** Determine the required syntax complexity.
   - *Low (Frictionless):* For impulse buys, high-stress avatars. Short sentences, highly visceral.
   - *Medium/High (Clinical):* For high-ticket, B2B, or high-consideration products where the avatar requires technical depth or jargon to build trust.
3. **Bias Category Routing:** Based on the demographic, restrict the agent to a specific subset of `docs/10` (e.g., "Social/Identity biases" for Gen Z apparel, or "Loss Aversion/Risk biases" for legacy financial products).
