---
title: "Ariadline Candidate Test Core Register v0.1"
type: evaluation-register
status: proposed-test-scope
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags: [ariadline, core, evaluation, narrowing]
---
# Ariadline Candidate Test Core Register v0.1

## Status

This register defines a **candidate test core**. It is not a stable profile and does not replace [[Ariadline Profile Applicability Register v0.1]].

The aim is to test the smallest defensible set of existing controls before Ariadline expands or stabilizes. Stable `SLE-RULE-*` identifiers are retained for traceability after the project rename.

## Selection standard

A rule enters the candidate test core only when it:

1. addresses a documented critical or major communication risk;
2. is likely to remain useful across changes in linguistic theory;
3. can be tested on authentic prose;
4. does not substantially duplicate another selected rule;
5. could justify universal scope at low author and reviewer burden;
6. preserves theoretical, methodological, linguistic, accessibility, and community plurality.

These criteria implement [[Quality Metrics and Acceptance Gates]].

## Identity

- Register ID: `SLE-CANDIDATE-CORE-0.1`
- Controlling rule set: [[Ariadline Language Rules v0.1]]
- Candidate rule count: 12
- Test protocol: [[Minimal Ariadline Kill-Test Protocol v0.1]]
- Decision record: [[Ariadline Kill-Test Decision Matrix v0.1]]
- Status: proposed for adversarial evaluation only

## Candidate rules

| Rule | Reason | Primary risk |
|---|---|---|
| `SLE-RULE-0002` | Ambiguous reference can change which entity or analysis a claim concerns. | antecedent error and unsupported inference |
| `SLE-RULE-0003` | Unbounded scope can turn a local result into a language-wide or population-wide claim. | overgeneralization |
| `SLE-RULE-0005` | Locally important terms need usable distinguishing criteria when competing interpretations affect the claim. | terminological misinterpretation |
| `SLE-RULE-0006` | A comparison cannot be reconstructed when items, dimensions, or bases are missing. | false or incomplete comparison |
| `SLE-RULE-0007` | Negation, quantifier, restriction, and exception scope can materially alter meaning. | logical-scope error |
| `SLE-RULE-0011` | Example origin, collection context, modification, and production method can alter evidential interpretation. | false provenance inference |
| `SLE-RULE-0014` | Dataset identity, version, and transformation determine what evidence was analyzed. | irreproducible or misidentified evidence |
| `SLE-RULE-0015` | Software output must not silently become a claim about speaker knowledge or language structure. | system-to-language inference |
| `SLE-RULE-0020` | Evidence wording must not claim more force than the method and assumptions support. | false certainty |
| `SLE-RULE-0021` | A negative result is uninterpretable without the searched space and a material sensitivity limit. | universalized absence claim |
| `SLE-RULE-0022` | A material limitation or counterexample must remain visible when it changes a central claim. | omitted qualifying evidence |
| `SLE-RULE-0023` | A central claim must connect to its actual supporting record or analysis. | unsupported claim attribution |

## Governance safeguard outside the reader-benefit core

`SLE-RULE-0018` remains a project-wide safeguard: conformance does not certify truth, grammaticality, theoretical correctness, ethical adequacy, or methodological validity.

It is not counted among the 12 reader-benefit rules because its principal function is to prevent false certification by Ariadline.

## Applicability

The kill test does not force every candidate rule onto every passage. For each passage, record:

- applicable rule IDs;
- not-applicable rule IDs;
- reasons for conditional applicability decisions;
- rule interactions that prevent isolated testing;
- missing source information that makes application impossible.

A rule receives no credit when it is merely listed but not applicable.

## No aggregation shortcut

Do not convert the 12 rules into one undifferentiated Ariadline score. Report rule-level preservation, benefit, burden, naturalness, interactions, ordinary-editing successes, and Ariadline-created problems.

## Promotion boundary

After evidence exists, each rule can receive one primary action:

- retain as a candidate core control;
- move to a bounded profile;
- revise and retest;
- remove;
- insufficient evidence.

No action in this register stabilizes a rule.