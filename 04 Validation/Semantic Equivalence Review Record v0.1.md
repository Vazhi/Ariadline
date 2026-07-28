---
title: "Semantic Equivalence Review Record v0.1"
type: validation-register
status: provisional
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - sle
  - validation
  - semantic-equivalence
  - review-record
---
# Semantic Equivalence Review Record v0.1

## Purpose

This register records the first meaning-preservation review for [[Multi-Domain SLE Evaluation Corpus v0.1]] and [[Canto-span Evaluation Subset v0.1]].

The checks use [[SLE Semantic Equivalence Review Template v0.1]]. They are project-internal pre-reviews, not independent domain or author approvals.

## Review rule

A controlled alternative may enter reader or author evaluation only when:

- its intended claim is defined by an item brief or authorized source record;
- every added detail is licensed by that record;
- polarity, scope, quantification, evidential force, certainty, theory, method, data status, and limitations are preserved or explicitly marked as changed;
- the result is `provisionally equivalent` or `equivalent with recorded uncertainty`;
- any `not equivalent` alternative is rejected rather than silently repaired in the result record.

## Item-level record

| Item | Initial result | Principal preserved content | Principal risk or unresolved review |
|---|---|---|---|
| SLE-EVAL-0001 | provisionally equivalent | all fictional sample tokens contain the classifier | not equivalent to a literal universal grammatical claim |
| SLE-EVAL-0002 | equivalent with recorded uncertainty | Analysis A derives the reading | independent premises might exclude Analysis B |
| SLE-EVAL-0003 | provisionally equivalent | disagreement is recurrent in the fictional sample | count summary may underrepresent sequential context |
| SLE-EVAL-0004 | provisionally equivalent | younger fictional sample has the higher observed proportion | no statistical uncertainty is available |
| SLE-EVAL-0005 | provisionally equivalent | selected examples share object-before-verb order | conventional `SOV` terminology may be useful and should not be banned |
| SLE-EVAL-0006 | equivalent with recorded uncertainty | participant supplied the translation “carry” | analyst gloss is more specific and remains tentative |
| SLE-EVAL-0007 | provisionally equivalent | most eligible participants gave low ratings | task result does not establish unrestricted speaker rejection |
| SLE-EVAL-0008 | equivalent with recorded uncertainty | fictional sense and local informal label are retained | named Māori form is fictional and cannot be treated as evidence |
| SLE-EVAL-0009 | provisionally equivalent | resource coverage and partial public access are retained | access permission and ethical reuse remain distinct |
| SLE-EVAL-0010 | provisionally equivalent | inspect context, mark uncertainty, escalate material cases | fixed context window is local, not a universal rule |
| SLE-EVAL-0011 | equivalent with recorded uncertainty | fictional 93% model result is retained | cognitive interpretation requires an explicit theory, not automatic deletion |
| SLE-EVAL-0012 | provisionally equivalent | corrections and coverage expansion are retained | compatibility effects may require a separate migration record |
| SLE-EVAL-0013 | equivalent with recorded uncertainty | topic and contrast functions remain | simplified explanation may not fit advanced or competing analyses |
| SLE-EVAL-0014 | provisionally equivalent | burst-to-voicing measurement workflow remains | field-specific landmark problems are not resolved |
| SLE-EVAL-0015 | equivalent with recorded uncertainty | analyst identifies interactional resistance or trouble | *interactional trouble* may be weaker than explicit disagreement |
| SLE-EVAL-0016 | equivalent with recorded uncertainty | preferred project term is retained for one defined concept | *construction* may still imply theoretical commitment |
| SLE-EVAL-CS-0001 | provisionally equivalent | current generalization lacks required project support | Canto-span status meaning is local and non-normative |
| SLE-EVAL-CS-0002 | provisionally equivalent | parser output triggers a review record | workflow is Canto-span-specific and cannot define SLE |

## Summary

- provisionally equivalent: 11 items;
- equivalent with recorded uncertainty: 7 items;
- not equivalent: 0 accepted alternatives;
- not determined: 0 at internal pre-review;
- independently reviewed: 0;
- source-author confirmed: 0, because all v0.1 passages are constructed.

The absence of rejected alternatives is a selection-bias risk. Corpus v0.2 must retain failed and disputed rewrites rather than publishing only successful pairs.

## Structural-change review

Common changes across the corpus include:

- splitting one sentence into two or three;
- adding dataset, population, version, task, or method scope from the item brief;
- replacing categorical evidence verbs with explicit evidence relations;
- separating observation, interpretation, limitation, and next action;
- replacing vague terms with defined local terms;
- changing a general or universal claim into the bounded claim stated in the brief;
- converting multi-action instructions into conditional ordered steps.

These changes are neither benefits nor failures by themselves. Later evaluation must measure interpretation, author meaning preservation, cohesion, naturalness, and burden.

## Required independent review

Before formal use, assign each item:

1. a domain or method reviewer;
2. an SLE editorial reviewer;
3. a language reviewer when the language context affects terminology or examples;
4. a translator for non-English-original or translated material;
5. a community or source-author authority when the material is community-controlled or authentic.

The independent record must state exact reviewed scope. Review of one passage must not be generalized to a full document, domain, theory, or language.

## Disagreement handling

When reviewers disagree:

- preserve both interpretations;
- identify the exact changed word, relation, or omitted assumption;
- mark the item `not determined` when no authorized resolution is available;
- reject the proposed alternative if meaning preservation cannot be shown;
- consider whether the rule should be narrowed, made optional, moved to a profile, or removed.

## Disposition

The v0.1 pairs may proceed to substantive review of corpus design. They may not yet enter effectiveness testing as independently verified equivalent pairs.