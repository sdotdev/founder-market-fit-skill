# Hallucination guardrails (open-ended scope)

Sam picked "fully open-ended" over "curated menu" because it produces more tailored recommendations. The cost is that without constraint, this skill can hallucinate TAM numbers, invent competitor companies, and make generic claims. These four rules prevent that.

## Rule 1: No market claims without persona evidence or explicit caveat

**Bad:** "The SMB payments market is growing at 15% CAGR and is a $200B opportunity by 2028."

**Why bad:** those numbers may or may not be true, and the founder has no way to tell if they came from the persona or were generated from the pattern of the model's training data. Either is a claim you cannot support.

**Correct alternative 1:** omit the market size entirely — the founder can research it themselves and it's not central to FMF.

**Correct alternative 2:** attribute it clearly: "The persona mentions Stripe's 2024 SMB report, which cites SMB payment volume growing ~15% YoY (persona-cited)." Only do this when the persona really does cite the number.

**Correct alternative 3:** flag as unverified: "(unverified — research signal only) SMB payments is commonly cited as a multi-hundred-billion-dollar market." Reader knows to check.

**Default:** skip TAM claims. Founder-market fit is about whether the founder is the right person to build into this market, not about how big the market is.

## Rule 2: Don't invent competitor names

**Bad:** "Competitors in this space include Recharge, Loop Returns, and ParcelLab." (All real companies, but the skill didn't verify their presence in the market or the founder's context.)

**Why bad:** naming competitors implies you know the competitive landscape. If you don't, don't pretend.

**Correct alternative 1:** don't name competitors. Describe the competitive shape: "This space is dominated by established enterprise vendors with long sales cycles." The founder knows the names.

**Correct alternative 2:** name only competitors the founder mentioned in the persona. If the persona's evidence cites "Stripe 2024 SMB report", you can reference Stripe. Otherwise, leave names out.

## Rule 3: The generic-suggestion test

After drafting each recommendation, ask yourself:

> *"Could I give this exact recommendation to a different persona and it would still fit?"*

If yes, the recommendation is generic and must be rewritten or cut. Examples:

- **Fails the test:** "SMB payment infrastructure — a large, growing market with lots of unmet need." (Could apply to any fintech-adjacent founder.)
- **Passes the test:** "SMB chargeback-dispute tooling — your substack is literally on this, you have three named warm intros in SMB payments (Priya Nair, Tom DiFranco, Sarah Okwu), and your Stripe Tax launch experience maps directly to the go-to-market motion."

The useful recommendation names specific persona evidence such that no other persona could produce the same sentence. That's the bar.

## Rule 4: Explicit cold-start marking

When a market has no warm-intro coverage in the persona's `network.warm_intros`, don't hide it. Mark it explicitly:

> "**First-customer path: cold start.** You have no warm intros in this market per your persona. That doesn't eliminate it as an option — but you'll need to earn credibility from scratch, which typically adds 6–9 months to first customer."

Cold-start markets can still be legitimate recommendations (especially for technical founders whose network is in dev communities, not buyer verticals). But the founder has to see the gap clearly so they can make an informed choice.

## Meta-rule: when in doubt, omit

Open-ended scope gives you freedom to generate. Grounding discipline constrains what you keep. If a claim is interesting but unsupported, cut it — don't caveat your way to the founder's confusion. The recommendation report should feel shorter and sharper than a generic market-analysis deck.

A 3-market report that's 100% grounded beats a 5-market report where 2 are made up.
