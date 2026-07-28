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

This package rehearses the merged [[Ariadline Kill-Test Execution Packet v0.1]] with fictional records. It tests whether the procedure blocks incomplete records, invalid state changes, information leakage, unfair condition construction, invalid preservation aggregation, and unsupported claims.

It does not test whether Ariadline benefits readers or authors.

## Contents

- [[Ariadline Kill-Test Synthetic Case Register v0.1]]
- [[Ariadline Kill-Test Synthetic Rehearsal Report v0.1]]
- [[Ariadline Kill-Test Synthetic Rehearsal Validation v0.1]]
- `tools/evaluation/rehearse_kill_test.py`
- `tools/evaluation/fixtures/ariadline_kill_test_rehearsal_valid.json`
- `tools/evaluation/fixtures/ariadline_kill_test_rehearsal_invalid.json`
- `tools/evaluation/fixtures/ariadline_kill_test_rehearsal_expected_findings.json`

## Rehearsal flow

1. Load an explicitly synthetic fixture.
2. Check fixture identity, study-state, and evidence-claim boundaries.
3. Check required human-gate records and allowed gate states.
4. Check case, condition, output-hash, shared-packet, scoring-key, and preservation-record completeness.
5. Check unique case identities and separate P/S editors.
6. Check scorer metadata separation and scoring-key freeze timing.
7. Derive preservation outcomes from valid material dimensions.
8. Derive pair eligibility from completeness, fairness, masking, freeze, comparability, and preservation.
9. Gate reader exposure through explicit launch selection and simulated launch readiness.
10. Retain failed and unresolved outcomes without allowing excluded records to block an otherwise valid selected set.
11. Block parent-study advancement and human-evidence claims.
12. Compare the negative fixture against the complete expected `(code, path)` finding manifest.

## Commands

```bash
python3 tools/evaluation/rehearse_kill_test.py \
  tools/evaluation/fixtures/ariadline_kill_test_rehearsal_valid.json

python3 tools/evaluation/rehearse_kill_test.py \
  tools/evaluation/fixtures/ariadline_kill_test_rehearsal_invalid.json \
  --expect-findings tools/evaluation/fixtures/ariadline_kill_test_rehearsal_expected_findings.json
```

## Interpretation

The valid fixture uses fictional `approved` gate values solely to rehearse selected-set launch logic. Those values are not real approvals. A passing rehearsal means only that the represented structural controls behave as specified for the fictional fixtures.

It does not approve materials, people, authority, oversight, accessibility, statistics, preregistration, recruitment, preservation, or project disposition.

## Authority boundary

All passages, people, authorities, permissions, gate states, outcomes, and identifiers in this package are fictional. The package cannot advance [[Evaluation Execution Status v0.1]], close parent issue #9, or satisfy human issues #30–#35.
