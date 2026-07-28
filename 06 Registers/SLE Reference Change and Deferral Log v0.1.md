---
title: "SLE Reference Change and Deferral Log v0.1"
type: change-log
status: proposed
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - sle
  - change-log
  - deferred
  - rejected
---
# SLE Reference Change and Deferral Log v0.1

## Purpose

This log records major assembly decisions for [[SLE for Linguistics Reference Artifact v0.1 Draft]].

It is an informative history. Normative changes must follow [[Governance and Change Control]] and [[Versioning and Release Model]].

## Accepted assembly decisions

### Prose-first reference artifact

The controlling product is a durable human-readable edition. Software, schemas, machine-readable exports, and repository metadata are optional supporting products.

### Independent authority

Core SLE design uses independent evidence and multi-domain evaluation. Canto-span remains a later non-authoritative stress test and adoption target.

### Modular controlling text

The package has separate controlling modules for rules, patterns, profiles and conformance, profile mappings, governance, versioning, and terminology. The master draft supplies navigation and hierarchy rather than silently rewriting those modules.

### Stable identifiers

Rule and pattern identifiers do not contain release versions. Version history controls their state.

### Human conformance

A trained human can apply the reference without software. Conformance result, review method, and typed evaluation are separate records.

### Authorized meaning

Meaning-changing editorial work requires a legitimate meaning record or a **not determined** outcome. Constructed audit briefs are not substitutes for authentic author or community authority.

### Flexible rhetorical order

Pattern sequences are recommended defaults. Alternative order can conform when required information relationships remain recoverable.

### Compatibility-based release classification

Major, minor, and patch classes follow effects on obligations and prior conformance outcomes, not file type or edit size.

## Rejected as universal v0.1 controls

The draft does not adopt:

- a fixed maximum sentence length;
- a universal active-voice requirement;
- a universal ban on passive voice;
- a universal ban on nominalization;
- mandatory visible claim-function labels;
- mandatory YAML or machine-readable headers;
- mandatory software checking;
- a universal evidence-verb hierarchy;
- a universal linguistic ontology;
- a universal theory, method, annotation schema, or rhetorical order;
- Canto-span terminology, statuses, repository structure, parser workflow, release process, or governance.

These proposals may be reconsidered only through the ordinary evidence and evaluation process.

## Deferred design decisions

### Preferred requirement verb

`SLE-RULE-0008` requires a declared consistent function system. Selection of **must**, **shall**, or another preferred requirement form remains an evaluation question.

### Evidence-verb profiles

The draft controls overstatement but does not define a universal ranking for *shows*, *supports*, *suggests*, *is consistent with*, *does not establish*, and *contradicts*.

### Provenance dimensions

The four example-provenance dimensions remain proposed pending field, corpus, experimental, documentation, lexicographic, signed-language, and community review.

### Controlled terminology module

The current [[Glossary]] supplies publication terminology. A larger stable controlled termbase remains future work and must not be derived from the non-normative Canto-span fixture.

### Multilingual and localized guidance

Non-English-original authoring, translated editions, bilingual review, and language-specific normative forms require authentic materials and appropriate authority.

### Publisher and community adoption packages

Publisher profiles, community extensions, and local declaration formats remain later work.

### Project-documentation annex

Pull requests, release notes, repository handoffs, and software project records are outside the core linguistic patterns. An informative annex may address them later.

### Optional automation

Automation may flag text for review. Executable rules, diagnostics, confidence policies, and software architecture require separately authorized implementation work.

## Evidence and evaluation gates still open

The draft has not established:

- broad reader-comprehension improvement;
- authoring-efficiency improvement;
- authentic cross-language meaning preservation;
- community acceptance;
- accessibility across user populations;
- full-document effectiveness;
- profile reconstruction reliability across independent reviewers;
- interlinear-glossing effectiveness on independently reviewed real examples;
- superiority over ordinary expert editing.

See [[Evaluation Framework]], [[Pilot Study Design]], [[SLE Evaluation Corpus Bias Assessment v0.1]], and [[Human Review Boundary Register v0.1]].

## Naming risk

**SLE** is a working abbreviation with other established meanings. A naming and acronym review is required before public release.

## Change history

- Issues #4 and #5 created the proposed rule, pattern, profile, conformance, waiver, and versioning modules.
- Issue #6 created and then corrected the constructed brief-based internal audit corpus.
- Issue #7 created the human editorial checklist, typed boundary prompts, authority boundary, and exact rule traceability.
- Issue #8 assembles the publication package without stabilizing its contents.
