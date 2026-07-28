---
title: "Ariadline Rule Traceability Matrix v0.1"
type: register
status: proposed
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - ariadline
  - traceability
  - rules
  - evaluation
---
# Ariadline Rule Traceability Matrix v0.1

## Purpose

This register links every proposed language rule to its controlling statement, independent rationale, checklist question, constructed test cases, internal audit prompts, and known substantive boundary.

- Controlling rules: [[Ariadline Language Rules v0.1]]
- Independent rationale: [[Independent Ariadline Rule Evidence Register v0.1]]
- Human checklist: [[Ariadline Editorial Conformance Checklist v0.1]]
- Classified cases: [[Ariadline Rule Test Case Catalog v0.1]]
- Internal audit corpus: [[Multi-Domain Ariadline Evaluation Corpus v0.1]]
- Coverage gaps: [[Evaluation Corpus Coverage Matrix v0.1]]

Corpus items are constructed audit prompts. Their controlled alternatives internally match constructed briefs, but independent preservation remains `not determined`. They are not normative evidence or verified examples of improvement.

## Mapping method

The non-Canto-span item column is an exact reverse index of the `Rules tested` fields in the four merged corpus-part notes. An item appears only when its own record names the full rule ID.

Canto-span prompts are listed separately so they cannot be mistaken for independent coverage. Every rule also has one pass, one fail, one provisional borderline, and one typed boundary prompt in the test-case catalog.

## Rule traceability

