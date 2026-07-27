---
title: "Profiles and Conformance"
type: implementation
status: revised
created: 2026-07-27
updated: 2026-07-27
aliases:
  - "Conformance"
  - "SLE Profile"
tags:
  - sle
  - implementation
  - conformance
  - profiles
---
# Profiles and Conformance

## Purpose

Conformance states whether a declared document or document part meets the applicable communication controls in a stated SLE for Linguistics version.

Conformance does not certify linguistic truth, theoretical correctness, methodological validity, ethical adequacy, speaker acceptability, or software quality.

The proposed document patterns are in [[SLE for Linguistics Document Patterns v0.1]]. The exact profile-to-rule mappings are in [[SLE Profile Applicability Register v0.1]]. The controlling rule text is in [[SLE for Linguistics Language Rules v0.1]].

## Conformance object

The conformance object must be identifiable. It can be:

- a complete document;
- a named section or chapter;
- an annotation guideline;
- a set of entries;
- a resource guide;
- another bounded text artifact.

Conformance does not automatically extend to an entire project, repository, dataset, theory, research program, publication series, or software system.

## Human-readable conformance is sufficient

Basic conformance does not require:

- YAML or another machine-readable header;
- repository metadata;
- a checker;
- a software schema;
- a public termbase;
- a project-specific workflow.

A document can establish its conformance result through ordinary prose and a human review record.

# Profiles

Profiles select exact rule groups. They do not define linguistic theories, methods, document genres, or scientific quality.

A profile name is auditable only when the declaration identifies the profile-set version in [[SLE Profile Applicability Register v0.1]] and resolves the conditional rules for the declared text.

## SLE-Core

Applies the general controls for principal messages, reference, scope, terminology, comparison, logical relations, stable navigation, limitations, claim-support connections, and the conformance-versus-truth boundary.

## SLE-Research

Adds rules for judgments, examples, datasets, tool behavior, observation and interpretation, evidence force, bounded negative claims, and interlinear glossing when applicable.

## SLE-Resource

Adds rules for example provenance, dataset and transformation identity, tool behavior, bounded negative claims, and interlinear glossing when applicable.

## SLE-Procedure

Adds rules for declared normative verbal forms, conditions before actions, and one principal action per procedural step.

## Relationship between profiles and patterns

A profile selects rule IDs. A pattern organizes a communicative purpose.

Examples:

- a corpus study can use `SLE-Research` with `SLE-PATTERN-0004`;
- an annotation guide can use `SLE-Procedure` and `SLE-Research` with `SLE-PATTERN-0007`;
- a resource guide can use `SLE-Resource` with `SLE-PATTERN-0010`;
- a theoretical article can use `SLE-Research` with `SLE-PATTERN-0003`.

A document may use a pattern without declaring a profile. A project or publisher extension may define a profile combination, but it must preserve the exact core rule mappings or declare its incompatibility.

# Conformance result

A conformance result is separate from the method used to review the text.

## Conforms

Use **conforms** only when:

- the conformance object is identified;
- the SLE version and applicable rule set are identified;
- every applicable requirement is met;
- no unresolved applicable nonconformity remains;
- any declared extension is compatible with the stated result.

## Conforms with declared waivers

Use **conforms with declared waivers** only when:

- every applicable unmet control is covered by a valid material waiver;
- the waiver scope, reason, risk, and mitigation are recorded;
- no unwaived applicable nonconformity remains.

A content limitation, missing evidence, ethical problem, method defect, data conflict, or theoretical disagreement is not a communication waiver.

## Does not conform

Use **does not conform** when one or more applicable requirements are not met and are not covered by valid waivers.

The result may include a corrective-action record. It must not imply that the linguistic content is false.

## Not determined

Use **not determined** when the applicable rule set, review scope, evidence, or review process is incomplete or unclear.

A self-review, independent review, or evaluation may still have occurred. The process record does not replace the result.

# Review method

The review method records who checked the applicable controls. It is not a conformance level.

## Author self-review

The author checked the declared conformance object against the resolved rule set and pattern elements.

## Independent editorial review

A human reviewer who did not author the reviewed passage checked the resolved rule set and pattern elements.

## Other declared review method

A publisher, community, collaborative, or specialist review method may be used when its roles and independence are stated.

Every review record should identify:

- reviewer role;
- review date;
- exact conformance object;
- exact applicable rule set or a stable applicability record;
- findings, waivers, and unresolved issues;
- resulting conformance result.

# Typed evaluation records

An evaluation record is separate from conformance and review. Different evaluation types are not interchangeable and do not form a hierarchy.

Permitted evaluation types include:

- reader-comprehension evaluation;
- author meaning-preservation evaluation;
- translation or localization evaluation;
- accessibility evaluation;
- domain-expert evaluation;
- theory-neutrality evaluation;
- method-neutrality evaluation;
- genre-combination or authoring-burden evaluation.

Each evaluation record must identify:

1. evaluation type;
2. exact document scope, passages, or sample;
3. method and task;
4. participant or evaluator role;
5. date;
6. findings and limitations;
7. any change proposed because of the findings.

An evaluation of representative passages applies only to those passages or to the explicitly justified inference from that sample. It must not make the entire document appear evaluated.

An evaluation result does not automatically change the conformance result. A resulting edit or newly discovered nonconformity must be recorded through the ordinary review process.

# Optional conformance declaration

A declaration may use ordinary prose. It should identify:

- SLE reference version;
- conformance object;
- profile-set version and profile or profiles, or the exact rule IDs;
- applicable document-pattern IDs;
- conformance result;
- review method;
- stable review or applicability record when the rule list is not written locally;
- material extensions and waivers;
- review date;
- controlling terminology source when required for interpretation.

Typed evaluations should be listed separately with their exact scope.

Example:

> Sections 2–4 conform with declared waivers to SLE for Linguistics v0.1. The review used SLE-PROFILE-SET-0.1, SLE-Research, and SLE-PATTERN-0004. The conditional-rule decisions and two material waivers are listed in Appendix A. Review method: independent editorial review. Review date: 2026-07-27. A reader-comprehension evaluation covered only paragraphs 2.3–2.5 and is recorded separately.

A declaration must not imply that SLE verified the content's truth or scientific quality.

# Waivers

A material waiver must identify:

1. affected rule or pattern element;
2. affected text or scope;
3. reason;
4. interpretation or consistency risk;
5. mitigation or alternative control;
6. approval when required by a declared extension;
7. review or expiry condition when appropriate.

A waiver addresses communication conformance. It must not hide missing evidence, a method defect, an ethical problem, a theoretical disagreement, or an unresolved data conflict.

# Extensions

A local extension must:

- identify the SLE version and profile-set version it extends;
- distinguish local requirements from SLE requirements;
- list added, replaced, or excluded rule IDs;
- preserve core distinctions or declare an incompatibility;
- avoid presenting one theory, language, method, or workflow as universal;
- define how a document declares the extension.

# Optional tools

A tool may assist terminology, cross-reference, or editorial review.

A tool result is not a conformance result, review method, or evaluation type. Tool availability is not required for ordinary SLE conformance.
