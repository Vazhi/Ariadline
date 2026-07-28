#!/usr/bin/env python3
"""Generate deterministic fictional evaluation dry-run fixtures."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from dry_run_reviewed import EXPECTED_CODES, SEED, write_fixtures


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="fixtures/evaluation-dry-run/v0.1")
    parser.add_argument("--seed", type=int, default=SEED)
    args = parser.parse_args()
    output = Path(args.output_dir)
    write_fixtures(output, args.seed)
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
