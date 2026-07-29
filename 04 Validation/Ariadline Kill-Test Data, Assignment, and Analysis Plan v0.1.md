---
title: "Ariadline Kill-Test Data, Assignment, and Analysis Plan v0.1"
type: evaluation-data-plan
status: planning-draft
version: "0.1"
created: 2026-07-29
updated: 2026-07-29
tags: [ariadline, evaluation, data, assignment, analysis]
---
# Ariadline Kill-Test Data, Assignment, and Analysis Plan v0.1

## Status and authority boundary

This document completes the compact planning package for issue #43. It is not a frozen protocol, preregistration, privacy approval, recruitment authorization, statistical approval, or permission to expose participants to materials.

Human issue #46 must approve or replace the data, assignment, exclusion, retention, accessibility, and analysis decisions before execution. The approved version and hash must be frozen before condition-labelled outcomes are inspected.

## Study question

Does the human-approved minimal Ariadline core produce an important advantage over competent ordinary expert editing (`P`) without increasing material meaning change, burden, unnaturalness, repetition, fragmentation, disagreement, or unresolved bias?

The primary publication-relevant contrast is `S` versus `P`. An optional authorized source condition `U` is descriptive and cannot replace that comparison.

## Information and data separation

Maintain at least six logically and access-separated record stores:

1. **Contact, consent, compensation, and withdrawal records** — directly identifying and accessible only to the approved participant-administration role.
2. **Participant key** — maps a random participant ID to contact records and remains separate from responses and analysis.
3. **Restricted material and authority records** — source passages, permissions, access restrictions, authorized meaning records, authority contacts, and protected context.
4. **Restricted administrative mappings** — P/S identities, editor identities, rule-applicability mappings, assignment codes, randomization keys, action logs, and unmasking keys.
5. **De-identified research records** — masked assignments, responses, scores, preservation results, timing, exclusions, and deviations using random IDs only.
6. **Analysis and release records** — a minimized analysis dataset and either approved de-identified data or publishable aggregates after disclosure and permission review.

Direct identifiers must not appear in response, scoring, preservation, assignment, or analysis tables.

## Identifier rules

Use random identifiers that do not encode institution, country, language, role, recruitment source, condition, health status, or accessibility need.

Recommended namespaces:

- participant: `ARI-PART-<random>`;
- material: `ARI-MAT-<sequence>`;
- meaning record: `ARI-MEAN-<sequence>-v<version>`;
- condition output: `ARI-COND-<random>`;
- masked text: `ARI-MASK-<random>`;
- assignment: `ARI-ASG-<random>`;
- response: `ARI-RESP-<random>`;
- score: `ARI-SCORE-<random>`;
- deviation: `ARI-DEV-<sequence>`.

Public or analysis identifiers must not permit reconstruction of the restricted condition or participant key without the separately held mapping.

## Minimum record tables

### Participant table

| Field | Requirement |
|---|---|
| `participant_id` | random study ID |
| `eligibility_state` | eligible, ineligible, not determined |
| `consent_state` | approved coded state; consent form stored separately |
| `primary_domain_band` | broad registered practice or method family |
| `secondary_experience_bands` | minimized coded experience |
| `editing_experience_band` | registered ordinal band |
| `scholarly_language_band` | broad category or suppressed when identifying |
| `ariadline_contributor` | yes/no |
| `canto_span_contributor` | yes/no |
| `accessibility_state` | accommodation supplied, unmet, none, or prefer not to state; details restricted |
| `completion_state` | complete, partial, withdrawn, technical failure, excluded |
| `exclusion_code` | frozen mechanical code or none |

Rare combinations must be coarsened or suppressed before public release.

### Material and condition table

| Field | Requirement |
|---|---|
| `material_id` | registered authentic material ID |
| `source_version` | immutable locator or hash |
| `meaning_record_id` | approved meaning-record version |
| `permission_state` | approved coded state; evidence restricted |
| `domain_family` | registered broad stratum |
| `neutral_risk_version` | frozen shared communication-risk brief |
| `condition_output_id` | immutable P or S output record |
| `condition_mapping` | restricted until authorized unmasking |
| `editor_id` | restricted random editor ID |
| `output_hash` | exact immutable output hash |
| `preservation_state` | preserved, not preserved, not determined |
| `pair_eligibility` | eligible, excluded, not determined with reason |

### Assignment table

