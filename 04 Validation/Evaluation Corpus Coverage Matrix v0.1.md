---
title: "Evaluation Corpus Coverage Matrix v0.1"
type: validation-register
status: proposed
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - sle
  - validation
  - corpus-coverage
  - representativeness
---
# Evaluation Corpus Coverage Matrix v0.1

## Purpose

This register describes the coverage and imbalance of [[Multi-Domain SLE Evaluation Corpus v0.1]] and the separately bounded [[Canto-span Evaluation Subset v0.1]].

The corpus is evaluation material, not normative evidence. No source project, named language, theory, or method becomes an authority merely because it contributes an item.

## Item inventory

| ID | Domain | Method | Theory or framework | Language context | Genre | Source class |
|---|---|---|---|---|---|---|
| SLE-EVAL-0001 | descriptive grammar | text corpus | framework-neutral description | Cantonese | grammar section | project-constructed |
| SLE-EVAL-0002 | theoretical syntax | constructed contrast | generative and type-driven alternatives | English | theoretical analysis | project-constructed |
| SLE-EVAL-0003 | discourse and interaction | sequential analysis | conversation-analytic and functional | Spanish | phenomenon description and analysis | project-constructed |
| SLE-EVAL-0004 | corpus variation | stratified corpus comparison | variationist | Arabic varieties | corpus study | project-constructed |
| SLE-EVAL-0005 | typology | cross-language comparison | descriptive typology | Turkish and Japanese | research summary | project-constructed |
| SLE-EVAL-0006 | field linguistics | picture-prompt elicitation | descriptive field analysis | Swahili | fieldwork note | project-constructed |
| SLE-EVAL-0007 | judgment research | rating task | framework-neutral experiment | Korean | judgment-study report | project-constructed |
| SLE-EVAL-0008 | lexicography | interview-corpus review | corpus-informed lexicography | Māori | lexical note | project-constructed |
| SLE-EVAL-0009 | signed-language documentation | community-reviewed video corpus | language documentation | American Sign Language | resource documentation | project-constructed |
| SLE-EVAL-0010 | annotation | rule-based annotation | dependency annotation | multilingual | annotation guideline | project-constructed |
| SLE-EVAL-0011 | computational linguistics | held-out benchmark | model evaluation | multilingual | system description | project-constructed |
| SLE-EVAL-0012 | language-resource documentation | curated speech-corpus release | resource documentation | Finnish | resource guide | project-constructed |
| SLE-EVAL-0013 | linguistic pedagogy | learner explanation | descriptive pedagogy | Japanese | learner-facing explanation | project-constructed |
| SLE-EVAL-0014 | phonetics | acoustic measurement | laboratory phonetics | Spanish | procedure document | project-constructed |
| SLE-EVAL-0015 | conversation analysis | sequential analysis | conversation analysis | Spanish | data commentary | project-constructed |
| SLE-EVAL-0016 | collaborative documentation | terminology decision | cross-framework collaboration | multilingual team | revision note | project-constructed |
| SLE-EVAL-CS-0001 | grammar-engineering documentation | source-state summary | project-local | Cantonese-oriented Canto-span | limitation record | Canto-span stress test |
| SLE-EVAL-CS-0002 | annotation and parser documentation | decision procedure | project-local | Cantonese-oriented Canto-span | annotation guideline | Canto-span stress test |

## Quantitative distribution

### Source class

- independent project-constructed items: 16 of 18;
- Canto-span items: 2 of 18;
- authentic permission-compatible external excerpts: 0;
- community-contributed or author-contributed passages: 0.

Canto-span supplies 11.1% of the items and cannot dominate corpus interpretation.

### Language context

The independent items include contexts involving:

- Cantonese;
- English;
- Spanish;
- Arabic varieties;
- Turkish;
- Japanese;
- Swahili;
- Korean;
- Māori;
- American Sign Language;
- Finnish;
- multilingual annotation, modeling, and collaboration.

Named-language context is not empirical evidence. Every independent passage is fictional test material.

### Theory and framework coverage

Represented:

- framework-neutral description;
- generative analysis;
- type-driven semantic analysis;
- functional analysis;
- conversation analysis;
- variationist analysis;
- descriptive typology;
- field-based descriptive analysis;
- experimental judgment reporting;
- corpus-informed lexicography;
- language documentation;
- dependency annotation;
- computational model evaluation;
- laboratory phonetics;
- descriptive pedagogy;
- cross-framework editorial collaboration.

