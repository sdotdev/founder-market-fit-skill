# MVP PRD Template

Use this template to produce the PRD skeleton for the top-ranked idea. Fill every section — do not leave placeholders. Sections marked *(skip if not applicable)* can be omitted with a one-sentence explanation.

This is a **skeleton PRD**, not a production spec. Its purpose is to give the founder a clear mental model of the MVP before they talk to engineers or co-founders. It should be readable in 10 minutes.

---

## PRD: {idea_title}

**Founder:** {founder_name}
**Date:** {YYYY-MM-DD}
**Status:** Draft — pre-validation

---

### 1. Problem statement

*2–3 sentences. What specific pain does this solve, for whom, and why existing solutions fail.*

The target user is **{specific job title / role}** at **{company type / size}**. They currently {describe the painful workaround}. Existing solutions fail because {root cause — pricing, feature mismatch, distribution gap, trust barrier, etc.}.

---

### 2. Target user (ICP)

*Be specific. Vague ICPs produce vague products.*

| Field | Value |
|---|---|
| Role | {e.g. "Head of payments at Series B fintech"} |
| Company type | {e.g. "SMB merchant processing $1–10M ARR"} |
| Geography | {e.g. "US-based, primarily Shopify/WooCommerce"} |
| Buying trigger | {what event makes them look for this — e.g. "chargeback ratio exceeds 0.8%"} |
| Budget signal | {how they currently spend money on this problem} |

---

### 3. Jobs-to-be-done (core)

*List the 2–3 things the user most needs to accomplish. Use "When I [situation], I want to [motivation], so I can [outcome]" format.*

1. When {situation}, I want to {motivation}, so I can {outcome}.
2. When {situation}, I want to {motivation}, so I can {outcome}.
3. *(optional)* When {situation}, I want to {motivation}, so I can {outcome}.

---

### 4. MVP feature list

*MoSCoW: Must / Should / Could / Won't (for MVP). Ruthlessly cut anything that isn't Must.*

#### Must have (MVP blockers — without these the product has no value)
- {Feature 1 — one sentence describing behaviour, not implementation}
- {Feature 2}
- {Feature 3}

#### Should have (important but not day-1)
- {Feature}
- {Feature}

#### Could have (nice-to-have, post-MVP)
- {Feature}

#### Won't have in MVP (explicitly out of scope)
- {Thing that might seem obvious but is deliberately deferred}
- {Reason: {why it's deferred — complexity, not-core-loop, premature scaling}}

---

### 5. Non-goals

*Things the MVP will never do, to prevent scope creep.*

- This product does **not** {out-of-scope concern 1}.
- This product does **not** {out-of-scope concern 2}.

---

### 6. Key metrics (how we know it's working)

*Pick 2–3 metrics that matter at MVP stage. Avoid vanity metrics.*

| Metric | Target at 90 days |
|---|---|
| {Primary activation metric} | {number} |
| {Retention / engagement metric} | {number or trend} |
| {Revenue / pilot signal} | {number} |

---

### 7. Technical constraints

*Based on the founder's `edges.technical.strength_1_to_10` and credibility flags.*

- {Constraint 1 — e.g. "No production ML pipeline in MVP; use rules-based logic until a technical co-founder joins"}
- {Constraint 2 — e.g. "Must integrate with Stripe Radar API; no proprietary chargeback data pipeline"}
- {Constraint 3 — e.g. "No-code or Retool acceptable for internal tooling; Webflow + Airtable acceptable for V1 customer-facing UI"}

*Stack suggestion (non-prescriptive):* Given technical edge score of {N}/10, a realistic MVP stack is {suggestion — e.g. "Next.js + Supabase + Stripe, with a Python backend for any data processing; no custom ML"}.

---

### 8. Risks and open questions

| Risk | Likelihood | Mitigation |
|---|---|---|
| {Risk 1 — e.g. "Visa API access required"} | High / Med / Low | {specific action — e.g. "Verify Visa Resolve Online access requirements before committing to this stack"} |
| {Risk 2} | | |
| {Risk 3} | | |

**Open questions before building:**
1. {Question that needs a customer conversation to answer}
2. {Question that needs a technical spike to answer}
3. {Question that needs a legal/regulatory check}

---

### 9. First 30-day build plan

*Concrete, ordered steps. Not a sprint plan — a sequence of decisions and artefacts.*

1. **Week 1:** {Specific action — e.g. "3 discovery calls with named warm intros to validate the job-to-be-done"}
2. **Week 2:** {e.g. "Wireframe the core loop; share async with the 3 discovery call contacts for feedback"}
3. **Week 3–4:** {e.g. "Ship a Retool/no-code prototype to 2 design partners; collect structured feedback"}
4. **End of 30 days:** {The artefact that will exist — e.g. "A working prototype with 2 paying pilot users or a clear 'why not' from the discovery calls"}
