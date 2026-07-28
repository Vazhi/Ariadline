---
title: "Ariadline Reference Artifact v0.1 Draft"
type: reference-artifact-draft
status: proposed
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - ariadline
  - reference-artifact
  - normative-draft
  - publication
---
# Ariadline Reference Artifact v0.1 Draft

## Status

This is the assembled **proposed** Ariadline reference artifact. It is a human-readable publication draft, not a stable standard.

The draft can be used for editorial review and evaluation. It must not be represented as an established international, publisher, community, or disciplinary standard.

Ariadline controls communication form. Ariadline conformance does not establish linguistic truth, grammaticality, theoretical correctness, methodological validity, ethical adequacy, translation quality, accessibility, software correctness, or community authority.

## How this publication works

This page is the publication front door. It does not duplicate every controlling rule or pattern.

When two package components appear inconsistent, use this authority order:

1. [[Ariadline Language Rules v0.1]] controls normative rule wording.
2. [[Ariadline Document Patterns v0.1]] controls proposed document-pattern obligations and boundaries.
3. [[Profiles and Conformance]] controls conformance results, review methods, typed evaluations, waivers, and extensions.
4. [[Ariadline Profile Applicability Register v0.1]] controls exact profile-to-rule mappings.
5. [[Governance and Change Control]] and [[Versioning and Release Model]] control change and compatibility decisions.
6. [[Glossary]] is an informative guide to package usage. It does not create obligations or universal linguistic definitions.
7. Indexes, examples, checklists, validation records, case studies, and annexes support interpretation but do not override the controlling modules.

The complete component classification is in [[Ariadline Reference Publication Map v0.1]].

## 1. Purpose

Ariadline is a proposed controlled form of English for linguistic description, evidence reporting, research documentation, editorial review, and related technical communication.

Its purpose is to help readers reconstruct:

- the principal claim or instruction;
- the intended scope;
- the declared terminology;
- the relation between evidence and analysis;
- the status and provenance of examples and data;
- uncertainty, alternatives, limitations, and counterevidence;
- the relationship between a document and its applicable communication controls.

The project mission and success condition are in [[Project Charter]].

## 2. Scope, audience, and non-goals

The initial scope is English prose used in descriptive, documentary, corpus, annotation, computational, methodological, and cross-subfield linguistic communication.

Primary users include authors, editors, reviewers, annotators, terminology managers, translators, research groups, publishers, and readers outside the author's immediate subfield. See [[Users and Use Cases]].

Ariadline does not:

- define a universal linguistic theory;
- require one analysis for disputed phenomena;
- determine whether a linguistic claim is true;
- replace peer review, ethics review, community authority, translation review, accessibility testing, or software testing;
- prohibit necessary technical terms;
- replace the Leipzig Glossing Rules;
- require a repository, schema, tool, checker, parser, linter, or machine-readable file;
- make Canto-span or another project the model for linguistic writing.

The detailed boundary is in [[Scope and Non-Goals]].

## 3. Basic writing principles

The package applies these principles:

1. Preserve necessary linguistic precision.
2. Control ambiguity rather than intellectual complexity.
3. Keep communicative functions distinguishable.
4. Use stable terminology for declared concepts.
5. State the scope that limits a claim.
6. Match evidence wording to the declared support.
7. Preserve theoretical and methodological plurality.
8. Adopt only controls that can be reviewed and evaluated.
9. Maintain rule, evidence, test, and change traceability.
10. Give human readability priority over machine convenience.

The design record is in [[Design Principles]].

## 4. Normative verbal forms

The proposed rule draft uses **must** for a proposed requirement, **must not** for a proposed prohibition, **should** for a recommendation with a possible documented exception, **may** for permission, and **can** for capability or factual possibility.

This draft-local convention does not require every conforming document to choose **must** rather than **shall**. A normative document must declare and consistently apply its own function mapping under `SLE-RULE-0008`.

## 5. Language rules

The controlling 24-rule chapter is [[Ariadline Language Rules v0.1]]. The compact publication index is [[Ariadline Rule and Pattern Index v0.1]].

### Sentence, reference, and terminology

The rules cover one principal message, clear reference, bounded generalization, stable preferred terms, defined technical terms, explicit comparisons, and clear logical scope.

### Evidence, analysis, and conclusions

The rules distinguish attestation from stronger properties, observation from interpretation, system behavior from language facts, and bounded support from overstatement. They also require material limitations, counterevidence, negative-claim boundaries, and explicit claim-support connections.

### Data, examples, translations, glosses, and citations

The rules cover judgment methods, orthogonal example-provenance dimensions, judgment notation, stable identifiers, dataset and transformation identity, and declared interlinear-glossing conventions.

Ariadline does not certify example acceptability, translation quality, segmentation, gloss analysis, citation correctness, or scientific sufficiency. Those require separately scoped authority.

### Procedures

Procedure controls cover declared normative verbal forms, conditions before actions, and one principal action per step, subject to the stated recommendation boundary.

## 6. Document patterns

The controlling pattern chapter is [[Ariadline Document Patterns v0.1]].

The 14 proposed patterns cover:

- descriptive grammar;
- construction or phenomenon descriptions;
- theoretical analysis;
- corpus studies;
- elicitation and judgment studies;
- fieldwork notes and data commentary;
- annotation guidelines;
- lexicographic entries;
- computational-linguistics system descriptions;
- language-resource documentation;
- methods and procedures;
- research summaries;
- limitation and open-question records;
- editorial changes and revision notes.

Pattern sequences are recommended defaults. A different rhetorical order can conform when applicable information relationships and distinctions remain recoverable.

