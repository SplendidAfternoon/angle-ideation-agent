# 10 — Cognitive Biases & Heuristics Catalog (Assist Layer)

**Version:** 1.9.0  
**Methodology pin:** `angle-ideation-agent@1.9.0`  
**Normative role:** Assistive only — **not** a gate source, **not** an angle engine  
**Depends on:** [`docs/01`](01-angle-pack-schema.md) currencies, [`docs/03`](03-angle-generation-methodology.md) Q1–Q8, [`docs/00`](00-source-hierarchy-and-trust.md) trust  
**Runtime protocol:** [`.cursor/skills/angle-ideation/psychology-biases.md`](../.cursor/skills/angle-ideation/psychology-biases.md)

---

## 0. Binding rules (normative)

1. Fetch this catalog **only** during candidate mining / scoring (after AngleFuel exists).  
2. Max **one dominant** `bias_id` assist per shipped angle (`assist_notes`).  
3. Assist must bind to fuel evidence (`pain_refs` / `failed_attempts` / vocabulary). No fuel → drop assist.  
4. **Core Idea must never be** “we use [bias/heuristic name].” That fails `A-CORE` (failure catalog F01 class).  
5. Spine remains: Currency + Hollow + Villain + Dream + belief move + Product Fit.  
6. Social-influence entries diagnose **avatar beliefs**, not instructions to forge proof.  
7. Debate section: use **reframe / steelman / wrong-enemy** tools on *category/advice villains*; never strawman the avatar.

### Dark-pattern ban list (never “allowed angle use”)

| Ban ID | Pattern | Why banned |
|--------|---------|------------|
| `BAN_FAKE_TIMER` | Fake countdown / false scarcity as the angle | Manufactured urgency; not fuel belief |
| `BAN_FORGED_PROOF` | Invented testimonials, fake stats, fake authority | Violates grounding / trust protocol |
| `BAN_SCARCITY_CORE` | Core Idea = “only N left” | Offer/claim, not emotional angle |
| `BAN_STRAWMAN_AVATAR` | Misrepresent avatar’s beliefs to dunk on them | Breaks voice + ethics |
| `BAN_MOTTE_BAILEY` | Sell extreme claim, retreat to mild claim | Deceptive debate method |
| `BAN_DIAGNOSIS_COPY` | Clinical labels as copy claims (“you have X disorder”) | Out of scope |
| `BAN_BIAS_SALAD` | Stacking 3+ biases as the story | Collapses distinct currencies |

### Entry schema

Tables use: **id** | **Name** | **Plain meaning** | **Currency hints** | **Attach** | **Allowed** | **Reject**

- **Attach:** `Hollow` `Villain` `Dream` `Twist` `Verdict` `Action` `tone`  
- **Currency hints:** only IDs from `docs/01` §4  

Optional candidate field:

```json
"assist_notes": { "bias_id": "BIAS_LOSS_AVERSION", "attach_to": "Hollow" }
```

---

## 1. Memory & salience

| id | Name | Plain meaning | Currency hints | Attach | Allowed | Reject |
|----|------|---------------|----------------|--------|---------|--------|
| `BIAS_AVAILABILITY` | Availability bias | What comes to mind easily feels more common/true | `SAFETY_SECURITY` `AUTHORITY` | Hollow, Action | Night cues / vivid fuel examples dominate attention | Invent rare catastrophe |
| `BIAS_RECENCY` | Recency effect | Latest events overweight judgment | `SAFETY_SECURITY` `FUTURE_SECURITY` | Hollow, Action | Last night’s scare / last failed try | Ignoring long pattern in fuel |
| `HEUR_SALIENCE` | Salience heuristic | Loud/bright features drive choice | `SOCIAL_STATUS` `SAFETY_SECURITY` | Hollow | Flash photos, gurgling, visible scalp | Decoration that aren’t in fuel |
| `BIAS_VON_RESTORFF` | Von Restorff / isolation effect | Distinct items remembered more | `IDENTITY_SELFHOOD` `SOCIAL_STATUS` | Dream, Headline | One concrete sensory contrast | Gimmick-only hooks without genuine friction |
| `BIAS_ATTENTIONAL` | Attentional bias | Threat-relevant cues capture attention | `SAFETY_SECURITY` | Hollow, Action | Hypervigilant scanning loops | Constant alarmism without Verdict |
| `BIAS_MEMORY_NEGATIVITY` | Negativity bias (memory) | Negative events stick harder | `GUILT_REGRET` `RELATIONAL_EQUITY` | Hollow | Named loss that won’t leave | Pure doom without doorway |
| `BIAS_PEAK_END` | Peak-end rule | Peak + ending shape remembered episode | `IDENTITY_SELFHOOD` `GENTLENESS` | Dream, Action | Emotional peak → calm ending | Unrealistic dramatization |
| `BIAS_ROSY_RETROSPECTION` | Rosy retrospection | Past self idealized | `IDENTITY_SELFHOOD` `RELATIONAL_EQUITY` | Setup, Dream | “Who we were before” Setup | Nostalgia-only with no villain |
| `BIAS_FADING_AFFECT` | Fading affect bias | Emotion of memories fades unevenly | `GUILT_REGRET` | Hollow | Guilt that didn’t fade | Claiming trauma clinically |
| `BIAS_CONTEXT_DEP_MEMORY` | Context-dependent memory | Cues in context retrieve states | `SAFETY_SECURITY` `IDENTITY_SELFHOOD` | Hollow, Dream | Same kitchen / same bathroom mirror | Arbitrary scene unrelated to fuel |

