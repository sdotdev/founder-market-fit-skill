#!/usr/bin/env python3
"""
Grade persona-skill eval outputs against assertions in evals.json.

Reads:
  - evals/founder-persona-interview/evals.json (assertion text)
  - <workspace>/iteration-N/eval-I-<name>/<config>/run-1/outputs/persona.{json,md}

Writes:
  - <workspace>/iteration-N/eval-I-<name>/<config>/run-1/grading.json
    with the schema the /skill-creator benchmark aggregator expects:
    { "summary": { "pass_rate", "passed", "failed", "total" },
      "expectations": [ { "text", "passed", "evidence" } ] }
"""

import json
import sys
from pathlib import Path


REPO = Path("C:/Users/Public/_sites/2026/2026.11")
EVALS_FILE = REPO / "evals" / "founder-persona-interview" / "evals.json"
WORKSPACE = REPO / "founder-persona-interview-workspace" / "iteration-1"


def load_persona(run_dir: Path):
    """Return (persona_json_dict, persona_md_text, load_errors)."""
    pj_path = run_dir / "outputs" / "persona.json"
    pm_path = run_dir / "outputs" / "persona.md"
    errors = []
    pj = None
    pm = ""
    try:
        pj = json.loads(pj_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"persona.json missing at {pj_path}")
    except json.JSONDecodeError as e:
        errors.append(f"persona.json invalid: {e}")
    try:
        pm = pm_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        errors.append(f"persona.md missing at {pm_path}")
    return pj, pm, errors


def has_keys(d, keys):
    if not isinstance(d, dict):
        return False
    return all(k in d for k in keys)


def get(d, *path, default=None):
    cur = d
    for p in path:
        if not isinstance(cur, dict) or p not in cur:
            return default
        cur = cur[p]
    return cur


def archetype_mix_valid(pj):
    mix = get(pj, "archetype_mix")
    if not isinstance(mix, dict):
        return False, "archetype_mix missing or not dict"
    required = {"hustler", "hacker", "hipster", "hound"}
    if set(mix.keys()) != required:
        return False, f"archetype_mix keys {set(mix.keys())} != {required}"
    try:
        total = sum(float(v) for v in mix.values())
    except (TypeError, ValueError):
        return False, "archetype_mix contains non-numeric values"
    if abs(total - 1.0) > 0.05:
        return False, f"archetype_mix sums to {total:.3f}, not ~1.0"
    return True, f"keys valid, sum={total:.3f}"


def pillar_scores_valid(pj):
    ps = get(pj, "pillar_scores")
    required = {"experience", "insight", "skill_edge", "network", "obsession"}
    if not isinstance(ps, dict) or set(ps.keys()) != required:
        return False, f"pillar_scores keys: {set(ps.keys()) if isinstance(ps, dict) else 'missing'}"
    for k, v in ps.items():
        if not isinstance(v, (int, float)) or not (1 <= v <= 10):
            return False, f"{k}={v} out of 1-10"
    return True, f"all pillars in 1-10: {ps}"


def any_warm_intro_has_cold_start(pj):
    for w in get(pj, "network", "warm_intros", default=[]) or []:
        if isinstance(w, dict) and w.get("cold_start") is True:
            return True, f"cold_start vertical: {w.get('vertical', '?')}"
    return False, "no cold_start entry"


def all_warm_intros_cold_or_empty(pj):
    wi = get(pj, "network", "warm_intros", default=[]) or []
    if not wi:
        return True, "warm_intros list is empty"
    for w in wi:
        if isinstance(w, dict) and not w.get("cold_start"):
            names = w.get("named_contacts") or []
            if names:
                return False, f"vertical '{w.get('vertical','?')}' has named contacts: {names}"
    return True, "all verticals marked cold_start or have no named contacts"


def credibility_flag_with_dim(pj, dims):
    flags = get(pj, "credibility_flags", default=[]) or []
    for f in flags:
        if isinstance(f, dict) and f.get("dimension") in dims:
            return True, f"flag dim={f['dimension']}: {f.get('claim', '')[:80]}"
    return False, f"no flag with dimension in {dims}"


def md_contains_any(pm, needles):
    hits = [n for n in needles if n.lower() in pm.lower()]
    return bool(hits), f"matched: {hits}" if hits else f"none of {needles} present"


