---
name: founder-market-recommender
description: Recommends specific markets a founder should research to find founder-market fit, grounded in their persona.json from founder-persona-interview. Use whenever the user (with a persona on hand) asks "what market should I explore", "where should I focus", "what should I build", "which vertical fits me", asks for market / vertical / business suggestions, or mentions wanting direction on which domain to go deep in. Also trigger immediately after founder-persona-interview completes if the user wants to go further. This skill does NOT pick from a fixed menu — it proposes open-ended specific markets with mandatory persona-grounded justification, hallucination guardrails, and business-model alignment per main.md. Prefer triggering this over generic "what should I build" advice, even if the user hasn't named the skill explicitly.
---

# Founder Market Recommender

## What this skill does

Reads a founder's `persona.json` and recommends 3–5 specific markets they should research next, plus 2–3 markets they should avoid. Every recommendation is grounded in named persona evidence — the research skill's discipline is that no market is suggested that could equally apply to a different founder.

## Input contract

- **Primary input:** `./persona/persona.json` (produced by `founder-persona-interview`).
- **Override:** the user may paste their own persona or provide a `--persona <path>` flag. Accept either.
- **Optional additional context:** the user may add constraints the persona doesn't capture ("I want to stay in B2B only", "please exclude crypto"). Respect those without relaxing the grounding rules.

**If no persona.json exists and the user hasn't pasted one:** stop and say clearly — *"I don't see a persona file at `./persona/persona.json`. Run the `founder-persona-interview` skill first, or paste your persona here, and I'll take it from there."* Do not invent a persona.

## Output contract

A single markdown report to stdout (or to `./market-recommendations.md` if the user asks for a file). Structure:

```
# Market recommendations for <founder_name>

## Top <N> markets to research

### 1. <Specific market — vertical + segment>
- **Why this fits you specifically:** <2–3 sentences citing named persona evidence — communities, warm intros, edges, obsession signals>
- **Market dynamics class:** <one of: regulated, pure SaaS, ops-intensive, marketplace, transactional, usage-based, consumer> — and why this class fits your archetype mix
- **Suggested business model:** <subscription / transactional / usage / marketplace / hybrid> — and why
- **First-customer path:** <named warm-intro candidates from persona.network.warm_intros, or explicit "cold start" flag>
- **Strongest pillars for this market:** <pillar_scores that apply>
- **Known risks:** <entrenchment, psychographic mismatch, credibility gap, other>

### 2. …

## Markets to avoid (or treat with caution)

### <Market> — <reason>
<2–3 sentences citing the specific persona evidence that makes this market a poor fit>
```

## Recommendation reasoning

Markets are recommended **open-endedly** — no curated list, no fixed taxonomy you pull from. Propose whatever specific markets/verticals/segments genuinely fit the persona.

Apply `main.md`'s strategic-matching logic as **reasoning filters**, not as hard gates. Before suggesting any market, you should have internally answered:

1. **Which market dynamics class** is this? (See `references/archetype-to-market-dynamics.md`.) Does that class fit the founder's archetype mix?
2. **Which business model** does this market best support? (See `references/business-model-alignment.md`.) Does that model align with the archetype?
3. **Does the persona have a first-customer path** into this market? (Warm-intro graph in `network.warm_intros`, or a named community where buyers live.) If not, mark explicitly as cold-start — don't hide it.
4. **Is the founder entrenched** here? (See `references/entrenchment-heuristics.md`.) If they're 10+ years deep in the status-quo of this market, suggest adjacent verticals where they're "embedded but naive" instead.
5. **Does the obsession pattern** sustain a 5-year commitment in this market? If persona obsession signals don't cover this space, flag it.
6. **Does psychographic fit** match the market's timeline? Missionary-coded founders → nascent/category-creating markets. Mercenary-coded → mature markets with exploitation plays and faster exits.

## Mandatory grounding rules

Every recommendation must cite specific persona evidence. Read `references/persona-grounding-protocol.md` before producing output — the "one-named-evidence-per-claim" rule is strictly enforced.

## Hallucination guardrails

The open-ended scope requires strict discipline to avoid inventing market data or competitor names. Read `references/hallucination-guardrails.md` — the four rules there (no unverified TAM, no invented competitors, no generic-applicable claims, explicit cold-start marking) are the difference between a useful recommendation and a confabulation.

The **generic-suggestion test**: after drafting each recommendation, ask yourself *"could I give this exact recommendation to a different persona and it'd still fit?"* If yes, it's generic and must be rewritten or cut.

## Process

1. Read `./persona/persona.json` (or override path). Bail clearly if missing.
2. Skim `persona.md` for context and direct quotes if available.
3. Read the 5 reference files in this skill — all relevant to every run.
4. Internally map the persona to candidate markets. Generate 6–10 candidates; then cull to top 3–5 by the grounding rules.
5. Generate 2–3 markets to avoid, each with specific reasoning from the persona.
6. Draft the report. Apply the generic-suggestion test to each recommendation. Rewrite or cut any that fail.
7. Present the report. If the user asks follow-up questions about specific markets, stay grounded in the persona — don't invent new evidence.

## Handoff to downstream skill

After producing recommendations, mention that `founder-idea-audit` is available to audit specific ideas within any of the recommended markets against the same persona. Don't invoke it automatically — let the founder choose a direction first.
