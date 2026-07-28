---
title: "Ariadline Kill-Test Synthetic Rehearsal v0.1"
type: evaluation-package
status: planning-draft
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags: [ariadline, evaluation, rehearsal, synthetic]
---
# Ariadline Kill-Test Synthetic Rehearsal v0.1

## Purpose

This package rehearses the merged [[Ariadline Kill-Test Execution Packet v0.1]] with fictional records. It tests whether the procedure blocks invalid state changes, information leakage, unfair condition construction, invalid preservation aggregation, and unsupported claims.

It does not test whether Ariadline benefits readers or authors.

## Contents

- [[Ariadline Kill-Test Synthetic Case Register v0.1]]
- [[Ariadline Kill-Test Synthetic Rehearsal Report v0.1]]
- [[Ariadline Kill-Test Synthetic Rehearsal Validation v0.1]]
- `tools/evaluation/rehearse_kill_test.py`
- `tools/evaluation/fixtures/ariadline_kill_test_rehearsal_valid.json`
- `tools/evaluation/fixtures/ariadline_kill_test_rehearsal_invalid.json`
- `tools/evaluation/fixtures/ariadline_kill_test_rehearsal_expected_codes.json`

## Rehearsal flow

1. Load an explicitly synthetic fixture.
2. Check study-state and evidence-claim boundaries.
3. Check required human-gate records.
4. Check unique case identities and P/S shared-packet equality.
5. Check same-record editor separation.
6. Check scorer metadata separation and scoring-key freeze timing.
7. Derive preservation outcomes from dimension records.
8. Check pair eligibility and reader-exposure restrictions.
9. Require failed and unresolved outcomes to remain visible.
10. Block launch and parent-study advancement when human gates remain unresolved.

## Commands

```bash
python3 tools/evaluation/rehearse_kill_test.py \
  tools/evaluation/fixtures/ariadline_kill_test_rehearsal_valid.json

python3 tools/evaluation/rehearse_kill_test.py \
  tools/evaluation/fixtures/ariadline_kill_test_rehearsal_invalid.json \
  --expect-codes tools/evaluation/fixtures/ariadline_kill_test_rehearsal_expected_codes.json
```

## Interpretation

A passing rehearsal means that the represented structural controls behave as specified for the fictional fixtures. It does not approve materials, people, authority, oversight, accessibility, statistics, preregistration, recruitment, preservation, or project disposition.

## Authority boundary

All passages, people, authorities, permissions, outcomes, and identifiers in this package are fictional. The package cannot advance [[Evaluation Execution Status v0.1]], close parent issue #9, or satisfy human issues #30–#35.
