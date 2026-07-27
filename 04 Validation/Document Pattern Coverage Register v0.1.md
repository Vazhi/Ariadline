---
title: "Document Pattern Coverage Register v0.1"
type: validation-register
status: proposed
version: "0.1"
created: 2026-07-27
updated: 2026-07-27
tags:
  - sle
  - validation
  - document-patterns
  - neutrality
---
# Document Pattern Coverage Register v0.1

## Purpose

This register reviews the proposed patterns in [[SLE for Linguistics Document Patterns v0.1]].

It records intended coverage, known gaps, neutrality risks, and evaluation requirements. It does not certify that the patterns are universally valid or final.

Canto-span is not an authority in this register. It may later supply one bounded test case only.

## Pattern inventory

| ID | Pattern | Principal purpose | Primary methods or settings |
|---|---|---|---|
| SLE-PATTERN-0001 | Descriptive grammar section | Describe form, distribution, and function | descriptive grammar, documentation, typology |
| SLE-PATTERN-0002 | Construction or phenomenon description | Bound and characterize one phenomenon | descriptive, corpus, experimental, theoretical |
| SLE-PATTERN-0003 | Theoretical analysis | Present an analysis under stated assumptions | formal, functional, cognitive, usage-based, interactional |
| SLE-PATTERN-0004 | Corpus study report | Report corpus search and analysis | corpus, historical, variationist, discourse |
| SLE-PATTERN-0005 | Elicitation or judgment study report | Report collected responses | fieldwork, experimental, psycholinguistic, annotation |
| SLE-PATTERN-0006 | Fieldwork note or data commentary | Preserve records and provisional analysis | language documentation, field linguistics, community research |
| SLE-PATTERN-0007 | Annotation guideline | Direct consistent annotation decisions | corpus annotation, treebanks, lexicons, qualitative coding |
| SLE-PATTERN-0008 | Lexicographic entry or lexical note | Describe lexical form, sense, and usage | lexicography, terminology, historical and community dictionaries |
| SLE-PATTERN-0009 | Computational-linguistics system description | Describe system behavior and evaluation | NLP, speech, computational modeling, tool development |
| SLE-PATTERN-0010 | Language-resource documentation | Document reusable resources | corpora, archives, databases, treebanks, lexicons |
| SLE-PATTERN-0011 | Methods or procedure document | Specify repeatable work | research methods, transcription, annotation, editorial procedure |
| SLE-PATTERN-0012 | Research summary | Give a bounded concise account | abstracts, executive summaries, literature and project summaries |
| SLE-PATTERN-0013 | Limitation and open-question record | Preserve unresolved boundaries | all methods and document genres |
| SLE-PATTERN-0014 | Editorial change or revision note | Explain controlled changes | standards, grammars, datasets, guidelines, dictionaries |

## Method coverage

The catalogue intentionally includes patterns for:

- descriptive and documentary work;
- theoretical argument;
- corpus and historical research;
- elicitation and experimental judgment work;
- field records and qualitative commentary;
- lexicography;
- annotation and resource publication;
- computational linguistics;
- methods, summaries, limitations, and revision history.

The patterns do not require one evidence hierarchy. A document can use corpus evidence, participant judgments, formal proof, interactional analysis, archival records, acoustic measurements, ethnographic observation, or another declared method.

## Theory-neutrality review

The catalogue does not require:

- a generative, functional, cognitive, constructional, usage-based, structuralist, interactional, or other framework;
- a universal inventory of linguistic entities;
- one definition of grammaticality, acceptability, productivity, frequency, or meaning;
- one relation between description and explanation;
- one annotation ontology;
- one theory of the lexicon;
- one model of speaker knowledge;
- computational implementation.

Potential theory bias remains in words such as *construction*, *feature*, *category*, *derivation*, *form*, and *function*. Pattern text uses these as replaceable examples, not mandatory ontological commitments.

## Language and scholarly-tradition review

The current drafts are written in English and may reflect English-language academic organization.

Before stabilization, evaluation must include:

- authors who publish primarily in languages other than English;
- translated and multilingual documents;
- signed-language research;
- community-authored and community-reviewed documentation;
- traditions in which argument, evidence, or citation order differs from the proposed shared order;
- documents that use non-Latin scripts, mixed writing systems, or transcription systems;
- research in which access restrictions prevent full public provenance disclosure.

The required distinctions may remain stable even when the preferred heading order changes. Evaluation must distinguish a true comprehension benefit from an English rhetorical preference.

## Genre-combination review

Many real documents combine patterns:

- a grammar chapter can combine SLE-PATTERN-0001, 0002, and 0003;
- a corpus article can combine 0004, 0003, and 0012;
- a documentation deposit can combine 0006, 0010, and 0013;
- an annotation manual can combine 0007, 0011, and 0014;
- a computational paper can combine 0009, 0004, and 0003;
- a dictionary introduction can combine 0008, 0010, and 0011.

