---
title: "Optional Automation Notes for SLE Review v0.1"
type: informative-note
status: informative
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - sle
  - automation
  - informative
  - non-normative
---
# Optional Automation Notes for SLE Review v0.1

## Status

This note is informative and outside the core reference artifact.

No software, schema, machine-readable diagnostic, repository metadata, or automated pass is required by [[SLE Editorial Conformance Checklist v0.1]].

A tool may flag text for human review. It cannot create a conformance result, establish authorized meaning, confirm preservation, determine linguistic truth, or replace human review.

## Possible assistance classes

| Assistance class | Potential rule areas | Required warning |
|---|---|---|
| terminology search | `SLE-RULE-0004`, `SLE-RULE-0005` | synonym and definition findings require human concept review |
| reference highlighting | `SLE-RULE-0002`, `SLE-RULE-0013` | intended antecedents cannot always be inferred automatically |
| comparison prompts | `SLE-RULE-0006` | detection does not reveal the author's intended comparison basis |
| normative-verb inventory | `SLE-RULE-0008` | the document's declared system controls; no universal must/shall policy applies |
| procedure segmentation | `SLE-RULE-0016`, `SLE-RULE-0017` | condition and action boundaries require workflow interpretation |
| provenance prompts | `SLE-RULE-0011`, `SLE-RULE-0012`, `SLE-RULE-0014`, `SLE-RULE-0024` | field completion does not verify source, judgment, or gloss correctness |
| dataset and version prompts | `SLE-RULE-0014`, `SLE-RULE-0015` | a tool cannot decide which transformations materially affect a claim |
| claim-support link checks | `SLE-RULE-0023` | link presence does not establish evidential sufficiency |
| limitation prompts | `SLE-RULE-0021`, `SLE-RULE-0022` | a tool cannot discover every sensitivity limit or counterexample |
| sentence-load heuristics | `SLE-RULE-0001` | no fixed sentence-length maximum is normative |
| evidence-word highlighting | `SLE-RULE-0019`, `SLE-RULE-0020` | no universal evidence-verb hierarchy exists |
| gloss-layout checks | `SLE-RULE-0024` | alignment checks cannot validate segmentation or gloss analysis |

## Prohibited interpretations

Automated output must not be labelled:

- full SLE conformance;
- independent meaning preservation;
- linguistic or grammaticality validation;
- theory or method approval;
- ethics approval;
- translation approval;
- accessibility certification;
- community authorization.

## Minimum disclosure

A project using optional automation should record:

- tool name and version or state;
- rules or heuristics attempted;
- input scope;
- known false-positive and false-negative risks;
- human reviewer role;
- disposition of material findings;
- confirmation that tool output did not replace [[Profiles and Conformance]], [[Human Review Boundary Register v0.1]], or the authorized-meaning process in [[SLE Semantic Equivalence Review Template v0.1]].

## Future boundary

A later software project may define executable heuristics only under separately authorized scope. Software feasibility cannot determine whether a language rule belongs in SLE.

Tool findings must remain distinct from human item outcomes, conformance results, and typed evaluation records.