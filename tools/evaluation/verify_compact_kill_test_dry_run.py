#!/usr/bin/env python3
"""Write or verify compact columnar fixtures for the Ariadline synthetic dry run."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from run_compact_kill_test_dry_run import OUTPUT_FILES, build, digest


def storage_view(filename: str, value: dict[str, Any]) -> dict[str, Any]:
    """Return the compact, lossless representation committed as an expected fixture."""
    if filename == "assignments.json":
        public = {row["assignment_id"]: row for row in value["assignments"]}
        restricted = {row["assignment_id"]: row for row in value["restricted_condition_mapping"]}
        material_manifest: dict[str, list[Any]] = {}
        by_participant: dict[str, list[list[Any]]] = {}
        for assignment_id, row in public.items():
            mapping = restricted[assignment_id]
            material_id = mapping["material_id"]
            manifest = material_manifest.setdefault(material_id, [mapping["meaning_record_id"], row["domain_family"], None, None])
            manifest[2 if mapping["condition"] == "P" else 3] = mapping["condition_output_hash"]
            by_participant.setdefault(row["participant_id"], []).append([
                row["order_position"], material_id, mapping["condition"], row["masked_text_code"]
            ])
        return {
            "fixture_id": value["fixture_id"],
            "synthetic_only": value["synthetic_only"],
            "seed": value["seed"],
            "algorithm": value["algorithm"],
            "participant_count": value["participant_count"],
            "eligible_material_count": value["eligible_material_count"],
            "schedule_version": "SYN-SCHEDULE-0.1",
            "schedule_hash": value["schedule_hash"],
            "derivation": "assignment_id=SYN-ASG-<participant number>-<order>; condition mapping is restricted metadata in each entry",
            "material_columns": ["material_id", "meaning_record_id", "domain_family", "P_output_hash", "S_output_hash"],
            "materials": [[material_id, *manifest] for material_id, manifest in sorted(material_manifest.items())],
            "entry_columns": ["order_position", "material_id", "condition", "masked_text_code"],
            "participant_schedules": [[participant_id, sorted(entries)] for participant_id, entries in sorted(by_participant.items())],
        }
    if filename == "scoring_and_adjudication.json":
        scores_by_response: dict[str, list[dict[str, Any]]] = {}
        for row in value["scores"]:
            scores_by_response.setdefault(row["response_id"], []).append(row)
        adjudications = {row["response_id"]: row for row in value["adjudications"]}
        by_participant: dict[str, list[list[Any]]] = {}
        key_manifest: dict[str, list[str]] = {}
        for response in value["responses"]:
            participant_id = response["assignment_id"].replace("SYN-ASG-", "SYN-PART-").rsplit("-", 1)[0]
            order_position = int(response["assignment_id"].rsplit("-", 1)[1])
            scorer_rows = sorted(scores_by_response[response["response_id"]], key=lambda item: item["scorer_id"])
            adjudication = adjudications.get(response["response_id"])
            material_number = response["question_id"].rsplit("-", 1)[1]
            material_id = f"MAT-{material_number}"
            key_manifest[material_id] = [response["question_id"], scorer_rows[0]["scoring_key_hash"]]
            by_participant.setdefault(participant_id, []).append([
                order_position,
                response["answer_class"],
                response["response_value"],
                response["completion_state"],
                response["mechanical_exclusion_code"],
                scorer_rows[0]["score"],
                scorer_rows[1]["score"],
                scorer_rows[0]["critical_error"],
                scorer_rows[1]["critical_error"],
                adjudication["final_score"] if adjudication else None,
            ])
        return {
            "fixture_id": value["fixture_id"],
            "synthetic_only": value["synthetic_only"],
            "masking_assertions": {"condition_identity_absent": True, "rule_metadata_absent": True, "editor_metadata_absent": True},
            "derivation": "assignment_id and response_id derive from participant number and order; masked code and material/condition come from assignments.json",
            "scorers": [["SYN-SCORER-A", False], ["SYN-SCORER-I", True]],
            "adjudicator": ["SYN-ADJ-I", True],
            "key_columns": ["material_id", "question_id", "scoring_key_hash"],
            "scoring_keys": [[material_id, *manifest] for material_id, manifest in sorted(key_manifest.items())],
            "entry_columns": ["order_position", "answer_class", "response_value", "completion_state", "mechanical_exclusion_code", "score_A", "score_I", "critical_A", "critical_I", "adjudicated_final"],
            "participant_results": [[participant_id, sorted(entries)] for participant_id, entries in sorted(by_participant.items())],
            "planned_exclusions": value["planned_exclusions"],
            "applied_exclusions": [[row["assignment_id"], row["response_id"], row["code"], row["reason"]] for row in value["applied_exclusions"]],
            "planned_deviations": value["planned_deviations"],
        }
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--expect-dir", type=Path)
    args = parser.parse_args()

    source = json.loads(args.source.read_text(encoding="utf-8"))
    raw_outputs = build(source)
    outputs = {name: storage_view(name, value) for name, value in raw_outputs.items()}

    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        for filename, value in outputs.items():
            (args.output_dir / filename).write_text(
                json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n",
                encoding="utf-8",
            )

    findings: list[dict[str, str]] = []
    if args.expect_dir:
        for filename in OUTPUT_FILES:
            expected_path = args.expect_dir / filename
            if not expected_path.exists():
                findings.append({"code": "EXPECTED_OUTPUT_MISSING", "path": filename})
                continue
            expected = json.loads(expected_path.read_text(encoding="utf-8"))
            if expected != outputs[filename]:
                findings.append({"code": "OUTPUT_MISMATCH", "path": filename})

    result = {
        "status": "expected_outputs_matched" if args.expect_dir and not findings else "generated" if not findings else "self_test_failed",
        "fixture_id": source["fixture_id"],
        "output_hashes": {name: f"sha256:{digest(value)}" for name, value in outputs.items()},
        "validation": raw_outputs["analysis.json"]["validation"],
        "mock_disposition": raw_outputs["analysis.json"]["mock_disposition"],
        "comparison_findings": findings,
        "synthetic_only": True,
        "evidence_claim": "procedure_only",
    }
    print(json.dumps(result, indent=2))
    return 0 if not findings else 2


if __name__ == "__main__":
    raise SystemExit(main())