def md_contains_none(pm, needles):
    hits = [n for n in needles if n.lower() in pm.lower()]
    return not bool(hits), f"matched (bad): {hits}" if hits else "none present (good)"


def warm_intro_has_names(pj, needed_names):
    wi = get(pj, "network", "warm_intros", default=[]) or []
    for w in wi:
        contacts = w.get("named_contacts") or []
        blob = " | ".join(str(c) for c in contacts).lower()
        if all(name.lower() in blob for name in needed_names):
            return True, f"vertical '{w.get('vertical','?')}' contains all of {needed_names}"
    return False, f"no vertical contains all of {needed_names}"


def obsession_signals_with_score(pj, min_score, min_count=1):
    signals = get(pj, "obsession_signals", default=[]) or []
    matching = [s for s in signals if isinstance(s, dict) and (s.get("specificity_score") or 0) >= min_score]
    return len(matching) >= min_count, f"{len(matching)} of {len(signals)} signals meet specificity>={min_score}"


def insider_markers_mention(pj, needles):
    markers = get(pj, "network", "insider_markers", default=[]) or []
    blob = " | ".join(str(m) for m in markers).lower()
    hits = [n for n in needles if n.lower() in blob]
    return bool(hits), f"markers hit: {hits}" if hits else f"markers {markers} do not mention {needles}"


def community_has_embed(pj, levels):
    comms = get(pj, "network", "communities", default=[]) or []
    for c in comms:
        if isinstance(c, dict) and c.get("embeddedness") in levels:
            return True, f"community {c.get('name','?')} @ {c['embeddedness']}"
    return False, f"no community at embeddedness in {levels}"


# Per-eval assertion check tables. Index matches evals.json assertion order.
# Each entry is a zero-arg lambda returning (passed: bool, evidence: str).

