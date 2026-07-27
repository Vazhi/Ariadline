---
title: "Linguistic Examples and Glossing"
type: design
status: draft
created: 2026-07-27
updated: 2026-07-27
tags:
  - sle
  - language-design
  - examples
  - glossing
---
# Linguistic Examples and Glossing

## Objective

A [[Linguistic Example]] must allow a reader to identify the form, language variety, source, analysis, and judgment status.

## Baseline

SLE should adopt the [[Standards and Sources|Leipzig Glossing Rules]] as the default for interlinear morpheme-by-morpheme glosses. SLE should specify only the additional controls needed for provenance, judgments, and analytical clarity.

## Required example metadata

For each central example, provide as applicable:

- stable example identifier;
- language and variety;
- orthographic or transcription system;
- segmentation;
- morpheme gloss;
- idiomatic translation;
- source or participant record;
- corpus location or elicitation task;
- speaker or annotator count;
- judgment symbol and its defined meaning;
- notes about normalization or editing.

## Judgment symbols

Do not assume that `*`, `?`, `??`, and `#` have identical meanings across publications.

Each document must define its judgment symbols or link to a declared profile.

## Constructed examples

Mark a constructed example as constructed. Do not present a constructed example as a corpus attestation.

## Adapted examples

When an author changes a cited example, state the type of change:

- orthographic normalization;
- shortened context;
- substituted lexical item;
- changed person or number;
- changed punctuation;
- analytical resegmentation.

## Gloss abbreviations

Use established abbreviations when available. Define project-specific abbreviations in the termbase.

## Example-reference rule

Refer to examples by stable identifiers, not only by relative phrases such as *the example above*.

## Data and analysis separation

The object-language line records the data. The gloss and labels record an analysis. SLE must permit alternative analyses without altering the underlying data line.
