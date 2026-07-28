---
title: "Multi-Domain Reader and Author Evaluation Protocol v0.1"
type: evaluation-protocol
status: preregistration-draft
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - sle
  - evaluation
  - human-study
  - preregistration
---
# Multi-Domain Reader and Author Evaluation Protocol v0.1

## Status

This protocol prepares the human evaluation required by issue #9.

The study has **not started**. No participant data, effect estimate, rule disposition, or `publish`, `revise`, or `stop` recommendation exists.

The protocol must be frozen before condition-labelled outcome data are inspected. Administrative, ethics, accessibility, community, publisher, or institutional review must occur before recruitment when applicable.

## Central question

Does the proposed [[SLE for Linguistics Reference Artifact v0.1 Draft]] improve reader reconstruction, editorial review, and authoring reliability while preserving authorized meaning and avoiding unacceptable burden or bias?

The study evaluates communication performance. It does not determine linguistic truth, grammaticality, theoretical correctness, methodological validity, ethics, translation quality, software correctness, or community authority.

## Controlling records

- Evaluation principles: [[Evaluation Framework]]
- Initial study architecture: [[Pilot Study Design]]
- Decision thresholds: [[Preregistered Analysis and Decision Plan v0.1]]
- Materials and task allocation: [[Evaluation Material and Task Register v0.1]]
- Participant quotas: [[Participant Sampling and Recruitment Plan v0.1]]
- Data and privacy controls: [[Evaluation Data Dictionary and Privacy Plan v0.1]]
- Current execution state: [[Evaluation Execution Status v0.1]]
- Constructed procedure-testing corpus: [[Multi-Domain SLE Evaluation Corpus v0.1]]
- Meaning review: [[SLE Semantic Equivalence Review Template v0.1]]
- Human editorial controls: [[SLE Editorial Conformance Checklist v0.1]]

## Study phases

### Phase 0 — Material authorization and audit

Before participant exposure:

1. Identify the exact source, version, permission, access boundary, and authorized meaning record for every authentic item.
2. Create the uncontrolled, expert-edited plain, and proposed SLE-controlled conditions from the same authorized record.
3. Obtain independent meaning review for each condition.
4. Exclude any item with unresolved material meaning change from confirmatory comparison.
5. Preserve rejected alternatives and the reason for rejection.
6. Freeze scoring keys, item exclusions, condition labels, and trial allocation.

Constructed corpus items may be used for procedure piloting. They must remain labelled synthetic and cannot support authentic effectiveness claims.

### Phase 1 — Cognitive and operational pilot

Purpose:

- test instructions and task comprehension;
- test timing and accessibility;
- detect broken scoring keys, ceiling or floor effects, and accidental condition cues;
- estimate nuisance parameters for the main-study sample-size simulation;
- identify material that requires repair.

Pilot results must not be combined with confirmatory results after material or scoring changes.

Condition labels may remain masked during nuisance-parameter estimation. Primary success thresholds must not change after labels are revealed.

### Phase 2 — Main reader evaluation

Use randomized, counterbalanced condition assignment. A participant must not see more than one condition for the same underlying meaning record.

Reader tasks measure whether participants can identify:

- principal claim or instruction;
- population, language, variety, dataset, time, or other scope;
- direct evidence or recorded result;
- interpretation, hypothesis, conclusion, and limitation;
- uncertainty, alternatives, and counterevidence;
- antecedents and logical scope;
- example, translation, gloss, citation, and provenance status;
- normative force in procedures.

Primary reader outcomes:

- claim-and-scope reconstruction accuracy;
- unsupported inference rate;
- material misinterpretation rate.

Secondary reader outcomes:

- response time;
- confidence and confidence calibration;
- reference and terminology-error rate;
- limitation and alternative detection;
- subjective clarity and naturalness.

### Phase 3 — Editorial review evaluation

Participants apply a bounded resolved rule set and selected document patterns to passages or short sections.

Measure:

- agreement on applicable rule IDs;
- agreement on final item outcomes;
- correct use of `not applicable`, `Justified exception`, waiver, and `not determined`;
- review time;
- false substantive-certification statements;
- disagreement causes and escalation needs.

`Borderline` is recorded only as a provisional flag. It must resolve before a completed review record.

### Phase 4 — Authoring and revision evaluation

Authors complete two separate tasks:

1. revise a passage against an authorized meaning record;
2. draft new text from a structured research brief.

Compare ordinary expert guidance and proposed SLE guidance. Do not compare SLE only against deliberately defective prose.

Measure:

- authorized-meaning preservation;
- unintended addition, deletion, strengthening, or weakening;
- writing and revision time;
- terminology consistency;
- unresolved uncertainty handling;
- cohesion, naturalness, repetition, and fragmentation;
- need for specialist help;
- rule usability and teachability;
- perceived burden.

