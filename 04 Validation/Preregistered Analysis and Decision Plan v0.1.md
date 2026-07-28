---
title: "Analysis and Decision Plan Draft v0.1"
type: evaluation-analysis-plan
status: freeze-ready-draft
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - ariadline
  - evaluation
  - analysis
  - decision
  - protocol-draft
---
# Analysis and Decision Plan Draft v0.1

## Status

This plan defines proposed analysis and decision rules for [[Multi-Domain Reader and Author Evaluation Protocol v0.1]].

It is **not yet preregistered**. No participant outcome data have been collected or analyzed. Numerical planning thresholds below are proposal-stage thresholds.

The plan becomes a preregistration only after all of the following are complete:

1. a human study lead and qualified statistical reviewer approve the exact primary outcome family, models, estimands, thresholds, exclusions, multiplicity treatment, sample target, and subgroup plan;
2. the protocol, material register, condition sets, scoring keys, and analysis code or calculation specification are frozen;
3. an immutable repository commit and, where applicable, an external registration record are created before confirmatory condition-labelled outcome inspection;
4. the registration date, responsible roles, immutable identifiers, and permitted amendment process are recorded.

Until then, cite this record only as an **analysis-plan draft**.

## Analysis principles

1. Analyze readers, reviewers, authors, translators, and full-document users separately before any synthesis.
2. Estimate condition effects with uncertainty; do not reduce evidence to significance labels alone.
3. Model participants and materials as varying sources when the design permits.
4. Preserve domain, participant-group, language-direction, and genre boundaries.
5. Treat `not determined` as an informative result, not missing success.
6. Report Ariadline versus ordinary expert editing for every publication-relevant task.
7. Report Ariadline versus an authorized U baseline only for tasks that registered U as admissible.
8. Keep confirmatory and exploratory analyses separate.
9. Do not use Canto-span results to determine the project-wide disposition.

## Condition and estimand rules

- `P` versus `S` is the required publication-relevant comparison.
- `U` is an optional authorized source or uncontrolled baseline, not a preservation-certified rewrite.
- An S-versus-U estimate is valid only for registered reader or full-document tasks with an admissible U baseline.
- Authoring compares participant outputs produced under P and S guidance against the same authorized record.
- Translation compares P and S outputs against the source-language authority; a source-order baseline is analyzed only when separately registered.
- Do not synthesize incompatible task estimands into one project effect.

## Primary reader outcomes

### Claim-and-scope reconstruction accuracy

Score the frozen claim, scope, and condition fields against the authorized key.

Required publication contrast:

- S condition minus P condition.

Optional baseline contrast:

- S condition minus U condition, only for registered admissible U items.

### Unsupported inference rate

A response counts as an unsupported inference when it asserts a materially stronger, broader, more certain, causal, universal, or substantive conclusion than the authorized record licenses.

### Material misinterpretation rate

A material misinterpretation changes polarity, quantification, scope, evidence force, theoretical commitment, example status, access boundary, normative force, or another frozen critical dimension.

The human statistical review must choose and freeze one primary reader outcome family and the exact relation among these components before registration.

## Primary author outcome

### Material meaning-preservation failure

A failure occurs when an independently reviewed output changes a critical or major meaning dimension relative to the authorized record.

`Not determined` is reported separately and cannot be recoded as preserved.

The authoring estimand compares failure risk under P guidance with failure risk under S guidance.

## Primary review outcome

### Final-outcome agreement and validity

Measure agreement on:

- applicable rule set;
- final item outcome;
- whole-object conformance result;
- need for substantive escalation.

A shared but incorrect answer does not count as valid agreement when an authorized key exists.

The final preregistration must identify the primary agreement or validity estimand and its adequacy threshold.

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

## Proposed statistical model families

The immutable preregistration must name the exact model, coding, estimand, software-independent equation or calculation specification, convergence and diagnostic rules, and fallback model.

Conceptual candidates are:

