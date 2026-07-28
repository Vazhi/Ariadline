---
title: "Users and Use Cases"
type: plan
status: draft
created: 2026-07-27
updated: 2026-07-27
tags:
  - ariadline
  - foundation
  - users
---
# Users and Use Cases

## Primary users

### Authors

- field linguists;
- descriptive linguists;
- grammar writers;
- corpus builders;
- annotation-guideline authors;
- computational linguists;
- graduate researchers.

### Reviewers and maintainers

- journal and volume editors;
- research assistants;
- corpus adjudicators;
- terminology managers;
- software-documentation maintainers.

### Readers

- linguists outside the author's subfield;
- linguists who use English as an additional language;
- engineers who use linguistic specifications;
- students who must trace a claim to evidence.

## Priority use cases

### UC-01 — State an empirical observation

The author identifies an attested form and gives its source.

Expected Ariadline behavior: separate the observation from the analysis. See [[Claim-Evidence Matrix]].

### UC-02 — State a generalization with a boundary

The author states a pattern and identifies the population, variety, register, corpus, or construction to which it applies.

Expected Ariadline behavior: make [[Ambiguity and Referential Clarity|scope]] explicit.

### UC-03 — Report a speaker judgment

The author records the task, scale, speaker population, and result.

Expected Ariadline behavior: do not convert a limited judgment into an unrestricted grammaticality claim.

### UC-04 — Define a technical term

The author introduces a term that has different meanings across frameworks.

Expected Ariadline behavior: create a [[Terminology Control|project-scoped definition]] and use one preferred designation.

### UC-05 — Write an annotation rule

The author specifies how annotators must label a construction.

Expected Ariadline behavior: use [[Normative Language|normative verbs]] consistently and provide positive, negative, and boundary examples.

### UC-06 — Document a parser behavior

The author distinguishes a runtime observation from a linguistic conclusion.

Expected Ariadline behavior: state that software output is evidence about the system, not automatically evidence about the language.

## User research questions

- Which ambiguities cause the most revision or adjudication work?
- Which technical terms produce the most cross-framework confusion?
- Which Ariadline restrictions reduce comprehension errors?
- Which restrictions increase authoring time without sufficient benefit?
- Which users need separate [[Ariadline Profile|profiles]]?
