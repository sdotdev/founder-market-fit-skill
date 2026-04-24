# Entrenchment heuristics

From `main.md`'s sufficient-vs-excessive market-edge nuance. This is one of the less obvious rules in the FMF research and the most likely to be missed by a naive recommender.

## The rule

*"While a lack of experience leads to shallow insights and slow iteration loops, too much time in an industry can lead to entrenchment in the status quo. Founders who have spent decades in a sector may lose the capacity for disruption, as they become conditioned to accept existing inefficiencies as inevitable."*

The optimal Market Edge:
- **Sufficient** — 5–8 years in the vertical is the sweet spot. Enough time to know arcane pain points. Enough time to build a warm-intro graph.
- **Not excessive** — 10+ years in a single role or company in the same vertical often means the founder has internalised the industry's status-quo acceptance. They know the pain exists but no longer believe it's solvable.

## How to detect entrenchment from persona.json

**Check `edges.market.entrenchment_risk`** — the persona-interview skill sets this flag when it detects the pattern. If `true`, treat the founder's primary vertical as disruption-risk.

**If the flag isn't set but you suspect entrenchment:**
- Total years in a single role or company at that vertical > 10?
- Evidence list contains phrases like "that's just how it works" or "the regulators would never"?
- Psychographic evidence suggests acceptance of slow deal cycles as inevitable?

## What to do with entrenched founders

Don't just avoid their primary vertical — that loses their earned edge. Instead, recommend **adjacent verticals where they're "embedded but naive"**:

- **A 15-year insurance underwriter** → not underwriting-tech (too entrenched); but **claims-automation** (adjacent, insurance-adjacent network transfers, less absorbed-as-inevitable).
- **A 20-year ICU physician** → not physician-facing EHR tools (entrenched); but **patient-family communication platforms** or **ICU-to-stepdown handoff tools** (adjacent, network transfers, the "that's just how it is" bias doesn't apply).
- **A 12-year investment banker** → not core M&A tooling; but **pre-deal CRM** or **post-close integration tracking**.

The test: *can you name the adjacent vertical where the founder has credibility but hasn't absorbed the resignation?*

## What NOT to do

- **Don't just strip out their primary vertical.** That turns their biggest asset into a gap. If they've been in fintech 15 years, fintech-adjacent markets should still dominate the recommendation — just flag the entrenchment and pivot within the space.
- **Don't assume all long tenure is entrenchment.** Some founders keep fighting the status quo internally for decades and emerge more disruptive, not less. Cross-check the psychographic and obsession sections before applying the flag.
- **Don't silently downgrade.** If you believe entrenchment is real, say so in the recommendation's "Known risks" line. Transparency gives the founder the chance to push back with evidence.

## The opposite failure mode

The other end of the Market Edge spectrum is "credibility theater" — claims of domain expertise without earned edge. The persona-interview skill should have already flagged these in `credibility_flags`. If a credibility flag exists on `dimension: experience`, you're in the opposite regime: don't recommend that vertical at all (the credibility gap means the founder will lose every early sales conversation), OR recommend it only if they're planning to shore up with a domain co-founder (flag this explicitly in mitigation).
