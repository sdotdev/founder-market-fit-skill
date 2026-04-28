# CLAUDE.md

This file provides comprehensive guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## What This Repository Is

A **skill development and evaluation framework** for Claude Code plugins that implements a four-skill chain for **Founder-Market Fit (FMF)** assessment. The framework helps founders understand their archetypal makeup, find matching markets, validate specific ideas, and discover proven startup opportunities.

### The Four-Skill Chain

The skills form a pipeline where each skill produces structured outputs that downstream skills consume automatically:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. founder-persona-interview                                │
│    Input: Conversational or written founder background       │
│    Output: persona.json + persona.md                         │
│    Purpose: Profile founder (archetype, edges, network)      │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. founder-market-recommender                               │
│    Input: persona.json                                       │
│    Output: market-recommendations.md                         │
│    Purpose: Identify 3-5 markets that fit this founder      │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. founder-idea-audit                                        │
│    Input: persona.json + specific idea                       │
│    Output: audit-report.md (scored 1-100)                   │
│    Purpose: Validate idea against founder profile            │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 4. founder-ideation                                          │
│    Input: persona.json + TrustMRR API                        │
│    Output: ideation-report.md + MVP PRD                      │
│    Purpose: Find real, revenue-verified startup ideas        │
└─────────────────────────────────────────────────────────────┘
```

Each skill can be used independently or in sequence. Users can drop in mid-chain if they already have persona data.

---

## Repository Structure

```
founder-market-fit-skill/
├── CLAUDE.md                              # This file
├── README.md                              # User-facing skill documentation
├── task-progress.md                       # Work tracking (6 done, 1 in progress, 3 open)
├── .claude/
│   └── settings.local.json                # Local Claude Code configuration
│
├── skills/                                # Skill implementations for Claude Code
│   ├── founder-persona-interview/
│   │   ├── SKILL.md                       # Skill definition + instructions (loaded by Claude Code)
│   │   ├── references/                    # Knowledge files the skill reads
│   │   │   ├── persona-schema.md          # JSON contract for persona.json (v1.0)
│   │   │   ├── credibility-theater-detection.md
│   │   │   ├── archetype-probes.md        # Interview playbook for archetypes
│   │   │   ├── edge-interview-playbook.md # Depth-probe techniques
│   │   │   └── network-mapping-playbook.md
│   │   └── assets/
│   │       └── persona-template.md        # Template for persona.md output
│   │
│   ├── founder-market-recommender/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── archetype-to-market-dynamics.md   # Market class definitions
│   │       ├── business-model-alignment.md       # Revenue model matching
│   │       ├── entrenchment-heuristics.md        # How to avoid bad markets
│   │       ├── hallucination-guardrails.md       # Grounding protocols
│   │       └── persona-grounding-protocol.md     # How to cite persona
│   │
│   ├── founder-idea-audit/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   ├── scorecard-weighting.md     # 1-100 calculation formula
│   │   │   ├── four-pillars-stress-tests.md
│   │   │   ├── red-flags-catalogue.md
│   │   │   ├── credibility-theater-crosscheck.md
│   │   │   └── idea-maze-probe.md
│   │   └── assets/
│   │       └── audit-report-template.md
│   │
│   └── founder-ideation/
│       ├── SKILL.md
│       ├── scripts/
│       │   ├── fetch_ideas.py             # TrustMRR API client
│       │   └── setup_env.py               # API key setup & validation
│       ├── references/
│       │   ├── marketing-channel-matrix.md
│       │   └── prd-template.md            # MVP PRD template
│       └── assets/
│           └── ideation-report-template.md
│
├── research/                              # Founder-Market Fit theory (ground truth)
│   ├── main.md                            # Primary theoretical framework
│   ├── founder-archetypes-frameworks.md
│   ├── founder-market-fit-assessment-frameworks.md
│   └── founder-startup-matching.md
│
├── evals/                                 # Test harness for skill validation
│   ├── founder-persona-interview/
│   │   └── evals.json                     # Assertions for persona skill
│   ├── founder-market-recommender/
│   │   └── evals.json                     # Assertions for market recommender
│   └── founder-idea-audit/
│       └── evals.json                     # Assertions for idea audit
│
├── *-workspace/                           # Eval runs and benchmarking
│   ├── founder-persona-interview-workspace/
│   │   └── iteration-1/                   # Current iteration
│   │       ├── eval-0-<name>/
│   │       │   ├── with_skill/
│   │       │   │   └── run-1/
│   │       │   │       ├── outputs/       # skill outputs (persona.json, persona.md)
│   │       │   │       ├── grading.json   # assertion pass/fail results
│   │       │   │       └── timing.json    # latency data
│   │       │   └── without_skill/         # baseline without Claude Code skill
│   │       │       └── run-1/
│   │       ├── benchmark.json             # Summary across all evals
│   │       └── review.html                # Human-readable eval report
│   │
│   ├── founder-market-recommender-workspace/
│   │   └── iteration-1/
│   │       ├── eval-N-<name>/
│   │       └── benchmark.json
│   │
│   └── founder-idea-audit-workspace/
│       └── iteration-1/
│           ├── eval-N-<name>/
│           └── benchmark.json
│
└── scripts/                               # Python grading + evaluation tools
    ├── grade_personas.py                  # Scores persona.json outputs against evals.json
    └── grade_recommendations.py           # Scores market recommender outputs
