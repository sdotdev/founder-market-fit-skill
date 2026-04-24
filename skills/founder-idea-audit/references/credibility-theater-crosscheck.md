# Credibility-theater crosscheck

The persona-interview skill flags claims it couldn't corroborate as `credibility_flags` in `persona.json`. This reference defines how the idea-audit uses those flags to adjust per-pillar scores.

**Core rule:** a credibility-flagged claim in a dimension relevant to this idea must **cap the score** for that dimension at 4/10 unless the idea-specific evidence overwhelmingly rehabilitates the flag.

## The map: credibility_flag.dimension → scorecard dimension

| Persona credibility_flag dimension | Affected scorecard dimension | Score cap |
|---|---|---|
| `experience` | Experience Alignment | 4/10 |
| `insight` | Non-Obvious Insight | 4/10 |
| `skill_edge` | Technical / Skill Edge | 4/10 |
| `network` | Network Density | 4/10 |
| `obsession` | Obsession / Stamina | 4/10 |

The cap applies to this idea's audit score for that dimension — not to the persona itself. If the founder shores up the flag later (ships a prototype, writes the substack, books the warm intros) and re-runs persona-interview, the flag goes away and audits after that won't be capped.

## The "rehabilitation" exception

In rare cases, the idea itself provides overwhelming evidence that rehabilitates a persona-level flag. Examples:

- Persona flagged `experience` for healthcare generally, but idea is specifically about nurse-facing tools and the founder is a 7-year ICU nurse with specificity-5 obsession on nurse handoffs. The narrower scope makes the generic flag less load-bearing.
- Persona flagged `network` because buyer verticals are cold-start, but idea's buyer is the developer community where founder has strong OSS markers.

In these cases, score up to the evidence's merits but **note the rehabilitation explicitly** in the audit's evidence field:

> "Credibility flag on `network` (dimension: network, reason: no buyer-vertical warm intros) rehabilitated for this idea because target buyer is the OSS developer community where founder has 2K-member Discord moderator status and KubeCon speaking record. Scored 7/10 rather than the default 4/10 cap."

If you can't write a rehabilitation note that specific, **apply the cap**. Don't fudge.

## The credibility compounding rule

If the persona has ≥2 credibility flags whose dimensions all apply to this idea, the audit score total is additionally penalised by 5 points, not just per-dimension. A founder with flagged `experience` AND `network` auditing an idea that requires both is structurally worse than a founder with one flagged dimension — the compounding signal is that the founder's self-perception is substantially out of step with reality, which is itself a red flag.

Example: a founder with `credibility_flags` on both `experience` and `network` audits a regulated-industry idea. Per-dimension caps apply to both (4/10 each), and the final weighted total gets an additional −5 points. This is because a founder who over-claims on two major dimensions is unlikely to have calibrated the idea's difficulty correctly — they're an order of magnitude more likely to fail the first discovery sprint.

## When there are no relevant flags

If `credibility_flags` is empty or contains only flags whose dimensions don't apply to this idea, no cross-check penalty applies. Score on merits.

## Reporting the crosscheck in the audit

The per-pillar breakdown table should show the crosscheck transparently. Use the format:

| Dimension | Base score | Cap applied | Final score | Weighted |
|---|---|---|---|---|
| Experience | 7/10 (persona merits) | Yes — flag on `experience` (persona claim: "somewhat technical", reality: Retool-level) | 4/10 | 10.0 |

If no cap applies, show "—" in the Cap column.

If the rehabilitation exception applies, show the rehabilitation note in the Cap column and the higher score in Final.

## Why this matters

`main.md`'s research on "credibility theater" is specifically about investors and customers detecting the gap between claimed edge and earned edge. The audit exists to help a founder see that gap *before* they pitch — or before they commit to an idea that their earned edge doesn't actually support.

A soft audit that ignores credibility flags protects the founder's ego but fails them strategically. The cap exists because the downside of an over-confident pitch is measurably worse than the downside of a humble one: investors and early customers both recognise earned edge faster than founders think they do, and a narrative that cracks under gentle pressure damages the founder's reputation for the next idea too.

The skill should be **kind and honest**. Kind: explain the cap clearly, offer rehabilitation paths. Honest: never paper over the flag to flatter the founder.
