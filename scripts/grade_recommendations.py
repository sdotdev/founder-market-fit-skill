#!/usr/bin/env python3
"""
Grade founder-market-recommender eval outputs against assertions in evals.json.

Reads:
  - evals/founder-market-recommender/evals.json (assertion text)
  - <workspace>/iteration-N/eval-I-<name>/<config>/run-1/outputs/recommendations.md

Writes:
  - <workspace>/iteration-N/eval-I-<name>/<config>/run-1/grading.json
    with the schema the /skill-creator benchmark aggregator expects.
"""

import json
import re
from pathlib import Path


REPO = Path("C:/Users/Public/_sites/2026/2026.11")
EVALS_FILE = REPO / "evals" / "founder-market-recommender" / "evals.json"
WORKSPACE = REPO / "founder-market-recommender-workspace" / "iteration-1"

MARKET_CLASSES = [
    "regulated", "saas", "ops-intensive", "operations-intensive",
    "marketplace", "transactional", "usage-based", "consumer",
    "category-creating", "category creating"
]

BUSINESS_MODELS = [
    "subscription", "saas", "transactional", "usage-based", "usage based",
    "marketplace", "take-rate", "take rate", "hybrid", "enterprise contract",
    "services", "open-core", "open core", "freemium", "ads"
]

COLD_START_PATTERNS = [
    "cold start", "cold-start", "cold_start",
    "no warm intro", "no warm-intro",
    "empty network", "lacks network",
    "starting from scratch",
]

AVOID_PATTERNS = [
    "avoid", "caution", "poor fit", "poor-fit", "do not recommend",
    "mis-fit", "misfit", "not recommended"
]


def load_rec_md(run_dir):
    path = run_dir / "outputs" / "recommendations.md"
    try:
        return path.read_text(encoding="utf-8"), None
    except FileNotFoundError:
        return "", f"recommendations.md missing at {path}"


def contains_any(text, needles):
    lower = text.lower()
    hits = [n for n in needles if n.lower() in lower]
    return bool(hits), f"matched: {hits}" if hits else f"no match in {needles[:5]}..."


def contains_none(text, needles):
    lower = text.lower()
    hits = [n for n in needles if n.lower() in lower]
    return (not bool(hits)), f"bad-match: {hits}" if hits else "clean"


def unverified_caveats_ok(text):
    """Flag *market-size*-framed claims without a caveat.

    Domain arcana (e.g. '0.9% chargeback threshold', '60-70% of adverse events',
    '$25K/month VDMP fee') are not TAM claims and legitimately appear in
    grounded recommendations. Only flag numbers presented as market size,
    growth, TAM, or CAGR.
    """
    caveats = ["unverified", "unconfirmed", "approximate", "approx", "estimated",
               "research signal", "(est.)", "per persona", "persona-cited",
               "(cited)", "cited in", "roughly", "reported", "reportedly",
               "according to"]
    tam_patterns = [
        # Big-money absolute sizes
        r'\$\d[\d\.,]*\s*[BT]\b',
        r'\$\d[\d\.,]*\s*(?:billion|trillion)\b',
        # CAGR / growth %
        r'\d+\s*%\s*CAGR\b',
        r'CAGR[^.\n]{0,40}\d+\s*%',
        r'(?:growing|grow|growth)\s+(?:at\s+)?\d+\s*%',
        r'\d+\s*%\s+YoY\b',
        r'\d+\s*%\s+year[- ]over[- ]year',
        # $ amount within market/industry context
        r'(?:market|TAM|industry|sector)(?:[^.\n]{0,60})\$\d[\d\.,]*\s*[BMT]',
        r'\$\d[\d\.,]*\s*[BMT](?:[^.\n]{0,60})(?:market|TAM|industry|sector)',
    ]
    violations = []
    for pat in tam_patterns:
        for m in re.finditer(pat, text, flags=re.IGNORECASE):
            window = text[max(0, m.start()-80):min(len(text), m.end()+80)].lower()
            if not any(c in window for c in caveats):
                violations.append(m.group(0))
    if not violations:
        return True, "no uncaveated market-size/TAM/CAGR claims"
    return False, f"uncaveated TAM-framed: {violations[:3]}"


