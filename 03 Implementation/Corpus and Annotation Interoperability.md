---
title: "Corpus and Annotation Interoperability"
type: implementation
status: draft
created: 2026-07-27
updated: 2026-07-27
tags:
  - ariadline
  - implementation
  - corpus
  - annotation
---
# Corpus and Annotation Interoperability

## Objective

Ariadline should describe linguistic datasets clearly without creating a new incompatible data ecosystem.

## Standards to evaluate

- [[Standards and Sources|Leipzig Glossing Rules]] for interlinear glossing;
- [[Standards and Sources|Universal Dependencies]] for cross-linguistic morphosyntactic annotation;
- [[Standards and Sources|CLDF]] for exchange of cross-linguistic data;
- stable language and script identifiers where a project requires them;
- project-specific annotation schemas.

## Interoperability principle

Ariadline controls prose and declarations around a data model. It does not require all projects to convert to one annotation framework.

## Required declaration for datasets

A dataset description should state:

- schema and version;
- annotation framework;
- language and variety identifiers;
- tokenization and segmentation policy;
- normalization policy;
- provenance;
- license;
- validation method;
- known limitations.

## Framework distinction

The writer must distinguish:

- source data;
- normalized data;
- annotations;
- derived measurements;
- model predictions;
- manual corrections.

## Mapping statements

When a project maps one label set to another, state whether the mapping is:

- exact;
- broader;
- narrower;
- overlapping;
- context-dependent;
- unresolved.

## Export goal

The Ariadline termbase and rule inventory should support Markdown plus structured export. Candidate formats include JSON, CSV, and YAML. Dataset-specific exports can align with CLDF or CoNLL-U where appropriate.
