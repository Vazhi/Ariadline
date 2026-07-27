---
title: "SLE-GE Canto-span Pilot Baseline v0.1"
type: validation-baseline
status: locked
version: "0.1"
created: 2026-07-27
updated: 2026-07-27
aliases:
  - "SLE-GE Pilot Baseline"
  - "Canto-span Pilot Baseline"
tags:
  - sle
  - validation
  - pilot-baseline
  - canto-span
  - grammar-engineering
---

# SLE-GE Canto-span Pilot Baseline v0.1

> [!abstract] Purpose
> This note freezes the source materials, reader questions, measures, safeguards, and decision outcomes for the first Canto-span SLE-GE test run. It must be fixed before paired rewriting begins.

## Baseline status

- Baseline version: **0.1**
- Lock state: **locked for material selection and question design**
- Baseline date: **2026-07-27**
- External repository: `Vazhi/canto-span`
- Frozen commit: [`c9dd631739734a5ab886f0b667db9888b0add13b`](https://github.com/Vazhi/canto-span/commit/c9dd631739734a5ab886f0b667db9888b0add13b)
- Parent SLE issue: [#1](https://github.com/Vazhi/simplified-linguistic-english/issues/1)
- Baseline issue: [#2](https://github.com/Vazhi/simplified-linguistic-english/issues/2)
- Deviation ledger: [#11](https://github.com/Vazhi/simplified-linguistic-english/issues/11)

This note is an SLE research instrument. It is not a current-state owner for Canto-span. All copied values are dated observations from the frozen commit.

## Experimental purpose

The test run has two objectives:

1. determine whether a proposed SLE Grammar Engineering Profile helps readers interpret Canto-span documentation;
2. discover where the current proposed [[Simplified Linguistic English|SLE]] notes, profiles, templates, and repository infrastructure are insufficient.

A workaround is evidence about a gap. It is not evidence that the current SLE already supported the task.

## Authority and reproducibility rules

1. Commit-pinned file URLs are the primary references for repository files.
2. A pull-request example must identify its PR number and associated head or merge commit.
3. Volatile Canto-span values must include the baseline date and canonical owner.
4. A source excerpt must not become a second canonical owner.
5. A later Canto-span change does not modify this baseline.
6. A material change to this baseline requires version `0.2` or later and must occur before paired rewriting begins.
7. After paired rewriting begins, additions are recorded as a new study wave rather than silently changing this baseline.

See [[Governance and Change Control]] and [[Versioning and Release Model]].

## Frozen material inventory

### Governance and current-state documents

| ID | Document class | Frozen source | Reason for inclusion |
|---|---|---|---|
| GOV-01 | cross-cutting project contract | [`docs/current/00-START-HERE.md`](https://github.com/Vazhi/canto-span/blob/c9dd631739734a5ab886f0b667db9888b0add13b/docs/current/00-START-HERE.md) | Tests authority, state ownership, workflow requirements, and dense normative prose. |
| GOV-02 | current-state report | [`docs/current/PROJECT-STATE.md`](https://github.com/Vazhi/canto-span/blob/c9dd631739734a5ab886f0b667db9888b0add13b/docs/current/PROJECT-STATE.md) | Tests dated volatile values and separation of status, runtime, evidence, readiness, and work order. |
| GOV-03 | evidence and release governance | [`docs/current/GOVERNANCE.md`](https://github.com/Vazhi/canto-span/blob/c9dd631739734a5ab886f0b667db9888b0add13b/docs/current/GOVERNANCE.md) | Tests evidence classes, corpus and panel policy, dispositions, and release boundaries. |
| GOV-04 | completion-gate specification | [`docs/current/DEFINITION-OF-DONE.md`](https://github.com/Vazhi/canto-span/blob/c9dd631739734a5ab886f0b667db9888b0add13b/docs/current/DEFINITION-OF-DONE.md) | Tests normative requirements, thresholds, exclusions, and non-criteria. |

### Construction-note sample

The sample uses four notes from each of the three sufficiently populated active statuses. It deliberately varies construction family, evidence maturity, and claim layer.

| ID | Frozen status | Permanent code | Legacy note label | Frozen source | Sampling reason |
|---|---|---:|---|---|---|
| CON-01 | `research_pending` | AA01 | `ANotAQuestion` | [`grammar/research_pending/ANotAQuestion.md`](https://github.com/Vazhi/canto-span/blob/c9dd631739734a5ab886f0b667db9888b0add13b/grammar/research_pending/ANotAQuestion.md) | Question structure; canonical-name versus legacy-label conflict; existing worked example. |
| CON-02 | `research_pending` | AA11 | `ChangeIntoPredicate` | [`grammar/research_pending/ChangeIntoPredicate.md`](https://github.com/Vazhi/canto-span/blob/c9dd631739734a5ab886f0b667db9888b0add13b/grammar/research_pending/ChangeIntoPredicate.md) | Lexeme-specific narrowing and competing result analyses. |
| CON-03 | `research_pending` | AB11 | `NominalPredicateClause` | [`grammar/research_pending/NominalPredicateClause.md`](https://github.com/Vazhi/canto-span/blob/c9dd631739734a5ab886f0b667db9888b0add13b/grammar/research_pending/NominalPredicateClause.md) | Measure predication, misleading broad label, and evidence-bound scope. |
| CON-04 | `research_pending` | AB30 | `PostverbalZoPerfectiveVP` | [`grammar/research_pending/PostverbalZoPerfectiveVP.md`](https://github.com/Vazhi/canto-span/blob/c9dd631739734a5ab886f0b667db9888b0add13b/grammar/research_pending/PostverbalZoPerfectiveVP.md) | Mature corpus packet, active panel links, parser evidence, and promotion blockers. |
| CON-05 | `unsupported_generalization` | AA02 | `AcceptabilityANotA` | [`grammar/unsupported_generalization/AcceptabilityANotA.md`](https://github.com/Vazhi/canto-span/blob/c9dd631739734a5ab886f0b667db9888b0add13b/grammar/unsupported_generalization/AcceptabilityANotA.md) | Acceptability terminology and a narrow lexical boundary under a broad label. |
| CON-06 | `unsupported_generalization` | AA12 | `ClassifierObjectNP` | [`grammar/unsupported_generalization/ClassifierObjectNP.md`](https://github.com/Vazhi/canto-span/blob/c9dd631739734a5ab886f0b667db9888b0add13b/grammar/unsupported_generalization/ClassifierObjectNP.md) | Role-specific runtime wrapper versus role-neutral NP analysis. |
| CON-07 | `unsupported_generalization` | AA93 | `MotionGoalVP` | [`grammar/unsupported_generalization/MotionGoalVP.md`](https://github.com/Vazhi/canto-span/blob/c9dd631739734a5ab886f0b667db9888b0add13b/grammar/unsupported_generalization/MotionGoalVP.md) | Source, goal, deictic, abstract, and purpose boundaries. |
| CON-08 | `unsupported_generalization` | AB64 | `SourceMotionClause` | [`grammar/unsupported_generalization/SourceMotionClause.md`](https://github.com/Vazhi/canto-span/blob/c9dd631739734a5ab886f0b667db9888b0add13b/grammar/unsupported_generalization/SourceMotionClause.md) | Broad family claim with incomplete exact boundaries. |
| CON-09 | `parser_heuristic` | AA13 | `ClauseRelationEdge` | [`grammar/parser_heuristic/ClauseRelationEdge.md`](https://github.com/Vazhi/canto-span/blob/c9dd631739734a5ab886f0b667db9888b0add13b/grammar/parser_heuristic/ClauseRelationEdge.md) | Internal relation representation that must not become a language claim. |
| CON-10 | `parser_heuristic` | AA14 | `ClauseRelationGraph` | [`grammar/parser_heuristic/ClauseRelationGraph.md`](https://github.com/Vazhi/canto-span/blob/c9dd631739734a5ab886f0b667db9888b0add13b/grammar/parser_heuristic/ClauseRelationGraph.md) | Internal aggregate and graph terminology. |
| CON-11 | `parser_heuristic` | AA16 | `ClauseSpan` | [`grammar/parser_heuristic/ClauseSpan.md`](https://github.com/Vazhi/canto-span/blob/c9dd631739734a5ab886f0b667db9888b0add13b/grammar/parser_heuristic/ClauseSpan.md) | Neutral span representation and system-language boundary. |
| CON-12 | `parser_heuristic` | AB22 | `PolarQuestionFrame` | [`grammar/parser_heuristic/PolarQuestionFrame.md`](https://github.com/Vazhi/canto-span/blob/c9dd631739734a5ab886f0b667db9888b0add13b/grammar/parser_heuristic/PolarQuestionFrame.md) | Narrow final-咩 system frame under a broad legacy label. |

#### Sampling limitation

At the frozen baseline, the current note inventory contains:

- 79 `research_pending`;
- 37 `unsupported_generalization`;
- 15 `parser_heuristic`;
- 2 `lexicalized_only`;
- 0 `supported_productive`;
- 0 `provisional_reaudit`;
- 0 `provisional`.

The twelve-note sample does not estimate performance for empty statuses or the two-record `lexicalized_only` stratum. A future wave may add the rare stratum through a versioned baseline amendment before rewriting begins.

### Identity, corpus, panel, PR, and release-facing materials

| ID | Document class | Frozen or stable source | Reason for inclusion |
|---|---|---|---|
| ID-01 | permanent identity registry | [`data/construction-identities.json`](https://github.com/Vazhi/canto-span/blob/c9dd631739734a5ab886f0b667db9888b0add13b/data/construction-identities.json) | Tests UUID, code, canonical name, legacy alias, claim layer, profile, and lifecycle distinctions. |
| COR-01 | corpus-review ledger | [`review-packets/corpus-review/AB30/candidate-ledger.json`](https://github.com/Vazhi/canto-span/blob/c9dd631739734a5ab886f0b667db9888b0add13b/review-packets/corpus-review/AB30/candidate-ledger.json) | Tests retrieval versus classification, stable candidates, totals, and evidence limits. |
| PAN-01 | native-panel state | [`review-packets/native-panel/active-v2/panel-review-state.json`](https://github.com/Vazhi/canto-span/blob/c9dd631739734a5ab886f0b667db9888b0add13b/review-packets/native-panel/active-v2/panel-review-state.json) | Tests instrument version, eligibility, item-level usable judgments, and historical-versus-current evidence. |
| PR-01 | substantive pull-request summary | [PR #209](https://github.com/Vazhi/canto-span/pull/209), merged as [`c9dd631739734a5ab886f0b667db9888b0add13b`](https://github.com/Vazhi/canto-span/commit/c9dd631739734a5ab886f0b667db9888b0add13b) | Tests whether a technical change report separates implementation scope from linguistic and governance effects. |
| REL-01A | release metadata proxy | [`manifest.json`](https://github.com/Vazhi/canto-span/blob/c9dd631739734a5ab886f0b667db9888b0add13b/manifest.json) | Provides the frozen runtime version and deployment metadata. |
| REL-01B | release-facing handoff proxy | [PR #177](https://github.com/Vazhi/canto-span/pull/177), head `2bcc773c383fbf615f22d348b7ae5b5f936f96bd`, merge `2d62d9f15d32e2137d372f0b9c97db17a43757d6` | Tests version, validation, protected state, and release-facing claims. It is not labelled as an original release note. |

No standalone release-note document was located at the frozen baseline. REL-01A and REL-01B therefore form an explicit proxy pair. This deviation is recorded in issue #11 and must not be hidden in the paired corpus.

## State dimensions that must remain separate

Participants must be able to distinguish these dimensions:

| Dimension | Direct question |
|---|---|
| permanent identity | Which UUID and code identify the record? |
| canonical ontology | What are the canonical name, family, profile, and claim layer? |
| legacy compatibility | Which runtime or note label remains for compatibility? |
| linguistic status | What evidence disposition is currently recorded? |
| runtime recognition | What does the parser recognize at the frozen version? |
| external source evidence | Which propositions have source-matched support? |
| corpus retrieval | What did the query retrieve? |
| corpus classification | Which candidates are genuine, false positive, ambiguous, or unusable? |
| panel evidence | Which item-level judgments are eligible, usable, and adjudicated? |
| discovery readiness | Which gaps does the readiness record expose? |
| work availability | Is the construction eligible for bounded work or parked? |
| workflow ownership | Who or what owns the active task? |
| authorization | Is promotion, merge, deployment, or release explicitly authorized? |
| historical provenance | Which record explains an earlier state without controlling the current state? |

A result in one dimension must not be used as a direct answer for another dimension.

## Locked reader questions

The reader-question set is locked for baseline version 0.1.

1. What is the canonical name of the construction or governed object?
2. Which label is only a legacy runtime, note, or compatibility label?
3. What exact structural or functional profile is claimed?
4. Which forms, analyses, populations, datasets, or contexts are excluded?
5. What is the current linguistic status at the frozen baseline?
6. Does the runtime recognize the form or profile?
7. What does each external source directly establish?
8. What does the source evidence not establish?
9. How many corpus candidates were retrieved?
10. How many candidates were reviewed as genuine, false positive, ambiguous, or unusable?
11. What does the corpus evidence establish, and what does it not establish?
12. What is the instrument version and current panel lifecycle state?
13. What is the usable numerator and denominator for each critical item?
14. Does the panel evidence satisfy the applicable gate?
15. Which record is the canonical owner of each answer?
16. Is the construction promotion-eligible?
17. Is the PR merge-authorized at the stated head?
18. Is a release or deployment action authorized?
19. Is the statement an observation, attestation, judgment, generalization, analysis, system result, requirement, decision, current-state fact, or limitation?
20. Is a cited record current authority or historical provenance?
21. Which state dimensions changed?
22. Which adjacent state dimensions explicitly did not change?

Questions may be presented in subsets appropriate to a document class. Their meanings and scoring keys must not change between original and SLE-GE conditions.

## Measures

### Primary reader measures

- answer accuracy for each locked question;
- unsupported-inference rate;
- time to complete each document task;
- confidence calibration.

### Secondary reader and review measures

- reviewer disagreement;
- number of source documents opened;
- number of rereads or navigation reversals;
- time to approve or reject a summary;
- qualitative reports of ambiguity, overload, or lost cohesion.

### Authoring and preservation measures

- rewrite time;
- number of controlled terms introduced;
- sentence and section expansion;
- semantic-equivalence disagreements;
- unintended changes in polarity, scope, evidential force, theoretical commitment, or authorization;
- number and severity of required waivers;
- blocker and deviation count.

### Checker measures for later phases

- precision and recall by rule;
- false-positive burden;
- false-negative severity;
- deterministic agreement across runs;
- number of diagnostics that require human adjudication.

These measures extend [[Evaluation Framework]] and [[Pilot Study Design]].

## Comparison conditions

Where the selected material permits, compare:

1. the frozen original;
2. expert-edited plain prose without SLE-specific controls;
3. SLE-GE prose.

The plain-edited condition is required when practical so that the evaluation does not attribute ordinary editing benefits to SLE.

## Semantic-equivalence safeguards

Every paired rewrite must:

1. preserve polarity and negation scope;
2. preserve quantification and thresholds;
3. preserve evidential force;
4. preserve theoretical neutrality or declared commitment;
5. preserve all stated exclusions and limitations;
6. preserve canonical-owner relationships;
7. preserve current-versus-historical status;
8. preserve permissions, prohibitions, and authorization requirements;
9. preserve the distinction between linguistic evidence and system behavior;
10. add no hidden linguistic argument, category, relation, or causal explanation;
11. receive a recorded semantic-equivalence review before participant use.

A rewrite that fails equivalence review is excluded or revised before evaluation. It is not scored as evidence against the original text.

See [[Claim-Evidence Matrix]], [[Terminology Control]], and [[Normative Language]].

## Decision outcomes

The final test-run disposition must be one of:

### `adopt`

Use when the tested controls improve interpretation or review without material semantic loss and without unacceptable authoring or checker burden.

### `revise`

Use when benefits are limited to specific document classes, claim classes, terms, or rules; or when correctable semantic, cohesion, authoring, or tooling problems remain.

### `stop`

Use when the tested controls provide no meaningful reader benefit, create material semantic drift, impose unacceptable burden, or produce false confidence that cannot be corrected within a bounded profile.

Exact numeric thresholds, sample sizes, exclusion rules, and statistical models must be fixed in the final study protocol before data collection. They must not be selected after inspecting outcomes. See [[Quality Metrics and Acceptance Gates]].

## Non-goals

This baseline does not:

- rewrite any selected Canto-span text;
- declare a final SLE-GE profile;
- certify that any linguistic analysis is true;
- change Canto-span identity, status, evidence, runtime behavior, readiness, workflow, release state, or authorization;
- make SLE conformance equivalent to linguistic validity;
- require adoption before evaluation;
- treat a proxy artifact as an original document class;
- generalize results beyond the sampled materials and participant groups.

## Blockers and deviations

The following test-run findings are recorded in issue #11:

- DEV-010 — local `gh` workflow unavailable;
- DEV-011 — no pilot-baseline template;
- DEV-012 — no standard cross-repository source-pinning rule;
- DEV-013 — no rare-stratum sampling guidance;
- DEV-014 — no branch-aware vault validator;
- DEV-015 — connector limitation for patching large existing notes;
- DEV-016 — no standalone release-note artifact located.

These deviations must be included in authoring-cost and infrastructure-burden analysis. A platform limitation must not be misclassified as an SLE language-design failure.

## Change control

- Baseline version 0.1 is locked when the PR for issue #2 is merged.
- A correction before paired rewriting begins requires a documented version increment.
- After rewriting begins, the selected materials and reader questions cannot change within the same study wave.
- A source that disappears remains identified by its frozen commit path and recorded metadata.
- A proxy can be replaced with an original artifact only through a baseline amendment before rewriting begins.

## Related SLE notes

- [[Canto-span Case Study]]
- [[Canto-span A-not-A Worked Example]]
- [[Evaluation Framework]]
- [[Pilot Study Design]]
- [[Quality Metrics and Acceptance Gates]]
- [[Claim-Evidence Matrix]]
- [[Terminology Control]]
- [[Normative Language]]
- [[Profiles and Conformance]]
- [[Governance and Change Control]]
- [[Versioning and Release Model]]
- [[Vault Validation Report]]