---

## 2. Probability & uncertainty

| id | Name | Plain meaning | Currency hints | Attach | Allowed | Reject |
|----|------|---------------|----------------|--------|---------|--------|
| `HEUR_REPRESENTATIVENESS` | Representativeness heuristic | Stereotypes substitute for base rates | `AUTHORITY` `SOCIAL_STATUS` | Twist | Expose bad “looks like care” rituals | Stereotyping demographic groups |
| `BIAS_BASE_RATE` | Base-rate neglect | Ignore background frequencies | `SAFETY_SECURITY` `AUTHORITY` | Twist, Verdict | Reframe wrong diagnosis (tool vs person) | Fake statistics |
| `BIAS_AMBIGUITY_AVERSION` | Ambiguity aversion | Prefer known risks over vague ones | `AUTHORITY` `AGENCY_CONTROL` | Villain, Hollow | Opaque tools / forum fog | Fear of unknown without fuel |
| `BIAS_OPTIMISM` | Optimism bias | Underestimate personal bad outcomes | `FUTURE_SECURITY` | Twist | “I still have time” calendar trap | Shaming hope itself |
| `BIAS_PESSIMISM` | Pessimism bias | Overweight personal doom | `SAFETY_SECURITY` `GUILT_REGRET` | Hollow | Spirals evidenced in fuel | Invented hopelessness |
| `BIAS_GAMBLERS` | Gambler’s fallacy | Past random outcomes change next odds | `AGENCY_CONTROL` | Action | “This next bottle will break the streak” | Encouraging gambling framing |
| `BIAS_HOT_HAND` | Hot-hand fallacy | Streaks seen as skill | `AGENCY_CONTROL` | Action | False confidence after one good night | Promising streaks |
| `BIAS_CLUSTERING_ILLUSION` | Clustering illusion | See patterns in noise | `AUTHORITY` | Twist | Category “upgrades” that aren’t | Conspiracy cosmology |
| `BIAS_INSENSITIVITY_SAMPLE` | Insensitivity to sample size | Small samples overtrusted | `TRUST_SAFETY` `AUTHORITY` | Villain | One anecdotal “hack” as gospel | Fake large-N claims |
| `BIAS_NORMALCY` | Normalcy bias | Underreact because “this is fine” | `SAFETY_SECURITY` `FUTURE_SECURITY` | Twist | “It’s just a phase” advice villain | Fear-mongering / alarmism |
| `BIAS_ZERO_RISK` | Zero-risk bias | Prefer eliminating one small risk entirely | `SAFETY_SECURITY` `TRUST_SAFETY` | Dream, Verdict | “Nothing sealed to grow” cleanliness | Claiming absolute zero risk |
| `BIAS_OUTCOME` | Outcome bias | Judge decision by result not process | `GUILT_REGRET` `AUTHORITY` | Hollow | Self-blame for bad night despite good intent | Blaming avatar as stupid |
| `BIAS_HINDSIGHT` | Hindsight bias | “I knew it all along” after outcome | `GUILT_REGRET` | Hollow, Twist | Regret of missed earlier fix | Omniscient narrator dunk |

---

## 3. Loss, risk & motivation

| id | Name | Plain meaning | Currency hints | Attach | Allowed | Reject |
|----|------|---------------|----------------|--------|---------|--------|
| `BIAS_LOSS_AVERSION` | Loss aversion | Losses outweigh equivalent gains | `RELATIONAL_EQUITY` `IDENTITY_SELFHOOD` `FUTURE_SECURITY` `SAFETY_SECURITY` | Hollow | Named concrete loss in scene | Generic FOMO Core Idea |
| `BIAS_SUNK_COST` | Sunk cost fallacy | Past spend justifies continuing | `AGENCY_CONTROL` `GUILT_REGRET` | Action | Lined-up failed purchases | Mocking the avatar |
| `BIAS_EFFORT_JUSTIFICATION` | Effort justification | Hard effort makes outcome feel worthier | `AGENCY_CONTROL` `IDENTITY_SELFHOOD` | Action | Painful rituals kept because “I suffered” | Glorifying suffering |
| `BIAS_IKEA` | IKEA effect | Labor increases valuation | `AGENCY_CONTROL` | Action | DIY hacks clung to | Irrelevant craft metaphors |
| `BIAS_ENDOWMENT` | Endowment effect | Owned default valued higher | `TRUST_SAFETY` `AGENCY_CONTROL` | Villain | Hospital bulb / default foam kept | Shaming ownership |
| `BIAS_REGRET_AVERSION` | Regret aversion | Avoid actions that might cause regret | `GUILT_REGRET` `FUTURE_SECURITY` | Hollow, Dream | Fear of starting wrong vs delaying | Paralysis with no Verdict |
| `BIAS_RISK_COMPENSATION` | Risk compensation | Feeling safer → riskier behavior | `SAFETY_SECURITY` | tone | Soft; rarely primary | Encouraging reckless use |
| `HEUR_AFFECT` | Affect heuristic | Feelings substitute for risk analysis | `SAFETY_SECURITY` `GENTLENESS` | Hollow | Disgust/fear from fuel drives tool choice | Pure emotional manipulation sans mechanism |
| `BIAS_PSEUDOCERTAINTY` | Pseudocertainty effect | Framing makes uncertain outcomes feel sure | `AUTHORITY` | Villain | “Hospital-grade” empty certainty | Fabricating certainty claims |

