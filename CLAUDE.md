# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A **skill development and evaluation framework** for Claude Code plugins. Three skills are being iteratively built and benchmarked:

- `founder-persona-interview` — deep founder interview → produces `persona.md` + `persona.json`
- `founder-market-recommender` — takes a persona.json → recommends markets
- `founder-idea-audit` — takes a persona.json + idea → produces a scored FMF audit (1–100 scorecard)

Skills are markdown files consumed by Claude Code's plugin system. Evals test whether skills produce correct structured JSON + narrative outputs against a set of assertions.

## Running evals and grading

Grade persona interview outputs:
```
python scripts/grade_personas.py
```

Grade market recommender outputs:
```
python scripts/grade_recommendations.py
```

Grading scripts read from `evals/<skill>/evals.json`, score outputs in `<skill>-workspace/iteration-N/eval-I-<name>/<with|without_skill>/run-1/outputs/`, and write `grading.json` files alongside each run. A benchmark summary lives at `<skill>-workspace/iteration-N/benchmark.json`.

## Eval output structure

Each eval run produces:
- `outputs/persona.json` (or `recommendations.md`, `audit-report.md` etc.) — the skill's main output
- `grading.json` — `{ summary: { pass_rate, passed, failed, total }, expectations: [...] }`
- `timing.json` — latency data

## Skill file layout

```
skills/<skill-name>/
  SKILL.md              # Loaded by Claude Code; contains description frontmatter + full instructions
  references/           # Reference files the skill reads during execution
  assets/               # Templates the skill uses for output
```

The `description` field in `SKILL.md` frontmatter is the trigger phrase — Claude Code matches user intent against it to decide which skill to invoke.

## Key domain concepts

The skills are grounded in `research/main.md` (Founder-Market Fit theory). Core ideas:
- **Archetypes**: Hustler / Hacker / Hipster / Hound — `archetype_mix` is a weighted object summing to 1.0
- **Edges**: Technical / Market / Catalyst — each has `strength_1_to_10` and `depth_probe_passed`
- **Pillar scores**: experience / insight / skill_edge / network / obsession (1–10 integers) — weighted into a 1–100 scorecard (25/20/20/15/20)
- **Credibility flags**: claims that failed depth-probes; downstream skills read these to adjust scoring
- `persona.json` schema version is `"1.0"` — always check `schema_version` in grading assertions

## Adding a new skill

1. Create `skills/<name>/SKILL.md` with frontmatter `name` + `description`
2. Add `evals/<name>/evals.json` with assertions array
3. Create `<name>-workspace/iteration-1/` eval directory structure
4. Write a grading script in `scripts/grade_<name>.py` mirroring the existing pattern
5. Run the grading script and check `benchmark.json`

## Current work status

See `task-progress.md` for which skills are in what phase (scaffold / evals / optimize description).
