# Marketing Channel Matrix

Use this reference to filter which marketing channels are *executable* for a given founder. Never recommend a channel the founder cannot actually run. Each channel lists the hard prerequisites — if the persona doesn't meet them, rule that channel out and explain why.

## Channel reference

### Personal brand / Twitter / X
**Prerequisite:** Existing following (≥ 3,000 followers on X, or a newsletter list, or both).
**Persona signals to check:**
- `network.insider_markers` — speaking slots, quoted-in pieces, published content indicate an existing audience
- `network.communities[].embeddedness = "speak"` — conference speaking implies a real audience
- If the founder has only "contribute" or "lurk" embeddedness and no insider markers mentioning media/press: **rule this out**

**Why it fails without prerequisites:** Building a following from scratch takes 12–18 months of consistent content before it converts to customers. A founder with 6–14 months runway cannot afford that timeline as a primary channel.

---

### SEO / content marketing
**Prerequisite:** ≥ 9 months runway, willingness to produce 10–20 high-quality articles before seeing traction.
**Persona signals to check:**
- `constraints.runway_months >= 9` — minimum threshold
- `stage_preference` — "0_to_1" founders often underestimate content's delayed payoff; note this explicitly
- Works well for Hound/Hipster archetypes who enjoy analysis and writing

**Why it works when it works:** Long-tail SEO builds a defensible moat with no ongoing distribution cost. Best for technical tools (developer-tools, analytics, saas) where buyer research begins on Google.

---

### Community-led growth
**Prerequisite:** The founder is already an active participant (moderator, speaker, or sustained contributor) in a community where their target buyers exist — not just where peers exist.
**Persona signals to check:**
- `network.communities[].embeddedness ∈ {"speak", "moderate"}` — lurking does not count
- The community's `name` must plausibly contain *buyers*, not just fellow founders or developers
- Example: Stripe alumni Slack #payments = relevant buyers. Indie Hackers general = founder peers, not buyers

**Why the buyer/peer distinction matters:** Community-led growth works because trust transfers from the community to the product. If the community is peers, you get feedback, not customers.

---

### Cold outbound (email / LinkedIn)
**Prerequisite:** Clear ICP definition AND at least a few warm reference points to open doors.
**Persona signals to check:**
- `network.warm_intros` with `named_contacts` (not `cold_start: true`) — even 2–3 warm intros in the vertical dramatically improve open rates
- `archetype_mix.hustler >= 0.35` — outbound is a Hustler motion; Hacker/Hipster-primary founders often underinvest in it
- `constraints.time_per_week_hours >= 30` — outbound at meaningful scale takes 10–15 hrs/week minimum

**Notes:** Cold outbound works in B2B where the buyer is identifiable. In regulated markets (fintech, healthtech), warm intro chains are far more effective — cold email to a compliance officer rarely converts. If the persona has warm intros in the vertical, use them as the entry point, then follow up with systematic outbound to adjacent names.

---

### Product Hunt launch
**Prerequisite:** Product has a strong visual/demo story; founder has some existing audience or community to drive Day-1 votes.
**Persona signals to check:**
- `archetype_mix.hipster >= 0.20` — Product Hunt rewards design taste and product storytelling
- `network.communities` with any online community where members would upvote (developer, designer, maker communities)
- Works poorly for regulated/compliance-heavy B2B products — Product Hunt audience skews consumer/prosumer

**When to use it:** One-time spike channel for product launches, not a sustainable acquisition loop. Best combined with a community-led warm-up.

---

### Partnership / BD / referral
**Prerequisite:** Warm intros exist in a vertical where a non-competing product already serves the same buyer.
**Persona signals to check:**
- `network.warm_intros[].named_contacts` not empty and not `cold_start: true` — named contacts are the initial partnership intros
- `edges.catalyst.strength_1_to_10 >= 6` — BD motion requires negotiation and relationship management
- `archetype_mix.hustler >= 0.35` — partnerships are a Hustler-native motion

**Why this works for regulated markets:** In fintech/healthtech, trust is already established between complementary vendors and their mutual buyers. A referral from Stripe alumni into a SMB merchant is worth 10x cold outreach.

---

### Developer / OSS community
**Prerequisite:** Product has a technical layer the developer community finds genuinely useful or interesting.
**Persona signals to check:**
- `edges.technical.strength_1_to_10 >= 6` — founder must be credible in dev community
- `archetype_mix.hacker >= 0.35`
- `network.communities` includes developer communities (GitHub, Discord, HN, dev-specific Slack)
- `network.insider_markers` with conference talks, OSS contributions, or HN front-page posts

**Notes:** This channel is powerful and cheap but only works if the founder *is* the community member — participation can't be faked. Also note: developer adoption ≠ revenue unless the product has a clear upgrade/enterprise path.

---

## Applying this matrix

For each of the 3 idea directions in the ideation report:
1. List all channels the startup's TrustMRR data suggests it used (infer from xFollowerCount, cofounders, category)
2. Cross-check each channel against persona prerequisites above
3. For channels the founder *can* execute: explain why (cite persona evidence)
4. For channels they *cannot*: say so explicitly and suggest the closest viable alternative
5. Recommend at most **2 primary channels** per idea — founders in 0→1 phase cannot run 5 channels simultaneously
