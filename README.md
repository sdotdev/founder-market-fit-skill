# Founder-Market Fit Skills

**Turn a founder's background into a validated, buildable startup direction** — in four steps, each producing a structured artefact the next skill reads automatically.

The chain: *profile the founder → identify matching markets → audit a specific idea → find a proven startup to build on*. Every output is grounded in the founder's actual evidence, not generic advice.

---

## The skill chain

```
founder-persona-interview
        ↓  persona.json
founder-market-recommender
        ↓  market-recommendations.md
founder-idea-audit
        ↓  audit-report.md
founder-ideation   ←  TrustMRR API (live revenue data)
        ↓  ideation-report.md + MVP PRD
```

Run them in order, or drop in at any step if you already have a persona.

---

## Skills

### 1. `founder-persona-interview`
**Build a structured founder profile by depth-probing every claim.**

Most founder self-assessments are checkbox quizzes — you say "I'm technical" and it accepts that. This skill does not. It probes every claim until it has evidence, records what fails as credibility flags, and produces a `persona.json` that downstream skills trust because every score is earned, not self-reported.

**When to use it:**
- "What kind of founder am I?"
- "Help me figure out my edge"
- "Profile me as a founder"
- "Assess my founder-market fit"
- You have a written self-description and want structured output
- Any downstream skill needs a `persona.json` and none exists yet

**What you get:**
- `persona/persona.md` — narrative persona document (human-readable)
- `persona/persona.json` — structured schema consumed by all other skills in this chain

**Modes:**
- **Live interview** (default): conversational 30–60 min session across 8 sections
- **Written brief**: paste 3+ paragraphs of background; skill produces persona directly from the writing without re-interviewing

**Example prompts:**
```
Profile me as a founder using founder-persona-interview.
I'll write out my background — please produce persona.md and persona.json.

---
I spent 5 years at Stripe on SMB payments, last 2 as a PM...
```
```
Help me figure out my edge. I've been an ICU nurse for 7 years
and I'm teaching myself to code. Where do I fit as a founder?
```

**Outputs example:**
```json
{
  "archetype_primary": "hustler",
  "edges": { "market": { "strength_1_to_10": 9, "depth_probe_passed": true } },
  "pillar_scores": { "experience": 9, "network": 8, "obsession": 8 },
  "credibility_flags": [{ "claim": "described self as technical", "dimension": "skill_edge" }]
}
```

**Benchmark:** 100% assertion pass rate with skill vs 36% without (across 3 diverse founder profiles, 3 runs each).

---

### 2. `founder-market-recommender`
**Get 3–5 specific markets that fit this founder — with a first-customer path for each.**

Reads `persona.json` and recommends open-ended markets grounded in the founder's actual edges, network, and obsession. Every recommendation cites named persona evidence; if it could apply to a different founder, it gets cut. Also produces a "markets to avoid" list with specific reasons.

**When to use it:**
- "What market should I explore?"
- "Where should I focus?"
- "Which vertical fits me?"
- "What should I build?" (when no specific idea exists yet)
- Immediately after `founder-persona-interview` if you want direction

**What you get:**
- Market recommendations printed to conversation (or `market-recommendations.md` if you ask for a file)
- Each recommendation includes: why it fits you specifically, market dynamics class, suggested business model, first-customer path (named people from your warm-intro graph), known risks

**Example prompt:**
```
I have my persona.json at ./persona/. What markets should I be exploring?
I want to stay in B2B and exclude crypto.
```

**Output structure per recommendation:**
```
### SMB chargeback-dispute automation
- Why this fits you: your 9-month Substack + Tom DiFranco intro last week
- Market class: regulated SaaS
- First-customer path: Tom DiFranco (LedgerLift), Sarah Okwu (Rhombus)
- Known risks: non-solicit blocks Stripe merchants for 18 months
```

**Requirements:** `persona.json` must exist. If not, the skill will tell you to run `founder-persona-interview` first.

---

### 3. `founder-idea-audit`
**Get a 1–100 founder-market-fit score for a specific idea against your persona.**

The same idea scores differently for different founders. A chargeback-automation tool scores 87 for a Stripe PM with named fintech contacts — and 31 for a generalist engineer with no payments background. This skill produces a disciplined, evidence-cited audit so you know exactly which pillars are strong, which are gaps, and what to do about it.

**When to use it:**
- "Should I build X?"
- "Audit this idea against my persona"
- "Is this idea a good fit for me?"
- "Give me a go/no-go on this wedge"
- After `founder-market-recommender` picks a direction you want to pressure-test

