---
title: "Claim-Evidence Matrix"
type: design
status: revised
created: 2026-07-27
updated: 2026-07-27
aliases:
  - "Evidence Language"
  - "Claim Types"
tags:
  - sle
  - language-design
  - evidence
---
# Claim-Evidence Matrix

## Objective

The matrix helps writers distinguish observation, attestation, judgment, generalization, analysis, hypothesis, negative evidence, system behavior, definition, limitation, and requirement.

It prevents a writer from presenting different evidential or communicative functions as if they were interchangeable.

The normative controls are in [[SLE for Linguistics Language Rules v0.1]]. The candidate-function decisions are in [[Claim Function Decision Register v0.1]].

## Editorial functions

| Function | Required information |
|---|---|
| Observation | source or object, method, unit, result, scope |
| Attestation | exact form or item, source, location or retrieval method, context |
| Judgment result | task, response system, population, item scope, result |
| Generalization | target domain, boundary, evidence basis, counterevidence policy |
| Analysis | assumptions or framework, analyzed material, inferential relation |
| Hypothesis | proposed relation, prediction, falsifier or revision condition |
| Negative claim | search or test space, method, sensitivity limit |
| System behavior | system and version, input, configuration, output |
| Definition | preferred term, scope, distinguishing criteria |
| Limitation | affected claim, narrowed scope or force, consequence |
| Requirement | actor or object, required action or condition, conformance scope |

## Label policy

Visible codes such as `[OBS]`, `[ATT]`, or `[ANA]` are optional editorial aids.

Basic SLE conformance does not require visible labels. A profile may use labels for a defined workflow, but labels do not establish that a claim is supported.

## Separation rule

Do not combine different functions when the combination hides an inference.

**Uncontrolled**

> The corpus contains three examples, proving that the construction is productive.

**Controlled draft**

> The corpus contains three tokens of the construction.  
> These tokens establish that the construction is attested in this corpus.  
> The tokens do not by themselves establish productivity.

See [[Attestation and Productivity]].

## Evidence wording

Evidence wording must not overstate the relationship between evidence and conclusion.

SLE does not define a universal hierarchy for *shows*, *supports*, *suggests*, *is consistent with*, *does not establish*, and *contradicts*. Their force can vary across disciplines, methods, and argument types.

A document should define an evidence expression when its force is important and not clear from context. The editor should identify the direct result, inference, assumptions, alternatives, and limitations.

## Evidence records

An important claim should identify:

- evidence type;
- source;
- extraction, elicitation, or observation method;
- date or version when relevant;
- direct result;
- inference;
- limitations;
- review status when relevant.

The information may appear in prose, a table, a note, a citation, or a linked record. Machine-readable metadata is optional.

## Negative evidence

A statement such as “the corpus does not contain X” is valid only relative to a documented corpus, query or test, normalization procedure, and sensitivity limit.

## Software evidence

Tool output establishes what the tool did under a specified state and configuration. It does not alone establish what speakers accept or how a language is structured.

## Evaluation

The pilot should test paired uncontrolled and controlled passages across multiple linguistic domains.

The evaluation must test whether readers identify the intended claim and evidence relation without requiring visible function labels or a fixed evidence-verb scale.
