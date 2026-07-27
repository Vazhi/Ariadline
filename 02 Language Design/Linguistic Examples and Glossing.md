---
title: "Linguistic Examples and Glossing"
type: design
status: revised
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

A [[Linguistic Example]] should allow a reader to identify the form, language variety, source or construction status, analysis, and judgment status when these details affect interpretation.

The proposed normative controls are SLE-RULE-0011 through SLE-RULE-0013 and SLE-RULE-0024 in [[SLE for Linguistics Language Rules v0.1]].

## Glossing baseline

SLE proposes the Leipzig Glossing Rules as the default for interlinear morpheme-by-morpheme glosses.

A document may use another convention when it declares that convention. SLE adds controls for provenance, judgments, cross-reference stability, and separation of data from analysis.

## Example information

For a central example, provide the applicable information:

- stable example identifier;
- language and relevant variety;
- orthographic or transcription system;
- segmentation;
- morpheme gloss;
- idiomatic translation;
- source, participant record, or constructed status;
- corpus location or elicitation task;
- speaker or annotator count when relevant;
- judgment symbol and its defined meaning;
- normalization or editing notes.

Not every example requires every field. The document must provide the information needed to interpret the claim that uses the example.

## Judgment symbols

Do not assume that `*`, `?`, `??`, and `#` have identical meanings across publications.

Each document must define its symbols or link to a controlling definition. The definition should identify the judgment task, population, or analytical convention when relevant.

## Constructed examples

Mark a constructed example as constructed when a reader could otherwise mistake it for attested data.

Do not present a constructed example as a corpus attestation.

## Adapted examples

When an author changes a cited example, state the material type of change, such as:

- orthographic normalization;
- shortened context;
- substituted lexical item;
- changed person or number;
- changed punctuation;
- analytical resegmentation.

Minor typographic changes that cannot affect interpretation need not be listed individually.

## Gloss abbreviations

Use established abbreviations when they fit the analysis.

Define a project-specific abbreviation in the document, glossary, or declared profile. A gloss abbreviation does not by itself establish the correct analysis.

## Stable references

Refer to an example by a stable identifier when the document refers to it more than once.

Avoid relying only on relative phrases such as *the example above*.

## Data and analysis separation

The object-language record is data. Segmentation, glosses, labels, and translations can contain analysis.

A document must allow the reader to identify which layer is the recorded form and which layers express an analysis.

An alternative analysis should not silently alter the quoted or recorded object-language line.

## Evaluation

Evaluation must include examples from typology, syntax, phonology, sociolinguistics, language documentation, corpus work, lexicography, and computational annotation.

The evaluation should test whether the rules preserve legitimate field-specific conventions rather than replacing them with one universal presentation format.