```

---

## Key Domain Concepts

All skills are grounded in **`research/main.md`** (Founder-Market Fit theory). Understanding these concepts is essential for developing skills and interpreting outputs.

### Core Taxonomies

**Archetypes** (How a founder works — behavioral orientation):
- **Hustler**: Sales/business development, "Chief Everything Officer," drives revenue and partnerships
- **Hacker**: Product/engineering, compulsive builder, extreme velocity on technical problems
- **Hipster**: UX/branding, creative innovator, focuses on emotional resonance and design
- **Hound**: Data analysis and market discovery, strategic analyst, refines through user signals

In a persona, `archetype_mix` is a weighted object summing to 1.0. Most founders are blends (e.g., 0.4 hustler + 0.35 hacker + 0.25 hipster).

**Edges** (Why they can win in a domain):
- **Technical Edge**: Deep expertise (PhD-level), differentiated skill set, can build at the frontier
- **Market Edge**: 5+ years exposure to a specific industry, knows non-obvious pain points, understands the "idea maze"
- **Catalyst Edge**: Operational excellence, ability to assemble resources and lead through pressure

Each edge has:
- `strength_1_to_10` — self-reported 1-10 strength (but skills depth-probe this)
- `depth_probe_passed` — boolean: did the interview corroborate this claim with evidence?

**Pillar Scores** (Weighted components of founder-market fit):
1. **Experience** (25%) — 5+ years in domain, speaks the language, anticipates edge cases
2. **Insight** (20%) — Owns a "secret truth," understands why past attempts failed
3. **Skill-Edge** (20%) — Differentiated technical/operational capability aligned to the business model
4. **Network** (15%) — Immediate access to first 10-20 customers and top talent
5. **Obsession** (20%) — "Missionary" identity (make meaning) vs "Mercenary" (quick exit); personally depends on outcome

### Key Patterns

**Credibility Theater**: Founders over-claiming experience. The skills detect this by:
- Asking follow-up questions ("Tell me about a time you...")
- Checking for specific examples vs. generic claims
- Flagging unverified claims in `credibility_flags` array in `persona.json`

Downstream skills read these flags to adjust scoring (cap pillars that rely on unverified claims).

**Idea Maze**: Why have past attempts to solve this problem failed? What changed to make it solvable now? A founder with "insight" can articulate this clearly. A founder with "credibility theater" cannot.

**Earned Edge vs. Generic Claims**:
- Earned edge: "I led 3 fintech integrations at Stripe, specifically in chargeback logic. Here's a non-obvious truth about dispute windows..."
- Credibility theater: "I'm technical and have fintech experience."

### The Founder-Market Fit Scorecard

**Calculation**:
```
Overall Score (1-100) = 
  (Experience × 0.25) + 
  (Insight × 0.20) + 
  (Skill-Edge × 0.20) + 
  (Network × 0.15) + 
  (Obsession × 0.20)
