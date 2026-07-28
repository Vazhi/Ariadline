---
title: "Linguistic Examples and Glossing"
type: design
status: revised
created: 2026-07-27
updated: 2026-07-27
tags:
  - ariadline
  - language-design
  - examples
  - glossing
---
# Linguistic Examples and Glossing

## Objective

A [[Linguistic Example]] should let a reader identify the recorded or proposed form, relevant language variety, provenance, analytical layers, and judgment basis when those details affect interpretation.

The proposed controls are SLE-RULE-0011 through SLE-RULE-0013 and SLE-RULE-0024 in [[Ariadline Language Rules v0.1]].

## Glossing baseline

Ariadline proposes the Leipzig Glossing Rules as the default convention for interlinear morpheme-by-morpheme glosses.

A document may use another convention when it declares that convention. The Leipzig rules themselves permit flexibility and alternative conventions. Ariadline adds proposed controls for provenance, judgments, reference stability, and separation of recorded material from analysis.

## Example information

For a central example, provide the applicable information:

- stable example identifier;
- language and relevant variety;
- orthographic or transcription system;
- segmentation;
- morpheme gloss;
- idiomatic translation;
- relevant provenance dimensions;
- judgment symbol and its defined meaning;
- normalization or editing notes.

Not every example requires every field. The document must provide the information needed to interpret the claim that uses the example.

## Provenance dimensions

Do not force an example into one exclusive category such as *attested*, *elicited*, *constructed*, *adapted*, or *generated*. These terms describe different axes and can co-occur.

Record the relevant dimensions separately.

### 1. Source or origin

Examples include:

- published source;
- corpus or archive record;
- participant response;
- author-created item;
- system-produced item.

### 2. Collection context

Examples include:

- naturally occurring interaction;
- corpus extraction;
- elicitation session;
- controlled experiment;
- introspective judgment;
- classroom or annotation task.

### 3. Modification status

Examples include:

- unchanged;
- orthographically normalized;
- punctuation changed;
- context shortened;
- lexical material substituted;
- resegmented or reglossed;
- translated;
- reconstructed or otherwise adapted.

### 4. Production method

Examples include:

- participant-produced;
- author-written;
- produced from a declared template or rule;
- produced by a named software system or model.

A **system-produced item** is output created by a named software system or model. This descriptor does not state whether the item is attested, acceptable, grammatical, or analytically correct.

## Multiple descriptors

One item can legitimately have several descriptors.

> Example (12) [participant response; elicitation task E3; orthography normalized]

> Example (13) [author-created experimental item; template-produced; unchanged]

> Example (14) [published source; adapted; lexical item replaced; segmentation revised]

This structure preserves distinctions that the earlier single-list formulation collapsed.

## Judgment symbols

Do not assume that `*`, `?`, `??`, and `#` have identical meanings across publications.

Each document must define its symbols or link to a controlling definition. The definition should identify the judgment task, population, or analytical convention when relevant.

## Gloss abbreviations

Use established abbreviations when they fit the analysis.

Define a project-specific abbreviation in the document, glossary, or declared profile. A gloss abbreviation does not by itself establish the correct analysis.

## Stable references

Refer to an example by a stable identifier when the document refers to it more than once.

Avoid relying only on relative phrases such as *the example above*.

## Recorded material and analysis

The object-language record can be data. Segmentation, glosses, labels, translations, and normalization choices can contain analysis.

A document must let the reader identify which layer records or reproduces the form and which layers express an analysis or editorial transformation.

An alternative analysis should not silently alter a quoted or recorded object-language line.

## Evaluation

Evaluation must include examples from typology, syntax, semantics, phonetics, phonology, sociolinguistics, signed-language research, language documentation, corpus work, lexicography, experimental work, and computational annotation.

The evaluation should test whether the four provenance dimensions are sufficient, whether descriptors remain understandable when combined, and whether the rules preserve legitimate field-specific conventions.
