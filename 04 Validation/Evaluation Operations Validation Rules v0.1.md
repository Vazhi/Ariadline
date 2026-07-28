---
title: "Evaluation Operations Validation Rules v0.1"
type: validation-register
status: proposed-informative
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - sle
  - evaluation
  - validation
  - automation
---
# Evaluation Operations Validation Rules v0.1

## Authority

These checks are informative automation support for [[Evaluation Operations Dry-Run Package v0.1]]. They do not amend [[Multi-Domain Reader and Author Evaluation Protocol v0.1]], [[Evaluation Data Dictionary and Privacy Plan v0.1]], or human decisions under issues #30 through #35.

## Validation classes

| Code | Automated check | Human decision still required |
|---|---|---|
| `FORBIDDEN_IDENTIFIER_FIELD` | participant rows do not contain direct-identifier field names | disclosure risk and lawful data handling |
| `BROKEN_PARTICIPANT_FK` | trial or finding participant IDs resolve | participant eligibility and consent |
| `BROKEN_MATERIAL_FK` | conditions and trials resolve to registered materials | source permission and authority |
| `BROKEN_TRIAL_FK` | responses, scores, and preservation rows resolve | validity of the recorded response |
| `REQUIRED_CONDITION_MISSING` | registered P/S conditions exist | whether P and S are fair and meaning-preserving |
| `PROHIBITED_U_CONDITION` | U occurs only when `u_admissible=yes` | whether an authorized U baseline is justified |
| `DUPLICATE_MEANING_EXPOSURE` | one participant does not see multiple wording conditions for one meaning record | whether other contamination exists |
| `MASK_LEAK` | condition codes use opaque `MX###` form | whether wording or interface reveals condition |
| `SCORING_UNMASKED` | scoring records state masked review | whether masking was maintained in practice |
| `PRESERVATION_NOT_CONFIRMED` | confirmatory-ready P/S does not carry a non-preserved state | authentic preservation judgment |
| `NOT_DETERMINED_AS_SUCCESS` | `not determined` is not recoded as success | resolution or continued uncertainty |
| `POST_WITHDRAWAL_TRIAL` | no assignment occurs after recorded withdrawal | actual withdrawal handling |
| `CANTO_PARTICIPANT_CAP` | Canto-span contributor share is at most 10% | independence and recruitment fairness |
| `CANTO_TRIAL_CAP` | Canto-span trial share is at most 10% | interpretation of the bounded arm |
| `TASK_CONDITION_REGISTRATION` | publication tasks register P and S | task validity and estimand choice |
| `UNIVERSAL_U_REQUIREMENT` | U is not mandatory for every task | whether U is useful for a specific task |

## Expected fixtures

The valid fixture must produce zero findings.

The intentionally invalid fixture must exercise at least:

- direct identifier leakage;
- missing foreign keys;
- duplicate meaning exposure;
- prohibited U use;
- mask leakage;
- missing P or S registration;
- invalid preservation readiness;
- `not determined` converted to success;
- post-withdrawal assignment;
- Canto-span cap violations.

The expected-code file verifies coverage. Extra findings are allowed when one injected fault causes more than one valid diagnostic.

## Severity

Automation findings are pipeline diagnostics, not participant harms or research conclusions.

Suggested operational severity:

- blocker: broken IDs, direct identifier fields, prohibited U, missing P/S, mask leak, post-withdrawal trial;
- major: invalid preservation readiness, Canto-span cap violation, repeated meaning exposure;
- warning: imbalance or non-critical metadata omission;
- informational: synthetic-only notices.

A human must decide whether a real-study finding requires exclusion, repair, deviation reporting, suspension, or a new issue.

## Exit behavior

`validate_dry_run.py` returns:

- `0` for a valid fixture;
- `1` when unanticipated findings exist without an expected-code comparison;
- `0` when all expected invalid codes are detected;
- `2` when the intentionally invalid fixture fails to trigger one or more expected codes.

A passing expected-invalid run means only that the validator detected its test faults.
