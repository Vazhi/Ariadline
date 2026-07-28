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
- Fixture version: `SLE-EVAL-DRY-RUN-0.1`
- Assignment output: `trials` records in the generated fixture

Changing the seed creates a new assignment version. Record the seed, generator commit, material register version, and output hash.

## Assignment constraints

The generator must:

1. assign no participant more than one wording condition from one meaning record;
2. balance P and S within synthetic blocks as closely as the fixture size permits;
3. use U only for a material with `u_admissible=yes`;
4. keep deliberately defective U material within synthetic pilot tasks;
5. include P and S in every publication-relevant registered condition set;
6. keep Canto-span contributors at or below 10% of the synthetic participant set;
7. keep Canto-span trials at or below 10% of pooled synthetic trials;
8. exclude withdrawn synthetic participants from post-withdrawal assignments;
9. use opaque `MX###` condition codes;
10. preserve assignment order and the seed for audit.

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
- leaked condition labels in mask codes or filenames;
- repeated rule-family exposure beyond the frozen limit;
- order imbalance by condition and domain;
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
