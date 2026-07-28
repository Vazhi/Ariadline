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

**Registration state:** `draft — not preregistered`

No participants have been recruited through this record. No outcome data have been collected. No rule has been classified from human-study evidence. No `publish`, `revise`, or `stop` recommendation is available.

## Prepared records

- [[Multi-Domain Reader and Author Evaluation Protocol v0.1]]
- [[Evaluation Material and Task Register v0.1]]
- [[Participant Sampling and Recruitment Plan v0.1]]
- [[Evaluation Data Dictionary and Privacy Plan v0.1]]
- [[Preregistered Analysis and Decision Plan v0.1|Analysis and Decision Plan Draft v0.1]]

## Lifecycle

Use these states:

1. `preparation` — protocol and materials are being drafted;
2. `administrative_review` — ethics, institutional, accessibility, community, publisher, or legal review is underway where applicable;
3. `material_authorization` — authentic sources, permissions, meaning records, and task-specific condition sets are being secured;
4. `pilot_ready` — constructed and approved materials can enter operational piloting;
5. `pilot_active` — cognitive or operational pilot is running;
6. `pilot_complete` — pilot is locked and reported;
7. `confirmatory_frozen` — main protocol, materials, required condition sets, sample target, scoring, analysis, and immutable preregistration are frozen;
8. `recruitment_active` — confirmatory recruitment is active;
9. `data_collection_active` — participant tasks are active;
10. `data_locked` — collection and frozen cleaning are complete;
11. `analysis_active` — confirmatory analysis is underway;
12. `analysis_complete` — results and limitations are recorded;
13. `disposition_pending` — rule actions and project recommendation await governance review;
14. `complete` — evidence-linked disposition and follow-up issues are published;
15. `stopped` — execution ended under a documented safety, authority, feasibility, or project stop decision.

A state change must identify date, responsible human role, evidence, immutable record when relevant, and unresolved blockers.

## Launch blockers

### Administrative and authority blockers

- applicable consent and oversight route not yet recorded;
- authentic source permissions not yet recorded;
- source-author, proxy, translator, or community meaning authority not yet secured;
- public-data and restricted-data release routes not yet approved;
- responsible study lead and data steward not yet recorded.

### Material blockers

- confirmatory `AUTH` records are not populated;
- task-specific required condition sets are not registered;
- ordinary expert-edited `P` conditions are not available;
- independently reviewed `S` conditions are not available;
- authorized `U` baselines are not registered where needed;
- non-English-original `TRANS` blocks are not available;
- authentic `GLOSS` blocks are not available;
- full-section `FULL` blocks are not available;
- independent preservation results are not available.

### Sampling blockers

- recruitment channels and responsible roles are not assigned;
- pilot sample is not recruited;
- main sample-size simulation or precision analysis is not complete;
- accessibility recruitment and accommodation route is not confirmed;
- compensation or recognition route is not confirmed where applicable.

### Analysis and registration blockers

- final primary outcome family is not frozen;
- exact estimands and model specifications are not frozen;
- smallest effects, safety margins, and adequacy thresholds are not human-approved;
- sample target is not frozen;
- multiplicity and subgroup plan is not frozen;
- scoring keys and adjudication training are not complete;
- material hashes or immutable versions are not frozen;
- immutable repository or external preregistration record does not exist.

## Current valid uses

The prepared package may be used to:

- recruit authorized material contributors;
- request administrative and ethics review;
- build and independently review P and S condition variants;
- authorize and document U baselines when a task needs them;
- train scorers on constructed examples;
- run operational tests after required authorization;
- estimate timing and task feasibility without making effectiveness claims;
- create transparent follow-up work items.

It must not be used to claim that SLE improves authentic writing, has completed preregistration, or is ready for stable publication.

## Required next records

Before `pilot_active`:

- material authorization ledger;
- participant-facing information and locally approved consent materials;
- pilot assignment schedule;
- frozen pilot scoring keys;
- accessibility test record;
- responsible study lead, data steward, and access list.

Before `confirmatory_frozen`:

- valid authentic material set;
- task-specific condition-set register;
- independent preservation register;
- human-approved sample-size simulation or precision analysis;
- immutable material and protocol versions;
- finalized statistical model, estimand, threshold, subgroup, and multiplicity plan;
- immutable preregistration identifier and date;
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
