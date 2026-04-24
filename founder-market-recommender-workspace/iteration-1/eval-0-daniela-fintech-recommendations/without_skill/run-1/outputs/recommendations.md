# Market Recommendations — Daniela Reyes

*Generated: 2026-04-22*
*Source persona: `eval-0-ex-stripe-pm-fintech-depth/with_skill/run-1/outputs/persona.json`*

---

## How I read the persona (one-paragraph synthesis)

Daniela is a Hustler/Hound with a 9/10 Market Edge in SMB payments, 7/10 Catalyst, and a calibrated 3-4/10 Technical Edge. She is a 0-to-1 stage preference with a 14-month runway, a 5-7 year exit shape ($200M-1B), and — crucially — an 18-month non-solicit on Stripe's SMB customer book. Warm-intro graph has three named SMB-payments contacts (Priya Nair / Tom DiFranco / Sarah Okwu), and embedded finance is explicitly cold-start. Obsessions (9-month SMB chargeback Substack, SMB fintech M&A spreadsheet) are convergent with her Market Edge, not scattered. This narrows the recommendable surface: SMB-payments adjacencies that (a) do not route through Stripe's current book, (b) exploit arcane Market Edge like chargebacks / KYC / interchange, (c) have a buyer reachable via the three warm intros, and (d) tolerate a non-production-engineer founder.

---

## Top market recommendations

### 1. Chargeback dispute automation for high-volume SMB card-not-present merchants

**Why this market, for Daniela specifically.** She co-authored Stripe's internal chargeback-ops playbook, writes an unprompted Substack on SMB chargeback disputes (9 months running), and recalls without hedging that Visa VMP triggers at 0.9% and VDMP at 1.8% with $25K/month in fees. That is not generic "fintech experience" — it is exactly the arcane pain she has lived in and still thinks about for free. Buyer profile is sub-enterprise merchants getting crushed by VDMP penalties or skating toward VMP — a buyer she understands viscerally.

**Warm-intro path.** Tom DiFranco (founder, LedgerLift) is the most natural first customer or design partner if LedgerLift or his adjacent network has SMBs with chargeback volume; Priya Nair (head of payments, Earnest) is a second-ring buyer if Earnest has any merchant-facing SMB book. At minimum they are first conversations, not cold calls.

**Market-dynamics class.** Transactional / regulated-adjacent SaaS. The product touches card-network rules (regulated surface) but the buyer motion is a SaaS subscription with usage-flavoured pricing.

**Business model.** Hybrid: flat SaaS base + usage component (per dispute filed, or per $ recovered). Usage alignment matters because the value metric is dispute win-rate and the buyer wants incentive alignment.

**Non-solicit check.** Safe *if* she targets merchants she did not own at Stripe. The non-solicit binds customer solicitation, not category re-entry. Design-partner pool must be sourced through non-Stripe channels (Money 20/20 roster, alumni Slack inbound, LedgerLift-style referrals).

**Risks.** Technical Edge gap — a production dispute-filing system touches card networks, evidence ingestion, and potentially PCI scope. She needs a technical co-founder or a heavy no-code/Retool-plus-services wedge for the first 10 customers.

---

### 2. SMB KYC / onboarding drop-off remediation (co-owned LLC specialist)

**Why this market, for Daniela specifically.** She named — without prompt — a 38% KYC drop-off on SMB payment onboarding, concentrated on the ownership-percentage field for co-owned LLCs. That is a named arcane edge case, not "KYC is hard." The wedge is a thin-layer product that sits in front of a PSP or bank's onboarding flow and specifically fixes the co-owned-LLC ownership-field failure mode (guided capture, inferred percentages from Secretary of State filings, doc re-use).

**Warm-intro path.** Sarah Okwu (CFO, Rhombus) is the natural early-design-partner conversation — a CFO running onboarding against multiple providers is exactly the person whose pain this addresses. Tom DiFranco again as a second-ring node.

