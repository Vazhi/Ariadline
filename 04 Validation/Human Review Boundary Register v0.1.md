---
title: "Human Review Boundary Register v0.1"
type: validation-register
status: proposed
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - sle
  - conformance
  - review-boundary
  - neutrality
---
# Human Review Boundary Register v0.1

## Purpose

This register prevents a human editorial review from being mistaken for linguistic, methodological, ethical, accessibility, translation, or software certification.

It supports [[SLE Editorial Conformance Checklist v0.1]], [[Profiles and Conformance]], and SLE-RULE-0018 in [[SLE for Linguistics Language Rules v0.1]].

## Core rule

A reviewer may decide whether the text communicates its declared content under the applicable SLE controls.

A reviewer may not use an SLE result to certify:

- the truth of a linguistic claim;
- the grammaticality or acceptability of an example;
- the superiority of a theory;
- the validity of a method or statistical analysis;
- the ethical adequacy of data collection or publication;
- the quality of a translation;
- the accessibility of a document for a specific population;
- the correctness of software output;
- the authority of a community representation.

These matters require separately named review authority and separately scoped evidence.

## Boundary decisions

| Area | Human SLE reviewer may decide | Human SLE reviewer must not decide | Appropriate separate record |
|---|---|---|---|
| claim scope | whether the stated population, variety, dataset, period, or condition is recoverable | whether the sample justifies the generalization | domain or methods review |
| evidence connection | whether a claim points to its stated support | whether the support is sufficient or scientifically valid | substantive peer review |
| evidential wording | whether wording exceeds the support that the document itself declares | one universal hierarchy for evidence verbs across fields | domain adjudication |
| observation and interpretation | whether the distinction is visible | whether the interpretation is correct | theoretical or analytical review |
| terminology | whether one controlled concept has a stable declared label | which theoretical terminology the field should adopt | terminology governance or domain review |
| definitions | whether the intended definition is available and usable | whether the definition is theoretically correct | domain review |
| judgments | whether task, population, response format, item scope, and result are reported | whether speakers' responses establish grammaticality | experimental or field-method review |
| examples | whether provenance, modification, and production method are declared | whether the example is acceptable or authentic | source-author, speaker, or community review |
| glossing | whether conventions and abbreviations are declared and layers are distinguishable | whether segmentation and gloss analysis are correct | language-specific expert review |
| datasets | whether identity, version, and transformations are stated | whether exclusions or transformations are methodologically justified | data and methods review |
| systems | whether system identity, state, input, and configuration are stated and system behavior is separated from language facts | whether the system output or linguistic analysis is correct | software evaluation and domain review |
| procedures | whether conditions, actions, and normative functions are clear | whether the procedure is safe, efficient, ethical, or scientifically valid | operational, safety, ethics, or methods review |
| limitations | whether a material stated limitation is connected to the affected claim | whether every possible limitation has been found | author, domain, and peer review |
| conformance declaration | whether the result is bounded to the declared artifact and applicable rules | whether the content is true, ethical, valid, accessible, or approved | separately named certification or review |
| translation | whether the translated edition declares its controlling source and normative functions | whether meaning is preserved across languages | translator and bilingual domain review |
| accessibility | whether an accessibility evaluation record identifies its scope and method | whether the document is accessible to all users | accessibility testing |
| community authority | whether the document states access, attribution, and authority boundaries | whether the representation is culturally or politically authorized | community-controlled review |
| historical statements | whether the text distinguishes historical state, current state, and source date | whether the historical reconstruction is correct | historical-linguistics or archival review |
| citations | whether a claim has an identifiable source reference | whether the cited source is correct, complete, or persuasive | source verification and peer review |
| ethics | whether the document avoids implying that SLE supplies ethics approval | whether collection, consent, or publication is ethical | ethics board or community authority |

## Escalation outcomes

Use one of these outcomes when the boundary is reached:

- **Pass for communication; substantive review pending**
- **Not determined — author meaning is unclear**
- **Not determined — domain authority required**
- **Not applicable to SLE**
- **Fail — the text falsely implies substantive certification**
- **Separate review record supplied**

## Conflict rule

When an editorial correction could alter polarity, quantification, scope, evidence force, theoretical commitment, example status, or normative force:

1. do not silently revise the passage;
2. record the conflict;
3. request author or authorized domain review;
4. preserve both versions when the disagreement matters to evaluation;
5. use **not determined** until the intended meaning is resolved.

Use [[SLE Semantic Equivalence Review Template v0.1]] and [[Semantic Equivalence Review Record v0.1]] for meaning-preservation decisions.

## Canto-span boundary

Canto-span findings remain project-adoption findings unless the same communication problem has independent multi-domain support. A Canto-span status, parser label, workflow, or release practice cannot become an SLE review criterion through this register.
