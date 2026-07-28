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
- Validator: `tools/evaluation/validate_dry_run.py`

Every person, passage, response, score, finding, authority record, and deviation is fictional.

## Table coverage

The fixture includes:

- 20 fictional participant rows across the five planned strata;
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
- opaque condition masks;
- scorer masking;
- Canto-span participant share at 10%;
- Canto-span trial share below 10%;
- no direct identifier fields;
- no post-withdrawal trial;
- preserved synthetic P/S condition status where required;
- `not determined` retained for U.

These are structural demonstrations, not human findings.

## Invalid-fixture injections

The invalid fixture intentionally adds:

1. a direct identifier field;
2. excessive Canto-span contributor share;
3. a broken participant foreign key;
4. multiple wording-condition exposure;
5. prohibited U use in a revision task;
6. a condition-mask leak;
7. a missing required P condition;
8. a confirmatory-ready P condition with unresolved preservation;
9. `not determined` marked as success;
10. a post-withdrawal trial;
11. a broken scoring foreign key;
12. excessive Canto-span trial share.

`expected_invalid_codes.json` lists the required diagnostics.

## Non-evidence rule

Do not:

- calculate study effects from the fixture;
- use the fixture for a sample-size estimate;
- infer that real masking or accessibility will work;
- count fictional strata as participant coverage;
- treat synthetic preservation values as independent review;
- treat a validator pass as readiness for recruitment or publication.

The fixture can test data flow and failure detection only.
