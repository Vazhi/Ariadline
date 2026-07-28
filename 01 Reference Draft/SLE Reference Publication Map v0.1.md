---
title: "SLE Reference Publication Map v0.1"
type: publication-map
status: proposed
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - sle
  - publication
  - authority
  - normative-informative
---
# SLE Reference Publication Map v0.1

## Purpose

This map identifies the components of the assembled [[SLE for Linguistics Reference Artifact v0.1 Draft]] and their authority.

A component's inclusion in the package does not make it normative.

## Authority classes

### A. Publication front door

- [[SLE for Linguistics Reference Artifact v0.1 Draft]] — status, navigation, package hierarchy, and integrated reader guidance.

The front door summarizes the package. It does not replace narrower controlling text.

### B. Controlling proposed normative modules

- [[SLE for Linguistics Language Rules v0.1]] — exact rule wording, boundaries, examples, and editorial checks.
- [[SLE for Linguistics Document Patterns v0.1]] — pattern obligations, required distinctions, recommended sequences, omissions, and pattern conformance guidance.
- [[Profiles and Conformance]] — conformance objects and results, review methods, typed evaluations, waivers, and extensions.
- [[SLE Profile Applicability Register v0.1]] — exact profile-set mappings and conditional applicability.
- [[Glossary]] — package terminology, except where a controlling rule states a narrower local definition.

All items in these modules remain proposed unless their own state says otherwise.

### C. Controlling governance modules

- [[Governance and Change Control]] — adoption, revision, dissent, evidence, evaluation, profile, waiver, and extension governance.
- [[Versioning and Release Model]] — compatibility classification, stable identifiers, releases, translation editions, and publication requirements.

### D. Normative review support

- [[SLE Editorial Conformance Checklist v0.1]] — human application questions and item outcomes.
- [[Human Review Boundary Register v0.1]] — limits of editorial authority.

These modules apply controlling rules but do not create new rules.

### E. Informative authoring aids

- [[SLE Document Pattern Outlines v0.1]]
- [[SLE Document Pattern Example Bank v0.1]]
- [[SLE Rule Test Case Catalog v0.1]]
- [[Optional Automation Notes for SLE Review v0.1]]
- [[SLE Rule and Pattern Index v0.1]]
- [[SLE Reference Change and Deferral Log v0.1]]

An informative example cannot override a rule or establish that its linguistic content is true.

### F. Evidence, validation, and evaluation records

- [[Independent SLE Rule Evidence Register v0.1]]
- [[SLE Rule Traceability Matrix v0.1]]
- [[Document Pattern Coverage Register v0.1]]
- [[Evaluation Framework]]
- [[Pilot Study Design]]
- [[Quality Metrics and Acceptance Gates]]
- [[Multi-Domain SLE Evaluation Corpus v0.1]]
- [[Evaluation Corpus Coverage Matrix v0.1]]
- [[Semantic Equivalence Review Record v0.1]]
- [[SLE Evaluation Corpus Bias Assessment v0.1]]

These records justify, test, qualify, or expose gaps. They are not normative text.

### G. Non-authoritative case studies and stress tests

- [[Canto-span Evaluation Subset v0.1]]
- [[Canto-span Pilot Termbase v0.1]]
- [[Canto-span Case Study]]
- [[Canto-span A-not-A Worked Example]]
- [[SLE-GE Canto-span Pilot Baseline v0.1]]

These components cannot define SLE terminology, rules, patterns, profiles, conformance, or governance.

## Conflict resolution

When components conflict:

1. use the narrower controlling normative module;
2. use the exact profile mapping for applicability;
3. use governance and versioning records for change and compatibility;
4. treat indexes, checklists, examples, corpora, and case studies as supporting material;
5. record unresolved conflict rather than silently selecting convenient wording.

A summary, index, test prompt, automation flag, or project-local practice must not amend a rule.

## Publication status labels

- **proposed** — available for evaluation; not stable;
- **revised** — changed after evidence or evaluation; not stable unless explicitly stated;
- **stable** — accepted into a controlling published edition;
- **informative** or **non-normative** — supports use but creates no obligation;
- **deprecated** — recognized but discouraged or scheduled for removal;
- **retired** — no longer normative and retained for history.

## Human-readable sufficiency

The complete package can be used without software, YAML, JSON, schemas, repository metadata, or automated checking.

Optional exports or tools must identify which readable reference version they support and must not become an undeclared competing authority.
