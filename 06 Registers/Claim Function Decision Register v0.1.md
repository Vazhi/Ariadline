---
title: "Claim Function Decision Register v0.1"
type: decision-register
status: proposed
version: "0.1"
created: 2026-07-27
updated: 2026-07-27
tags:
  - sle
  - claims
  - decisions
  - neutrality
---
# Claim Function Decision Register v0.1

## Purpose

This register evaluates the candidate claim-function codes from [[Claim-Evidence Matrix]].

The functions are editorial concepts. [[SLE for Linguistics Language Rules v0.1]] does not require visible labels in normal prose.

A function can help a writer identify missing information. It does not determine whether a claim is true.

## Decision meanings

- **adopt:** retain the distinction as a general editorial function;
- **revise:** retain a narrower or differently organized distinction;
- **merge:** express the function as a subtype or property of another function;
- **defer:** keep for later study without a normative decision;
- **reject:** do not include as a general SLE function.

## Decisions

| Candidate | Original idea | Decision | Result |
|---|---|---|---|
| OBS | observation | adopt | A directly recorded result under a stated method and scope. Visible label optional. |
| ATT | attestation | revise | Retain as a subtype of observation for an identified occurrence in a source, dataset, or participant record. |
| JUD | judgment result | adopt | A response collected under a stated task, population, item scope, and response system. |
| GEN | generalization | adopt | A claim extending beyond individual records; scope and boundary must be explicit. |
| ANA | analysis | adopt | An interpretation under stated assumptions or a framework. |
| HYP | hypothesis | adopt | A provisional claim linked to predicted observations or revision conditions. |
| NEG | negative claim | merge | Treat as a polarity and evidence-boundary property of observation or generalization, governed by SLE-RULE-0021. |
| SYS | system behavior | adopt | Output or action of a specified tool, version, input, and configuration. |
| DEF | definition | adopt | A controlled statement of term scope and distinguishing criteria. |
| LIM | limitation | adopt | A statement that narrows the scope, force, or applicability of another claim. |
| REQ | requirement | adopt | Use only in normative or procedural documents with a declared verbal-form system. |
| DEC | decision | defer | Project decisions are important, but a general linguistic-writing function has not been established. |
| STA | state/status | reject | The category is too broad. A document must name the state dimension instead of using a generic status function. |

## Required information by adopted function

| Function | Minimum information |
|---|---|
| Observation | source or object, method, unit, result, scope |
| Attestation | exact form or item, source, location or retrieval method, relevant context |
| Judgment result | task, response system, population, item scope, result |
| Generalization | target domain, evidence basis, boundary, counterevidence policy |
| Analysis | assumptions or framework, analyzed material, inferential relation |
| Hypothesis | proposed relation, predicted observation, possible falsifier or revision condition |
| System behavior | system and version, input, configuration, output |
| Definition | preferred term, scope, distinguishing criteria |
| Limitation | affected claim, restricted scope or force, consequence |
| Requirement | actor or object, required action or condition, conformance scope, declared verbal form |

## Visible-label decision

Visible labels such as `[OBS]` or `[ANA]` are not required for basic conformance.

Reasons:

1. prose can usually express the distinction directly;
2. labels can interrupt reading;
3. a fixed label set can import a theory or workflow;
4. labels can create false confidence when required information is still missing;
5. labels can be useful during drafting, annotation, teaching, or evaluation.

A profile may permit or require labels for a defined workflow, but the profile must define the labels and must not claim that the labels establish evidential adequacy.

## Evidence-wording decision

The functions in this register do not impose a universal hierarchy for evidence verbs.

Terms such as *shows*, *supports*, *suggests*, *is consistent with*, *does not establish*, and *contradicts* can have different force in different disciplines and argument types. SLE-RULE-0020 controls overstatement, not a fixed lexical scale.

A document should define an evidence expression when its force is important and not clear from context.

## Neutrality review

The adopted functions do not assume a particular theory, model of grammaticality, experimental design, corpus-first or judgment-first method, computational implementation, or repository governance model.

The functions describe communicative roles, not linguistic entities.

## Relationship to the term inventory

The general concepts should use definitions in [[Term Inventory]] when suitable.

Canto-span-specific terms in [[Canto-span Pilot Termbase v0.1]] are non-normative test material and do not control this register.

## Evaluation questions

1. Can readers distinguish observations from analyses without visible labels?
2. Do authors preserve intended inferential strength?
3. Does the ATT subtype help across corpus, fieldwork, elicitation, and citation contexts?
4. Does merging NEG avoid an unnecessary class without hiding search limitations?
5. Is REQ useful outside annotation and project documentation?
6. Are DEC and STA needed in a later document-governance profile?
7. Which evidence expressions require local definitions, and in which document types?
8. Does a declared **must** or **shall** system produce clearer conformance judgments?

Record evaluation results under [[Evaluation Framework]].
