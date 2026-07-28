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

PASS — the repaired package contains every automated deliverable in issue #55 and keeps all human-study authority outside the synthetic rehearsal.

## Files checked

- [[Ariadline Kill-Test Synthetic Rehearsal v0.1]]
- [[Ariadline Kill-Test Synthetic Case Register v0.1]]
- [[Ariadline Kill-Test Synthetic Rehearsal Report v0.1]]
- `tools/evaluation/rehearse_kill_test.py`
- valid fixture JSON;
- invalid fixture JSON;
- exact expected `(code, path)` finding manifest.

## Executed checks

```text
valid fixture: valid
valid findings: 0
invalid fixture: expected_failures_detected
invalid findings: 50
distinct diagnostic classes: 27
expected finding identities: 50
missing finding identities: 0
unexpected finding identities: 0
```

## Structural coverage

The validator checks:

- required fixture, case, scenario, P/S condition, editor, shared-packet, output-hash, scoring-key, and preservation records;
- explicit synthetic-only status;
- permitted rehearsal study states and procedure-only evidence claims;
- required human gates and allowed gate states;
- unique case identifiers;
- separate P/S editors for one meaning record;
- identical non-empty P/S shared-packet hashes;
- absence of rule, condition, and editor metadata from scorer materials;
- scoring-key freeze before condition-output access with a recorded key hash;
- valid preservation dimensions and deterministic aggregation;
- pair benefit eligibility derived from all structural and preservation controls;
- explicit launch selection;
- pair-level reader eligibility and launch readiness;
- retention of adverse and unresolved records;
- prohibition on promoting `not determined`;
- launch blocking for unresolved gates or ineligible selected records;
- permission for excluded adverse records to coexist with an eligible selected set;
- prohibition on advancing parent issue #9.

## Determinism

The validator uses only the Python standard library. The negative self-test compares the complete ordered multiset of `(code, path)` finding identities. A missing duplicate, changed path, or unexpected finding fails the self-test even when the diagnostic-class set remains unchanged.

## Authority boundary

The valid fixture's `approved` gate values are fictional state markers. A PASS means only that the supplied fictional records exercise the represented structural controls as expected. It does not validate real materials, human decisions, study readiness, or Ariadline effectiveness.
