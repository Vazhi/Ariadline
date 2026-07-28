---
title: "Vault Validation Report"
type: report
status: complete
created: 2026-07-27
updated: 2026-07-28
tags:
  - sle
  - validation
  - vault
---
# Vault Validation Report

- Markdown notes: 95
- Wikilinks checked: 613
- Duplicate note basenames: 0
- Broken wikilinks: 0

## Result

PASS — all current wikilinks resolve and all note basenames are unique.

## Validation scope

This report describes the issue #36 synthetic evaluation-operations dry-run package on top of the merged issue #9 preparation package.

The assembled reference package remains:

- [[SLE for Linguistics Reference Artifact v0.1 Draft]]
- [[SLE Reference Publication Map v0.1]]
- [[SLE Rule and Pattern Index v0.1]]
- [[SLE Reference Change and Deferral Log v0.1]]
- [[Glossary]]

The corrected corpus and preservation records remain:

- [[Multi-Domain SLE Evaluation Corpus v0.1]]
- [[Evaluation Corpus Items 0001–0004 v0.1]]
- [[Evaluation Corpus Items 0005–0008 v0.1]]
- [[Evaluation Corpus Items 0009–0012 v0.1]]
- [[Evaluation Corpus Items 0013–0016 v0.1]]
- [[Canto-span Evaluation Subset v0.1]]
- [[Evaluation Corpus Coverage Matrix v0.1]]
- [[Semantic Equivalence Review Record v0.1]]
- [[SLE Evaluation Corpus Bias Assessment v0.1]]
- [[SLE Semantic Equivalence Review Template v0.1]]

The editorial-review package remains:

- [[SLE Editorial Conformance Checklist v0.1]]
- [[SLE Rule Test Case Catalog v0.1]]
- [[Human Review Boundary Register v0.1]]
- [[SLE Rule Traceability Matrix v0.1]]
- [[Optional Automation Notes for SLE Review v0.1]]

Issue #9 preparation remains:

- [[Multi-Domain Reader and Author Evaluation Protocol v0.1]]
- [[Evaluation Material and Task Register v0.1]]
- [[Participant Sampling and Recruitment Plan v0.1]]
- [[Evaluation Data Dictionary and Privacy Plan v0.1]]
- [[Preregistered Analysis and Decision Plan v0.1|Analysis and Decision Plan Draft v0.1]]
- [[Evaluation Execution Status v0.1]]

Issue #36 adds:

- [[Evaluation Operations Dry-Run Package v0.1]]
- [[Material Intake and Authority Ledger Template v0.1]]
- [[Condition Development and Preservation Review Worksheet v0.1]]
- [[Operational Pilot Randomization Plan v0.1]]
- [[Evaluation Operations Validation Rules v0.1]]
- [[Participant Flow and Deviation Report Template v0.1]]
- [[Synthetic Evaluation Operations Fixture v0.1]]
- [[Evaluation Dry-Run Tool Instructions]]

## Count method

Merged `main` contained 87 Markdown notes and 574 wikilinks.

The merged baseline count already includes the issue #9 links from [[Evaluation Framework]], [[Pilot Study Design]], and [[Quality Metrics and Acceptance Gates]].

The issue #36 branch:

- adds eight uniquely named Markdown notes containing 23 wikilinks;
- adds eight links to the map of content;
- replaces the prior 29-link validation report with this 37-link report, for a net increase of eight.

Result: 95 Markdown notes and 613 wikilinks.

The eight Markdown notes are seven readable validation or template records and one uniquely named tool-instruction note. Python and JSON files are not included in the Markdown-note count.

Ordinary Markdown links and plain rule, pattern, profile, material, participant, condition, question, issue, path, and version IDs are not included in the wikilink total.

## Synthetic execution validation

The exact source committed on the branch was executed locally before upload.

- deterministic seed: `20260728`;
- valid fixture: zero findings and exit status 0;
- intentionally invalid fixture: 51 findings;
- expected invalid-code coverage: 13 of 13;
- missing expected codes: 0;
- unexpected codes: 0.

The valid and invalid JSON fixtures are generated outputs. The expected-code manifest is committed. Regeneration is deterministic under the recorded seed and source version.

## Data-model validation

The generator populates every operational table defined by the evaluation data plan:

- participants;
- materials;
- conditions;
- trials;
- responses;
- scoring;
- preservation;
- qualitative findings;
- protocol deviations.

All records are visibly fictional. No authentic passage, real participant, contact record, consent form, restricted material, or human approval is included.

## Condition and assignment validation

The valid dry run demonstrates:

- task-specific required condition sets;
- P and S availability for publication-relevant synthetic tasks;
- U limited to an admissible reader baseline;
- no participant exposure to multiple wording conditions from one meaning record;
- opaque masking codes;
- masked scoring records;
- no post-withdrawal assignments;
- Canto-span participant share at 10%;
- Canto-span trial share below 10%;
- `not determined` retained rather than converted to success.

These are structural tests only. They do not establish that P or S preserves authentic meaning or that a real assignment is fair, accessible, or scientifically valid.

## Invalid-fixture validation

The intentionally invalid fixture exercises:

- prohibited direct-identifier fields;
- broken participant and trial references;
- duplicate meaning-record exposure;
- prohibited U use;
- mask leakage;
- missing required P condition;
- unregistered trial conditions;
- confirmatory readiness without preservation;
- `not determined` recorded as success;
- post-withdrawal assignment;
- Canto-span participant and trial cap violations.

Extra row-level findings can occur when one injected fault affects several records. Expected-code coverage, not the total finding count, controls the self-test.

## Human authority boundary

The dry run cannot:

- approve oversight, consent, privacy, retention, or accessibility;
- grant material permission;
- identify legitimate source, translator, publisher, or community authority;
- certify meaning preservation;
- freeze statistical choices or preregister the study;
- recruit or supervise participants;
- classify rules from human evidence;
- advance the study state beyond preparation;
- support a `publish`, `revise`, or `stop` recommendation.

Human issues #30 through #35 remain open.

## Duplicate basenames

```json
{}
```

## Broken wikilinks

```json
[]
```
