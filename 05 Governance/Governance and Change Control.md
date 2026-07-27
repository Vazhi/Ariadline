---
title: "Governance and Change Control"
type: governance
status: revised
created: 2026-07-27
updated: 2026-07-27
tags:
  - sle
  - governance
  - change-control
---
# Governance and Change Control

## Purpose

Governance protects the meaning, neutrality, usability, auditability, and version history of the SLE for Linguistics reference artifact.

A project inconvenience, software limitation, or one-domain preference does not by itself justify a normative change.

Conformance semantics are defined in [[Profiles and Conformance]]. Exact profile mappings are controlled by [[SLE Profile Applicability Register v0.1]].

## Governance roles

### Maintainer group

Responsibilities:

- manage public editions;
- maintain rule, pattern, term, profile, and decision registers;
- prevent undocumented normative changes;
- publish compatibility and migration information;
- distinguish the controlling reference text from optional supporting products.

### Linguistics review group

Include reviewers from multiple subfields, theoretical traditions, methods, languages, and scholarly communities.

Responsibilities:

- identify theory- or method-specific bias;
- review definitions, rules, patterns, examples, omissions, and profile mappings;
- determine whether a problem is general, domain-specific, or local;
- protect necessary linguistic distinctions.

### Author, editor, and reader group

Include authors, editors, annotators, translators, non-native English users, community researchers, and readers with different expertise levels.

Responsibilities:

- report comprehension and consistency problems;
- test author meaning preservation and authoring burden;
- evaluate document patterns and waivers;
- test whether profiles resolve to the same rule set;
- test whether conformance results are distinguished from review methods and evaluation activities;
- propose profile, translation, accessibility, or publisher needs.

Tool developers may contribute optional implementation feedback. Tool feasibility is not a criterion for normative adoption.

## Rule, pattern, and profile states

Use these states:

- **proposed** — drafted for evaluation;
- **revised** — changed after evidence or evaluation;
- **stable** — accepted into a published controlling edition;
- **deprecated** — still recognized but discouraged or scheduled for removal;
- **retired** — no longer normative and retained for history.

A proposed or revised item must not be described as established SLE practice.

A profile-set version controls an exact rule mapping. Changing that mapping is a normative change and must receive a compatibility classification.

## Change process

1. Submit [[SLE Change Request Template|a change request]].
2. Identify affected rules, patterns, terms, profile mappings, conformance results, review methods, evaluation types, translations, examples, and annexes.
3. State the communication problem and its scope.
4. Provide independent evidence, examples, and alternatives appropriate to the proposed change.
5. Test reader benefit, author meaning preservation, authoring burden, theory neutrality, method neutrality, profile reconstruction, conformance interpretation, and translation effects as applicable.
6. Record dissent, uncertainty, and unresolved risks.
7. Record the decision in [[Decision Log]].
8. Update the human reference text and all controlling registers before release.
9. Publish compatibility and migration guidance under [[Versioning and Release Model]].

Optional tools and machine-readable exports may be updated after the controlling reference text. They do not define the normative decision.

## Decision record

A decision record must state:

- issue and affected identifiers;
- current rule, pattern, or profile mapping;
- proposed alternatives;
- evidence and exact source locations;
- evaluation results and exact evaluated scope;
- selected action;
- dissent or uncertainty;
- theory, method, language, translation, accessibility, profile, conformance, and authoring-burden risks where relevant;
- compatibility effect;
- required migration;
- review date and responsible role.

## Generalization gate

A finding can motivate a core normative rule or pattern only when it describes a recurring communication problem with independent support beyond one project, one language, one theory, one method, or one publication venue.

A narrower finding may support:

- an optional profile;
- an informative annex;
- a publisher or community extension;
- a worked example;
- no SLE change.

Canto-span-specific findings can inform a later adoption guide. They cannot become core SLE requirements without independent justification.

## Conflict-of-framework rule

A change must not present one theoretical framework, analytical ontology, evidence source, research workflow, rhetorical order, or evaluation method as neutral when the control depends on it.

A necessary framework-specific control belongs in a declared extension or informative example unless independent review supports a broader formulation.

## Conformance governance

A conformance result records whether the applicable communication controls are met.

A review method records who checked the text.

A typed evaluation record describes a specific evaluation and its exact scope or sample.

Governance must prevent these three records from being collapsed into a single level or badge.

A review or evaluation cannot by itself create a passing conformance result. An unresolved applicable nonconformity must remain visible.

## Profile governance

A profile declaration must identify a profile-set version and resolve to exact rule IDs.

A profile change must state:

- prior and new rule mappings;
- conditional-rule changes;
- effect on prior conformance results;
- migration requirement;
- whether a new optional profile is preferable to changing an existing profile.

Two declarations using the same profile and profile-set version must refer to the same candidate rule set.

## Waiver governance

A waiver permits a bounded departure from an applicable communication control. It does not amend SLE.

A material waiver record must identify:

- affected rule or pattern element;
- affected document scope;
- reason;
- interpretation or consistency risk;
- mitigation;
- approval when required;
- review or expiry condition.

Repeated waivers must trigger review. The review may conclude that:

- the rule or pattern needs revision;
- a domain extension is needed;
- the local practice is nonconforming but justified;
- no change is appropriate.

A waiver must not conceal an unsupported claim, missing evidence, ethical problem, method defect, data conflict, or theoretical disagreement.

## Extension governance

An extension must identify:

- controlling SLE version;
- controlling profile-set version;
- responsible publisher, community, or project;
- local requirements and their justification;
- added, replaced, or excluded rule IDs;
- affected patterns;
- compatibility with core SLE;
- declaration method;
- review and retirement process.

Local terminology and document types must be labelled as local.

## Public record

Publish as appropriate:

- change requests;
- decisions;
- rule, pattern, and profile histories;
- deprecated and retired controls;
- compatibility and migration guidance;
- evaluation summaries with bounded scope;
- accepted extensions.

Personal, confidential, restricted, or community-controlled research data must remain outside the public record unless disclosure is authorized.
