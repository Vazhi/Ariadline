---
title: "Pilot Specification Outline"
type: implementation-plan
status: revised
created: 2026-07-27
updated: 2026-07-27
tags:
  - sle
  - implementation
  - pilot
---
# Pilot Specification Outline

## Purpose

The pilot assembles an auditable proposed reference artifact for human evaluation. It is not a software implementation and it is not a stabilized standard.

## Proposed v0.1 contents

### Part 1 — Introduction

- purpose and users;
- scope and non-goals;
- authority and neutrality boundaries;
- normative verbal-form declaration;
- definitions;
- relationship between rules, patterns, profiles, extensions, review methods, and evaluation records.

### Part 2 — Language rules

Use the proposed rules in [[SLE for Linguistics Language Rules v0.1]].

Each rule must include:

- stable ID;
- normative or recommended text;
- scope and non-scope;
- rationale;
- compliant and noncompliant examples;
- exceptions or boundaries;
- human editorial check;
- exact evidence reference;
- status and unresolved evaluation needs.

### Part 3 — Document patterns

Use [[SLE for Linguistics Document Patterns v0.1]] and [[SLE Document Pattern Outlines v0.1]].

The pattern catalogue must cover multiple linguistic purposes without requiring one section schema or English rhetorical order. It must include:

- recommended default sequence and required information relationships;
- required distinctions;
- example, glossing, citation, uncertainty, and limitation practices where applicable;
- permitted omissions;
- minimum editorial checks;
- optional conformance declarations;
- waiver and extension guidance.

### Part 4 — Terminology

Publish only terminology required to interpret the reference artifact consistently.

The core term list must remain independent of Canto-span. Project-specific termbases may appear as non-normative test or adoption material.

### Part 5 — Profiles and conformance

Use [[Profiles and Conformance]] and [[SLE Profile Applicability Register v0.1]].

Define:

- conformance object;
- exact versioned mappings for SLE-Core, SLE-Research, SLE-Resource, and SLE-Procedure;
- conformance results: conforms, conforms with declared waivers, does not conform, and not determined;
- review methods such as author self-review and independent editorial review;
- typed evaluation records with exact scope or sample;
- human editorial checklist;
- optional prose declarations;
- waiver and extension records;
- conformance-versus-truth boundary.

Software checks are optional aids. They do not create a conformance result, review method, or evaluation type.

### Part 6 — Governance and versioning

Define:

- rule and pattern states;
- stable identifiers;
- profile-set versions;
- change control;
- generalization gates;
- compatibility-based major, minor, and patch decisions;
- non-breaking transition mechanisms;
- translation and localized-edition policy;
- public change and migration records.

### Annexes

Possible informative annexes:

- compliant and noncompliant examples;
- boundary cases;
- reusable outlines;
- evidence and coverage registers;
- human review forms;
- profile applicability records;
- evaluation materials;
- translation notes;
- optional project-documentation patterns.

Annexes must state whether they are normative or informative.

## Evaluation corpus

The pilot evaluation set should contain representative passages from:

- descriptive grammar;
- theoretical analysis;
- corpus research;
- elicitation and experimental judgment work;
- fieldwork and language documentation;
- sociolinguistics and discourse or conversation analysis;
- phonetics and laboratory phonology;
- lexicography;
- annotation guidelines;
- computational linguistics;
- language-resource documentation;
- signed-language research;
- academic traditions and author communities beyond English-dominant publishing.

The evaluation set should include original passages, controlled revisions, alternative rhetorical orders, boundary cases, justified omissions, conditional-rule decisions, conformance-result disagreements, and rejected rewrites that lose necessary meaning.

Canto-span may supply a small non-authoritative subset after independent rules and patterns exist.

## Exit condition for a proposed pilot edition

A proposed pilot edition can be published for evaluation when:

1. every included rule and pattern has a stable ID and proposed status;
2. each normative item states its scope, boundaries, and editorial check;
3. evidence and unsupported specificity are distinguishable;
4. profiles map to exact rule IDs under a versioned register;
5. conformance result is separate from review method and typed evaluation records;
6. all required internal links resolve;
7. the human-readable edition is complete without software or machine-readable metadata;
8. known domain, theory, method, language, translation, order, profile, and compatibility gaps are recorded;
9. the edition clearly states that it is not stabilized.

## Stabilization boundary

No rule, pattern, profile mapping, conformance result, review method, evaluation type, or term becomes stable merely because it appears in the pilot.

Stabilization requires the evidence, reader benefit, author meaning preservation, authoring-burden, neutrality, translation, profile-reconstruction, conformance-result, and compatibility gates defined by governance and validation records.
