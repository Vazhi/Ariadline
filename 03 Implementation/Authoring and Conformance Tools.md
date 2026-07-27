---
title: "Authoring and Conformance Tools"
type: implementation
status: draft
created: 2026-07-27
updated: 2026-07-27
tags:
  - sle
  - implementation
  - tooling
---
# Authoring and Conformance Tools

## Tooling objective

Software should identify likely violations and provide evidence for revision. It should not silently rewrite a linguistic claim.

## Minimum viable checker

The first checker should detect or assist with:

- undefined abbreviations;
- inconsistent preferred terms;
- prohibited synonym substitutions;
- ambiguous pronouns after multiple candidate antecedents;
- long sentences with multiple finite clauses;
- weak evidence phrases;
- undefined judgment symbols;
- missing example identifiers;
- inconsistent gloss abbreviations;
- missing conformance declarations;
- invalid internal cross-references.

## Checker result classes

- **error** — deterministic violation of a machine-checkable rule;
- **warning** — probable problem that requires human review;
- **notice** — optional improvement;
- **not checked** — rule requires human judgment.

## Author control

The tool must show:

- the rule identifier;
- the text span;
- the reason;
- compliant examples;
- permitted exceptions;
- the method to record a waiver.

## Tool architecture

Proposed components:

1. Markdown and plain-text parser;
2. sentence and token analyzer;
3. project termbase;
4. rule engine;
5. example-block validator;
6. report generator;
7. editor integration.

## Obsidian workflow

The project vault can use:

- YAML frontmatter for status and identifiers;
- wikilinks for concepts and decisions;
- templates for rules and tests;
- Dataview-compatible fields for inventories;
- Git for version control;
- automated link and schema validation.

## Rewriting constraint

Automated suggestions must preserve:

- claim class;
- polarity;
- quantifier;
- evidence strength;
- scope;
- named entities;
- examples and citations.

Any uncertain rewrite must be presented as a proposal, not an automatic correction.
