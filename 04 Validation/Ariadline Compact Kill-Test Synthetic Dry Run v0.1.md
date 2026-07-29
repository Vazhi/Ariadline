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

This package exercises the complete compact kill-test workflow required by issue #45 using entirely fictional records. It tests data generation, assignment, masking, scoring, exclusions, preservation, analysis, and disposition routing before authentic materials or participant data are used.

It does not establish that Ariadline is effective, safe, fair, meaningful, feasible, or approved for human execution.

## Package contents

- [[Ariadline Compact Kill-Test Synthetic Data Dictionary v0.1]]
- [[Ariadline Compact Kill-Test Synthetic Dry Run Report v0.1]]
- [[Ariadline Compact Kill-Test Synthetic Dry Run Validation v0.1]]
- [[Ariadline Compact Kill-Test Synthetic Readiness Checklist v0.1]]
- `tools/evaluation/run_compact_kill_test_dry_run.py`
- `tools/evaluation/fixtures/ariadline_compact_kill_test_dry_run_source.json`
- `tools/evaluation/fixtures/ariadline_compact_kill_test_dry_run_expected/assignments.json`
- `tools/evaluation/fixtures/ariadline_compact_kill_test_dry_run_expected/scoring_and_adjudication.json`
- `tools/evaluation/fixtures/ariadline_compact_kill_test_dry_run_expected/analysis.json`

## Synthetic design

- 12 fictional meaning records;
- four domain families;
- paired fictional P and S condition records;
- 24 fictional participants;
- six assignments per participant;
- 144 total masked assignments;
- nine eligible P/S pairs;
- three retained ineligible pairs;
- deterministic seed `4501`;
- exact eight-P/eight-S exposure for each eligible material;
- correct, incorrect, uncertain, missing, and technical-failure response states;
- two masked scorers per response, including an independent scoring route;
- deterministic adjudication;
- planned exclusions and deviations;
- adverse S, inconclusive, bias, preservation-failure, and ordinary-editing-superiority cases.

## Commands

```bash
python tools/evaluation/run_compact_kill_test_dry_run.py \
  tools/evaluation/fixtures/ariadline_compact_kill_test_dry_run_source.json \
  --output-dir /tmp/ariadline-compact-dry-run

python tools/evaluation/run_compact_kill_test_dry_run.py \
  tools/evaluation/fixtures/ariadline_compact_kill_test_dry_run_source.json \
  --expect-dir tools/evaluation/fixtures/ariadline_compact_kill_test_dry_run_expected
```

## Expected exact outputs

- `assignments.json`: `sha256:16b99df65ae2a2e1bebcd7fcce2d14ad19b4634a8431374c75982c4d4dff0f4c`
- `scoring_and_adjudication.json`: `sha256:5cae5fe6cea6b544a7c78c396692075c296eece01890dee9e02f1760ded5bc6f`
- `analysis.json`: `sha256:6d02757f3f5607fffa4c10792bb9fce648c91d45ee54952caea7411f48fa9b83`

## Boundary

Every passage, participant, editor, scorer, authority, permission, gate, response, score, exclusion, deviation, and outcome is fictional. Human issues #40, #42, #44, #46, and #48 remain unsatisfied. Synthetic outcomes cannot be cited as evidence about authentic linguistic writing or human readers.