**What you get:**
- Quantitative score 1–100 (weighted: Experience 25% / Insight 20% / Skill-Edge 20% / Network 15% / Obsession 20%)
- Per-pillar breakdown table with evidence and gaps
- Four-pillars qualitative narrative (Experience / Knowledge / Network / Passion)
- Top 3 red flags with specific mitigations
- Gap-mitigation plan (co-founder archetypes, advisors, design partners named from your warm intros)
- Investor-ready "why you, why now, why this" paragraph
- Pivot suggestion if score < 40

**Score bands:**
| Band | Score | Meaning |
|---|---|---|
| Strong Alignment | 75–100 | Unfair advantage. Iterate fast. |
| Promising but Fragmented | 40–74 | Missing a pillar. Fill the gap before scaling. |
| Pre-PMF / High Risk | < 40 | Fundamental mismatch. Consider pivot. |

**Example prompts:**
```
Audit this idea against my persona:
SMB chargeback-dispute automation — SaaS that files and wins disputes
for merchants approaching Visa VMP thresholds.
Target buyer: SMBs processing $1–10M ARR on Shopify/WooCommerce.
```
```
Is building a healthcare handoff tool a good fit for me?
I'm an ex-ICU nurse, still learning to code.
```

**Requirements:** `persona.json` must exist. The idea must include a target buyer and a rough business model — the skill will ask if either is missing.

---

### 4. `founder-ideation`
**Find proven, revenue-verified startup ideas from TrustMRR that fit your persona — then get a marketing strategy and PRD for the top one.**

The previous skills tell you what fits. This one tells you what to actually build, grounded in real startups that already make money. It fetches live data from TrustMRR (verified MRR, tech stacks, growth, cofounder social profiles), filters to startups in your domain, and adapts the ideas to your specific edge and network. Crucially, it only recommends marketing channels you can actually execute — no "build a personal brand" for founders with 6 months runway and no audience.

**When to use it:**
- "What should I build?"
- "Give me startup ideas"
- "Find me a real idea that fits me"
- "Show me validated ideas"
- "What's next?" (after persona or market recommender)

**What you get:**
- `ideation/trustmrr_raw.json` — raw TrustMRR data for your categories
- `ideation/ideation-report.md` — full report containing:
  - 3 validated idea directions, each with a real TrustMRR comp (named startup + MRR + growth)
  - Your differentiation angle per idea (what you can do that the comp cannot)
  - A persona-filtered marketing strategy (2 channels you can execute + 1 explicitly ruled out)
  - 5 specific next-step research actions
  - A complete MVP PRD for the top-ranked idea

**Example prompts:**
```
I have my persona ready. Give me validated startup ideas using founder-ideation.
```
```
What should I build? Show me real startups in my space and help me find my angle.
```

**Requirements:**
- `persona.json` must exist at `./persona/persona.json`
- `TRUSTMRR_API_KEY` environment variable must be set (see Setup below)

---

## Installation

### 1. Clone or download

```bash
git clone https://github.com/your-repo/2026.11
cd 2026.11
```

### 2. Place skills in Claude Code

The `skills/` directory is already structured for Claude Code's plugin system. Each skill folder contains a `SKILL.md` that Claude Code loads automatically.

If you're installing into an existing Claude Code setup, copy each skill folder into your Claude Code skills directory:

```bash
cp -r skills/founder-persona-interview ~/.claude/plugins/<your-plugin>/skills/
cp -r skills/founder-market-recommender ~/.claude/plugins/<your-plugin>/skills/
cp -r skills/founder-idea-audit ~/.claude/plugins/<your-plugin>/skills/
cp -r skills/founder-ideation ~/.claude/plugins/<your-plugin>/skills/
```

### 3. Set up the TrustMRR API key (for `founder-ideation` only)

Run the setup script:

```bash
python skills/founder-ideation/scripts/setup_env.py
```

