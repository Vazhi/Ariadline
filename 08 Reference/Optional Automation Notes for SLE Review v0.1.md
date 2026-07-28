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

A tool may flag text for human review. It must not create a conformance result, determine linguistic truth, or replace semantic-equivalence review.

## Possible assistance classes

| Assistance class | Potentially useful rule areas | Required warning |
|---|---|---|
| terminology search | SLE-RULE-0004, 0005 | synonym and definition findings require human concept review |
| reference highlighting | SLE-RULE-0002, 0013 | a tool cannot reliably determine intended antecedent in all linguistic prose |
| comparison-field prompts | SLE-RULE-0006 | a detected comparative does not establish which measure the author intended |
| normative-verb inventory | SLE-RULE-0008 | the declared verbal-form system controls; no universal must/shall policy is assumed |
| procedure segmentation | SLE-RULE-0016, 0017 | condition and action boundaries require human workflow interpretation |
| provenance-field prompts | SLE-RULE-0011, 0012, 0014, 0024 | tool completion does not verify source truth, judgment validity, or gloss correctness |
| dataset/version prompts | SLE-RULE-0014, 0015 | a tool cannot determine which transformation details materially affect a claim |
| claim-support link checks | SLE-RULE-0023 | link presence does not establish evidential sufficiency |
| limitation prompts | SLE-RULE-0021, 0022 | a tool cannot discover every relevant sensitivity limit or counterexample |
| sentence-load heuristics | SLE-RULE-0001 | no fixed maximum sentence length is normative |
| evidence-word highlighting | SLE-RULE-0019, 0020 | SLE defines no universal evidence-verb hierarchy |
| gloss-layout checks | SLE-RULE-0024 | alignment checks cannot validate linguistic segmentation or gloss analysis |

## Prohibited interpretations

An automated output must not be labelled:

- full SLE conformance;
- linguistic validation;
- grammaticality approval;
- theory approval;
- method approval;
- ethics approval;
- translation approval;
- accessibility certification;
- community authorization.

## Minimum tool disclosure

A project that uses optional automation should record:

- tool name and version or state;
- rules or heuristics attempted;
- input scope;
- known false-positive and false-negative risks;
- human reviewer role;
- disposition of every material finding;
- confirmation that tool output did not replace the result model in [[Profiles and Conformance]].

## Future authorization boundary

A later software project may define executable heuristics only under a separately authorized scope. Software feasibility cannot determine whether a language rule belongs in SLE.

Findings from optional tools must remain distinct from human-review results in [[Human Review Boundary Register v0.1]].
