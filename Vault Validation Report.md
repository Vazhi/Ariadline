---
title: "Vault Validation Report"
type: report
status: complete
created: 2026-07-27
updated: 2026-07-28
tags:
  - ariadline
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

- [[Ariadline Reference Artifact v0.1 Draft]]
- [[Ariadline Reference Publication Map v0.1]]
- [[Ariadline Rule and Pattern Index v0.1]]
- [[Ariadline Reference Change and Deferral Log v0.1]]
- [[Glossary]]

The corrected corpus and preservation records remain:

- [[Multi-Domain Ariadline Evaluation Corpus v0.1]]
- [[Evaluation Corpus Items 0001–0004 v0.1]]
- [[Evaluation Corpus Items 0005–0008 v0.1]]
- [[Evaluation Corpus Items 0009–0012 v0.1]]
- [[Evaluation Corpus Items 0013–0016 v0.1]]
- [[Canto-span Evaluation Subset v0.1]]
- [[Evaluation Corpus Coverage Matrix v0.1]]
- [[Semantic Equivalence Review Record v0.1]]
- [[Ariadline Evaluation Corpus Bias Assessment v0.1]]
- [[Ariadline Semantic Equivalence Review Template v0.1]]

The editorial-review package remains:

- [[Ariadline Editorial Conformance Checklist v0.1]]
- [[Ariadline Rule Test Case Catalog v0.1]]
- [[Human Review Boundary Register v0.1]]
- [[Ariadline Rule Traceability Matrix v0.1]]
- [[Optional Automation Notes for Ariadline Review v0.1]]

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

The reviewed implementation layer was exercised locally against the original dry-run base API after blocker repair.

- deterministic seed: `20260728`;
- valid fixture: zero findings;
- expected invalid-code coverage: 34 of 34;
- missing expected codes: 0;
- unexpected codes: 0;
- expected-invalid success requires exact distinct-code agreement.

The valid and invalid JSON fixtures are generated outputs. The 34-code expected manifest is committed. Regeneration is deterministic under the recorded seed and source version.

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

The reviewed valid dry run demonstrates:

- 20 active fictional participants and one separately retained withdrawn row;
- 16 exposures for every core material;
- task-specific required condition sets;
- P and S availability for publication-relevant synthetic tasks;
- U limited to an admissible reader baseline;
- 6 P, 6 S, and 4 U assignments for that baseline;
- 8 P and 8 S assignments for every other core material;
- P/S difference at most 1 for every order position;
- no participant exposure to multiple wording conditions from one meaning record;
- exact agreement between trial masks and registered material-condition masks;
- masked scoring records;
- no post-withdrawal assignments;
- Canto-span contributor and trial shares below 10%;
- `not determined` retained rather than converted to success.

These are structural tests only. They do not establish that P or S preserves authentic meaning or that a real assignment is fair, accessible, or scientifically valid.

## Invalid-fixture validation

The intentionally invalid fixture exercises all 34 registered validation classes across:

- evidence and authenticity boundaries;
- missing tables;
- invalid and duplicate identifiers;
- broken participant, material, and trial references;
- condition and trial meaning mismatches;
- universal, missing, unregistered, and prohibited conditions;
- duplicate meaning exposure;
- condition and order imbalance;
- mask leakage, duplication, and registered-mask mismatch;
- unmasked scoring;
- invalid preservation readiness and uncertainty downgrading;
- post-withdrawal assignment;
- duplicate deviations;
- Canto-span participant and trial cap violations.

One injected fault can create several row-level findings. The distinct code set, not the total row count, controls the self-test. Missing and unexpected codes both fail the expected-invalid command.

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
