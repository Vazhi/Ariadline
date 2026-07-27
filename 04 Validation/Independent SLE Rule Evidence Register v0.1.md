---
title: "Independent SLE Rule Evidence Register v0.1"
type: evidence-register
status: proposed
version: "0.1"
created: 2026-07-27
updated: 2026-07-27
tags:
  - sle
  - evidence
  - language-rules
  - cross-domain
---
# Independent SLE Rule Evidence Register v0.1

## Purpose

This register records the independent basis for [[SLE for Linguistics Language Rules v0.1]].

The Canto-span project is not an authority in this register. Canto-span can provide later test cases only after a candidate SLE rule exists.

The register distinguishes:

- **direct support**: a source explicitly states an equivalent communication control;
- **convergent practice**: independent domains use a similar control for clarity, reproducibility, or consistency;
- **pilot rationale**: the rule is plausible but still requires reader and author testing.

A source can justify the communication problem without controlling the exact wording of an SLE rule.

## External source set

### ER-01 — ISO House Style

Official standards-drafting guidance from ISO. Relevant controls include plain language, short and focused sentences, consistent normative verbal forms, explicit references to figures and tables, and terminology consistency.

Source: [ISO House Style](https://www.iso.org/fr/home/developing-standards/resources/drafting-standards/iso-house-style-search.html), updated 2025-05-21.

Domain: international standards drafting and translation.

### ER-02 — Leipzig Glossing Rules

The Leipzig Glossing Rules provide shared conventions for interlinear morpheme-by-morpheme glosses while allowing declared flexibility.

Source: [Leipzig Glossing Rules](https://www.eva.mpg.de/lingua/resources/glossing-rules.php), revised February 2008; site last changed 2015-05-31.

Domain: typology, descriptive linguistics, field linguistics, and language documentation.

### ER-03 — ISO normative verbal forms and conformance boundary

ISO distinguishes requirements, recommendations, permissions, and capabilities and defines conformance against document requirements.

Source: [ISO Foreword — supplementary information](https://www.iso.org/foreword-supplementary-information.html).

Domain: normative reference documents and conformity assessment.

SLE adopts the need for stable meanings but independently chooses **must** as its requirement verb.

### ER-04 — Generic Style Rules for Linguistics

The Generic Style Rules seek uniform, functional, and simple conventions across linguistic journals and books.

Source: [Generic Style Rules for Linguistics](https://www.eva.mpg.de/de/linguistics/past-research-resources/resources/generic-style-rules).

Domain: general linguistic publishing.

### ER-05 — Linguistic Society of America proceedings guidance

The LSA proceedings guidance requires adherence to a style sheet and complete, consistent citation and reference information.

Source: [Proceedings of the Linguistic Society of America — submissions](https://journals.linguisticsociety.org/proceedings/index.php/PLSA/about/submissions).

Domain: general linguistics publishing and references.

### ER-06 — ACL reproducibility checklist

The ACL-IJCNLP checklist asks authors to identify experimental settings, evaluation measures, datasets, languages, exclusions, preprocessing, collection methods, and quality controls.

Source: [ACL-IJCNLP 2021 Reproducibility Checklist](https://2021.aclweb.org/calls/reproducibility-checklist/).

Domain: computational linguistics, experiments, datasets, and language resources.

### ER-07 — ACL review criteria

The ACL 2023 review form asks whether scientific claims are clearly stated and adequately supported and whether methods and resources are described in enough detail for evaluation and reproduction.

Source: [ACL 2023 Peer Review Form](https://2023.aclweb.org/blog/review-form/).

Domain: computational and empirical linguistics review.

### ER-08 — Cross-Linguistic Data Formats

CLDF emphasizes explicit semantics, stable identifiers, compatibility, hand-editable data, and separation between data and tools.

Source: [Cross-Linguistic Data Formats](https://cldf.clld.org/).

Domain: typology, historical linguistics, lexical data, and reusable language resources.

### ER-09 — Component Metadata Infrastructure

CMDI provides reusable metadata components and profiles for describing language resources across research communities.

Source: [CMDI metadata information](https://archive.mpi.nl/forums/t/cmdi-metadata-information/2640).

Domain: language documentation, archives, corpora, and metadata interoperability.

### ER-10 — Penn Parsed Corpora documentation

The 2025 LDC release describes explicit corpus periods, encoding, annotation formats, documentation, review, corrections, and versioned updates.

Source: [Penn Parsed Corpora of Historical English, second release](https://catalog.ldc.upenn.edu/LDC2025T09).

Domain: corpus linguistics, historical linguistics, annotation, and language-resource publication.

## Rule evidence matrix

| Rule | Primary communication problem | Independent support | Evidence status |
|---|---|---|---|
| SLE-RULE-0001 | Multiple assertions hide inference and scope | ER-01, ER-04 | direct + convergent |
| SLE-RULE-0002 | Ambiguous antecedent | ER-01, ER-04 | convergent |
| SLE-RULE-0004 | Synonym variation creates concept drift | ER-01, ER-04, ER-08 | direct + convergent |
| SLE-RULE-0005 | Undefined terms prevent consistent interpretation | ER-01, ER-04, ER-08 | direct + convergent |
| SLE-RULE-0006 | Comparison lacks baseline or measure | ER-06, ER-07 | convergent |
| SLE-RULE-0007 | Negation or quantifier scope changes claim | ER-01, ER-04 | pilot rationale + convergent |
| SLE-RULE-0016 | Reader acts before seeing applicability condition | ER-01, ER-06 | convergent |
| SLE-RULE-0017 | Multi-action instructions hide skipped or failed steps | ER-01, ER-06, ER-10 | convergent |
| SLE-RULE-0008 | Modal variation obscures conformance force | ER-01, ER-03 | direct |
| SLE-RULE-0019 | Data and interpretation are conflated | ER-06, ER-07, ER-10 | convergent |
| SLE-RULE-0020 | Evidence wording overstates inference | ER-06, ER-07 | pilot rationale + convergent |
| SLE-RULE-0003 | Claim scope expands beyond sampled domain | ER-06, ER-07, ER-08, ER-09 | direct + convergent |
| SLE-RULE-0010 | Judgment result cannot be interpreted or reproduced | ER-06, ER-07 | direct |
| SLE-RULE-0021 | Absence claim hides search sensitivity | ER-06, ER-07, ER-10 | convergent |
| SLE-RULE-0009 | Attestation is treated as stronger evidence | ER-06, ER-07, ER-08 | pilot rationale + convergent |
| SLE-RULE-0015 | Tool output is treated as language evidence | ER-06, ER-07, ER-08, ER-10 | cross-domain rationale |
| SLE-RULE-0022 | Limitation or counterexample is detached from claim | ER-06, ER-07 | direct + convergent |
| SLE-RULE-0023 | Reader cannot map evidence to claim | ER-01, ER-05, ER-06, ER-07 | direct + convergent |
| SLE-RULE-0011 | Example provenance is misread | ER-02, ER-04, ER-05 | convergent |
| SLE-RULE-0012 | Judgment symbols vary across traditions | ER-02, ER-04 | field-specific convergence |
| SLE-RULE-0013 | Relative references break after editing | ER-01, ER-02, ER-04, ER-05 | direct + convergent |
| SLE-RULE-0024 | Gloss conventions or analysis layers are unclear | ER-02, ER-04 | direct |
| SLE-RULE-0014 | Dataset or transformation cannot be identified | ER-06, ER-08, ER-09, ER-10 | direct + convergent |
| SLE-RULE-0018 | Stylistic conformance is mistaken for scientific validity | ER-03, ER-06, ER-07 | standards boundary + research boundary |

## Cross-domain coverage

The source set includes:

- international standards drafting;
- general linguistic publishing;
- typology and descriptive glossing;
- computational and experimental linguistics;
- historical corpus linguistics;
- annotation and language-resource publication;
- language documentation and metadata;
- cross-linguistic data exchange.

This coverage is sufficient for a first draft. It is not sufficient for final adoption.

## Missing coverage before stabilization

Before a rule becomes stable, the project should add direct review from:

- phonetics and laboratory phonology;
- formal syntax and semantics;
- sociolinguistics and variation;
- lexicography and dictionary writing;
- signed-language research;
- community-based language documentation;
- qualitative discourse and conversation analysis;
- annotation manuals written for non-specialist annotators;
- languages whose academic writing conventions differ substantially from English.

## Evidence safeguards

1. A source does not become normative merely because it is widely used.
2. A formatting convention does not automatically justify a language rule.
3. A computational reproducibility checklist does not govern non-computational research.
4. A glossing rule does not govern the underlying linguistic analysis.
5. A Canto-span practice cannot supply normative justification.
6. A proposed SLE rule must survive reader testing and author-preservation testing under [[Pilot Study Design]].
7. A rule must be revised or rejected when it removes a necessary distinction or favors one linguistic theory without justification.

## Disposition

All 24 rules remain **proposed**. None is stable in v0.1.

The evidence register supports drafting and evaluation. It does not by itself authorize publication as a final standard.
