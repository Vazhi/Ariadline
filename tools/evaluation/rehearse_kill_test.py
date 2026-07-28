#!/usr/bin/env python3
"""Validate fictional Ariadline kill-test rehearsal fixtures."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any

ALLOWED_STUDY_STATES={"not_started","synthetic_rehearsal"}
ALLOWED_EVIDENCE_CLAIMS={"procedure_only"}
REQUIRED_HUMAN_GATES={"oversight","permissions","meaning_authority","accessibility","statistics","preregistration","recruitment"}
MATERIAL_SEVERITIES={"critical","major"}

def add(findings, code, path, message):
    findings.append({"code":code,"path":path,"message":message})

def derived_preservation(record:dict[str,Any])->str:
    dims=record.get("dimensions",[])
    for dim in dims:
        if dim.get("result")=="not_preserved" and dim.get("severity") in MATERIAL_SEVERITIES:
            return "not_preserved"
    if any(dim.get("result")=="not_determined" and dim.get("material",False) for dim in dims):
        return "not_determined"
    for dim in dims:
        if dim.get("material",False) and dim.get("result")!="preserved":
            return "not_determined"
        if dim.get("result") in {"minor_difference","editorial_difference"} and not dim.get("confirmed_nonmaterial",False):
            return "not_determined"
    return "preserved"

def validate(data:dict[str,Any]):
    findings=[]
    if data.get("synthetic_only") is not True:
        add(findings,"SYNTHETIC_FLAG_REQUIRED","$.synthetic_only","Rehearsal fixtures must be synthetic-only.")
    if data.get("study_state") not in ALLOWED_STUDY_STATES:
        add(findings,"STUDY_STATE_ADVANCED","$.study_state","A rehearsal cannot advance the human study state.")
    if data.get("evidence_claim") not in ALLOWED_EVIDENCE_CLAIMS:
        add(findings,"HUMAN_EVIDENCE_CLAIMED","$.evidence_claim","Synthetic fixtures may claim procedure validation only.")
    gates=data.get("human_gates",{})
    for gate in sorted(REQUIRED_HUMAN_GATES):
        if gate not in gates:
            add(findings,"HUMAN_GATE_MISSING",f"$.human_gates.{gate}",f"Human gate {gate} is missing.")
    unresolved=[g for g in REQUIRED_HUMAN_GATES if gates.get(g) not in {"approved","not_applicable"}]
    seen=set(); any_ineligible=False; any_unresolved=False
    for i,case in enumerate(data.get("cases",[])):
        pfx=f"$.cases[{i}]"; cid=case.get("case_id")
        if not cid or cid in seen:
            add(findings,"CASE_ID_INVALID",f"{pfx}.case_id","Case IDs must be present and unique.")
        if cid: seen.add(cid)
        p=case.get("conditions",{}).get("P",{}); s=case.get("conditions",{}).get("S",{})
        if p.get("editor_id") and p.get("editor_id")==s.get("editor_id"):
            add(findings,"SAME_EDITOR_SAME_RECORD",f"{pfx}.conditions","One editor cannot produce P and S for the same record.")
        if p.get("shared_packet_hash")!=s.get("shared_packet_hash"):
            add(findings,"SHARED_PACKET_HASH_MISMATCH",f"{pfx}.conditions","P and S must use the same shared packet.")
        if case.get("scorer_packet",{}).get("rule_metadata_absent") is not True:
            add(findings,"SCORER_METADATA_LEAK",f"{pfx}.scorer_packet","Scorer material must exclude restricted metadata.")
        if case.get("scoring_freeze",{}).get("frozen_before_condition_output") is not True:
            add(findings,"SCORING_FREEZE_AFTER_OUTPUT",f"{pfx}.scoring_freeze","Scoring must freeze before condition outputs are examined.")
        preservation=case.get("preservation",{}); eligible={}
        for cond in ("P","S"):
            record=preservation.get(cond,{})
            expected=derived_preservation(record); actual=record.get("overall")
            if actual!=expected:
                add(findings,"PRESERVATION_AGGREGATION_INVALID",f"{pfx}.preservation.{cond}.overall",f"Recorded {actual!r}; derived {expected!r}.")
            if expected=="not_determined": any_unresolved=True
            eligible[cond]=expected=="preserved"
        should=eligible["P"] and eligible["S"] and case.get("comparability")=="comparable"
        recorded=case.get("pair_eligible_for_benefit") is True
        if recorded!=should:
            add(findings,"PAIR_ELIGIBILITY_INVALID",f"{pfx}.pair_eligible_for_benefit","Pair eligibility requires comparable preserved P and S.")
        if not should: any_ineligible=True
        adverse=any(derived_preservation(preservation.get(c,{})) in {"not_preserved","not_determined"} for c in ("P","S"))
        if adverse and case.get("adverse_result_retained") is not True:
            add(findings,"ADVERSE_RESULT_NOT_RETAINED",f"{pfx}.adverse_result_retained","Failed or unresolved preservation must remain visible.")
        if case.get("reader_exposure_allowed") is True and not should:
            add(findings,"READER_EXPOSURE_WITH_INELIGIBLE_PAIR",f"{pfx}.reader_exposure_allowed","An ineligible pair cannot enter reader exposure.")
        if case.get("not_determined_promoted_to_success") is True:
            add(findings,"NOT_DETERMINED_PROMOTED",f"{pfx}.not_determined_promoted_to_success","not determined cannot be promoted to success.")
    launch=data.get("launch",{})
    if launch.get("ready") is True and unresolved:
        add(findings,"LAUNCH_WITH_UNRESOLVED_HUMAN_GATES","$.launch.ready","Launch cannot be ready with unresolved human gates.")
    if launch.get("ready") is True and (any_ineligible or any_unresolved):
        add(findings,"LAUNCH_WITH_INELIGIBLE_RECORDS","$.launch.ready","Launch cannot be ready with failed or unresolved records.")
    if data.get("parent_issue_9_advanced") is True:
        add(findings,"PARENT_STUDY_ADVANCED","$.parent_issue_9_advanced","A rehearsal cannot advance parent issue #9.")
    return sorted(findings,key=lambda x:(x["code"],x["path"],x["message"]))

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("fixture",type=Path); ap.add_argument("--expect-codes",type=Path)
    args=ap.parse_args(); findings=validate(load(args.fixture)); codes=sorted({f["code"] for f in findings})
    if args.expect_codes:
        expected=sorted(load(args.expect_codes)["expected_codes"])
        status="expected_failures_detected" if codes==expected else "self_test_failed"
        print(json.dumps({"status":status,"expected_codes":expected,"actual_codes":codes,"finding_count":len(findings),"findings":findings},indent=2))
        return 0 if codes==expected else 2
    print(json.dumps({"status":"valid" if not findings else "invalid","finding_count":len(findings),"findings":findings},indent=2))
    return 0 if not findings else 1

if __name__=="__main__": raise SystemExit(main())
