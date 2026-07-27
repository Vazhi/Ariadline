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

- Markdown notes: 47
- Wikilinks checked: 268
- Duplicate note basenames: 0
- Broken wikilinks: 0

## Result

PASS — all wikilinks resolve and all note basenames are unique.

## Validation scope

This report describes the current Markdown vault after the addition of the Canto-span case study, construction-level worked example, locked SLE-GE pilot baseline, and two immutable PR-body snapshots.

`manifest.json` remains the immutable manifest of the original ZIP import. Its 42-note and 182-wikilink counts describe that imported baseline, not later repository additions.

## Validation method

Relative to `main`, the issue #2 branch adds three uniquely named Markdown notes and 28 wikilinks: 23 in the pilot baseline, one in each source snapshot, one in the MOC, one in the evaluation framework, and one in the pilot-study design. Every target basename is present in the current vault.

The repository does not yet contain an executable branch-aware vault validator. This manual validation limitation is recorded as DEV-014 in issue #11.

## Duplicate basenames

```json
{}
```

## Broken wikilinks

```json
[]
```