def build_checks(eval_id, pj, pm):
    if pj is None:
        pj = {}

    REQUIRED_TOP_KEYS = [
        "archetype_primary", "archetype_mix", "edges", "network",
        "psychographic", "obsession_signals", "stage_preference",
        "constraints", "pillar_scores", "credibility_flags"
    ]

    common = [
        # 0 persona.json exists and is valid JSON
        lambda: (bool(pj), "persona.json loaded" if pj else "persona.json missing/invalid"),
        # 1 persona.md exists
        lambda: (bool(pm), f"persona.md {'loaded' if pm else 'missing'} ({len(pm)} chars)"),
        # 2 schema_version 1.0
        lambda: (get(pj, "schema_version") == "1.0",
                 f"schema_version={get(pj, 'schema_version')}"),
        # 3 required top-level keys
        lambda: (has_keys(pj, REQUIRED_TOP_KEYS),
                 f"missing keys: {[k for k in REQUIRED_TOP_KEYS if k not in pj]}"
                 if not has_keys(pj, REQUIRED_TOP_KEYS) else "all required keys present"),
        # 4 archetype_mix valid
        archetype_mix_valid.__get__(pj, pj) if False else (lambda: archetype_mix_valid(pj)),
        # 5 pillar_scores valid
        (lambda: pillar_scores_valid(pj)),
    ]

    if eval_id == 0:  # Daniela
        return common + [
            lambda: ((get(pj, "edges", "market", "strength_1_to_10") or 0) >= 8,
                     f"market_strength={get(pj, 'edges', 'market', 'strength_1_to_10')}"),
            lambda: (get(pj, "edges", "market", "depth_probe_passed") is True,
                     f"depth_probe_passed={get(pj, 'edges', 'market', 'depth_probe_passed')}"),
            lambda: ((get(pj, "edges", "technical", "strength_1_to_10") or 0) <= 4,
                     f"technical_strength={get(pj, 'edges', 'technical', 'strength_1_to_10')}"),
            lambda: (get(pj, "archetype_primary") in ("hustler", "hound"),
                     f"archetype_primary={get(pj, 'archetype_primary')}"),
            lambda: warm_intro_has_names(pj, ["Priya Nair", "Tom DiFranco", "Sarah Okwu"]),
            lambda: any_warm_intro_has_cold_start(pj),
            lambda: (
                len(get(pj, "network", "insider_markers", default=[]) or []) >= 2
                and insider_markers_mention(pj, ["Money 20/20", "Stripe"])[0],
                f"markers={get(pj, 'network', 'insider_markers', default=[])}"
            ),
            lambda: obsession_signals_with_score(pj, 4, 2),
            lambda: (get(pj, "stage_preference") == "0_to_1",
                     f"stage_preference={get(pj, 'stage_preference')}"),
            lambda: (
                (get(pj, "pillar_scores", "experience") or 0) >= 8
                and (get(pj, "pillar_scores", "network") or 0) >= 7,
                f"experience={get(pj, 'pillar_scores', 'experience')}, network={get(pj, 'pillar_scores', 'network')}"
            ),
            lambda: (
                len(get(pj, "credibility_flags", default=[]) or []) <= 2,
                f"flag_count={len(get(pj, 'credibility_flags', default=[]) or [])}"
            ),
            lambda: md_contains_any(pm, ["Priya Nair", "Tom DiFranco", "Sarah Okwu"]),
            lambda: md_contains_any(pm, ["chargeback", "Visa", "KYC", "interchange"]),
        ]

    if eval_id == 1:  # Marcus
        return common + [
            lambda: ((get(pj, "edges", "market", "strength_1_to_10") or 0) >= 7,
                     f"market_strength={get(pj, 'edges', 'market', 'strength_1_to_10')}"),
            lambda: (get(pj, "edges", "market", "depth_probe_passed") is True,
                     f"depth_probe_passed={get(pj, 'edges', 'market', 'depth_probe_passed')}"),
            lambda: ((get(pj, "edges", "technical", "strength_1_to_10") or 0) <= 2,
                     f"technical_strength={get(pj, 'edges', 'technical', 'strength_1_to_10')}"),
            lambda: (get(pj, "edges", "technical", "depth_probe_passed") is False,
                     f"technical depth_probe_passed={get(pj, 'edges', 'technical', 'depth_probe_passed')}"),
            lambda: (get(pj, "archetype_primary") in ("hustler", "hound"),
                     f"archetype_primary={get(pj, 'archetype_primary')}"),
            lambda: any_warm_intro_has_cold_start(pj),
            lambda: (
                len(get(pj, "network", "insider_markers", default=[]) or []) <= 1,
                f"markers={get(pj, 'network', 'insider_markers', default=[])}"
            ),
            lambda: ((get(pj, "psychographic", "missionary_score") or 0) >= 8,
                     f"missionary={get(pj, 'psychographic', 'missionary_score')}"),
            lambda: ((get(pj, "psychographic", "mercenary_score") or 10) <= 4,
                     f"mercenary={get(pj, 'psychographic', 'mercenary_score')}"),
            lambda: obsession_signals_with_score(pj, 4, 1),
            lambda: ((get(pj, "pillar_scores", "experience") or 0) >= 7,
                     f"experience={get(pj, 'pillar_scores', 'experience')}"),
            lambda: ((get(pj, "pillar_scores", "network") or 10) <= 5,
                     f"network_pillar={get(pj, 'pillar_scores', 'network')}"),
            lambda: ((get(pj, "pillar_scores", "skill_edge") or 10) <= 3,
                     f"skill_edge={get(pj, 'pillar_scores', 'skill_edge')}"),
            lambda: (
                len(get(pj, "credibility_flags", default=[]) or []) >= 1,
                f"flag_count={len(get(pj, 'credibility_flags', default=[]) or [])}"
            ),
            lambda: credibility_flag_with_dim(pj, {"skill_edge", "network"}),
            lambda: md_contains_any(pm, ["SBAR", "handoff", "ICU", "vasopressor"]),
            lambda: md_contains_none(pm, ["strong hospital network", "solid hospital network",
                                           "extensive hospital network", "well-connected in hospitals"]),
        ]

    if eval_id == 2:  # Jamie
        return common + [
            lambda: ((get(pj, "edges", "technical", "strength_1_to_10") or 0) >= 8,
                     f"technical_strength={get(pj, 'edges', 'technical', 'strength_1_to_10')}"),
            lambda: (get(pj, "edges", "technical", "depth_probe_passed") is True,
                     f"technical depth_probe_passed={get(pj, 'edges', 'technical', 'depth_probe_passed')}"),
            lambda: ((get(pj, "edges", "market", "strength_1_to_10") or 10) <= 3,
                     f"market_strength={get(pj, 'edges', 'market', 'strength_1_to_10')}"),
            lambda: (get(pj, "edges", "market", "depth_probe_passed") is False,
                     f"market depth_probe_passed={get(pj, 'edges', 'market', 'depth_probe_passed')}"),
            lambda: (get(pj, "archetype_primary") == "hacker",
                     f"archetype_primary={get(pj, 'archetype_primary')}"),
            lambda: ((get(pj, "archetype_mix", "hacker") or 0) >= 0.45,
                     f"hacker_mix={get(pj, 'archetype_mix', 'hacker')}"),
            lambda: all_warm_intros_cold_or_empty(pj),
            lambda: insider_markers_mention(pj, ["KubeCon", "HN", "Hacker News"]),
            lambda: community_has_embed(pj, {"speak", "moderate"}),
            lambda: ((get(pj, "psychographic", "missionary_score") or 0) >= 8,
                     f"missionary={get(pj, 'psychographic', 'missionary_score')}"),
            lambda: ((get(pj, "psychographic", "mercenary_score") or 10) <= 3,
                     f"mercenary={get(pj, 'psychographic', 'mercenary_score')}"),
            lambda: (
                any(
                    isinstance(s, dict)
                    and (s.get("specificity_score") or 0) >= 4
                    and any(kw in (s.get("signal") or "").lower() for kw in ["solo stack", "cli"])
                    for s in (get(pj, "obsession_signals", default=[]) or [])
                ),
                f"signals={get(pj, 'obsession_signals', default=[])}"
            ),
            lambda: (get(pj, "stage_preference") == "0_to_1",
                     f"stage_preference={get(pj, 'stage_preference')}"),
            lambda: ((get(pj, "pillar_scores", "skill_edge") or 0) >= 8,
                     f"skill_edge={get(pj, 'pillar_scores', 'skill_edge')}"),
            lambda: ((get(pj, "pillar_scores", "experience") or 10) <= 4,
                     f"experience={get(pj, 'pillar_scores', 'experience')}"),
            lambda: credibility_flag_with_dim(pj, {"experience", "insight"}),
            lambda: md_contains_any(pm, ["Raft", "Kubernetes", "K8s", "Solo Stack", "HN"]),
        ]

    return common


