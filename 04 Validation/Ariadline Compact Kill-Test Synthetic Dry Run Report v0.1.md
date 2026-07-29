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

The deterministic synthetic workflow completed and reproduced exactly. All 13 registered operational checks passed. The mock data produced a `stop` disposition because S had one synthetic material preservation failure while P had none. This is a procedure test, not an empirical finding.

## Generated records

- fictional meaning records: 12;
- domain families: 4;
- eligible P/S pairs: 9;
- retained ineligible pairs: 3;
- fictional participants: 24;
- assignments: 144;
- analyzable responses: 137;
- score rows: 288;
- adjudications: 24;
- applied exclusions: 7;
- response classes: 100 correct, 22 incorrect, 17 uncertain, 5 missing;
- completion states include one technical failure;
- condition exposure: 72 P and 72 S assignments.

## Balance and masking

Every participant received six unique underlying meaning records and never saw both conditions for one meaning record. Each eligible material received 16 exposures, split exactly eight P and eight S. The deterministic schedule covers four domain families and records seed, algorithm, schedule version, public assignments, restricted condition mappings, and a schedule hash.

Scorer packets exclude condition and editor metadata. Each response receives two synthetic initial scores, including one scorer marked independent of Ariadline development. Initial scores remain present after deterministic adjudication.

## Mechanical missingness and exclusions

Missing and technical-failure responses are not converted into zero comprehension scores. They receive frozen mechanical exclusion codes. The generated package contains five `MISSING_RESPONSE` records, one `TECHNICAL_FAILURE`, and one `FROZEN_MISSINGNESS_LIMIT` application.

Two planned deviations remain linked to their affected records and interpretation. Adverse conditions are retained even when their P/S pairs are ineligible for exposure or benefit analysis.

## Adverse and inconclusive cases

The source fixture contains:

- four `adverse_S` materials;
- three `inconclusive` materials;
- one S `not_preserved` condition;
- two S `not_determined` conditions;
- three unresolved bias flags;
- one deliberate applicability disagreement;
- multiple materials where ordinary editing is synthetically configured to outperform S.

Every qualitative adverse or inconclusive record remains linked to its exact material ID and candidate `SLE-RULE-*` IDs.

## Synthetic summary

| Measure | P | S |
|---|---:|---:|
| Mean synthetic score | 0.7121 | 0.8380 |
| Mean synthetic burden | 7.389 | 8.867 |
| Mean synthetic naturalness | 4.067 | 3.822 |
| Preservation failures | 0 | 1 |
| Missing responses | 4 | 1 |
| Excluded responses | 6 | 1 |

The higher aggregate S score does not hide the S preservation failure. The disposition function therefore returns `stop`, demonstrating that a hard safety failure cannot be outweighed by aggregate comprehension.

## Disposition route exercise

Four valid synthetic input patterns were evaluated independently:

- continue → `continue`;
- revise → `revise`;
- stop → `stop`;
- insufficient evidence → `insufficient_evidence`.

This proves only that the code can represent every permitted route.

## Defects found and repaired during development

1. The first assignment algorithm produced condition imbalance.
2. The first assignment algorithm produced unacceptable domain imbalance.
3. The first schedule hash omitted the restricted condition mapping.
4. Missing responses were initially counted as zero rather than excluded mechanically.
5. An S preservation failure did not initially trigger the hard-stop branch directly.
6. Qualitative adverse records initially lacked exact rule IDs.
7. The seed was initially recorded but did not affect assignment order.

The final outputs incorporate all seven repairs. No unresolved synthetic operational finding remains.

## Non-generalization

The numbers above are generated artifacts. They do not estimate an effect, validate a rule, justify a threshold, approve recruitment, establish preservation on authentic text, or support any conclusion about linguistics, Ariadline, authors, editors, or readers.