- binary outcomes: mixed-effects logistic model or a frozen equivalent;
- bounded ordinal outcomes: cumulative ordinal model or a frozen equivalent;
- continuous timing outcomes: transformed mixed-effects model or robust frozen equivalent;
- count outcomes: Poisson or negative-binomial mixed model under frozen diagnostic criteria;
- agreement: raw agreement plus a frozen chance-adjusted or model-based measure;
- preservation dimensions: item-level risk estimates with exact counts and uncertainty.

Include participant and material effects when identifiable. Add domain or participant-group interactions only as frozen primary subgroup analyses or clearly labelled exploratory analyses.

Do not change the model solely because a preferred result is not obtained.

## Proposed smallest effects and decision thresholds

These values are planning proposals. Human statistical review must justify, revise if necessary, and freeze them before confirmatory recruitment. Any revision must occur before condition-labelled outcome inspection and must be recorded.

### Reader benefit and safety gate

For registered reader tasks:

- S-versus-P claim-and-scope accuracy must meet the frozen benefit or non-inferiority criterion;
- unsupported inference and material misinterpretation must not increase beyond frozen safety margins;
- where U is registered, S-versus-U benefit may provide supporting evidence but cannot replace S-versus-P evidence.

Initial planning values for review:

- S-versus-U improvement target, where applicable: 8 percentage points;
- S-versus-P non-inferiority margin for claim-and-scope accuracy: 5 percentage points;
- S-versus-P non-inferiority margin for material misinterpretation: 3 percentage points.

These numbers have no confirmatory authority until justified and frozen.

### Author preservation gate

Initial planning proposal:

- no unresolved Ariadline-attributable critical meaning failure in confirmatory authentic material;
- S-versus-P increase in critical-or-major preservation failure does not exceed a frozen margin, initially proposed as 3 percentage points;
- `not determined` rates are reported and must not be hidden through exclusion;
- source-author or authorized-proxy review confirms the exact scope of any preservation claim.

### Author burden gate

Initial planning proposal:

- median S completion time should not exceed P by more than 25% without a demonstrated reader, safety, or operational benefit;
- severe burden, fragmentation, or theory-bias reports must not concentrate in one tested group;
- accommodation-related time is analyzed separately and never treated as failure.

### Reviewability gate

- applicable-rule and final-outcome agreement must reach a human-approved frozen adequacy threshold;
- false substantive-certification statements must be rare and individually reviewed;
- frequent `not determined` outcomes trigger rule, material, training, or applicability review rather than automatic failure.

## Sample-size and precision requirement

Before preregistration, a qualified human reviewer must complete a simulation or precision analysis using:

- the frozen primary estimand and model;
- justified smallest effects or safety margins;
- participant and material variance estimates from the pilot or defensible independent priors;
- planned condition, material, and stratum allocation;
- expected attrition and exclusions;
- multiplicity and subgroup requirements.

The sample target is not frozen in this draft.

## Domain and participant safeguards

A pooled positive result cannot support `publish` when:

- one domain or participant group shows material harm;
- a theory, method, language direction, accessibility group, or community reports unresolved structural bias;
- the pooled result is driven by one source or material family;
- authentic material results conflict materially with constructed-pilot results;
- source-author preservation fails.

Report each primary stratum and material family even when estimates are imprecise.

## Rule-level classification

Classify every evaluated rule as one or more of the following, with tested scope and evidence:

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

- reader benefit or strong operational need is demonstrated under the frozen criteria;
- ordinary expert editing is not clearly preferable on combined benefit, safety, and burden evidence;
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

The immutable preregistration must identify:

- one primary reader outcome family;
- one primary author safety outcome;
- one primary reviewability outcome;
- multiplicity handling for confirmatory secondary tests;
- subgroup analyses that can affect disposition;
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
- immutable preregistration identifier;
- deviations before and after outcome unmasking;
- all exclusions;
- all primary results;
- adverse and null results;
- code or reproducible calculation details when publishable;
- limitations and non-generalization boundaries.

## Current decision state

No project-level or rule-level result exists. The only valid current recommendation is **not determined — study not executed**.