Reusable outlines and examples are in [[Ariadline Document Pattern Outlines v0.1]] and [[Ariadline Document Pattern Example Bank v0.1]].

## 7. Profiles and applicability

Profiles select exact rule groups. They do not define theories, methods, genres, or scientific quality.

The proposed profiles are `SLE-Core`, `SLE-Research`, `SLE-Resource`, and `SLE-Procedure`.

A profile declaration is auditable only when it identifies the profile-set version and resolves conditional applicability. [[Ariadline Profile Applicability Register v0.1]] controls the exact mappings.

## 8. Editorial conformance

[[Ariadline Editorial Conformance Checklist v0.1]] provides one human-review question for each rule.

Final item outcomes are:

- **Pass**;
- **Fail**;
- **Not applicable**;
- **Justified exception**;
- **Waived**;
- **Not determined**.

**Borderline** is a provisional review flag. It must resolve before review completion.

A declared conformance object receives one result:

- **conforms**;
- **conforms with declared waivers**;
- **does not conform**;
- **not determined**.

Conformance result, review method, and typed evaluation record are separate.

## 9. Exceptions, waivers, and extensions

An exception exists only when the controlling rule or recommendation provides the boundary.

A waiver is a visible bounded departure from an applicable communication control. It must identify scope, reason, risk, mitigation, approval when required, and review condition. It cannot conceal missing evidence, a method defect, an ethical problem, a theoretical disagreement, or a data conflict.

An extension must identify the controlling Ariadline and profile-set versions, distinguish local requirements, list affected rule IDs, and state compatibility.

## 10. Human-review boundary

[[Human Review Boundary Register v0.1]] separates editorial communication review from substantive authority.

An editor may determine whether declared content is communicated under applicable Ariadline controls. The editor must not use the Ariadline result to certify truth, grammaticality, theory, method, ethics, translation, accessibility, software, or community authorization.

When a proposed edit could change authorized meaning, use [[Ariadline Semantic Equivalence Review Template v0.1]]. If legitimate meaning authority is unavailable, record **not determined**.

## 11. Examples and internal audit material

[[Ariadline Rule Test Case Catalog v0.1]] contains constructed pass, fail, provisional borderline, and typed boundary prompts.

[[Multi-Domain Ariadline Evaluation Corpus v0.1]] is a constructed internal audit corpus. Its controlled alternatives match project-constructed briefs in internal review, but independent preservation remains **not determined**.

These materials do not establish effectiveness, authentic multilingual coverage, or rule validity.

## 12. Evidence and traceability

Independent source analysis is in [[Independent Ariadline Rule Evidence Register v0.1]].

Exact rule-to-rationale, checklist, case, and audit-prompt mappings are in [[Ariadline Rule Traceability Matrix v0.1]].

The current evidence and constructed prompts justify an auditable proposed draft. They do not justify stabilization. Missing authentic, multilingual, full-document, community-governed, translation, accessibility, and independently reviewed glossing evidence remains visible.

For issue #8 assembly, every proposed rule must have auditable independent rationale and exact traceability. Independent cross-domain justification sufficient for stable normative status remains a separate stabilization gate. This assembly does not waive or satisfy that stronger requirement.

## 13. Governance and revision

[[Governance and Change Control]] defines roles, change requests, evidence requirements, evaluation, dissent, decision records, profile governance, waiver governance, and extensions.

A normative change requires independent support beyond one project, language, theory, method, or venue.

[[Versioning and Release Model]] classifies changes by compatibility effect:

- **major** changes can change prior conformance outcomes;
- **minor** changes are backward-compatible additions;
- **patch** changes do not change intended obligations or review outcomes.

The current rejected and deferred proposals are recorded in [[Ariadline Reference Change and Deferral Log v0.1]].

## 14. Terminology

The informative publication glossary is [[Glossary]]. It summarizes package usage and does not create universal linguistic definitions.

A local project may define specialized terms differently when it declares the definition, scope, and relation to external terminology. Local terminology must not be presented as universal Ariadline terminology.

## 15. Normative and informative components

The package distinguishes:

- controlling proposed normative modules;
- conformance and governance modules;
- controlled review support;
- informative terminology and authoring aids;
- validation and evaluation records;
- non-authoritative case studies and stress tests.

The detailed status of every component is in [[Ariadline Reference Publication Map v0.1]].

## 16. Canto-span boundary

Canto-span is not a normative source, gold standard, profile, terminology authority, repository requirement, or conformance model for Ariadline.

[[Canto-span Evaluation Subset v0.1]], [[Canto-span Case Study]], and related fixtures are informative, non-authoritative stress tests only. A Canto-span finding can affect core Ariadline only through the ordinary independent-evidence and governance process.

## 17. Optional tooling and project documentation

Software is optional. [[Optional Automation Notes for Ariadline Review v0.1]] describes limited flagging and review assistance.

A tool cannot create a conformance result, establish authorized meaning, confirm semantic preservation, or certify substantive content.

Project-management documentation is outside the core linguistic document patterns. It may be addressed through informative annexes or local extensions without becoming a universal Ariadline requirement.

## 18. Draft readiness and remaining gates

This package is ready for substantive publication review as a coherent proposed draft.

It is not ready for stabilization or broad effectiveness claims. Remaining gates include:

- authentic independent author passages;
- non-English-original and translated material;
- independently reviewed meaning preservation;
- community-governed contributions;
- full-document and mixed-pattern evaluation;
- direct interlinear-glossing evaluation;
- reader comprehension and authoring-burden studies;
- theory, method, translation, accessibility, and rhetorical-order evaluation;
- naming and acronym review before public release.
