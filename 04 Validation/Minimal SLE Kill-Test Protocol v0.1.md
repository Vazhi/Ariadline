---
title: "Minimal SLE Kill-Test Protocol v0.1"
type: evaluation-protocol
status: planning-draft
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - sle
  - evaluation
  - kill-test
  - adversarial
---
# Minimal SLE Kill-Test Protocol v0.1

## Purpose

This protocol asks one bounded question:

> Does the 12-rule candidate core in [[SLE Candidate Test Core Register v0.1]] improve important communication outcomes beyond ordinary expert editing without creating unacceptable meaning loss, burden, unnaturalness, repetition, fragmentation, or bias?

The protocol is intentionally smaller than [[Multi-Domain Reader and Author Evaluation Protocol v0.1]]. It is a planning draft, not a frozen protocol or preregistration.

## Authority and prerequisites

Human issues #30 through #35 remain controlling for oversight, permissions, meaning authority, condition development, recruitment, statistical review, execution, and disposition.

Before any participant sees material, the study must satisfy the relevant launch gates in [[Quality Metrics and Acceptance Gates]]. In particular:

- every source must have a legitimate use and authority record;
- every P and S condition must undergo independent meaning-preservation review;
- scoring and adjudication must be frozen;
- accessibility and withdrawal procedures must be approved;
- the analysis plan and sample target must receive human statistical review;
- the immutable registration record must exist.

This note does not satisfy those gates.

## Materials

Use 10 to 12 authentic, authorized passages.

The set must include at least three substantially different linguistic subfields or research practices. At minimum, include:

1. one descriptive, documentary, fieldwork, or community-governed passage;
2. one theoretical, typological, historical, or argument-focused passage;
3. one corpus, experimental, annotation, resource, or computational passage.

No subfield may contribute more than half of the passages. Canto-span may appear only as a separately bounded stress test and cannot satisfy the independent coverage requirement.

Prefer passages of 100 to 250 words. A shorter or longer passage may be included when its communicative problem cannot be preserved at the preferred length. Record the reason.

## Passage eligibility

A passage is eligible only when:

- its source and version are known;
- use permission or a lawful approved basis is recorded;
- a legitimate source, author, translator, publisher, or community authority can define or approve the meaning record;
- the passage contains at least one applicable candidate-core risk;
- the risk is not created solely by truncation or decontextualization;
- the passage can be shown without disclosing protected or identifying information;
- the passage does not require reviewers to resolve the underlying linguistic theory as a condition of scoring communication.

Record ineligible and excluded candidates so passage selection cannot silently favor SLE.

## Conditions

### P — ordinary expert editing

A qualified editor receives the passage, authorized meaning record, document purpose, intended readership, and ordinary editorial brief. The editor does not receive the candidate SLE rules.

P must represent competent normal practice, not a deliberately weak control.

### S — candidate-core editing

A comparably qualified editor receives the same passage, meaning record, purpose, readership, and editorial resources. The editor also receives the 12-rule candidate core and passage-specific applicability decisions.

S must not receive extra substantive information that P does not receive.

### U — optional source baseline

U is optional and non-primary. Use it only when the unedited source is independently authorized and the task separately registers its purpose. U cannot replace the P-versus-S comparison.

## Fairness controls

- Separate P and S editors when practical.
- Match or record editor expertise, language background, subfield familiarity, and editing time.
- Do not tell editors which condition is expected to perform better.
- Give both conditions the same meaning record and source information.
- Allow both editors to flag `not determined` when authorized meaning is insufficient.
- Keep reader and scorer condition labels masked.
- Prevent one participant from seeing both P and S versions of one meaning record.
- Record all deviations and cross-condition information leaks.

## Meaning-preservation gate

A passage-condition pair cannot enter reader testing until independent reviewers compare it with the authorized meaning record.

Review at least:

- claim content;
- claim scope;
- evidential force;
- uncertainty and modality;
- comparison structure;
- examples and provenance;
- limitations and counterevidence;
- theory- or community-sensitive terminology;
- permissions and access boundaries.

Use `preserved`, `not preserved`, or `not determined`. Do not convert `not determined` into success. A material preservation failure excludes the condition from benefit analysis and remains an adverse result.

## Planning sample

The initial planning range is approximately 20 to 30 readers or editorial reviewers.

This range is not a justified sample size, recruitment target, frozen quota, or preregistration. Human statistical review under issue #34 must decide whether the design can answer the registered question.

Recruit across the represented subfields and include meaningful variation in career stage, scholarly English experience, controlled-language experience, and accessibility needs. Record contributor relationships and cap project insiders before launch.

## Reader and reviewer tasks

Use the smallest task set that directly tests the registered passage risk.

Possible tasks:

- reconstruct the central claim and its scope;
- identify which evidence supports a claim;
- identify a limitation, counterexample, or sensitivity boundary;
- resolve an antecedent or logical-scope contrast;
- identify whether a statement reports software behavior or a language claim;
- identify provenance and material transformation;
- rate naturalness, cohesion, repetition, fragmentation, and burden;
- classify rule applicability and final outcome.

Do not require every task for every passage.

## Primary outcomes

The primary publication-relevant contrast is S versus P.

Register no more than three primary outcomes before launch. Candidate outcomes are:

1. unsupported-inference rate;
2. claim-and-scope reconstruction accuracy;
3. material meaning-preservation failure.

Meaning-preservation failure is a safety outcome and cannot be traded away for reader benefit.

## Supporting outcomes

- claim-support identification;
- limitation and counterevidence detection;
- antecedent and logical-scope accuracy;
- evidence-force calibration;
- editing time;
- reader response time;
- naturalness and cohesion;
- repetition and fragmentation;
- editor and reviewer burden;
- reviewer agreement;
- `not determined` frequency;
- qualitative theory, method, language, accessibility, and community-bias reports.

## Rule-level analysis

For each rule, report:

- number of eligible passages;
- number where it was applicable;
- P and S editing actions;
- preservation outcomes;
- reader or reviewer outcomes;
- burden and naturalness effects;
- interactions with other rules;
- dissent and adverse cases.

Do not infer rule benefit from the package-level result alone.

## Adversarial checks

The study lead must actively search for cases where:

- P solves the problem without SLE;
- S adds words without improving interpretation;
- S fragments a cohesive argument;
- S erases deliberate ambiguity or terminological plurality;
- the rule is theory- or method-dependent;
- the authorized meaning record is itself disputed;
- editors cannot agree that the rule applies;
- a community or accessibility requirement conflicts with the proposed control.

Retain these cases in the report.

## Decision route

Apply [[SLE Kill-Test Decision Matrix v0.1]] after approved analysis.

Possible project-level conclusions are:

- continue with a narrowed candidate core;
- move most controls to profiles or optional guidance;
- revise and rerun a smaller test;
- stop or substantially reconceive the controlled-language project;
- insufficient evidence.

## Non-evidence boundary

Constructed corpus items and the synthetic operations fixture may test procedures, joins, masking, and scoring logic. They cannot satisfy authentic-material, reader-benefit, author-safety, or meaning-preservation requirements.

No result from this planning document changes the current `not_started` human-study state in [[Evaluation Execution Status v0.1]].
