---
title: "Ariadline Compact Kill-Test Synthetic Data Dictionary v0.1"
type: data-dictionary
status: synthetic-complete
version: "0.1"
created: 2026-07-29
updated: 2026-07-29
tags: [ariadline, evaluation, synthetic, data]
---
# Ariadline Compact Kill-Test Synthetic Data Dictionary v0.1

## Scope

This dictionary describes only the fictional dry-run fixtures and generated outputs. It does not define the final human-study schema.

## Source fixture

### Top-level fields

| Field | Meaning |
|---|---|
| `fixture_id` | Stable fictional package identifier. |
| `synthetic_only` | Must be `true`. |
| `study_state` | Must remain `synthetic_rehearsal`. |
| `evidence_claim` | Must remain `procedure_only`. |
| `human_gates_simulated_only` | Records that no human gate is actually approved. |
| `design` | Seed, participant count, assignments per participant, conditions, domain families, and primary comparison. |
| `materials` | Twelve fictional meaning and P/S condition records. |
| `planned_exclusions` | Frozen synthetic exclusion cases. |
| `planned_deviations` | Frozen synthetic deviation cases. |

### Material fields

| Field | Meaning |
|---|---|
| `material_id` | Fictional material identifier. |
| `meaning_record_id` | Fictional authorized-meaning record identifier. |
| `domain_family` | One of four broad synthetic strata. |
| `scenario_class` | Neutral, `adverse_S`, or `inconclusive`. |
| `synthetic_text` | Invented text; never authentic source material. |
| `authority_state` | Simulated state marker only. |
| `comparability` | Simulated P/S comparability state. |
| `bias_flags` | Fictional risk labels retained for reporting. |
| `candidate_rule_ids` | Coordinator-side candidate `SLE-RULE-*` mapping. |
| `s_editor_rule_ids` | Independent synthetic S-editor applicability judgment. |
| `applicability_agreement` | Whether the two synthetic mappings agree. |
| `adverse_record_retained` | Confirms adverse state remains represented. |
| `scoring_key` | Synthetic question, accepted answer class, and frozen hash. |
| `conditions` | P and S editor, packet, output, preservation, burden, naturalness, and response-probability records. |

## Assignment output

| Field | Meaning |
|---|---|
| `assignment_id` | Unique fictional assignment. |
| `participant_id` | Random fictional participant ID. |
| `masked_text_code` | Reader-facing code without condition identity. |
| `order_position` | Position within the six-item assignment. |
| `domain_family` | Broad synthetic stratum. |
| `schedule_version` | Deterministic schedule version. |
| `schedule_hash` | Hash covering seed, algorithm, public assignments, and restricted condition mapping. |
| `restricted_condition_mapping` | Separate mapping from masked code to material and P/S identity. |

## Scoring and adjudication output

### Response fields

| Field | Meaning |
|---|---|
| `response_id` | Unique fictional response. |
| `assignment_id` | Link to one assignment. |
| `masked_text_code` | Masked text identity. |
| `question_id` | Synthetic scoring-key link. |
| `answer_class` | `correct`, `incorrect`, `uncertain`, or `missing`. |
| `response_value` | Fictional response value. |
| `condition_identity_absent` | Masking assertion. |
| `rule_metadata_absent` | Masking assertion. |
| `completion_state` | `complete`, `missing`, or `technical_failure`. |
| `mechanical_exclusion_code` | Frozen code or null. |

### Score and adjudication fields

| Field | Meaning |
|---|---|
| `score_id` | Unique initial score. |
| `response_id` | Response link. |
| `scorer_id` | Fictional scorer identity. |
| `independent_of_ariadline` | Marks the independent scoring route. |
| `condition_identity_absent` | Scorer masking assertion. |
| `editor_metadata_absent` | Scorer masking assertion. |
| `scoring_key_hash` | Frozen key identity. |
| `score` | `0`, `0.5`, or `1`; excluded missing records do not enter analysis as zero. |
| `critical_error` | Synthetic critical-error marker. |
| `adjudications` | Deterministic resolution of initial scorer disagreement while retaining initial scores. |
| `applied_exclusions` | Frozen planned and mechanically generated exclusion applications. |

## Analysis output

| Field | Meaning |
|---|---|
| `summary` | Condition-level score, burden, naturalness, preservation, missingness, exclusion, applicability, and bias summaries. |
| `mock_disposition` | Procedure-only derived route for the actual fixture. |
| `adverse_and_inconclusive_items` | Exact material/rule linkage for qualitative cases. |
| `exposure_by_material_condition` | P/S exposure counts for each eligible material. |
| `disposition_scenarios` | Independent continue, revise, stop, and insufficient-evidence branch tests. |
| `validation` | Thirteen operational checks and any findings. |
| `non_generalization` | Mandatory synthetic-evidence boundary. |

## Privacy boundary

No value in this package identifies a real person or authentic source. The IDs deliberately resemble study IDs only to test workflow behavior.
