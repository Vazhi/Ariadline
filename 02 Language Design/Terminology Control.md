---
title: "Terminology Control"
type: design
status: draft
created: 2026-07-27
updated: 2026-07-27
aliases:
  - "Term Control"
tags:
  - sle
  - language-design
  - terminology
---
# Terminology Control

## Objective

[[Terminology Control]] reduces ambiguity caused by synonyms, polysemy, framework-specific meanings, and unmarked shifts in analysis.

## Core policy

Within a declared scope:

- use one preferred designation for one defined concept;
- define terms that have multiple established meanings;
- record allowed variants;
- do not use a variant as if it were a different concept;
- do not use the same term for two concepts unless the text explicitly distinguishes the meanings.

## Project-scoped definitions

Linguistics contains legitimate theoretical disagreement. Therefore, SLE should not force one universal definition for every term.

A term entry can have:

- a core cross-project meaning;
- one or more framework-specific meanings;
- a project-specific selected meaning;
- prohibited interpretations for the current document.

## Term-entry fields

Use [[SLE Term Entry Template]].

Required fields:

- preferred term;
- definition;
- part of speech;
- concept identifier;
- scope;
- status;
- source;
- allowed variants;
- disallowed substitutions;
- examples;
- related terms.

## Priority term classes

The pilot should control terms that frequently cause evidential or analytical confusion:

- grammatical;
- acceptable;
- attested;
- productive;
- frequent;
- possible;
- construction;
- pattern;
- rule;
- category;
- feature;
- marker;
- particle;
- subject;
- object;
- argument;
- adjunct;
- dialect;
- variety;
- register.

See [[Attestation and Productivity]] and [[Term Inventory]].

## Term-change rule

A writer must not change a preferred term only to avoid repetition. Repetition is acceptable when a synonym could imply a different concept.

## Definition pattern

Preferred form:

> **TERM** means DEFINITION in this document.

Avoid circular definitions and undefined superordinate terms.

## Acceptance test

A controlled term is successful when independent readers map its uses to the intended concept with high agreement. See [[Evaluation Framework]].

## Non-normative Canto-span stress-test fixture

[[Canto-span Pilot Termbase v0.1]] is a project-specific vocabulary fixture used to test whether independently proposed SLE rules preserve difficult distinctions. It is not the SLE controlled vocabulary and does not establish normative terms or definitions.

Canto-span cannot define SLE. A general SLE term requires independent justification across linguistic subfields, methods, theories, languages, and document genres.