No framework controls the corpus vocabulary or item structure.

### Method coverage

Represented:

- corpus observation;
- cross-language comparison;
- formal or theoretical reasoning;
- sequential qualitative analysis;
- elicitation;
- rating tasks;
- lexicographic evidence review;
- video-corpus documentation;
- annotation procedures;
- computational benchmarks;
- resource release documentation;
- learner explanation;
- acoustic measurement;
- terminology governance.

### Genre coverage

Represented:

- descriptive grammar section;
- phenomenon description;
- theoretical analysis;
- corpus study report;
- judgment-study report;
- fieldwork note;
- annotation guideline;
- lexical note;
- system description;
- resource guide;
- methods or procedure document;
- research summary;
- data commentary;
- editorial revision note;
- limitation record.

## Rule coverage

| Rule area | Principal item IDs |
|---|---|
| principal message and reference | 0002, 0010, 0013 |
| scope and comparison | 0001, 0003, 0004, 0005, 0007, 0009, 0011 |
| terminology and definitions | 0002, 0005, 0008, 0010, 0013, 0014, 0016 |
| normative language and procedures | 0010, 0014, CS-0002 |
| attestation and stronger claims | 0001, 0005, 0008 |
| judgment reporting | 0006, 0007 |
| provenance and identifiers | 0006, 0008, 0009, 0012, 0015 |
| dataset and transformation identity | 0004, 0008, 0011, 0012 |
| system behavior boundary | 0011, CS-0002 |
| observation and interpretation | 0001–0009, 0011, 0015 |
| evidence force | 0001–0005, 0007–0009, 0011, 0015 |
| bounded negative claims | 0001, 0009, 0012 |
| limitations and counterevidence | all research and resource items |
| claim-support connection | all research items |
| conformance-versus-truth boundary | 0016 and corpus-wide instructions |
| interlinear glossing | not directly tested in v0.1 |

## Pattern coverage

The independent corpus directly tests 13 of the 14 proposed patterns.

- Directly represented: `SLE-PATTERN-0001` through `0012` and `0014`.
- Not directly represented as a principal item: `SLE-PATTERN-0013`, limitation and open-question record.
- The Canto-span subset supplies a bounded `SLE-PATTERN-0013` stress test, but an independent non-Canto-span item is still required.

## Overrepresentation risks

1. **Constructed prose:** all independent items are project-constructed rather than authentic author passages.
2. **English metalanguage:** all items are currently written in English, even when the language context differs.
3. **Research-report orientation:** research and documentation genres outnumber teaching, community, policy, and public-facing genres.
4. **Short-passage bias:** the corpus tests paragraphs and short records rather than full chapters, dictionaries, manuals, or articles.
5. **Explicit-number bias:** many controlled alternatives use counts because counts make scope visible; not all legitimate linguistic reasoning is quantitative.
6. **Academic-register bias:** community-authored, oral, signed, and collaborative forms are represented only through constructed English prose.
7. **Rule-selection bias:** items were designed around the current 24 rules, so they may fail to expose missing rules.

## Underrepresented or absent coverage

Required future additions include:

- authentic permission-compatible passages from independent authors;
- passages written originally in languages other than English;
- translated pairs reviewed by translators and domain experts;
- community-authored documentation with community-controlled access decisions;
- signed-language examples represented through video-aware documentation rather than English summaries alone;
- sociolinguistic ethnography;
- historical linguistics and philology;
- morphology and phonology beyond the current examples;
- semantics and pragmatics outside the single theoretical item;
- language acquisition and psycholinguistics;
- accessibility-oriented linguistic explanation;
- peer review and editorial correspondence;
- an independent limitation and open-question record;
- direct testing of interlinear glossing conventions;
- full-document and mixed-pattern tests.

## Representativeness rule

The v0.1 corpus is sufficient for a first internal audit of rule coverage. It is not representative enough to support a claim that SLE works across linguistics.

Before stabilization or effectiveness claims:

1. at least half of the evaluated passages must come from independent, permission-compatible, non-Canto-span sources;
2. no single repository, institution, language, theory, or method may supply most evaluated passages;
3. translated and non-English-original material must receive language-specific meaning-preservation review;
4. community-controlled material must retain its access and authority boundaries;
5. full-document tests must supplement short-passage pairs;
6. coverage gaps must remain visible rather than being filled with unreviewed synthetic examples.

## Disposition

The matrix supports issue #6 as a versioned first evaluation corpus. It records clear imbalance and does not authorize normative or effectiveness claims.