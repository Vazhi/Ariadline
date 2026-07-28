---
title: "Canto-span Evaluation Subset v0.1"
type: evaluation-subset
status: non-normative
normative_status: non-normative
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - sle
  - validation
  - canto-span
  - stress-test
  - non-normative
---
# Canto-span Evaluation Subset v0.1

## Authority warning

This subset is a non-authoritative stress test for [[Multi-Domain SLE Evaluation Corpus v0.1]].

Canto-span does not define SLE rules, document patterns, profiles, conformance results, evaluation methods, or terminology. The subset cannot supply normative justification. It contains 2 of the 18 v0.1 corpus items.

The source vocabulary fixture is [[Canto-span Pilot Termbase v0.1]]. That fixture is also non-normative. These passages are project-constructed test items rather than copied Canto-span documentation.

## Stable provenance

- SLE repository baseline: merge commit `4334ef9a8afb1ec0e995145865afa38292ba9bf2`
- Canto-span fixture role: bounded vocabulary and documentation stress test
- External Canto-span repository authority: none for SLE design
- Item source class: constructed from documented Canto-span-local distinctions
- Semantic-equivalence template: [[SLE Semantic Equivalence Review Template v0.1]]

# SLE-EVAL-CS-0001 — Status label is not a truth judgment

- **Domain:** grammar-engineering documentation
- **Method:** status and limitation record
- **Theory or framework:** project-local
- **Language context:** Cantonese-oriented Canto-span documentation
- **Genre:** limitation and open-question record
- **Pattern:** `SLE-PATTERN-0013`
- **Rules tested:** `SLE-RULE-0003`, `0004`, `0005`, `0018`, `0019`, `0020`, `0022`, `0023`

## Uncontrolled passage

> This construction is unsupported, so it is wrong and should be removed.

## Proposed controlled alternative

> In the fictional frozen Canto-span record, the note has status `unsupported_generalization`. The status records that the current generalization lacks the required support. It does not establish that the construction is impossible or that every descriptive example must be removed. The next review must identify the unsupported claim, retained observations, and evidence needed for a narrower or revised analysis.

## Change record

- status name, controlled meaning, and affected claim are separated;
- *wrong* is removed because the status does not license that conclusion;
- removal becomes one possible future decision rather than an automatic action;
- required resolution evidence is stated.

## Semantic-equivalence review

- **Result:** provisionally equivalent to the intended project-status record, not to the literal claim that the construction is false;
- **Preserved:** current generalization lacks required support;
- **Risk:** the exact operational meaning of `unsupported_generalization` remains Canto-span-local and must not become a core SLE status.

# SLE-EVAL-CS-0002 — Parser output is not linguistic support

- **Domain:** annotation and parser documentation
- **Method:** parser-assisted review procedure
- **Theory or framework:** project-local grammar engineering
- **Language context:** Cantonese-oriented Canto-span documentation
- **Genre:** annotation guideline and procedure
- **Patterns:** `SLE-PATTERN-0007`, `SLE-PATTERN-0011`
- **Rules tested:** `SLE-RULE-0003`, `0005`, `0008`, `0015`, `0016`, `0017`, `0018`, `0019`, `0020`, `0022`, `0023`

## Uncontrolled passage

> If the parser labels the sentence `A_NOT_A`, mark the grammar note supported and update everything.

## Proposed controlled alternative

> If Parser P at the frozen test state labels the input `A_NOT_A`, record the parser result in the test record. Do not change the grammar note's evidence status from parser output alone. A reviewer must separately compare the input, parser configuration, linguistic definition, examples, counterexamples, and independent sources. Update only the records affected by the documented review decision.

## Change record

- condition, parser identity, action, and review boundary are separated;
- parser output is distinguished from linguistic support;
- *update everything* becomes a bounded record update;
- the required human evidence review is stated.

## Semantic-equivalence review

- **Result:** provisionally equivalent to the intended safe parser-assisted workflow, not to the literal automatic-support rule;
- **Preserved:** parser output triggers a review record;
- **Risk:** the procedure is Canto-span-specific and cannot become a universal SLE workflow requirement.

# Subset restrictions

- Keep these IDs under the `SLE-EVAL-CS-*` namespace.
- Do not combine their counts with independent-source coverage without showing the source class.
- Do not use the subset to satisfy an independent theory, language, method, or genre requirement.
- Do not generalize Canto-span statuses or parser workflows into SLE.
- Retain failed or disputed rewrites as Canto-span adoption findings, not as defects in SLE unless independent multi-domain evidence supports the same problem.

# Relationship to coverage

The subset contributes a project-local limitation record and parser-assisted procedure test. [[Evaluation Corpus Coverage Matrix v0.1]] treats both as one bounded source project and preserves the requirement for an independent non-Canto-span limitation-record item.