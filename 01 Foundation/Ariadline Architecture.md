---
title: "Ariadline Architecture"
type: design
status: draft
created: 2026-07-27
updated: 2026-07-27
tags:
  - ariadline
  - foundation
  - architecture
---
# Ariadline Architecture

## Proposed architecture

Ariadline will use six coordinated components.

| Component | Function | Primary note |
|---|---|---|
| Core prose rules | Control sentence structure, reference, coordination, and discourse | [[Grammar and Style Rule Plan]] |
| Termbase | Define preferred terms, variants, meanings, and scope | [[Controlled Vocabulary Plan]] |
| Claim system | Distinguish observation, analysis, hypothesis, and limitation | [[Claim-Evidence Matrix]] |
| Data conventions | Standardize examples, glosses, judgments, and identifiers | [[Linguistic Examples and Glossing]] |
| Profiles | Select rule subsets for document types | [[Profiles and Conformance]] |
| Checker interface | Define what software can detect or assist | [[Authoring and Conformance Tools]] |

## Human-oriented position

The initial Ariadline design is a **human-oriented controlled language**. It will improve consistency and reduce ambiguity without requiring every sentence to map to a formal logic.

Machine-oriented extensions can be developed later as optional profiles.

## Rule classes

Each Ariadline rule will have one class:

- **Lexical** — controls a word or phrase.
- **Syntactic** — controls sentence form.
- **Referential** — controls pronouns, ellipsis, and antecedents.
- **Epistemic** — controls certainty and evidence wording.
- **Normative** — controls requirements and recommendations.
- **Data-presentational** — controls examples, glosses, tables, and identifiers.
- **Document-structural** — controls definitions, sections, and cross-references.

## Compliance model

A document conforms to:

1. a named Ariadline version;
2. a named [[Ariadline Profile|profile]];
3. a declared termbase;
4. any listed project extensions.

Example declaration:

> This document conforms to Ariadline 0.1, Research Profile, with the Cantonese Grammar Termbase 0.3.

## Extension rule

A project can add technical terms and local conventions. An extension must not silently change the meaning of a core Ariadline term.
