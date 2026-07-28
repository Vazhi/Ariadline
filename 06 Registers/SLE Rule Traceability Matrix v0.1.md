---
title: "SLE Rule Traceability Matrix v0.1"
type: register
status: proposed
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - sle
  - traceability
  - rules
  - evaluation
---
# SLE Rule Traceability Matrix v0.1

## Purpose

This register links every proposed language rule to its controlling statement, independent rationale, checklist question, constructed test cases, internal audit prompts, and known substantive boundary.

- Controlling rules: [[SLE for Linguistics Language Rules v0.1]]
- Independent rationale: [[Independent SLE Rule Evidence Register v0.1]]
- Human checklist: [[SLE Editorial Conformance Checklist v0.1]]
- Classified cases: [[SLE Rule Test Case Catalog v0.1]]
- Internal audit corpus: [[Multi-Domain SLE Evaluation Corpus v0.1]]
- Coverage gaps: [[Evaluation Corpus Coverage Matrix v0.1]]

Corpus items are constructed audit prompts. Their controlled alternatives internally match constructed briefs, but independent preservation remains `not determined`. They are not normative evidence or verified examples of improvement.

## Rule traceability

| Rule ID | Independent rationale | Principal internal audit items | Test-case set | Boundary or gap |
|---|---|---|---|---|
| `SLE-RULE-0001` | ER-01, ER-04 | `SLE-EVAL-0002`, `SLE-EVAL-0010`, `SLE-EVAL-0013` | pass/fail/borderline/exception | review information load, not scientific correctness |
| `SLE-RULE-0002` | ER-01, ER-04 | `SLE-EVAL-0002`, `SLE-EVAL-0010`, `SLE-EVAL-0013` | pass/fail/borderline/exception | intentionally open reference may require meaning authority |
| `SLE-RULE-0003` | ER-06, ER-07, ER-08, ER-09 | `SLE-EVAL-0001`, `SLE-EVAL-0003`, `SLE-EVAL-0004`, `SLE-EVAL-0005`, `SLE-EVAL-0007`, `SLE-EVAL-0009`, `SLE-EVAL-0011` | pass/fail/borderline/exception | do not judge sampling adequacy |
| `SLE-RULE-0004` | ER-01, ER-04, ER-08 | `SLE-EVAL-0002`, `SLE-EVAL-0005`, `SLE-EVAL-0008`, `SLE-EVAL-0010`, `SLE-EVAL-0013`, `SLE-EVAL-0014`, `SLE-EVAL-0016` | pass/fail/borderline/exception | terminology choice remains theory- and community-sensitive |
| `SLE-RULE-0005` | ER-01, ER-04, ER-08 | `SLE-EVAL-0002`, `SLE-EVAL-0005`, `SLE-EVAL-0008`, `SLE-EVAL-0010`, `SLE-EVAL-0013`, `SLE-EVAL-0014`, `SLE-EVAL-0016` | pass/fail/borderline/exception | do not certify theoretical correctness |
| `SLE-RULE-0006` | ER-06, ER-07 | `SLE-EVAL-0003`, `SLE-EVAL-0004`, `SLE-EVAL-0005`, `SLE-EVAL-0007`, `SLE-EVAL-0011`, `SLE-EVAL-0014` | pass/fail/borderline/exception | do not validate metric choice |
| `SLE-RULE-0007` | ER-01, ER-04 | `SLE-EVAL-0002`, `SLE-EVAL-0003`, `SLE-EVAL-0007`, `SLE-EVAL-0010`, `SLE-EVAL-0013` | pass/fail/borderline/exception | formal analysis remains substantive |
| `SLE-RULE-0008` | ER-01, ER-03, ER-11 | `SLE-EVAL-0010`, `SLE-EVAL-0014`; supplementary `SLE-EVAL-CS-0002` | pass/fail/borderline/exception | no universal must-versus-shall rule |
| `SLE-RULE-0009` | ER-06, ER-07, ER-08 | `SLE-EVAL-0001`, `SLE-EVAL-0005`, `SLE-EVAL-0008` | pass/fail/borderline/exception | stronger claims require separate support |
| `SLE-RULE-0010` | ER-06, ER-07 | `SLE-EVAL-0006`, `SLE-EVAL-0007` | pass/fail/borderline/exception | do not infer grammaticality from responses |
| `SLE-RULE-0011` | ER-02, ER-04, ER-05 | `SLE-EVAL-0006`, `SLE-EVAL-0008`, `SLE-EVAL-0009`, `SLE-EVAL-0012`, `SLE-EVAL-0015` | pass/fail/borderline/exception | provenance model remains proposed |
| `SLE-RULE-0012` | ER-02, ER-04 | `SLE-EVAL-0002`, `SLE-EVAL-0006`, `SLE-EVAL-0007` | pass/fail/borderline/exception | symbol assignment is not validated |
| `SLE-RULE-0013` | ER-01, ER-05, ER-08 | `SLE-EVAL-0006`, `SLE-EVAL-0008`, `SLE-EVAL-0009`, `SLE-EVAL-0012`, `SLE-EVAL-0015` | pass/fail/borderline/exception | one-time adjacent references may be exempt |
| `SLE-RULE-0014` | ER-06, ER-08, ER-09, ER-10 | `SLE-EVAL-0004`, `SLE-EVAL-0008`, `SLE-EVAL-0011`, `SLE-EVAL-0012` | pass/fail/borderline/exception | do not approve preprocessing choices |
| `SLE-RULE-0015` | ER-06, ER-07, ER-08, ER-10 | `SLE-EVAL-0011`; supplementary `SLE-EVAL-CS-0002` | pass/fail/borderline/exception | system and linguistic correctness require separate review |
| `SLE-RULE-0016` | ER-01, ER-06 | `SLE-EVAL-0010`, `SLE-EVAL-0014`; supplementary `SLE-EVAL-CS-0002` | pass/fail/borderline/exception | do not validate the condition itself |
| `SLE-RULE-0017` | ER-01, ER-06, ER-10 | `SLE-EVAL-0010`, `SLE-EVAL-0014`; supplementary `SLE-EVAL-CS-0002` | pass/fail/borderline/exception | inseparable operations may be exceptions |
| `SLE-RULE-0018` | ER-03, ER-06, ER-07 | `SLE-EVAL-0016` and corpus-wide restrictions | pass/fail/borderline/exception | core truth-versus-conformance boundary |
| `SLE-RULE-0019` | ER-06, ER-07, ER-10 | `SLE-EVAL-0001`–`SLE-EVAL-0009`, `SLE-EVAL-0011`, `SLE-EVAL-0015` | pass/fail/borderline/exception | interpretation correctness remains substantive |
| `SLE-RULE-0020` | ER-07 | `SLE-EVAL-0001`–`SLE-EVAL-0005`, `SLE-EVAL-0007`–`SLE-EVAL-0009`, `SLE-EVAL-0011`, `SLE-EVAL-0015` | pass/fail/borderline/exception | no universal evidence-verb hierarchy |
| `SLE-RULE-0021` | ER-06, ER-07, ER-10 | `SLE-EVAL-0001`, `SLE-EVAL-0009`, `SLE-EVAL-0012` | pass/fail/borderline/exception | do not certify nonexistence |
| `SLE-RULE-0022` | ER-07 | all research and resource audit items | pass/fail/borderline/exception | do not discover every possible limitation |
| `SLE-RULE-0023` | ER-05, ER-06, ER-07 | all research audit items | pass/fail/borderline/exception | link presence does not establish sufficiency |
| `SLE-RULE-0024` | ER-02 | no direct independent audit item | pass/fail/borderline/exception only | authentic independently reviewed gloss blocks remain required |

## Interpretation

- **Independent rationale** refers to source analysis recorded before this checklist.
- **Internal audit items** show where a constructed brief exercises a rule; they have no independent preservation confirmation.
- **Test-case set** means four constructed classifications exist, not that human reviewers agree.
- A gap prevents stabilization but does not prevent proposed editorial support.
- Broad mappings may reflect rule-selection bias because the audit corpus was built around the current rules.

## Canto-span supplement

[[Canto-span Evaluation Subset v0.1]] supplies only supplementary project-local cases. Neither item satisfies independent rationale, coverage, or stabilization requirements.

## Change rule

When a controlling rule changes:

1. update the checklist item;
2. update all four classified cases;
3. update this matrix;
4. reassess affected meaning briefs and audit items;
5. preserve prior results under their original rule version;
6. classify compatibility under [[Versioning and Release Model]].