---

## 4. Social influence (diagnose avatar beliefs)

| id | Name | Plain meaning | Currency hints | Attach | Allowed | Reject |
|----|------|---------------|----------------|--------|---------|--------|
| `BIAS_SOCIAL_PROOF` | Social proof | Others’ behavior as cue | `SOCIAL_STATUS` | Hollow | Public failure / audience pressure | “Everyone loves X” as Core Idea; forged proof |
| `BIAS_AUTHORITY` | Authority bias | Over-trust credentials/defaults | `TRUST_SAFETY` `AUTHORITY` | Villain | Bad hospital advice / guru protocol | Fake doctors |
| `BIAS_LIKING` | Liking bias | Prefer people we like | `RELATIONAL_EQUITY` `SOCIAL_STATUS` | tone | Partner/family scenes | Parasocial fake friends |
| `BIAS_RECIPROCITY` | Reciprocity | Felt debt after receiving | `RELATIONAL_EQUITY` `AGENCY_PARTNERSHIP` | Action | Soft; gift dynamics if in fuel | Free-gift dark patterns |
| `BIAS_UNITY` | Unity bias | Shared identity increases influence | `IDENTITY_SELFHOOD` `RELATIONAL_EQUITY` | Setup | “We were a team” Setup | Fake tribe claims |
| `BIAS_CONFORMITY` | Conformity | Align with group norms | `SOCIAL_STATUS` | Hollow | Cap lifestyle / hide ritual | Shaming nonconformity |
| `BIAS_BANDWAGON` | Bandwagon effect | Join rising popularity | `SOCIAL_STATUS` `AGENCY_CONTROL` | Villain | Category trend without mechanism | “Viral so it works” |
| `BIAS_HALO` | Halo effect | One trait colors all judgment | `TRUST_SAFETY` `AUTHORITY` | Villain | Pretty packaging hides failure | Attacking aesthetics only |
| `BIAS_HORNS` | Horns effect | One bad trait colors all | `GUILT_REGRET` `IDENTITY_SELFHOOD` | Hollow | One bad night → “bad parent/person” | Character assassination |
| `BIAS_INGROUP` | In-group bias | Prefer own group | `SOCIAL_STATUS` `IDENTITY_SELFHOOD` | tone | Careful identity belonging | Out-group hostility |
| `BIAS_STEREOTYPE` | Stereotype bias | Group schemas distort judgment | `SOCIAL_STATUS` | Twist | Expose unfair audience judgment | Reinforcing harmful stereotypes |

---

## 5. Self & identity

| id | Name | Plain meaning | Currency hints | Attach | Allowed | Reject |
|----|------|---------------|----------------|--------|---------|--------|
| `BIAS_COMMITMENT` | Commitment & consistency | Stay aligned with prior self-image | `IDENTITY_SELFHOOD` `GUILT_REGRET` | Core-adjacent Hollow | Identity fracture when ritual fails | “You already said you’d buy” |
| `BIAS_IDENTITY_PROTECTIVE` | Identity-protective cognition | Reject info that threatens self | `IDENTITY_SELFHOOD` | Twist, tone | Externalize villain; soft doorway | Ego attack as strategy |
| `BIAS_SELF_SERVING` | Self-serving bias | Credit self for wins, blame context for losses | `GUILT_REGRET` `AGENCY_CONTROL` | Twist | Flip: tool blamed correctly | Excusing real harm |
| `BIAS_FUNDAMENTAL_ATTR` | Fundamental attribution error | Over-attribute to character not situation | `GUILT_REGRET` `SOCIAL_STATUS` | Twist | Audience blames mum/man not tool | Blaming avatar character |
| `BIAS_SPOTLIGHT` | Spotlight effect | Overestimate how much others notice | `SOCIAL_STATUS` | Hollow | Caps, hiding, photo dread | Inventing mockery not in fuel |
| `BIAS_TRANSPARENCY` | Illusion of transparency | Think others see our inner state | `SOCIAL_STATUS` `RELATIONAL_EQUITY` | Hollow | Partner misreads silence | Mind-reading claims |
| `BIAS_SELF_EFFICACY_GAP` | Self-efficacy collapse | Belief “I can’t execute” after failures | `AGENCY_CONTROL` `AUTHORITY` | Hollow | After category failures | Permanent helplessness |
| `BIAS_DUNNING_KRUGER` | Dunning–Kruger | Skill/confidence mismatch | `AUTHORITY` | Villain | Forum overconfidence as villain | Calling avatar stupid/unskilled |
| `BIAS_IMP_POSTER` | Impostor feelings (popular) | Success feels unearned / fraud | `IDENTITY_SELFHOOD` `SOCIAL_STATUS` | Hollow | Only if fuel shows it | Clinical impostor diagnosis |
| `BIAS_NAIVE_REALISM` | Naïve realism | “I see reality; others biased” | `AUTHORITY` `RELATIONAL_EQUITY` | Twist | Couple conflict over night strategy | Smug narrator |
| `BIAS_CONFIRMATION` | Confirmation bias | Seek supportive evidence | `AUTHORITY` `AGENCY_CONTROL` | Action | Forum cherry-picking | Instructing cherry-pick to sell |
| `BIAS_BACKFIRE` | Backfire effect (contested) | Strong challenge entrenches belief | `IDENTITY_SELFHOOD` | tone | Prefer soft shift | Aggressive correction |

