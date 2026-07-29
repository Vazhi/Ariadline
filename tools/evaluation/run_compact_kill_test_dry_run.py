#!/usr/bin/env python3
"""Run and validate the fictional Ariadline compact kill-test dry run.

The tool uses only deterministic synthetic records. It cannot approve human gates
or provide evidence that Ariadline is effective or safe for authentic writing.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean
from typing import Any

OUTPUT_FILES = (
    "assignments.json",
    "scoring_and_adjudication.json",
    "analysis.json",
)
ALLOWED_DOMAINS = {
    "theoretical_typological",
    "descriptive_community",
    "corpus_experimental",
    "computational_resource",
}
ALLOWED_PRESERVATION = {"preserved", "not_preserved", "not_determined"}
MECHANICAL_EXCLUSION_CODES = {
    "TECHNICAL_FAILURE",
    "FROZEN_MISSINGNESS_LIMIT",
    "DUPLICATE_PARTICIPATION",
    "WITHDRAWAL",
    "ASSIGNMENT_INTEGRITY_FAILURE",
    "MISSING_RESPONSE",
}


def canonical(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def digest(value: Any) -> str:
    return hashlib.sha256(canonical(value).encode("utf-8")).hexdigest()


def unit(seed: int, *parts: str) -> float:
    payload = "|".join((str(seed), *parts)).encode("utf-8")
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "big") / 2**64


def require(condition: bool, code: str, message: str, findings: list[dict[str, str]]) -> None:
    if not condition:
        findings.append({"code": code, "message": message})


def eligible_pair(material: dict[str, Any]) -> bool:
    conditions = material["conditions"]
    return (
        conditions["P"]["preservation"] == "preserved"
        and conditions["S"]["preservation"] == "preserved"
        and material["comparability"] == "comparable"
        and material["authority_state"] == "simulated_approved"
    )


def validate_source(data: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    require(data.get("synthetic_only") is True, "SYNTHETIC_FLAG", "synthetic_only must be true", findings)
    require(data.get("evidence_claim") == "procedure_only", "EVIDENCE_BOUNDARY", "evidence_claim must be procedure_only", findings)
    require(data.get("study_state") == "synthetic_rehearsal", "STUDY_STATE", "study_state must remain synthetic_rehearsal", findings)

    design = data.get("design", {})
    participant_count = design.get("participant_count")
    require(isinstance(participant_count, int) and 20 <= participant_count <= 30, "PARTICIPANT_RANGE", "participant_count must be 20-30", findings)
    require(design.get("items_per_participant") == 6, "ITEM_COUNT", "items_per_participant must be 6", findings)
    require(isinstance(design.get("seed"), int), "SEED_REQUIRED", "deterministic seed required", findings)

    materials = data.get("materials", [])
    require(isinstance(materials, list) and 10 <= len(materials) <= 12, "MATERIAL_RANGE", "10-12 materials required", findings)
    material_ids = [m.get("material_id") for m in materials if isinstance(m, dict)]
    require(len(material_ids) == len(set(material_ids)), "MATERIAL_IDS", "material IDs must be unique", findings)
    domains = {m.get("domain_family") for m in materials if isinstance(m, dict)}
    require(len(domains) >= 3 and domains <= ALLOWED_DOMAINS, "DOMAIN_COVERAGE", "at least three registered domains required", findings)

    s_worse = False
    inconclusive = False
    adverse_preservation = False
    for material in materials:
        conditions = material.get("conditions", {})
        for label in ("P", "S"):
            condition = conditions.get(label, {})
            require(condition.get("preservation") in ALLOWED_PRESERVATION, "PRESERVATION_STATE", f"{material.get('material_id')} {label} preservation invalid", findings)
        if conditions.get("S", {}).get("correct_probability", 1) < conditions.get("P", {}).get("correct_probability", 0):
            s_worse = True
        if material.get("scenario_class") == "inconclusive":
            inconclusive = True
        if any(conditions.get(label, {}).get("preservation") != "preserved" for label in ("P", "S")):
            adverse_preservation = True
        require(material.get("scoring_key", {}).get("meaning_record_id") == material.get("meaning_record_id"), "KEY_TRACEABILITY", f"{material.get('material_id')} key must trace to meaning record", findings)

    require(s_worse, "S_ADVERSE_SCENARIO", "at least one material must make S worse", findings)
    require(inconclusive, "INCONCLUSIVE_SCENARIO", "at least one inconclusive material required", findings)
    require(adverse_preservation, "PRESERVATION_ADVERSE", "at least one preservation failure or unresolved case required", findings)

    deviations = data.get("planned_deviations", [])
    exclusions = data.get("planned_exclusions", [])
    require(bool(deviations), "DEVIATION_REQUIRED", "at least one synthetic deviation required", findings)
    require(bool(exclusions), "EXCLUSION_REQUIRED", "at least one synthetic exclusion required", findings)
    for exclusion in exclusions:
        require(exclusion.get("code") in MECHANICAL_EXCLUSION_CODES, "EXCLUSION_CODE", "exclusion code must be frozen and mechanical", findings)

    return sorted(findings, key=lambda item: (item["code"], item["message"]))


def make_assignments(data: dict[str, Any]) -> dict[str, Any]:
    design = data["design"]
    seed = design["seed"]
    participants = [f"SYN-PART-{index:02d}" for index in range(1, design["participant_count"] + 1)]
    eligible = [m for m in data["materials"] if eligible_pair(m)]
    eligible.sort(key=lambda m: m["material_id"])
    item_count = design["items_per_participant"]
    assignments: list[dict[str, Any]] = []
    restricted_mapping: list[dict[str, Any]] = []

    require_shape = len(eligible) == 9 and item_count == 6 and len(participants) % 3 == 0
    if not require_shape:
        raise ValueError("cyclic-balanced-v1 requires 9 eligible materials, 6 items, and participant count divisible by 3")

    group_material_indexes = (
        (0, 1, 2, 3, 4, 5),
        (3, 4, 5, 6, 7, 8),
        (6, 7, 8, 0, 1, 2),
    )
    condition_by_group = (
        {0: "P", 1: "P", 2: "P", 3: "S", 4: "S", 5: "S"},
        {3: "P", 4: "P", 5: "P", 6: "S", 7: "S", 8: "S"},
        {6: "P", 7: "P", 8: "P", 0: "S", 1: "S", 2: "S"},
    )

    for p_index, participant_id in enumerate(participants):
        group = (p_index + seed % 3) % 3
        block = p_index // 3
        material_indexes = list(group_material_indexes[group])
        rotation = (block + seed % item_count) % item_count
        material_indexes = material_indexes[rotation:] + material_indexes[:rotation]
        selected = [eligible[index] for index in material_indexes]
        for order_position, material in enumerate(selected, start=1):
            m_index = eligible.index(material)
            condition = condition_by_group[group][m_index]
            assignment_id = f"SYN-ASG-{p_index + 1:02d}-{order_position:02d}"
            masked_text_code = f"SYN-TXT-{digest([assignment_id, material['material_id']])[:10]}"
            assignments.append({
                "assignment_id": assignment_id,
                "participant_id": participant_id,
                "masked_text_code": masked_text_code,
                "order_position": order_position,
                "domain_family": material["domain_family"],
                "schedule_version": "SYN-SCHEDULE-0.1",
                "schedule_hash": "pending",
            })
            restricted_mapping.append({
                "assignment_id": assignment_id,
                "material_id": material["material_id"],
                "meaning_record_id": material["meaning_record_id"],
                "condition": condition,
                "condition_output_hash": material["conditions"][condition]["output_hash"],
            })

    schedule_hash = digest({
        "seed": seed,
        "algorithm": "cyclic-balanced-v1",
        "assignments": [
            {"assignment_id": row["assignment_id"], "participant_id": row["participant_id"], "masked_text_code": row["masked_text_code"], "order_position": row["order_position"]}
            for row in assignments
        ],
        "restricted_condition_mapping": restricted_mapping,
    })
    for row in assignments:
        row["schedule_hash"] = f"sha256:{schedule_hash}"

    return {
        "fixture_id": data["fixture_id"],
        "synthetic_only": True,
        "seed": seed,
        "algorithm": "cyclic-balanced-v1",
        "participant_count": len(participants),
        "eligible_material_count": len(eligible),
        "assignments": assignments,
        "restricted_condition_mapping": restricted_mapping,
        "schedule_hash": f"sha256:{schedule_hash}",
    }


def response_class(seed: int, assignment_id: str, condition: dict[str, Any]) -> str:
    value = unit(seed, "response", assignment_id)
    missing = condition["missing_probability"]
    uncertain = condition["uncertain_probability"]
    correct = condition["correct_probability"]
    if value < missing:
        return "missing"
    if value < missing + uncertain:
        return "uncertain"
    if value < missing + uncertain + correct:
        return "correct"
    return "incorrect"


def make_scoring(data: dict[str, Any], assignment_output: dict[str, Any]) -> dict[str, Any]:
    seed = data["design"]["seed"]
    materials = {m["material_id"]: m for m in data["materials"]}
    mapping = {row["assignment_id"]: row for row in assignment_output["restricted_condition_mapping"]}
    responses: list[dict[str, Any]] = []
    scores: list[dict[str, Any]] = []
    adjudications: list[dict[str, Any]] = []
    applied_exclusions: list[dict[str, Any]] = []

    exclusions_by_assignment = {item["assignment_id"]: item for item in data["planned_exclusions"]}

    for assignment in assignment_output["assignments"]:
        assignment_id = assignment["assignment_id"]
        restricted = mapping[assignment_id]
        material = materials[restricted["material_id"]]
        condition_label = restricted["condition"]
        condition = material["conditions"][condition_label]
        answer_class = response_class(seed, assignment_id, condition)
        response_id = assignment_id.replace("SYN-ASG", "SYN-RESP")
        excluded = exclusions_by_assignment.get(assignment_id)
        exclusion_code = excluded["code"] if excluded else "MISSING_RESPONSE" if answer_class == "missing" else None
        response = {
            "response_id": response_id,
            "assignment_id": assignment_id,
            "masked_text_code": assignment["masked_text_code"],
            "question_id": material["scoring_key"]["question_id"],
            "answer_class": answer_class,
            "response_value": None if answer_class == "missing" else f"synthetic-{answer_class}",
            "condition_identity_absent": True,
            "rule_metadata_absent": True,
            "completion_state": "technical_failure" if exclusion_code == "TECHNICAL_FAILURE" else "missing" if answer_class == "missing" else "complete",
            "mechanical_exclusion_code": exclusion_code,
        }
        responses.append(response)
        if exclusion_code:
            applied_exclusions.append({
                "response_id": response_id,
                "assignment_id": assignment_id,
                "code": exclusion_code,
                "frozen_mechanical_rule": True,
                "reason": excluded["reason"] if excluded else "synthetic missing response",
            })

        base_score = {"correct": 1.0, "uncertain": 0.5, "incorrect": 0.0, "missing": 0.0}[answer_class]
        scorer_a = base_score
        disagree = answer_class != "missing" and unit(seed, "disagreement", assignment_id) < 0.12
        scorer_b = (0.5 if base_score in {0.0, 1.0} else 1.0) if disagree else base_score
        for scorer_id, score_value, independent in (
            ("SYN-SCORER-A", scorer_a, False),
            ("SYN-SCORER-I", scorer_b, True),
        ):
            scores.append({
                "score_id": f"{response_id}-{scorer_id[-1]}",
                "response_id": response_id,
                "scorer_id": scorer_id,
                "independent_of_ariadline": independent,
                "condition_identity_absent": True,
                "editor_metadata_absent": True,
                "scoring_key_hash": material["scoring_key"]["key_hash"],
                "score": score_value,
                "critical_error": answer_class == "incorrect" and unit(seed, "critical", assignment_id) < condition["critical_error_probability"],
            })
        if scorer_a != scorer_b:
            adjudications.append({
                "response_id": response_id,
                "adjudicator_id": "SYN-ADJ-I",
                "independent_of_ariadline": True,
                "condition_identity_absent": True,
                "initial_scores": [scorer_a, scorer_b],
                "final_score": base_score,
                "reason": "synthetic deterministic adjudication",
            })

    return {
        "fixture_id": data["fixture_id"],
        "synthetic_only": True,
        "responses": responses,
        "scores": scores,
        "adjudications": adjudications,
        "planned_exclusions": data["planned_exclusions"],
        "applied_exclusions": applied_exclusions,
        "planned_deviations": data["planned_deviations"],
    }


def derive_disposition(summary: dict[str, Any]) -> str:
    if summary.get("s_preservation_failures", 0) > summary.get("p_preservation_failures", 0):
        return "stop"
    if summary.get("critical_preservation_failures", 0) > 0 and summary.get("s_critical_failures", 0) > summary.get("p_critical_failures", 0):
        return "stop"
    if summary.get("eligible_pairs", 0) < 6 or summary.get("analyzable_responses", 0) < 80:
        return "insufficient_evidence"
    advantage = summary.get("mean_score_S", 0) - summary.get("mean_score_P", 0)
    burden = summary.get("mean_burden_S", 0) - summary.get("mean_burden_P", 0)
    naturalness = summary.get("mean_naturalness_S", 0) - summary.get("mean_naturalness_P", 0)
    if advantage >= 0.08 and burden <= 1.0 and naturalness >= -0.25 and summary.get("unresolved_bias_flags", 0) == 0:
        return "continue"
    return "revise"


def make_analysis(data: dict[str, Any], assignments: dict[str, Any], scoring: dict[str, Any]) -> dict[str, Any]:
    materials = {m["material_id"]: m for m in data["materials"]}
    mapping = {row["assignment_id"]: row for row in assignments["restricted_condition_mapping"]}
    response_by_id = {r["response_id"]: r for r in scoring["responses"]}
    final_scores: dict[str, float] = {}
    score_groups: defaultdict[str, list[float]] = defaultdict(list)
    for score in scoring["scores"]:
        score_groups[score["response_id"]].append(score["score"])
    adjudicated = {a["response_id"]: a["final_score"] for a in scoring["adjudications"]}
    for response_id, values in score_groups.items():
        final_scores[response_id] = adjudicated.get(response_id, mean(values))

    by_condition: defaultdict[str, list[float]] = defaultdict(list)
    critical_by_condition: Counter[str] = Counter()
    exposure_by_material_condition: Counter[tuple[str, str]] = Counter()
    missing_by_condition: Counter[str] = Counter()
    exclusions_by_condition: Counter[str] = Counter()

    for response_id, final_score in final_scores.items():
        response = response_by_id[response_id]
        restricted = mapping[response["assignment_id"]]
        condition = restricted["condition"]
        exposure_by_material_condition[(restricted["material_id"], condition)] += 1
        if response["answer_class"] == "missing":
            missing_by_condition[condition] += 1
        if response["mechanical_exclusion_code"]:
            exclusions_by_condition[condition] += 1
            continue
        by_condition[condition].append(final_score)
        if any(s["critical_error"] for s in scoring["scores"] if s["response_id"] == response_id):
            critical_by_condition[condition] += 1

    eligible_materials = [m for m in data["materials"] if eligible_pair(m)]
    mean_burden = {
        label: mean(m["conditions"][label]["burden_minutes"] for m in eligible_materials)
        for label in ("P", "S")
    }
    mean_naturalness = {
        label: mean(m["conditions"][label]["naturalness"] for m in eligible_materials)
        for label in ("P", "S")
    }
    adverse_items = [
        {
            "material_id": m["material_id"],
            "scenario_class": m["scenario_class"],
            "P_preservation": m["conditions"]["P"]["preservation"],
            "S_preservation": m["conditions"]["S"]["preservation"],
            "S_worse_probability": m["conditions"]["S"]["correct_probability"] < m["conditions"]["P"]["correct_probability"],
            "bias_flags": m.get("bias_flags", []),
            "rule_ids": m.get("candidate_rule_ids", []),
            "applicability_agreement": m.get("applicability_agreement"),
        }
        for m in data["materials"]
        if m["scenario_class"] in {"adverse_S", "inconclusive"}
        or not eligible_pair(m)
        or m.get("bias_flags")
    ]

    summary = {
        "eligible_pairs": len(eligible_materials),
        "participant_count": data["design"]["participant_count"],
        "assignment_count": len(assignments["assignments"]),
        "analyzable_responses": sum(len(values) for values in by_condition.values()),
        "mean_score_P": round(mean(by_condition["P"]), 4),
        "mean_score_S": round(mean(by_condition["S"]), 4),
        "mean_burden_P": round(mean_burden["P"], 3),
        "mean_burden_S": round(mean_burden["S"], 3),
        "mean_naturalness_P": round(mean_naturalness["P"], 3),
        "mean_naturalness_S": round(mean_naturalness["S"], 3),
        "p_critical_failures": critical_by_condition["P"],
        "s_critical_failures": critical_by_condition["S"],
        "p_preservation_failures": sum(m["conditions"]["P"]["preservation"] == "not_preserved" for m in data["materials"]),
        "s_preservation_failures": sum(m["conditions"]["S"]["preservation"] == "not_preserved" for m in data["materials"]),
        "critical_preservation_failures": sum(
            m["conditions"][label]["preservation"] == "not_preserved"
            for m in data["materials"] for label in ("P", "S")
        ),
        "applicability_agreement_rate": round(mean(1.0 if m.get("applicability_agreement") else 0.0 for m in eligible_materials), 4),
        "missing_P": missing_by_condition["P"],
        "missing_S": missing_by_condition["S"],
        "excluded_P": exclusions_by_condition["P"],
        "excluded_S": exclusions_by_condition["S"],
        "unresolved_bias_flags": sum(bool(m.get("bias_flags")) for m in data["materials"]),
    }
    mock_disposition = derive_disposition(summary)

    disposition_scenarios = [
        {"scenario": "continue", "expected": "continue", "derived": derive_disposition({"eligible_pairs": 10, "analyzable_responses": 130, "mean_score_P": 0.60, "mean_score_S": 0.72, "mean_burden_P": 8.0, "mean_burden_S": 8.5, "mean_naturalness_P": 4.0, "mean_naturalness_S": 3.9, "p_preservation_failures": 0, "s_preservation_failures": 0, "critical_preservation_failures": 0, "p_critical_failures": 0, "s_critical_failures": 0, "unresolved_bias_flags": 0})},
        {"scenario": "revise", "expected": "revise", "derived": derive_disposition({"eligible_pairs": 9, "analyzable_responses": 120, "mean_score_P": 0.65, "mean_score_S": 0.68, "mean_burden_P": 8.0, "mean_burden_S": 11.0, "mean_naturalness_P": 4.1, "mean_naturalness_S": 3.5, "p_preservation_failures": 0, "s_preservation_failures": 0, "critical_preservation_failures": 0, "p_critical_failures": 0, "s_critical_failures": 0, "unresolved_bias_flags": 1})},
        {"scenario": "stop", "expected": "stop", "derived": derive_disposition({"eligible_pairs": 8, "analyzable_responses": 110, "mean_score_P": 0.70, "mean_score_S": 0.58, "mean_burden_P": 8.0, "mean_burden_S": 12.0, "mean_naturalness_P": 4.2, "mean_naturalness_S": 3.1, "p_preservation_failures": 0, "s_preservation_failures": 2, "critical_preservation_failures": 2, "p_critical_failures": 0, "s_critical_failures": 2, "unresolved_bias_flags": 2})},
        {"scenario": "insufficient_evidence", "expected": "insufficient_evidence", "derived": derive_disposition({"eligible_pairs": 4, "analyzable_responses": 50, "mean_score_P": 0.60, "mean_score_S": 0.72, "mean_burden_P": 8.0, "mean_burden_S": 8.5, "mean_naturalness_P": 4.0, "mean_naturalness_S": 3.9, "p_preservation_failures": 0, "s_preservation_failures": 0, "critical_preservation_failures": 0, "p_critical_failures": 0, "s_critical_failures": 0, "unresolved_bias_flags": 0})},
    ]

    validation = validate_outputs(data, assignments, scoring, summary, disposition_scenarios)
    return {
        "fixture_id": data["fixture_id"],
        "synthetic_only": True,
        "evidence_claim": "procedure_only",
        "summary": summary,
        "mock_disposition": mock_disposition,
        "adverse_and_inconclusive_items": adverse_items,
        "exposure_by_material_condition": [
            {"material_id": material_id, "condition": condition, "count": count}
            for (material_id, condition), count in sorted(exposure_by_material_condition.items())
        ],
        "disposition_scenarios": disposition_scenarios,
        "validation": validation,
        "non_generalization": "Synthetic operational output only; not evidence of Ariadline effectiveness, safety, or representativeness.",
    }


def validate_outputs(
    data: dict[str, Any],
    assignments: dict[str, Any],
    scoring: dict[str, Any],
    summary: dict[str, Any],
    disposition_scenarios: list[dict[str, str]],
) -> dict[str, Any]:
    findings: list[dict[str, str]] = []
    assignment_rows = assignments["assignments"]
    restricted = assignments["restricted_condition_mapping"]
    restricted_by_assignment = {row["assignment_id"]: row for row in restricted}

    by_participant: defaultdict[str, list[str]] = defaultdict(list)
    for row in restricted:
        by_participant[next(a["participant_id"] for a in assignment_rows if a["assignment_id"] == row["assignment_id"])].append(row["material_id"])
    require(all(len(items) == len(set(items)) for items in by_participant.values()), "DUPLICATE_MEANING_EXPOSURE", "participant saw both or duplicate underlying record", findings)

    materials = {m["material_id"]: m for m in data["materials"]}
    require(all(eligible_pair(materials[row["material_id"]]) for row in restricted), "INELIGIBLE_EXPOSURE", "ineligible pair entered assignment", findings)

    counts = Counter((row["material_id"], row["condition"]) for row in restricted)
    balance_ok = True
    for material_id in {row["material_id"] for row in restricted}:
        if abs(counts[(material_id, "P")] - counts[(material_id, "S")]) > 1:
            balance_ok = False
    require(balance_ok, "CONDITION_IMBALANCE", "P/S exposure differs by more than one for a material", findings)

    domain_counts = Counter(row["domain_family"] for row in assignment_rows)
    eligible_domain_materials = Counter(m["domain_family"] for m in data["materials"] if eligible_pair(m))
    normalized_domain_exposure = {
        domain: domain_counts[domain] / eligible_domain_materials[domain]
        for domain in eligible_domain_materials
    }
    require(max(normalized_domain_exposure.values()) - min(normalized_domain_exposure.values()) <= 1, "DOMAIN_IMBALANCE", "domain exposure per eligible material is not acceptably balanced", findings)

    assignment_ids = {row["assignment_id"] for row in assignment_rows}
    require(all(r["assignment_id"] in assignment_ids for r in scoring["responses"]), "RESPONSE_ASSIGNMENT_TRACE", "response lacks assignment", findings)
    require(all(s["response_id"] in {r["response_id"] for r in scoring["responses"]} for s in scoring["scores"]), "SCORE_RESPONSE_TRACE", "score lacks response", findings)
    require(all(r["condition_identity_absent"] and r["rule_metadata_absent"] for r in scoring["responses"]), "RESPONSE_MASKING", "response packet leaked condition or rule metadata", findings)
    require(all(s["condition_identity_absent"] and s["editor_metadata_absent"] for s in scoring["scores"]), "SCORER_MASKING", "scorer packet leaked restricted metadata", findings)
    require(any(s["independent_of_ariadline"] for s in scoring["scores"]), "INDEPENDENT_SCORER", "no independent scorer", findings)

    for row in restricted:
        material = materials[row["material_id"]]
        require(material["scoring_key"]["meaning_record_id"] == row["meaning_record_id"], "ANSWER_KEY_TRACE", "answer key does not trace to meaning record", findings)

    adverse = [m for m in data["materials"] if not eligible_pair(m)]
    require(bool(adverse) and all(m.get("adverse_record_retained") for m in adverse), "ADVERSE_RETENTION", "preservation adverse record hidden", findings)
    require(all(e["code"] in MECHANICAL_EXCLUSION_CODES and e.get("frozen_mechanical_rule") is True for e in scoring["applied_exclusions"]), "MECHANICAL_EXCLUSIONS", "non-mechanical exclusion used", findings)
    require({"correct", "incorrect", "uncertain", "missing"} <= {r["answer_class"] for r in scoring["responses"]}, "RESPONSE_CLASS_COVERAGE", "correct, incorrect, uncertain, and missing responses are all required", findings)
    require(all(item.get("material_id") and item.get("rule_ids") for item in [
        {"material_id": m["material_id"], "rule_ids": m.get("candidate_rule_ids", [])}
        for m in data["materials"] if m["scenario_class"] in {"adverse_S", "inconclusive"} or not eligible_pair(m) or m.get("bias_flags")
    ]), "QUALITATIVE_TRACEABILITY", "qualitative failures must link exact materials and rules", findings)
    require(all(item["derived"] == item["expected"] for item in disposition_scenarios), "DISPOSITION_BRANCHES", "continue/revise/stop/insufficient route failed", findings)
    require(summary["participant_count"] == data["design"]["participant_count"], "PARTICIPANT_COUNT", "participant count mismatch", findings)
    require(data["evidence_claim"] == "procedure_only", "OVERCLAIM", "analysis overstates synthetic evidence", findings)

    checks = {
        "no_duplicate_meaning_exposure": not any(f["code"] == "DUPLICATE_MEANING_EXPOSURE" for f in findings),
        "condition_balance": not any(f["code"] == "CONDITION_IMBALANCE" for f in findings),
        "domain_balance": not any(f["code"] == "DOMAIN_IMBALANCE" for f in findings),
        "scoring_masked": not any(f["code"] == "SCORER_MASKING" for f in findings),
        "answer_key_traceability": not any(f["code"] == "ANSWER_KEY_TRACE" for f in findings),
        "preservation_failures_retained": not any(f["code"] == "ADVERSE_RETENTION" for f in findings),
        "mechanical_exclusions": not any(f["code"] == "MECHANICAL_EXCLUSIONS" for f in findings),
        "all_disposition_routes": not any(f["code"] == "DISPOSITION_BRANCHES" for f in findings),
        "small_pilot_boundary": not any(f["code"] == "OVERCLAIM" for f in findings),
        "ordinary_editing_can_outperform": any(m["conditions"]["P"]["correct_probability"] > m["conditions"]["S"]["correct_probability"] for m in data["materials"]),
        "inconclusive_case_retained": any(m["scenario_class"] == "inconclusive" for m in data["materials"]),
        "deviation_case_retained": bool(data["planned_deviations"]),
        "independent_scoring_route": not any(f["code"] == "INDEPENDENT_SCORER" for f in findings),
    }
    return {
        "status": "pass" if not findings else "fail",
        "check_count": len(checks),
        "checks": checks,
        "findings": sorted(findings, key=lambda item: (item["code"], item["message"])),
    }


def build(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    source_findings = validate_source(data)
    if source_findings:
        raise ValueError(json.dumps({"status": "source_invalid", "findings": source_findings}, indent=2))
    assignments = make_assignments(data)
    scoring = make_scoring(data, assignments)
    analysis = make_analysis(data, assignments, scoring)
    if analysis["validation"]["status"] != "pass":
        raise ValueError(json.dumps({"status": "output_invalid", "validation": analysis["validation"]}, indent=2))
    return {
        "assignments.json": assignments,
        "scoring_and_adjudication.json": scoring,
        "analysis.json": analysis,
    }


def write_outputs(outputs: dict[str, dict[str, Any]], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for filename, value in outputs.items():
        (output_dir / filename).write_text(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")


def compare_expected(outputs: dict[str, dict[str, Any]], expected_dir: Path) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for filename in OUTPUT_FILES:
        expected_path = expected_dir / filename
        if not expected_path.exists():
            findings.append({"code": "EXPECTED_OUTPUT_MISSING", "message": filename})
            continue
        expected = json.loads(expected_path.read_text(encoding="utf-8"))
        if expected != outputs[filename]:
            findings.append({"code": "OUTPUT_MISMATCH", "message": filename})
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--expect-dir", type=Path)
    args = parser.parse_args()

    data = json.loads(args.source.read_text(encoding="utf-8"))
    try:
        outputs = build(data)
    except ValueError as exc:
        print(str(exc))
        return 2

    if args.output_dir:
        write_outputs(outputs, args.output_dir)

    comparison = compare_expected(outputs, args.expect_dir) if args.expect_dir else []
    status = "expected_outputs_matched" if args.expect_dir and not comparison else "generated" if not comparison else "self_test_failed"
    result = {
        "status": status,
        "fixture_id": data["fixture_id"],
        "output_hashes": {name: f"sha256:{digest(value)}" for name, value in outputs.items()},
        "validation": outputs["analysis.json"]["validation"],
        "mock_disposition": outputs["analysis.json"]["mock_disposition"],
        "comparison_findings": comparison,
        "synthetic_only": True,
        "evidence_claim": "procedure_only",
    }
    print(json.dumps(result, indent=2))
    return 0 if not comparison else 2


if __name__ == "__main__":
    raise SystemExit(main())
