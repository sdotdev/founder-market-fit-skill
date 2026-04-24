# Red flags catalogue

Consolidated from the "Red Flags" sections of the FMF research (`founder-market-fit-assessment-frameworks.md`). For each audit, pick the **top 3** most-relevant red flags given the specific founder × idea combination. Cite the specific persona/idea evidence that triggered each.

Do not water the flags down. Honest flags are the point of the audit. A 78/100 audit with 3 real red flags is more trustworthy than a 78/100 audit with no flags surfaced.

## Experience and Insight

**E1. Unable to predict customer responses without research.**
Founder can't anticipate how target buyers will react to the product / pricing / positioning. Test: ask "what will the first buyer's first objection be?" A strong-FMF founder names it immediately.

**E2. Speaking in trends rather than constraints and trade-offs.**
Pitch focuses on market size, growth, "AI-native", "underserved segment" — abstractions any outsider could articulate. No specific trade-offs named.

**E3. Lack of emotional connection when discussing the problem.**
Founder speaks about the problem like an analyst or investor rather than like someone who's lived it. No personal stake evident.

**E4. Difficulty identifying non-obvious market blockers.**
When asked "what stops this from being built in 18 months by a competitor with 2× the capital", founder cannot articulate specific structural blockers — regulatory, technical, distribution-trust.

**E5. Generic understanding matching public information only.**
Everything the founder says about the market could be recovered from a public-search-accessible industry report. No private-knowledge signals.

## Commitment and Motivation

**C1. Motivation dependent on external validation or traction.**
Founder's energy visibly tracks investor interest, customer pilots, team sentiment. When one drops, motivation drops. Persona's `psychographic.mercenary_score` high AND `missionary_score` low.

**C2. Unwillingness to endure long feedback loops.**
Idea is in a category with 9-18 month sales cycles, but founder's stated runway + psychographic profile suggests intolerance. Mercenary 8+ on a 5-year-compound idea.

**C3. Lack of organic engagement in market-related learning.**
No `obsession_signals` with `specificity_score` ≥4 on this idea's problem space. Founder reads about the space only when preparing for a pitch.

**C4. Short time horizon (<1 year) for problem engagement.**
Idea requires multi-year category education or trust-building, but founder's stated time horizon is shorter. Explicit statement of "3-year exit" on a 10-year-category idea.

**C5. Interest that feels theoretical rather than visceral.**
Founder can't name a moment where this problem made them angry, curious, or driven. The problem is an idea to them, not a lived experience.

## Credibility and Trust

**T1. Target customers expressing skepticism or distrust.**
Early discovery calls show buyer wariness about the founder's legitimacy for this market. They ask "who else is on your team?" repeatedly.

**T2. Inability to communicate in market-native language.**
Founder uses generic B2B SaaS vocabulary for a market that has its own terminology (e.g. says "customers" where the industry says "providers" or "members").

**T3. Lack of first-user willingness from target segment.**
In Sean-Ellis-style pre-fit testing, target users do NOT say they would be "very disappointed" if this product didn't exist. <40% threshold from `main.md`.

**T4. Market insiders not opening up or sharing insights.**
When founder tries to do discovery conversations, insiders stay at pleasantry level — don't surface the arcane pain points. Insider-detection signal.

**T5. Perception as outsider rather than participant.**
The market's key influencers, operators, or communities do NOT recognise the founder as one of their own. No `insider_markers` in persona that this specific market would recognise.

## Resource and Alignment

**R1. Psychological intolerance for market's feedback loop length.**
Mismatch between founder's stated runway/patience and market's typical proof-point cadence. E.g., 6-month runway on a 12-month enterprise sales cycle.

**R2. Resource constraints incompatible with market requirements.**
Market requires regulatory approval, clinical trials, hardware manufacturing, or similar capital-intensive gating that the founder can't survive. `constraints.runway_months` incompatible with category.

**R3. Skill gaps in critical, unhireable areas for the market.**
Market requires a rare skill (e.g. clinical trial design, specific compliance credentials, a particular language) that cannot be hired at seed stage. Founder lacks and has no clear plan.

**R4. Misaligned definitions of success with market realities.**
Founder wants $1B outcome; market structure produces $50M outcomes reliably. Or vice versa — founder wants lifestyle, market demands venture-scale stamina.

**R5. Fundamental mismatch in work style preferences.**
Stage-fit mismatch (founder wants 0→1, idea requires scaling; or inverse). `stage_preference` from persona misaligned with the idea's phase requirement.

## Surfacing the right 3

When choosing the top 3 red flags to surface:

1. **Prioritise flags that the persona's credibility_flags directly support.** If the persona flags Technical over-claim and the idea requires strong technical leadership, surface the skill-edge red flag (E4 if about build feasibility, R3 if about unhireable skill).

2. **Prioritise actionable flags.** A flag that maps cleanly to a gap-mitigation action (hire, advise, delay launch, pivot scope) is more useful than a purely diagnostic flag.

3. **Avoid duplication.** Don't surface three flags that say the same thing in different words.

4. **Match flag severity to audit score.** A <40 audit deserves the most structural flags (C1, T3, R1). A 70+ audit deserves the marginal flags that explain why it isn't 90+.

## Citing the flag

Each surfaced flag in the output must include:

- **Flag name + catalogue ID** (e.g. "E2 — Speaking in trends rather than constraints").
- **Specific persona/idea evidence** that triggered it (named quote, field, or score).
- **Recommended mitigation** (one sentence).

No generic mitigation phrases. "Improve network" is not a mitigation. "Schedule warm-intro calls with Tom DiFranco and Sarah Okwu in the next two weeks, using the chargeback-substack as a conversation starter" is a mitigation.
