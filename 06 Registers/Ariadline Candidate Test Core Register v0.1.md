---
title: "Ariadline Candidate Test Core Register v0.1"
type: evaluation-register
status: proposed-test-scope
version: "0.1"
created: 2026-07-28
updated: 2026-07-29
tags: [ariadline, core, evaluation, narrowing]
---
# Ariadline Candidate Test Core Register v0.1

## Status

This register defines a **candidate test core**. It is not a stable profile and does not replace [[Ariadline Profile Applicability Register v0.1]].

The aim is to test the smallest defensible set of existing controls before Ariadline expands or stabilizes. Stable `SLE-RULE-*` identifiers are retained for traceability after the project rename.

The shortlist is an evaluation hypothesis prepared for human decision in issue #40. It is not an approval, stabilization, or claim of effectiveness.

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

## Functional overlap and dependency analysis

The candidate rules are not assumed to be statistically or editorially independent. The kill test must record the following interactions while preserving rule-level outcomes.

| Functional cluster | Rules | Relationship | Test treatment |
|---|---|---|---|
| Reference and scope recovery | `SLE-RULE-0002`, `SLE-RULE-0003`, `SLE-RULE-0007` | All reduce ambiguity, but they target different objects: antecedent identity, claim domain, and operator or exception scope. | May occur in one passage; score separately. Do not merge unless human review finds that readers and editors cannot distinguish the failure types. |
| Terminology control | `SLE-RULE-0005` with local-extension rule `SLE-RULE-0004` | A definition can be clear while term choice remains unstable, or one preferred term can remain undefined. | Retain `SLE-RULE-0005` in the test core. Route `SLE-RULE-0004` to local terminology governance and record interactions. |
| Comparison and claim scope | `SLE-RULE-0006`, `SLE-RULE-0003`, `SLE-RULE-0020` | A comparison needs identified items and measures, a bounded population or dataset, and calibrated evidential force. | Test as a linked claim package when all apply, but retain separate scoring because each omission supports a different repair. |
| Example and dataset provenance | `SLE-RULE-0011`, `SLE-RULE-0014` | Both concern provenance. `SLE-RULE-0011` is example-level and multidimensional; `SLE-RULE-0014` identifies dataset/version and transformations. | Test together when an example derives from a dataset. Do not collapse unless separate application proves unworkable. |
| System and resource reporting | `SLE-RULE-0015`, `SLE-RULE-0014`, `SLE-RULE-0020` | A system-behavior claim commonly depends on system/data identity and calibrated inference wording. | Treat `SLE-RULE-0015` as the boundary rule; use `SLE-RULE-0014` and `SLE-RULE-0020` as supporting controls when applicable. |
| Negative and qualified claims | `SLE-RULE-0021`, `SLE-RULE-0022`, `SLE-RULE-0020`, `SLE-RULE-0023` | A negative claim needs a searched space and sensitivity bound, visible limitations, calibrated force, and a traceable support record. | Permit one passage to test the cluster, but report each rule and any interaction separately. |
| Evidence chain | `SLE-RULE-0014`, `SLE-RULE-0023`, `SLE-RULE-0020`, `SLE-RULE-0022` | These rules connect input identity, support mapping, inferential force, and qualifications. None alone guarantees a reconstructable evidence chain. | Report both individual results and whether the chain fails at any link. Do not convert the cluster into one undifferentiated score. |

### Consolidation decision

No candidate rules are merged before authentic testing. Premature merging would hide whether a benefit or harm comes from reference repair, scope control, provenance, evidence calibration, or support mapping.

A later human decision may merge, narrow, or separate rules only when the evaluation shows that:

- reviewers cannot distinguish their applicability or outcomes;
- one rule consistently subsumes another without added burden;
- separate rules create avoidable repetition or fragmentation; and
- the merged function preserves theory, method, language, accessibility, and community plurality.

## Bias and burden risks requiring human review

| Risk family | Candidate rules most exposed | Material concern | Required human review question |
|---|---|---|---|
| Theory and ontology | `SLE-RULE-0005`, `SLE-RULE-0015`, `SLE-RULE-0020`, `SLE-RULE-0023` | Definitions, explicit support links, or system/language boundaries may privilege analyses that expose commitments in one conventional form. | Can the control preserve framework-specific terminology and argument structure without requiring reviewers to decide which analysis is correct? |
| Method and genre | `SLE-RULE-0011`, `SLE-RULE-0014`, `SLE-RULE-0021`, `SLE-RULE-0022`, `SLE-RULE-0023` | Provenance, dataset identity, sensitivity limits, and local support mapping may fit empirical reports better than formal proofs, conceptual arguments, grammars, or community documents. | Is the rule genuinely applicable across practices, or should it move to a profile rather than be forced onto non-empirical genres? |
| Language and translation | `SLE-RULE-0002`, `SLE-RULE-0003`, `SLE-RULE-0006`, `SLE-RULE-0007`, `SLE-RULE-0020`, `SLE-RULE-0022`, `SLE-RULE-0023` | English-style explicitness, local attachment, and constituent order may not transfer cleanly to non-English originals or translated prose. | Does the rule control recoverable information relationships rather than English word order, sentence segmentation, or rhetorical sequence? |
| Community and cultural authority | `SLE-RULE-0005`, `SLE-RULE-0011`, `SLE-RULE-0022` | Required definitions or provenance disclosure may conflict with community-controlled terminology, restricted knowledge, anonymity, or legitimate nondisclosure. | Can authority holders restrict, generalize, or withhold information without being misclassified as nonconforming? |
| Accessibility and cognitive burden | all 12 candidate rules, especially `SLE-RULE-0003`, `SLE-RULE-0011`, `SLE-RULE-0014`, `SLE-RULE-0022`, `SLE-RULE-0023` | Added qualifications and provenance can increase length, density, repetition, or navigation burden. | Does the benefit exceed the burden for the intended readers, including readers using assistive technology or working in an additional language? |
| Rhetorical cohesion and naturalness | `SLE-RULE-0002`, `SLE-RULE-0003`, `SLE-RULE-0005`, `SLE-RULE-0020`, `SLE-RULE-0022`, `SLE-RULE-0023` | Repeated nouns, local scope statements, definitions, and support links may fragment cohesive expert prose. | Can the information remain recoverable through section-level scope, tables, cross-references, or other natural forms? |
| Publication and infrastructure conventions | `SLE-RULE-0014`, `SLE-RULE-0023` | Stable identifiers, dataset versions, or local links may be unavailable or imposed differently by publishers, archives, or community repositories. | Is a bounded alternative available without inventing identifiers or implying infrastructure quality? |
| Reviewer consistency | all 12 candidate rules | Rules may appear distinct in text but collapse in practice, producing unstable applicability judgments or double-counted benefits. | Do independent reviewers agree on applicability and primary cause strongly enough for the claimed scope? |

Human issue #40 must approve, narrow, or reject the shortlist and these risk treatments before the candidate core becomes controlling for the kill test.

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