### Phase 5 — Translation and rhetorical-order evaluation

This phase requires non-English-original material and independently reviewed translations.

Compare:

- source-order translation;
- ordinary expert translation or editing;
- translation or reorganization using proposed SLE controls.

Measure normative-function preservation, terminology preservation, reader reconstruction, naturalness, rhetorical-order acceptability, burden, and disagreement.

A translated result applies only to the tested language direction, passage, participant group, and review authority.

### Phase 6 — Full-document and combined-pattern evaluation

Apply the reference artifact to full sections or documents that combine multiple communicative purposes.

Measure:

- duplication and fragmentation;
- ordering conflict;
- cross-reference burden;
- profile reconstruction;
- conformance-result reconstruction;
- cohesion;
- whether short-passage benefits or harms persist.

## Experimental conditions

For each authorized meaning record, use up to three conditions:

- **U — uncontrolled or source draft**;
- **P — ordinary expert-edited plain alternative**;
- **S — proposed SLE-controlled alternative**.

The comparison of S with P is required for publication claims. A benefit over U alone does not establish benefit over ordinary expert editing.

Each condition must preserve the same authorized information. A condition with a possible material change receives `not determined` and is not used as a valid confirmatory comparison.

## Assignment and counterbalancing

- Randomize condition assignment within material blocks.
- Counterbalance domain, condition, and presentation order.
- Prevent the same participant from seeing multiple conditions from one meaning record.
- Limit repeated exposure to one rule family.
- Record device, interruption, and accessibility accommodations when relevant.
- Do not reveal the intended “better” condition.

## Participant groups

Recruit across:

- descriptive, documentary, and field linguistics;
- theoretical linguistics from multiple frameworks;
- corpus, experimental, sociolinguistic, discourse, or phonetic research;
- computational linguistics and language-resource work;
- editing, reviewing, research assistance, and advanced study;
- authors who have not contributed to SLE design.

Cross-cutting records include primary scholarly language, English-use context, career stage, method and theory experience, controlled-language familiarity, accessibility needs, and community relationship where relevant.

Canto-span maintainers may enter only the labelled Canto-span arm. They must not dominate any domain stratum or the overall sample.

## Material coverage gates

The main study cannot launch until the material register includes:

- multiple domains, methods, theories, genres, and participant roles;
- authentic authorized passages from independent sources;
- at least one non-English-original and independently reviewed translation block;
- direct example and interlinear-glossing tasks;
- procedure and annotation tasks;
- full-document or full-section material;
- ordinary expert-edited plain comparison conditions;
- no single source, project, language, framework, or venue dominating the confirmatory set.

The current constructed corpus does not satisfy these gates.

## Exclusion policy

Participant-level exclusions must be mechanical and preregistered, such as:

- no consent or required authorization;
- duplicate participation;
- failure to complete the minimum assigned task block;
- technical failure that prevents stimulus display or response recording;
- failure of a neutral attention or instruction check defined before launch.

Do not exclude a participant for disagreeing with SLE, reporting bias, selecting `not determined`, or preferring ordinary editing.

Item-level exclusions include:

- unresolved authorized meaning;
- material condition mismatch;
- invalid or ambiguous scoring key;
- permission or access failure;
- condition cue that reveals the expected answer;
- post-freeze material change.

Report all exclusions by condition and reason.

## Safeguards against result-dependent revision

Before the main study:

1. freeze the protocol version;
2. freeze materials and hashes or immutable versions;
3. freeze primary outcomes and thresholds;
4. freeze exclusions and analysis models;
5. freeze rule-level harm and stop criteria;
6. record deviations without rewriting the original plan;
7. keep exploratory analyses visibly separate.

## Reporting requirements

Report:

- recruitment and attrition by participant group;
- material coverage by domain, theory, method, language, and genre;
- primary and secondary results by condition;
- subgroup estimates with uncertainty;
- semantic-preservation failures;
- harmful, biased, burdensome, neutral, beneficial, and inconclusive rule findings;
- qualitative failure cases, including ordinary editing outperforming SLE;
- all protocol deviations;
- tested scope and explicit non-generalization boundaries.

No result may be generalized beyond the tested materials, participant groups, languages, directions, methods, or document lengths.

## Canto-span boundary

The Canto-span arm is supplementary and separately reported. It cannot satisfy independent coverage or determine the project-wide recommendation.

## Completion rule

Issue #9 remains open until:

- participant and material authorization is complete;
- the study is actually run;
- anonymized data or publishable aggregates are deposited when appropriate;
- analysis is completed under the frozen plan;
- rule-level dispositions are recorded;
- an evidence-linked `publish`, `revise`, or `stop` recommendation is made;
- epic #1 is updated.
