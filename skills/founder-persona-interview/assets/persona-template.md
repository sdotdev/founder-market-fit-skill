# Persona: {founder_name}

*Interview date: {interview_date}*
*Schema version: 1.0*

---

## Summary

{One paragraph, 4–6 sentences. Articulate: their dominant work pattern (not job title), strongest edge, weakest edge, primary archetype, one-line psychographic read, and the core constraint that bounds their choices. Avoid hedges — downstream skills need a crisp read.}

---

## Archetype

**Primary:** {archetype_primary} ({archetype_mix[primary]*100}%)
**Secondary:** {archetype_secondary} ({archetype_mix[secondary]*100}%)
**Full mix:** Hustler {X}% / Hacker {X}% / Hipster {X}% / Hound {X}%

{2–3 sentences citing the specific probe answers that drove this triangulation. Quote the founder directly where possible.}

---

## Edges

### Technical Edge — {strength}/10
**Claim:** {claim}
**Evidence:**
- {evidence[0]}
- {evidence[1]}
**Depth probe:** {passed / failed}
{If failed, note here briefly — the credibility flag section carries the fuller note.}

### Market Edge — {strength}/10
**Claim:** {claim}
**Evidence:**
- {evidence[0]}
- {evidence[1]}
**Depth probe:** {passed / failed}
**Entrenchment risk:** {yes / no}
{If yes, explain what signals triggered the risk flag.}

### Catalyst Edge — {strength}/10
**Claim:** {claim}
**Evidence:**
- {evidence[0]}
- {evidence[1]}
**Depth probe:** {passed / failed}

---

## Network

### Communities
| Community | Venue | Embeddedness |
|---|---|---|
| {name} | {online/offline} | {speak/moderate/contribute/lurk} |

### Warm-intro graph
**{Vertical 1}**
- {Named contact 1, role}
- {Named contact 2, role}
- {Named contact 3, role}

**{Vertical 2}** — *cold start*

### Insider markers
- {marker 1}
- {marker 2}

---

## Psychographic: Missionary vs Mercenary

**Missionary:** {score}/10
**Mercenary:** {score}/10

{One paragraph on the blend. Cite the specific evidence — quotes from the "what keeps you building when the money stops" probe, the ideal-exit answer, and the would-you-still-do-this-unpaid probe.}

---

## Obsession signals

- *(specificity {score}/5)* {signal}
- *(specificity {score}/5)* {signal}

{One sentence: what these obsessions reveal about the kind of market they'd survive the 5-year slog in.}

---

## Stage fit

**Preference:** {0_to_1 / 1_to_10 / scale / mixed}

{One sentence citing the specific past-experience evidence.}

---

## Constraints

- **Time per week:** {hours}
- **Runway:** {months}
- **Geography:** {location}
- **Family:** {context}
- **Regulatory:** {non-competes, clearances, visa, etc.}
- **Other:** {anything else that bounds feasible markets}

---

## Pillar scores (feeds idea-audit)

| Pillar | Score (1–10) | Evidence |
|---|---|---|
| Experience | {N} | {one-line citation} |
| Insight | {N} | {one-line citation} |
| Skill-Edge | {N} | {one-line citation} |
| Network | {N} | {one-line citation} |
| Obsession | {N} | {one-line citation} |

---

## Credibility flags

*These are claims the interview couldn't fully corroborate. Downstream skills will weight these dimensions conservatively. Not a failure — a prompt for where to invest in shoring up before the next pitch.*

- **{claim}** (dimension: {dimension}) — {why_flagged}

---

## Incomplete sections

*Sections not covered in this interview (if any):* {list or "all sections covered"}

---

## Next steps

1. `founder-market-recommender` will read `persona.json` from this directory to suggest specific markets grounded in the network and edges above.
2. `founder-idea-audit` will read the same file to audit any specific idea you bring, scored against the main.md 1–100 scorecard.
3. Re-run `founder-persona-interview` any time to update this persona — especially after shoring up any credibility flags.