| Field | Requirement |
|---|---|
| `assignment_id` | unique masked assignment |
| `participant_id` | random participant ID |
| `masked_text_code` | reader-facing text identity |
| `material_id` | restricted or analysis-layer material link |
| `order_position` | presentation position |
| `domain_family` | broad balance stratum |
| `schedule_version` | frozen schedule identifier |
| `schedule_hash` | exact frozen schedule hash |
| `completion_state` | assigned, started, completed, skipped, withdrawn, technical failure |

Condition identity remains outside the reader-facing assignment record until registered unmasking.

### Response and timing table

| Field | Requirement |
|---|---|
| `response_id` | unique response record |
| `assignment_id` | assignment link |
| `question_id` | frozen task identifier |
| `response_type` | categorical, numeric, text, confidence, or `not determined` |
| `response_value` | minimized response or restricted locator |
| `response_time_ms` | elapsed time under the approved timing policy |
| `completion_state` | complete, skipped, interrupted, technical failure |
| `accommodation_applied` | coded state without medical detail |

Free text must undergo disclosure review before release.

### Scoring table

| Field | Requirement |
|---|---|
| `score_id` | unique scoring record |
| `response_id` | masked response link |
| `scorer_id` | random scorer ID |
| `scoring_key_version` | frozen version and hash |
| `score` | frozen categorical or numeric result |
| `error_class` | registered class including unsupported inference or material misinterpretation |
| `condition_masked` | yes/no/not determined |
| `adjudication_required` | yes/no |
| `adjudicated_result` | final result where applicable |

Initial scores must remain available so agreement and adjudication effects can be reported.

### Editor and preservation table

| Field | Requirement |
|---|---|
| `condition_output_id` | immutable output link |
| `editor_id` | restricted random editor ID |
| `condition_role` | restricted P/S mapping |
| `editing_time_ms` | elapsed editing time under approved policy |
| `action_log_version` | restricted frozen log |
| `reviewer_id` | random preservation-reviewer ID |
| `preservation_dimension` | registered meaning dimension |
| `preservation_result` | preserved, not preserved, not determined, not applicable |
| `severity` | critical, major, minor, editorial, not applicable |
| `adjudication_state` | not required, pending, complete |

A material unresolved difference remains `not determined`; it must not be promoted to preserved.

### Exclusion and deviation table

| Field | Requirement |
|---|---|
| `record_id` | exclusion or deviation ID |
| `record_type` | exclusion or deviation |
| `date` | recorded date |
| `study_phase` | setup, editing, preservation, assignment, recruitment, collection, scoring, analysis |
| `affected_scope` | participants, materials, conditions, assignments, tasks, outcomes |
| `frozen_code` | registered code or `unregistered` |
| `reason` | factual bounded reason |
| `outcome_data_visible` | yes/no/not determined |
| `corrective_action` | action or none |
| `eligibility_effect` | none, exclude, sensitivity-only, not determined |
| `interpretive_effect` | bounded effect on analysis or disposition |
| `responsible_role` | approved role, not a personal identifier in public records |

The original frozen record must remain available after any amendment.

## Assignment and counterbalancing

The approved assignment schedule must satisfy all of the following:

- each participant sees no more than one wording condition for a given meaning record;
- both P and S receive exposure for every eligible retained material unless a frozen design states an explicit reason otherwise;
- P/S exposure is balanced by material, broad domain family, and order position as closely as the approved sample permits;
- each participant receives a feasible mix across the registered domain families without repeated underlying meaning records;
- condition sequences are randomized or counterbalanced under a frozen algorithm, seed, schedule, and hash;
- participant replacement or late assignment follows a frozen rule and does not use condition-labelled outcomes;
- assignment changes after exposure begins are versioned deviations;
- accommodations may alter approved presentation or timing without being treated as inferior performance.

The final schedule and sample target require human statistical and operational approval under issue #46.

## Editor assignment and contamination controls

- Different editors must produce P and S for the same meaning record.
- An editor must not see the other condition's output, action log, preservation result, reader task answer, or participant result.
- An editor may work in both conditions only across different meaning records under a frozen cross-record counterbalancing plan.
- Editor expertise, language background, domain familiarity, prior Ariadline exposure, timing, and resources must be matched or recorded.
- The coordinator's preregistered applicability mapping remains hidden from both editors.
- The S editor records an independent applicability judgment; P does not receive the candidate-core rules.

## Mechanical exclusion rules

