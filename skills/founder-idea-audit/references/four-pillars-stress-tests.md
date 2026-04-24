# Four Pillars narrative stress test

From `main.md`'s qualitative audit: Experience / Knowledge / Network / Passion. The scorecard (previous reference) gives a number; the four pillars give the *story*. Both are required — numbers without narrative are easy to argue with; narrative without numbers is hand-waving.

For each pillar, write **one short paragraph** testing whether the founder can tell a defensible *inevitability story* for this idea. The question is: *"If we wound the clock forward 3 years and this idea succeeded, would the retrospective narrative feel inevitable?"*

## 1. Experience

**What to test:** can the founder articulate the moment their domain experience intersected with this specific problem? Is there a "war story" that converts a generic claim ("I worked in X for 5 years") into a specific one ("I watched Y fail a hundred times and realised Z")?

**Probes to answer internally while writing:**
- Did the founder personally encounter this problem, or did they read about it?
- Can they name the first customer who'd immediately recognise the pain?
- Would a peer in the same role instantly understand why this founder is uniquely positioned?

**Pass signal in the paragraph:** cites a specific persona moment tied to a specific problem observation.
**Fail signal:** pure credential-stacking ("5 years at X + 3 years at Y = therefore qualified").

## 2. Knowledge

**What to test:** does the founder possess a "secret" or non-obvious truth about this market? The Idea Maze question — can they name why previous attempts failed and what has changed?

**Probes:**
- Name 3 prior attempts at this problem. What did each get wrong?
- What's changed (technological, regulatory, behavioural) that makes it solvable now?
- What's the one thing they know that a smart outsider would NOT know?

**Pass signal:** specific prior attempts + specific failure modes + coherent now-possible thesis.
**Fail signal:** "AI makes everything possible"; "Timing is right"; or zero prior attempts named.

## 3. Network

**What to test:** can the founder reach the first 10 customers without cold outreach? Can they recruit the first 3–5 hires through warm network?

**Probes:**
- Name the first 10 customers they could call tomorrow.
- Name 3–5 people they could recruit or consult as first hires/advisors.
- What communities would an announcement resonate in before any paid distribution?

**Pass signal:** named first-10-customer list from `persona.network.warm_intros`; named recruit/advisor candidates.
**Fail signal:** "I have a lot of LinkedIn connections"; "I can hire"; cold-start with no mitigation plan.

## 4. Passion (Obsession/Stamina)

**What to test:** will the founder still care about this problem in year 5 when it's slow, when competitors emerge, when exit is uncertain? Is there a visceral feedback loop where the founder personally depends on the outcome?

**Probes:**
- Does the persona's `obsession_signals` cover this specific problem? With what `specificity_score`?
- Would the founder build a non-monetised version of this if no investor funded it?
- Is the `psychographic.missionary_score` high enough to survive the category's specific timeline?

**Pass signal:** specific named obsession artefacts (substack, spreadsheet, prototype, essays) about this problem or adjacent problems; Missionary ≥ 7.
**Fail signal:** obsession signals absent or generic; Mercenary dominant on a long-timeline idea.

## Writing the paragraph

Each pillar paragraph should be 3–5 sentences. No headers inside the paragraph. Direct prose. Cite persona/idea evidence by name.

**Good (Knowledge pillar for Daniela auditing chargeback-dispute automation):**
> Daniela's persona names three specific prior attempts at chargeback automation — the legacy dispute-filing services at processors, the in-house build at Stripe (which she was adjacent to), and the early-stage independents bought by Chargebacks911. She can articulate why each failed at the SMB tier: the processor tooling optimises for enterprise reps, the in-house builds never get funded past initial launch, and the independents hit a distribution ceiling. Her "what's changed" thesis — that SMB merchants are now chargeback-aware because of TikTok dispute-shop content and card-network penalty escalation — is testable. This pillar reads inevitable.

**Bad (generic):**
> Daniela has deep knowledge of chargebacks and would be a great founder here. Her experience and insights are strong. She understands the market well.

Note: the bad example would pass every substring assertion but fails the stress test — it could be written about any founder in any market.

## The inevitability test

After drafting all four pillars, re-read the set together. Ask:

> *"If I removed the founder's name from these four paragraphs, could I tell who they were from the specifics?"*

If yes: the narrative is founder-specific and defensible.
If no: rewrite until yes, or lower the per-pillar scores to match what the evidence actually supports.

Inevitability is earned, not claimed. Don't write confident inevitability narratives when the evidence is thin — that's the failure mode the skill must prevent.
