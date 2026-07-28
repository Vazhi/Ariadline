---
title: "Evaluation Execution Status v0.1"
type: evaluation-status
status: preparation
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - sle
  - evaluation
  - status
  - execution
---
# Evaluation Execution Status v0.1

## Current status

**Study state:** `not_started`

**Current recommendation:** `not determined — study not executed`

No participants have been recruited through this record. No outcome data have been collected. No rule has been classified from human-study evidence. No `publish`, `revise`, or `stop` recommendation is available.

## Prepared records

- [[Multi-Domain Reader and Author Evaluation Protocol v0.1]]
- [[Evaluation Material and Task Register v0.1]]
- [[Participant Sampling and Recruitment Plan v0.1]]
- [[Evaluation Data Dictionary and Privacy Plan v0.1]]
- [[Preregistered Analysis and Decision Plan v0.1]]

## Lifecycle

Use these states:

1. `preparation` — protocol and materials are being drafted;
2. `administrative_review` — ethics, institutional, accessibility, community, publisher, or legal review is underway where applicable;
3. `material_authorization` — authentic sources, permissions, and meaning records are being secured;
4. `pilot_ready` — constructed and approved materials can enter operational piloting;
5. `pilot_active` — cognitive or operational pilot is running;
6. `pilot_complete` — pilot is locked and reported;
7. `confirmatory_frozen` — main protocol, materials, sample target, scoring, and analysis are frozen;
8. `recruitment_active` — confirmatory recruitment is active;
9. `data_collection_active` — participant tasks are active;
10. `data_locked` — collection and preregistered cleaning are complete;
11. `analysis_active` — confirmatory analysis is underway;
12. `analysis_complete` — results and limitations are recorded;
13. `disposition_pending` — rule actions and project recommendation await governance review;
14. `complete` — evidence-linked disposition and follow-up issues are published;
15. `stopped` — execution ended under a documented safety, authority, feasibility, or project stop decision.

A state change must identify date, responsible role, evidence, and unresolved blockers.

## Launch blockers

### Administrative and authority blockers

- applicable consent and oversight route not yet recorded;
- authentic source permissions not yet recorded;
- source-author, proxy, translator, or community meaning authority not yet secured;
- public-data and restricted-data release routes not yet approved.

### Material blockers

- confirmatory `AUTH` records are not populated;
- ordinary expert-edited `P` conditions are not available;
- non-English-original `TRANS` blocks are not available;
- authentic `GLOSS` blocks are not available;
- full-section `FULL` blocks are not available;
- independent preservation results are not available.

### Sampling blockers

- recruitment channels and responsible roles are not assigned;
- pilot sample is not recruited;
- main sample-size simulation is not complete;
- accessibility recruitment and accommodation route is not confirmed.

### Analysis blockers

- final primary outcome family is not frozen;
- exact model specification is not frozen;
- sample target is not frozen;
- scoring keys and adjudication training are not complete;
- material hashes or immutable versions are not frozen.

## Current valid uses

The prepared package may be used to:

- recruit authorized material contributors;
- request administrative and ethics review;
- build and independently review condition variants;
- train scorers on constructed examples;
- run operational tests after required authorization;
- estimate timing and task feasibility without making effectiveness claims;
- create transparent follow-up work items.

It must not be used to claim that SLE improves authentic writing or is ready for stable publication.

## Required next records

Before `pilot_active`:

- material authorization ledger;
- participant-facing information and locally approved consent materials;
- pilot assignment schedule;
- frozen pilot scoring keys;
- accessibility test record;
- responsible data steward and access list.

Before `confirmatory_frozen`:

- valid authentic material set;
- independent preservation register;
- sample-size simulation or precision analysis;
- immutable material and protocol versions;
- finalized statistical model and multiplicity plan;
- finalized data-retention and public-release decision.

## Completion evidence

The study can become `complete` only when the repository contains or links to:

- recruitment and participant-flow summary;
- material coverage summary;
- anonymized dataset or publishable aggregate where appropriate;
- scoring and adjudication report;
- confirmatory and exploratory analysis;
- rule-level classifications;
- domain-gap and participant-gap analysis;
- protocol deviations;
- explicit evidence-linked `publish`, `revise`, or `stop` recommendation;
- epic #1 disposition update;
- follow-up issues for unresolved findings.

## Canto-span boundary

Canto-span execution state is recorded separately. Completion of its arm cannot advance the overall study to `analysis_complete` or `complete` when independent multi-domain execution is missing.