```

Each pillar is 1-10; the score ranges 1-100.

**Interpretation**:
- **75-100 (Strong Alignment)**: Unfair advantage. Iterate fast. Founder is likely to reach PMF 23% faster.
- **40-74 (Promising but Fragmented)**: Missing a pillar. Fill the gap with advisors/co-founders before scaling.
- **<40 (Pre-PMF/High Risk)**: Fundamental mismatch. Pivot or restructure team.

### Schema Versions

`persona.json` schema version is **`"1.0"`**. Always check `schema_version` in grading assertions. If the schema changes, increment to `"1.1"`.

---

## Running Skills

### Triggering Skills in Claude Code

Each skill has a `description` field in its `SKILL.md` frontmatter. Claude Code matches user intent against this description to decide which skill to invoke.

**Example triggers**:
- "Profile me as a founder" → `founder-persona-interview`
- "What markets should I explore?" → `founder-market-recommender` (if persona exists)
- "Audit this idea against my persona" → `founder-idea-audit`
- "Find me validated startup ideas" → `founder-ideation`

### Running Skills from Command Line

While these are designed for Claude Code's plugin system, you can test skills manually:

```bash
# Test a skill by reading its SKILL.md
cat skills/founder-persona-interview/SKILL.md

# For founder-ideation, set up the API key first:
export TRUSTMRR_API_KEY=tmrr_your_key_here
python skills/founder-ideation/scripts/setup_env.py
```

---

## Running Evals and Grading

The repository includes a **test harness** that validates skill outputs against a set of assertions.

### Grading Persona Interview Outputs

```bash
python scripts/grade_personas.py
```

This script:
1. Reads assertions from `evals/founder-persona-interview/evals.json`
2. Finds all persona outputs in `founder-persona-interview-workspace/iteration-1/eval-*/with_skill/run-1/outputs/`
3. Runs each persona through the assertions (JSON structure checks, field presence, score ranges)
4. Writes `grading.json` alongside each run
5. Aggregates results into `founder-persona-interview-workspace/iteration-1/benchmark.json`

### Grading Market Recommender Outputs

```bash
python scripts/grade_recommendations.py
```

Similar flow for market recommendations.

### Eval Output Structure

Each eval run produces:
```
eval-N-<name>/
├── with_skill/
│   └── run-1/
│       ├── outputs/
│       │   ├── persona.json              # Skill's main output
│       │   └── persona.md
│       ├── grading.json                  # { summary: { pass_rate, passed, failed, total }, expectations: [...] }
│       └── timing.json                   # { prompt_tokens, completion_tokens, latency_ms }
└── without_skill/                        # Baseline (no Claude Code skill; manual output)
    └── run-1/
        └── outputs/