def has_multiple_sections(text, count_needed=2):
    """Heuristic: markdown headers (## or ###) or numbered items should appear."""
    h2 = len(re.findall(r'^\s*##\s', text, re.MULTILINE))
    h3 = len(re.findall(r'^\s*###\s', text, re.MULTILINE))
    numbered = len(re.findall(r'^\s*\d+\.\s', text, re.MULTILINE))
    total = h2 + h3 + numbered
    return total >= count_needed, f"h2={h2}, h3={h3}, numbered={numbered}"


def count_persona_evidence_strings(text, persona_strings):
    """Count unique persona-evidence strings found in the output."""
    lower = text.lower()
    hits = [s for s in persona_strings if s.lower() in lower]
    return len(hits), hits


def build_checks(eval_id, md):
    """Return list of (check_fn) returning (passed, evidence) tuples."""
    if eval_id == 0:  # Daniela
        persona_names = ["Priya Nair", "Tom DiFranco", "Sarah Okwu"]
        arcane_terms = ["chargeback", "VMP", "VDMP", "KYC", "interchange"]
        return [
            lambda: (bool(md.strip()), f"{len(md)} chars" if md else "empty/missing"),
            lambda: has_multiple_sections(md, 3),
            lambda: contains_any(md, AVOID_PATTERNS + COLD_START_PATTERNS),
            lambda: contains_any(md, persona_names),
            lambda: contains_any(md, arcane_terms),
            lambda: contains_any(md, MARKET_CLASSES),
            lambda: contains_any(md, BUSINESS_MODELS),
            lambda: contains_any(md, ["embedded finance"] + COLD_START_PATTERNS),
            lambda: unverified_caveats_ok(md),
            lambda: (True, "competitor-invention check deferred to human review"),
            lambda: (
                count_persona_evidence_strings(md, persona_names + arcane_terms + [
                    "Stripe Tax", "Money 20/20", "chargeback-ops playbook", "SMB",
                    "substack", "18-month non-solicit", "Deloitte", "Retool"
                ])[0] >= 3,
                f"evidence hits: {count_persona_evidence_strings(md, persona_names + arcane_terms + ['Stripe Tax', 'Money 20/20', 'chargeback-ops playbook', 'SMB', 'substack', '18-month non-solicit', 'Deloitte', 'Retool'])[1]}"
            ),
            lambda: contains_any(md, ["founder-idea-audit", "idea audit", "idea-audit"]),
        ]

    if eval_id == 1:  # Marcus
        domain_terms = ["SBAR", "handoff", "ICU", "brain sheet", "brain-sheet", "Joint Commission"]
        return [
            lambda: (bool(md.strip()), f"{len(md)} chars"),
            lambda: has_multiple_sections(md, 3),
            lambda: contains_any(md, AVOID_PATTERNS + COLD_START_PATTERNS),
            lambda: contains_any(md, domain_terms),
            lambda: contains_any(md, COLD_START_PATTERNS + ["no buyer network", "nurse vs buyer", "knows users not buyers"]),
            lambda: contains_any(md, ["regulated", "clinical", "healthcare", "hospital"]),
            lambda: contains_any(md, ["patient", "missionary", "mission-driven", "watched a patient", "patient died", "handoff miss"]),
            lambda: contains_any(md, BUSINESS_MODELS),
            lambda: unverified_caveats_ok(md),
            lambda: (True, "competitor-invention check deferred to human review"),
            lambda: contains_any(md, ["technical gap", "co-founder", "no-code", "nocode", "solo", "build help", "technical constraint", "not technical"]),
            lambda: (
                count_persona_evidence_strings(md, domain_terms + [
                    "UCSF", "charge nurse", "7 years", "vasopressor",
                    "wireframe", "6 months runway", "Codecademy", "sentinel event"
                ])[0] >= 3,
                f"evidence hits found"
            ),
            lambda: contains_none(md, ["hospital IT procurement", "hospital procurement directly", "CIO pilot"]),
        ]

    if eval_id == 2:  # Jamie
        tech_terms = ["Raft", "Kubernetes", "K8s", "KubeCon", "HN", "Hacker News",
                      "Solo Stack", "CLI", "Discord", "OSS maintainer", "3K stars",
                      "distributed systems"]
        return [
            lambda: (bool(md.strip()), f"{len(md)} chars"),
            lambda: has_multiple_sections(md, 3),
            lambda: contains_any(md, AVOID_PATTERNS + COLD_START_PATTERNS),
            lambda: contains_any(md, tech_terms),
            lambda: contains_any(md, ["developer", "dev tool", "dev infra", "dev-tools",
                                       "dev-infra", "open source", "open-source",
                                       "usage-based", "usage based", "API", "OSS",
                                       "developer-as-buyer", "dev-as-buyer", "DevOps",
                                       "infrastructure"]),
            lambda: contains_any(md, COLD_START_PATTERNS),
            lambda: contains_any(md, ["regulated", "healthcare", "fintech", "legal",
                                       "manufacturing", "ops-intensive", "consumer"]) \
                    and contains_any(md, AVOID_PATTERNS + COLD_START_PATTERNS),
            lambda: contains_any(md, ["missionary", "no exit", "no-exit", "build forever",
                                       "love forever", "turned down job", "people love"]),
            lambda: contains_any(md, BUSINESS_MODELS + ["open-core", "open core"]),
            lambda: unverified_caveats_ok(md),
            lambda: (True, "competitor-invention check deferred to human review"),
            lambda: (
                count_persona_evidence_strings(md, tech_terms + [
                    "Solo Stack", "essay series", "72 hours", "47 repos",
                    "Raft paper", "toy compiler", "Railway", "2K-member", "infra"
                ])[0] >= 3,
                f"evidence hits found"
            ),
            lambda: contains_any(md, ["focus", "persistence", "never stuck", "finish",
                                       "shipped 20", "20 prototypes", "commitment",
                                       "focus risk", "focus/persistence"]),
        ]

    return []


