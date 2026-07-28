---
title: "Evaluation Operations Dry-Run Package v0.1"
type: evaluation-operations-package
status: proposed-synthetic
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - sle
  - evaluation
  - automation
  - synthetic
---
# Evaluation Operations Dry-Run Package v0.1

## Status and authority

This package supports issue #36 and the preparation stage of [[Multi-Domain Reader and Author Evaluation Protocol v0.1]].

It uses only fictional participants, constructed material identifiers, synthetic responses, and synthetic findings. It is not participant evidence, authentic linguistic evidence, ethics approval, permission, meaning authority, preservation certification, preregistration, or a project disposition.

The controlling human boundaries remain in [[Evaluation Execution Status v0.1]], [[Evaluation Data Dictionary and Privacy Plan v0.1]], and [[Human Review Boundary Register v0.1]].

## Package contents

### Readable templates

- [[Material Intake and Authority Ledger Template v0.1]]
- [[Condition Development and Preservation Review Worksheet v0.1]]
- [[Operational Pilot Randomization Plan v0.1]]
- [[Evaluation Operations Validation Rules v0.1]]
- [[Participant Flow and Deviation Report Template v0.1]]
- [[Synthetic Evaluation Operations Fixture v0.1]]

### Optional machine-readable support

- `tools/evaluation/generate_dry_run.py`
- `tools/evaluation/validate_dry_run.py`
- `tools/evaluation/README.md`
- `fixtures/evaluation-dry-run/v0.1/valid_fixture.json`
- `fixtures/evaluation-dry-run/v0.1/invalid_fixture.json`
- `fixtures/evaluation-dry-run/v0.1/expected_invalid_codes.json`

Software is optional. The readable records remain usable without running code.

## Reproducible dry run

From the repository root:

```bash
python3 tools/evaluation/generate_dry_run.py

python3 tools/evaluation/validate_dry_run.py \
  fixtures/evaluation-dry-run/v0.1/valid_fixture.json

python3 tools/evaluation/validate_dry_run.py \
  fixtures/evaluation-dry-run/v0.1/invalid_fixture.json \
  --expect-codes fixtures/evaluation-dry-run/v0.1/expected_invalid_codes.json
```

Expected result:

- the valid fixture reports `PASS` with zero findings;
- the intentionally invalid fixture reports findings for every listed expected code;
- neither result changes the study state from `not_started`.

## What the automation checks

The validator can check:

- required tables and stable identifiers;
- foreign-key consistency;
- task-specific condition registration;
- mandatory P-versus-S availability for publication-relevant synthetic tasks;
- U use only when the task registers an admissible baseline;
- repeated exposure to multiple wording conditions from one meaning record;
- opaque masking codes;
- scorer masking state;
- withdrawal-order violations;
- Canto-span participant and trial caps;
- prohibited direct-identifier fields in the participant table;
- invalid preservation-state transitions;
- conversion of `not determined` into success.

## What it cannot check

The validator cannot establish:

- whether human review or consent is legally or ethically sufficient;
- whether an authentic source may be used;
- what an author, translator, publisher, or community intended;
- whether P or S preserves authentic meaning;
- whether a statistical model or threshold is scientifically appropriate;
- whether recruitment is fair or accessible in practice;
- whether SLE helps real readers or authors;
- whether the project should `publish`, `revise`, or `stop`.

Those decisions remain assigned to human issues #30 through #35.

## Data-model coverage

The synthetic fixture covers every table defined by [[Evaluation Data Dictionary and Privacy Plan v0.1]]:

1. participant;
2. material and condition;
3. trial;
4. response;
5. scoring;
6. authoring and preservation;
7. qualitative finding;
8. protocol deviation.

The fixture also records task registration, masking, assignment order, synthetic accessibility state, and expected validation failures.

## Use restriction

Do not merge synthetic rows into any real study dataset. Do not replace fictional identifiers with real identifying information in the committed fixture. Use a separate approved restricted environment for actual contact, consent, participant-key, authentic-material, or community-controlled records.