```

### Benchmark Summary

After grading, a `benchmark.json` file at `<skill>-workspace/iteration-1/` aggregates results:

```json
{
  "skill_name": "founder-persona-interview",
  "iteration": 1,
  "total_evals": 3,
  "with_skill": {
    "pass_rate": 1.0,
    "passed": 9,
    "failed": 0,
    "total": 9
  },
  "without_skill": {
    "pass_rate": 0.36,
    "passed": 3,
    "failed": 5,
    "total": 8
  },
  "improvement": "178%"
}
```

---

## Key Files for Claude Developers

When building new skills or extending existing ones:

### Persona Schema
**File**: `skills/founder-persona-interview/references/persona-schema.md`

This defines the JSON contract that all downstream skills expect. Do not change the schema without updating `schema_version`.

**Critical fields**:
- `schema_version` (string) — must be `"1.0"` or increment if schema changes
- `archetype_primary` (string) — "hustler", "hacker", "hipster", or "hound"
- `archetype_mix` (object) — weights of all four archetypes, must sum to 1.0
- `edges` (object) — `{ technical: {...}, market: {...}, catalyst: {...} }`
- `pillar_scores` (object) — `{ experience, insight, skill_edge, network, obsession }` each 1-10 integers
- `credibility_flags` (array) — `[{ claim, dimension, reason }, ...]`

### Evaluation Assertions
**Files**: `evals/<skill>/evals.json`

Each eval file contains an array of assertions. Example:

```json
{
  "evals": [
    {
      "name": "ex-stripe-pm-fintech-depth",
      "assertions": [
        {
          "type": "field_exists",
          "path": "schema_version",
          "expected": "1.0"
        },
        {
          "type": "range",
          "path": "pillar_scores.experience",
          "min": 8,
          "max": 10,
          "reason": "5+ years Stripe + financial services background"
        },
        {
          "type": "field_equals",
          "path": "credibility_flags",
          "expected": [],
          "reason": "All claims should be corroborated"
        }
      ]
    }
  ]
}
```

### Grading Scripts
**Files**: `scripts/grade_personas.py`, `scripts/grade_recommendations.py`

These Python scripts:
1. Load assertions from `evals/*.json`
2. Find outputs in `*-workspace/iteration-1/eval-*/with_skill/run-1/outputs/`
3. Run assertions (JSON structure validation, field checks, score ranges)
4. Write `grading.json` with pass/fail details
5. Aggregate into `benchmark.json`

When adding a new skill:
- Create `scripts/grade_<skill>.py` following the existing pattern
- Implement assertion logic matching your skill's output schema

---

## Development Workflows

### Adding a New Skill

1. **Create the skill directory and SKILL.md**:
   ```bash
   mkdir -p skills/<skill-name>/references skills/<skill-name>/assets
   cat > skills/<skill-name>/SKILL.md << 'EOF'
   ---
   name: <skill-name>
   description: A clear trigger phrase describing what the skill does
   ---
   # Skill Name
   ## What this skill does
   [Instructions and implementation...]
   EOF
   ```

2. **Create eval assertions**:
   ```bash
   mkdir -p evals/<skill-name>
   cat > evals/<skill-name>/evals.json << 'EOF'
   {
     "evals": [
       {
         "name": "test-case-1",
         "assertions": [...]
       }
     ]
   }
   EOF
   ```

3. **Create workspace directories**:
   ```bash
   mkdir -p <skill-name>-workspace/iteration-1
   ```

4. **Write a grading script**:
   ```bash
   cp scripts/grade_personas.py scripts/grade_<skill-name>.py
   # Modify to match your skill's output schema
   ```

5. **Run the grading script**:
   ```bash
   python scripts/grade_<skill-name>.py
   ```

6. **Review `benchmark.json`**:
   ```bash
   cat <skill-name>-workspace/iteration-1/benchmark.json
   ```

### Iterating on a Skill

1. Update the skill's `SKILL.md` with new instructions
2. Run the skill against test cases (either manually in Claude Code or via the workspace)
3. Run the grading script:
   ```bash
   python scripts/grade_<skill>.py
   ```
4. Review `benchmark.json` to see improvement
5. Commit and push changes

### Debugging Eval Failures

1. Check the specific `grading.json` file for which assertions failed:
   ```bash
   cat <skill>-workspace/iteration-1/eval-N-<name>/with_skill/run-1/grading.json
   ```

2. Compare against the expected assertion in `evals/<skill>/evals.json`

3. If the output is wrong, debug the skill's logic by:
   - Running the skill manually in Claude Code
   - Checking the `outputs/` folder for the actual generated file
   - Updating the skill's instructions based on what went wrong

4. Re-run the grading script to validate the fix

---

## Current Work Status

See `task-progress.md`:

- ✅ Scaffold founder-persona-interview skill
- ✅ Write evals for founder-persona-interview
- ✅ Run + review founder-persona-interview evals
- ⚪ Optimize founder-persona-interview description (skill tuning)
- ✅ Scaffold founder-market-recommender skill
- ✅ Write + run evals for founder-market-recommender
- ⚪ Optimize founder-market-recommender description (skill tuning)
- ✅ Scaffold founder-idea-audit skill
- 🔄 Write + run evals for founder-idea-audit (IN PROGRESS)
- ⚪ Optimize founder-idea-audit description (skill tuning)

---

## Common Patterns and Conventions

### Output File Paths

Skills produce outputs to predictable default paths. Downstream skills read from these:

| Skill | Output | Default Path |
|-------|--------|--------------|
| founder-persona-interview | persona.json | `./persona/persona.json` |
| founder-persona-interview | persona.md | `./persona/persona.md` |
| founder-market-recommender | recommendations | `./recommendations/market-recommendations.md` |
| founder-idea-audit | audit report | `./audit/audit-report.md` |
| founder-ideation | ideation report | `./ideation/ideation-report.md` |
| founder-ideation | PRD | `./ideation/prd.md` |

If a user provides a different path, skills adjust accordingly (they will ask for confirmation).

### Referencing the Persona

When a skill needs to cite persona evidence, it uses this pattern:

```markdown
**Why this fits you**: Your 5+ years at Stripe (Experience: 9/10) combined with 
your expertise in chargeback workflows (Skill-Edge: 9/10) make you uniquely 
positioned to build this. You also have warm intros to Tom DiFranco at LedgerLift 
and Sarah Okwu at Rhombus (Network: 8/10).
```

Always cite:
1. The pillar (Experience, Insight, Network, etc.)
2. The specific persona evidence (not generic claims)
3. The score (e.g., "9/10") to show grounding

### Handling Missing Persona Data

If a skill needs `persona.json` and it doesn't exist, the skill:
1. Checks `./persona/persona.json` first
2. If missing, asks the user to run `founder-persona-interview` first or provide a path

---

## Testing and CI/CD

### Running Tests Locally

```bash
# Grade all persona outputs
python scripts/grade_personas.py