---

## 6. Control & agency

| id | Name | Plain meaning | Currency hints | Attach | Allowed | Reject |
|----|------|---------------|----------------|--------|---------|--------|
| `BIAS_STATUS_QUO` | Status quo bias | Prefer current state | `TRUST_SAFETY` `AGENCY_CONTROL` | Villain | Default tool/advice inertia | Shame for not switching |
| `BIAS_DEFAULT` | Default effect | Preselected options stick | `TRUST_SAFETY` | Villain | Hospital-issued default | Dark default UI tricks |
| `BIAS_ILLUSION_CONTROL` | Illusion of control | Overestimate influence on chance | `AGENCY_CONTROL` | Action | Rituals that feel like control | Promising total control |
| `BIAS_LEARNED_HELPLESS` | Learned helplessness | Repeated failure → stop trying new paths | `AGENCY_CONTROL` | Hollow, Twist | Category trap → mechanism path | Hopeless ending |
| `BIAS_REACTANCE` | Reactance | Pushback when freedom threatened | tone `AGENCY_CONTROL` | tone, Verdict | Soft Product Fit doorway | Hard-sell Verdict |
| `BIAS_CHOICE_OVERLOAD` | Choice overload | Too many options impair choice | `AGENCY_CONTROL` `AUTHORITY` | Action | Shelf of aspirators/serums | Fake “only one left” |
| `BIAS_DECISION_FATIGUE` | Decision fatigue | Depleted choosing quality | `AGENCY_CONTROL` `IDENTITY_SELFHOOD` | Hollow | Night decision collapse | Excusing everything |
| `BIAS_OMISSION` | Omission bias | Harm via inaction feels better than action | `GUILT_REGRET` `FUTURE_SECURITY` | Twist | Delay vs starting | Pushing reckless action |
| `BIAS_ACTION_BIAS` | Action bias | Prefer doing something over nothing | `AGENCY_CONTROL` | Action | Impulse-buying tools without research | Busywork without mechanism |
| `BIAS_SYSTEM_JUSTIF` | System justification | Defend existing order | `TRUST_SAFETY` `AUTHORITY` | Villain | “That’s just how parenting/hair loss is” | Political propaganda |

---

## 7. Temporal

| id | Name | Plain meaning | Currency hints | Attach | Allowed | Reject |
|----|------|---------------|----------------|--------|---------|--------|
| `BIAS_PRESENT` | Present bias | Overweight now vs later | `FUTURE_SECURITY` | Hollow, Twist | Milestone calendar | Fake timers (`BAN_FAKE_TIMER`) |
| `BIAS_HYPERBOLIC` | Hyperbolic discounting | Steep short-term discounting | `FUTURE_SECURITY` `AGENCY_CONTROL` | Twist | Delay loop | Manufactured urgency Core Idea |
| `BIAS_PLANNING_FALLACY` | Planning fallacy | Underestimate time/effort | `AGENCY_CONTROL` `FUTURE_SECURITY` | Action | “I’ll start next month” | Unrealistic product timelines |
| `BIAS_PROJECTION` | Projection bias | Future preferences ≈ current | `IDENTITY_SELFHOOD` `FUTURE_SECURITY` | Hollow | Always-ON self feels permanent | Claiming permanence falsely |
| `BIAS_IMPACT` | Impact bias | Overestimate future emotion intensity | `SAFETY_SECURITY` `GUILT_REGRET` | Hollow | Soften with Dream render | Terror inflation |
| `BIAS_TIME_SAVING` | Time-saving bias | Misjudge time saved by tools | `AGENCY_CONTROL` | Verdict | Mechanism ends episode faster | Fake minute claims |

---

## 8. Framing & language

