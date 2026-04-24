---
name: founder-persona-interview
description: Runs a deep founder-market fit interview that depth-probes a founder's archetype, edges, network, and obsession to produce a structured persona artefact (persona.md + persona.json) that downstream FMF skills consume. Use whenever the user says "what kind of founder am I", "profile me as a founder", "founder self-assessment", "help me figure out my edge", "assess my founder-market fit", describes their background and asks for analysis, or when a market/idea skill needs persona data and none exists. This skill is deliberately not a personality quiz — it depth-tests every claim to separate earned edge from credibility theater, so trigger it even if the user seems ready to self-diagnose.
---

# Founder Persona Interview

## What this skill does

Conducts a structured but adaptive founder-market fit interview — typically 30–60 minutes of real conversation — and produces two output files:

- `./persona/persona.md` — narrative persona document (human-readable).
- `./persona/persona.json` — structured schema consumed by `founder-market-recommender` and `founder-idea-audit`.

The persona captures archetype mix, edges, network access, psychographics, obsession signals, stage fit, and constraints. Crucially it also records `credibility_flags` — claims the founder made that this interview couldn't corroborate. Downstream skills read those flags to adjust scoring.

## Modes: live interview vs written brief

This skill handles two input shapes:

- **Live interview mode (default).** The user starts with a short intro ("help me figure out my edge", "profile me as a founder") and you drive the 8-section interview conversationally, branching probes based on their answers. Expect 30–60 minutes of back-and-forth.
- **Written brief mode.** The user provides a long self-description up front — a paragraph or more covering career, domain, network, obsession. In this case **treat the writing itself as the probe material**. Specifics in the brief (named people, arcane edge cases, named artefacts, specific dates) pass the same depth tests you'd run conversationally. Vagueness in the brief ("I know lots of people in healthcare", "I'm technical", "I'm obsessed with X") fails the same tests and fires the same credibility flags. Do NOT re-interview — produce the persona directly from what's on the page.

Detect the mode from the first user turn:
- ≥3 paragraphs of self-description with concrete details → written brief mode.
- A short intro or question → live interview mode.
- If ambiguous, ask once: "Do you want to walk me through your background conversationally, or would you rather write it all out and have me produce the persona from that?"

Output contract is identical in both modes — see the Output section below. The `credibility_flags` logic is the same: in live mode, flags come from failed conversational probes; in brief mode, flags come from claims in the writing that lack specific detail.

## Core principle: depth-probe, don't checkbox

Most founder quizzes ask "are you a Hustler, Hacker, or Hipster?" and accept the answer. This skill does not. Founders are lossy self-reporters — they over-claim domain expertise, inflate community access, and call themselves missionaries when they're mercenaries. The whole point of this interview is to **earn the persona rather than accept the self-portrait**.

Every substantive claim gets a depth-probe:

