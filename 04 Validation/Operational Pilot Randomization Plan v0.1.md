---
title: "Operational Pilot Randomization Plan v0.1"
type: evaluation-randomization-plan
status: proposed-synthetic
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - sle
  - evaluation
  - randomization
  - pilot
---
# Operational Pilot Randomization Plan v0.1

## Purpose

This plan defines a reproducible synthetic assignment check for issue #36. Human issue #33 must approve and freeze the actual pilot schedule.

## Seed and reproducibility

- Default dry-run seed: `20260728`
- Generator: `tools/evaluation/generate_dry_run.py`
- Reviewed assignment layer: `tools/evaluation/dry_run_reviewed.py`
- Fixture version: `SLE-EVAL-DRY-RUN-0.1`
- Assignment output: `trials` records in the generated fixture

Changing the seed creates a new assignment version. Record the seed, reviewed-layer commit, material register version, and output hash.

## Synthetic block construction

The reviewed valid fixture contains 20 active fictional participants and one separately retained withdrawn row.

1. Shuffle the five core materials once under the recorded seed.
2. Rotate that order across the 20 active fictional participants.
3. Omit one material per participant, producing 16 exposures per core material.
4. Assign P to even-indexed active participants and S to odd-indexed active participants.
5. Replace four baseline assignments with U only for `SLE-DRY-MAT-0001`, one at each order position and with two removed from P and two removed from S.
6. Add one P and one S Canto-span trial as a separately bounded supplement.

Resulting core allocation:

- `SLE-DRY-MAT-0001`: 6 P, 6 S, 4 U;
- each other core material: 8 P, 8 S;
- each order position: absolute P/S difference at most 1.

These counts are fixture mechanics, not a proposed human sample size.

## Assignment constraints

The generator must:

1. assign no participant more than one wording condition from one meaning record;
2. keep the P/S difference for each material at most 1;
3. keep the P/S difference for each order position at most 1;
4. use U only for a material with `u_admissible=yes`;
5. keep deliberately defective U material within synthetic pilot tasks;
6. include P and S in every publication-relevant registered condition set;
7. keep Canto-span contributors at or below 10% of the synthetic participant set;
8. keep Canto-span trials at or below 10% of pooled synthetic trials;
9. exclude withdrawn synthetic participants from post-withdrawal assignments;
10. use opaque `MX###` condition codes that exactly match the registered material-condition mask;
11. preserve assignment order and the seed for audit.

## Task-specific exposure

- Reader reconstruction: P and S; U only when an authorized baseline is registered.
- Editorial review: registered passages needed for the checklist task.
- Authoring and revision: P-guidance versus S-guidance.
- Translation: P versus S; source-order baseline only when separately registered.
- Full-document: P versus S; U optional.

No schedule may infer a universal U/P/S requirement from the existence of three condition labels.

## Contamination checks

Before use, check:

- duplicate participant-plus-meaning-record pairs;
- participant exposure to both P and S for one record;
- leaked, duplicated, or mismatched condition masks;
- repeated rule-family exposure beyond the frozen limit;
- condition imbalance by material;
- order imbalance by condition;
- Canto-span cap;
- accessibility incompatibility;
- withdrawn or excluded participants in later assignments.

## Human freeze record

The actual issue #33 schedule must record:

- responsible human:
- approval date:
- participant quota:
- material version:
- scoring-key version:
- random seed:
- algorithm version:
- schedule hash:
- accommodation adjustments:
- deviations:
- whether outcome data were visible:

Synthetic schedule validation cannot approve recruitment or participant exposure.
