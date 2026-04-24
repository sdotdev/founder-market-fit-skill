# Edge interview playbook

From the Entrepreneur First (EF) Edge framework via `main.md`. Three edges — Technical, Market, Catalyst. Most founders have 0–2 genuine edges. Zero is a flag. Three is rare and usually means one is inflated; probe harder.

Run every edge through the probe → evidence → verdict loop from `credibility-theater-detection.md`. This file lists the probes specific to each edge and the nuance the research calls out.

---

## Technical Edge

**Definition (from `main.md`):** Differentiated deep-tech expertise — PhD-level research, systems-level mastery, or the ability to build on the boundary of what's currently possible.

**Note:** "Can ship code" is not a Technical Edge. Most hackers have shipping capability; few have a *differentiated* technical edge. This distinction matters — a full-stack engineer is a Hacker archetype but may have no Technical Edge in the EF sense.

### Probes

- "What's a technical capability you have that 99% of engineers don't?"
- "What's the last technical paper or deep-dive you engaged with that you thought was wrong in a specific way?"
- "If a senior engineer at a top lab reviewed your work, what would impress them? What would they roast?"
- "Is there a category of problem where you think you'd outperform a strong generalist engineer by 10x?"

### Scoring

- **Strong (8–10):** PhD or postdoc in a relevant domain; research-lab experience; named publications/patents; builds on a platform like Anyscale / Modal / a custom ML training stack; can articulate a technical moat.
- **Moderate (4–7):** 5+ years of senior engineering in a specialised stack (distributed systems, infra, graphics, compilers, crypto) but not research-grade.
- **Weak (1–3):** Full-stack web / mobile / generic AI app. Shipping capability without differentiation. Still valuable, but not a Technical Edge — more likely the Hacker archetype.

### Record in persona.json

```json
"edges.technical": {
  "claim": "<what they said>",
  "evidence": ["<specific artefacts>"],
  "depth_probe_passed": true_or_false,
  "strength_1_to_10": N
}
```

---

## Market Edge

**Definition (from `main.md`):** Industry depth that lets the founder identify non-obvious problems and opportunities insiders recognise but outsiders can't see. It is the most common edge among successful founders and the most prone to credibility theater.

**Critical nuance — the "sufficient but not excessive" test:** from `main.md`, *"While a lack of experience leads to shallow insights, too much time in an industry can lead to entrenchment. Founders who have spent decades in a sector may lose the capacity for disruption."* The optimal Market Edge is intimate enough to know the arcane pain, naive enough to believe it can be solved.

### Depth probes (tailored per vertical)

See the vertical-specific probe bank in `credibility-theater-detection.md`. Key verticals with tested probes:

- Healthcare: prior-auth gotchas, EOB parsing, billing-code edge cases.
- Fintech / payments: chargeback thresholds, KYC drop-off, interchange mechanics.
- Legal: discovery workflow, billable leakage rates.
- Logistics: dwell time, EDI document sets.
- Enterprise SaaS: buyer path, ACV-dependent sales motion changes.

If you're interviewing a founder in a vertical not listed, generate a probe with this template: *"What's a workflow in [vertical] that looks routine on the outside but has a specific failure mode that only people who've done it know about?"*

### Entrenchment check

After scoring strength, run the entrenchment probe:

- "What's a practice in [industry] that insiders accept as 'just how it works' but that you've privately thought was broken for years?"
- "Have you tried to change anything within [industry] internally? What happened?"

**Pass signal:** names specific practices they've pushed against (even unsuccessfully); still believes change is possible.
**Fail signal (entrenched):** "That's just how it is"; "The regulators would never allow it"; "Enterprise buyers will never adopt new workflows" — i.e., has absorbed the status quo as inevitability.

If entrenched: set `entrenchment_risk: true`. Market Edge strength stays high, but downstream skills will flag this as disruption-risk.

### Scoring

- **Strong (8–10):** 5–8 years in a specific role within the vertical, exposure to multiple customer segments, can name arcane edge cases, still believes change is possible.
- **Moderate (4–7):** 3–5 years of adjacent or partial exposure; can speak the language but misses some edge cases.
- **Weak (1–3):** <2 years or purely observational (consulting, analyst, journalist). Still valuable as a starting point but not Market Edge.

### Record in persona.json

```json
"edges.market": {
  "claim": "<what they said>",
  "evidence": ["<specific arcane answers>"],
  "depth_probe_passed": true_or_false,
  "strength_1_to_10": N,
  "entrenchment_risk": true_or_false
}
```

---

## Catalyst Edge

**Definition (from `main.md`):** Operational and communicative ability to assemble resources, rally teams, and generate momentum under pressure. Rarer than it seems — many founders have leadership *experience* but not Catalyst Edge (which is specifically about zero-to-traction momentum, not managing a mature team).

### Probes

- "Tell me about a time you assembled a team from zero for something new. How did you find the first 3 people?"
- "When's the last time you raised money, closed a lighthouse customer, or locked in a strategic partnership? Walk me through the narrative you used."
- "What's the most momentum you've ever created around an idea that wasn't your own? Why did people follow?"
- "Describe the messiest cross-functional project you salvaged. What specifically did you do in the first 48 hours?"

### Scoring

- **Strong (8–10):** Has raised money; has hired the first 5–10 people at a startup; has closed a lighthouse customer against institutional resistance; has led a team through a turnaround.
- **Moderate (4–7):** Has managed teams; has run cross-functional projects; has secured resources internally at a larger company.
- **Weak (1–3):** Individual contributor track record; no team-assembly experience; hasn't fundraised or sold.

### Record in persona.json

```json
"edges.catalyst": {
  "claim": "<what they said>",
  "evidence": ["<specific fundraising / hiring / closing examples>"],
  "depth_probe_passed": true_or_false,
  "strength_1_to_10": N
}
```

---

## Reading the combination

Downstream skills (especially `founder-market-recommender`) read the edge combination as a vector, not three independent scores. Common patterns:

- **High Market + Low Technical + Moderate Catalyst:** classic sales-led SMB or enterprise founder. Needs a Hacker co-founder.
- **High Technical + Low Market + Low Catalyst:** deep-tech researcher. Needs a Hustler or Catalyst co-founder to commercialise.
- **Moderate across all three:** well-rounded. May lack a differentiated edge; downstream skills may flag.
- **High Market + High Catalyst + Low Technical:** experienced operator. Strong for regulated or ops-heavy markets.
- **High Technical + High Catalyst:** technical founder-CEO. Rare and often very successful; make sure it's earned, not claimed.
