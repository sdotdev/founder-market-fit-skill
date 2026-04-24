# Network mapping playbook

This is the section that makes the persona most actionable for downstream skills. `founder-market-recommender` uses it to filter recommendations to markets where the founder has a real first-customer path. `founder-idea-audit` uses it to score the Network pillar (15% weight in the main.md scorecard) and to name specific design partners in the gap-mitigation plan.

Three sub-structures. Run them in this order.

## 1. Communities

Goal: a list of communities the founder is actually embedded in, with an **embeddedness level** that's earned, not claimed.

### Probes

For each community the founder names:

- "What do you do in [community] — just watch, comment sometimes, post/contribute, moderate, or speak?"
- "When's the last time you posted, commented, or spoke there?"
- "Who are 2–3 people in [community] who'd reply to you within 24 hours?"

### Embeddedness levels

| Level | Evidence required |
|---|---|
| `speak` | Has given a talk, been on a panel, run a workshop at community events in the last 18 months. Or: has an admin/moderator role. |
| `moderate` | Admin, moderator, or organiser role. Note: if they speak AND moderate, use `moderate` as it's higher signal. |
| `contribute` | Posts original content regularly (at least monthly). Quoted by others in the community. |
| `lurk` | Member, reads regularly, occasional comment. No original output. |

**Don't accept self-reported levels without evidence.** If they claim `speak`, ask for the specific talk. If they claim `moderate`, ask what they moderated this week. If no evidence surfaces, drop them one level.

### Recording

```json
"communities": [
  { "name": "Stripe alumni Slack", "venue": "online", "embeddedness": "contribute" },
  { "name": "Money 20/20", "venue": "offline", "embeddedness": "speak" }
]
```

**Don't list communities at `lurk` level unless they're the only connection to an otherwise relevant vertical.** A lurk-only presence in a community is weak signal — it's closer to "reads the newsletter" than "has network access".

---

## 2. Warm-intro graph

This is the most important sub-structure. It answers: **for each vertical the founder has touched, who are the 3 people they'd call first to get a paying customer?**

### Probes

For each vertical that came up in the career timeline or edge sections:

> "If you decided tomorrow to build something in [vertical] and needed a paying customer within 60 days, who are the first 3 people you'd reach out to? Full names, current roles."

Follow-ups if needed:

- "Would they take the call? Answer within a week?"
- "Have you kept in touch? When's the last conversation?"
- "Are they decision-makers or champions who'd need to escalate?"

### Pass / partial / fail

| Outcome | Recording |
|---|---|
| 3 named people with current roles, offered without hedging | Full entry, no flag |
| 1–2 named people + vague claim to know more | Record named ones, flag the gap: "partial warm-intro graph for [vertical]" |
| Zero named people, even after probing | `cold_start: true` for this vertical + credibility flag if they claimed network earlier |

**Do not accept:**

- "I have a lot of LinkedIn connections there." (Connections ≠ warm intros.)
- "I used to know people." (Dormant relationships are cold-start.)
- "I can find people." (That's research, not network capital.)

### Multi-vertical coverage

Some founders have deep warm-intro graphs in one vertical and nothing in others. That's normal and important information — it constrains which markets downstream skills should recommend.

Ask about each vertical separately. Don't average. A founder with 3 strong intros in SMB payments and cold-start everywhere else is exactly that shape, and should be recorded as such.

### Recording

```json
"warm_intros": [
  {
    "vertical": "SMB payments",
    "named_contacts": [
      "Priya Nair (head of payments, Earnest)",
      "Tom DiFranco (founder, LedgerLift)",
      "Sarah Okwu (CFO, Rhombus)"
    ]
  },
  {
    "vertical": "embedded finance",
    "named_contacts": [],
    "cold_start": true
  }
]
```

---

## 3. Insider markers

Goal: specific external signals that the founder is recognised inside a space, beyond their own claims.

### What counts

- Quoted in an industry report, newsletter, or article.
- Speaking slot at a non-trivial conference (not their own company's).
- Admin/moderator role in a relevant community.
- Co-author on an industry standard, playbook, or widely-shared internal doc.
- Podcast guest on a vertical-specific show.

### Probes

- "Have you been quoted, cited, or referenced anywhere in the last 2 years in [vertical]?"
- "Have you spoken at a conference, meetup, or podcast about [vertical]?"
- "Is there a document, post, or framework associated with your name in [vertical]?"

### What doesn't count

- "I have 5K followers on LinkedIn." (Following ≠ recognition.)
- "I went to [conference]." (Attending ≠ speaking.)
- "I posted about [topic] on Twitter." (Personal posting ≠ insider marker unless the post itself became a reference.)

### Recording

Free-text list of specific claims, each verifiable:

```json
"insider_markers": [
  "Quoted in Stripe's 2024 SMB report",
  "Co-author on Stripe's internal chargeback-ops playbook",
  "Moderator of Stripe alumni Slack #payments channel"
]
```

If none surface after probing: `"insider_markers": []`. That's fine; not every founder has them, and their absence doesn't indicate low fit — it just means the Network pillar score comes entirely from communities + warm intros.

---

## Synthesis into `pillar_scores.network`

After all three sub-sections, synthesise a 1–10 Network pillar score using this rubric:

| Score | Profile |
|---|---|
| 9–10 | 2+ `speak` or `moderate` communities + 3+ verticals with full warm-intro graphs + 2+ insider markers |
| 7–8 | 1 `speak`/`moderate` + 1–2 verticals with warm intros + 1+ insider markers |
| 5–6 | Mostly `contribute` community level + 1 vertical with warm intros + 0–1 insider markers |
| 3–4 | `contribute` or `lurk` + partial warm intros + no insider markers |
| 1–2 | Only lurk presence + cold-start on every relevant vertical + no markers |

Record the score in `pillar_scores.network` and cite the evidence trail in `persona.md`.

---

## Why this section is non-negotiable

From `main.md`: *"A founder's existing relationships are a proxy for how deeply they are 'embedded' in the market."* And: *"Investors look for earned edge — the kind of insight that manifests in lightning-fast answers..."*

A warm-intro graph is the network equivalent of lightning-fast answers. A founder who can name first-three-people-to-call without hesitation has earned their network claim. A founder who hedges, says "I can find people", or produces LinkedIn metrics has not.

The whole suite's open-ended market recommendation (skill 2) and idea audit (skill 3) depend on this section being **specific rather than claim-based**. Make the founder work for it. They'll thank you later when they can actually execute on the markets skill 2 recommends.
