---
title: "Preregistered Analysis and Decision Plan v0.1"
type: evaluation-analysis-plan
status: preregistration-draft
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - sle
  - evaluation
  - analysis
  - decision
---
# Preregistered Analysis and Decision Plan v0.1

## Status

This plan defines analysis and decision rules for [[Multi-Domain Reader and Author Evaluation Protocol v0.1]].

No participant outcome data have been collected or analyzed. Numerical planning thresholds below are proposal-stage thresholds and must be frozen before confirmatory condition labels are inspected.

## Analysis principles

1. Analyze readers, reviewers, authors, translators, and full-document users separately before any synthesis.
2. Estimate condition effects with uncertainty; do not reduce evidence to significance labels alone.
3. Model participants and materials as varying sources when the design permits.
4. Preserve domain, participant-group, language-direction, and genre boundaries.
5. Treat `not determined` as an informative result, not missing success.
6. Report SLE versus uncontrolled prose and SLE versus ordinary expert editing.
7. Keep confirmatory and exploratory analyses separate.
8. Do not use Canto-span results to determine the project-wide disposition.

## Primary reader outcomes

### Claim-and-scope reconstruction accuracy

Score the preregistered claim, scope, and condition fields against the frozen authorized key.

Primary contrast:

- S condition minus U condition.

Required comparative contrast:

- S condition minus P condition.

### Unsupported inference rate

A response counts as an unsupported inference when it asserts a materially stronger, broader, more certain, causal, universal, or substantive conclusion than the authorized record licenses.

### Material misinterpretation rate

A material misinterpretation changes polarity, quantification, scope, evidence force, theoretical commitment, example status, access boundary, normative force, or another preregistered critical dimension.

## Primary author outcome

### Material meaning-preservation failure

A failure occurs when an independently reviewed output changes a critical or major meaning dimension relative to the authorized record.

`Not determined` is reported separately and cannot be recoded as preserved.

## Primary review outcome

### Final-outcome agreement

Measure agreement on:

- applicable rule set;
- final item outcome;
- whole-object conformance result;
- need for substantive escalation.

A shared but incorrect answer does not count as valid agreement when an authorized key exists.

## Secondary outcomes

- response or completion time;
- confidence and calibration;
- terminology consistency;
- limitation and alternative detection;
- antecedent and logical-scope accuracy;
- procedure action accuracy;
- review and authoring burden;
- cohesion and naturalness;
- repetition and fragmentation;
- rule usability and teachability;
- qualitative bias or oversimplification reports.

## Proposed statistical models

The final preregistration must name the exact software-independent model specification. The conceptual default is:

- binary outcomes: mixed-effects logistic model or a prespecified equivalent;
- bounded ordinal outcomes: cumulative ordinal model or a prespecified equivalent;
- continuous timing outcomes: transformed mixed-effects model or robust prespecified equivalent;
- count outcomes: Poisson or negative-binomial mixed model according to frozen diagnostic criteria;
- agreement: raw agreement plus an appropriate chance-adjusted or model-based measure;
- preservation dimensions: item-level risk estimates with exact counts and uncertainty.

Include participant and material effects when identifiable. Add domain or participant-group interactions only as preregistered primary subgroup analyses or clearly labelled exploratory analyses.

Do not change the model solely because a preferred result is not obtained.

## Smallest effects and proposed success thresholds

These thresholds must be frozen before confirmatory data inspection.

### Reader benefit gate

For the pooled tested scope:

- estimated S versus U improvement in claim-and-scope accuracy is at least 8 percentage points;
- the uncertainty interval excludes no improvement in the harmful direction;
- unsupported inference and material misinterpretation do not increase.

### Ordinary-editing comparison gate

S must not be materially worse than P:

- non-inferiority margin for claim-and-scope accuracy: 5 percentage points;
- non-inferiority margin for material misinterpretation: 3 percentage points;
- any time or burden increase must be interpreted with the authoring gate rather than ignored.

S does not need to outperform P on every outcome. A finding that ordinary editing performs equally well with lower burden is a valid reason to revise or narrow SLE.

### Author preservation gate

- no unresolved SLE-attributable critical meaning failure in confirmatory authentic material;
- estimated S versus P increase in critical-or-major preservation failure does not exceed 3 percentage points;
- `not determined` rates are reported and must not be hidden through exclusion;
- source-author or authorized-proxy review confirms the exact scope of any preservation claim.

### Author burden gate

For the pooled tested authoring tasks:

- median S condition completion time should not exceed P by more than 25% without a demonstrated reader or safety benefit;
- severe burden, fragmentation, or theory-bias reports must not concentrate in one tested group;
- accommodation-related time is analyzed separately and never treated as failure.

### Reviewability gate