This will prompt for your key, validate it against the TrustMRR API, and write it to a `.env` file at the repo root. Get your key at [trustmrr.com/dashboard/api-keys](https://trustmrr.com/dashboard/api-keys).

To load the key in your current shell:

```bash
export TRUSTMRR_API_KEY=tmrr_your_key_here
# or
source .env
```

---

## Usage

### Full chain (recommended for new founders)

```
1. "Profile me as a founder" → runs founder-persona-interview
2. "What markets should I explore?" → runs founder-market-recommender
3. "Audit [specific idea from step 2]" → runs founder-idea-audit
4. "What should I build?" → runs founder-ideation
```

Each skill reads the output of the previous one automatically from default paths. You don't need to pass files between them.

### Drop in mid-chain

Already have a persona? Skip to step 2:
```
I have persona.json at ./persona/. What markets fit me?
```

Already know the market? Skip to step 3:
```
Audit "SMB KYC onboarding tooling" against my persona.
```

Want real startup comps immediately? Skip to step 4:
```
Find me validated startup ideas in fintech using my persona.
```

---

## File layout

```
.
├── research/
│   └── main.md                          # Founder-Market Fit theory (primary source)
├── skills/
│   ├── founder-persona-interview/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   ├── persona-schema.md        # persona.json contract (v1.0)
│   │   │   ├── credibility-theater-detection.md
│   │   │   ├── archetype-probes.md
│   │   │   ├── edge-interview-playbook.md
│   │   │   └── network-mapping-playbook.md
│   │   └── assets/
│   │       └── persona-template.md
│   ├── founder-market-recommender/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── archetype-to-market-dynamics.md
│   │       ├── business-model-alignment.md
│   │       ├── entrenchment-heuristics.md
│   │       ├── hallucination-guardrails.md
│   │       └── persona-grounding-protocol.md
│   ├── founder-idea-audit/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   ├── scorecard-weighting.md
│   │   │   ├── four-pillars-stress-tests.md
│   │   │   ├── red-flags-catalogue.md
│   │   │   ├── credibility-theater-crosscheck.md
│   │   │   └── idea-maze-probe.md
│   │   └── assets/
│   │       └── audit-report-template.md
│   └── founder-ideation/
│       ├── SKILL.md
│       ├── scripts/
│       │   ├── fetch_ideas.py           # TrustMRR API client
│       │   └── setup_env.py             # API key setup + validation
│       ├── references/
│       │   ├── marketing-channel-matrix.md
│       │   └── prd-template.md
│       └── assets/
│           └── ideation-report-template.md
├── evals/
│   ├── founder-persona-interview/evals.json
│   ├── founder-market-recommender/evals.json
│   └── founder-idea-audit/evals.json
└── scripts/
    ├── grade_personas.py
    └── grade_recommendations.py
```

---

## Running evals

Each skill has a grading script that scores outputs against structured assertions:

```bash
python scripts/grade_personas.py
python scripts/grade_recommendations.py
```

Grading reads from `evals/<skill>/evals.json` and writes `grading.json` + `benchmark.json` into each workspace directory. See `CLAUDE.md` for the full eval output structure.

---

## Troubleshooting

### "I don't see a persona at ./persona/persona.json"
The skill can't find your persona file. Either run `founder-persona-interview` first, or pass the path explicitly:
```
Run founder-idea-audit with --persona path/to/my/persona.json
```

### "TRUSTMRR_API_KEY is not set" (founder-ideation)
Run the setup script: `python skills/founder-ideation/scripts/setup_env.py`
Or set it directly: `export TRUSTMRR_API_KEY=tmrr_your_key`

### TrustMRR returns no results for my categories
The fetch script infers categories from your persona's market edge, obsession signals, and warm-intro verticals. If your domain is niche (e.g. logistics, IoT), it may fall back to a broad category like `saas`. Check `ideation/trustmrr_raw.json` — the `inferred_categories` field shows what was queried. You can re-run with a manual category override:
```bash
python skills/founder-ideation/scripts/fetch_ideas.py \
  --persona ./persona/persona.json \
  --out ./ideation/trustmrr_raw.json \
  --api-key $TRUSTMRR_API_KEY
```
Then tell Claude: "Use the raw data in `./ideation/trustmrr_raw.json` and focus on the logistics category."

### Idea audit score seems too high / too low
The score is calibrated to the persona — not the idea in isolation. If the score feels off, check:
- Are there credibility flags in `persona.json` that should be capping a pillar?
- Did the idea description include a target buyer and business model? Thin idea descriptions inflate insight scores.
- Is `stage_preference` in the persona set correctly? A scale-stage idea for a 0→1 founder should take a stage-mismatch penalty.

### Skill doesn't trigger
Make sure the SKILL.md is in the correct directory and Claude Code has reloaded its skills list. The trigger description in each SKILL.md frontmatter is the matching mechanism — if you're using unusual phrasing, try the exact phrases listed in the "When to use it" section above.

---

## Domain background

All skills are grounded in `research/main.md`, which synthesises Founder-Market Fit theory from the Entrepreneur First edge framework, Doerr's missionary/mercenary distinction, and the 3H/4H archetype model. The key ideas:

- **Archetypes** (Hustler / Hacker / Hipster / Hound) describe how a founder works
- **Edges** (Technical / Market / Catalyst) describe why they're qualified to win in a domain
- **Credibility theater** — the pattern of founders over-claiming experience — is the main failure mode the skills guard against
- The **1–100 scorecard** weights Experience (25%), Insight (20%), Skill-Edge (20%), Network (15%), Obsession (20%)

Reading `research/main.md` is not required to use the skills, but it explains why every scoring decision is made the way it is.
