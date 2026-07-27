---
title: "Profiles and Conformance"
type: implementation
status: revised
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

## Purpose

Conformance states how a declared document or document part was reviewed against a stated version of SLE for Linguistics.

Conformance does not certify linguistic truth, theoretical correctness, methodological validity, ethical adequacy, speaker acceptability, or software quality.

The proposed document patterns and detailed conformance guidance are in [[SLE for Linguistics Document Patterns v0.1]].

## Conformance object

The conformance object must be identifiable.

It can be:

- a complete document;
- a named section or chapter;
- an annotation guideline;
- a set of entries;
- a resource guide;
- another bounded text artifact.

Conformance does not automatically extend to an entire project, repository, dataset, theory, research program, publication series, or software system.

## Human-readable conformance is sufficient

Basic conformance does not require:

- YAML or another machine-readable header;
- repository metadata;
- a checker;
- a software schema;
- a public termbase;
- a project-specific workflow.

A document can conform through ordinary prose and human editorial review.

## Proposed profiles

Profiles select applicable rule groups. They do not define linguistic theories, methods, or document genres.

### SLE-Core

Applies the general controls for:

- one principal message;
- clear reference;
- explicit scope and comparison;
- stable and defined terminology;
- clear logical relations;
- claim-support connections;
- conformance boundaries.

### SLE-Research

Adds controls for:

- observation and interpretation;
- claim scope and evidence force;
- judgments and negative claims;
- attestation and stronger inferences;
- limitations, alternatives, and counterevidence;
- linguistic examples and provenance;
- dataset and transformation identity;
- system behavior versus language claims.

### SLE-Resource

Adds controls for:

- stable identifiers;
- resource scope and version;
- source and derived representations;
- annotation and transformation history;
- rights, consent, access, citation, and known issues where applicable.

Machine-readable exports are optional and are not part of basic profile conformance.

### SLE-Procedure

Adds controls for:

- declared normative verbal forms;
- conditions before actions;
- one principal action per step when practical;
- ordered procedures;
- exceptions, waivers, escalation, and completion criteria.

## Relationship between profiles and patterns

A profile selects rule groups. A pattern organizes a communicative purpose.

For example:

- a corpus study can use SLE-Research with SLE-PATTERN-0004;
- an annotation guide can use SLE-Procedure and SLE-Research with SLE-PATTERN-0007;
- a resource guide can use SLE-Resource with SLE-PATTERN-0010;
- a theoretical article can use SLE-Research with SLE-PATTERN-0003.

A document may use a pattern without declaring a profile. A publisher or project may define an extension that combines profiles and patterns.

## Proposed conformance states

### SLE-Prepared

The author applied the relevant SLE rules and patterns and completed a self-review.

### SLE-Reviewed

A human reviewer who did not author the reviewed passage checked the applicable rules and pattern elements. Material waivers and unresolved issues are recorded.

### SLE-Evaluated

The document or representative passages also underwent a defined reader, author-preservation, translation, accessibility, or domain-expert evaluation.

The declaration must name the evaluation type. *Evaluated* does not mean scientifically validated.

## Optional conformance declaration

A declaration may use ordinary prose. It should identify:

- SLE version;
- conformance object;
- applicable profile or profiles when declared;
- applicable document-pattern IDs;
- conformance state;
- material extensions and waivers;
- review date;
- controlling terminology source when required for interpretation.

Example:

> Sections 2–4 were reviewed against SLE for Linguistics v0.1 using SLE-Research and SLE-PATTERN-0004. The review covered claim scope, corpus provenance, evidence wording, and limitations. Two material waivers are listed in Appendix A. The review was completed on 2026-07-27.

A declaration must not imply that SLE verified the content's truth or scientific quality.

## Waivers

A material waiver must identify:

1. affected rule or pattern element;
2. affected text or scope;
3. reason;
4. interpretation or consistency risk;
5. mitigation or alternative control;
6. approval when required by a declared extension;
7. review or expiry condition when appropriate.

A waiver addresses communication conformance. It must not be used to hide missing evidence, a method defect, an ethical problem, a theoretical disagreement, or an unresolved data conflict.

## Extensions

A local extension must:

- identify the SLE version it extends;
- distinguish local requirements from SLE requirements;
- preserve core distinctions or declare an incompatibility;
- avoid presenting one theory, language, method, or workflow as universal;
- define how a document declares the extension.

## Optional tools

A tool may assist terminology, cross-reference, or editorial review.

A tool result is not a separate or superior conformance state. Tool availability is not required for ordinary SLE conformance.