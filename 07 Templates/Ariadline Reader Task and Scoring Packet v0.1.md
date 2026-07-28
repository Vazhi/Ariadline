---
title: "Ariadline Reader Task and Scoring Packet v0.1"
type: evaluation-template
status: planning-draft
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags: [ariadline, evaluation, readers, scoring]
---
# Ariadline Reader Task and Scoring Packet v0.1

Use only tasks registered for the passage’s authentic rule-neutral communication risk.

This template has three information layers:

1. **restricted administrative mapping** — condition identity, `SLE-RULE-*` IDs, editor identity, and action logs;
2. **reader-facing packet** — masked text and registered questions only;
3. **scorer-facing packet** — masked responses and a frozen scoring key only.

Restricted administrative mapping must not be exposed to readers, scorers, adjudicators, or task/key designers before the relevant records are frozen.

## Restricted administrative registration

- Passage ID:
- Masked text code:
- Meaning-record ID and version:
- Condition mapping, held by data manager:
- Applicable `SLE-RULE-*` IDs, held by data manager:
- Editor identity and action-log locator, held by data manager:
- Registered rule-neutral risk:
- Primary task:
- Supporting tasks:
- Scoring-key version and hash:
- Expected response type:
- Accessibility format:

## Task and scoring-key freeze

Task constructs, questions, accepted elements, prohibited unsupported elements, and adjudication rules must be derived only from:

- the source passage;
- the authorized meaning record;
- the shared rule-neutral communication-risk brief;
- the registered construct and accessibility requirements.

Freeze the task and scoring key before task designers or scorers examine P/S outputs, editor logs, preservation outcomes, condition mappings, or participant outcomes.

A later change requires a versioned deviation record. Outcome-visible or condition-visible changes cannot be silently applied to the primary comparison.

## Reader-facing packet

Reader-facing material contains only:

- masked text code;
- masked passage text;
- reader instructions;
- registered questions and response scales;
- approved accessibility support.

It must not contain condition labels, rule IDs, editor identity, action logs, meaning-record text, expected direction, or scoring answers.

### Reader instructions

Read the passage as you would read professional linguistic writing. Answer only from the passage. Use `not determined from this passage` when the passage does not provide enough information.

## Task bank

Select the smallest relevant set.

### Claim and scope

- State the central claim in your own words.
- What population, variety, dataset, register, period, or condition limits the claim?
- Which broader statement would the passage **not** justify?

### Evidence and support

- Which stated evidence or analysis supports the central claim?
- What conclusion is stronger than the evidence permits?
- Is the passage reporting software behavior, a linguistic analysis, or both?

### Limitations and negative findings

- What relevant limitation or counterexample is stated?
- What space was searched or tested?
- What could the method have missed?

### Reference and logical scope

- What does the highlighted expression refer to?
- Which interpretation of negation, quantification, restriction, or exception is supported?

### Provenance and transformation

- What is the origin of the example or data?
- Was it elicited, extracted, adapted, translated, normalized, system-produced, or otherwise transformed?

### Experience ratings

Use the frozen response scale for:

- naturalness;
- cohesion;
- repetition;
- fragmentation;
- effort or burden;
- confidence in interpretation.

## Scoring key template

For each scored question, record:

- question ID;
- construct;
- accepted elements;
- prohibited unsupported elements;
- partial-credit rule, if any;
- `not determined` treatment;
- critical error classes;
- examples of pass, fail, and borderline responses;
- masking requirement;
- adjudication trigger;
- key version and hash;
- freeze date and human approvers.

The scoring key must not contain a condition label, rule ID, editor identity, rule-action log, or condition-specific expected answer.

## Scorer-facing packet and record

Scorers receive only masked response IDs, masked answers, and the frozen scoring key.

- Scorer ID:
- Condition masked: yes/no/not determined
- Rule metadata absent: yes/no/not determined
- Editor metadata absent: yes/no/not determined
- Training and calibration version:
- Response ID:
- Score:
- Error class:
- Unsupported inference present: yes/no/not determined
- Material misinterpretation present: yes/no/not determined
- Confidence calibration result:
- Adjudication required:
- Notes:

Any failed or indeterminate masking check must trigger the registered deviation and eligibility review.

## Agreement and adjudication

Report agreement separately for:

- task applicability;
- binary or categorical scores;
- error class;
- unsupported-inference classification;
- final adjudicated result.

Adjudicators receive the same restricted scorer-facing information unless the frozen protocol authorizes a documented unmasking step.

Do not hide systematic disagreement behind a package average.

## Analysis boundary

The primary contrast is masked S versus P. U, when registered, is descriptive and cannot replace S-versus-P. Scores cannot override a failed or unresolved meaning-preservation gate.
