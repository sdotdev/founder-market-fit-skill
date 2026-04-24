# Scorecard weighting (25/20/20/15/20) — per-dimension rubric

Canonical weights from `main.md`. Do not re-weight. The per-dimension 1–10 score is the interviewer's synthesis based on cited evidence from *both* the persona and the idea.

Weighted contribution = score × multiplier (below). Total = sum = N/100.

| Dimension | Weight | Multiplier |
|---|---|---|
| Experience Alignment | 25% | × 2.5 |
| Non-Obvious Insight | 20% | × 2.0 |
| Technical / Skill Edge | 20% | × 2.0 |
| Network Density | 15% | × 1.5 |
| Obsession / Stamina | 20% | × 2.0 |

## Per-dimension scoring rubric

### Experience Alignment (25%)

Scores the alignment between the founder's earned domain experience and the target market/buyer of the idea. Not the founder's general experience — the fit to *this idea's* market.

- **10** — 5+ years of direct, hands-on role in this idea's exact vertical and buyer segment. Cites arcane edge cases without hedging. `edges.market` in persona is 8+ AND `depth_probe_passed` is true AND no relevant credibility flag.
- **8–9** — 3–5 years in the vertical OR 5+ years in an adjacent vertical that transfers clearly. Edges.market 6–8.
- **5–7** — Exposure to the vertical through a related role (consulting, analyst, adjacent function). Can speak the language but misses some edge cases.
- **3–4** — Academic or second-hand familiarity. Has read about it, hasn't lived it.
- **1–2** — Outsider. No relevant domain exposure.
- **Adjust down** if `credibility_flags` contains `dimension: experience` — apply the crosscheck in `credibility-theater-crosscheck.md`.

### Non-Obvious Insight (20%)

Scores the founder's proprietary, defensible truth about *this idea's* problem space. The Idea Maze test: can they name what prior attempts got wrong and what changed?

- **10** — Articulates 3+ specific prior attempts and their specific failure modes AND a coherent "now-possible" thesis. Has personally encountered the failure mode.
- **8–9** — Names 1–2 prior attempts with specific failure modes. Coherent thesis.
- **5–7** — Recognises the problem is non-trivial but can't cite prior attempts specifically. "The timing feels right" without specifics.
- **3–4** — Surface-level understanding. Restates common industry opinions.
- **1–2** — Treats the problem as novel ("AI changes everything") without evidence.
- **See `idea-maze-probe.md`** for the probe protocol.

### Technical / Skill Edge (20%)

Scores the fit between the founder's differentiated technical/skill capability and *this idea's* implementation requirements. A founder can have a strong Technical Edge (per persona) and still score low here if the idea needs a different kind of technical depth.

- **10** — Founder's Technical Edge (persona) directly matches the idea's hardest technical requirement. OR: the idea is sales-led and founder has a differentiated Catalyst Edge matching the GTM.
- **8–9** — Strong match with one sub-requirement unaddressed.
- **5–7** — Moderate match; can lead but will need 1–2 specialist hires.
- **3–4** — Mismatch in ≥1 major dimension (e.g. needs ML research capability, founder is a web full-stack). Addressable with a co-founder.
- **1–2** — Fundamental mismatch; no realistic path to ship without a different team.
- **Adjust down** if `credibility_flags` contains `dimension: skill_edge`.

### Network Density (15%)

Scores the founder's warm-intro path to this idea's target buyer. Not general network — network *for this specific buyer*.

- **10** — 3+ named warm-intros in `persona.network.warm_intros` for this idea's target vertical, plus ≥1 community at `speak`/`moderate` level in buyer-adjacent venues.
- **8–9** — 3 named warm-intros; weaker community coverage.
- **5–7** — 1–2 named warm-intros; moderate community coverage.
- **3–4** — Cold-start on this vertical per persona; some adjacent community coverage that *might* transfer.
- **1–2** — Cold-start with no adjacent community coverage. First-customer conversation would be cold outreach.
- **Adjust down** if `credibility_flags` contains `dimension: network`.

### Obsession / Stamina (20%)

Scores the founder's durable commitment to this idea's problem, independent of outcome. Missionary vs Mercenary signal per persona, plus obsession-signal relevance.

- **10** — `psychographic.missionary_score` ≥8 AND at least one `obsession_signal` with `specificity_score: 5` on this specific problem space. Founder would keep working on it unpaid.
- **8–9** — Missionary ≥7 AND one specificity-4/5 obsession signal adjacent to this idea.
- **5–7** — Mixed missionary/mercenary. Obsession signals exist but don't cover this specific space.
- **3–4** — Mercenary-dominant. Obsession signals general or vague.
- **1–2** — Mercenary ≥8 AND no obsession signal in this space. Motivated by exit, not by the problem.

The 5-year test: would the founder still care about this problem in year 5, if the business was slow, if competitors were emerging, if exit was uncertain?

## Evidence requirements

Every score must cite **at least one specific evidence string** from either the persona or the idea description. Evidence sources acceptable (ranked):

1. Direct quote from persona or idea brief (strongest).
2. Specific named entity (company, person, community, artefact) from `persona.json`.
3. Specific arcane fact or workflow cited in persona.
4. Pillar score (1–10) directly from persona.
5. Score inherited from persona's own `pillar_scores` (weakest — shows you used persona but didn't add idea-level insight).

If you cannot cite at least one type-1 or type-2 evidence for a score, write "limited evidence" and score conservatively (5 or below).

## Computing the final number

Example (Daniela auditing a chargeback-dispute-automation idea):

| Dimension | Score | Multiplier | Weighted |
|---|---|---|---|
| Experience | 9 | × 2.5 | 22.5 |
| Insight | 8 | × 2.0 | 16 |
| Skill-Edge | 5 | × 2.0 | 10 (mid because idea needs tech co-founder) |
| Network | 9 | × 1.5 | 13.5 |
| Obsession | 9 | × 2.0 | 18 |
| **Total** | | | **80/100** → Strong Alignment |

Same founder on an embedded-finance idea (cold-start network, no specific obsession):

| Dimension | Score | Multiplier | Weighted |
|---|---|---|---|
| Experience | 5 | × 2.5 | 12.5 |
| Insight | 4 | × 2.0 | 8 |
| Skill-Edge | 5 | × 2.0 | 10 |
| Network | 2 | × 1.5 | 3 |
| Obsession | 4 | × 2.0 | 8 |
| **Total** | | | **41.5/100** → Promising but Fragmented, right at the band edge |

Arithmetic must always be shown in the output (the per-pillar breakdown table). If the math doesn't match the total, the table is wrong — do not silently "correct" the total; re-check the scores.
