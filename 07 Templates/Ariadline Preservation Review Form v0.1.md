---
title: "Ariadline Preservation Review Form v0.1"
type: evaluation-template
status: planning-draft
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags: [ariadline, evaluation, preservation, adjudication]
---
# Ariadline Preservation Review Form v0.1

Use one masked form per passage-condition pair. Reviewers must not be told whether the text is P or S.

Reviewers receive only the masked edited text, the authorized meaning record, and the restrictions needed to judge preservation. They must not receive condition labels, `SLE-RULE-*` IDs, editor identity, action logs, unresolved-question records, expected direction, or the other condition’s output.

## Record identity

- Passage ID:
- Masked condition code:
- Edited version ID:
- Edited version hash:
- Authorized meaning-record ID and version:
- Reviewer ID:
- Reviewer authority or qualification basis:
- Masking check: `pass`, `fail`, or `not determined`
- Review date:

## Dimension review

Allowed results: `preserved`, `not preserved`, `not determined`, `not applicable`.

| Dimension | Result | Severity | Evidence and explanation |
|---|---|---|---|
| Central claim content | | | |
| Claim scope | | | |
| Evidential force | | | |
| Uncertainty and modality | | | |
| Comparison structure | | | |
| Antecedent and logical scope | | | |
| Examples and provenance | | | |
| Dataset and transformation identity | | | |
| Limitations and counterevidence | | | |
| Claim-support connection | | | |
| Theory-sensitive terminology | | | |
| Community-sensitive meaning | | | |
| Permission and access boundaries | | | |
| Other authorized meaning | | | |

Severity: `critical`, `major`, `minor`, `editorial`, or `not applicable`.

## Deterministic overall result

- `not preserved` is required when any applicable dimension contains a critical or major non-preservation.
- `not determined` is required when any material dimension remains unresolved, unless another material dimension already requires `not preserved`.
- `preserved` is permitted only when every applicable material dimension is preserved and every minor or editorial difference is explicitly confirmed nonmaterial.
- Dimension results must not be averaged to override a material loss or uncertainty.

Overall result:

- `preserved`
- `not preserved`
- `not determined`

Aggregation evidence:

## Source-author or authority confirmation

Required when the registered authority route calls for it.

- Requested: yes/no
- Authority ID:
- Confirmation result:
- Disputed points:
- Restrictions on disclosure:

## Independent review agreement

- Second reviewer result:
- Agreement: yes/no/partial
- Disagreement dimensions:
- Adjudication required: yes/no

## Adjudication

Adjudicators must remain masked to condition, rule IDs, editor identity, and action logs where practical. Any unmasking must be authorized, timed, and recorded as a deviation.

- Adjudicator IDs:
- Masking state:
- Material reviewed:
- Final result:
- Final severity:
- Reason:
- Dissent retained:
- Revision permitted under the frozen protocol: yes/no
- If revised, new version, hash, and repeat-review requirement:

## Condition and pair eligibility

- Condition eligible for reader exposure: yes/no/not determined
- Condition eligible for benefit analysis: yes/no/not determined
- Paired P/S comparison eligible: yes/no/not determined
- Adverse preservation result retained: yes/no
- Exclusion or deviation record:

A condition with overall `not preserved` or `not determined` cannot enter benefit analysis. If either member of the P/S pair is ineligible, the pair cannot enter the primary S-versus-P benefit comparison. The adverse result remains reportable.

## Boundary

Automation may check that fields exist. Only authorized humans can judge preservation. `Not determined` must never be recoded as success.