# Grade all market recommender outputs
python scripts/grade_recommendations.py

# Check a specific skill's benchmark
cat founder-persona-interview-workspace/iteration-1/benchmark.json
```

### Expected Benchmarks

Target improvement (with skill vs. without):
- **founder-persona-interview**: 100% → 36% = 178% improvement
- **founder-market-recommender**: TBD (in progress)
- **founder-idea-audit**: TBD (in progress)

If a skill's improvement drops below 50%, it may be time to:
1. Review the skill's instructions (`SKILL.md`)
2. Check if the eval assertions are too strict or misaligned
3. Run a manual test to understand failure modes

---

## Extending the Framework

### Adding a New Evaluation Case

1. Run the skill on a new founder profile (manually in Claude Code)
2. Save outputs to `<skill>-workspace/iteration-1/eval-N-<name>/with_skill/run-1/outputs/`
3. Add assertions to `evals/<skill>/evals.json`:
   ```json
   {
     "name": "new-founder-profile",
     "assertions": [
       {
         "type": "range",
         "path": "pillar_scores.insight",
         "min": 7,
         "max": 10,
         "reason": "This founder has a proven track record in discovery"
       }
     ]
   }
   ```
4. Re-run the grading script and validate

### Modifying the Persona Schema

If you need to add or change fields in `persona.json`:

1. **Update the schema** in `skills/founder-persona-interview/references/persona-schema.md`
2. **Increment the version**: Change `schema_version` from `"1.0"` to `"1.1"`
3. **Update the skill** to populate new fields in `skills/founder-persona-interview/SKILL.md`
4. **Update downstream skills** to read and handle new fields
5. **Update assertions** in all `evals/*/evals.json` files to expect the new version
6. **Re-run grading scripts** to validate

---

## Recommended Reading Order

For a new developer on this project:

1. **Start here**: This file (CLAUDE.md)
2. **User perspective**: `README.md` — understand what each skill does
3. **Theory**: `research/main.md` — read the first few sections to understand archetypes and edges
4. **Skill implementation**: Pick one skill (e.g., `founder-persona-interview`) and read its `SKILL.md`
5. **Evaluation**: Check `evals/founder-persona-interview/evals.json` to see test cases
6. **Grading**: Read `scripts/grade_personas.py` to understand how outputs are validated

---

## Questions or Issues?

- **Skill doesn't trigger?** Check the `description` field in `SKILL.md` frontmatter. Try the exact trigger phrases in the "When to use it" section of the skill.
- **Eval assertions failing?** Check `grading.json` in the eval run directory to see which assertions failed and why.
- **Want to add a skill?** Follow the "Adding a New Skill" section above.
- **Schema questions?** See `skills/founder-persona-interview/references/persona-schema.md`.

---

## Current Context (as of April 28, 2026)

- **Active branch**: `claude/add-claude-documentation-3EeKe`
- **Total tasks**: 10 (6 done, 1 in progress, 3 open)
- **Next priority**: Complete evals for founder-idea-audit, then optimize skill descriptions
- **Theory stability**: `research/main.md` is the ground truth; all skills derive from it
