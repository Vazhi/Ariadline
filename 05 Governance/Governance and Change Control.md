---
title: "Governance and Change Control"
type: governance
status: draft
created: 2026-07-27
updated: 2026-07-27
tags:
  - sle
  - governance
  - change-control
---
# Governance and Change Control

## Governance bodies

### Maintainer group

Responsibilities:

- manage releases;
- maintain registers;
- enforce process;
- publish decisions;
- prevent undocumented rule changes.

### Linguistics review group

Include representatives from multiple subfields and theoretical traditions.

Responsibilities:

- evaluate technical accuracy;
- identify theory-specific bias;
- review definitions and examples.

### User and implementation group

Include authors, editors, annotators, non-native English users, and tool developers.

Responsibilities:

- report usability problems;
- evaluate checker behavior;
- propose profile needs.

## Rule states

- proposed;
- experimental;
- candidate;
- approved;
- deprecated;
- retired.

## Change process

1. Submit [[SLE Change Request Template|a change request]].
2. Identify the affected rules, terms, profiles, and tests.
3. Provide evidence and examples.
4. Conduct technical and usability review.
5. Record the decision in [[Decision Log]].
6. update tests before implementation.
7. release under [[Versioning and Release Model|version control]].

## Decision requirements

A decision record must state:

- issue;
- alternatives;
- evidence;
- selected action;
- dissent or uncertainty;
- compatibility effect;
- required migration;
- review date.

## Conflict-of-framework rule

A change must not make one theoretical framework appear neutral when the rule depends on that framework. Such a rule belongs in a declared profile or extension.

## Public feedback

Publish:

- change requests;
- decisions;
- rule histories;
- deprecated forms;
- migration guidance.

Personal or confidential research data must remain outside the public record.
