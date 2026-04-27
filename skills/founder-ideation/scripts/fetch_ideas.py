#!/usr/bin/env python3
"""
Fetch validated startup ideas from TrustMRR, filtered by the founder's persona.

Usage:
    python fetch_ideas.py --persona <path-to-persona.json> --out <output-path.json>
    python fetch_ideas.py --persona ./persona/persona.json --out ./ideation/trustmrr_raw.json

API key resolution order:
  1. --api-key flag
  2. TRUSTMRR_API_KEY environment variable
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

BASE_URL = "https://trustmrr.com/api/v1"
DETAIL_FETCH_COUNT = 8

# Maps persona archetype + market edge domain keywords to TrustMRR categories
ARCHETYPE_CATEGORY_MAP = {
    "hustler":  ["saas", "fintech", "sales", "marketing", "productivity"],
    "hacker":   ["developer-tools", "ai", "saas", "no-code", "analytics"],
    "hipster":  ["design-tools", "content-creation", "social-media", "no-code", "community"],
    "hound":    ["analytics", "saas", "ai", "fintech", "market"],
}

DOMAIN_KEYWORD_CATEGORY_MAP = {
    "fintech": "fintech",
    "payment": "fintech",
    "health": "health-fitness",
    "medical": "health-fitness",
    "healthcare": "health-fitness",
    "legal": "legal",
    "real estate": "real-estate",
    "ecommerce": "ecommerce",
    "education": "education",
    "security": "security",
    "crypto": "crypto-web3",
    "developer": "developer-tools",
    "devtools": "developer-tools",
    "infrastructure": "developer-tools",
    "marketing": "marketing",
    "sales": "sales",
    "analytics": "analytics",
    "recruiting": "recruiting",
    "travel": "travel",
    "ai": "ai",
}


def get_api_key(args_key: str | None) -> str:
    key = args_key or os.environ.get("TRUSTMRR_API_KEY", "")
    if not key:
        print("ERROR: No API key. Pass --api-key or set TRUSTMRR_API_KEY.", file=sys.stderr)
        sys.exit(1)
    return key


def api_get(path: str, params: dict, api_key: str) -> dict:
    query = "&".join(f"{k}={v}" for k, v in params.items() if v is not None)
    url = f"{BASE_URL}{path}?{query}" if query else f"{BASE_URL}{path}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {api_key}"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"HTTP {e.code} for {url}: {body}", file=sys.stderr)
        return {}
    except Exception as e:
        print(f"Request error for {url}: {e}", file=sys.stderr)
        return {}


def infer_categories(persona: dict) -> list[str]:
    """Derive the most relevant TrustMRR category filters from the persona."""
    categories: list[str] = []

    # Primary archetype → category candidates
    primary = persona.get("archetype_primary", "hustler")
    categories.extend(ARCHETYPE_CATEGORY_MAP.get(primary, []))

    # Market edge claim and obsession signals → domain keywords → categories
    text_corpus = " ".join([
        persona.get("edges", {}).get("market", {}).get("claim", ""),
        " ".join(persona.get("edges", {}).get("market", {}).get("evidence", [])),
        " ".join(s.get("signal", "") for s in persona.get("obsession_signals", [])),
        " ".join(w.get("vertical", "") for w in persona.get("network", {}).get("warm_intros", [])),
    ]).lower()

    for keyword, category in DOMAIN_KEYWORD_CATEGORY_MAP.items():
        if keyword in text_corpus and category not in categories:
            categories.append(category)

    # Deduplicate while preserving order (most-relevant first)
    seen: set[str] = set()
    unique: list[str] = []
    for c in categories:
        if c not in seen:
            seen.add(c)
            unique.append(c)

    return unique[:4]  # Top 4 categories max


def fetch_list(category: str, api_key: str, limit: int = 20) -> list[dict]:
    result = api_get(
        "/startups",
        {"category": category, "sort": "revenue-desc", "limit": limit},
        api_key,
    )
    return result.get("data", [])


def fetch_detail(slug: str, api_key: str) -> dict:
    result = api_get(f"/startups/{slug}", {}, api_key)
    return result.get("data", {})


def deduplicate(startups: list[dict]) -> list[dict]:
    seen: set[str] = set()
    out: list[dict] = []
    for s in startups:
        slug = s.get("slug", "")
        if slug and slug not in seen:
            seen.add(slug)
            out.append(s)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--persona", required=True, help="Path to persona.json")
    parser.add_argument("--out", required=True, help="Output path for trustmrr_raw.json")
    parser.add_argument("--api-key", default=None, help="TrustMRR API key")
    parser.add_argument("--detail-count", type=int, default=DETAIL_FETCH_COUNT,
                        help="How many top startups to fetch full detail for")
    args = parser.parse_args()

    api_key = get_api_key(args.api_key)

    persona_path = Path(args.persona)
    if not persona_path.exists():
        print(f"ERROR: persona.json not found at {persona_path}", file=sys.stderr)
        sys.exit(1)
    persona = json.loads(persona_path.read_text(encoding="utf-8"))

    categories = infer_categories(persona)
    print(f"Inferred categories: {categories}")

    # Phase 1: list fetch across top categories
    all_summaries: list[dict] = []
    for cat in categories:
        print(f"Fetching list: category={cat}")
        summaries = fetch_list(cat, api_key, limit=20)
        all_summaries.extend(summaries)
        time.sleep(0.2)

    all_summaries = deduplicate(all_summaries)
    # Sort by last-30-day revenue descending
    all_summaries.sort(key=lambda s: s.get("revenue", {}).get("last30Days", 0), reverse=True)
    top_summaries = all_summaries[:args.detail_count]

    print(f"Total unique startups from list: {len(all_summaries)}. Fetching detail for top {len(top_summaries)}.")

    # Phase 2: detail fetch for top candidates
    details: list[dict] = []
    for s in top_summaries:
        slug = s.get("slug", "")
        if not slug:
            continue
        print(f"Fetching detail: {slug}")
        detail = fetch_detail(slug, api_key)
        if detail:
            details.append(detail)
        time.sleep(0.2)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps({
            "persona_name": persona.get("founder_name", "unknown"),
            "inferred_categories": categories,
            "list_summaries": all_summaries,
            "detail_results": details,
        }, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote {len(details)} detailed results to {out_path}")


if __name__ == "__main__":
    main()