| Rule ID | Independent rationale | Exact non-Canto-span audit items | Supplementary Canto-span prompts | Boundary or gap |
|---|---|---|---|---|
| `SLE-RULE-0001` | ER-01, ER-04 | `SLE-EVAL-0002`, `SLE-EVAL-0010`, `SLE-EVAL-0013` | none | review information load, not scientific correctness |
| `SLE-RULE-0002` | ER-01, ER-04 | `SLE-EVAL-0013` | none | intentionally open reference may require meaning authority |
| `SLE-RULE-0003` | ER-06, ER-07, ER-08, ER-09 | `SLE-EVAL-0001`, `SLE-EVAL-0003`, `SLE-EVAL-0004`, `SLE-EVAL-0005`, `SLE-EVAL-0006`, `SLE-EVAL-0007`, `SLE-EVAL-0008`, `SLE-EVAL-0009`, `SLE-EVAL-0011`, `SLE-EVAL-0012`, `SLE-EVAL-0015` | `SLE-EVAL-CS-0001`, `SLE-EVAL-CS-0002` | do not judge sampling adequacy |
| `SLE-RULE-0004` | ER-01, ER-04, ER-08 | `SLE-EVAL-0005`, `SLE-EVAL-0008`, `SLE-EVAL-0010`, `SLE-EVAL-0012`, `SLE-EVAL-0013`, `SLE-EVAL-0014`, `SLE-EVAL-0016` | `SLE-EVAL-CS-0001` | terminology choice remains theory- and community-sensitive |
| `SLE-RULE-0005` | ER-01, ER-04, ER-08 | `SLE-EVAL-0002`, `SLE-EVAL-0005`, `SLE-EVAL-0008`, `SLE-EVAL-0010`, `SLE-EVAL-0013`, `SLE-EVAL-0014`, `SLE-EVAL-0016` | `SLE-EVAL-CS-0001`, `SLE-EVAL-CS-0002` | do not certify theoretical correctness |
| `SLE-RULE-0006` | ER-06, ER-07 | `SLE-EVAL-0003`, `SLE-EVAL-0004`, `SLE-EVAL-0005`, `SLE-EVAL-0007`, `SLE-EVAL-0011` | none | do not validate metric choice |
| `SLE-RULE-0007` | ER-01, ER-04 | `SLE-EVAL-0010`, `SLE-EVAL-0013` | none | formal analysis remains substantive |
| `SLE-RULE-0008` | ER-01, ER-03, ER-11 | `SLE-EVAL-0010`, `SLE-EVAL-0014`, `SLE-EVAL-0016` | `SLE-EVAL-CS-0002` | no universal must-versus-shall rule |
| `SLE-RULE-0009` | ER-06, ER-07, ER-08 | `SLE-EVAL-0001` | none | stronger claims require separate support |
| `SLE-RULE-0010` | ER-06, ER-07 | `SLE-EVAL-0006`, `SLE-EVAL-0007` | none | do not infer grammaticality from responses |
| `SLE-RULE-0011` | ER-02, ER-04, ER-05 | `SLE-EVAL-0006`, `SLE-EVAL-0008`, `SLE-EVAL-0009`, `SLE-EVAL-0015` | none | provenance model remains proposed |
| `SLE-RULE-0012` | ER-02, ER-04 | `SLE-EVAL-0006`, `SLE-EVAL-0007`, `SLE-EVAL-0010` | none | symbol assignment is not validated |
| `SLE-RULE-0013` | ER-01, ER-05, ER-08 | `SLE-EVAL-0006`, `SLE-EVAL-0008`, `SLE-EVAL-0009`, `SLE-EVAL-0010`, `SLE-EVAL-0012`, `SLE-EVAL-0014`, `SLE-EVAL-0015` | none | one-time adjacent references are outside the repeated-reference trigger |
| `SLE-RULE-0014` | ER-06, ER-08, ER-09, ER-10 | `SLE-EVAL-0004`, `SLE-EVAL-0008`, `SLE-EVAL-0009`, `SLE-EVAL-0011`, `SLE-EVAL-0012` | none | do not approve preprocessing choices |
| `SLE-RULE-0015` | ER-06, ER-07, ER-08, ER-10 | `SLE-EVAL-0011` | `SLE-EVAL-CS-0002` | system and linguistic correctness require separate review |
| `SLE-RULE-0016` | ER-01, ER-06 | `SLE-EVAL-0010`, `SLE-EVAL-0014` | `SLE-EVAL-CS-0002` | do not validate the condition itself |
| `SLE-RULE-0017` | ER-01, ER-06, ER-10 | `SLE-EVAL-0010`, `SLE-EVAL-0014` | `SLE-EVAL-CS-0002` | inseparable operations are a recommendation boundary |
| `SLE-RULE-0018` | ER-03, ER-06, ER-07 | `SLE-EVAL-0016` | `SLE-EVAL-CS-0001`, `SLE-EVAL-CS-0002` | core truth-versus-conformance boundary |
| `SLE-RULE-0019` | ER-06, ER-07, ER-10 | `SLE-EVAL-0001`, `SLE-EVAL-0002`, `SLE-EVAL-0003`, `SLE-EVAL-0004`, `SLE-EVAL-0005`, `SLE-EVAL-0006`, `SLE-EVAL-0007`, `SLE-EVAL-0008`, `SLE-EVAL-0009`, `SLE-EVAL-0011`, `SLE-EVAL-0015` | `SLE-EVAL-CS-0001`, `SLE-EVAL-CS-0002` | interpretation correctness remains substantive |
| `SLE-RULE-0020` | ER-07 | `SLE-EVAL-0001`, `SLE-EVAL-0002`, `SLE-EVAL-0003`, `SLE-EVAL-0004`, `SLE-EVAL-0005`, `SLE-EVAL-0007`, `SLE-EVAL-0008`, `SLE-EVAL-0011`, `SLE-EVAL-0015` | `SLE-EVAL-CS-0001`, `SLE-EVAL-CS-0002` | no universal evidence-verb hierarchy |
| `SLE-RULE-0021` | ER-06, ER-07, ER-10 | `SLE-EVAL-0001`, `SLE-EVAL-0012` | none | do not certify nonexistence |
| `SLE-RULE-0022` | ER-07 | `SLE-EVAL-0001` through `SLE-EVAL-0016` | `SLE-EVAL-CS-0001`, `SLE-EVAL-CS-0002` | do not assume every possible limitation was discovered |
| `SLE-RULE-0023` | ER-05, ER-06, ER-07 | `SLE-EVAL-0001`–`SLE-EVAL-0009`, `SLE-EVAL-0011`, `SLE-EVAL-0012`, `SLE-EVAL-0015`, `SLE-EVAL-0016` | `SLE-EVAL-CS-0001`, `SLE-EVAL-CS-0002` | link presence does not establish sufficiency |
| `SLE-RULE-0024` | ER-02 | none | none | authentic independently reviewed gloss blocks remain required |

## Interpretation

- **Independent rationale** refers to source analysis recorded before this checklist.
- **Exact non-Canto-span audit items** show where a constructed brief explicitly names a rule; they have no independent preservation confirmation.
- **Supplementary Canto-span prompts** are project-local stress tests and cannot satisfy independent rationale or coverage.
- **Test-case catalog coverage** means four constructed prompts exist for each rule; the fourth is a typed boundary case and is not necessarily an exception.
- A gap prevents stabilization but does not prevent proposed editorial support.
- Broad mappings may reflect rule-selection bias because the audit corpus was built around the current rules.

## Change rule

When a controlling rule or corpus `Rules tested` field changes:

1. update the checklist item;
2. update the four classified prompts;
3. regenerate this exact reverse index;
4. reassess affected meaning briefs and audit items;
5. preserve prior results under their original rule version;
6. classify compatibility under [[Versioning and Release Model]].