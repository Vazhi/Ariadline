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

This dictionary describes only the fictional dry-run source, rich generated records, and compact expected fixtures. It does not define the final human-study schema.

The core runner uses explicit row objects for validation and analysis. The exact expected assignment and scoring fixtures are losslessly compacted by participant to reduce repository size. The verifier reconstructs the relevant relationships through the declared derivation and column records before exact comparison.

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
| `scenario_class` | Benefit, neutral, `adverse_S`, or `inconclusive`. |
| `synthetic_text` | Invented text; never authentic source material. |
| `authority_state` | Simulated state marker only. |
| `comparability` | Simulated P/S comparability state. |
| `bias_flags` | Fictional risk labels retained for reporting. |
| `candidate_rule_ids` | Coordinator-side candidate `SLE-RULE-*` mapping. |
| `s_editor_rule_ids` | Independent synthetic S-editor applicability judgment. |
| `applicability_agreement` | Whether the two synthetic mappings agree. |
| `adverse_record_retained` | Confirms adverse state remains represented. |
| `scoring_key` | Synthetic question, accepted and prohibited elements, meaning-record link, and frozen hash. |
| `conditions` | P and S editor, output, preservation, burden, naturalness, and response-probability records. |

## Rich assignment records

The core generator creates one public assignment row and one restricted mapping row per exposure. The public row contains assignment, participant, masked text, order, domain, schedule version, and schedule hash. The restricted row links the assignment to material, meaning record, P/S identity, and output hash.

The schedule hash covers:

- deterministic seed and algorithm;
- public assignment identities and ordering;
- complete restricted condition mapping.

## Compact assignment fixture

| Field | Meaning |
|---|---|
| `material_columns` and `materials` | Manifest for the nine eligible materials: meaning record, domain, and P/S output hashes. |
| `entry_columns` | Declares participant-entry order: position, material, condition, and masked text code. |
| `participant_schedules` | Twenty-four participant records with six complete assignment entries each. |
| `derivation` | Declares how the unique assignment ID derives from participant number and order. |
| `schedule_hash` | Exact hash from the rich schedule, including restricted mapping. |

The compact fixture therefore retains all 144 assignment identities, participant links, masked codes, order positions, material and meaning identities, domains, conditions, output hashes, seed, algorithm, and schedule hash without repeating invariant fields in every row.

## Rich response, score, and adjudication records

The core generator creates:

- one masked response row per assignment;
- two initial masked score rows per response;
- one deterministic adjudication row when the initial scores differ;
- explicit planned and applied exclusion records;
- explicit planned deviation records.

Missing or mechanically excluded responses remain recorded but do not enter the analyzable score mean as zero.

## Compact scoring fixture

| Field | Meaning |
|---|---|
| `scoring_keys` | Material, question ID, and frozen scoring-key hash manifest. |
| `scorers` | Synthetic scorer IDs and independence states. |
| `adjudicator` | Synthetic independent adjudicator record. |
| `entry_columns` | Declares result order: response class/value, completion, exclusion, two scores, two critical-error states, and adjudicated result. |
| `participant_results` | Twenty-four result tapes with six entries each, ordered exactly as the assignment fixture. |
| `derivation` | Declares how assignment and response IDs derive and where masked code, material, and condition are recovered. |
| `planned_exclusions` and `applied_exclusions` | Frozen cases and exact affected assignment/response records. |
| `planned_deviations` | Exact fictional deviations retained for interpretation. |

The participant result tapes preserve all 144 responses, 288 initial scores, 24 adjudications, completion states, exclusions, critical-error states, key links, scorer independence, and masking assertions.

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