| id | Name | Plain meaning | Currency hints | Attach | Allowed | Reject |
|----|------|---------------|----------------|--------|---------|--------|
| `BIAS_FRAMING` | Framing effect | Same facts, different frame → different choice | all (careful) | Twist, Core | Loss frame for Hollow; mechanism frame for Verdict | Misleading frames vs fuel |
| `BIAS_ANCHORING` | Anchoring | First number/claim skews judgment | `AUTHORITY` `AGENCY_CONTROL` | Villain | Competitor claim anchors | Fake anchors |
| `BIAS_DECOY` | Decoy effect | Inferior option steers choice | `AGENCY_CONTROL` | Villain | Category “premium” decoys | Building decoy dark patterns |
| `BIAS_CONTRAST` | Contrast effect | Judgment relative to comparison | `SOCIAL_STATUS` `IDENTITY_SELFHOOD` | Hollow, Dream | Before/after sensory contrast | Fake before/after |
| `BIAS_EUPHEMISM` | Euphemism treadmill | Soft labels hide harsh realities | `TRUST_SAFETY` `AUTHORITY` | Villain | “Maturing hairline” / “just a phase” | Using euphemism to hide product limits |
| `BIAS_LEADING_QUESTION` | Leading question | Question wording steers answer | `AUTHORITY` | Villain | Bad advice questions | Leading the reader dishonestly |
| `HEUR_FLUENCY` | Processing fluency | Easy-to-process feels true | `AUTHORITY` `TRUST_SAFETY` | tone | Clear confession voice | Smooth lies |
| `BIAS_JARGON_FOG` | Jargon / mystification | Complexity signals false expertise | `AUTHORITY` | Villain | Forum protocol fog | Adding jargon to sell |

---

## 9. Judgment heuristics (named)

| id | Name | Plain meaning | Currency hints | Attach | Allowed | Reject |
|----|------|---------------|----------------|--------|---------|--------|
| `HEUR_AVAILABILITY` | Availability heuristic | Ease of recall ≈ probability | `SAFETY_SECURITY` | Hollow | Same as availability bias family | Invented vividness |
| `HEUR_REPRESENT` | Representativeness (heuristic form) | Similarity ≈ probability | `AUTHORITY` | Twist | Ritual “looks medical” | Stereotypes |
| `HEUR_AFFECT_J` | Affect heuristic (judgment) | Good/bad feeling guides risk | `GENTLENESS` `TRUST_SAFETY` | Hollow | Disgust/trust from tools | Feeling-only pitch |
| `HEUR_RECOGNITION` | Recognition heuristic | Recognized option preferred | `TRUST_SAFETY` `SOCIAL_STATUS` | Villain | Famous brand still fails | Fake fame |
| `HEUR_SATISFICE` | Satisficing | “Good enough” stops search | `AGENCY_CONTROL` | Action | Settling on bad default | Blocking better mechanism unfairly |
| `HEUR_TAKE_BEST` | Take-the-best | Decide on one discriminating cue | `AUTHORITY` | Verdict | One mechanism cue (see/clean/control) | Single fake cue |
| `HEUR_SIMULATION` | Simulation heuristic | Ease of imagining → judged likelier | `FUTURE_SECURITY` `SAFETY_SECURITY` | Dream, Hollow | Rendered Dream/Hollow | Fantasies off-fuel |
| `HEUR_EFFORT` | Effort heuristic | More effort ≈ more quality | `AGENCY_CONTROL` | Action | Painful rituals mistaken for efficacy | Glorifying grind |
| `HEUR_SCARCITY` | Scarcity heuristic | Rare ≈ valuable | `FUTURE_SECURITY` | — | **Almost never as angle** | `BAN_SCARCITY_CORE` / fake scarcity |
| `HEUR_DEFAULT_TRUST` | Trust heuristic | Familiar source ≈ safe | `TRUST_SAFETY` | Villain | Default tool betrayal | Blind trust claims for product |

---

## 10. Debate & rhetorical heuristics

### 10.1 Allowed (story / Twist / Verdict)

| id | Name | Plain meaning | Currency hints | Attach | Allowed | Reject |
|----|------|---------------|----------------|--------|---------|--------|
| `DEBATE_BURDEN` | Burden of proof shift (expose) | Who must prove what | `AUTHORITY` | Twist | Expose advice that demands avatar prove suffering | Shifting burden onto reader dishonestly |
| `DEBATE_STEELMAN` | Steelmanning | Strongest form of opposing view first | tone `TRUST_SAFETY` | Setup, Action | Grant why default tool seemed sensible | Using steelman to bury mechanism |
| `DEBATE_REFRAME` | Reframe / relabel | Change category of the problem | all | Twist, Core | Congestion→partnership; thinning→identity | Relabel that contradicts fuel |
| `DEBATE_WRONG_ENEMY` | Wrong-enemy pivot | Blame relocated to true agent | all | Twist, Villain | Tool/advice/category as enemy | Blaming the avatar |
| `DEBATE_DISTINCTION` | Distinction-drawing | Split conflated ideas | `AUTHORITY` `AGENCY_CONTROL` | Twist | Mechanism vs packaging; guilt vs tool | Pedantic splits without genuine tension |
| `DEBATE_REDUCTIO_CAT` | Reductio of category claim | Show category promise collapses | `AGENCY_CONTROL` | Twist | “Four boxes, same failure” | Strawman competitors unfairly |
| `DEBATE_CONCESSIVE` | Concessive opener | Admit opposing point then pivot | tone | Setup | “He isn’t useless — the tool blocked handoff” | Fake concessions |
| `DEBATE_NON_ID_BLAME` | Non-identity blame relocation | Separate person from fault object | `GUILT_REGRET` `IDENTITY_SELFHOOD` | Villain, Twist | Aligns with Hollow/Villain craft | Absolving real negligence when fuel says otherwise |
| `DEBATE_LEVELS` | Levels of analysis | Symptom vs mechanism vs meaning | `AUTHORITY` | Verdict | Mechanism layer unlock | Fake science layers |
| `DEBATE_CRITERIA` | Criteria contest | Change success metric | `AGENCY_CONTROL` `AUTHORITY` | Verdict | From “more suction” to “see + clean + control” | Moving goalposts deceptively |