def grade_run(eval_id, assertion_texts, run_dir):
    pj, pm, errors = load_persona(run_dir)
    checks = build_checks(eval_id, pj, pm)
    expectations = []
    passed_count = 0
    for text, check in zip(assertion_texts, checks):
        try:
            result = check()
            # check() may return (bool, str) — tolerate different arities
            if isinstance(result, tuple) and len(result) == 2:
                p, ev = result
            else:
                p, ev = bool(result), str(result)
        except Exception as e:
            p, ev = False, f"exception: {type(e).__name__}: {e}"
        expectations.append({"text": text, "passed": bool(p), "evidence": ev})
        if p:
            passed_count += 1

    total = len(expectations)
    grading = {
        "summary": {
            "pass_rate": (passed_count / total) if total else 0.0,
            "passed": passed_count,
            "failed": total - passed_count,
            "total": total
        },
        "expectations": expectations,
        "load_errors": errors
    }
    return grading


def main():
    evals = json.loads(EVALS_FILE.read_text(encoding="utf-8"))["evals"]

    for e in evals:
        eid = e["id"]
        eval_dir_name = f"eval-{eid}-{e['eval_name']}"
        assertions = e.get("assertions", [])
        for config in ("with_skill", "without_skill"):
            run_dir = WORKSPACE / eval_dir_name / config / "run-1"
            if not run_dir.exists():
                print(f"SKIP: {run_dir} not found")
                continue
            grading = grade_run(eid, assertions, run_dir)
            (run_dir / "grading.json").write_text(
                json.dumps(grading, indent=2), encoding="utf-8"
            )
            s = grading["summary"]
            print(f"eval-{eid} {config}: {s['passed']}/{s['total']} "
                  f"({s['pass_rate']*100:.0f}%)")


if __name__ == "__main__":
    main()
