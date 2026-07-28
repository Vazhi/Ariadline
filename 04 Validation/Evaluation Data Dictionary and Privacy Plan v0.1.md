---
title: "Evaluation Data Dictionary and Privacy Plan v0.1"
type: evaluation-data-plan
status: preparation
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - ariadline
  - evaluation
  - data
  - privacy
---
# Evaluation Data Dictionary and Privacy Plan v0.1

## Purpose

This plan defines the minimum research records for [[Multi-Domain Reader and Author Evaluation Protocol v0.1]] and the boundary between internal identifying records and publishable study data.

It is not a substitute for applicable institutional, legal, ethics, accessibility, community, or data-protection review.

## Data separation

Maintain separate stores for:

1. **contact and consent records** — identifying and access-controlled;
2. **participant key** — maps a random study ID to contact records and is stored separately;
3. **research responses** — uses study IDs only;
4. **material permissions and authority records** — may contain restricted source information;
5. **analysis dataset** — minimized and de-identified;
6. **publishable dataset or aggregate** — reviewed for disclosure risk and permission.

Do not place direct identifiers in the response dataset.

## Participant identifier

Use a random identifier such as `SLE-PART-8F3K2` that does not encode institution, country, language, role, or recruitment source.

A participant key is not published and is deleted or retained only under the approved retention plan.

## Participant table

Required fields:

| Field | Description |
|---|---|
| `participant_id` | random study identifier |
| `study_phase` | pilot, reader, review, authoring, translation, or full-document |
| `primary_stratum` | `PG-DESC`, `PG-THEORY`, `PG-EMP`, `PG-COMP`, or `PG-EDIT` |
| `secondary_experience` | bounded multi-select experience codes |
| `career_stage_band` | broad non-identifying band |
| `primary_scholarly_language_band` | coded language or protected broader category when disclosure risk exists |
| `professional_english_use` | predefined ordinal band |
| `sle_contributor` | yes or no |
| `canto_span_contributor` | yes or no |
| `controlled_language_experience` | predefined ordinal band |
| `translation_experience` | predefined ordinal band |
| `accessibility_accommodation` | none, provided category, unmet need, or prefer not to state |
| `consent_state` | eligible consent state without storing the form itself |
| `completion_state` | complete, withdrawn, technical failure, excluded, or partial |
| `exclusion_code` | preregistered code or none |

Rare combinations must be coarsened or suppressed before public release.

## Trial table

Required fields:

| Field | Description |
|---|---|
| `participant_id` | de-identified participant key |
| `trial_id` | unique trial record |
| `material_id` | registered material ID |
| `material_version` | frozen version or hash |
| `condition` | masked condition code during scoring; U, P, or S after unmasking |
| `task_type` | reconstruction, ambiguity, procedure, review, revision, drafting, translation, or full-document |
| `domain_family` | registered broad domain |
| `pattern_ids` | applicable pattern IDs |
| `rule_ids` | targeted rule IDs, not all rules that could be inferred later |
| `order_position` | presentation order |
| `response_started_at` | optional minimized timestamp or elapsed-time origin |
| `response_time_ms` | elapsed time under the timing policy |
| `completion_state` | complete, skipped, interrupted, or technical failure |
| `device_band` | broad interface category when relevant |
| `accommodation_applied` | coded accommodation state |

Do not publish exact timestamps when they increase re-identification risk without analytical value.

## Response table

Required fields depend on task:

| Field | Description |
|---|---|
| `trial_id` | trial key |
| `question_id` | frozen question identifier |
| `response_type` | selected, numeric, confidence, text, annotation, revision, or file reference |
| `response_value` | minimized response or coded value |
| `confidence` | frozen scale when collected |
| `self_reported_clarity` | frozen scale when collected |
| `self_reported_burden` | frozen scale when collected |
| `not_determined_selected` | yes or no where available |
| `participant_comment` | de-identified free text or restricted record |

Free-text responses require disclosure review before publication.

## Scoring table

| Field | Description |
|---|---|
| `trial_id` | trial key |
| `question_id` | scoring target |
| `scorer_id` | random scorer identifier |
| `scoring_key_version` | frozen key version |
| `score` | predefined numeric or categorical score |
| `error_class` | none, minor, material, unsupported inference, scope error, evidence-force error, or other frozen code |
| `adjudication_required` | yes or no |
| `adjudicated_score` | final score where applicable |
| `adjudication_reason` | coded or restricted text |
| `condition_masked` | confirms scorer masking state |

Preserve initial scores so disagreement is measurable.

## Authoring and preservation table

| Field | Description |
|---|---|
| `trial_id` | authoring trial key |
| `draft_version` | frozen participant output version |
| `meaning_record_id` | authorized brief or authentic authority record |
| `preservation_dimension` | polarity, quantification, scope, force, theory, method, data status, access, terminology, or normative force |
| `preservation_result` | preserved, changed, or not determined |
| `severity` | critical, major, minor, editorial, or not applicable |
| `independent_reviewer_id` | random reviewer ID |
| `source_author_confirmation` | yes, no, unavailable, or not applicable |
| `revision_time_ms` | elapsed authoring time under the timing policy |

A possible material unresolved change must remain `not determined`.

## Qualitative finding table

| Field | Description |
|---|---|
| `finding_id` | stable finding identifier |
| `participant_id` | de-identified key or suppressed for public reporting |
| `material_id` | related material |
| `rule_ids` | implicated rules |
| `finding_type` | helpful, neutral, harmful, biased, burdensome, oversimplifying, unclear, inaccessible, or other |
| `summary` | de-identified analytic summary |
| `verbatim_quote` | optional restricted quote with permission state |
| `domain_scope` | tested scope |
| `disposition` | rule review, material repair, task repair, no action, or follow-up issue |

## Protocol deviation table

Record every deviation with:

- deviation ID;
- date and study phase;
- affected participants, materials, conditions, and outcomes;
- reason;
- whether outcome data were visible;
- corrective action;
- effect on confirmatory status;
- responsible role.

The original protocol remains preserved.

## Restricted data

Treat as restricted unless explicitly authorized:

- names, emails, account identifiers, precise institutions, or exact locations;
- consent forms and signatures;
- rare combinations of language, community, role, and institution;
- community-controlled or access-restricted linguistic material;
- unpublished source drafts;
- contact details of source authors or translators;
- exact accessibility or health information;
- raw free text containing identifiable details.

## Publishable data rule

Publish row-level de-identified data only when:

- participant consent and oversight permit it;
- material permissions permit redistribution;
- disclosure review finds acceptable risk;
- rare categories are coarsened or suppressed;
- free text is redacted or withheld appropriately;
- community or source authority permits release;
- the release states its tested scope and limitations.

Otherwise publish aggregate tables, model summaries, codebooks, and synthetic examples.

## Retention and deletion

Before recruitment, define:

- retention periods for contact, key, raw, scored, and public data;
- who can access each store;
- encryption and backup expectations;
- withdrawal limits after de-identification or aggregation;
- destruction method;
- incident response and notification route.

Do not invent one universal retention period. Use the applicable approved plan.

## Data release versioning

Every release must identify:

- protocol version;
- material-register version;
- scoring-key version;
- analysis-plan version;
- data-cleaning version;
- exclusions and deviations;
- publication date;
- license or access terms;
- relation to the controlling Ariadline draft.

A released dataset does not become normative Ariadline evidence merely because it is public.
