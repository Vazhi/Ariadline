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

This is a bounded non-authoritative stress test for [[Multi-Domain SLE Evaluation Corpus v0.1]].

Canto-span does not define SLE rules, patterns, profiles, conformance, evaluation methods, or terminology. These are project-constructed test passages, not copied Canto-span source prose. They cannot satisfy independent domain, theory, language, method, or genre coverage.

- SLE baseline: merge commit `4334ef9a8afb1ec0e995145865afa38292ba9bf2`
- Source fixture: [[Canto-span Pilot Termbase v0.1]]
- Review template: [[SLE Semantic Equivalence Review Template v0.1]]

## SLE-EVAL-CS-0001 — Status label is not a truth judgment

- **Meaning brief:** `SLE-BRIEF-CS-0001`
- **Brief authority:** project-constructed evaluation specification; no external source-author authority
- **Provenance:** project-constructed fictional editorial test item
- **Domain:** grammar-engineering documentation
- **Method:** status and limitation record
- **Illustrative context:** Canto-span documentation
- **Framework prompt:** project-local
- **Genre:** limitation record
- **Pattern:** `SLE-PATTERN-0013`
- **Rules tested:** `SLE-RULE-0003`, `SLE-RULE-0004`, `SLE-RULE-0005`, `SLE-RULE-0018`, `SLE-RULE-0019`, `SLE-RULE-0020`, `SLE-RULE-0022`, `SLE-RULE-0023`

### Authorized meaning brief

> In the fictional frozen Canto-span record, unsupported_generalization means the current generalization lacks the required support. It does not mean the construction is impossible or that all examples must be removed. Review must separate unsupported claims, retained observations, and missing evidence.

### Uncontrolled draft

> This construction is unsupported, so it is wrong and should be removed.

### Proposed controlled alternative

> In the fictional frozen Canto-span record, the note has status unsupported_generalization. The status records that the current generalization lacks the required support. It does not establish that the construction is impossible or that every descriptive example must be removed. The next review must identify the unsupported claim, retained observations, and evidence needed for a narrower or revised analysis.

### Pair audit

- **Length:** 12 → 58 words (+46); 1 → 4 sentences (+3)
- **Structure and terminology:** Defines the local status, removes wrong, bounds removal, and states the review task.
- **Uncontrolled-to-brief result:** does not match brief
- **Controlled-to-brief internal result:** matches brief
- **Literal passage-to-passage equivalence:** not equivalent by design when the uncontrolled draft overstates or obscures the authorized brief
- **Independent preservation result:** not determined
- **Risk:** The status meaning remains Canto-span-local and non-normative.

## SLE-EVAL-CS-0002 — Parser output is not linguistic support

- **Meaning brief:** `SLE-BRIEF-CS-0002`
- **Brief authority:** project-constructed evaluation specification; no external source-author authority
- **Provenance:** project-constructed fictional editorial test item
- **Domain:** annotation and parser documentation
- **Method:** parser-assisted review procedure
- **Illustrative context:** Canto-span documentation
- **Framework prompt:** project-local grammar engineering
- **Genre:** annotation guideline and procedure
- **Patterns:** `SLE-PATTERN-0007`, `SLE-PATTERN-0011`
- **Rules tested:** `SLE-RULE-0003`, `SLE-RULE-0005`, `SLE-RULE-0008`, `SLE-RULE-0015`, `SLE-RULE-0016`, `SLE-RULE-0017`, `SLE-RULE-0018`, `SLE-RULE-0019`, `SLE-RULE-0020`, `SLE-RULE-0022`, `SLE-RULE-0023`

### Authorized meaning brief

> Parser P at a frozen test state can trigger a review record. Parser output alone cannot change a grammar note's evidence status. A human reviewer must compare the input, configuration, definition, examples, counterexamples, and independent sources. Only affected records may change.

### Uncontrolled draft

> If the parser labels the sentence A_NOT_A, mark the grammar note supported and update everything.

### Proposed controlled alternative

> If Parser P at the frozen test state labels the input A_NOT_A, record the parser result in the test record. Do not change the grammar note's evidence status from parser output alone. A reviewer must separately compare the input, parser configuration, linguistic definition, examples, counterexamples, and independent sources. Update only the records affected by the documented review decision.

### Pair audit

- **Length:** 15 → 58 words (+43); 1 → 4 sentences (+3)
- **Structure and terminology:** Separates trigger, system record, evidence boundary, human review, and bounded update.
- **Uncontrolled-to-brief result:** does not match brief
- **Controlled-to-brief internal result:** matches brief
- **Literal passage-to-passage equivalence:** not equivalent by design when the uncontrolled draft overstates or obscures the authorized brief
- **Independent preservation result:** not determined
- **Risk:** The workflow remains Canto-span-specific and cannot define SLE.

# Subset restrictions

- Keep the IDs under `SLE-EVAL-CS-*`.
- Keep the briefs under `SLE-BRIEF-CS-*`.
- Do not combine this subset with independent-source coverage without showing the source class.
- Do not generalize Canto-span statuses or workflows into SLE.
- Treat failed or disputed rewrites as adoption findings unless independent multi-domain evidence supports the same issue.
- Independent preservation remains `not determined` for both items.

[[Evaluation Corpus Coverage Matrix v0.1]] records the subset as one bounded source project.
