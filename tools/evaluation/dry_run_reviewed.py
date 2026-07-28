"""Reviewed synthetic dry-run operations.

This module wraps the original fixture builder with balanced assignments,
exact mask checks, and full negative-code coverage. All records remain
fictional and non-evidential.
"""
from __future__ import annotations

import copy
import json
import random
from collections import Counter, defaultdict
from pathlib import Path

import dry_run_common as base

SEED = base.SEED

EXPECTED_CODES = [
    "AUTHENTICITY_BOUNDARY",
    "BROKEN_MATERIAL_FK",
    "BROKEN_PARTICIPANT_FK",
    "BROKEN_TRIAL_FK",
    "CANTO_PARTICIPANT_CAP",
    "CANTO_TRIAL_CAP",
    "CONDITION_IMBALANCE",
    "CONDITION_MEANING_MISMATCH",
    "DUPLICATE_DEVIATION_ID",
    "DUPLICATE_MASK_CODE",
    "DUPLICATE_MEANING_EXPOSURE",
    "DUPLICATE_PARTICIPANT_ID",
    "DUPLICATE_TRIAL_ID",
    "EVIDENCE_BOUNDARY",
    "FORBIDDEN_IDENTIFIER_FIELD",
    "INVALID_PARTICIPANT_ID",
    "INVALID_TRIAL_ID",
    "MASK_CODE_MISMATCH",
    "MASK_LEAK",
    "MEANING_RECORD_MISMATCH",
    "MISSING_TABLE_ROWS",
    "NOT_DETERMINED_AS_SUCCESS",
    "NOT_DETERMINED_DOWNGRADED",
    "NOT_SYNTHETIC",
    "ORDER_IMBALANCE",
    "POST_WITHDRAWAL_TRIAL",
    "PRESERVATION_NOT_CONFIRMED",
    "PROHIBITED_U_CONDITION",
    "PROHIBITED_U_REGISTRATION",
    "REQUIRED_CONDITION_MISSING",
    "SCORING_UNMASKED",
    "TASK_CONDITION_REGISTRATION",
    "UNIVERSAL_U_REQUIREMENT",
    "UNREGISTERED_TRIAL_CONDITION",
]

_BASE_PARTICIPANTS = base.participants
_BASE_TRIAL_ROWS = base.trial_rows


def participants():
    rows = _BASE_PARTICIPANTS()
    rows[-1].update({
        "completion_state": "complete",
        "exclusion_code": "none",
        "withdrawal_order_position": None,
    })
    withdrawn = copy.deepcopy(rows[-1])
    withdrawn.update({
        "participant_id": "SLE-PART-D021",
        "completion_state": "withdrawn",
        "exclusion_code": "synthetic-withdrawal",
        "withdrawal_order_position": 0,
        "canto_span_contributor": "no",
    })
    rows.append(withdrawn)
    return rows


