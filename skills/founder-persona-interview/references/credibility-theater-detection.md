# Credibility theater detection

The core question this reference answers: **when does a founder's claim survive probing, and when does it become a credibility flag?**

From `main.md`: *"Investors look for 'earned edge' — the kind of insight that manifests in lightning-fast answers about arcane buyer pain points that only an insider could identify."* Credibility theater is the opposite — polished claims with no retrievable specificity behind them.

## The probe → evidence → verdict loop

For every claim a founder makes that maps to a `pillar_score` dimension (Experience, Insight, Skill-Edge, Network, Obsession), run this loop:

1. **Accept the claim as stated.** Don't argue. Let them say what they want to say.
2. **Ask one specific, non-leading follow-up** that only someone with the earned version of the claim could answer quickly.
3. **Listen for two things:** *specificity* (named people, named cases, named edge-cases) and *speed* (fast + confident, or slow + hedging).
4. **Verdict:**
   - **Pass:** specific + fast → log evidence, no flag.
   - **Partial:** specific but slow, or fast but vague → log what they said, ask one clarifier, decide.
   - **Fail:** vague + slow, or deflects, or changes the subject → log as a credibility flag with the exact claim string and dimension.

Do not tell the founder in-conversation that they failed a probe. The flag is a downstream artefact — the interviewer's honesty to downstream skills, not a performance critique in the room. At the end of the interview, surface the flags to the founder as "things downstream skills will weight conservatively", not "things you got wrong".

## Probe pattern per dimension

### Experience / Market Edge

Claim shape: *"I worked in X for N years"* or *"I know the Y industry."*

Good probes (pick one that matches the claimed vertical):

- **Healthcare:** "What's a prior-auth workflow gotcha that surprises new providers? Or: what's typically wrong with a payer's EOB parsing logic?"
- **Fintech (payments):** "What's the chargeback-ratio threshold at which card networks start applying penalty tiers? Or: what's the typical SMB onboarding KYC drop-off rate?"
- **Legal:** "What's a discovery-stage workflow that partners still do manually that associates hate? Or: what's the typical billable-hour leakage rate at a mid-size firm?"
- **Logistics / supply chain:** "What's the typical dwell-time variance at a Long Beach terminal vs Savannah? Or: what's the normal EDI document set a 3PL needs to support?"
- **Enterprise SaaS buyer:** "What's the typical path from an IT gatekeeper to the economic buyer, and at what ACV does that path change?"

Pass signal: names a specific number, range, workflow, or named sub-actor within 15 seconds.
Fail signal: "it depends", "there's a lot of variation", "I'd have to think about that", or a generic answer any outsider could Google.

### Technical Edge

Claim shape: *"I'm technical"*, *"I can build the MVP"*, *"I'm a hacker"*.

Good probes:

- "What's the last thing you shipped end-to-end? How long did it take?"
- "If I asked you to prototype an MVP for this idea in 72 hours, what specifically would you build? What's the shortcut, what's the hack?"
- "What stack do you reach for first, and why?"

Pass signal: names concrete last-shipped thing with realistic time estimate; can articulate a prototype plan with specifics (framework, data source, shortcut).
Fail signal: "I'd pair with a technical co-founder", "I can prompt LLMs well enough", or a gap of >18 months since last hands-on shipping.

**Nuance:** a founder who says "I'm semi-technical, I can do SQL and Retool but I'm not a production engineer" is *passing* the probe — they're calibrated. The flag is for over-claiming, not for being non-technical.

### Network

Claim shape: *"I have a network in X"*, *"I know people in Y"*, *"I can get customers easily."*

Probe: "Name the first three people you'd call to get a paying customer in [specific vertical]. Full names, current roles."

Pass signal: three named people with current roles, offered without hedging.
Partial signal: two named people + "I'd also reach out to my network."
Fail signal: zero named people; "I can make introductions"; "I know a lot of people in that space."

**Do not accept LinkedIn connections as network capital.** Network capital is the people who would reply to a cold Slack from this founder within 24 hours.

### Obsession / Passion

Claim shape: *"I'm obsessed with this"*, *"I've been thinking about this for years"*, *"This is my passion."*

Probe: "What have you been reading, tinkering on, or writing about in this space in your free time in the last 6 months, with no external reward?"

Pass signal: specific artefact (a substack post, a spreadsheet, a repo, a group chat they run, a conference talk they gave) in the last 6 months.
Fail signal: "I think about it all the time", "I read a lot about it", "I follow everyone in the space on Twitter" — these are consumption, not production.

The Under30CEO test: *do they naturally spend free time on this?* Consumption is weak evidence; creation, community-building, or specific analysis is strong evidence.

### Non-obvious insight / Idea Maze

Claim shape (arises during skill 3 audit, but foreshadowed here): *"I have a unique insight about this market."*

Probe: "What have the last three attempts at this problem gotten wrong, and what's changed that makes it solvable now?"

Pass signal: names three specific prior attempts with specific failure modes and a coherent now-possible thesis.
Fail signal: can't name any prior attempt; "the timing is just right"; generic "AI changes everything" claims.

## Recording a credibility flag

In `persona.json`:

```json
"credibility_flags": [
  {
    "claim": "<exact claim string the founder made>",
    "why_flagged": "<one sentence: what the probe revealed>",
    "dimension": "<experience | insight | skill_edge | network | obsession>"
  }
]
```

The `dimension` must match a `pillar_scores` key so downstream skills can cross-reference.

## What this is NOT

- **Not a hostile interrogation.** The tone is warm curiosity. Most founders fail some probes; that's normal and fixable.
- **Not a binary score.** A founder can pass Market Edge, fail Technical Edge, and be a strong venture candidate for the right idea in the right team.
- **Not permanent.** Probes fail today; the founder ships a thing next month; the probe passes. The persona is versioned for this reason.
- **Not private.** The founder sees every flag at the end. Transparency is the whole point — this document exists to make the handoff to downstream skills honest, not to secretly downgrade the founder.
