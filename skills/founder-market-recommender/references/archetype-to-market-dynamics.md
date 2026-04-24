# Archetype → market dynamics reasoning

From `main.md` §Strategic Matching. This is **reasoning, not a menu** — use it to justify why a specific market's dynamics fit the persona, not as a drop-down you pick from.

## The six market-dynamic classes

Each market tends to dominate in one of these patterns. Identify which class a candidate market falls into, then check archetype fit.

### 1. Regulated / High-compliance
**Examples:** healthcare (clinical SaaS, RCM, payer tech), fintech (payments, lending, insurance), legaltech, defence, govtech.

**Market reality:** the primary barrier is not technology but compliance and institutional trust. Long procurement cycles (6–18 months). Buyers are risk-averse and demand references. Regulations change and reward founders who can navigate them.

**From main.md:** *"In healthcare and biotech, approximately 80% of successful founding CEOs have direct relevant experience, as they must navigate complex regulations and long procurement cycles that outsiders often underestimate."*

**Best founder fit:** strong Market Edge (5–8 years domain, not 10+ which triggers entrenchment) + established network (warm intros to buyers + insider markers) + Hustler or Catalyst archetype to navigate sales cycles. Hacker-only founders typically struggle here without a Market-Edge co-founder.

### 2. Pure B2B SaaS / developer tools / dev-adjacent AI
**Examples:** vertical SaaS that's not heavily regulated, dev infra, AI-native apps for generic workflows.

**Market reality:** switching costs are low, product velocity matters, demos win. "Magic" moments in the product drive adoption. Short sales cycles at the bottom of the market; enterprise at the top. PLG works.

**Best founder fit:** Hacker-heavy or Hacker-Hipster mix. Product-Led founders do well. Market Edge helps but isn't prerequisite if the product is strong. Obsession signals around dev/product experience matter more than domain depth.

### 3. Operations-intensive / logistics / marketplaces
**Examples:** B2B marketplaces (construction, trucking, wholesale), field services, logistics orchestration, supply-chain coordination.

**Market reality:** two-sided liquidity problems. Fragmented buyers and sellers. Operational complexity. Sales is strategic, consultative, interwoven with product and ops. Must achieve "liquidity thresholds" before network effects kick in.

**Best founder fit:** Hustler-heavy (execution stamina) or Catalyst-heavy (coordination). Hacker-only founders tend to underestimate operational complexity. Market Edge useful. Missionary psychographic helps since liquidity takes years.

### 4. Transactional / consumer / e-commerce
**Examples:** D2C, consumer subscription, payment-rails startups with end-user distribution, creator tools.

**Market reality:** high-volume, low-margin, marketing-driven. Acquisition cost and conversion matter more than complex workflows.

**Best founder fit:** Hustler or Hipster-heavy. Strong design/brand instincts help. Mercenary psychographic can fit if the opportunity is time-sensitive. Network matters less than creative distribution.

### 5. Usage-based / consumption infrastructure
**Examples:** cloud infra, dev tools billed by usage, API-first products, data platforms.

**Market reality:** value aligned directly to consumption. Buyers are technical. Unit economics depend on compute/storage/API cost. Often a developer-marketing dynamic — the buyer is the end-user.

**Best founder fit:** Technical-Edge founders with differentiated expertise. Hacker-Hound mix. Developer-community insider markers matter. This is the one class where a strong Technical Edge alone can carry the founder, provided there's a dev-community network.

### 6. Category-creating / frontier / deeply non-obvious
**Examples:** new computing paradigms (quantum, privacy tech), novel healthcare modalities (gene therapy platforms, psychedelic-assisted therapy), climate tech with regulatory creation.

**Market reality:** no existing market to sell into. Founders help define the space. Long timelines (7–10+ years). Investor education is part of GTM.

**Best founder fit:** strong Technical Edge or strong Market Edge + Missionary psychographic. Mercenary founders rarely survive the timeline. Catalyst edge helps. Obsession signals must be genuinely deep — this is where `specificity_score: 5` obsession evidence is table stakes.

## Reading the persona's archetype mix

Don't match on `archetype_primary` alone. Read `archetype_mix` as a vector:

- **Balanced mix (no axis >0.4):** well-rounded founder; most classes fit, but none stand out. Look for decisive signal in Edges and Network to pick among classes.
- **Dominant Hustler (>0.45):** regulated, ops-intensive, transactional work well. SaaS can work if paired with strong obsession. Pure usage-based often struggles.
- **Dominant Hacker (>0.45):** pure SaaS, usage-based, dev-adjacent AI, frontier tech. Regulated and ops-intensive are risky without a Hustler or Catalyst co-founder — call this out.
- **Dominant Hipster (>0.45):** consumer, creator tools, taste-driven prosumer, design-heavy B2B. Regulated and ops-intensive are mis-fit.
- **Dominant Hound (>0.45):** any market where data/interpretation is the wedge. Pairs naturally with regulated (the data-driven disruptor) or with usage-based (analytics platforms).

## Cross-check: Edges should match class

- Regulated: Market Edge ≥7 required. Technical Edge optional if there's a co-founder plan.
- Pure SaaS: Technical Edge ≥6 OR Hipster archetype + product taste.
- Ops-intensive: Catalyst Edge ≥6 OR proven Hustler track record.
- Transactional: Hipster or Hustler + at least some distribution signal (communities at `speak`/`moderate` level).
- Usage-based: Technical Edge ≥8 + dev-community insider markers.
- Category-creating: Technical Edge ≥8 OR Market Edge ≥9 + Missionary ≥8 + specificity-5 obsession.

If a persona fails the cross-check for a class, **don't recommend markets in that class** — or, if you do, flag the mis-fit explicitly.

## What this file is NOT

- Not a drop-down menu. You can recommend markets that don't neatly fit one class; just name the class or mix.
- Not a hard gate. Edge cases exist; the research is a pattern, not a law.
- Not a replacement for the founder's judgment. Recommend, justify, leave the choice.
