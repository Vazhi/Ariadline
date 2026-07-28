#!/usr/bin/env python3
"""Generate deterministic fictional evaluation dry-run fixtures."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from dry_run_reviewed import EXPECTED_CODES, SEED, build_invalid, build_valid


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="fixtures/evaluation-dry-run/v0.1")
    parser.add_argument("--seed", type=int, default=SEED)
    args = parser.parse_args()
    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)

    valid = build_valid(args.seed)
    invalid = build_invalid(valid)
    invalid["materials"][2]["required_conditions"].append("U")

    (output / "valid_fixture.json").write_text(
        json.dumps(valid, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (output / "invalid_fixture.json").write_text(
        json.dumps(invalid, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (output / "expected_invalid_codes.json").write_text(
        json.dumps(
            {
                "fixture_id": "SLE-EVAL-DRY-RUN-INVALID-0.1",
                "expected_codes": EXPECTED_CODES,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Wrote dry-run fixtures to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
