---
title: "Canto-span Pilot Termbase v0.1 — Workflow and Authorization"
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

# Canto-span Pilot Termbase v0.1 — Workflow and Authorization

Part of [[Canto-span Pilot Termbase v0.1]]. These meanings are project-scoped and do not form a universal linguistic ontology.

## CS-TERM-0038 — available construction

- **Concept ID:** `CS-CONCEPT-AVAILABLE-CONSTRUCTION`
- **Definition:** a current construction that is not listed in the canonical parking registry and can receive bounded work.
- **Scope:** work selection.
- **Allowed variants:** available record.
- **Excluded interpretations:** supported construction; promotion-ready construction; assigned construction.
- **Example:** AA01 is available because it is current and not parked.
- **Canonical owner:** `data/parked-constructions.json`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:data/parked-constructions.json`
- **Change status:** `new_project_term`

## CS-TERM-0039 — parked construction

- **Concept ID:** `CS-CONCEPT-PARKED-CONSTRUCTION`
- **Definition:** a current construction temporarily excluded from normal work selection by the canonical parking registry.
- **Scope:** work selection and routing.
- **Allowed variants:** parked record.
- **Excluded interpretations:** retired construction; unsupported construction; disabled agent.
- **Example:** Parking AB30 prevents ordinary pickup but preserves its identity and status.
- **Canonical owner:** `data/parked-constructions.json`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:data/parked-constructions.json`
- **Change status:** `new_project_term`

## CS-TERM-0040 — discovery readiness

- **Concept ID:** `CS-CONCEPT-DISCOVERY-READINESS`
- **Definition:** a deterministic summary of missing evidence, boundary, ontology, or validation gates used to guide future work.
- **Scope:** canonical readiness data.
- **Allowed variants:** readiness state, discovery score.
- **Excluded interpretations:** promotion; assignment; authorization; linguistic support.
- **Example:** AB30 is boundary_ready and its next action is corpus review.
- **Canonical owner:** `canonical readiness data`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:validation/current/supported-productive-discovery.json`
- **Change status:** `new_project_term`

## CS-TERM-0041 — work claim

- **Concept ID:** `CS-CONCEPT-WORK-CLAIM`
- **Definition:** a bounded coordination record that reserves a semantic scope, owner, revision, branch, and pull request.
- **Scope:** multi-agent coordination.
- **Allowed variants:** coordination claim, semantic work claim.
- **Excluded interpretations:** issue assignment alone; merge authorization; file lock only.
- **Example:** The work claim reserves the A-not-A detector extraction scope for one branch.
- **Canonical owner:** `the matching open work claim and current intake ownership block`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:docs/current/MULTI-AGENT-COORDINATION.md`
- **Change status:** `new_project_term`

## CS-TERM-0042 — merge authorization

- **Concept ID:** `CS-CONCEPT-MERGE-AUTHORIZATION`
- **Definition:** explicit user approval for one pull request at one unchanged head commit.
- **Scope:** per-PR merge control.
- **Allowed variants:** merge approval.
- **Excluded interpretations:** passing checks; PR ownership; review readiness; absence of conflicts.
- **Example:** The user authorizes merge of PR #209 at head b802410.
- **Canonical owner:** `docs/current/USER-MERGE-REVIEW.md`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:docs/current/USER-MERGE-REVIEW.md`
- **Change status:** `new_project_term`

## CS-TERM-0043 — release authorization

- **Concept ID:** `CS-CONCEPT-RELEASE-AUTHORIZATION`
- **Definition:** explicit approval to perform the declared release or publication action after the applicable release gates pass.
- **Scope:** release governance.
- **Allowed variants:** release approval, publication authorization.
- **Excluded interpretations:** merge authorization; passing release checks; version metadata.
- **Example:** Release authorization applies to version 0.5.216 after the release gate is reviewed.
- **Canonical owner:** `docs/current/GOVERNANCE.md and release verification records`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:docs/current/GOVERNANCE.md`
- **Change status:** `new_project_term`
