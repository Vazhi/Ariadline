#!/usr/bin/env python3
"""Generate deterministic fictional evaluation dry-run fixtures."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from dry_run_common import SEED, write_fixtures

EXPECTED_CODES=[
 "FORBIDDEN_IDENTIFIER_FIELD","CANTO_PARTICIPANT_CAP","BROKEN_PARTICIPANT_FK",
 "DUPLICATE_MEANING_EXPOSURE","PROHIBITED_U_CONDITION","MASK_LEAK",
 "REQUIRED_CONDITION_MISSING","NOT_DETERMINED_AS_SUCCESS",
 "PRESERVATION_NOT_CONFIRMED","POST_WITHDRAWAL_TRIAL","BROKEN_TRIAL_FK",
 "CANTO_TRIAL_CAP","UNREGISTERED_TRIAL_CONDITION"
]

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output-dir",default="fixtures/evaluation-dry-run/v0.1")
    p.add_argument("--seed",type=int,default=SEED)
    a=p.parse_args(); out=Path(a.output_dir)
    write_fixtures(out,a.seed)
    (out/"expected_invalid_codes.json").write_text(
      json.dumps({"fixture_id":"SLE-EVAL-DRY-RUN-INVALID-0.1","expected_codes":EXPECTED_CODES},indent=2)+"\n",
      encoding="utf-8")
    print(f"Wrote dry-run fixtures to {out}")
    return 0
if __name__=="__main__": raise SystemExit(main())
