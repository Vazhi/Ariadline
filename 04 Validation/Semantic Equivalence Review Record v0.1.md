---
title: "Meaning-Preservation Review Record v0.1"
aliases:
  - "Semantic Equivalence Review Record v0.1"
type: validation-register
status: provisional
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - sle
  - validation
  - meaning-preservation
  - review-record
---
# Meaning-Preservation Review Record v0.1

## Purpose

This register records the project-internal construction checks for [[Multi-Domain SLE Evaluation Corpus v0.1]] and [[Canto-span Evaluation Subset v0.1]].

The checks use [[SLE Semantic Equivalence Review Template v0.1]]. They are not independent domain, language, community, translator, or source-author approvals.

## Controlling distinction

Each item has a stable authorized meaning brief declared before both passages.

The register records separately:

1. whether the uncontrolled draft matches the brief;
2. whether the controlled alternative matches the brief in project-internal review;
3. whether the two passages are literally equivalent;
4. whether an independent reviewer has confirmed preservation.

The uncontrolled passages are deliberately defective drafts. Therefore, literal passage-to-passage equivalence is generally **not equivalent by design**. This is not a semantic-preservation success. It means the controlled alternative is being tested against the authorized brief rather than against the uncontrolled draft's overstatement.

## Item-level record

| Item | Brief | Uncontrolled-to-brief | Controlled-to-brief, internal | Literal relation | Independent preservation |
|---|---|---|---|---|---|
| SLE-EVAL-0001 | SLE-BRIEF-0001 | does not match | matches | not equivalent | not determined |
| SLE-EVAL-0002 | SLE-BRIEF-0002 | does not match | matches | not equivalent | not determined |
| SLE-EVAL-0003 | SLE-BRIEF-0003 | does not match | matches | not equivalent | not determined |
| SLE-EVAL-0004 | SLE-BRIEF-0004 | ambiguous | matches | not equivalent | not determined |
| SLE-EVAL-0005 | SLE-BRIEF-0005 | does not match | matches | not equivalent | not determined |
| SLE-EVAL-0006 | SLE-BRIEF-0006 | does not match | matches | not equivalent | not determined |
| SLE-EVAL-0007 | SLE-BRIEF-0007 | does not match | matches | not equivalent | not determined |
| SLE-EVAL-0008 | SLE-BRIEF-0008 | does not match | matches | not equivalent | not determined |
| SLE-EVAL-0009 | SLE-BRIEF-0009 | does not match | matches | not equivalent | not determined |
| SLE-EVAL-0010 | SLE-BRIEF-0010 | ambiguous | matches | not equivalent | not determined |
| SLE-EVAL-0011 | SLE-BRIEF-0011 | does not match | matches | not equivalent | not determined |
| SLE-EVAL-0012 | SLE-BRIEF-0012 | does not match | matches | not equivalent | not determined |
| SLE-EVAL-0013 | SLE-BRIEF-0013 | does not match | matches | not equivalent | not determined |
| SLE-EVAL-0014 | SLE-BRIEF-0014 | ambiguous | matches | not equivalent | not determined |
| SLE-EVAL-0015 | SLE-BRIEF-0015 | ambiguous | matches | not equivalent | not determined |
| SLE-EVAL-0016 | SLE-BRIEF-0016 | does not match | matches | not equivalent | not determined |
| SLE-EVAL-CS-0001 | SLE-BRIEF-CS-0001 | does not match | matches | not equivalent | not determined |
| SLE-EVAL-CS-0002 | SLE-BRIEF-CS-0002 | does not match | matches | not equivalent | not determined |

## Summary

- controlled alternatives matching their constructed briefs in internal review: 18;
- uncontrolled drafts not matching their briefs: 14;
- uncontrolled drafts ambiguous relative to their briefs: 4;
- literally equivalent passage pairs: 0;
- independent preservation confirmations: 0;
- independent preservation results `not determined`: 18.

The absence of rejected controlled alternatives remains a selection-bias risk. A later corpus version must retain failed and disputed alternatives.

## Entry condition for testing

An item may enter reader testing when:

- the brief exists before evaluation;
- the brief authority is stated;
- every controlled detail is licensed by the brief;
- exact full rule IDs and pattern IDs are recorded;
- word and sentence counts are recorded;
- the internal controlled-to-brief result is `matches`;
- independent preservation is still displayed as `not determined` unless a qualified independent reviewer confirms it.

## Authentic-source rule

For authentic passages, the authorized meaning record must come from the source author, controlling publication context, or another legitimate authority. A project editor must not silently invent the source author's intended meaning.

When no authorized resolution exists:

- preserve competing interpretations;
- mark preservation `not determined`;
- reject the alternative from the confirmed pair set;
- record whether the rule, pattern, or evaluation method needs revision.

## Disposition

The v0.1 items may support internal rule auditing and reader-task design. They may not be described as independently equivalent pairs or as evidence that SLE improves linguistic writing.
