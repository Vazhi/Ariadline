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

- Markdown notes: 45
- Wikilinks checked: 264
- Duplicate note basenames: 0
- Broken wikilinks: 0

## Result

PASS — all wikilinks resolve and all note basenames are unique.

## Validation scope

This report describes the current Markdown vault after the addition of the Canto-span case study, construction-level worked example, and locked SLE-GE pilot baseline.

`manifest.json` remains the immutable manifest of the original ZIP import. Its 42-note and 182-wikilink counts describe that imported baseline, not later repository additions.

## Validation method

The issue #2 branch adds one uniquely named Markdown note and 24 wikilinks: 21 in the new baseline, one in the MOC, one in the evaluation framework, and one in the pilot-study design. Every target basename is present in the current vault.

The repository does not yet contain an executable branch-aware vault validator. This manual validation limitation is recorded as DEV-014 in issue #11.

## Duplicate basenames

```json
{}
```

## Broken wikilinks

```json
[]
```
