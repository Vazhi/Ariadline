---
title: "Human Review Boundary Register v0.1"
type: validation-register
status: proposed
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - ariadline
  - conformance
  - review-boundary
  - neutrality
---
# Human Review Boundary Register v0.1

## Purpose

This register prevents human editorial review from being mistaken for linguistic, methodological, ethical, accessibility, translation, software, or community certification.

It supports [[Ariadline Editorial Conformance Checklist v0.1]], [[Profiles and Conformance]], and `SLE-RULE-0018` in [[Ariadline Language Rules v0.1]].

## Core rule

A reviewer may decide whether text communicates its authorized or declared content under applicable Ariadline controls.

A reviewer may not use an Ariadline result to certify:

- linguistic truth;
- grammaticality or acceptability;
- theoretical superiority;
- methodological or statistical validity;
- ethical adequacy;
- translation quality;
- accessibility for a population;
- software correctness;
- community authority.

These matters require separately named authority and evidence.

## Boundary decisions

| Area | Human Ariadline reviewer may decide | Human Ariadline reviewer must not decide | Appropriate separate record |
|---|---|---|---|
| authorized meaning | whether the controlling meaning record is identified and whether a revision visibly changes it | what an authentic author intended when no legitimate meaning authority exists | source-author, authorized-proxy, or community review |
| claim scope | whether population, variety, dataset, period, or condition is recoverable | whether the sample justifies the generalization | domain or methods review |
| evidence connection | whether a claim points to its stated support | whether support is sufficient or scientifically valid | substantive peer review |
| evidential wording | whether wording exceeds the support the document itself declares | one universal evidence-verb hierarchy | domain adjudication |
| observation and interpretation | whether the distinction is visible | whether the interpretation is correct | theoretical or analytical review |
| terminology | whether a controlled concept has a stable declared label | which theoretical term a field should adopt | terminology governance or domain review |
| definitions | whether the intended definition is available and usable | whether the definition is theoretically correct | domain review |
| judgments | whether task, population, response, item scope, and result are reported | whether responses establish grammaticality | experimental or field-method review |
| examples | whether provenance, modification, and production method are declared | whether an example is acceptable, authentic, or community-authorized | source-author, speaker, language, or community review |
| glossing | whether conventions and abbreviations are declared and layers are distinguishable | whether segmentation and gloss analysis are correct | language-specific expert review |
| datasets | whether identity, version, and transformations are stated | whether transformations are methodologically justified | data and methods review |
| systems | whether system state and output boundaries are stated | whether system output or linguistic analysis is correct | software evaluation and domain review |
| procedures | whether conditions, actions, and normative functions are clear | whether a procedure is safe, efficient, ethical, or scientifically valid | operational, safety, ethics, or methods review |
| limitations | whether a stated limitation connects to the affected claim | whether every possible limitation was found | author, domain, and peer review |
| conformance declaration | whether the result is bounded to the declared artifact and applicable rules | whether content is true, ethical, valid, accessible, or approved | separately named certification or review |
| translation | whether a translated edition declares controlling source and normative functions | whether meaning is preserved across languages | translator and bilingual domain review |
| accessibility | whether an evaluation record identifies scope and method | whether the document is accessible to all users | accessibility testing |
| community authority | whether access, attribution, and authority boundaries are stated | whether representation is culturally or politically authorized | community-controlled review |
| historical statements | whether historical state, current state, and source date are distinguished | whether reconstruction is correct | historical or archival review |
| citations | whether a claim has an identifiable source reference | whether the source is correct, complete, or persuasive | source verification and peer review |
| ethics | whether text avoids implying Ariadline ethics approval | whether collection, consent, or publication is ethical | ethics board or community authority |

## Escalation outcomes

Use one of these when the boundary is reached:

- **Pass for communication; substantive review pending**
- **Not determined — authorized meaning is unclear or unavailable**
- **Not determined — domain authority required**
- **Not applicable to Ariadline**
- **Fail — the text falsely implies substantive certification**
- **Separate review record supplied**

## Conflict rule

When an editorial correction could alter polarity, quantification, scope, evidence force, theoretical commitment, example status, access boundary, or normative force:

1. do not silently revise the passage;
2. identify the authorized meaning record or record its absence;
3. preserve the competing versions;
4. request author, proxy, translator, community, or domain review as applicable;
5. use **not determined** until meaning authority resolves the conflict.

Use [[Ariadline Semantic Equivalence Review Template v0.1]] and [[Semantic Equivalence Review Record v0.1]] for passage-to-brief and preservation decisions.

## Canto-span boundary

Canto-span findings remain project-adoption findings unless the same communication problem has independent multi-domain support. Its statuses, parser labels, workflows, and release practices cannot become Ariadline criteria through this register.