---
title: "Evaluation Operations Validation Rules v0.1"
type: validation-register
status: proposed-informative
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - ariadline
  - evaluation
  - validation
  - automation
---
# Evaluation Operations Validation Rules v0.1

## Authority

These checks are informative automation support for [[Evaluation Operations Dry-Run Package v0.1]]. They do not amend [[Multi-Domain Reader and Author Evaluation Protocol v0.1]], [[Evaluation Data Dictionary and Privacy Plan v0.1]], or human decisions under issues #30 through #35.

## Validation families

The committed expected-code manifest lists all 34 validation classes exercised by the negative fixture.

### Evidence and privacy boundary

- `NOT_SYNTHETIC`
- `EVIDENCE_BOUNDARY`
- `AUTHENTICITY_BOUNDARY`
- `FORBIDDEN_IDENTIFIER_FIELD`

### Table, identifier, and foreign-key integrity

- `MISSING_TABLE_ROWS`
- `INVALID_PARTICIPANT_ID`
- `DUPLICATE_PARTICIPANT_ID`
- `INVALID_TRIAL_ID`
- `DUPLICATE_TRIAL_ID`
- `BROKEN_PARTICIPANT_FK`
- `BROKEN_MATERIAL_FK`
- `BROKEN_TRIAL_FK`
- `CONDITION_MEANING_MISMATCH`
- `MEANING_RECORD_MISMATCH`
- `DUPLICATE_DEVIATION_ID`

### Condition and exposure integrity

- `UNIVERSAL_U_REQUIREMENT`
- `TASK_CONDITION_REGISTRATION`
- `PROHIBITED_U_REGISTRATION`
- `REQUIRED_CONDITION_MISSING`
- `UNREGISTERED_TRIAL_CONDITION`
- `PROHIBITED_U_CONDITION`
- `DUPLICATE_MEANING_EXPOSURE`
- `CONDITION_IMBALANCE`
- `ORDER_IMBALANCE`

### Masking and scoring integrity

- `MASK_LEAK`
- `DUPLICATE_MASK_CODE`
- `MASK_CODE_MISMATCH`
- `SCORING_UNMASKED`

`MASK_CODE_MISMATCH` compares each trial’s opaque code with the exact code registered for that material and condition. A different valid-looking `MX###` value does not pass.

### Preservation and lifecycle integrity

- `PRESERVATION_NOT_CONFIRMED`
- `NOT_DETERMINED_AS_SUCCESS`
- `NOT_DETERMINED_DOWNGRADED`
- `POST_WITHDRAWAL_TRIAL`

### Bounded-arm integrity

- `CANTO_PARTICIPANT_CAP`
- `CANTO_TRIAL_CAP`

## Balance rule

For the synthetic valid fixture:

- each core material receives an equal or near-equal P/S allocation;
- the absolute P/S difference for one material is at most 1;
- the absolute P/S difference at one order position is at most 1;
- U rows are excluded from the P/S balance calculation;
- Canto-span rows remain separately capped.

These are fixture checks, not proof that a real schedule is statistically adequate.

## Expected fixtures

The valid fixture must produce zero findings.

The intentionally invalid fixture must trigger every code in `expected_invalid_codes.json`. The comparison is exact:

- a missing expected code fails the self-test;
- an unexpected code also fails the self-test;
- row-level finding counts may vary when one injected fault affects several records, but the distinct code set must remain exact.

## Severity

Automation findings are pipeline diagnostics, not participant harms or research conclusions.

Suggested operational severity:

- blocker: broken IDs, direct identifier fields, prohibited U, missing P/S, mask mismatch or leak, post-withdrawal trial;
- major: invalid preservation readiness, Canto-span cap violation, repeated meaning exposure, material or order imbalance;
- warning: non-critical metadata omission;
- informational: synthetic-only notices.

A human must decide whether a real-study finding requires exclusion, repair, deviation reporting, suspension, or a new issue.

## Exit behavior

`validate_dry_run.py` returns:

- `0` for a valid fixture with no expected-code comparison;
- `1` when findings exist without an expected-code comparison;
- `0` for an expected-invalid run only when actual and expected code sets match exactly;
- `2` when the expected-invalid run has a missing or unexpected code.

A passing expected-invalid run means only that the validator detected the exact synthetic fault classes registered for that fixture version.
