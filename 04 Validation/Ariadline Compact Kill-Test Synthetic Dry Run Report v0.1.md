---
title: "Ariadline Compact Kill-Test Synthetic Dry Run Report v0.1"
type: evaluation-report
status: synthetic-complete
version: "0.1"
created: 2026-07-29
updated: 2026-07-29
tags: [ariadline, evaluation, synthetic, report]
---
# Ariadline Compact Kill-Test Synthetic Dry Run Report v0.1

## Result

The deterministic synthetic workflow completed and reproduced exactly. All 16 registered operational checks passed. The mock data produced a `stop` disposition because S had one synthetic material-preservation failure while P had none. This is a procedure test, not an empirical finding.

## Generated records

- fictional meaning records: 12;
- domain families: 4;
- eligible P/S pairs: 9;
- retained ineligible pairs: 3;
- fictional participants: 24;
- assignments and raw responses: 144;
- analyzable responses: 137;
- initial score rows: 274;
- adjudications: 23;
- applied mechanical exclusions: 7;
- response classes: 97 correct, 24 incorrect, 16 uncertain, and 7 missing;
- condition exposure: 72 P and 72 S assignments.

## Balance and masking

Every participant received six unique meaning records and never saw both conditions for one meaning record. Each eligible material received 16 exposures, split exactly eight P and eight S. Per-participant domain counts differ by no more than one.

The schedule hash covers the seed, algorithm, public assignment records, and restricted condition mapping. Reader-facing assignment records do not reveal condition identity.

Every analyzable response has exactly two initial score rows from distinct scorers, including one scorer independent of Ariadline development. A disagreement receives one independent adjudication. Every mechanically excluded response has zero score and adjudication rows.

## Mechanical missingness and exclusions

Missing and technical-failure responses are not converted into zero comprehension scores. The package contains five generated `MISSING_RESPONSE` records, one planned `TECHNICAL_FAILURE`, and one planned `FROZEN_MISSINGNESS_LIMIT` record. All seven remain visible as raw responses and applied exclusions but do not enter scoring or benefit analysis.

Two planned deviations remain linked to their affected assignment or material. Adverse conditions remain represented even when their P/S pairs are ineligible for exposure or benefit analysis.

## Adverse and inconclusive cases

The source fixture contains:

- four `adverse_S` materials;
- three `inconclusive` materials;
- one S `not_preserved` condition;
- two S `not_determined` conditions;
- three bias flags;
- one deliberate applicability disagreement;
- multiple materials where ordinary editing is configured to outperform S.

Every adverse or inconclusive record remains linked to its material ID, meaning-record ID, and candidate `SLE-RULE-*` IDs.

## Synthetic summary

| Measure | P | S |
|---|---:|---:|
| Mean synthetic score | 0.6970 | 0.8310 |
| Mean synthetic burden | 7.278 | 8.556 |
| Mean synthetic naturalness | 4.078 | 3.844 |
| Preservation failures | 0 | 1 |
| Missing responses | 6 | 1 |
| Excluded responses | 6 | 1 |

The higher aggregate S score does not compensate for the S preservation failure. The disposition function therefore returns `stop`, demonstrating the intended non-compensable safety route.

## Disposition-route exercise

Four valid synthetic input patterns were evaluated independently:

- continue → `continue`;
- revise → `revise`;
- stop → `stop`;
- insufficient evidence → `insufficient_evidence`.

This establishes only that every permitted route can be represented and derived by the procedure.

## Defects found and repaired

1. The first assignment algorithm produced condition imbalance.
2. The first assignment algorithm produced unacceptable domain imbalance.
3. The first schedule hash omitted the restricted condition mapping.
4. Missing and technical records initially received zero score rows.
5. An S preservation failure did not initially trigger the stop branch directly.
6. Qualitative adverse records initially lacked exact rule IDs.
7. The recorded seed initially did not affect assignment order.
8. The compact scoring fixture initially inferred material identity from a question-ID suffix.
9. Scorer independence was initially checked only at package level rather than per analyzable response and per question.
10. Narrative counts and hashes initially remained stale after scoring repairs.

All ten defects are repaired in the exact expected fixtures. No unresolved synthetic operational finding remains.

## Non-generalization

The numbers above are generated artifacts. They do not estimate an effect, validate a rule, justify a threshold, approve recruitment, establish preservation on authentic text, or support a conclusion about linguistics, Ariadline, authors, editors, or readers.
