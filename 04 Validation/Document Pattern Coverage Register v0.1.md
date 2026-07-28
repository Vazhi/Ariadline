---
title: "Document Pattern Coverage Register v0.1"
type: validation-register
status: proposed
version: "0.1"
created: 2026-07-27
updated: 2026-07-27
tags:
  - ariadline
  - validation
  - document-patterns
  - neutrality
---
# Document Pattern Coverage Register v0.1

## Purpose

This register reviews the proposed patterns in [[Ariadline Document Patterns v0.1]].

It records intended coverage, known gaps, neutrality risks, conformance risks, and evaluation requirements. It does not certify that the patterns are universally valid or final.

Conformance semantics are defined in [[Profiles and Conformance]]. Exact profile mappings are defined in [[Ariadline Profile Applicability Register v0.1]].

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
| SLE-PATTERN-0012 | Research summary | Give a bounded concise account | abstracts, literature and project summaries |
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
- traditions in which argument, evidence, or citation order differs from the recommended default sequence;
- documents using non-Latin scripts, mixed writing systems, or transcription systems;
- research in which access restrictions prevent full public provenance disclosure.

The required information relationships may remain stable even when the rhetorical order changes. Reordering is not a waiver condition by itself.

Evaluation must distinguish a true comprehension benefit from an English rhetorical preference.

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

## Conformance-result review

The proposed results are:

- **conforms**;
- **conforms with declared waivers**;
- **does not conform**;
- **not determined**.

Risks requiring evaluation:

1. **False certification:** readers may treat a communication result as scientific approval.
2. **Reviewer variability:** different reviewers may apply qualitative controls differently.
3. **Waiver inflation:** repeated waivers may hide an unsuitable control.
4. **Not-determined misuse:** incomplete reviews may be presented as near-passing results.
5. **Access inequality:** independent review may be unavailable to individual or community researchers.

Safeguards:

- result is bounded to a stated conformance object;
- result is separate from review method and evaluation records;
- unresolved applicable nonconformities prevent a **conforms** result;
- a declaration must not certify truth or method;
- tools are optional aids only.

## Review-method review

Review methods include author self-review, independent editorial review, and other declared human methods.

The method records who checked the text. It does not indicate pass or fail.

Evaluation must test whether a self-review record is sufficiently auditable and whether independent-review expectations create disproportionate access barriers.

## Typed-evaluation review

Reader comprehension, author meaning preservation, translation, accessibility, domain-expert review, theory neutrality, method neutrality, genre combination, and authoring burden are separate evaluation types.

They are not interchangeable levels.

Every evaluation record must identify:

- type;
- exact document scope or sample;
- method;
- participant or evaluator role;
- date;
- findings and limitations.

Evaluation of representative passages must not be presented as evaluation of the entire document.

## Profile auditability review

The profile applicability register maps each profile to exact rule IDs and a profile-set version.

A declaration must identify the profile-set version and preserve an exact record of conditional rules that were applied or judged not applicable.

Evaluation must test whether two reviewers reconstruct the same applicable rule set from the same profile declaration and text.

## Waiver-model review

A waiver records a communication departure. It must not conceal:

- unsupported linguistic claims;
- missing evidence;
- ethical or consent problems;
- a methodological defect;
- a theoretical disagreement;
- an unresolved data conflict.

Evaluation must test whether the waiver record is proportionate for short documents and whether publisher-level waivers can be reused without becoming hidden local standards.

## Versioning review

Version class follows compatibility effect.

A new rule, pattern element, or clarification is major when it changes an existing profile's obligations or prior conformance outcomes. It is minor only when optional or otherwise backward-compatible. Patch changes cannot alter obligations or review results.

Before stabilization, reviewers must test:

- whether compatibility can be determined consistently;
- whether transition mechanisms preserve prior declarations explicitly;
- whether profile mapping changes always receive appropriate migration treatment;
- how translated editions relate to the controlling version;
- how urgent corrections are released without misclassification.

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

Some may be covered by combinations of existing patterns. Others may require a new pattern or informative annex after evidence and testing.

## Evaluation matrix

| Evaluation | Question |
|---|---|
| reader reconstruction | Can readers identify purpose, scope, direct result, interpretation, and limitation? |
| alternative order | Do non-English or field-specific rhetorical orders preserve recoverable relationships? |
| author meaning preservation | Does applying the pattern preserve intended claim and evidential force? |
| authoring burden | Does the pattern require unnecessary repetition or process? |
| domain-expert review | Does the pattern preserve legitimate field conventions? |
| theory-neutrality review | Does wording favor one framework without necessity? |
| method-neutrality review | Does the pattern privilege one evidence source or inferential method? |
| translation review | Can the distinctions be expressed naturally outside English? |
| accessibility review | Can readers with different expertise levels navigate the document? |
| genre-combination review | Can patterns combine without duplication or conflict? |
| profile reconstruction | Do reviewers derive the same exact rule set? |
| conformance-result review | Do reviewers separate pass/fail result from review process? |
| waiver review | Do omissions remain visible without excessive process? |

## Stabilization gates

A pattern or conformance control cannot become stable until:

1. at least two substantially different linguistic domains have tested it;
2. author and reader results show a communication or consistency benefit;
3. no material loss of linguistic meaning remains unresolved;
4. theory and method reviews find no unjustified universalization;
5. translation or multilingual review identifies no unmanageable English-specific dependency;
6. alternative rhetorical orders remain conforming when relationships are recoverable;
7. permitted omissions and waivers work in realistic documents;
8. profiles resolve to reproducible rule sets;
9. conformance result, review method, and evaluation records remain distinguishable;
10. versioning decisions follow compatibility effect consistently.

## Disposition

All 14 patterns, four conformance results, review-method guidance, typed evaluation records, the profile mappings, waiver model, and versioning model remain **proposed**.

The register supports issue #5's first auditable draft. It does not authorize publication as a stable standard.