Freeze exact exclusion codes before participant exposure. Exclusions may use only objective registered conditions such as:

- ineligible or unapproved consent state;
- duplicate or prohibited repeat participation;
- prohibited duplicate exposure to one meaning record;
- withdrawal under the approved policy;
- technical failure that prevents presentation or response capture;
- missing response beyond the frozen analyzability rule;
- failed masking or assignment integrity;
- condition comparability failure;
- preservation state `not preserved` or `not determined` for the relevant P/S pair;
- outcome-visible protocol deviation that invalidates the registered comparison.

Do not exclude a participant, response, material, condition, editor, or scorer because it:

- favors P;
- criticizes Ariadline;
- reports confusion, burden, unnaturalness, bias, or inaccessibility;
- selects `not determined`;
- creates a null, adverse, mixed, stop, or reconception result;
- disagrees with the expected rule applicability or project interpretation.

Unregistered exclusions must be reported as deviations and analyzed separately rather than silently treated as planned.

## Analysis boundary

### Primary comparison

Use masked `S` versus `P` as the primary contrast. Register no more than three primary outcomes before launch. Meaning-preservation failure remains a safety outcome and cannot be traded for reader benefit.

### Candidate outcomes

Objective or rule-bound outcomes may include:

- principal claim reconstruction;
- claim-scope reconstruction;
- identification of supporting evidence or recorded result;
- identification of a material limitation or uncertainty;
- unsupported inference;
- material misinterpretation.

Supporting outcomes include editing and response time, naturalness, cohesion, repetition, fragmentation, burden, reviewer agreement, `not determined` frequency, applicability agreement, and qualitative theory, method, language, community, translation, and accessibility concerns.

### Small-pilot interpretation

This 20–30-person planning range is not automatically powered for precise population estimates or small effects. The human-approved analysis must:

- report item-level and rule-level results before aggregate conclusions;
- show uncertainty and missingness;
- retain adverse cases and P successes;
- distinguish descriptive patterns from registered inferential claims;
- avoid manufacturing numerical thresholds unsupported by the design;
- avoid treating subjective clarity ratings as comprehension;
- preserve initial scorer judgments and disagreement;
- avoid generalizing from tested passages or participants to linguistics as a whole.

### Decision classes

Distinguish:

1. **Hard safety failure** — a registered critical or major meaning-preservation failure, prohibited contamination, invalid authority or permission, or another approved non-compensable failure.
2. **Descriptive warning** — a material adverse pattern in burden, naturalness, cohesion, repetition, fragmentation, applicability agreement, bias, accessibility, or P superiority that requires human interpretation.
3. **Insufficient evidence** — too few eligible materials, participants, exposures, applicable rule instances, reliable scores, or uncontaminated comparisons to answer the registered question.

Apply [[Ariadline Kill-Test Decision Matrix v0.1]]. Valid project routes remain continue, revise or reconceive, stop as a controlled language, and insufficient evidence. Only human issue #48 may select the final project disposition.

## Masking and unmasking

Reader, scorer, preservation-reviewer, and adjudicator packets must exclude condition labels, expected direction, editor identity, rule-action logs, and unneeded authority metadata.

Unmask only under the frozen sequence after:

- response collection is complete for the relevant frozen scope;
- scoring and adjudication are frozen;
- exclusions and deviations are recorded without condition-labelled outcome-driven changes;
- the approved analysis role authorizes access.

Every unmasking event must record role, date, scope, purpose, and version.

## Retention, access, and release

Before recruitment, human issue #46 must approve:

- access roles for every store;
- encryption, backup, transfer, and incident-response requirements;
- retention and deletion periods;
- withdrawal limits after de-identification or aggregation;
- disclosure-risk review;
- community, source, publisher, and material restrictions;
- whether row-level de-identified data, restricted-access data, synthetic records, or aggregates may be released.

Publish no exact identifiers, rare combinations, restricted materials, authority contacts, unredacted free text, or condition keys unless the approved route permits them.

Every release must identify the protocol, material, condition, assignment, scoring-key, cleaning, exclusion, deviation, and analysis versions used.

## Non-generalization statement

The pilot evaluates a small approved candidate core on 10–12 authorized passages and approximately 20–30 participants under one frozen design. It cannot establish that Ariadline represents all linguistics, works across all languages or communities, validates any linguistic analysis, or warrants a universal standard. Null, mixed, harmful, infeasible, revise, stop, and insufficient-evidence outcomes are valid.