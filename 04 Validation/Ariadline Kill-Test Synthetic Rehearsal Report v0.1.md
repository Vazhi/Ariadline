---
title: "Ariadline Kill-Test Synthetic Rehearsal Report v0.1"
type: evaluation-report
status: complete
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags: [ariadline, evaluation, rehearsal, report]
---
# Ariadline Kill-Test Synthetic Rehearsal Report v0.1

## Result

The deterministic rehearsal completed successfully on the exact fixture, manifest, and validator sources prepared for issue #55.

- valid fixture: `valid`, 0 findings;
- invalid fixture: `expected_failures_detected`;
- invalid-fixture findings: 50;
- distinct diagnostic classes: 27;
- missing expected `(code, path)` findings: 0;
- unexpected `(code, path)` findings: 0.

## Valid-path behavior

The valid fixture demonstrates that the represented procedure can:

- require complete case, P/S condition, output-hash, scoring-key, and preservation records;
- retain a structurally eligible fictional P/S pair only when fairness, masking, freeze, comparability, and preservation controls all pass;
- simulate reader exposure for one explicitly selected eligible pair after fictional gate states are marked `approved`;
- retain excluded `not preserved` and `not determined` pairs without making the selected eligible pair structurally unlaunchable;
- keep failed and unresolved outcomes visible as adverse records;
- keep parent issue #9 unchanged;
- limit claims to procedure validation.

The `approved` gate values are fictional state markers used only to test launch-set logic. They do not represent human approval.

## Negative-path behavior

The invalid fixture confirms detection of:

- missing fixture, case, condition, output-hash, scoring-key, and preservation information;
- false evidence and study-state claims;
- missing or invalid human-gate states;
- duplicate case identity and invalid comparability;
- same-record editor carryover;
- mismatched or missing shared packets;
- restricted scorer metadata leakage;
- late or incomplete scoring-key freeze;
- invalid preservation dimensions and aggregation;
- contaminated or failed pairs marked benefit-eligible;
- ineligible pairs selected for launch;
- reader exposure for unselected, ineligible, or launch-unready pairs;
- hidden adverse outcomes;
- promotion of `not determined`;
- attempted launch and parent-study advancement.

See [[Ariadline Kill-Test Synthetic Case Register v0.1]] and the expected-findings JSON for the exact identities.

## Limits

The rehearsal does not use authentic passages, real editors, real readers, real authorities, real permissions, or human preservation judgments. It therefore provides no evidence about reader benefit, author burden, naturalness, cohesion, meaning preservation, accessibility, bias, or whether Ariadline should continue.

## Required human continuation

Issues #30–#35 remain controlling. The rehearsal cannot replace oversight, authentic-material authorization, legitimate meaning authority, independent human preservation review, statistical review, preregistration, recruitment, execution, analysis, or final disposition.
