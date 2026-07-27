---
title: "Vault Validation Report"
type: report
status: complete
created: 2026-07-27
updated: 2026-07-27
tags:
  - sle
  - validation
  - vault
---

# Vault Validation Report

- Markdown notes: 54
- Wikilinks checked: 286
- Duplicate note basenames: 0
- Broken wikilinks: 0

## Result

PASS — all current wikilinks resolve and all note basenames are unique.

## Validation scope

This report describes the branch after the addition, review repair, authority-scope correction, and boundary cleanup of the 46-entry Canto-span vocabulary stress-test fixture.

The package is non-normative test material. It does not define the SLE for Linguistics reference specification and does not make Canto-span a gold standard.

`manifest.json` remains the immutable manifest of the original ZIP import. Its 42-note and 182-wikilink counts describe that imported baseline, not later repository additions.

## Validation method

Relative to merged `main`, issue #3 adds seven uniquely named Markdown notes and 18 wikilinks:

- ten links in the fixture index;
- one backlink in each of the six fixture parts;
- one link from `Terminology Control`;
- one link from `Term Inventory`.

All referenced basenames are present. Six TSV part exports and one TSV manifest are non-Markdown structured test files and do not change the note count.

The 46 Markdown entries and 46 TSV rows were compared by entry ID and required field. The fixture includes all seven frozen Canto-span status literals and keeps status, readiness, availability, runtime, and authorization separate.

`source snapshot` and `release proxy` were removed because they are SLE test-run methods rather than Canto-span-specific vocabulary. They remain preserved in issue #11 and the locked pilot records.

The six TSV SHA-256 values use the exact UTF-8 file bytes with LF line endings and one terminal newline. Five unchanged hashes continue to reproduce. The revised provenance part contains only `CS-TERM-0046` and reproduces as `9ef0ccca6ca9208e92ae82b90ff8ae05e4590bfd68215add6cdf4be343cf1604`.

Every fixture `frozen_reference` identifies one or more exact commit-pinned Canto-span files. Authority descriptions remain in the separate `source_or_canonical_owner` field.

The fixture index, all six human-readable parts, the structured manifest, `Terminology Control`, and `Term Inventory` explicitly state the corrected non-normative authority boundary. The accidental temporary file is absent from the final branch diff.

The repository does not require an executable checker or terminology validator for completion of the SLE reference artifact. Any future validator is optional tooling and must be authorized as a separate project.

## Duplicate basenames

```json
{}
```

## Broken wikilinks

```json
[]
```