### 10.2 Expose-as-villain / reject-as-method

| id | Name | Plain meaning | Use | Reject as method |
|----|------|---------------|-----|------------------|
| `FALLACY_STRAWMAN` | Straw man | Misrepresent opponent | Villain: advice that mislabels avatar | Never strawman avatar (`BAN_STRAWMAN_AVATAR`) |
| `FALLACY_MOTTE_BAILEY` | Motte-and-bailey | Extreme claim ↔ mild retreat | Villain: brand claim pattern | Never use (`BAN_MOTTE_BAILEY`) |
| `FALLACY_AD_HOMINEM` | Ad hominem | Attack person not claim | Villain: audience judgment | Never attack avatar |
| `FALLACY_FALSE_DILEMMA` | False dilemma | Only two options | Villain: oral-or-nothing / accept-or-fail | Don’t create false dilemmas to sell |
| `FALLACY_SLIPPERY` | Slippery slope | Unjustified cascade | Rare Hollow if fuel has cascade fear | Inventing cascades |
| `FALLACY_APPEAL_NATURE` | Appeal to nature | Natural = good | Villain: rosemary folklore | Don’t claim “natural hence works” |
| `FALLACY_APPEAL_TRAD` | Appeal to tradition | Old = correct | Villain: hospital bulb ritual | Tradition ≠ proof |
| `FALLACY_APPEAL_POP` | Appeal to popularity | Popular = true | Villain: bandwagon category | Popularity ≠ mechanism |
| `FALLACY_CIRCULAR` | Circular reasoning | Conclusion in premises | Villain: forum logic | Don’t circular-sell |
| `FALLACY_NO_TRUE_SCOTS` | No true Scotsman | Exclude counterexamples | Villain: “you didn’t try right” | Don’t gatekeep sufferers |
| `FALLACY_SPECIAL_PLEAD` | Special pleading | Uneven standards | Villain: category excuses | Don’t excuse product uniquely without mechanism |
| `FALLACY_EQUIVOCATION` | Equivocation | Word shifts meaning mid-argument | Villain: “hospital-grade” vagueness | Don’t equivocate in Product Fit |
| `FALLACY_LOADED` | Loaded question | Presupposes contested claim | Villain: shaming questions | Don’t load the reader |
| `FALLACY_WHATABOUT` | Tu quoque / whataboutism | Deflect via hypocrisy | Partner conflict tone caution | Don’t deflect product limits |
| `FALLACY_MIDDLE` | Middle-ground fallacy | Truth must be compromise | Rare | Fake compromise science |
| `FALLACY_ANECDOTE` | Misleading anecdote | Story replaces rates | Action confession OK; not proof | Invented anecdotes as evidence |

---

## 11. Contamination, disgust & purity

| id | Name | Plain meaning | Currency hints | Attach | Allowed | Reject |
|----|------|---------------|----------------|--------|---------|--------|
| `BIAS_DISGUST` | Disgust bias | Contamination cues drive avoidance | `TRUST_SAFETY` `BODILY_AUTONOMY` `AGENCY_PARTNERSHIP` `GENTLENESS` | Villain, Hollow | Mouth tube, mould, grease | Gross-out without mechanism |
| `BIAS_CONTAMINATION` | Magical contagion | Contact transfers essence | `TRUST_SAFETY` `BODILY_AUTONOMY` | Villain | Filter fear / shared mouth path | Irrational purity cult |
| `HEUR_PURITY` | Purity heuristic | Clean/closed feels morally safer | `TRUST_SAFETY` `GENTLENESS` | Dream, Verdict | See/clean/sterilise doorway | Shame about normal body fluids |
| `BIAS_OMNIVORE_PARADOX` | Omnivore’s paradox (applied) | Desire novelty vs fear contamination | `AGENCY_CONTROL` `TRUST_SAFETY` | Action | Trying new tools vs distrust | Irrelevant food metaphors |

---

## 12. Cross-cutting “angle craft” levers (not biases)

| id | Name | Attach | Notes |
|----|------|--------|-------|
| `CRAFT_CONFESSION` | Confession voice | Headline, Hollow | Diary, not ad-ese |
| `CRAFT_VILLAIN_OBJECT` | Concrete villain object | Villain, Twist | Required by `A-VILLAIN` |
| `CRAFT_SENSORY_DREAM` | Sensory dream anchor | Dream | Required by `A-DREAM` |
| `CRAFT_MECHANISM_KEY` | Mechanism as missing key | Verdict, Product Fit | Door not hero |
| `CRAFT_FAILED_RITUAL` | Failed ritual specificity | Action | From `failed_attempts` |

