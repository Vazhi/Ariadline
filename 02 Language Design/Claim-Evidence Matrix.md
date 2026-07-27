---
title: "Claim-Evidence Matrix"
type: design
status: draft
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

The [[Claim-Evidence Matrix]] prevents a writer from presenting attestation, judgment, software output, or theoretical interpretation as if these were the same type of evidence.

## Claim classes

| Code | Claim class | Required information |
|---|---|---|
| OBS | Observation | source, unit, method, and scope |
| ATT | Attestation | exact form, source, context, and retrieval method |
| JUD | Judgment result | task, scale, participants, item, and result |
| GEN | Generalization | population or dataset, boundary, and counterevidence policy |
| ANA | Analysis | framework or assumptions and supporting evidence |
| HYP | Hypothesis | predicted observations and possible falsifiers |
| NEG | Negative claim | search space, method, and sensitivity limit |
| SYS | System behavior | software version, input, configuration, and output |
| DEF | Definition | term, scope, and distinguishing criteria |
| LIM | Limitation | affected claim and consequence |

## Separation rule

Do not combine different claim classes when the combination hides an inference.

**Uncontrolled**

> The corpus contains three examples, proving that the construction is productive.

**SLE form**

> The corpus contains three tokens of the construction. [ATT]  
> These tokens show that the construction is attested in this corpus. [OBS]  
> The tokens do not establish that the construction is productive. [LIM]

See [[Attestation and Productivity]].

## Evidence records

Each important claim should link to an evidence record that identifies:

- evidence type;
- source;
- extraction or elicitation method;
- date and version;
- direct result;
- inference;
- limitations;
- reviewer status.

## Negative evidence

A statement such as “the corpus does not contain X” is valid only relative to a documented corpus, query, normalization procedure, and search sensitivity.

## Software evidence

Parser output establishes what the parser did under a configuration. It does not alone establish what speakers accept or how the language is structured.

## Pilot deliverable

Create 100 paired examples in which uncontrolled prose is rewritten with explicit claim classes. Use these pairs in [[Pilot Study Design]].
