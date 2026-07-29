#!/usr/bin/env python3
"""Write or verify compact, round-trip-safe Ariadline synthetic dry-run fixtures."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from run_compact_kill_test_dry_run import OUTPUT_FILES, build, digest

ANSWER_CODES = {"correct": "C", "incorrect": "I", "uncertain": "U", "missing": "M"}
ANSWER_VALUES = {value: key for key, value in ANSWER_CODES.items()}
COMPLETION_CODES = {"complete": "C", "missing": "M", "technical_failure": "T", "excluded": "E"}
COMPLETION_VALUES = {value: key for key, value in COMPLETION_CODES.items()}


def assignment_id(participant_number: int, order: int) -> str:
    return f"SYN-ASG-{participant_number:02d}-{order:02d}"


def participant_id(participant_number: int) -> str:
    return f"SYN-PART-{participant_number:02d}"


def response_id(participant_number: int, order: int) -> str:
    return f"SYN-RESP-{participant_number:02d}-{order:02d}"


def assignment_storage(value: dict[str, Any]) -> dict[str, Any]:
    public = {row["assignment_id"]: row for row in value["assignments"]}
    restricted = {row["assignment_id"]: row for row in value["restricted_condition_mapping"]}
    material_manifest: dict[str, list[Any]] = {}
    participant_schedules: dict[int, list[list[Any]]] = {}

    for aid, row in public.items():
        mapping = restricted[aid]
        material_id = mapping["material_id"]
        manifest = material_manifest.setdefault(material_id,[mapping["meaning_record_id"], row["domain_family"], None, None])
        manifest[2 if mapping["condition"] == "P" else 3] = mapping["condition_output_hash"]
        number = int(row["participant_id"].rsplit("-", 1)[1])
        participant_schedules.setdefault(number, []).append([row["order_position"], material_id, mapping["condition"], row["masked_text_code"]])

    return {
        "fixture_id": value["fixture_id"], "synthetic_only": value["synthetic_only"],
        "seed": value["seed"], "algorithm": value["algorithm"],
        "participant_count": value["participant_count"], "eligible_material_count": value["eligible_material_count"],
        "schedule_version": "SYN-SCHEDULE-0.2", "schedule_hash": value["schedule_hash"],
        "id_derivation": "participant=SYN-PART-%02d; assignment=SYN-ASG-%02d-%02d",
        "material_columns": ["material_id", "meaning_record_id", "domain_family", "P_output_hash", "S_output_hash"],
        "materials": [[mid, *manifest] for mid, manifest in sorted(material_manifest.items())],
        "entry_columns": ["order_position", "material_id", "condition", "masked_text_code"],
        "participant_schedules": [[number, sorted(entries)] for number, entries in sorted(participant_schedules.items())],
    }


def reconstruct_assignments(compact: dict[str, Any]) -> dict[str, Any]:
    materials = {row[0]: {"meaning_record_id": row[1], "domain_family": row[2], "P_output_hash": row[3], "S_output_hash": row[4]} for row in compact["materials"]}
    assignments=[]; restricted=[]
    for number, entries in compact["participant_schedules"]:
        for order, material_id, condition, masked_text_code in entries:
            aid=assignment_id(number,order); material=materials[material_id]
            assignments.append({"assignment_id":aid,"participant_id":participant_id(number),"masked_text_code":masked_text_code,"order_position":order,"domain_family":material["domain_family"],"schedule_version":compact["schedule_version"],"schedule_hash":compact["schedule_hash"]})
            restricted.append({"assignment_id":aid,"material_id":material_id,"meaning_record_id":material["meaning_record_id"],"condition":condition,"condition_output_hash":material[f"{condition}_output_hash"]})
    return {"fixture_id":compact["fixture_id"],"synthetic_only":compact["synthetic_only"],"seed":compact["seed"],"algorithm":compact["algorithm"],"participant_count":compact["participant_count"],"eligible_material_count":compact["eligible_material_count"],"assignments":assignments,"restricted_condition_mapping":restricted,"schedule_hash":compact["schedule_hash"]}


def scoring_storage(value: dict[str, Any], source: dict[str, Any], assignments_compact: dict[str, Any]) -> dict[str, Any]:
    assignment_lookup={}
    for number, entries in assignments_compact["participant_schedules"]:
        for order, material_id, condition, masked_text_code in entries: assignment_lookup[(number,order)]=(material_id,condition,masked_text_code)
    scores_by_response={}
    for row in value["scores"]: scores_by_response.setdefault(row["response_id"],[]).append(row)
    adjudications={row["response_id"]:row for row in value["adjudications"]}; participant_results={}
    for response in value["responses"]:
        parts=response["assignment_id"].split("-"); number,order=int(parts[-2]),int(parts[-1]); material_id,condition,masked_text_code=assignment_lookup[(number,order)]
        if response["material_id"]!=material_id or response["masked_text_code"]!=masked_text_code: raise ValueError(f"response mapping mismatch for {response['response_id']}")
        rows=sorted(scores_by_response.get(response["response_id"],[]),key=lambda x:x["scorer_id"]); adj=adjudications.get(response["response_id"])
        participant_results.setdefault(number,[]).append([order,material_id,condition,ANSWER_CODES[response["answer_class"]],response["response_value"],COMPLETION_CODES[response["completion_state"]],response["mechanical_exclusion_code"],rows[0]["score"] if rows else None,rows[1]["score"] if rows else None,rows[0]["critical_error"] if rows else None,rows[1]["critical_error"] if rows else None,adj["final_score"] if adj else None])
    manifest=[[m["material_id"],m["meaning_record_id"],m["scoring_key"]["question_id"],m["scoring_key"]["key_hash"]] for m in sorted(source["materials"],key=lambda x:x["material_id"])]
    return {
        "fixture_id":value["fixture_id"],"synthetic_only":value["synthetic_only"],
        "id_derivation":"response=SYN-RESP-%02d-%02d; assignment=SYN-ASG-%02d-%02d",
        "source_manifest_columns":["material_id","meaning_record_id","question_id","scoring_key_hash"],"source_manifest":manifest,
        "scorers":[["SYN-SCORER-A",False],["SYN-SCORER-I",True]],"adjudicator":["SYN-ADJ-I",True],
        "entry_columns":["order_position","material_id","condition","answer_code","response_value","completion_code","mechanical_exclusion_code","score_A","score_I","critical_A","critical_I","adjudicated_final"],
        "participant_results":[[n,sorted(e)] for n,e in sorted(participant_results.items())],
        "planned_exclusions":value["planned_exclusions"],
        "applied_exclusions":[[r["assignment_id"],r["response_id"],r["code"],r["reason"]] for r in value["applied_exclusions"]],
        "planned_deviations":value["planned_deviations"],
    }


def reconstruct_scoring(compact: dict[str, Any], assignments_compact: dict[str, Any]) -> dict[str, Any]:
    amap={}
    for number, entries in assignments_compact["participant_schedules"]:
        for order, material_id, _condition, masked in entries: amap[(number,order)]=(material_id,masked)
    manifest={r[0]:{"meaning_record_id":r[1],"question_id":r[2],"key_hash":r[3]} for r in compact["source_manifest"]}
    responses=[];scores=[];adjudications=[];sa,si=compact["scorers"];adj=compact["adjudicator"]
    for number, entries in compact["participant_results"]:
        for e in entries:
            order,material_id,_condition,answer_code,response_value,completion_code,exclusion_code,score_a,score_i,critical_a,critical_i,final=e
            aid=assignment_id(number,order);rid=response_id(number,order);mapped,masked=amap[(number,order)]
            if mapped!=material_id: raise ValueError(f"compact material mismatch for {aid}")
            m=manifest[material_id]
            responses.append({"response_id":rid,"assignment_id":aid,"masked_text_code":masked,"material_id":material_id,"meaning_record_id":m["meaning_record_id"],"question_id":m["question_id"],"answer_class":ANSWER_VALUES[answer_code],"response_value":response_value,"condition_identity_absent":True,"rule_metadata_absent":True,"completion_state":COMPLETION_VALUES[completion_code],"mechanical_exclusion_code":exclusion_code})
            if score_a is not None or score_i is not None:
                if score_a is None or score_i is None: raise ValueError(f"partial score pair for {rid}")
                for scorer,score,critical in ((sa,score_a,critical_a),(si,score_i,critical_i)):
                    scores.append({"score_id":f"{rid}-{scorer[0].rsplit('-',1)[1]}","response_id":rid,"question_id":m["question_id"],"scorer_id":scorer[0],"independent_of_ariadline":scorer[1],"condition_identity_absent":True,"editor_metadata_absent":True,"scoring_key_hash":m["key_hash"],"score":score,"critical_error":critical})
            if final is not None: adjudications.append({"response_id":rid,"question_id":m["question_id"],"adjudicator_id":adj[0],"independent_of_ariadline":adj[1],"condition_identity_absent":True,"initial_scores":[score_a,score_i],"final_score":final,"reason":"synthetic deterministic adjudication"})
    applied=[{"assignment_id":r[0],"response_id":r[1],"code":r[2],"frozen_mechanical_rule":True,"reason":r[3]} for r in compact["applied_exclusions"]]
    return {"fixture_id":compact["fixture_id"],"synthetic_only":compact["synthetic_only"],"responses":responses,"scores":scores,"adjudications":adjudications,"planned_exclusions":compact["planned_exclusions"],"applied_exclusions":applied,"planned_deviations":compact["planned_deviations"]}


def compact_outputs(raw: dict[str, dict[str, Any]], source: dict[str, Any]) -> dict[str, dict[str, Any]]:
    a=assignment_storage(raw["assignments.json"]);s=scoring_storage(raw["scoring_and_adjudication.json"],source,a)
    return {"assignments.json":a,"scoring_and_adjudication.json":s,"analysis.json":raw["analysis.json"]}


def validate_round_trip(compact: dict[str, dict[str, Any]], raw: dict[str, dict[str, Any]]) -> list[dict[str, str]]:
    findings=[]
    if reconstruct_assignments(compact["assignments.json"])!=raw["assignments.json"]: findings.append({"code":"ASSIGNMENT_ROUND_TRIP_MISMATCH","path":"assignments.json"})
    if reconstruct_scoring(compact["scoring_and_adjudication.json"],compact["assignments.json"])!=raw["scoring_and_adjudication.json"]: findings.append({"code":"SCORING_ROUND_TRIP_MISMATCH","path":"scoring_and_adjudication.json"})
    if compact["analysis.json"]["validation"]["status"]!="pass": findings.append({"code":"RAW_VALIDATION_FAILED","path":"analysis.json"})
    return findings


def main() -> int:
    p=argparse.ArgumentParser();p.add_argument("source",type=Path);p.add_argument("--output-dir",type=Path);p.add_argument("--expect-dir",type=Path);x=p.parse_args()
    source=json.loads(x.source.read_text());raw=build(source);outputs=compact_outputs(raw,source);findings=validate_round_trip(outputs,raw)
    if x.output_dir:
        x.output_dir.mkdir(parents=True,exist_ok=True)
        for name,value in outputs.items():(x.output_dir/name).write_text(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\n")
    if x.expect_dir:
        for name in OUTPUT_FILES:
            path=x.expect_dir/name
            if not path.exists(): findings.append({"code":"EXPECTED_OUTPUT_MISSING","path":name})
            elif json.loads(path.read_text())!=outputs[name]: findings.append({"code":"OUTPUT_MISMATCH","path":name})
    result={"status":"expected_outputs_matched" if x.expect_dir and not findings else "generated" if not findings else "self_test_failed","fixture_id":source["fixture_id"],"output_hashes":{n:"sha256:"+digest(v) for n,v in outputs.items()},"validation":raw["analysis.json"]["validation"],"summary":raw["analysis.json"]["summary"],"mock_disposition":raw["analysis.json"]["mock_disposition"],"comparison_findings":findings,"synthetic_only":True,"evidence_claim":"procedure_only"}
    print(json.dumps(result,indent=2,sort_keys=True));return 0 if not findings else 2
if __name__=="__main__":raise SystemExit(main())