- applicable-rule and final-outcome agreement must reach the frozen adequacy threshold after the pilot;
- false substantive-certification statements must be rare and individually reviewed;
- frequent `not determined` outcomes trigger rule, material, training, or applicability review rather than automatic failure.

## Domain and participant safeguards

A pooled positive result cannot support `publish` when:

- one domain or participant group shows material harm;
- a theory, method, language direction, or community reports unresolved structural bias;
- the pooled result is driven by one source or material family;
- authentic material results conflict materially with constructed-pilot results;
- source-author preservation fails.

Report each primary stratum and material family even when estimates are imprecise.

## Rule-level classification

Classify every evaluated rule as one of:

### Beneficial

Observed evidence shows a relevant improvement with no material semantic, bias, or burden failure in the tested scope.

### Neutral

No material benefit or harm is established, and the rule may still serve a documented low-burden consistency function.

### Harmful

The rule causes or contributes to meaning loss, misinterpretation, false certainty, unacceptable burden, damaged cohesion, or substantive-certification risk.

### Biased

The rule or its implementation privileges a theory, method, language, rhetorical order, access model, or scholarly tradition without adequate justification.

### Burdensome

The rule creates substantial time, repetition, fragmentation, training, or specialist-support cost without proportionate benefit.

### Inconclusive

Coverage, precision, meaning authority, agreement, or task validity is insufficient.

A rule can receive more than one adverse tag. Do not silently retain a harmful or biased rule as merely neutral.

## Rule action mapping

- beneficial: retain as proposed or consider stabilization only after all independent gates pass;
- neutral: retain experimentally, narrow, make optional, or retire according to burden and rationale;
- harmful: revise, narrow, move to an extension, suspend, or remove;
- biased: revise with affected authorities, limit scope, move to an extension, or remove;
- burdensome: simplify, consolidate, make optional, or remove;
- inconclusive: remain proposed with explicit gaps or suspend pending evidence.

No rule becomes stable from one pooled study result.

## Project-level disposition

### `publish`

Use only when all apply within the tested scope:

- reader benefit or strong operational need is demonstrated;
- ordinary expert editing is not clearly preferable on the combined benefit, safety, and burden evidence;
- authentic authorized meaning preservation passes;
- no unresolved critical domain, theory, method, language, accessibility, or community harm remains;
- harmful and biased rule findings have been resolved or removed;
- evidence and limitations are publishable and traceable;
- the recommendation identifies the exact proposed release scope and remaining non-generalization boundaries.

`Publish` does not mean universal effectiveness or stable status for every rule.

### `revise`

Use when:

- benefits are mixed, narrow, or offset by burden;
- some rules are harmful, biased, burdensome, or unclear but repair appears feasible;
- coverage or precision is incomplete;
- ordinary editing performs as well or better for important tasks;
- authentic and constructed results conflict;
- additional testing is required before publication.

### `stop`

Use when:

- repeated critical meaning loss remains after repair;
- the core approach produces systematic theoretical, methodological, linguistic, accessibility, or community harm;
- burden materially exceeds demonstrated benefit across the intended scope;
- the reference cannot be applied with adequate reliability;
- the central benefit is not supported after appropriately powered testing and plausible repair has failed.

Stopping the current core design does not prohibit narrower local guidance or future independent work.

## Missing-data and `not determined` handling

- Report missingness by condition and reason.
- Do not impute a correct interpretation or preservation result from a participant's other responses.
- Do not convert `not determined` to success.
- Sensitivity analyses may test bounded assumptions but must remain labelled.
- Participant withdrawal and restricted-data removal follow the approved privacy plan.

## Multiple outcomes

The final preregistration must identify:

- one primary reader outcome family;
- one primary author safety outcome;
- one primary reviewability outcome;
- multiplicity handling for confirmatory secondary tests;
- exploratory analyses that do not affect the primary disposition.

## Qualitative analysis

Use a frozen coding framework for:

- lost distinctions;
- unnatural or English-specific order;
- theory or method bias;
- inaccessible instructions;
- repetition and fragmentation;
- unavailable meaning authority;
- ordinary editing advantages;
- beneficial rule explanations;
- requests for local extensions or waivers.

Preserve negative cases and dissent. Report who supplied an interpretation and the tested scope.

## Deviations and transparency

Every deviation is recorded under [[Evaluation Data Dictionary and Privacy Plan v0.1]].

The final report must include:

- frozen protocol and analysis versions;
- deviations before and after outcome unmasking;
- all exclusions;
- all primary results;
- adverse and null results;
- code or reproducible calculation details when publishable;
- limitations and non-generalization boundaries.

## Current decision state

No project-level or rule-level result exists. The only valid current recommendation is **not determined — study not executed**.
