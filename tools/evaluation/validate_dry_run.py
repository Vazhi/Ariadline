#!/usr/bin/env python3
"""Validate fictional evaluation dry-run fixtures."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from dry_run_common import validate

def main():
    p=argparse.ArgumentParser()
    p.add_argument("fixture")
    p.add_argument("--expect-codes")
    p.add_argument("--json",action="store_true")
    a=p.parse_args()
    path=Path(a.fixture); findings=validate(json.loads(path.read_text(encoding="utf-8")))
    codes=sorted({f.code for f in findings}); expected=None
    if a.expect_codes:
        expected=set(json.loads(Path(a.expect_codes).read_text(encoding="utf-8")).get("expected_codes",[]))
    result={"fixture":str(path),"finding_count":len(findings),"codes":codes,
      "findings":[f.as_dict() for f in findings],
      "expected_codes":sorted(expected) if expected is not None else None,
      "missing_expected_codes":sorted(expected-set(codes)) if expected is not None else [],
      "unexpected_codes":sorted(set(codes)-expected) if expected is not None else [],
      "valid":not findings}
    if a.json: print(json.dumps(result,indent=2))
    else:
        print(f"{'PASS' if result['valid'] else 'FAIL'}: {path} ({len(findings)} finding(s))")
        for f in findings: print(f"- {f.code}: {f.message}{' ['+f.record+']' if f.record else ''}")
        if expected is not None:
            print(f"Expected-code coverage: {len(expected&set(codes))}/{len(expected)}")
            if result["missing_expected_codes"]: print("Missing expected codes:",", ".join(result["missing_expected_codes"]))
            if result["unexpected_codes"]: print("Unexpected codes:",", ".join(result["unexpected_codes"]))
    return (0 if not result["missing_expected_codes"] else 2) if expected is not None else (0 if result["valid"] else 1)
if __name__=="__main__": raise SystemExit(main())
