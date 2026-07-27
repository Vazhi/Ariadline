---
title: "Evaluation Framework"
type: validation
status: draft
created: 2026-07-27
updated: 2026-07-27
tags:
  - sle
  - validation
  - evaluation
---
# Evaluation Framework

## Central question

Does SLE improve understanding and consistency while preserving the intended linguistic content?

## Evaluation dimensions

### Comprehension

Measure whether readers identify:

- the main claim;
- the evidence type;
- the scope;
- the level of certainty;
- the relevant limitation;
- the antecedent of references.

### Authoring performance

Measure:

- time to write or revise;
- number of rule violations;
- number of unintended meaning changes;
- perceived difficulty;
- need for specialist support.

### Review and adjudication

Measure:

- reviewer agreement;
- terminology conflicts;
- unresolved references;
- evidence-class disagreements;
- time to approve a passage.

### Machine assistance

Measure:

- precision and recall for each checker rule;
- false-positive burden;
- missed high-severity ambiguities;
- consistency across editor integrations.

### Content preservation

Expert reviewers compare the uncontrolled and SLE versions for:

- polarity;
- quantification;
- scope;
- evidential force;
- theoretical commitment;
- example status.

## Comparison design

Use paired or randomized comparisons between:

- original prose;
- expert-edited plain prose;
- SLE-controlled prose.

This separation tests whether benefits come from SLE controls rather than editing quality alone.

## User groups

Include:

- experienced linguists;
- graduate students;
- linguists who use English as an additional language;
- corpus or annotation workers;
- technical readers outside the subfield.

## Evidence policy

Automated readability formulas can supplement the evaluation. They cannot establish comprehension or scientific accuracy.

## Iteration rule

A rule that does not improve a target metric, or that causes unacceptable precision loss, must be revised, limited to a profile, or removed.

## Active grammar-engineering baseline

The first grammar-engineering test run uses [[SLE-GE Canto-span Pilot Baseline v0.1]]. That note freezes the external source materials, reader questions, semantic-equivalence safeguards, measures, and decision outcomes before paired rewriting begins.
