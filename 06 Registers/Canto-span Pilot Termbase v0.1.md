---
title: "Canto-span Pilot Termbase v0.1"
type: termbase
status: proposed
version: "0.1"
created: 2026-07-27
updated: 2026-07-27
aliases:
  - "SLE-GE Canto-span Termbase"
  - "Canto-span Termbase"
tags:
  - sle
  - terminology
  - canto-span
  - grammar-engineering
  - pilot
---

# Canto-span Pilot Termbase v0.1

> [!abstract] Purpose
> This termbase controls 48 high-risk project meanings for the Canto-span SLE-GE pilot. It separates identity, ontology, linguistic status, evidence, corpus review, panel evidence, runtime behavior, verification, workflow, readiness, release, and authorization.

## Authority and scope

- External baseline: `Vazhi/canto-span` at `c9dd631739734a5ab886f0b667db9888b0add13b`
- Entry count: **48**
- Human-readable package: this index and its six linked parts
- Machine-readable export: `06 Registers/Canto-span Pilot Termbase v0.1.tsv` manifest plus six part TSV files
- Status: **proposed for pilot v0.1**

This termbase is project-scoped. It is not a universal linguistic ontology. It does not change Canto-span identity, status, evidence, runtime behavior, workflow, readiness, release state, or authorization.

Each entry contains a preferred term, concept ID, definition, scope, allowed variants, excluded interpretations, example, source or canonical owner, frozen reference, and change status.

See [[Terminology Control]], [[Term Inventory]], [[Canto-span Case Study]], and [[SLE-GE Canto-span Pilot Baseline v0.1]].

## Termbase parts

| Part | Entries |
|---|---:|
| [[Canto-span Termbase — Identity and Governance]] | 11 |
| [[Canto-span Termbase — Status and Evidence]] | 16 |
| [[Canto-span Termbase — Corpus and Panel]] | 8 |
| [[Canto-span Termbase — Runtime and Verification]] | 4 |
| [[Canto-span Termbase — Workflow and Authorization]] | 6 |
| [[Canto-span Termbase — Provenance and Release]] | 3 |
| **Total** | **48** |

## Required separations

| Dimension | Controlled term | Must remain separate from |
|---|---|---|
| Permanent identity | construction identity | canonical name, status, runtime, readiness |
| Linguistic evidence | linguistic status | availability, runtime recognition, authorization |
| Software behavior | runtime recognition | attestation, productivity, speaker judgment |
| Work selection | available construction / parked construction | status, retirement, agent availability |
| Research prioritization | discovery readiness | promotion, assignment, authorization |
| Repository action | merge authorization | passing checks, review readiness, ownership |
| Publication action | release authorization | merge authorization, release metadata, release proxy |

## Representation rule for the pilot

The six Markdown parts are the human-readable record. The TSV manifest and six TSV parts are the machine-readable mirror. Both forms must change in the same pull request.

This arrangement is a pilot workaround. The current SLE infrastructure does not specify whether the human or machine representation is canonical, and it does not provide a termbase generator or validator.

## Reference contract

- `source_or_canonical_owner` identifies the authority for the controlled meaning. It may name a dynamic owner class, such as the current status note or matching work claim.
- `frozen_reference` identifies the exact artifact used to verify the pilot definition.
- A Canto-span frozen reference must use `owner/repository@commit:path` and name a file, not only a directory.
- An SLE frozen reference must identify a commit-owned note at a fixed repository commit.
- Multiple exact artifacts are separated with ` | `.
- Free-text placeholders, directory-only paths, and mutable collaboration pages are not valid frozen references.

This contract separates authority from reproducibility. A frozen reference does not become the canonical owner of the external project state.

## Change control

- Preserve a concept ID when only the preferred designation changes.
- Create a new concept ID when the controlled meaning changes materially.
- Record every change status.
- Do not silently import a Canto-span state change into this frozen pilot termbase.

## Validation requirements

- 48 unique entry IDs.
- 48 unique concept IDs.
- 48 unique preferred terms within this scope.
- The Markdown and TSV records agree.
- All `frozen_reference` values satisfy the reference contract.
- All vault wikilinks resolve.

## Blockers and deviations

Issue #11 records the package decomposition, missing canonical-representation rule, absence of an executable generator or termbase validator, and the formal issue #3 amendment that permits the case-study link to remain one-directional in pilot v0.1.
