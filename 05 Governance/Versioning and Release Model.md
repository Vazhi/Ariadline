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

Conformance terminology and profile resolution are defined in [[Profiles and Conformance]] and [[SLE Profile Applicability Register v0.1]].

## Version format

Use:

`MAJOR.MINOR.PATCH`

Pre-release editions may use labels such as:

- `0.1-alpha`;
- `0.1-beta`;
- `1.0-rc.1`.

## Compatibility principle

Version class follows the effect on normative meaning and prior conformance outcomes. It does not follow the file type, number of edited lines, or label applied to the change request.

Before assigning a version class, determine:

1. whether the change creates, removes, or changes a normative obligation;
2. whether the applicable rule or profile set changes;
3. whether a document that conformed to the prior edition can keep the same result under the new edition without revision;
4. whether declarations, waivers, extensions, or translations require migration.

## Major change

Increase the major version when a change:

- removes or changes a required distinction;
- creates a new mandatory obligation in an existing profile and can change prior conformance outcomes;
- changes the meaning of a normative rule, conformance result, waiver, extension, or profile mapping;
- changes a stable identifier's controlling meaning;
- makes a previously conforming document materially nonconforming under the new edition;
- requires authors or publishers to migrate existing declarations.

A change remains major even when it is described as a clarification, new rule, new pattern element, or editorial improvement.

## Minor change

Increase the minor version only for a backward-compatible addition that does not change prior conformance outcomes.

Examples include:

- a new optional pattern, profile, annex, example set, or editorial aid;
- a new rule placed only in a new optional profile;
- an additional evaluation type or review form that does not change the conformance result;
- added explanatory text that does not create a new obligation;
- a transition mechanism that explicitly preserves prior declarations and does not silently expand an existing profile.

A new rule is not automatically minor. A newly explicit requirement is not minor when it changes what an existing profile requires.

## Non-breaking transition mechanism

A normative addition can avoid an immediate major change only when the release explicitly uses a non-breaking mechanism, such as:

- placing the obligation in a new optional profile;
- publishing it as proposed or recommended rather than required;
- setting a future effective major edition while preserving current declarations;
- versioning a local extension separately from core SLE.

The release record must state who remains covered by the prior requirement set, for how long, and how migration will occur.

## Patch change

Increase the patch version for a correction that does not change intended normative meaning or any conformance result, such as:

- typographic or formatting corrections;
- repaired cross-references;
- source-link corrections;
- improved examples with the same rule boundary;
- wording that removes ambiguity without changing applicable obligations or editorial outcomes.

A change is not a patch when it changes scope, evidential force, a required distinction, profile membership, applicability, or the result of a review.

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

The public release must identify compatible versions of:

- reference specification text;
- rule inventory;
- document-pattern catalogue;
- profile applicability register;
- controlled terminology modules when published;
- profiles and conformance guidance;
- example and boundary-case annexes;
- human editorial checklist;
- change log and migration guidance.

Evaluation corpora, machine-readable exports, schemas, and software tools may have separate versions. They must identify which reference-artifact version they support.

## Compatibility statement

Each release must state:

- whether prior conforming documents retain the same result under the new edition;
- which rules, patterns, terms, profile mappings, conformance results, or review requirements changed;
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

Translation must preserve normative function and required distinctions. It need not preserve English syntax, heading names, or recommended sequence.

## Urgent correction rule

A harmful, unsafe, discriminatory, factually misleading, or seriously ambiguous provision may require an urgent correction.

The release record must state whether the correction changes normative meaning. Urgency does not permit a major normative change to be labelled as a patch merely to avoid migration.

## Publication package

A release must provide at least:

- a readable controlling edition;
- a stable public version identifier and date;
- a change log;
- compatibility and migration information;
- stable rule and pattern identifiers;
- profile-set identity;
- accessible examples and declared annexes.

The controlling edition may be published as web pages, PDF, print, Markdown, or another durable readable format.

Optional supporting products may include:

- machine-readable JSON, YAML, XML, or tabular exports;
- downloadable archives and checksums;
- editorial tools;
- evaluation datasets;
- publisher integrations.

Failure to provide an optional supporting product does not make the human reference artifact incomplete.
