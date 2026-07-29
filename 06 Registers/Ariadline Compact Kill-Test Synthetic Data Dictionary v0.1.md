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

This dictionary describes only the fictional issue #45 dry-run source and exact expected fixtures. It does not define, approve, or freeze the human-study schema.

## Source fixture

The source fixture contains:

- `fixture_id`, `synthetic_only`, `study_state`, and `evidence_claim` boundary fields;
- a deterministic design record with seed, participant count, items per participant, domain families, conditions, and primary comparison;
- twelve fictional material and meaning records;
- paired fictional P and S condition parameters;
- scoring-key records tied explicitly to their material and meaning-record IDs;
- frozen synthetic exclusions and deviations;
- simulated-only human-gate states.

Each material record includes its exact `material_id`, `meaning_record_id`, domain, scenario class, candidate rule IDs, independent S-editor applicability IDs, comparability state, preservation states, burden and naturalness values, response probabilities, output hashes, and scoring key.

## Rich generated records

`run_compact_kill_test_dry_run.py` generates rich in-memory records before compaction.

### Assignment records

Each assignment contains:

- `assignment_id`;
- `participant_id`;
- `masked_text_code`;
- `order_position`;
- `domain_family`;
- schedule version and hash.

A separate restricted mapping contains the exact assignment, material, meaning-record, condition, and condition-output identities. The schedule hash covers the seed, algorithm, public assignment records, and restricted mapping.

### Response records

Each raw response contains:

- `response_id` and `assignment_id`;
- masked text, question, material, and meaning-record identities;
- answer class and response value;
- completion state;
- mechanical exclusion code where applicable;
- masking assertions.

All 144 assignments produce a raw response record. The seven mechanically excluded missing or technical-failure records remain visible but receive no score or adjudication rows.

### Score and adjudication records

Each analyzable response receives exactly two initial masked score records:

- one project-associated fictional scorer;
- one fictional scorer marked independent of Ariadline development.

Every score record includes the exact material, meaning-record, question, and scoring-key identities. Disagreements produce a deterministic independent adjudication while preserving both initial scores. The final fixture contains 137 analyzable responses, 274 initial score rows, and 23 adjudications.

### Exclusion and deviation records

Applied exclusions preserve response and assignment identity, frozen code, reason, and the fact that no score was emitted. Planned deviations remain linked to affected records and interpretation.

## Exact compact fixtures

`verify_compact_kill_test_dry_run.py` converts the rich generated objects into lossless compact fixtures and immediately round-trips them back to the rich objects before comparison.

### `assignments.json`

Contains:

- design metadata and schedule hash;
- a material manifest with exact meaning-record, domain, and P/S output hashes;
- participant schedules with explicit assignment ID, participant ID, order, material ID, meaning-record ID, condition, masked code, domain, and output hash.

No identifier is inferred from a numeric suffix.

### `scoring_and_adjudication.json`

Contains:

- masking assertions and scorer/adjudicator manifests;
- scoring-key manifest keyed by explicit material, meaning-record, question, and key-hash values;
- 144 explicit response entries;
- score pairs only for analyzable responses;
- adjudication fields only where initial scores disagree;
- planned and applied exclusions;
- planned deviations.

The compact verifier checks exact response, score, and adjudication counts; zero scoring for excluded responses; two initial scores per analyzable response; and one independent score per analyzable response and per question family.

### `analysis.json`

Contains:

- condition-level synthetic score, burden, naturalness, preservation, missingness, exclusion, applicability, and bias summaries;
- exact material and rule linkage for adverse and inconclusive cases;
- P/S exposure by eligible material;
- independent tests of continue, revise, stop, and insufficient-evidence routes;
- sixteen operational validation checks;
- the mandatory synthetic-only non-generalization statement.

## Exactness and boundary

The verifier requires:

1. source validation before generation;
2. rich-object validation before compaction;
3. compact-to-rich round-trip equality;
4. exact equality with each committed expected fixture;
5. matching canonical SHA-256 hashes.

No value identifies a real participant, editor, scorer, authority, community member, or authentic passage. Synthetic gate states and outputs cannot satisfy human issues #40, #42, #44, #46, or #48 and cannot be cited as evidence of Ariadline effectiveness or safety.