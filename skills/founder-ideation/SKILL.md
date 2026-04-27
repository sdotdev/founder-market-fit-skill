---
name: founder-ideation
description: Generates validated startup ideas grounded in real, revenue-verified startups from TrustMRR, tailored to the founder's persona. Use after founder-persona-interview (and optionally founder-market-recommender) whenever the user asks "what should I build", "give me startup ideas", "find me a real idea that fits me", "ideation", "show me validated ideas", "what startup should I start", or wants to move from persona/market analysis to a concrete buildable direction with real market proof. This skill fetches live market data from TrustMRR, filters by what's actually marketable given the founder's specific network and channels, proposes differentiation angles tailored to their edge, and produces a PRD skeleton for the top idea. Trigger this skill even if the user only vaguely says "now what" or "what's next" after running the persona or market recommender — they almost certainly want ideation.
---

# Founder Ideation

## What this skill does

Takes a founder's `persona.json` and fetches real, revenue-verified startups from TrustMRR to surface:

1. **3 validated idea directions** — each grounded in a real startup as proof the market pays
2. **A differentiation angle per idea** — what this specific founder can do that the comp cannot
3. **A persona-filtered marketing strategy** — only channels the founder can actually execute
4. **Next steps** — 5 specific research actions before writing code
5. **An MVP PRD skeleton** for the top-ranked idea

The key discipline: every output is non-generic. If the same ideation report could apply to a different founder, something is wrong. TrustMRR proves the market exists; the persona determines whether *this founder* can win in it.

## Input contract

- **Primary:** `./persona/persona.json` (produced by `founder-persona-interview`)
- **Optional:** `./market-recommendations.md` (from `founder-market-recommender`) — if it exists, use it to pre-filter which TrustMRR categories to prioritise
- **Required:** `TRUSTMRR_API_KEY` environment variable, or the user provides their key
- **Override:** the user may pass `--persona <path>` to point at a different persona file

**If no persona.json exists:** stop and say — *"I need a founder persona to run ideation. Run `founder-persona-interview` first, or paste your persona.json here."*

**If no API key:** stop and say — *"I need a TrustMRR API key to fetch validated startups. Set `TRUSTMRR_API_KEY` in your environment or pass it with `--api-key <key>`."*

## Step 1: Fetch TrustMRR data

Run the fetch script from the skill's `scripts/` directory:

```bash
python skills/founder-ideation/scripts/fetch_ideas.py \
  --persona ./persona/persona.json \
  --out ./ideation/trustmrr_raw.json
```

If `TRUSTMRR_API_KEY` is not set, add `--api-key <key>`.

The script will:
- Infer 2–4 TrustMRR categories from the persona's archetype, market edge, and obsession signals
- Fetch up to 20 startups per category (list endpoint)
- Fetch full detail (tech stack, cofounders, xFollowerCount) for the top 8 by revenue
- Write `./ideation/trustmrr_raw.json`

Read `trustmrr_raw.json` before proceeding. The `detail_results` array is your primary input.

## Step 2: Score and filter candidates

For each startup in `detail_results`, mentally score it against the persona on three criteria:

**A. Category / domain overlap**
Does the startup's `category` align with the founder's `edges.market`, `obsession_signals`, or warm-intro `vertical`? If there's no overlap at all, skip it — you can always use the `list_summaries` array for a wider fallback.

**B. Tech stack compatibility**
Cross-check `techStack[].slug` against `edges.technical.strength_1_to_10`:
- Score ≤ 3: flag any idea that requires a production engineering skillset (custom ML, infra, complex APIs). Note it as a "requires technical co-founder" constraint.
- Score 4–6: standard SaaS stacks (Next.js, Stripe, Supabase, Retool) are feasible. Custom ML or infra is not.
- Score ≥ 7: no constraint.

**C. Marketing channel feasibility**
Infer how the TrustMRR comp likely acquired customers: if their `xFollowerCount` (or their cofounder's) is high, assume personal brand was a key channel. If category is `developer-tools` and they have OSS markers, assume community/OSS. Then check `references/marketing-channel-matrix.md` to see if that channel is executable by this founder. If not, find the closest viable alternative from the matrix.

Select the **top 3 ideas** that score best across all three criteria. Prioritise ideas where the founder has at least one named warm intro in the vertical and at least one obsession signal with specificity ≥ 3.

## Step 3: Produce the ideation report

Write `./ideation/ideation-report.md` using `assets/ideation-report-template.md` as the scaffold.

**Fill every section.** Do not use placeholder text in the final output. Specifically:

- **Proof of demand**: name the actual TrustMRR startup, its MRR (convert from cents: divide by 100), customer count, and growth. Include the website URL.
- **Differentiation angle**: this should be the hardest-to-write section. What can *this founder specifically* do that the TrustMRR comp cannot? Their 9/10 Market Edge, their insider community, their warm intro graph, their non-obvious domain knowledge. If you can't name a specific differentiator, choose a different idea.
- **Marketing strategy**: read `references/marketing-channel-matrix.md` before writing this. Name the 2 channels the founder can execute and explicitly name the channel(s) they cannot. Do not recommend "build a Twitter following" to a founder with no audience and 6 months runway.
- **FMF alignment table**: fill with real pillar scores from `persona.pillar_scores`, cited against actual persona evidence — not generic phrases.
- **Next steps**: make these specific enough that the founder can take them tomorrow. Name the person to call, the artefact to produce, the question to answer.

## Step 4: Write the MVP PRD

For the top-ranked idea, fill in a complete PRD using `references/prd-template.md` as the skeleton. Append it to `ideation-report.md` under the "MVP PRD" section.

Key constraints when writing the PRD:
- The "Technical constraints" section must reflect the founder's actual technical edge score — don't suggest a full custom ML pipeline to a Retool-level founder
- The "First 30-day build plan" must name actual people from `network.warm_intros` for the discovery call step
- The "Key metrics" must be measurable within 90 days, not lagging indicators like "annual revenue"

## Step 5: Tell the founder

After writing the files:

1. Tell them where the report lives: `./ideation/ideation-report.md`
2. Name the top-ranked idea and in one sentence why it ranks first
3. Name the single most important next step (usually: the first warm intro call)
4. Tell them: if they want to pressure-test a specific idea, run `founder-idea-audit` next — it applies the full 1–100 FMF scorecard against the idea and this persona

## Grounding rules

Every idea recommendation must be traceable to:
- A real TrustMRR startup (by name and MRR) proving demand
- A specific persona field (edge, obsession signal, warm intro, or community) justifying fit

If TrustMRR returns no results in a relevant category, say so explicitly and note which categories had empty results. Do not fabricate startup examples. Use the `list_summaries` fallback (lower-revenue but broader) before inventing.
