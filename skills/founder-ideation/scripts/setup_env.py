#!/usr/bin/env python3
"""
Set up the environment for founder-ideation.

Run once before using the skill:
    python skills/founder-ideation/scripts/setup_env.py

What this does:
  - Checks for TRUSTMRR_API_KEY in the current environment
  - If missing, prompts for it and writes it to a .env file at the repo root
  - Optionally validates the key against the TrustMRR API with a lightweight test call
"""

import os
import sys
import urllib.request
import urllib.error
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent  # skills/founder-ideation/scripts/ -> repo root
ENV_FILE = REPO_ROOT / ".env"
TEST_URL = "https://trustmrr.com/api/v1/startups?limit=1&sort=revenue-desc"


def load_existing_env(env_path: Path) -> dict[str, str]:
    if not env_path.exists():
        return {}
    result: dict[str, str] = {}
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, _, v = line.partition("=")
            result[k.strip()] = v.strip().strip('"').strip("'")
    return result


def write_env(env_path: Path, values: dict[str, str]) -> None:
    existing_lines: list[str] = []
    if env_path.exists():
        existing_lines = env_path.read_text(encoding="utf-8").splitlines()

    # Update or append each key
    updated_keys: set[str] = set()
    new_lines: list[str] = []
    for line in existing_lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("#") and "=" in stripped:
            k = stripped.split("=", 1)[0].strip()
            if k in values:
                new_lines.append(f'{k}={values[k]}')
                updated_keys.add(k)
                continue
        new_lines.append(line)

    for k, v in values.items():
        if k not in updated_keys:
            new_lines.append(f"{k}={v}")

    env_path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


def validate_key(api_key: str) -> bool:
    req = urllib.request.Request(
        TEST_URL,
        headers={"Authorization": f"Bearer {api_key}"},
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            return "data" in data
    except urllib.error.HTTPError as e:
        if e.code == 401:
            print("  ✗ API key rejected (401 Unauthorized).")
        else:
            print(f"  ✗ HTTP {e.code} from TrustMRR.")
        return False
    except Exception as e:
        print(f"  ✗ Could not reach TrustMRR: {e}")
        return False


def main() -> None:
    print("=== founder-ideation environment setup ===\n")

    # 1. Check environment variable
    env_key = os.environ.get("TRUSTMRR_API_KEY", "")
    if env_key:
        print(f"✓ TRUSTMRR_API_KEY already set in environment ({env_key[:8]}...).")
        validate_choice = input("  Validate it against the TrustMRR API? [Y/n]: ").strip().lower()
        if validate_choice != "n":
            ok = validate_key(env_key)
            if ok:
                print("  ✓ Key is valid.")
            else:
                print("  Check your key at https://trustmrr.com/dashboard/api-keys")
        print("\nSetup complete. You're ready to use the skill.")
        return

    # 2. Check .env file
    existing = load_existing_env(ENV_FILE)
    file_key = existing.get("TRUSTMRR_API_KEY", "")
    if file_key:
        print(f"✓ TRUSTMRR_API_KEY found in {ENV_FILE} ({file_key[:8]}...).")
        print("  To load it in your shell:\n")
        print(f"    source {ENV_FILE}  (bash/zsh)")
        print(f"    # or: export $(grep -v '^#' {ENV_FILE} | xargs)\n")
        validate_choice = input("  Validate it against the TrustMRR API? [Y/n]: ").strip().lower()
        if validate_choice != "n":
            ok = validate_key(file_key)
            print("  ✓ Key is valid." if ok else "  Check your key at https://trustmrr.com/dashboard/api-keys")
        return

    # 3. Neither set — prompt
    print("TRUSTMRR_API_KEY is not set.")
    print("Get your API key at: https://trustmrr.com/dashboard/api-keys\n")
    api_key = input("Paste your TrustMRR API key: ").strip()
    if not api_key:
        print("No key entered. Exiting.")
        sys.exit(1)

    print("\nValidating key...")
    ok = validate_key(api_key)
    if not ok:
        print("Key validation failed. Double-check at https://trustmrr.com/dashboard/api-keys")
        save_anyway = input("Save it anyway? [y/N]: ").strip().lower()
        if save_anyway != "y":
            sys.exit(1)
    else:
        print("  ✓ Key is valid.")

    write_env(ENV_FILE, {"TRUSTMRR_API_KEY": api_key})
    print(f"\n✓ Key saved to {ENV_FILE}")
    print("\nTo load it in your current shell:")
    print(f"  export TRUSTMRR_API_KEY={api_key[:8]}...  (or source {ENV_FILE})")
    print("\nSetup complete.")


if __name__ == "__main__":
    main()
