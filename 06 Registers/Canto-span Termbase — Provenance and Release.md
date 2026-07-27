---
title: "Canto-span Pilot Termbase v0.1 — Provenance and Release"
type: termbase-part
status: proposed
version: "0.1"
created: 2026-07-27
updated: 2026-07-27
tags:
  - sle
  - terminology
  - canto-span
  - termbase-part
---

# Canto-span Pilot Termbase v0.1 — Provenance and Release

Part of [[Canto-span Pilot Termbase v0.1]]. These meanings are project-scoped and do not form a universal linguistic ontology.

## CS-TERM-0044 — source snapshot

- **Concept ID:** `CS-CONCEPT-SOURCE-SNAPSHOT`
- **Definition:** an immutable captured copy of mutable external text with source URL, capture date, associated commit or state, and content hash.
- **Scope:** SLE pilot materials that use mutable collaboration records.
- **Allowed variants:** snapshot record.
- **Excluded interpretations:** canonical owner; live source page; ordinary quotation.
- **Example:** The PR #209 body is stored as a hashed source snapshot for the pilot.
- **Canonical owner:** `the SLE pilot baseline snapshot record`
- **Frozen reference:** `Vazhi/simplified-linguistic-english:04 Validation/Source Snapshots/`
- **Change status:** `new_project_term`

## CS-TERM-0045 — release proxy

- **Concept ID:** `CS-CONCEPT-RELEASE-PROXY`
- **Definition:** an explicitly labelled substitute artifact set used when the required release-note document class is absent.
- **Scope:** the SLE-GE pilot baseline only.
- **Allowed variants:** release-facing proxy.
- **Excluded interpretations:** original release note; release authorization; current project state.
- **Example:** The pinned manifest and PR #177 snapshot form the approved release proxy set.
- **Canonical owner:** `docs/current/GOVERNANCE.md and release verification records`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:docs/current/GOVERNANCE.md`
- **Change status:** `new_project_term`

## CS-TERM-0046 — historical provenance

- **Concept ID:** `CS-CONCEPT-HISTORICAL-PROVENANCE`
- **Definition:** a record that explains an earlier state or decision without controlling current state.
- **Scope:** research records, immutable reports, retired records, closed collaboration records, and Git history.
- **Allowed variants:** provenance record, historical record.
- **Excluded interpretations:** current authority; canonical owner.
- **Example:** The merged PR explains why the detector moved, but current runtime source owns present behavior.
- **Canonical owner:** `research records, immutable reports, retired records, and Git history`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:historical records and Git history`
- **Change status:** `new_project_term`
