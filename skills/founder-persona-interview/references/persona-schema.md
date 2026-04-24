# persona.json schema (v1.0)

This is the structured output that `founder-market-recommender` and `founder-idea-audit` consume. Treat it as a contract — adding fields is fine (downstream skills ignore unknown keys), but never rename or change the meaning of an existing field without bumping `schema_version`.

## Full example

```json
{
  "schema_version": "1.0",
  "founder_name": "Daniela Reyes",
  "interview_date": "2026-04-23",

  "archetype_primary": "hustler",
  "archetype_secondary": "hound",
  "archetype_mix": {
    "hustler": 0.55,
    "hacker": 0.05,
    "hipster": 0.10,
    "hound": 0.30
  },

  "edges": {
    "technical": {
      "claim": "Can read SQL, shipped a Retool internal tool at Stripe, not a production engineer",
      "evidence": ["internal tool at Stripe, ~3 weeks, SQL + Retool"],
      "depth_probe_passed": true,
      "strength_1_to_10": 3
    },
    "market": {
      "claim": "5 years on Stripe's SMB payments team, shipped the Tax product GTM",
      "evidence": [
        "named arcane: chargeback-ratio thresholds for card-network penalty tiers",
        "knows the SMB-to-enterprise handoff friction in payments"
      ],
      "depth_probe_passed": true,
      "strength_1_to_10": 9,
      "entrenchment_risk": false
    },
    "catalyst": {
      "claim": "Ran the Stripe Tax launch team, raised a friends+family round for a prior side project",
      "evidence": ["led 7-person launch team at Stripe", "raised $180k side round"],
      "depth_probe_passed": true,
      "strength_1_to_10": 7
    }
  },

  "network": {
    "communities": [
      { "name": "Stripe alumni Slack", "venue": "online", "embeddedness": "contribute" },
      { "name": "Indie Hackers SMB fintech channel", "venue": "online", "embeddedness": "lurk" },
      { "name": "Money 20/20", "venue": "offline", "embeddedness": "speak" }
    ],
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
    ],
    "insider_markers": [
      "Quoted in Stripe's 2024 SMB report",
      "Co-author on Stripe's internal chargeback-ops playbook",
      "Moderator of Stripe alumni Slack #payments channel"
    ]
  },

  "psychographic": {
    "missionary_score": 6,
    "mercenary_score": 7,
    "evidence": [
      "Wants to reduce SMB churn caused by payment friction — mission framing",
      "But also wants a 5–7 year exit window, not open-ended"
    ]
  },

  "obsession_signals": [
    {
      "signal": "Has been writing a personal substack on SMB chargeback disputes for 9 months",
      "specificity_score": 5
    },
    {
      "signal": "Maintains a spreadsheet tracking every SMB fintech M&A deal since 2022",
      "specificity_score": 5
    }
  ],

  "stage_preference": "0_to_1",
  "stage_evidence": "Led 0→1 launch at Stripe; disliked the 10→100 operating phase of the Tax team after year 2",

  "constraints": {
    "time_per_week_hours": 50,
    "runway_months": 14,
    "geography": "SF Bay Area, open to remote",
    "family": "partner + 1 kid under 5",
    "regulatory": "18-month non-solicit on Stripe customers",
    "other": []
  },

  "pillar_scores": {
    "experience": 9,
    "insight": 7,
    "skill_edge": 6,
    "network": 8,
    "obsession": 8
  },

  "credibility_flags": [
    {
      "claim": "Described self as 'somewhat technical' initially",
      "why_flagged": "Depth-probe revealed Retool-level SQL, not production engineering. Not dishonest, but downstream skills should not treat 'technical' as a build-from-scratch signal.",
      "dimension": "skill_edge"
    }
  ],

  "incomplete_sections": []
}
```

## Field reference

| Field | Type | Required | Notes |
|---|---|---|---|
| `schema_version` | string | yes | Currently `"1.0"`. Bump on breaking changes. |
| `founder_name` | string | yes | For the persona.md header; persona.json can use an alias if founder prefers. |
| `interview_date` | ISO date | yes | Absolute date, not "today". |
| `archetype_primary` | enum | yes | One of `hustler`, `hacker`, `hipster`, `hound`. |
| `archetype_secondary` | enum | optional | Same enum; omit if archetype_primary dominates (>0.7 in mix). |
| `archetype_mix` | object | yes | Keys match the 4 archetypes; values sum to 1.0 ±0.01. |
| `edges.technical` | object | yes | `claim`, `evidence[]`, `depth_probe_passed`, `strength_1_to_10`. |
| `edges.market` | object | yes | Same shape + `entrenchment_risk: bool`. |
| `edges.catalyst` | object | yes | Same shape as technical. |
| `network.communities` | array | yes | Each: `name`, `venue` (`online`/`offline`), `embeddedness` (`speak`/`moderate`/`contribute`/`lurk`). |
| `network.warm_intros` | array | yes | Each: `vertical`, `named_contacts[]` (strings including role), optional `cold_start: bool` if contacts is empty. |
| `network.insider_markers` | string[] | yes | Free-text specific claims; empty array if none. |
| `psychographic` | object | yes | `missionary_score` (1-10), `mercenary_score` (1-10), `evidence[]`. Not mutually exclusive. |
| `obsession_signals` | array | yes | Each: `signal` (string), `specificity_score` (1-5). |
| `stage_preference` | enum | yes | `0_to_1`, `1_to_10`, `scale`, or `mixed` with rationale. |
| `stage_evidence` | string | yes | One-sentence citation. |
| `constraints` | object | yes | See structure above. Unused fields set to null or empty. |
| `pillar_scores` | object | yes | `experience`, `insight`, `skill_edge`, `network`, `obsession` — each 1-10. Feeds the idea-audit scorecard. |
| `credibility_flags` | array | yes | Each: `claim`, `why_flagged`, `dimension` (matches a pillar_scores key). Empty array if none. |
| `incomplete_sections` | string[] | yes | Names of interview sections not covered. Empty if full interview completed. |

## Rules

1. **Every `depth_probe_passed: false` edge must also appear as a `credibility_flag`.** Don't log a failure in one place without the other — downstream skills check consistency.
2. **`pillar_scores` are the interviewer's synthesis, not the founder's self-rating.** They should reconcile with evidence + credibility flags.
3. **`warm_intros.named_contacts` must be real names (with role) or the entry must set `cold_start: true`.** No vague "people I know in X".
4. **Unknowns are explicit.** If a section wasn't covered, list it in `incomplete_sections`. Never guess.
5. **Direct quotes belong in `evidence` arrays,** not in synthesised claim strings.