def trial_rows(parts, materials, conditions, seed=SEED):
    rng = random.Random(seed)
    masks = {
        (row["material_id"], row["condition"]): row["mask_code"]
        for row in conditions
    }
    active = [row for row in parts if row["completion_state"] != "withdrawn"]
    core = [row for row in materials if row["canto_span"] == "no"]
    rng.shuffle(core)

    schedule = []
    for participant_index, participant in enumerate(active):
        rotated = core[participant_index % len(core):] + core[:participant_index % len(core)]
        for order_position, material in enumerate(rotated[:-1], 1):
            schedule.append((participant_index, participant, material, order_position))

    baseline_id = "SLE-DRY-MAT-0001"
    baseline = [row for row in schedule if row[2]["material_id"] == baseline_id]
    u_participants = set()
    for position, parity in ((1, 1), (2, 0), (3, 0), (4, 1)):
        row = next(
            item for item in baseline
            if item[3] == position and item[0] % 2 == parity
        )
        u_participants.add(row[1]["participant_id"])

    output = []
    number = 1
    for participant_index, participant, material, position in schedule:
        material_id = material["material_id"]
        if material_id == baseline_id and participant["participant_id"] in u_participants:
            condition = "U"
        else:
            condition = "P" if participant_index % 2 == 0 else "S"
        output.append({
            "trial_id": f"SLE-DRY-TRIAL-{number:04d}",
            "participant_id": participant["participant_id"],
            "material_id": material_id,
            "meaning_record_id": material["meaning_record_id"],
            "material_version": "dry-run-v0.1",
            "condition": condition,
            "masked_condition": masks[(material_id, condition)],
            "task_type": material["task_type"],
            "domain_family": material["domain_family"],
            "pattern_ids": ["SLE-PATTERN-0001"],
            "rule_ids": ["SLE-RULE-0001", "SLE-RULE-0004"],
            "order_position": position,
            "response_started_at": None,
            "response_time_ms": 30000 + (participant_index * 137 + position * 211) % 45000,
            "completion_state": "complete",
            "device_band": ["desktop", "tablet", "mobile"][participant_index % 3],
            "accommodation_applied": participant["accessibility_accommodation"],
        })
        number += 1

    canto = next(row for row in materials if row["canto_span"] == "yes")
    for participant_index, condition in ((1, "P"), (11, "S")):
        participant = active[participant_index]
        output.append({
            "trial_id": f"SLE-DRY-TRIAL-{number:04d}",
            "participant_id": participant["participant_id"],
            "material_id": canto["material_id"],
            "meaning_record_id": canto["meaning_record_id"],
            "material_version": "dry-run-v0.1",
            "condition": condition,
            "masked_condition": masks[(canto["material_id"], condition)],
            "task_type": canto["task_type"],
            "domain_family": canto["domain_family"],
            "pattern_ids": ["SLE-PATTERN-0014"],
            "rule_ids": ["SLE-RULE-0001"],
            "order_position": 5,
            "response_started_at": None,
            "response_time_ms": 42000 + participant_index,
            "completion_state": "complete",
            "device_band": "desktop",
            "accommodation_applied": participant["accessibility_accommodation"],
        })
        number += 1
    return output


def build_valid(seed=SEED):
    old_participants = base.participants
    old_trial_rows = base.trial_rows
    base.participants = participants
    base.trial_rows = trial_rows
    try:
        fixture = base.build_valid(seed)
    finally:
        base.participants = old_participants
        base.trial_rows = old_trial_rows
    for row in fixture["conditions"]:
        row["result_scope"] = "synthetic-fixture-only"
    for row in fixture["preservation"]:
        row["result_scope"] = "synthetic-fixture-only"
    return fixture


def build_invalid(valid):
    fixture = base.build_invalid(valid)
    fixture["metadata"].update({
        "synthetic": False,
        "participant_evidence": True,
        "authentic_material": True,
    })
    fixture["qualitative_findings"] = []

    fixture["participants"].append(copy.deepcopy(fixture["participants"][0]))
    fixture["participants"][-1]["participant_id"] = "bad participant id"
    fixture["participants"].append(copy.deepcopy(fixture["participants"][1]))

    fixture["materials"][0]["required_conditions"].append("U")
    fixture["materials"][1]["required_conditions"] = ["S"]
    fixture["materials"][3]["optional_conditions"].append("U")

    fixture["conditions"].append({
        "condition_id": "SLE-DRY-MISSING-MAT-P",
        "material_id": "SLE-DRY-MAT-MISSING",
        "meaning_record_id": "SLE-DRY-BRIEF-MISSING",
        "condition": "P",
        "mask_code": "MX998",
        "condition_author_role": "synthetic-generator",
        "material_version": "dry-run-v0.1",
        "preservation_result": "preserved",
        "preservation_success": True,
        "result_scope": "synthetic-fixture-only",
        "independent_review_state": "synthetic-only",
        "lifecycle_state": "pilot_ready",
    })
    fixture["conditions"][0]["meaning_record_id"] = "SLE-DRY-BRIEF-WRONG"
    fixture["conditions"][1]["mask_code"] = fixture["conditions"][2]["mask_code"]

    def append_trial(source, trial_id, **changes):
        row = copy.deepcopy(source)
        row.update({"trial_id": trial_id, **changes})
        fixture["trials"].append(row)

    append_trial(fixture["trials"][0], "BAD-TRIAL-ID")
    append_trial(fixture["trials"][0], fixture["trials"][0]["trial_id"])
    append_trial(
        fixture["trials"][1],
        "SLE-DRY-TRIAL-9010",
        meaning_record_id="SLE-DRY-BRIEF-WRONG",
    )
    append_trial(
        fixture["trials"][3],
        "SLE-DRY-TRIAL-9011",
        masked_condition="MX997",
    )
    append_trial(
        fixture["trials"][5],
        "SLE-DRY-TRIAL-9012",
        material_id="SLE-DRY-MAT-MISSING",
        meaning_record_id="SLE-DRY-BRIEF-MISSING",
    )

    masks = {
        (row["material_id"], row["condition"]): row["mask_code"]
        for row in fixture["conditions"]
    }
    for row in [
        trial for trial in fixture["trials"]
        if trial["material_id"] == "SLE-DRY-MAT-0002"
        and trial["condition"] == "P"
    ][:4]:
        row["condition"] = "S"
        row["masked_condition"] = masks[("SLE-DRY-MAT-0002", "S")]

    fixture["scoring"][0]["condition_masked"] = "no"
    fixture["preservation"].append({
        "preservation_id": "SLE-DRY-PRES-9010",
        "trial_id": fixture["trials"][0]["trial_id"],
        "draft_version": "synthetic-output-v0.1",
        "meaning_record_id": fixture["trials"][0]["meaning_record_id"],
        "preservation_dimension": "scope",
        "preservation_result": "not determined",
        "severity": "editorial",
        "result_scope": "synthetic-fixture-only",
        "independent_reviewer_id": "SLE-REVIEWER-D001",
        "source_author_confirmation": "not applicable",
        "revision_time_ms": 1,
    })
    fixture["protocol_deviations"].append(
        copy.deepcopy(fixture["protocol_deviations"][0])
    )
    return fixture


