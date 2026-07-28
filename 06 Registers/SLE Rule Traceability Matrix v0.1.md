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

This register links every proposed language rule to:

- its controlling statement in [[SLE for Linguistics Language Rules v0.1]];
- independent rationale in [[Independent SLE Rule Evidence Register v0.1]];
- the human question in [[SLE Editorial Conformance Checklist v0.1]];
- cases in [[SLE Rule Test Case Catalog v0.1]];
- principal items in [[Multi-Domain SLE Evaluation Corpus v0.1]];
- known coverage gaps in [[Evaluation Corpus Coverage Matrix v0.1]].

Corpus items are test material, not normative evidence. Canto-span items are supplementary only and never supply the principal independent rationale.

## Rule traceability

| Rule ID | Rule title | Independent rationale | Principal corpus items | Direct test state | Boundary or gap |
|---|---|---|---|---|---|
| SLE-RULE-0001 | One principal message | ER-01, ER-04 | SLE-EVAL-0002, 0010, 0013 | pass/fail/borderline/exception cases | reviewer checks information load, not scientific correctness |
| SLE-RULE-0002 | Clear reference | ER-01, ER-04 | SLE-EVAL-0002, 0010, 0013 | pass/fail/borderline/exception cases | intentionally open discourse reference may require author clarification |
| SLE-RULE-0003 | Scope of generalization | ER-06, ER-07, ER-08, ER-09 | SLE-EVAL-0001, 0003, 0004, 0005, 0007, 0009, 0011 | pass/fail/borderline/exception cases | reviewer does not judge sampling adequacy |
| SLE-RULE-0004 | Stable preferred term | ER-01, ER-04, ER-08 | SLE-EVAL-0002, 0005, 0008, 0010, 0013, 0014, 0016 | pass/fail/borderline/exception cases | terminology choice remains theory- and community-sensitive |
| SLE-RULE-0005 | Defined technical term | ER-01, ER-04, ER-08 | SLE-EVAL-0002, 0005, 0008, 0010, 0013, 0014, 0016 | pass/fail/borderline/exception cases | reviewer does not certify theoretical correctness of definition |
| SLE-RULE-0006 | Explicit comparison | ER-06, ER-07 | SLE-EVAL-0003, 0004, 0005, 0007, 0011, 0014 | pass/fail/borderline/exception cases | reviewer does not validate metric choice |
| SLE-RULE-0007 | Clear logical scope | ER-01, ER-04 | SLE-EVAL-0002, 0003, 0007, 0010, 0013 | pass/fail/borderline/exception cases | formal analysis remains a domain decision |
| SLE-RULE-0008 | Declared normative verbal forms | ER-01, ER-03, ER-11 | SLE-EVAL-0010, 0014; supplementary CS-0002 | pass/fail/borderline/exception cases | no universal must-versus-shall rule is adopted |
| SLE-RULE-0009 | Attestation does not establish stronger properties | ER-06, ER-07, ER-08 | SLE-EVAL-0001, 0005, 0008 | pass/fail/borderline/exception cases | stronger claim may proceed only through separate support |
| SLE-RULE-0010 | Judgment method | ER-06, ER-07 | SLE-EVAL-0006, 0007 | pass/fail/borderline/exception cases | reviewer does not decide grammaticality from responses |
| SLE-RULE-0011 | Example provenance dimensions | ER-02, ER-04, ER-05 | SLE-EVAL-0006, 0008, 0009, 0012, 0015 | pass/fail/borderline/exception cases | four-dimensional model remains proposed |
| SLE-RULE-0012 | Defined judgment notation | ER-02, ER-04 | SLE-EVAL-0002, 0006, 0007 | pass/fail/borderline/exception cases | symbol assignment itself is not validated |
| SLE-RULE-0013 | Stable example identifier | ER-01, ER-05, ER-08 | SLE-EVAL-0006, 0008, 0009, 0012, 0015 | pass/fail/borderline/exception cases | one-time adjacent references may be exempt |
| SLE-RULE-0014 | Dataset and transformation identity | ER-06, ER-08, ER-09, ER-10 | SLE-EVAL-0004, 0008, 0011, 0012 | pass/fail/borderline/exception cases | reviewer does not approve preprocessing choices |
| SLE-RULE-0015 | System behavior is not a language fact | ER-06, ER-07, ER-08, ER-10 | SLE-EVAL-0011; supplementary CS-0002 | pass/fail/borderline/exception cases | system and linguistic correctness require separate review |
| SLE-RULE-0016 | Condition before action | ER-01, ER-06 | SLE-EVAL-0010, 0014; supplementary CS-0002 | pass/fail/borderline/exception cases | reviewer does not validate the condition itself |
| SLE-RULE-0017 | One action per instruction | ER-01, ER-06, ER-10 | SLE-EVAL-0010, 0014; supplementary CS-0002 | pass/fail/borderline/exception cases | recommendation permits documented inseparable operations |
| SLE-RULE-0018 | Conformance does not certify truth | ER-03, ER-06, ER-07 | SLE-EVAL-0016 and corpus-wide instructions | pass/fail/borderline/exception cases | core truth-versus-conformance boundary |
| SLE-RULE-0019 | Observation separate from interpretation | ER-06, ER-07, ER-10 | SLE-EVAL-0001–0009, 0011, 0015 | pass/fail/borderline/exception cases | interpretation correctness remains substantive |
| SLE-RULE-0020 | Evidence wording does not overstate force | ER-07 | SLE-EVAL-0001–0005, 0007–0009, 0011, 0015 | pass/fail/borderline/exception cases | no universal evidence-verb hierarchy |
| SLE-RULE-0021 | Bounded negative claim | ER-06, ER-07, ER-10 | SLE-EVAL-0001, 0009, 0012 | pass/fail/borderline/exception cases | reviewer does not certify nonexistence |
| SLE-RULE-0022 | Limitations and counterevidence | ER-07 | all research and resource items | pass/fail/borderline/exception cases | reviewer does not discover every possible limitation |
| SLE-RULE-0023 | Claim-support connection | ER-05, ER-06, ER-07 | all research items | pass/fail/borderline/exception cases | link presence does not establish sufficiency |
| SLE-RULE-0024 | Interlinear glossing declaration | ER-02 | not directly tested in SLE-EVAL-CORPUS-0.1 | constructed checklist cases only | independently reviewed real gloss blocks remain required |

## Coverage interpretation

- **Independent rationale** refers to external or cross-domain source analysis recorded before the checklist.
- **Principal corpus items** show where the current synthetic corpus exercises the rule.
- **Direct test state** does not mean the rule has passed human evaluation.
- A stated gap prevents stabilization but does not prevent a proposed checklist item.
- SLE-RULE-0024 remains the clearest direct-coverage gap because the v0.1 corpus contains no independently reviewed interlinear-gloss block.
- Rules with broad corpus mappings may still be overfit because the corpus was constructed around the current rule set.

## Canto-span supplement

[[Canto-span Evaluation Subset v0.1]] provides only supplementary cases:

- `SLE-EVAL-CS-0001` stresses status wording, evidence force, limitations, and conformance-versus-truth boundaries.
- `SLE-EVAL-CS-0002` stresses system behavior, procedures, and normative language.

Neither item satisfies an independent rationale requirement or a multi-domain stabilization gate.

## Change rule

When a controlling rule changes:

1. update the checklist item;
2. update all four test-case classes;
3. update this traceability row;
4. reassess affected corpus items;
5. preserve prior test results under their original rule version;
6. classify the compatibility effect under [[Versioning and Release Model]].
