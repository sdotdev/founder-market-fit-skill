---
name: founder-idea-audit
description: Audits a specific startup idea for how well it fits *this founder* using their persona.json. Applies main.md's 1-100 weighted scorecard (Experience 25% / Insight 20% / Skill-Edge 20% / Network 15% / Obsession 20%) with preserved scoring bands (75-100 strong / 40-74 promising / <40 high-risk), surfaces red flags from the FMF research, cross-checks credibility flags, and proposes gap-mitigation. Use whenever the user says "should I build X", "audit this idea", "is this idea a good fit for me", "founder-market fit for <idea>", pastes an idea description asking for feedback tied to their profile, or asks for a go/no-go on a specific wedge. Also trigger after founder-market-recommender when the user picks a direction and wants to pressure-test it. This skill does NOT score the idea in a vacuum — every dimension is scored against the founder's persona, so the same idea can score 85 for one founder and 25 for another.
---

# Founder Idea Audit

## What this skill does

Takes a founder's persona + a specific startup idea and produces a disciplined founder-market-fit audit with:

1. **Quantitative score 1-100** using `main.md`'s five-dimension weighted scorecard.
2. **Qualitative four-pillars narrative stress test** (Experience / Knowledge / Network / Passion).
3. **Top 3 red flags** from the FMF research catalogue.
4. **Gap-mitigation plan** naming specific co-founder archetypes, advisors, and design partners from `persona.network.warm_intros`.
5. **Investor-ready narrative paragraph** — "why you, why now, why this".
6. **Pivot suggestion** if score falls below 40.

Output contains two framings side-by-side: a **founder-coaching** section (honest, next-steps focus) and a separately-framed **investor-ready narrative** paragraph. Per Sam's design intent, both are always included.

## Canonical scorecard (from main.md, non-negotiable)

| Component | Weight | 10/10 signal | 1/10 signal |
|---|---|---|---|
| Experience Alignment | **25%** | 5+ years direct domain tenure; lived the problem | Outsider perspective; no prior industry exposure |
| Non-Obvious Insight | **20%** | Ownership of a "secret" truth; understands the idea maze | Second-hand anecdotes; surface-level problem understanding |
| Technical / Skill Edge | **20%** | Differentiated skill that maps to the business model | Generic skill set; mismatch between skills and revenue model |
| Network Density | **15%** | Immediate access to first 10 customers and top talent | Zero industry connections |
| Obsession / Stamina | **20%** | Missionary identity; personally dependent on outcome | Mercenary identity; opportunistic quick-exit goal |

**Interpretation bands (preserve verbatim):**
- **75–100** — Strong Alignment. The founder has a compelling "Story" and an unfair advantage. Iteration and PMF likely faster than peers.
- **40–74** — Promising but Fragmented. May have some pillars strong but lacks network or secret insight. Strategy: add advisors/co-founders to fill gaps.
- **<40** — Pre-PMF / High Risk. Fundamental mismatch. Consider significant pivot or team restructure before venture-scale funding.

Do not re-weight. Do not re-normalise the bands. These thresholds are cited in the research and in Sam's `CLAUDE.md` as canon. The full scoring math with evidence requirements is in `references/scorecard-weighting.md`.

## Input contract

