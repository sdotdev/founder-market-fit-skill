# Persona-grounding protocol

Every claim in every recommendation must be traceable to specific persona evidence. This file defines what "specific" means and how to structure the citation.

## The rule

For every market recommendation and for every "avoid" recommendation, you must be able to answer these four questions by pointing at persona.json fields (not paraphrasing, not inferring):

1. **Which specific persona evidence drove this suggestion?** Name the field and the value.
2. **Which archetype mix or edge made this market's dynamics a match?** Cite the number or the edge strength.
3. **What is the first-customer path from this founder's network?** Name the warm-intro candidate(s) or explicitly mark cold-start.
4. **Why does their obsession/psychographic sustain a 5-year commitment in this market?** Cite the specific obsession signal.

If you can't answer all four, the recommendation isn't grounded — rewrite it or cut it.

## How to cite

Use direct references in prose, not footnotes. Examples:

**Good:**
> "Your persona shows 9 years of SMB payments domain with specific arcana (chargeback-ratio thresholds, 38% KYC drop-off). Three named warm intros — Priya Nair at Earnest, Tom DiFranco at LedgerLift, Sarah Okwu at Rhombus — could be your first-customer pipeline within 60 days. Your 9-month personal substack on chargeback disputes is the obsession signal for a 5-year build."

**Why good:** three specific persona evidence references (domain arcana, named intros, substack), each tied to a specific claim.

**Bad (paraphrased, ungrounded):**
> "You have strong fintech expertise and a solid network in payments, plus you seem genuinely interested in this area."

**Why bad:** could describe any fintech-adjacent founder. No specific evidence.

## Citation source-of-truth

When in doubt, prefer citations from these persona.json fields:

- `edges.market.evidence` — arcane domain specifics
- `network.warm_intros[].named_contacts` — literal names with roles
- `network.insider_markers` — specific external signals
- `obsession_signals[].signal` — specific artefacts the founder produces
- `psychographic.evidence` — quotes about motivation

Don't cite:

- `archetype_mix` values directly ("you're 55% Hustler") — use the *implication* of the mix, not the number.
- `pillar_scores` directly ("your network pillar is 8") — interpret it, don't recite it.

## Evidence-reuse limits

A single piece of persona evidence should support at most **two** recommendations. If the same obsession signal (e.g. "substack on chargeback disputes") is the only thing justifying every recommended market, you're over-fitting that signal. Find additional evidence or cut the less-supported recommendations.

## What counts as evidence — severity ranking

From strongest to weakest:

1. **Named person + current role** (in warm_intros.named_contacts) — strongest grounding for network claims.
2. **Specific artefact the founder produced** (substack, GitHub repo, talk, playbook) — strongest for obsession and insider-marker claims.
3. **Arcane domain specifics** (named edge cases, specific numbers, named workflows) — strongest for edge claims.
4. **Community with embeddedness ≥ `contribute`** — moderate grounding.
5. **Years in a vertical** — weak grounding by itself; often credibility theater. Require arcana or named artefacts to reinforce.
6. **Archetype label or pillar score alone** — weakest; use only as interpretation, not citation.

## When persona evidence is thin

Some founders (e.g., Jamie the generalist hacker) have persona fields where every warm_intros entry is `cold_start: true` for buyer verticals. In that case:

- **Don't invent verticals.** Their network is in dev communities — recommend markets where developers are the buyer (usage-based infra, dev tools, OSS-monetisation).
- **Be explicit about the constraint.** "Your persona shows no warm-intro path into any non-dev buyer vertical. That makes non-dev markets high-friction for you right now — either recommend a co-founder plan or stick to dev-as-buyer markets."
- **Don't paper over it with vague optimism.** Cold-start is a real constraint.

## The final check

Before finalising, re-read each recommendation and confirm that **every claim** has a specific persona reference. If any sentence contains a generic claim ("strong network", "deep expertise", "real passion"), rewrite it with a named specific or cut it.
