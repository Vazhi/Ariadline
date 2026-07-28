---
title: "Independent Ariadline Rule Evidence Register v0.1"
type: evidence-register
status: proposed
version: "0.1"
created: 2026-07-27
updated: 2026-07-27
tags:
  - ariadline
  - evidence
  - language-rules
  - cross-domain
---
# Independent Ariadline Rule Evidence Register v0.1

## Purpose

This register records the independent basis for [[Ariadline Language Rules v0.1]].

Canto-span is not an authority in this register. It can provide later test cases only after a candidate Ariadline rule exists.

## Evidence roles

Every rule mapping distinguishes three roles:

1. **Problem evidence** — an independent source documents the communication, interpretation, consistency, or reproducibility problem.
2. **Control evidence** — an independent source explicitly uses or recommends an equivalent control.
3. **Ariadline-local hypothesis** — Ariadline proposes a more specific formulation that still requires reader, author, neutrality, and cross-domain evaluation.

A source can establish a problem without establishing the exact Ariadline wording. `Direct` is used only when the cited locator states an equivalent control. `Convergent` means that more than one independent practice points in the same direction. It does not mean that the Ariadline wording is already validated.

## External sources and exact locators

### ER-01 — ISO House Style

Source: [ISO House Style](https://www.iso.org/fr/home/developing-standards/resources/drafting-standards/iso-house-style-search.html), updated 2025-05-21.

Exact locators:

- **ER-01-A — Text → Plain English:** plain English reduces misunderstanding and mistranslation; use short sentences and paragraphs; include one idea in each sentence.
- **ER-01-B — Text → Relationship with the ISO/IEC Directives, Parts 1 and 2:** `shall` indicates a requirement, `should` a recommendation, `may` a permission, and `can` a possibility or capability.
- **ER-01-C — Text → Plain English → Might and could:** use `may` for permission and `can` for possibility or capability; avoid undefined alternatives when they can cause confusion or mistranslation.

Domain: international standards drafting and translation.

### ER-02 — Leipzig Glossing Rules

Source: [Leipzig Glossing Rules](https://www.eva.mpg.de/lingua/resources/glossing-rules.php), revised February 2008; site last changed 2015-05-31.

Exact locators:

- **ER-02-A — About the rules:** the rules are shared conventions but authors may add or modify conventions.
- **ER-02-B — The rules → Preamble:** different purposes permit different detail; alternatives and flexibility are allowed; glossing conventions do not decide between linguistic analyses.
- **ER-02-C — Preamble, paragraph on cited data:** glosses are analysis rather than data and may be changed when an author adopts different terminology, style, or analysis.
- **ER-02-D — Rule 1: Word-by-word alignment:** interlinear glosses are aligned vertically with the example.

Domain: typology, descriptive linguistics, field linguistics, and language documentation.

### ER-03 — ISO conformance and verbal-form declaration

Source: [ISO Foreword supplementary information](https://www.iso.org/foreword-supplementary-information.html) and ER-01-B.

Exact locator:

- **ER-03-A — Verbal forms:** ISO declares separate forms for requirement, recommendation, permission, and capability and explains that conformance relates to document requirements.

Domain: normative reference documents and conformity assessment.

### ER-04 — Generic Style Rules for Linguistics

Source: [Generic Style Rules for Linguistics](https://www.eva.mpg.de/de/linguistics/past-research-resources/resources/generic-style-rules).

Exact locator:

- **ER-04-A — Page introduction:** the rules seek uniform conventions for text structure, examples, citations, and references and balance conventionality, functionality, and simplicity.

Domain: general linguistic publishing.

This source supports the general need for consistent conventions. It does not directly establish every Ariadline sentence or evidence rule.

### ER-05 — Linguistic Society of America proceedings guidance

Source: [Proceedings of the Linguistic Society of America — Submissions](https://journals.linguisticsociety.org/proceedings/index.php/PLSA/about/submissions).

Exact locators:

- **ER-05-A — Author Guidelines:** manuscripts must follow the stated formatting and style guidance, including citation and reference instructions.
- **ER-05-B — Submission Preparation Checklist:** references must contain the required information and follow the specified format.

Domain: general linguistics publishing and references.

### ER-06 — ACL-IJCNLP reproducibility checklist

Source: [ACL-IJCNLP 2021 Reproducibility Checklist](https://2021.aclweb.org/calls/reproducibility-checklist/).

Exact locators:

- **ER-06-A — For all reported experimental results:** describe the setting, model or algorithm, infrastructure, evaluation measures, and reported results.
- **ER-06-B — For all results involving multiple experiments:** report run counts, parameter bounds, selection methods, and summary statistics.
- **ER-06-C — For all datasets used:** report statistics, splits, exclusions, preprocessing, languages, and dataset access.
- **ER-06-D — For new data collected:** describe collection instructions and quality-control methods.

Domain: computational linguistics, experiments, datasets, and language resources.

### ER-07 — ACL 2023 peer-review form and policy

Sources: [ACL 2023 Peer Review Form](https://2023.aclweb.org/blog/review-form/) and [ACL 2023 Peer Review Policies](https://2023.aclweb.org/blog/review-acl23/).

Exact locators:

- **ER-07-A — Peer Review Form → 1. In-Depth Review → What is this paper about and what contributions does it make?:** identify the problem or question and the contributions.
- **ER-07-B — Peer Review Form → 3. Overall Recommendation → Soundness:** scientific claims should be clearly stated and adequately supported; methods and resources should be described in enough detail for evaluation and reproduction.
- **ER-07-C — Peer Review Policies → What is this paper about?:** claims should be clearly articulated and supported by appropriate evidence, literature, theory, or argument.
- **ER-07-D — Peer Review Policies → Reasons to reject:** conclusions should not exceed the evidence or argument; hypotheses and discussion should not be presented as established conclusions.

Domain: computational and empirical linguistics review.

### ER-08 — Cross-Linguistic Data Formats

Source: [Cross-Linguistic Data Formats](https://cldf.clld.org/) and the [CLDF ontology](https://cldf.clld.org/v1.0/terms.html).

Exact locators:

- **ER-08-A — Why?:** standardized formats support exchange and decouple tools and methods from databases.
- **ER-08-B — Design principles:** data should be human-editable and machine-readable; referenced entities should use identifiers; semantics must be explicit.
- **ER-08-C — Technology:** CLDF emphasizes a useful separation between data and tools.
- **ER-08-D — Ontology → ID and reference properties:** rows and referenced entities use stable identifiers, including example references.

Domain: typology, historical linguistics, lexical data, and reusable language resources.

### ER-09 — Component Metadata Infrastructure

Source: [CMDI metadata information](https://archive.mpi.nl/forums/t/cmdi-metadata-information/2640).

Exact locator:

- **ER-09-A — CMDI Metadata:** language-resource descriptions vary across communities; reusable components and profiles provide explicit, shareable descriptions while allowing domain-specific structures.

Domain: language documentation, archives, corpora, and metadata interoperability.

### ER-10 — Penn Parsed Corpora documentation

Source: [Penn Parsed Corpora of Historical English Second Release](https://catalog.ldc.upenn.edu/LDC2025T09).

Exact locators:

- **ER-10-A — Introduction:** the release identifies periods, constituent corpora, corrections, annotation changes, directory changes, and updated documentation.
- **ER-10-B — Data:** the release identifies text forms, manual review, encoding, file formats, and annotation format.

Domain: corpus linguistics, historical linguistics, annotation, and language-resource publication.

### ER-11 — IETF BCP 14 requirement words

Source: [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.html), updated by RFC 8174.

Exact locators:

- **ER-11-A — Abstract:** standards documents declare the special meanings of requirement words.
- **ER-11-B — Sections 1–5:** `MUST` or `SHALL` indicates an absolute requirement; `MUST NOT` or `SHALL NOT` a prohibition; `SHOULD` a recommendation with possible justified exceptions; `MAY` permission or optionality.
- **ER-11-C — Section 6, Guidance in the use of these Imperatives:** requirement words should be used carefully and only where the requirement is necessary for the specification’s purpose.

Domain: technical specifications and conformance language.

## Rule-by-rule traceability

| Rule | Problem evidence | Control evidence | Ariadline-local hypothesis or unresolved design choice |
|---|---|---|---|
| SLE-RULE-0001 | ER-01-A documents misunderstanding and one-idea guidance. | ER-01-A explicitly recommends one idea per sentence. | “One principal message” and its exception boundary require linguistic reader testing. |
| SLE-RULE-0002 | ER-01-A and ER-04-A support unambiguous, functional prose. | No cited source in v0.1 states the exact antecedent test. | The substitution test is Ariadline-local. |
| SLE-RULE-0003 | ER-06-C, ER-07-B, and ER-09-A show that data, population, and resource scope affect interpretation. | ER-06-C directly requires dataset, language, exclusion, and preprocessing information. | Near-claim placement and the full scope list are Ariadline-local. |
| SLE-RULE-0004 | ER-01-A, ER-04-A, and ER-08-B document consistency and explicit semantics problems. | ER-04-A and ER-08-B support consistent conventions and semantics. | One preferred term per controlled concept remains subject to multilingual testing. |
| SLE-RULE-0005 | ER-08-B and ER-09-A document the need for explicit semantics. | ER-08-B directly supports explicit semantics for reusable data. | The “before claim-critical use” timing is Ariadline-local. |
| SLE-RULE-0006 | ER-06-A/B and ER-07-B show that measures and evaluation bases must be interpretable. | ER-06-A/B requires defined measures and reported statistics. | The exact item–dimension–measure triad is Ariadline-local. |
| SLE-RULE-0007 | ER-01-A supports unambiguous prose. | No source in this set states the exact quantifier-negation control. | The paraphrase test is Ariadline-local and needs formal-semantics review. |
| SLE-RULE-0008 | ER-01-B/C, ER-03-A, and ER-11-A document ambiguity when normative terms are not declared consistently. | ER-01-B/C and ER-11-B directly define stable function mappings. | Ariadline does not yet choose **must** over **shall**; the final form requires comparison and reader testing. |
| SLE-RULE-0009 | ER-07-C/D establishes that conclusions must not exceed evidence; ER-08-B requires explicit semantics. | No source in this set directly states “attestation is not productivity.” | The specific linguistic inference boundary is Ariadline-local and requires corpus, fieldwork, and theoretical review. |
| SLE-RULE-0010 | ER-06-D and ER-07-B show that collected responses require method and population information. | ER-06-D directly requires collection instructions and quality-control description. | The exact task–response–population–item–result fields are Ariadline-local pending experimental and fieldwork review. |
| SLE-RULE-0011 | ER-02-B/C shows that example presentation and analysis can differ and that cited glosses can be changed. | ER-02-C directly requires treating changed glosses as analysis rather than unchanged data. | The four provenance dimensions are Ariadline-local and must be tested across elicited, corpus, constructed, and system-produced examples. |
| SLE-RULE-0012 | ER-02-A/B and ER-04-A show convention variation. | ER-02-A/B explicitly permits modified or alternative conventions. | Requiring task or population linkage for every symbol remains Ariadline-local. |
| SLE-RULE-0013 | ER-05-B and ER-08-D show the need for complete references and identifiers. | ER-08-D directly provides stable IDs and example references. | The “referred to more than once” threshold is Ariadline-local. |
| SLE-RULE-0014 | ER-06-C, ER-09-A, and ER-10-A/B document version, preprocessing, metadata, and format requirements. | ER-06-C directly requires exclusions and preprocessing; ER-10-A/B demonstrates release and format identification. | “Material transformation” needs profile-specific interpretation. |
| SLE-RULE-0015 | ER-06-A/C and ER-08-A/C distinguish system, data, and method descriptions. | ER-08-C directly emphasizes separation between data and tools. | The prohibition on treating system output as speaker evidence is an Ariadline-local epistemic safeguard. |
| SLE-RULE-0016 | ER-01-A supports clear instructions; ER-06-D requires usable collection instructions. | No source in this set directly requires condition-first order. | Condition-first order is Ariadline-local and requires procedural testing. |
| SLE-RULE-0017 | ER-01-A supports focused sentences and instructions. | ER-01-A directly supports one idea per sentence. | One principal action per step and the independence test are Ariadline-local. |
| SLE-RULE-0018 | ER-03-A separates conformance from content; ER-07-B evaluates scientific soundness independently. | ER-03-A directly limits conformance to declared document requirements. | The expanded truth, ethics, theory, and method disclaimer is an Ariadline-local safeguard. |
| SLE-RULE-0019 | ER-07-C/D distinguishes claims, evidence, hypotheses, and conclusions; ER-10-A/B separates documented data and annotation description. | ER-07-D directly warns against presenting unsupported claims as conclusions. | Mandatory local separation of record and interpretation is Ariadline-local. |
| SLE-RULE-0020 | ER-07-B/C/D directly documents overstatement when conclusions exceed evidence. | ER-07-D supports matching conclusion strength to evidence or argument. | No universal evidence-verb hierarchy is adopted; lexical mappings are deferred for evaluation. |
| SLE-RULE-0021 | ER-06-C and ER-07-B show that search/test coverage and method affect conclusions. | ER-06-C directly requires exclusions and preprocessing. | A mandatory sensitivity-limit statement for absence claims is Ariadline-local. |
| SLE-RULE-0022 | ER-07-C/D requires appropriate support and acknowledgement of counterarguments or unsupported conclusions. | ER-07-C explicitly asks for appropriate evidence and counterarguments. | Local attachment of each limitation to an affected claim is Ariadline-local. |
| SLE-RULE-0023 | ER-05-B, ER-06-A, and ER-07-B show that claims and references must be traceable. | ER-05-B directly requires complete references; ER-07-B requires adequate support. | The exact local cross-reference forms are Ariadline-local. |
| SLE-RULE-0024 | ER-02-A/B/D documents shared glossing conventions, flexibility, and alignment. | ER-02-D directly states word-by-word alignment; ER-02-A/B permits declared alternatives. | The exact Ariadline declaration wording remains proposed. |

## Cross-domain coverage and limits

The sources cover standards drafting, general linguistic publishing, descriptive and typological glossing, computational and empirical review, historical corpora, annotation, metadata, and cross-linguistic data exchange.

This coverage is sufficient to justify a first proposed draft. It is not sufficient for stabilization.

Before any rule becomes stable, the project must add direct review from phonetics and laboratory phonology, formal syntax and semantics, sociolinguistics and variation, lexicography, signed-language research, community-based language documentation, qualitative discourse and conversation analysis, non-specialist annotation manuals, and academic traditions whose writing conventions differ substantially from English.

## Evidence safeguards

1. A source does not become normative merely because it is widely used.
2. A formatting convention does not automatically justify a language rule.
3. A computational checklist does not govern non-computational research.
4. A glossing rule does not govern the underlying linguistic analysis.
5. Two documents from the same research community do not by themselves establish cross-domain convergence.
6. A Canto-span practice cannot supply normative justification.
7. Every Ariadline-local hypothesis must survive reader testing, author meaning-preservation testing, neutrality review, and multi-domain review.
8. A rule must be revised or rejected when it removes a necessary distinction or favors one theory without justification.

## Disposition

All 24 rules remain **proposed**. None is stable in v0.1.

The evidence register supports drafting and evaluation. It does not authorize publication as a final standard.
