---
title: "Synthetic Evaluation Operations Fixture v0.1"
type: evaluation-fixture
status: synthetic-test-only
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - sle
  - evaluation
  - fixture
  - synthetic
---
# Synthetic Evaluation Operations Fixture v0.1

## Identity

- Valid fixture ID: `SLE-EVAL-DRY-RUN-VALID-0.1`
- Invalid fixture ID: `SLE-EVAL-DRY-RUN-INVALID-0.1`
- Generator seed: `20260728`
- Generator: `tools/evaluation/generate_dry_run.py`
- Reviewed layer: `tools/evaluation/dry_run_reviewed.py`
- Validator: `tools/evaluation/validate_dry_run.py`

Every person, passage, response, score, finding, authority record, and deviation is fictional.

## Table coverage

The fixture includes:

- 21 fictional participant rows across the five planned strata;
- 20 active fictional participants;
- one fictional withdrawn participant with no valid post-withdrawal trials;
- six constructed material records;
- task-specific U, P, and S condition records;
- deterministic assignment and trial rows;
- response rows;
- two fictional scorer rows per trial;
- preservation rows for revision and translation tasks;
- qualitative-finding rows;
- a protocol-deviation row.

The fixture is compatible with the fields in [[Evaluation Data Dictionary and Privacy Plan v0.1]] but is not a substitute for an approved real-data implementation.

## Valid-fixture constraints

The valid fixture demonstrates:

- P and S available for every publication-relevant synthetic task;
- U limited to one registered reader baseline;
- no repeated wording-condition exposure from one meaning record;
- exact agreement between each trial mask and the registered material-condition mask;
- P/S difference at most 1 for every material and order position;
- scorer masking;
- Canto-span contributor share below 10%;
- Canto-span trial share below 10%;
- no direct identifier fields;
- no post-withdrawal trial;
- synthetic P/S result values explicitly scoped to the fictional fixture;
- `not determined` retained for U.

These are structural demonstrations, not human findings.

## Invalid-fixture coverage

The invalid fixture intentionally exercises all 34 codes in `expected_invalid_codes.json`, including:

- false evidence and authenticity metadata;
- missing tables;
- invalid and duplicate identifiers;
- broken participant, material, and trial references;
- condition and trial meaning mismatches;
- universal or prohibited U registration and use;
- missing and unregistered conditions;
- duplicate meaning exposure;
- condition and order imbalance;
- mask leakage, duplicate masks, and registered-mask mismatch;
- unmasked scoring;
- invalid preservation readiness and uncertainty downgrading;
- post-withdrawal assignment;
- duplicate deviations;
- excessive Canto-span contributor and trial shares.

The expected-invalid command passes only when the actual distinct code set matches the 34-code manifest exactly.

## Non-evidence rule

Do not:

- calculate study effects from the fixture;
- use the fixture for a sample-size estimate;
- infer that real masking or accessibility will work;
- count fictional strata as participant coverage;
- treat synthetic preservation values as independent review;
- treat a validator pass as readiness for recruitment or publication.

The fixture can test data flow and failure detection only.
