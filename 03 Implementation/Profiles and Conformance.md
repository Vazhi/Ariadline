---
title: "Profiles and Conformance"
type: implementation
status: draft
created: 2026-07-27
updated: 2026-07-27
aliases:
  - "Conformance"
  - "SLE Profile"
tags:
  - sle
  - implementation
  - conformance
  - profiles
---
# Profiles and Conformance

## Reason for profiles

Different documents require different controls. An annotation manual needs strict [[Normative Language|normative language]]. A research discussion needs richer qualification and theoretical terminology.

## Proposed profiles

### SLE-Core

Applies the minimum rules for:

- terminology consistency;
- referential clarity;
- one principal claim per sentence;
- explicit scope;
- defined abbreviations.

### SLE-Research

Adds:

- [[Claim-Evidence Matrix|claim classes]];
- evidence-strength wording;
- limitation statements;
- example provenance;
- explicit constructed-versus-attested status.

### SLE-Data

Adds:

- stable data identifiers;
- metadata fields;
- example and gloss conventions;
- dataset and query versioning;
- machine-readable exports.

### SLE-Procedure

For annotation and workflow instructions. Adds:

- strict *must/should/may/can* meanings;
- one action per instruction;
- explicit conditions;
- ordered steps;
- validation outcomes.

## Conformance levels

- **Level A — Declared:** version, profile, and termbase are identified.
- **Level B — Reviewed:** a trained reviewer completed a checklist.
- **Level C — Checked:** approved software checks passed, with documented exceptions.
- **Level D — Validated:** the document also passed project-specific user or adjudication tests.

## Conformance statement

A conformance statement must identify:

- SLE version;
- profile;
- termbase version;
- extensions;
- waived rules;
- checker version;
- review date.

## No false certification

A checker result alone must not be called full conformance unless the profile defines full conformance as fully machine-verifiable.