def validate(fixture):
    findings = list(base.validate(fixture))
    add = lambda code, message, record="": findings.append(
        base.Finding(code, message, record)
    )

    materials = {
        str(row.get("material_id")): row
        for row in fixture.get("materials", [])
        if isinstance(row, dict)
    }
    meanings = {
        material_id: str(row.get("meaning_record_id"))
        for material_id, row in materials.items()
    }
    conditions = defaultdict(set)
    masks = {}
    seen_masks = set()
    for row in fixture.get("conditions", []):
        if not isinstance(row, dict):
            continue
        material_id = str(row.get("material_id", ""))
        condition = str(row.get("condition", ""))
        conditions[material_id].add(condition)
        if material_id in meanings and str(row.get("meaning_record_id", "")) != meanings[material_id]:
            add(
                "CONDITION_MEANING_MISMATCH",
                "Condition meaning does not match material.",
                str(row.get("condition_id", "")),
            )
        mask = str(row.get("mask_code", ""))
        if mask in seen_masks:
            add("DUPLICATE_MASK_CODE", "Duplicate mask.", mask)
        seen_masks.add(mask)
        masks[(material_id, condition)] = mask

    by_material = defaultdict(Counter)
    by_order = defaultdict(Counter)
    for row in fixture.get("trials", []):
        if not isinstance(row, dict):
            continue
        material_id = str(row.get("material_id", ""))
        condition = str(row.get("condition", ""))
        expected_mask = masks.get((material_id, condition))
        actual_mask = str(row.get("masked_condition", ""))
        if expected_mask is not None and actual_mask != expected_mask:
            add(
                "MASK_CODE_MISMATCH",
                "Trial mask does not match the registered condition mask.",
                str(row.get("trial_id", "")),
            )
        if condition in {"P", "S"}:
            by_material[material_id][condition] += 1
            position = row.get("order_position")
            if isinstance(position, int):
                by_order[position][condition] += 1

    for material_id, counts in by_material.items():
        if counts["P"] and counts["S"] and abs(counts["P"] - counts["S"]) > 1:
            add(
                "CONDITION_IMBALANCE",
                f"P/S counts are {counts['P']}/{counts['S']}.",
                material_id,
            )
    for position, counts in by_order.items():
        if counts["P"] and counts["S"] and abs(counts["P"] - counts["S"]) > 1:
            add(
                "ORDER_IMBALANCE",
                f"P/S counts are {counts['P']}/{counts['S']}.",
                str(position),
            )
    return findings


def write_fixtures(output_dir, seed=SEED):
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    valid = build_valid(seed)
    invalid = build_invalid(valid)
    (output / "valid_fixture.json").write_text(
        json.dumps(valid, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (output / "invalid_fixture.json").write_text(
        json.dumps(invalid, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return valid, invalid