| Surface claim | Checkbox question (don't) | Depth probe (do) |
|---|---|---|
| "I'm technical" | "Rate your technical skill 1–10" | "What's the last thing you shipped end-to-end, and how long did it take?" |
| "I know healthcare" | "How many years in healthcare?" | "What's a prior-authorisation workflow gotcha that new providers routinely miss?" |
| "I have a network in X" | "Do you know people in X?" | "Name the first three people you'd call to get a paying customer in X." |
| "I'm obsessed with Y" | "Are you passionate about Y?" | "What have you read or tinkered on in Y in the last 6 months with no external pressure?" |

If a probe fails (they can't name, can't cite, can't answer specifically), **record a credibility flag in persona.json rather than silently downgrading the score**. The flag lets downstream skills weight that dimension appropriately without being rude to the founder in the persona document itself.

The full detection protocol — what counts as a fail, how to soften the ask, how to log it — is in `references/credibility-theater-detection.md`. Read that file before conducting probes.

## Interview workflow

Eight sections. Do them in roughly this order, but follow threads as they surface. Don't march through them mechanically — if the founder mentions a community in section 1, probe it in section 1 rather than waiting for section 4.

Read the specific reference files as you hit each section; the probe banks live there, not here.

### 1. Career timeline + energy map

Walk the founder's last 5–10 years. For each major role ask: what were you doing day-to-day, what drained you, what energised you? The goal is not their LinkedIn — it's the **mismatch between role title and actual work pattern**. A "Product Manager" who mostly closed deals and broke political bottlenecks is a Hustler, not a product-led founder.

Exit criteria: you can articulate their dominant work pattern in one sentence that isn't their job title.

### 2. Archetype triangulation

Do NOT ask "are you a Hustler, Hacker, or Hipster?" Instead, probe with scenarios and infer. Full probe bank: `references/archetype-probes.md`.

Triangulate primary + secondary archetype. Populate `archetype_mix` as weighted scores (summing to 1.0), not a single label. Most founders aren't pure types.

### 3. Edges (EF framework)

Three edges: Technical, Market, Catalyst. Probes per edge in `references/edge-interview-playbook.md`.

- **Technical Edge** — PhD, research, deep tech, differentiated builder capability.
- **Market Edge** — industry depth. Apply the "sufficient-but-not-excessive" test: 10+ years entrenched in a status quo is a disruption-risk flag, not a pure asset.
- **Catalyst Edge** — track record of assembling teams, raising capital, shipping under pressure.

For each edge: record the claim string, the evidence list, and whether the depth-probe succeeded or failed. Failed probes → `credibility_flags` (not silent score reduction).

### 4. Network mapping

This section deserves time and structured capture — it's the single most actionable input for downstream skills. Full schema: `references/network-mapping-playbook.md`.

Three sub-structures:

- **Communities** — online (Slack / Discord / subreddit / newsletter) and offline (industry groups, alumni, conferences, meetups). Each ranked by **embeddedness**: *speak*, *moderate*, *contribute*, *lurk*.
- **Warm-intro graph** — for each vertical the founder has touched, collect **3 named people** they could call to get a first customer. Generic answers ("lots of people in fintech") are credibility flags; named people are network capital.
- **Insider markers** — quoted by, speaks at, authored on, holds admin/moderator role.

Goal is **specificity**, not completeness. A founder with one verifiable warm intro per vertical beats a founder who claims to "know everyone in X".

### 5. Psychographics: Missionary vs Mercenary

From Doerr, via `main.md`. Probes:

- "If this venture pays you nothing for 3 years, what keeps you building?"
- "Describe your ideal exit — how many years out, what size?"
- "What would you be doing in this space even if no one paid you?"

Record `missionary_score` and `mercenary_score` 1–10 each (they are not mutually exclusive — some founders hold both). Cite evidence per score. Don't average.

### 6. Obsession test

Under30CEO Q5, from the FMF research. Ask:

> "What have you been reading, tinkering on, or thinking about in your free time over the last 6 months — not because anyone asked, not for a job, but because it pulled at you?"

The answer's **specificity** is the signal. "AI agents" is not an obsession signal. "I've been benchmarking tool-calling latency across open-source agent frameworks and the trade-off space isn't what people claim" is an obsession signal.

Record each signal with a `specificity_score` 1–5. Generic signals (1–2) go in `credibility_flags`.

### 7. Stage fit

0→1 vs 1→10 vs scale preference. Probes:

- "Describe the last time you brought something from nothing to something. What pace did you enjoy?"
- "Describe the last time you scaled something from 10 to 100. Did you enjoy it the same way, more, or less?"

Record `stage_preference`. Downstream skills use this to flag mis-fits (a 0→1 founder pointed at a mature market is a mis-fit even if domain matches).

### 8. Constraints and resources

Time available per week. Runway. Geography. Family commitments. Regulatory exposures (non-compete, clearances, visa). Health constraints. Anything that bounds feasible markets.

Frame it honestly: "These aren't judgements, they're guardrails. What's off the table practically?"

## Output contract

At end of interview (or after processing the written brief), write both files atomically to `./persona/` in the cwd by default. Create the directory if it doesn't exist.

**Override:** if the user or invoking context specifies a different output directory (e.g. an eval harness saying "save outputs to <path>"), respect that override and write `persona.md` + `persona.json` into the specified directory instead. The filenames stay the same.

- **`persona.json`** — full schema in `references/persona-schema.md`. Include `schema_version: "1.0"` at the top so future skill revisions can read older personas safely.
- **`persona.md`** — narrative version. Use `assets/persona-template.md` as the output scaffold.

Both files use the founder's voice where verbatim; your synthesis elsewhere. Cite direct quotes sparingly but specifically — a named quote is more persuasive than a paragraph of summary.

## Handoff to downstream skills

After writing the files, tell the founder:

1. Where the files live (`./persona/persona.md` and `./persona/persona.json`).
2. That `founder-market-recommender` and `founder-idea-audit` read `persona.json` automatically from the default path.
3. That they can re-run this skill to update the persona at any time — the schema is versioned.

Then **show the credibility flags explicitly**. They are the most important honest-mirror output. The founder should know which claims didn't land, and consider shoring them up (by doing the actual research, talking to the actual people, shipping the actual prototype) before invoking downstream skills. Don't be cruel, but don't hide.

## When to stop

The interview is complete when:

- All 8 sections have at least one concrete, depth-probed signal.
- `archetype_mix` is triangulated (not self-selected).
- `network.warm_intros` has either ≥3 named people or an explicit "cold start" flag per vertical the founder claimed.
- Every edge claim has either succeeded depth-probes or is listed in `credibility_flags`.

If the founder tires before this, that's fine. Write a partial `persona.json` with `incomplete_sections: [...]` listing what wasn't covered, and let downstream skills handle it. **Don't invent signals to fill gaps** — a missing field is more useful to downstream skills than a confabulated one.
