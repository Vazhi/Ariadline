---
title: "Ariadline Kill-Test Synthetic Rehearsal Validation v0.1"
type: validation-report
status: complete
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags: [ariadline, validation, rehearsal]
---
# Ariadline Kill-Test Synthetic Rehearsal Validation v0.1

## Package result

PASS — the package contains every automated deliverable in issue #55 and keeps all human-study authority outside the synthetic rehearsal.

## Files checked

- [[Ariadline Kill-Test Synthetic Rehearsal v0.1]]
- [[Ariadline Kill-Test Synthetic Case Register v0.1]]
- [[Ariadline Kill-Test Synthetic Rehearsal Report v0.1]]
- `tools/evaluation/rehearse_kill_test.py`
- valid fixture JSON;
- invalid fixture JSON;
- exact expected-code manifest.

## Executed checks

```text
valid fixture: valid
valid findings: 0
invalid fixture: expected_failures_detected
invalid findings: 20
distinct expected classes: 16
missing expected classes: 0
unexpected classes: 0
```

## Structural coverage

The validator checks:

- explicit synthetic-only status;
- permitted rehearsal study states;
- procedure-only evidence claims;
- presence of required human gates;
- unique case identifiers;
- separate P/S editors for one meaning record;
- identical P/S shared-packet hashes;
- absence of restricted scorer metadata;
- scoring-key freeze before condition-output access;
- deterministic preservation aggregation;
- pair benefit eligibility;
- reader-exposure eligibility;
- adverse-result retention;
- prohibition on promoting `not determined`;
- launch blocking with unresolved human gates or ineligible records;
- prohibition on advancing parent issue #9.

## Determinism

The validator uses only the Python standard library. The negative self-test compares the exact set of diagnostic codes, not only the exit status or finding count.

## Authority boundary

A PASS means only that the supplied fictional records exercise the represented structural controls as expected. It does not validate real materials, human decisions, study readiness, or Ariadline effectiveness.
