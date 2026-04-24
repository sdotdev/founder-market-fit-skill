# Archetype probes (3H/4H triangulation)

From `main.md`. The 3H model (Hustler / Hacker / Hipster) plus the Hound. Most founders are weighted blends of two or three. The goal is to triangulate `archetype_mix` from behaviour evidence, not from self-identification.

Never ask "are you a Hustler, Hacker, or Hipster?" directly. The categories are memed and self-serving ("I'm visionary"). Instead, probe with scenarios and infer.

## Hustler probes

The Hustler drives commercial momentum — deals, partnerships, unblocking, chasing. Listens for social graph and closing instinct.

- "Tell me about the last deal, sale, or partnership you closed. Walk me through what actually moved it from 'maybe' to 'yes'."
- "When's the last time you got an ambivalent stakeholder to commit to something on a tight timeline?"
- "Describe the last time you spent a weekend on something that wasn't your job. If it was pitching or networking, lean Hustler."
- "If this venture needed $50K of revenue in 30 days, what would you do on day 1?"

Pass signal: names specific deal, names the counterparty, articulates the social dynamics, moves fast when talking about it.
Anti-signal: talks about sales as "building a process" or "hiring someone for GTM" — that's not Hustler, that's Catalyst or Operator.

## Hacker probes

The Hacker is the compulsive builder. Listens for speed, craft specificity, and fascination with how things work.

- "What was the last working prototype you shipped end-to-end? How many hours did it take, and what'd you cut to get it out?"
- "When you hit a new problem, do you reach for an LLM, a framework, or a textbook first?"
- "What's the smallest thing you've built in the last month just because you wanted to?"
- "If you got 72 hours and no meetings, what would you make?"

Pass signal: names specific shipped thing in the last few months, articulates the trade-offs, has strong opinions about tools.
Anti-signal: "I'd pair with my technical co-founder" — that's not Hacker, regardless of credentials.

## Hipster probes

The Hipster bridges technology and user experience. Listens for taste, craft obsession about polish, and design reference library.

- "Describe the last thing you made where you obsessed over the polish — interface, copy, typography, feel."
- "What products do you use daily that you think are underrated for their craft?"
- "When's the last time you killed a feature because it didn't feel right, even though it worked?"
- "Show me something from your phone or computer that you love aesthetically."

Pass signal: specific references, strong opinions about design, willing to kill working-but-ugly work.
Anti-signal: "I know good design when I see it" without specific references — that's aspiration, not Hipster.

## Hound probes

The Hound interprets data and user signals to find unmet needs. Listens for analytical specificity and comfort with messy data.

- "Last time you had a messy dataset to interpret, what did you do with it?"
- "What's a counter-intuitive thing you learned from user interviews or behavioural data in the last year?"
- "How do you know when you're wrong about a product hypothesis?"
- "Describe a time you killed your own idea based on data."

Pass signal: specific dataset or interview memory, named counter-intuition, articulates hypothesis-testing process.
Anti-signal: "I look at analytics regularly" — passive consumption isn't Hound.

## Triangulation

After running ≥3 probes per archetype (or until you have a clear signal), compute `archetype_mix` weights that sum to 1.0. Examples:

- Classic sales-led founder: `{ hustler: 0.65, hacker: 0.05, hipster: 0.10, hound: 0.20 }`
- Product-led technical founder: `{ hustler: 0.10, hacker: 0.60, hipster: 0.20, hound: 0.10 }`
- Design-led consumer founder: `{ hustler: 0.15, hacker: 0.15, hipster: 0.55, hound: 0.15 }`
- Data-led B2B founder: `{ hustler: 0.20, hacker: 0.20, hipster: 0.10, hound: 0.50 }`

Most founders should NOT be above 0.65 on any single axis. If they are, double-check — pure archetypes usually indicate a missing co-founder gap, not a strength.

Populate `archetype_primary` (highest weight) and `archetype_secondary` (second highest) if the second is ≥0.20. Otherwise leave `archetype_secondary` null.

## Cross-walks to other frameworks

For downstream skills and narrative use, the persona.md can also reference a **secondary taxonomy match** — picked from the archetype frameworks file, not persona.json (which stays on 3H/4H). Rough cross-walks:

| 3H/4H | Founder Institute 9-type | FOALED |
|---|---|---|
| Hustler | Diplomat / Commander / Evangelist | Fighter / Accomplisher |
| Hacker | Prodigy / Inventor / Architect | Engineer / Developer |
| Hipster | Inventor / Evangelist | Developer / Leader |
| Hound | Prodigy / Architect / Administrator | Engineer / Operator |

Use these cross-walks in persona.md prose when they add resonance. Don't over-use — the 3H/4H is the canon for this suite.

## Edge case: the Operator

Some founders don't fit 3H/4H cleanly because their core mode is building repeatable process (scaling ops, hiring systems, running a machine). In the 3H/4H frame they get high Hustler + high Hound scores, but the real signal is stage preference: Operators dominate the 1→10 phase.

If you detect an Operator pattern, mark `stage_preference: "1_to_10"` strongly, and note it in the narrative. Downstream skills will flag them as mis-fit for most 0→1 opportunities — which is correct and important.
