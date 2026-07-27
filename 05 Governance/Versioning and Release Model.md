---
title: "Versioning and Release Model"
type: governance
status: draft
created: 2026-07-27
updated: 2026-07-27
tags:
  - sle
  - governance
  - versioning
---
# Versioning and Release Model

## Version format

Use semantic versioning for the public standard:

`MAJOR.MINOR.PATCH`

### Major

A breaking change to core meaning, conformance, or identifiers.

### Minor

A backward-compatible addition, such as a new rule, term module, or optional profile.

### Patch

A correction that does not change intended normative meaning.

## Pre-release labels

- `0.1-alpha`
- `0.1-beta`
- `1.0-rc.1`

## Versioned components

Release these components together:

- standard text;
- rule inventory;
- termbase;
- profiles;
- test corpus;
- checker schema;
- change log;
- migration notes.

## Stable identifiers

Do not encode the version in a permanent rule or term identifier.

Examples:

- `SLE-RULE-0012`
- `SLE-TERM-0048`
- `SLE-TEST-0173`

The version record states when the identifier changed status or meaning.

## Compatibility policy

A release must state:

- whether old documents remain conformant;
- whether checker results can change;
- whether term definitions changed;
- whether a migration is required;
- whether a profile was added, changed, or retired.

## Publication package

Provide:

- Markdown source;
- rendered web or PDF form;
- machine-readable JSON or YAML;
- ZIP archive;
- checksums;
- release notes.
