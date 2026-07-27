---
title: "Versioning and Release Model"
type: governance
status: revised
created: 2026-07-27
updated: 2026-07-27
tags:
  - sle
  - governance
  - versioning
---
# Versioning and Release Model

## Purpose

Versioning identifies the controlling edition of the human-readable SLE for Linguistics reference artifact and explains compatibility effects.

The reference artifact is primary. Machine-readable representations and tools are optional supporting products.

## Version format

Use:

`MAJOR.MINOR.PATCH`

Pre-release editions may use labels such as:

- `0.1-alpha`;
- `0.1-beta`;
- `1.0-rc.1`.

## Major change

Increase the major version when a change:

- removes or changes a required distinction;
- changes the meaning of a normative rule, conformance state, waiver, or extension;
- changes a stable identifier's controlling meaning;
- makes a previously conforming document materially nonconforming;
- requires authors or publishers to migrate existing declarations.

## Minor change

Increase the minor version for a backward-compatible addition, such as:

- a new rule or document pattern;
- a new optional profile or annex;
- a new example set or editorial check;
- a new conformance option that does not invalidate prior declarations;
- a clarified control that adds an explicit requirement without changing the intended interpretation of earlier conforming text.

A proposed addition must be reviewed carefully before it is called backward-compatible.

## Patch change

Increase the patch version for a correction that does not change intended normative meaning, such as:

- typographic or formatting corrections;
- repaired cross-references;
- improved examples with the same rule boundary;
- source-link corrections;
- wording changes that remove ambiguity without changing conformance outcomes.

A change is not a patch when it changes scope, evidential force, a required distinction, or the result of an editorial review.

## Stable identifiers

Do not encode the release version in permanent identifiers.

Examples:

- `SLE-RULE-0012`;
- `SLE-PATTERN-0004`;
- `SLE-TERM-0048`;
- `SLE-TEST-0173`.

The version history states when an identifier was proposed, revised, stabilized, deprecated, or retired.

Do not reuse a retired identifier for a different concept.

## Versioned components

The public release should identify compatible versions of:

- reference specification text;
- rule inventory;
- document-pattern catalogue;
- controlled terminology modules when published;
- profiles and conformance guidance;
- example and boundary-case annexes;
- human editorial checklist;
- change log and migration guidance.

Evaluation corpora, machine-readable exports, schemas, and software tools may have separate versions. They must identify which reference-artifact version they support.

## Compatibility statement

Each release must state:

- whether prior conforming documents remain conformant;
- which rules, patterns, terms, profiles, or conformance states changed;
- whether any waiver or extension record must change;
- whether migration is required;
- whether translations or localized editions require revision;
- whether optional tools can produce different findings.

## Translation and localized editions

A translated or localized edition must identify:

- the controlling source edition;
- translation or localization version;
- known differences in normative verbal forms, terminology, examples, or rhetorical order;
- the authority responsible for resolving conflicts.

Translation must preserve normative function and required distinctions. It need not preserve English syntax or heading order.

## Urgent correction rule

A harmful, unsafe, discriminatory, factually misleading, or seriously ambiguous provision may require an urgent correction.

The release record must state whether the correction changes normative meaning. Urgency does not permit a normative change to be labelled as a patch merely to avoid migration.

## Publication package

A release must provide at least:

- a readable controlling edition;
- a stable public version identifier and date;
- a change log;
- compatibility and migration information;
- stable rule and pattern identifiers;
- accessible examples and declared annexes.

The controlling edition may be published as web pages, PDF, print, Markdown, or another durable readable format.

Optional supporting products may include:

- machine-readable JSON, YAML, XML, or tabular exports;
- downloadable archives and checksums;
- editorial tools;
- evaluation datasets;
- publisher integrations.

Failure to provide an optional supporting product does not make the human reference artifact incomplete.