Evaluation must test whether combined patterns cause duplication, contradictory ordering, or excessive authoring burden.

## Required-distinction coverage

| Distinction | Principal patterns | Status |
|---|---|---|
| recorded material vs analysis | 0001, 0003, 0006, 0007, 0010 | represented; requires field testing |
| observation vs interpretation | 0001–0006, 0009, 0012 | represented; proposed |
| attestation vs stronger claims | 0001, 0002, 0004, 0008 | represented; proposed |
| response vs author conclusion | 0005, 0006, 0007 | represented; proposed |
| tool behavior vs language fact | 0009, 0010 | represented; proposed |
| hypothesis vs conclusion | 0003, 0012, 0013 | represented; proposed |
| requirement vs recommendation | 0007, 0011, 0014 | represented; proposed |
| source vs transformation | 0004, 0006, 0008, 0010 | represented; proposed |
| current coverage vs intended coverage | 0009, 0010, 0013, 0014 | represented; proposed |
| limitation vs uninvestigated area | all research patterns | represented; proposed |

## Conformance-model review

The proposed states are:

- **SLE-Prepared** — author self-review;
- **SLE-Reviewed** — independent human editorial review;
- **SLE-Evaluated** — defined reader, author-preservation, translation, or expert evaluation.

These states are intentionally human-first. They do not require software.

Risks requiring evaluation:

1. **Status inflation:** readers may interpret *Reviewed* or *Evaluated* as scientific approval.
2. **Reviewer variability:** two reviewers may apply a qualitative pattern differently.
3. **Author burden:** detailed pattern review may be excessive for short notes or examples.
4. **Publisher mismatch:** journal structures may conflict with the proposed order.
5. **False completeness:** use of all headings may hide weak evidence rather than improve communication.
6. **Access inequality:** independent review may be unavailable to individual or community researchers.

Safeguards in the proposed chapter:

- conformance applies to a stated document or part;
- a declaration must not certify truth or method;
- headings are optional;
- permitted omissions and waivers are explicit;
- SLE-Evaluated names the type of evaluation rather than implying universal approval;
- tools are optional aids only.

## Waiver-model review

A waiver records a communication departure. It must not conceal:

- unsupported linguistic claims;
- missing evidence;
- ethical or consent problems;
- a methodological defect;
- a theoretical disagreement;
- an unresolved data conflict.

Those matters belong in the document's content as limitations, alternatives, or open questions.

Evaluation must test whether the waiver record is proportionate for short documents and whether publisher-level waivers can be reused without becoming hidden local standards.

## Versioning review

The proposed pattern IDs are stable and version-independent.

The major/minor/patch model applies to the public reference artifact, but this remains a governance proposal. Before stabilization, reviewers must test:

- whether a new required pattern element is always backward-compatible;
- whether changes to examples can change normative interpretation;
- whether conformance-state changes require a major release;
- how translated editions relate to the controlling version;
- how corrections to harmful or misleading guidance should be released rapidly.

## Known omissions

The v0.1 catalogue does not yet define a dedicated pattern for:

- phonetic or laboratory measurement reports;
- conversation-analysis transcripts and sequential analyses;
- sociolinguistic ethnography;
- signed-language video example presentation;
- language-teaching materials;
- ethics and consent protocols;
- grant proposals or institutional reports;
- peer reviews;
- project-management records.

Some of these may be covered by combinations of existing patterns. Others may require a new pattern or informative annex after evidence and testing.

## Evaluation matrix

Each pattern must be tested through at least the applicable procedures below.

| Evaluation | Question |
|---|---|
| reader reconstruction | Can readers identify purpose, scope, direct result, interpretation, and limitation? |
| author meaning preservation | Does applying the pattern preserve the author's intended claim and evidential force? |
| authoring burden | Does the pattern require unnecessary repetition or documentation? |
| domain-expert review | Does the pattern preserve legitimate field conventions and distinctions? |
| theory-neutrality review | Does the wording favor one framework without necessity? |
| method-neutrality review | Does the pattern privilege one evidence source or inferential method? |
| translation review | Can the distinctions be expressed naturally outside English? |
| accessibility review | Can readers with different expertise levels navigate the document? |
| genre-combination review | Can multiple patterns combine without duplication or conflict? |
| waiver review | Do omissions remain visible without creating excessive process? |

## Stabilization gates

A pattern cannot become stable until:

1. at least two substantially different linguistic domains have tested it;
2. author and reader results show a communication benefit or consistency benefit;
3. no material loss of linguistic meaning remains unresolved;
4. theory and method reviews find no unjustified universalization;
5. translation or multilingual review identifies no unmanageable English-specific dependency;
6. permitted omissions and waivers work in realistic documents;
7. the pattern's required distinctions and conformance effect are clear.

## Disposition

All 14 patterns, three conformance states, the waiver model, and the versioning model remain **proposed**.

The register supports issue #5's first auditable draft. It does not authorize publication as a stable standard.