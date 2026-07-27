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

This report describes the branch after the addition, review repair, and authority-scope correction of the 48-entry Canto-span vocabulary stress-test fixture.

The package is non-normative test material. It does not define the SLE for Linguistics reference specification and does not make Canto-span a gold standard.

`manifest.json` remains the immutable manifest of the original ZIP import. Its 42-note and 182-wikilink counts describe that imported baseline, not later repository additions.

## Validation method

Relative to merged `main`, issue #3 adds seven uniquely named Markdown notes and 18 wikilinks:

- ten links in the fixture index;
- one backlink in each of the six fixture parts;
- one link from `Terminology Control`;
- one link from `Term Inventory`.

All referenced basenames are present. Six TSV part exports and one TSV manifest are non-Markdown structured test files and do not change the note count.

The 48 Markdown entries and 48 TSV rows were compared by entry ID and required field. The review repair adds `provisional_reaudit` and `provisional`, corrects `research_pending`, and updates exact frozen references in both representations.

The six TSV SHA-256 values were recalculated over the exact UTF-8 file bytes with LF line endings and one terminal newline. The manifest records that hash contract. All six recorded hashes reproduce for the reviewed entry content.

Every `frozen_reference` identifies one or more exact commit-pinned files or exact SLE commit-owned notes. Authority descriptions remain in the separate `source_or_canonical_owner` field.

The fixture index, all six human-readable parts, the structured manifest, `Terminology Control`, and `Term Inventory` explicitly state the corrected non-normative authority boundary. The accidental temporary file is absent from the final branch diff.

The repository does not require an executable checker or termbase validator for completion of the SLE reference artifact. Any future validator is optional tooling and must be authorized as a separate project.

## Duplicate basenames

```json
{}
```

## Broken wikilinks

```json
[]
```
