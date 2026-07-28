---
title: "Canto-span Vocabulary Stress-Test Fixture v0.1"
type: test-fixture
status: proposed
normative_status: non-normative
version: "0.1"
created: 2026-07-27
updated: 2026-07-27
aliases:
  - "Canto-span Pilot Termbase v0.1"
  - "Canto-span Vocabulary Fixture"
tags:
  - ariadline
  - test-fixture
  - canto-span
  - terminology
  - non-normative
---

# Canto-span Vocabulary Stress-Test Fixture v0.1

> [!warning] Non-normative test material
> This package records Canto-span-specific vocabulary for stress-testing future Ariadline rules. It does not define Ariadline terminology, establish normative writing rules, or make Canto-span a model that other linguistic projects must copy.

## Purpose

The fixture records 46 Canto-span-specific meanings that are easy to collapse in documentation. The entries cover identity, ontology, linguistic status, evidence, corpus review, panel evidence, runtime behavior, verification, workflow, readiness, release authorization, and provenance.

The fixture has three permitted uses:

1. identify difficult communication problems;
2. test whether an independently proposed Ariadline rule preserves important distinctions;
3. support a later, separate effort to apply the completed Ariadline reference specification to Canto-span documentation.

It must not be used as normative evidence for Ariadline.

## Authority boundary

Canto-span is not a gold standard. No term, status system, workflow, ontology, schema, or governance rule in this fixture enters normative Ariadline merely because Canto-span uses it.

A general Ariadline rule or term requires independent justification across linguistic subfields, methods, theories, languages, document genres, and project types.

The intended direction of influence is:

```text
independent Ariadline design and multi-domain validation
        ↓
Ariadline reference specification
        ↓
optional later application to Canto-span documentation
```

The fixture must not create the reverse dependency.

## Test scope

- External test baseline: `Vazhi/canto-span` at `c9dd631739734a5ab886f0b667db9888b0add13b`
- Entry count: **46**
- Human-readable package: this index and its six linked parts
- Structured mirror: `06 Registers/Canto-span Pilot Termbase v0.1.tsv` manifest plus six part TSV files
- Status: **non-normative stress-test fixture v0.1**

The structured mirror exists only to reproduce and compare this test material. Machine-readable files are not required for the eventual Ariadline reference specification.

Each entry contains a preferred local designation, concept ID, project-local definition, scope, allowed variants, excluded interpretations, example, project-local owner or source, frozen test reference, and change status.

See [[Terminology Control]], [[Term Inventory]], [[Canto-span Case Study]], and [[Ariadline-GE Canto-span Pilot Baseline v0.1]].

## Fixture parts

| Part | Entries |
|---|---:|
| [[Canto-span Termbase — Identity and Governance]] | 11 |
| [[Canto-span Termbase — Status and Evidence]] | 16 |
| [[Canto-span Termbase — Corpus and Panel]] | 8 |
| [[Canto-span Termbase — Runtime and Verification]] | 4 |
| [[Canto-span Termbase — Workflow and Authorization]] | 6 |
| [[Canto-span Termbase — Provenance and Release]] | 1 |
| **Total** | **46** |

The legacy filenames retain the word `Termbase` for branch continuity. The normative status is controlled by this index and by the explicit notice in each part.

## Stress-test separations

| Project-local dimension | Fixture term | Must remain separate from |
|---|---|---|
| Permanent identity | construction identity | canonical name, status, runtime, readiness |
| Linguistic evidence | linguistic status | availability, runtime recognition, authorization |
| Software behavior | runtime recognition | attestation, productivity, speaker judgment |
| Work selection | available construction / parked construction | status, retirement, agent availability |
| Research prioritization | discovery readiness | promotion, assignment, authorization |
| Repository action | merge authorization | passing checks, review readiness, ownership |
| Publication action | release authorization | merge authorization, passing release checks, version metadata |

These distinctions are test cases. Future Ariadline may preserve, combine, rename, or reject them after independent review.

## Representation rule for the fixture

The six Markdown parts are the human-readable test record. The TSV manifest and six TSV parts are a structured mirror. Both forms must change in the same pull request while this fixture is maintained.

This local maintenance rule does not establish a general Ariadline requirement for machine-readable terminology.

## Reference contract

- `source_or_canonical_owner` identifies the Canto-span record or record class that owns the local meaning.
- `frozen_reference` identifies the exact artifact used to verify the fixture entry.
- A frozen reference must use `owner/repository@commit:path` and name a file, not only a directory.
- Multiple exact artifacts are separated with ` | `.
- Free-text placeholders, directory-only paths, and mutable collaboration pages are not valid frozen references.

A frozen reference supports reproducibility of the fixture. It does not transfer authority to Ariadline and does not make the referenced project state normative.

## Change control

- Preserve a concept ID when only the local preferred designation changes.
- Create a new concept ID when the project-local meaning changes materially.
- Record every change status.
- Do not silently import a Canto-span state change into the frozen fixture.
- Do not promote a fixture entry into normative Ariadline without a separate independent decision and evidence record.

## Validation requirements

- 46 unique entry IDs.
- 46 unique concept IDs.
- 46 unique preferred local terms within this fixture.
- The Markdown and TSV fixture records agree.
- All `frozen_reference` values satisfy the reference contract.
- Every fixture part states its non-normative status.
- All vault wikilinks resolve.

## Blockers and deviations

Issue #11 preserves the removed Ariadline test-run methods `source snapshot` and `release proxy`, records the historical authority inversion and software-first scope drift, and documents the package and navigation deviations.
