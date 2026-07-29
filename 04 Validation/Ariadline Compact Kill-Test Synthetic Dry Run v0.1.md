---
title: "Ariadline Compact Kill-Test Synthetic Dry Run v0.1"
type: evaluation-package
status: synthetic-complete
version: "0.1"
created: 2026-07-29
updated: 2026-07-29
tags: [ariadline, evaluation, synthetic, dry-run]
---
# Ariadline Compact Kill-Test Synthetic Dry Run v0.1

## Purpose

This package exercises the complete compact kill-test workflow required by issue #45 using entirely fictional records. It tests material registration, assignment, masking, scoring, exclusions, preservation, analysis, exact reproduction, and disposition routing before authentic materials or participant data are used.

It does not establish that Ariadline is effective, safe, fair, meaningful, feasible, or approved for human execution.

## Package contents

- [[Ariadline Compact Kill-Test Synthetic Data Dictionary v0.1]]
- [[Ariadline Compact Kill-Test Synthetic Dry Run Report v0.1]]
- [[Ariadline Compact Kill-Test Synthetic Dry Run Validation v0.1]]
- [[Ariadline Compact Kill-Test Synthetic Readiness Checklist v0.1]]
- `tools/evaluation/run_compact_kill_test_dry_run.py`
- `tools/evaluation/verify_compact_kill_test_dry_run.py`
- `tools/evaluation/fixtures/ariadline_compact_kill_test_dry_run_source.json`
- `tools/evaluation/fixtures/ariadline_compact_kill_test_dry_run_expected/assignments.json`
- `tools/evaluation/fixtures/ariadline_compact_kill_test_dry_run_expected/scoring_and_adjudication.json`
- `tools/evaluation/fixtures/ariadline_compact_kill_test_dry_run_expected/analysis.json`

The core runner builds and validates explicit in-memory records. The verifier converts those records into lossless columnar fixtures, reconstructs the declared records, and compares them exactly with the committed outputs.

## Synthetic design

- 12 fictional meaning records;
- four domain families;
- paired fictional P and S conditions;
- 24 fictional participants;
- six assignments per participant;
- 144 masked assignments and raw responses;
- nine eligible P/S pairs and three retained ineligible pairs;
- exact eight-P/eight-S exposure for each eligible material;
- deterministic seed `4501` and schedule algorithm `cyclic-balanced-v2`;
- 137 analyzable responses;
- 274 initial score rows, exactly two for each analyzable response;
- 23 deterministic adjudications;
- seven mechanically excluded missing or technical records with no score or adjudication rows;
- an independent scoring route for every analyzable response and every represented question;
- adverse-S, inconclusive, bias, preservation-failure, and ordinary-editing-superiority cases;
- continue, revise, stop, and insufficient-evidence route tests.

## Commands

Generate compact outputs:

```bash
python tools/evaluation/verify_compact_kill_test_dry_run.py \
  tools/evaluation/fixtures/ariadline_compact_kill_test_dry_run_source.json \
  --output-dir /tmp/ariadline-compact-dry-run
```

Run the exact self-test:

```bash
python tools/evaluation/verify_compact_kill_test_dry_run.py \
  tools/evaluation/fixtures/ariadline_compact_kill_test_dry_run_source.json \
  --expect-dir tools/evaluation/fixtures/ariadline_compact_kill_test_dry_run_expected
```

## Expected exact outputs

- `assignments.json`: `sha256:44ed785714ea80084a2c5dd670bf25eec58a1576d0bf4ab0ff08ba378987cb88`
- `scoring_and_adjudication.json`: `sha256:0a8222ec8811ce5de253c886163e2cffa5770f13cd71d394a0c07d7793c333d7`
- `analysis.json`: `sha256:b334d8acc27b682ebe82cfee7a6eac9c3964cbdf403c715f80f39c767ab3d0b5`

## Boundary

Every passage, participant, editor, scorer, authority, permission, gate, response, score, exclusion, deviation, and outcome is fictional. Human issues #40, #42, #44, #46, and #48 remain unsatisfied. Synthetic outputs cannot be cited as evidence about authentic linguistic writing or human readers.