---

## 13. Quick map: common angle jobs → starter IDs

| Job | Starter assists |
|-----|-----------------|
| Nighttime vigilance / risk scanning | `BIAS_AVAILABILITY` `BIAS_ATTENTIONAL` `BIAS_NORMALCY` |
| Trusted tool betrays | `BIAS_AUTHORITY` `BIAS_ENDOWMENT` `BIAS_DISGUST` `BIAS_DEFAULT` |
| Bought everything | `BIAS_SUNK_COST` `BIAS_ACTION_BIAS` `BIAS_LEARNED_HELPLESS` `DEBATE_REDUCTIO_CAT` |
| Identity erased | `BIAS_COMMITMENT` `BIAS_PROJECTION` `BIAS_IDENTITY_PROTECTIVE` |
| Partnership / handoff | `BIAS_REACTANCE` (tone) `DEBATE_CONCESSIVE` `BIAS_DISGUST` |
| Public competence | `BIAS_SPOTLIGHT` `BIAS_SOCIAL_PROOF` `BIAS_CONFORMITY` |
| Guilt | `BIAS_HINDSIGHT` `BIAS_OUTCOME` `DEBATE_NON_ID_BLAME` |
| Milestone dread | `BIAS_PRESENT` `BIAS_OPTIMISM` `BIAS_LOSS_AVERSION` |
| Forum fog | `BIAS_CHOICE_OVERLOAD` `BIAS_CONFIRMATION` `BIAS_DUNNING_KRUGER` `DEBATE_CRITERIA` |
| Wrong enemy reveal | `DEBATE_WRONG_ENEMY` `DEBATE_REFRAME` `DEBATE_DISTINCTION` |

---

## 14. A–Z index (name → id)

