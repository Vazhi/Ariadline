---
title: "Ariadline Compact Kill-Test Synthetic Dry Run Validation v0.1"
type: validation-report
status: complete
version: "0.1"
created: 2026-07-29
updated: 2026-07-29
tags: [ariadline, validation, synthetic, dry-run]
---
# Ariadline Compact Kill-Test Synthetic Dry Run Validation v0.1

## Result

PASS — exact deterministic outputs match the committed expected fixtures and all 13 synthetic operational checks pass.

This PASS is limited to procedure, data integrity, and reproducibility. It is not human approval or authentic evidence.

## Exact-output check

- fixture: `ARIADLINE-COMPACT-DRY-RUN-0.1`;
- seed: `4501`;
- generated files: 3;
- hash mismatches: 0;
- validation findings: 0;
- mock disposition: `stop`.

Expected hashes:

- `assignments.json`: `sha256:16b99df65ae2a2e1bebcd7fcce2d14ad19b4634a8431374c75982c4d4dff0f4c`;
- `scoring_and_adjudication.json`: `sha256:5cae5fe6cea6b544a7c78c396692075c296eece01890dee9e02f1760ded5bc6f`;
- `analysis.json`: `sha256:6d02757f3f5607fffa4c10792bb9fce648c91d45ee54952caea7411f48fa9b83`.

## Checks

1. No participant receives both conditions of one meaning record.
2. Eligible material exposure is exactly balanced between P and S.
3. Domain exposure remains within the registered bound.
4. Scoring packets remain masked.
5. Every scoring key traces to one synthetic meaning record.
6. Preservation failures remain visible and cannot be hidden by aggregate scores.
7. Missingness and exclusions use frozen mechanical codes.
8. Continue, revise, stop, and insufficient-evidence branches all derive correctly.
9. The report preserves the small-pilot non-generalization boundary.
10. Ordinary editing can outperform S when the fixture specifies that outcome.
11. Inconclusive cases remain visible.
12. Deviation cases remain linked to affected records.
13. Every scored task family has an independent scoring route.

## Repaired defects

The validation record includes the seven development defects listed in [[Ariadline Compact Kill-Test Synthetic Dry Run Report v0.1]]. They were found before publication, repaired, and covered by the final exact-output test.

## Boundary checks

- no authentic passage is included;
- no real participant, editor, scorer, or authority is represented;
- every gate is simulated only;
- the study state remains synthetic rehearsal;
- the evidence claim remains `procedure_only`;
- no human issue or evaluation status is advanced;
- no synthetic threshold is treated as empirical.
