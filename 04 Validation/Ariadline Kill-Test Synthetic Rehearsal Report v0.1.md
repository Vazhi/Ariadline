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

The deterministic rehearsal completed successfully on the exact fixture and validator sources prepared for issue #55.

- valid fixture: `valid`, 0 findings;
- invalid fixture: `expected_failures_detected`;
- invalid-fixture findings: 23;
- distinct expected diagnostic classes: 17;
- missing expected classes: 0;
- unexpected diagnostic classes: 0.

## Valid-path behavior

The valid fixture demonstrates that the represented procedure can:

- retain a structurally eligible fictional P/S pair when both conditions are comparable and derive to `preserved`;
- keep reader exposure blocked even for that eligible pair while human launch gates remain unresolved;
- exclude a pair when one condition derives to `not preserved`;
- exclude a pair when one condition derives to `not determined`;
- preserve failed and unresolved outcomes as adverse records;
- keep the rehearsal non-launchable while human gates remain unresolved;
- keep parent issue #9 unchanged;
- limit claims to procedure validation.

## Negative-path behavior

The invalid fixture confirms detection of:

- false evidence and study-state claims;
- missing human gates;
- same-record editor carryover;
- mismatched shared packets;
- restricted scorer metadata leakage;
- late scoring-key freeze;
- invalid preservation aggregation;
- invalid pair eligibility and reader exposure;
- reader exposure before human launch gates pass;
- hidden adverse outcomes;
- promotion of `not determined`;
- attempted launch and parent-study advancement.

See [[Ariadline Kill-Test Synthetic Case Register v0.1]] for the exact diagnostic classes.

## Limits

The rehearsal does not use authentic passages, real editors, real readers, real authorities, real permissions, or human preservation judgments. It therefore provides no evidence about reader benefit, author burden, naturalness, cohesion, meaning preservation, accessibility, bias, or whether Ariadline should continue.

## Required human continuation

Issues #30–#35 remain controlling. The rehearsal cannot replace oversight, authentic-material authorization, legitimate meaning authority, independent human preservation review, statistical review, preregistration, recruitment, execution, analysis, or final disposition.