| Name | id |
|------|-----|
| Action bias | `BIAS_ACTION_BIAS` |
| Ad hominem | `FALLACY_AD_HOMINEM` |
| Affect heuristic | `HEUR_AFFECT` / `HEUR_AFFECT_J` |
| Ambiguity aversion | `BIAS_AMBIGUITY_AVERSION` |
| Anchoring | `BIAS_ANCHORING` |
| Anecdote (misleading) | `FALLACY_ANECDOTE` |
| Appeal to nature | `FALLACY_APPEAL_NATURE` |
| Appeal to popularity | `FALLACY_APPEAL_POP` |
| Appeal to tradition | `FALLACY_APPEAL_TRAD` |
| Attentional bias | `BIAS_ATTENTIONAL` |
| Authority bias | `BIAS_AUTHORITY` |
| Availability bias/heuristic | `BIAS_AVAILABILITY` / `HEUR_AVAILABILITY` |
| Backfire effect | `BIAS_BACKFIRE` |
| Bandwagon | `BIAS_BANDWAGON` |
| Base-rate neglect | `BIAS_BASE_RATE` |
| Burden of proof (expose) | `DEBATE_BURDEN` |
| Choice overload | `BIAS_CHOICE_OVERLOAD` |
| Circular reasoning | `FALLACY_CIRCULAR` |
| Clustering illusion | `BIAS_CLUSTERING_ILLUSION` |
| Commitment & consistency | `BIAS_COMMITMENT` |
| Concession (concessive opener) | `DEBATE_CONCESSIVE` |
| Confirmation bias | `BIAS_CONFIRMATION` |
| Conformity | `BIAS_CONFORMITY` |
| Contamination (magical contagion) | `BIAS_CONTAMINATION` |
| Context-dependent memory | `BIAS_CONTEXT_DEP_MEMORY` |
| Contrast effect | `BIAS_CONTRAST` |
| Criteria contest | `DEBATE_CRITERIA` |
| Decoy effect | `BIAS_DECOY` |
| Default effect | `BIAS_DEFAULT` |
| Decision fatigue | `BIAS_DECISION_FATIGUE` |
| Disgust bias | `BIAS_DISGUST` |
| Distinction-drawing | `DEBATE_DISTINCTION` |
| Dunning–Kruger | `BIAS_DUNNING_KRUGER` |
| Effort heuristic | `HEUR_EFFORT` |
| Effort justification | `BIAS_EFFORT_JUSTIFICATION` |
| Endowment effect | `BIAS_ENDOWMENT` |
| Equivocation | `FALLACY_EQUIVOCATION` |
| Euphemism treadmill | `BIAS_EUPHEMISM` |
| Fading affect bias | `BIAS_FADING_AFFECT` |
| False dilemma | `FALLACY_FALSE_DILEMMA` |
| Framing effect | `BIAS_FRAMING` |
| Fundamental attribution error | `BIAS_FUNDAMENTAL_ATTR` |
| Gambler’s fallacy | `BIAS_GAMBLERS` |
| Halo effect | `BIAS_HALO` |
| Hindsight bias | `BIAS_HINDSIGHT` |
| Horns effect | `BIAS_HORNS` |
| Hot-hand fallacy | `BIAS_HOT_HAND` |
| Hyperbolic discounting | `BIAS_HYPERBOLIC` |
| Identity-protective cognition | `BIAS_IDENTITY_PROTECTIVE` |
| IKEA effect | `BIAS_IKEA` |
| Illusion of control | `BIAS_ILLUSION_CONTROL` |
| Illusion of transparency | `BIAS_TRANSPARENCY` |
| Impact bias | `BIAS_IMPACT` |
| Impostor feelings | `BIAS_IMP_POSTER` |
| In-group bias | `BIAS_INGROUP` |
| Insensitivity to sample size | `BIAS_INSENSITIVITY_SAMPLE` |
| Jargon fog | `BIAS_JARGON_FOG` |
| Leading question | `BIAS_LEADING_QUESTION` |
| Learned helplessness | `BIAS_LEARNED_HELPLESS` |
| Levels of analysis | `DEBATE_LEVELS` |
| Liking bias | `BIAS_LIKING` |
| Loaded question | `FALLACY_LOADED` |
| Loss aversion | `BIAS_LOSS_AVERSION` |
| Middle-ground fallacy | `FALLACY_MIDDLE` |
| Motte-and-bailey | `FALLACY_MOTTE_BAILEY` |
| Naïve realism | `BIAS_NAIVE_REALISM` |
| Negativity bias | `BIAS_MEMORY_NEGATIVITY` |
| No true Scotsman | `FALLACY_NO_TRUE_SCOTS` |
| Non-identity blame relocation | `DEBATE_NON_ID_BLAME` |
| Normalcy bias | `BIAS_NORMALCY` |
| Omission bias | `BIAS_OMISSION` |
| Omnivore’s paradox (applied) | `BIAS_OMNIVORE_PARADOX` |
| Optimism bias | `BIAS_OPTIMISM` |
| Outcome bias | `BIAS_OUTCOME` |
| Peak-end rule | `BIAS_PEAK_END` |
| Pessimism bias | `BIAS_PESSIMISM` |
| Planning fallacy | `BIAS_PLANNING_FALLACY` |
| Present bias | `BIAS_PRESENT` |
| Processing fluency | `HEUR_FLUENCY` |
| Projection bias | `BIAS_PROJECTION` |
| Pseudocertainty | `BIAS_PSEUDOCERTAINTY` |
| Purity heuristic | `HEUR_PURITY` |
| Reactance | `BIAS_REACTANCE` |
| Reciprocity | `BIAS_RECIPROCITY` |
| Recognition heuristic | `HEUR_RECOGNITION` |
| Recency effect | `BIAS_RECENCY` |
| Reductio of category claim | `DEBATE_REDUCTIO_CAT` |
| Reframe / relabel | `DEBATE_REFRAME` |
| Regret aversion | `BIAS_REGRET_AVERSION` |
| Representativeness | `HEUR_REPRESENTATIVENESS` / `HEUR_REPRESENT` |
| Risk compensation | `BIAS_RISK_COMPENSATION` |
| Rosy retrospection | `BIAS_ROSY_RETROSPECTION` |
| Salience heuristic | `HEUR_SALIENCE` |
| Satisficing | `HEUR_SATISFICE` |
| Scarcity heuristic | `HEUR_SCARCITY` |
| Self-efficacy collapse | `BIAS_SELF_EFFICACY_GAP` |
| Self-serving bias | `BIAS_SELF_SERVING` |
| Simulation heuristic | `HEUR_SIMULATION` |
| Slippery slope | `FALLACY_SLIPPERY` |
| Social proof | `BIAS_SOCIAL_PROOF` |
| Special pleading | `FALLACY_SPECIAL_PLEAD` |
| Spotlight effect | `BIAS_SPOTLIGHT` |
| Status quo bias | `BIAS_STATUS_QUO` |
| Steelmanning | `DEBATE_STEELMAN` |
| Stereotype bias | `BIAS_STEREOTYPE` |
| Straw man | `FALLACY_STRAWMAN` |
| Sunk cost fallacy | `BIAS_SUNK_COST` |
| System justification | `BIAS_SYSTEM_JUSTIF` |
| Take-the-best | `HEUR_TAKE_BEST` |
| Time-saving bias | `BIAS_TIME_SAVING` |
| Trust heuristic | `HEUR_DEFAULT_TRUST` |
| Tu quoque / whataboutism | `FALLACY_WHATABOUT` |
| Unity bias | `BIAS_UNITY` |
| Von Restorff | `BIAS_VON_RESTORFF` |
| Wrong-enemy pivot | `DEBATE_WRONG_ENEMY` |
| Zero-risk bias | `BIAS_ZERO_RISK` |

---

## 15. Consistency notes

- Currency hints use **only** `docs/01` allowlisted IDs.  
- `HEUR_SCARCITY` is catalogued for diagnosis; using it as Core Idea is banned.  
- Fallacies in §10.2 are **villain patterns or method bans**, not approved techniques.  
- Catalog completeness is practitioner-scoped (angle/DTC/story); synonyms may map to the nearest `id`.
