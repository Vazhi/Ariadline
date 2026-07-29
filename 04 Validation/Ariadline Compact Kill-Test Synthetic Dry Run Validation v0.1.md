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

PASS — exact deterministic outputs match the committed expected fixtures, the compact representations reconstruct the declared assignment and scoring records, and all 16 synthetic operational checks pass.

This PASS is limited to procedure, data integrity, and reproducibility. It is not human approval or authentic evidence.

## Exact-output check

- fixture: `ARIADLINE-COMPACT-DRY-RUN-0.2`;
- seed: `4501`;
- generated compact files: 3;
- comparison findings: 0;
- validation findings: 0;
- mock disposition: `stop`.

Expected hashes:

- `assignments.json`: `sha256:44ed785714ea80084a2c5dd670bf25eec58a1576d0bf4ab0ff08ba378987cb88`;
- `scoring_and_adjudication.json`: `sha256:0a8222ec8811ce5de253c886163e2cffa5770f13cd71d394a0c07d7793c333d7`;
- `analysis.json`: `sha256:b334d8acc27b682ebe82cfee7a6eac9c3964cbdf403c715f80f39c767ab3d0b5`.

## Operational checks

1. The source fixture satisfies its synthetic-only schema and authority boundary.
2. No participant receives both conditions for one meaning record.
3. Eligible-material exposure is exactly balanced between P and S.
4. Per-participant domain exposure remains within the registered bound.
5. Scoring records remain masked.
6. Every scoring key traces explicitly to one material and meaning record.
7. Mechanically excluded responses receive no score or adjudication rows.
8. Every analyzable response receives exactly two distinct initial scoring routes.
9. Every analyzable response includes an independent scorer; every disagreement receives an independent adjudication.
10. Every represented question has an independent scoring route.
11. Missingness and exclusions use frozen mechanical codes and include all planned exclusions.
12. Preservation failures and adverse records remain linked to exact items and rules.
13. Continue, revise, stop, and insufficient-evidence branches derive correctly.
14. The small-pilot and synthetic-evidence boundaries remain explicit.
15. Ordinary editing can outperform S when the fixture specifies that outcome.
16. Inconclusive and deviation cases remain visible and linked.

## Count invariants

- raw responses: 144;
- applied exclusions: 7;
- analyzable responses: 137;
- initial scores: 274 = 137 × 2;
- excluded responses with score rows: 0;
- adjudications: 23, only where the two initial scores disagree.

## Repaired defects

The validation record covers the ten development and review defects listed in [[Ariadline Compact Kill-Test Synthetic Dry Run Report v0.1]]. They were repaired before this exact-head result.

## Boundary checks

- no authentic passage is included;
- no real participant, editor, scorer, or authority is represented;
- every authority or gate value is simulated only;
- the study state remains `synthetic_rehearsal`;
- the evidence claim remains `procedure_only`;
- no human issue or evaluation status is advanced;
- no synthetic threshold is treated as empirical.
