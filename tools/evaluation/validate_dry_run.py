#!/usr/bin/env python3
"""Validate fictional evaluation dry-run fixtures."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from dry_run_reviewed import validate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture")
    parser.add_argument("--expect-codes")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    path = Path(args.fixture)
    findings = validate(json.loads(path.read_text(encoding="utf-8")))
    codes = sorted({finding.code for finding in findings})
    expected = None
    if args.expect_codes:
        expected = set(
            json.loads(Path(args.expect_codes).read_text(encoding="utf-8")).get(
                "expected_codes", []
            )
        )

    result = {
        "fixture": str(path),
        "finding_count": len(findings),
        "codes": codes,
        "findings": [finding.as_dict() for finding in findings],
        "expected_codes": sorted(expected) if expected is not None else None,
        "missing_expected_codes": sorted(expected - set(codes)) if expected is not None else [],
        "unexpected_codes": sorted(set(codes) - expected) if expected is not None else [],
        "valid": not findings,
    }

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(
            f"{'PASS' if result['valid'] else 'FAIL'}: {path} "
            f"({len(findings)} finding(s))"
        )
        for finding in findings:
            suffix = f" [{finding.record}]" if finding.record else ""
            print(f"- {finding.code}: {finding.message}{suffix}")
        if expected is not None:
            print(f"Expected-code coverage: {len(expected & set(codes))}/{len(expected)}")
            if result["missing_expected_codes"]:
                print("Missing expected codes:", ", ".join(result["missing_expected_codes"]))
            if result["unexpected_codes"]:
                print("Unexpected codes:", ", ".join(result["unexpected_codes"]))

    if expected is not None:
        return 0 if not result["missing_expected_codes"] and not result["unexpected_codes"] else 2
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