**Market-dynamics class.** Regulated SaaS. KYC rules (BSA, FinCEN CDD) are federal, and the product must not break compliance posture — it augments it.

**Business model.** Subscription (seat- or flow-based) with a per-onboarding-attempt usage rider. Straight SaaS works because the buyer is a fintech/SMB-services ops leader who already budgets for KYC tooling.

**Non-solicit check.** Clean — the buyer is a fintech platform or neobank, not Stripe's SMB merchants.

**Risks.** KYC is a crowded category at the incumbent layer; the wedge must be *the ownership-field failure*, not "better KYC generally." If it broadens, she loses the arcane-edge moat. Also: regulated class means longer sales cycles — mercenary score 7 and 14-month runway are okay but tight; plan for a seed round at month 9.

---

### 3. Interchange-arbitrage tooling for hybrid-POS SMBs

**Why this market, for Daniela specifically.** Arcane edge: she can rattle off that Visa interchange reimbursement fees differ 15-40bps between card-present and card-not-present for the same MCC, and that this is exploitable via hybrid POS. Most founders in payments do not know this at her level of specificity. The product is a decisioning layer that routes transactions through the optimal acceptance rail (or configures POS/e-com flows to capture the lower-interchange variant) for SMBs with both physical and e-com channels — restaurants-with-delivery, retail-with-Shopify, etc.

**Warm-intro path.** Priya Nair (Earnest) for a partner-bank angle if Earnest has merchant-acquiring adjacency; Tom DiFranco (LedgerLift) for SMB-finance-adjacent referrals. The Stripe alumni #payments Slack (she moderates) is a viable secondary distribution channel.

**Market-dynamics class.** Transactional / usage-based. Value is measured in bps saved per transaction — naturally usage-priced.

**Business model.** Usage — a share of interchange savings (gainshare) or flat bps on routed volume. Subscription does not align incentives here; buyers will not pay a flat SaaS fee for a benefit that scales with their volume.

**Non-solicit check.** Safe provided initial merchants are not Stripe's current SMB customers. Hybrid-POS SMBs often use Square, Toast, Clover, Lightspeed etc. — a cleaner target pool anyway.

**Risks.** Proving savings requires real transaction data — a chicken-and-egg integration problem. Pilot design must be aggressive: "we'll work for free until you see X bps saved, then we take Y% of that." Also: 0-to-1 preference is well-matched here (pilot-heavy design-partner phase).

---

### 4. SMB fintech M&A advisory / diligence-infrastructure micro-software (exploratory)

**Why this market, for Daniela specifically.** She maintains an unprompted spreadsheet tracking every SMB fintech M&A deal since 2022. That is not a throwaway signal — it is a 2+ year obsession that overlaps with her Hound archetype. A product here could be either (a) a productised diligence tool for acquirers/operators evaluating SMB-payments targets, or (b) a data/research subscription for PE and strategics in the space.

**Warm-intro path.** Weaker than #1-3. Sarah Okwu (CFO) is a plausible early buyer if Rhombus does corp-dev. Money 20/20 speaker status opens warm conversations with strategics. Still partially cold-start on the buyer side (acquirers, not operators).

**Market-dynamics class.** SaaS (if productised as a research tool) or services-with-software (if advisory-first). Lean toward SaaS for outcome-shape fit with her 5-7 year exit target.

**Business model.** Subscription (annual research seats) — possibly a hybrid with a per-deal usage component. Not a fit for usage-only pricing because buyer cadence is lumpy.

**Non-solicit check.** Clean — the buyer is an acquirer or strategic, not a Stripe merchant.

**Risks.** This is the weakest-warm-intro recommendation of the four. It exploits Obsession and Hound but does not use her Hustler deal-closing muscle as directly. Flag as exploratory — confirm buyer pull via 5-10 discovery calls before committing to a stage-1 build.

---

## Markets to avoid or treat as cold-start

