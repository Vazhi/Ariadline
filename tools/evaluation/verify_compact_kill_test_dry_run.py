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
        assignment_columns = ["assignment_id", "participant_id", "masked_text_code", "order_position", "domain_family"]
        mapping_columns = ["assignment_id", "material_id", "meaning_record_id", "condition", "condition_output_hash"]
        return {
            "fixture_id": value["fixture_id"],
            "synthetic_only": value["synthetic_only"],
            "seed": value["seed"],
            "algorithm": value["algorithm"],
            "participant_count": value["participant_count"],
            "eligible_material_count": value["eligible_material_count"],
            "schedule_version": "SYN-SCHEDULE-0.1",
            "schedule_hash": value["schedule_hash"],
            "assignment_columns": assignment_columns,
            "assignments": [[row[column] for column in assignment_columns] for row in value["assignments"]],
            "mapping_columns": mapping_columns,
            "restricted_condition_mapping": [[row[column] for column in mapping_columns] for row in value["restricted_condition_mapping"]],
        }
    if filename == "scoring_and_adjudication.json":
        response_columns = ["response_id", "assignment_id", "masked_text_code", "question_id", "answer_class", "response_value", "completion_state", "mechanical_exclusion_code"]
        score_columns = ["score_id", "response_id", "scorer_id", "independent_of_ariadline", "scoring_key_hash", "score", "critical_error"]
        adjudication_columns = ["response_id", "adjudicator_id", "independent_of_ariadline", "initial_scores", "final_score", "reason"]
        exclusion_columns = ["response_id", "assignment_id", "code", "frozen_mechanical_rule", "reason"]
        return {
            "fixture_id": value["fixture_id"],
            "synthetic_only": value["synthetic_only"],
            "masking_assertions": {"condition_identity_absent": True, "rule_metadata_absent": True, "editor_metadata_absent": True},
            "response_columns": response_columns,
            "responses": [[row[column] for column in response_columns] for row in value["responses"]],
            "score_columns": score_columns,
            "scores": [[row[column] for column in score_columns] for row in value["scores"]],
            "adjudication_columns": adjudication_columns,
            "adjudications": [[row[column] for column in adjudication_columns] for row in value["adjudications"]],
            "planned_exclusions": value["planned_exclusions"],
            "applied_exclusion_columns": exclusion_columns,
            "applied_exclusions": [[row[column] for column in exclusion_columns] for row in value["applied_exclusions"]],
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
