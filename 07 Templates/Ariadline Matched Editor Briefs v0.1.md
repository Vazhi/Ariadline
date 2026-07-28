---
title: "Ariadline Matched Editor Briefs v0.1"
type: evaluation-template
status: planning-draft
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags: [ariadline, evaluation, editing, conditions]
---
# Ariadline Matched Editor Briefs v0.1

## Shared rule-neutral information packet

The following information must be identical for P and S:

- passage ID and source version;
- authorized meaning-record ID and version;
- document purpose and intended readership;
- a frozen rule-neutral description of the authentic communication risk;
- permitted degree of editing;
- protected terminology and quotations;
- source, community, privacy, and access restrictions;
- formatting and length constraints;
- deadline and time-recording method;
- allowed external resources;
- route for `not determined` questions.

The risk description must not contain `SLE-RULE-*` IDs, Ariadline terminology, an expected condition direction, or a condition-specific diagnosis.

Freeze and hash the shared packet before assignment. Record any later change as a deviation affecting both conditions.

An independent coordinator may preregister candidate-rule applicability for later analysis. Keep that mapping from both editors until editing and all editor-facing records are frozen.

## P — ordinary expert editing brief

You are performing competent ordinary expert editing. Improve clarity, precision, cohesion, and usability while preserving the authorized meaning and addressing the shared communication risk.

You may use your normal professional methods and the shared resources. You are not given the Ariadline candidate-rule register or any preregistered rule-applicability mapping.

You must:

- preserve claim content, scope, evidential force, uncertainty, examples, limitations, and access boundaries;
- avoid adding unsupported substantive information;
- identify questions you cannot resolve from the authorized record;
- return `not determined` rather than invent an answer;
- record editing time and major editorial actions.

Deliverables:

- edited P version and immutable version hash;
- change summary;
- unresolved questions;
- time record;
- resource-use record.

## S — Ariadline candidate-core editing brief

The legacy condition code `S` is retained for compatibility. Perform the same task, using the same shared information and professional resources as P.

You also receive:

- [[Ariadline Candidate Test Core Register v0.1]].

You do not receive the coordinator’s preregistered applicability mapping. Determine applicability from the shared packet and record your decisions during editing.

You must:

- apply only rules that you judge applicable and record the reason;
- preserve claim content, scope, evidential force, uncertainty, examples, limitations, and access boundaries;
- avoid adding substantive information not available to P;
- record when a rule adds burden, repetition, fragmentation, or unnaturalness;
- identify rule conflicts and return `not determined` when needed;
- record editing time and each material rule-driven action.

Deliverables:

- edited S version and immutable version hash;
- editor-generated applicability and rule-action log;
- change summary;
- unresolved questions;
- burden or conflict flags;
- time record;
- resource-use record.

## Editor assignment and contamination controls

- One editor must not produce both P and S for the same passage or meaning record.
- An editor must not see the other condition’s output, action log, unresolved questions, preservation record, or reader result.
- When an editor works in both conditions across different passages, register and counterbalance condition and order.
- Record prior Ariadline exposure, ordinary editing experience, subfield familiarity, language background, and any contamination concern.
- Any prohibited access or same-record carryover makes the pair `not comparable` unless the frozen protocol explicitly defines a narrower non-primary use.

## Comparability audit

Before preservation review, a masked coordinator records:

| Check | P | S | Result |
|---|---|---|---|
| Same source version | | | |
| Same meaning-record version | | | |
| Same rule-neutral risk brief | | | |
| Same substantive source information | | | |
| Same purpose and readership | | | |
| Same allowed resources | | | |
| Same length and formatting constraints | | | |
| Same time rules | | | |
| Different editors for the same meaning record | | | |
| No access to the other condition’s output or logs | | | |
| Cross-passage condition and order controls recorded | | | |
| Differences limited to candidate-core guidance | | | |

Allowed result: `comparable`, `not comparable`, or `not determined`.

A non-comparable pair cannot enter the primary S-versus-P analysis.

## Boundary

These briefs do not certify editor qualification, fairness, preservation, or study readiness. Those are human decisions.
