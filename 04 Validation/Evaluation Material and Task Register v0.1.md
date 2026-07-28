---
title: "Evaluation Material and Task Register v0.1"
type: evaluation-register
status: preparation
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - sle
  - evaluation
  - materials
  - tasks
---
# Evaluation Material and Task Register v0.1

## Purpose

This register controls which materials may enter the human study defined in [[Multi-Domain Reader and Author Evaluation Protocol v0.1]].

A registered item is not automatically valid for confirmatory analysis. The item must pass its authorization, preservation, permission, and scoring gates.

## Material classes

### `SYN` — constructed procedure-pilot material

Source: [[Multi-Domain SLE Evaluation Corpus v0.1]].

Permitted use:

- instruction testing;
- timing and interface piloting;
- scoring-key testing;
- reviewer-training exercises;
- detecting rule and task failures.

Prohibited use:

- authentic effectiveness claims;
- source-author preservation claims;
- multilingual representation claims;
- stabilization decisions by itself.

### `AUTH` — authentic authorized material

Required properties:

- independent source or contributor;
- exact passage and version identity;
- permission and access status;
- authorized meaning record;
- independently reviewed condition variants;
- source-domain, theory, method, language, and genre metadata.

Only valid `AUTH` items may support the main publication decision.

### `TRANS` — non-English-original and translation material

Required properties:

- source-language original;
- source authority;
- translation direction;
- translator role;
- bilingual or multilingual review;
- normative-function and terminology review;
- rhetorical-order notes.

### `FULL` — full-section or full-document material

Required properties:

- identifiable document scope;
- multiple interacting claims or instructions;
- at least two applicable document patterns or a justified single-pattern full section;
- authorized meaning and structure record;
- permission for participant use.

### `CS` — Canto-span supplementary material

Source: [[Canto-span Evaluation Subset v0.1]].

The class is reported separately and cannot satisfy independent coverage.

## Condition fields

Every comparison record must include:

- material ID;
- class;
- immutable source or version reference;
- authorized meaning record ID;
- condition `U`, `P`, or `S`;
- condition author and role;
- independent preservation result;
- condition word and sentence count;
- condition-specific notes;
- scoring-key version;
- permission and access state;
- inclusion state.

## Current constructed pilot blocks

The following blocks are available only for procedure piloting. Item meaning and restrictions remain controlled by the four corpus-part notes.

### Block SYN-R1 — claim, scope, and evidence reconstruction

- `SLE-EVAL-0001` — bounded corpus observation;
- `SLE-EVAL-0002` — competing analyses;
- `SLE-EVAL-0003` — interactional function and distribution;
- `SLE-EVAL-0004` — corpus-group comparison;
- `SLE-EVAL-0005` — typological comparison boundary;
- `SLE-EVAL-0007` — judgment-task distribution;
- `SLE-EVAL-0011` — computational model claim;
- `SLE-EVAL-0015` — sequential-analysis claim.

Tasks:

- identify principal claim;
- identify direct record;
- identify inference;
- reconstruct scope;
- identify unsupported inference;
- identify limitation or competing analysis;
- rate confidence.

### Block SYN-R2 — data, example, resource, and provenance interpretation

- `SLE-EVAL-0006` — participant translation and analyst gloss;
- `SLE-EVAL-0008` — lexicographic usage label;
- `SLE-EVAL-0009` — signed-language resource access;
- `SLE-EVAL-0012` — resource release scope.

Tasks:

- identify source, collection, modification, and production status;
- distinguish participant wording from analyst analysis;
- identify access and coverage limits;
- identify dataset or release state;
- detect overgeneralization.

### Block SYN-P1 — procedure and annotation use

- `SLE-EVAL-0010` — annotation decision procedure;
- `SLE-EVAL-0014` — phonetic measurement procedure.

Tasks:

- apply conditions and actions to fictional records;
- record uncertainty;
- choose escalation or abstention;
- identify normative force;
- measure action accuracy and time.

### Block SYN-A1 — terminology and learner-facing authoring

- `SLE-EVAL-0013` — learner-facing explanation;
- `SLE-EVAL-0016` — collaborative terminology decision.

Tasks:

- revise against the authorized brief;
- identify concept and term boundaries;
- preserve theory and scope boundaries;
- report burden, cohesion, and naturalness.

### Block CS-S1 — bounded Canto-span arm

- `SLE-EVAL-CS-0001`;
- `SLE-EVAL-CS-0002`.

This block must be labelled project-local, capped in participant exposure, and reported separately.

## Missing confirmatory material sets

The following IDs are reserved but not populated:

- `AUTH-DESC-0001`–`AUTH-DESC-0004` — descriptive, documentary, or field materials;
- `AUTH-THEORY-0001`–`AUTH-THEORY-0004` — at least two theoretical traditions;
- `AUTH-EMP-0001`–`AUTH-EMP-0004` — corpus, experimental, phonetic, sociolinguistic, or discourse materials;
- `AUTH-COMP-0001`–`AUTH-COMP-0004` — computational or language-resource materials;
- `AUTH-EDIT-0001`–`AUTH-EDIT-0004` — editorial, review, annotation, or teaching materials;
- `TRANS-0001`–`TRANS-0006` — at least two source languages and two directions where feasible;
- `FULL-0001`–`FULL-0004` — full-section or combined-pattern materials;
- `GLOSS-0001`–`GLOSS-0004` — authentic independently reviewed interlinear-glossing blocks.

Reserved IDs do not indicate that material has been obtained.

## Main-study minimum coverage

Before launch, the confirmatory register must contain at least:

- 12 valid `AUTH` meaning records;
- 2 or more records in each of four broad domain families;
- 2 or more theoretical or analytical traditions;
- 3 or more methods;
- 5 or more document genres;
- 2 or more non-English-original `TRANS` records;
- 2 or more `FULL` records;
- 2 or more authentic `GLOSS` records;
- ordinary expert-edited `P` conditions for every confirmatory meaning record;
- no source contributing more than 20% of confirmatory trials;
- no Canto-span material contributing more than 10% of any pooled trial set.

These are minimum diversity gates, not evidence that the final sample represents linguistics as a whole.

## Scoring-key requirements

Each scored question must identify:

- the authorized answer or answer set;
- acceptable paraphrases or multiple selections;
- material-error and minor-error boundaries;
- `not determined` conditions;
- scorer training example;
- adjudication route;
- whether scoring can be performed without knowing condition identity.

Open responses should be scored by at least two trained reviewers who are masked to condition where feasible.

## Material lifecycle

Use these states:

- `candidate`;
- `permission_pending`;
- `meaning_pending`;
- `condition_drafting`;
- `independent_review`;
- `pilot_ready`;
- `confirmatory_ready`;
- `excluded`;
- `retired`.

A material can become `confirmatory_ready` only after all three conditions and the scoring key pass independent review.

## Change control

After the main-study freeze:

- do not edit a stimulus silently;
- assign a new material version for any change;
- remove an invalid item under the preregistered exclusion rule;
- report the item, reason, timing, and affected analyses;
- do not replace an excluded item after viewing its condition effect.