### Embedded finance (BaaS, embedded lending, embedded insurance)
**Why flagged.** The persona is explicit — embedded finance warm-intro list is empty, labelled `cold_start: true`. She knows the terrain academically but has no named contact who can be a first design partner. Combined with her modest Technical Edge (these products tend to be infra-heavy) and her 14-month runway, this would be a 6+ month network-building detour before the first customer conversation — expensive time for a 0-to-1 mercenary-leaning founder. Treat as cold-start; revisit after she has seeded 5-10 warm intros in the space.

### Anything sold into Stripe's current SMB customer base
**Why flagged.** 18-month non-solicit. This is a hard legal constraint, not a strategic one — it binds independent of market fit. It removes a huge chunk of the most obvious ICP and must be respected in design-partner sourcing for any of the four recommendations above.

### Consumer fintech (neobanks, budgeting apps, investing for retail)
**Why flagged.** Consumer market-dynamics class — acquisition is performance-marketing and brand, not the warm-intro / deal-closing / partner-bank motion Daniela has. Her Hustler edge is B2B deal-closing; her Hipster score is 10% (no brand/craft signal). Missionary score 5 with explicit "not a save-the-world type" framing further disqualifies the missionary energy consumer fintech typically demands. Avoid.

### Crypto / DeFi / stablecoin rails (unless explicitly re-scoped)
**Why flagged.** No persona evidence of edge here — not named in arcane callouts, not in the M&A tracker focus, not in the Substack. Regulatory posture is adversarial right now in the US, which extends sales cycles for a 14-month-runway founder. Avoid unless she surfaces a specific wedge.

### Ops-intensive verticals she has no network in (healthcare fintech, construction fintech, legal fintech)
**Why flagged.** "SMB payments" is a real, narrow edge — "vertical fintech for X industry" is a different network game and would require cold-building domain access in the vertical. Her obsessions are tightly coupled to SMB-payments-specifically, not SMB-broadly. Do not cross-vertical without a co-founder who brings the vertical Market Edge.

---

## Cross-cutting risks and mitigations

- **Technical Edge gap (3-4/10).** All four top recommendations assume either (a) a technical co-founder, or (b) a services-heavy MVP wedge where Retool + humans handle what software eventually will. This must be resolved before committing to stage-1 build. Her Catalyst Edge (running a 7-person launch team) supports recruiting a technical co-founder.
- **Non-solicit propagation.** Any pilot-customer pipeline must be audited — if she finds herself calling a former Stripe SMB contact, she has to re-route through a non-Stripe introduction (alumni Slack with a third-party intermediary, Money 20/20 floor, etc.).
- **Runway vs regulated-class sales cycles.** Recommendations 1, 2, and 3 all touch regulated surfaces. Plan the seed-raise timing for month 8-9, not month 12-13.
- **Mercenary-leaning psychographic (7 merc, 5 miss).** She will walk from a problem that does not show a 5-7 year arc. Do not recommend category-creation plays without a clear commercial trigger in year 1-2.

---

## TAM note

I have not put dollar-sized TAM figures on any of the four markets. Public TAM numbers in SMB payments adjacencies are heavily contested and would be *(unverified)* in this context; Daniela's own M&A tracker is a better ground-truth source than an analyst report for deal comps. Any specific TAM should be validated against her spreadsheet plus 5-10 buyer discovery calls before being cited in a pitch.

---

## Recommended next step

Hand this persona + recommendations to **`founder-idea-audit`** next. Before committing to a stage-1 build on any of markets #1-#4 above, audit the specific idea formulation against the 1-100 scorecard — Technical Edge will be the likely scoring gap and should be resolved (co-founder signed, or services-wedge scoped) before resources are committed.

Suggested order of operations:
1. `founder-idea-audit` on market #1 (chargeback automation) — highest evidence density.
2. 5-10 buyer discovery calls via Priya / Tom / Sarah on whichever of #1-#3 scores highest.
3. Technical co-founder search in parallel — 60-day target.
4. Re-run `founder-persona-interview` when non-solicit expires or a technical co-founder signs, to refresh the downstream recommendation surface.
