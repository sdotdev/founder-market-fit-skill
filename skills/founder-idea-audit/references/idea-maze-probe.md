# Idea Maze probe

From `main.md`: *"Knowledge refers to the possession of a 'secret' or 'non-obvious truth' about the market. It involves a deep understanding of the 'idea maze' — knowing why previous attempts to solve this problem failed and what has changed to make it possible now."*

The Idea Maze probe is how the idea-audit scores the Non-Obvious Insight dimension (20% weight). It's a single question with a rigorous rubric.

## The probe

> "What have the last three attempts at this problem gotten wrong, and what's changed that makes it solvable now?"

Ask the founder if you're in conversational mode. If in static-brief mode, look for the answer in the brief. If not present, **note the absence explicitly and score Insight conservatively (≤5/10)** — don't invent what the founder didn't say.

## Scoring the answer

**10/10 signal:** names 3+ specific prior attempts (with company names, product names, or specific approaches), names the specific failure mode for each, names a coherent now-possible thesis tied to specific technological, regulatory, or behavioural changes. Ideally: has personally witnessed or participated in one of the failed attempts.

Example for a chargeback-automation idea:
> "The legacy dispute-filing services at Verifi and Chargebacks911 optimised for enterprise reps with large case volumes, so they priced SMBs out. Mid-2010s startups like Chargeback (acquired by Sift) tried to productise the dispute flow but couldn't get distribution below the enterprise tier. And I was adjacent to Stripe's own internal build — it never got prioritised against newer SKUs. What's changed: card-network penalty escalation (VDMP costs were 40% lower in 2018), SMB awareness from TikTok dispute-shop content, and LLMs make evidence-compiling scale to SMB economics for the first time."

That's a 10. Three specific prior attempts, three specific failure modes, a three-pronged thesis on what's changed. Could be challenged but is defensible.

**8–9/10 signal:** names 1–2 prior attempts with specific failure modes; coherent thesis. Less depth than 10 but still substantive.

**5–7/10 signal:** recognises the problem is non-trivial; can name a general "timing" or "technology" shift; but can't articulate specific prior attempts. This is the baseline for a founder who has researched the space but hasn't lived the failures.

**3–4/10 signal:** generic "AI makes this possible now" or "the market is ready" claims without specifics. Surface-level.

**1–2/10 signal:** treats the problem as novel, asserts no one has tried it before (usually false and reveals lack of research). Or, worse, dismisses prior attempts as "not serious" without engaging with why they failed.

## Common failure patterns to flag

- **"The incumbents are slow"** — almost never true at the level of detail a founder can defend. If the founder says this, push back: which specific incumbent is slow on which specific workflow?
- **"AI changes everything"** — generic. Which specific capability? When did it unlock (last 12 months / last 24 / last 36)? What specifically does it enable that wasn't possible before?
- **"The timing is right"** — usually an unsupported vibe. Demand specifics: regulatory change? Behavioural shift? Supply-side shift? Demand-side shift? Each with a verifiable anchor.
- **"No one else is doing this"** — often means the founder hasn't researched. Ask: have you talked to anyone who *tried* and stopped? Have you searched for patents / failed Y Combinator pitches / defunct startup postmortems?

## In the audit output

The per-pillar breakdown should show the Idea Maze probe result explicitly:

> **Insight — 8/10 (×2.0 = 16)**
> Idea Maze: founder named Chargebacks911 and Verifi as prior enterprise-focused attempts that couldn't crack SMB economics; named SMB awareness from TikTok content and card-network penalty escalation as two independent now-possible drivers. Did not name the Stripe internal attempt (which they were adjacent to per persona) — minor gap. Insight score is high but not maxed; rehabilitating to 9 would require the third attempt cited.

This shows the founder exactly what they'd need to add to reach a higher score. Transparent scoring makes the audit useful as a coaching tool, not just as a gate.

## When the brief doesn't answer the probe

If the founder's static brief doesn't address the idea maze question, default to:

- **Score 5/10 or below** (usually 4).
- **In the evidence field**, note: "Idea-maze probe not answered in the brief. Cannot score above 5 without the founder naming specific prior attempts and specific now-possible drivers."
- **In the gap-mitigation plan**, add a concrete learning item: "Spend 1 week researching 3 specific prior attempts at this problem — company names, failure modes, and one 2024-2026 change that makes the current attempt different."

This gives the founder a specific path to improve the audit score next time rather than leaving them confused about what "insight" means.