- **Persona:** `./persona/persona.json` by default, or `--persona <path>`, or pasted inline.
- **Idea:** provided conversationally or as a written description. Must include at minimum: what the product is, who the target buyer is, and a rough business model (or the founder's best guess).
- **Optional context:** any prior discovery work, any pitch materials, any design partner conversations already in progress.

If persona is missing, stop and say: *"I don't see a persona at `./persona/persona.json`. Run `founder-persona-interview` first, or paste your persona here."* Do not audit without a persona.

If the idea description is too thin to score, ask one round of clarifying questions (target buyer? business model? what's the wedge?). Don't score a ghost.

## Modes: conversational vs static brief

As with `founder-persona-interview`, support both:

- **Conversational:** user describes the idea briefly, you probe for missing dimensions (especially the **idea-maze probe**: "what did the last three attempts at this problem get wrong, and what's changed?"), then produce the audit.
- **Static brief:** user pastes a complete idea description. Score directly. If the idea-maze probe isn't answered in the brief, **note its absence explicitly as an insight gap** — don't fabricate an answer.

## Scoring process

Follow this sequence for every audit:

### 1. Read the persona
Pull the key fields: `pillar_scores` (starting baseline — these are the founder's general-purpose scores), `credibility_flags` (will adjust per-idea scores downward), `edges`, `network`, `obsession_signals`, `psychographic`, `stage_preference`, `constraints`.

### 2. Read the idea
Identify: target vertical, target buyer, business model, wedge/MVP, claimed unique insight, evidence of prior discovery.

### 3. Score each of the five dimensions 1–10
For each dimension, cite evidence from BOTH the persona and the idea. A dimension's score reflects the *alignment*, not either side alone. See `references/scorecard-weighting.md` for per-dimension scoring rubrics.

### 4. Apply credibility-theater crosscheck
For each `credibility_flag` in the persona whose `dimension` matches a scorecard component, apply the penalty rule in `references/credibility-theater-crosscheck.md`. A founder who claims 7-year healthcare experience but whose persona flagged that claim as unsupported should not score 9/10 on Experience for a healthcare idea — they should score 2–4/10.

### 5. Apply the idea-maze probe
Either the idea description answers "what did prior attempts get wrong and what changed?" — in which case score the Insight dimension based on that answer's quality (see `references/idea-maze-probe.md`) — or note the absence as an insight gap and score Insight conservatively (5 or below).

### 6. Compute weighted total
`(Experience × 2.5) + (Insight × 2) + (Skill-Edge × 2) + (Network × 1.5) + (Obsession × 2) = N/100`.

The weights (25/20/20/15/20) must sum to 100 for each dimension × weight-multiplier combination — i.e. score × multiplier per row, sum.

### 7. Apply interpretation band
75–100 / 40–74 / <40. Cite the band explicitly in the output. Do not invent intermediate bands.

### 8. Run the four-pillars qualitative stress test
For each of Experience / Knowledge / Network / Passion, write one paragraph testing whether the founder can tell a *defensible inevitability story* for this idea. See `references/four-pillars-stress-tests.md` for the probes per pillar.

### 9. Surface top 3 red flags
From `references/red-flags-catalogue.md`, pick the 3 most-relevant to this founder × idea combination. Cite the specific persona/idea evidence that triggered each.

### 10. Draft gap-mitigation plan
- **Co-founder archetype needed** (if skill-edge or market-edge pillar is low) — name the specific archetype (Hacker / Hustler / Hipster / Hound) based on the persona's gap.
- **Advisors to engage** — specific expertise gaps the persona reveals.
- **Design partners to secure** — name 3 from `persona.network.warm_intros` matching the idea's target vertical. If no warm intros match, flag cold-start with a 30-day plan to secure 5 conversations.
- **Learning plan** — specific topics the founder should study based on knowledge gaps.

### 11. Draft the investor-ready narrative
One paragraph, third-person-narrative voice, answering "why you, why now, why this" — tight, defensible, no hedges, citing the founder's specific earned edge. This is the paragraph an investor would quote back. If the audit score is <40, **do not write a confident narrative** — instead write "The founder-market-fit narrative for this idea does not yet hold; here is why..." and be honest about what's missing.

### 12. If score <40, write a pivot suggestion
Propose ≥1 concrete pivot: either the same idea for a different buyer where persona network/edge stronger, OR a different idea in the same founder's wheelhouse. Cite specific persona evidence for the pivot direction.

## Output contract

Use `assets/audit-report-template.md` as the scaffold. Write to stdout by default, or to `./audit-<idea-slug>.md` if the user asks for a file. The output must include, in this order:

1. Score header (N/100 — band name)
2. Per-pillar breakdown table (dimension, score, weight, weighted contribution, evidence, gap)
3. Four-pillars qualitative stress test
4. Top 3 red flags
5. Gap-mitigation plan
6. Investor-ready narrative paragraph (OR the "narrative does not yet hold" alternative if <40)
7. Pivot suggestion (only if <40)

## Anti-patterns to avoid

- **Do not score an idea in isolation** from the persona. Same idea, different founder, different score.
- **Do not re-weight the components** to fit a preferred outcome. If the math says 38, the band says <40, write that.
- **Do not soften the red flags** because the founder will read the output. Honest red flags are the point.
- **Do not invent evidence** where the persona has a gap. Absence of persona evidence is itself a gap finding.
- **Do not produce an investor narrative for a sub-40 audit.** Investors see through confident narratives on weak FMF and the skill should not help founders fake it.