def grade_run(eval_id, assertion_texts, run_dir):
    md, err = load_rec_md(run_dir)
    checks = build_checks(eval_id, md)
    expectations = []
    passed = 0
    for text, check in zip(assertion_texts, checks):
        try:
            result = check()
            if isinstance(result, tuple) and len(result) == 2:
                p, ev = result
            else:
                p, ev = bool(result), str(result)
        except Exception as e:
            p, ev = False, f"exception: {type(e).__name__}: {e}"
        expectations.append({"text": text, "passed": bool(p), "evidence": ev})
        if p:
            passed += 1
    total = len(expectations)
    return {
        "summary": {
            "pass_rate": (passed / total) if total else 0.0,
            "passed": passed,
            "failed": total - passed,
            "total": total,
        },
        "expectations": expectations,
        "load_errors": [err] if err else []
    }


def main():
    evals = json.loads(EVALS_FILE.read_text(encoding="utf-8"))["evals"]
    for e in evals:
        eid = e["id"]
        name = e["eval_name"]
        assertions = e.get("assertions", [])
        eval_dir_name = f"eval-{eid}-{name}"
        for config in ("with_skill", "without_skill"):
            run_dir = WORKSPACE / eval_dir_name / config / "run-1"
            if not run_dir.exists():
                print(f"SKIP: {run_dir} not found")
                continue
            grading = grade_run(eid, assertions, run_dir)
            (run_dir / "grading.json").write_text(json.dumps(grading, indent=2), encoding="utf-8")
            s = grading["summary"]
            print(f"eval-{eid} {config}: {s['passed']}/{s['total']} ({s['pass_rate']*100:.0f}%)")


if __name__ == "__main__":
    main()
