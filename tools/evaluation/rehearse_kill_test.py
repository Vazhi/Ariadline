#!/usr/bin/env python3
"""Validate fictional Ariadline kill-test rehearsal fixtures."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ALLOWED_STUDY_STATES = {"not_started", "synthetic_rehearsal"}
ALLOWED_EVIDENCE_CLAIMS = {"procedure_only"}
ALLOWED_GATE_STATES = {"approved", "not_applicable", "not_determined", "not_started", "rejected"}
REQUIRED_HUMAN_GATES = {
    "oversight", "permissions", "meaning_authority", "accessibility",
    "statistics", "preregistration", "recruitment",
}
ALLOWED_RESULTS = {
    "preserved", "not_preserved", "not_determined",
    "minor_difference", "editorial_difference", "not_applicable",
}
ALLOWED_SEVERITIES = {"critical", "major", "minor", "editorial", "not_applicable"}
ALLOWED_COMPARABILITY = {"comparable", "not_comparable", "not_determined"}


def add(findings: list[dict[str, str]], code: str, path: str, message: str) -> None:
    findings.append({"code": code, "path": path, "message": message})


def text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def preservation_result(record: Any, path: str, findings: list[dict[str, str]]) -> str:
    if not isinstance(record, dict):
        add(findings, "PRESERVATION_RECORD_INCOMPLETE", path, "Preservation record must be an object.")
        return "not_determined"

    dimensions = record.get("dimensions")
    hard_failure = False
    unresolved = False
    material_count = 0

    dimensions_present = isinstance(dimensions, list) and bool(dimensions)
    if not dimensions_present:
        add(findings, "PRESERVATION_DIMENSIONS_INCOMPLETE", f"{path}.dimensions", "At least one preservation dimension is required.")
        dimensions = []
        unresolved = True

    for index, dimension in enumerate(dimensions):
        dpath = f"{path}.dimensions[{index}]"
        if not isinstance(dimension, dict):
            add(findings, "PRESERVATION_DIMENSION_INVALID", dpath, "Dimension must be an object.")
            unresolved = True
            continue

        if not text(dimension.get("dimension")):
            add(findings, "PRESERVATION_DIMENSION_INVALID", f"{dpath}.dimension", "Dimension identifier is required.")
            unresolved = True

        result = dimension.get("result")
        severity = dimension.get("severity")
        material = dimension.get("material")

        if result not in ALLOWED_RESULTS:
            add(findings, "PRESERVATION_DIMENSION_INVALID", f"{dpath}.result", "Preservation result is invalid.")
            unresolved = True
            continue
        if severity not in ALLOWED_SEVERITIES:
            add(findings, "PRESERVATION_DIMENSION_INVALID", f"{dpath}.severity", "Preservation severity is invalid.")
            unresolved = True
        if not isinstance(material, bool):
            add(findings, "PRESERVATION_DIMENSION_INVALID", f"{dpath}.material", "Material must be a boolean.")
            unresolved = True
            continue

        if material and result != "not_applicable":
            material_count += 1
        if result == "not_preserved" and severity in {"critical", "major"}:
            hard_failure = True
        elif result == "not_determined" and material:
            unresolved = True
        elif material and result != "preserved":
            unresolved = True
        elif result in {"minor_difference", "editorial_difference"} and not dimension.get("confirmed_nonmaterial", False):
            unresolved = True

    if dimensions_present and material_count == 0:
        add(findings, "PRESERVATION_DIMENSIONS_INCOMPLETE", f"{path}.dimensions", "At least one valid applicable material dimension is required.")
        unresolved = True

    expected = "not_preserved" if hard_failure else "not_determined" if unresolved else "preserved"
    actual = record.get("overall")
    if actual != expected:
        add(findings, "PRESERVATION_AGGREGATION_INVALID", f"{path}.overall", f"Recorded {actual!r}; derived {expected!r}.")
    return expected


def validate(data: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []

    if not text(data.get("fixture_id")):
        add(findings, "FIXTURE_ID_REQUIRED", "$.fixture_id", "Fixture ID is required.")
    if data.get("synthetic_only") is not True:
        add(findings, "SYNTHETIC_FLAG_REQUIRED", "$.synthetic_only", "Rehearsal fixtures must be synthetic-only.")
    if data.get("study_state") not in ALLOWED_STUDY_STATES:
        add(findings, "STUDY_STATE_ADVANCED", "$.study_state", "A rehearsal cannot advance the human study state.")
    if data.get("evidence_claim") not in ALLOWED_EVIDENCE_CLAIMS:
        add(findings, "HUMAN_EVIDENCE_CLAIMED", "$.evidence_claim", "Synthetic fixtures may claim procedure validation only.")

    gates = data.get("human_gates") if isinstance(data.get("human_gates"), dict) else {}
    for gate in sorted(REQUIRED_HUMAN_GATES):
        if gate not in gates:
            add(findings, "HUMAN_GATE_MISSING", f"$.human_gates.{gate}", f"Human gate {gate} is missing.")
        elif gates[gate] not in ALLOWED_GATE_STATES:
            add(findings, "HUMAN_GATE_STATE_INVALID", f"$.human_gates.{gate}", f"Human gate {gate} has an invalid state.")
    unresolved_gates = [gate for gate in REQUIRED_HUMAN_GATES if gates.get(gate) not in {"approved", "not_applicable"}]

    launch = data.get("launch") if isinstance(data.get("launch"), dict) else {}
    if not isinstance(launch.get("ready"), bool):
        add(findings, "LAUNCH_RECORD_INCOMPLETE", "$.launch.ready", "Launch readiness must be a boolean.")
    launch_ready = launch.get("ready") is True

    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        add(findings, "CASES_REQUIRED", "$.cases", "At least one rehearsal case is required.")
        cases = []

    seen: set[str] = set()
    selected_count = 0
    selected_ineligible = False

    for index, case in enumerate(cases):
        path = f"$.cases[{index}]"
        if not isinstance(case, dict):
            add(findings, "CASE_RECORD_INCOMPLETE", path, "Case must be an object.")
            continue

        complete = True
        case_id = case.get("case_id")
        if not text(case_id) or case_id in seen:
            add(findings, "CASE_ID_INVALID", f"{path}.case_id", "Case IDs must be present and unique.")
            complete = False
        if text(case_id):
            seen.add(case_id)
        if not text(case.get("scenario")):
            add(findings, "CASE_RECORD_INCOMPLETE", f"{path}.scenario", "Scenario is required.")
            complete = False

        selected = case.get("selected_for_launch")
        if not isinstance(selected, bool):
            add(findings, "LAUNCH_SELECTION_INVALID", f"{path}.selected_for_launch", "Launch selection must be a boolean.")
            selected = False
            complete = False
        selected_count += int(selected)

        conditions = case.get("conditions") if isinstance(case.get("conditions"), dict) else {}
        records: dict[str, dict[str, Any]] = {}
        for condition in ("P", "S"):
            cpath = f"{path}.conditions.{condition}"
            record = conditions.get(condition)
            if not isinstance(record, dict):
                add(findings, "CONDITION_RECORD_INCOMPLETE", cpath, f"{condition} condition record is required.")
                record = {}
                complete = False
            for field in ("editor_id", "shared_packet_hash", "output_hash"):
                if not text(record.get(field)):
                    add(findings, "CONDITION_RECORD_INCOMPLETE", f"{cpath}.{field}", f"{condition} condition requires {field}.")
                    complete = False
            records[condition] = record

        p_record, s_record = records["P"], records["S"]
        separate_editors = bool(p_record.get("editor_id")) and p_record.get("editor_id") != s_record.get("editor_id")
        if not separate_editors:
            add(findings, "SAME_EDITOR_SAME_RECORD", f"{path}.conditions", "One editor cannot produce P and S for the same record.")

        same_packet = text(p_record.get("shared_packet_hash")) and p_record.get("shared_packet_hash") == s_record.get("shared_packet_hash")
        if not same_packet:
            add(findings, "SHARED_PACKET_HASH_MISMATCH", f"{path}.conditions", "P and S must use the same non-empty shared packet hash.")

        scorer = case.get("scorer_packet") if isinstance(case.get("scorer_packet"), dict) else {}
        scorer_clean = all(scorer.get(field) is True for field in ("rule_metadata_absent", "condition_identity_absent", "editor_metadata_absent"))
        if not scorer_clean:
            add(findings, "SCORER_METADATA_LEAK", f"{path}.scorer_packet", "Scorer material must exclude restricted metadata.")

        freeze = case.get("scoring_freeze") if isinstance(case.get("scoring_freeze"), dict) else {}
        freeze_valid = freeze.get("frozen_before_condition_output") is True and text(freeze.get("key_hash"))
        if not freeze_valid:
            add(findings, "SCORING_FREEZE_INVALID", f"{path}.scoring_freeze", "Scoring must freeze before condition output and record a key hash.")

        preservation = case.get("preservation") if isinstance(case.get("preservation"), dict) else {}
        results = {
            condition: preservation_result(preservation.get(condition), f"{path}.preservation.{condition}", findings)
            for condition in ("P", "S")
        }

        comparability = case.get("comparability")
        if comparability not in ALLOWED_COMPARABILITY:
            add(findings, "COMPARABILITY_INVALID", f"{path}.comparability", "Comparability state is invalid.")
            comparable = False
        else:
            comparable = comparability == "comparable"

        structurally_valid = complete and separate_editors and same_packet and scorer_clean and freeze_valid and comparable
        expected_eligible = structurally_valid and results["P"] == "preserved" and results["S"] == "preserved"
        if (case.get("pair_eligible_for_benefit") is True) != expected_eligible:
            add(findings, "PAIR_ELIGIBILITY_INVALID", f"{path}.pair_eligible_for_benefit", "Pair eligibility requires complete, comparable, uncontaminated, masked, frozen, preserved P and S records.")

        adverse = any(result in {"not_preserved", "not_determined"} for result in results.values())
        if adverse and case.get("adverse_result_retained") is not True:
            add(findings, "ADVERSE_RESULT_NOT_RETAINED", f"{path}.adverse_result_retained", "Failed or unresolved preservation must remain visible.")

        exposure = case.get("reader_exposure_allowed") is True
        if exposure and not selected:
            add(findings, "READER_EXPOSURE_WITH_UNSELECTED_PAIR", f"{path}.reader_exposure_allowed", "Reader exposure requires explicit launch selection.")
        if exposure and not expected_eligible:
            add(findings, "READER_EXPOSURE_WITH_INELIGIBLE_PAIR", f"{path}.reader_exposure_allowed", "An ineligible pair cannot enter reader exposure.")
        if exposure and (not launch_ready or unresolved_gates):
            add(findings, "READER_EXPOSURE_WITH_UNREADY_LAUNCH", f"{path}.reader_exposure_allowed", "Reader exposure cannot be allowed before launch readiness and human gates pass.")

        if selected and not expected_eligible:
            add(findings, "LAUNCH_SELECTION_INELIGIBLE", f"{path}.selected_for_launch", "Only structurally valid preserved pairs may be selected for launch.")
            selected_ineligible = True
        if case.get("not_determined_promoted_to_success") is True:
            add(findings, "NOT_DETERMINED_PROMOTED", f"{path}.not_determined_promoted_to_success", "not determined cannot be promoted to success.")

    if launch_ready and unresolved_gates:
        add(findings, "LAUNCH_WITH_UNRESOLVED_HUMAN_GATES", "$.launch.ready", "Launch cannot be ready with unresolved human gates.")
    if launch_ready and selected_count == 0:
        add(findings, "LAUNCH_WITHOUT_SELECTED_RECORDS", "$.launch.ready", "Launch readiness requires at least one selected pair.")
    if launch_ready and selected_ineligible:
        add(findings, "LAUNCH_WITH_INELIGIBLE_RECORDS", "$.launch.ready", "Launch cannot be ready with ineligible selected records.")
    if data.get("parent_issue_9_advanced") is True:
        add(findings, "PARENT_STUDY_ADVANCED", "$.parent_issue_9_advanced", "A rehearsal cannot advance parent issue #9.")

    return sorted(findings, key=lambda item: (item["code"], item["path"], item["message"]))


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def identities(findings: list[dict[str, str]]) -> list[dict[str, str]]:
    return sorted(
        ({"code": finding["code"], "path": finding["path"]} for finding in findings),
        key=lambda finding: (finding["code"], finding["path"]),
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture", type=Path)
    parser.add_argument("--expect-findings", type=Path)
    args = parser.parse_args()

    findings = validate(load(args.fixture))
    actual = identities(findings)
    if args.expect_findings:
        expected = sorted(load(args.expect_findings)["expected_findings"], key=lambda finding: (finding["code"], finding["path"]))
        status = "expected_failures_detected" if actual == expected else "self_test_failed"
        print(json.dumps({"status": status, "expected_findings": expected, "actual_findings": actual, "finding_count": len(findings), "findings": findings}, indent=2))
        return 0 if actual == expected else 2

    print(json.dumps({"status": "valid" if not findings else "invalid", "finding_count": len(findings), "findings": findings}, indent=2))
    return 0 if not findings else 1


if __name__ == "__main__":
    raise SystemExit(main())
