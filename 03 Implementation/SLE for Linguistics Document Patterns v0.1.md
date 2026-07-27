---
title: "SLE for Linguistics Document Patterns v0.1"
type: normative-draft
status: proposed
version: "0.1"
created: 2026-07-27
updated: 2026-07-27
tags:
  - sle
  - document-patterns
  - conformance
  - linguistics
---
# SLE for Linguistics Document Patterns v0.1

## Status and purpose

This chapter proposes human-readable document patterns for the SLE for Linguistics reference specification.

A document pattern is a communication structure. It is not a mandatory file schema, repository layout, research method, linguistic theory, or software data model.

The patterns organize information so that readers can distinguish data, observation, analysis, hypothesis, system behavior, limitation, and conclusion when those distinctions are relevant. They apply the proposed rules in [[SLE for Linguistics Language Rules v0.1]].

All patterns in v0.1 remain **proposed**. They require cross-domain author and reader evaluation before stabilization.

## Authority boundary

The patterns are designed for linguistic writing generally.

They do not derive from Canto-span terminology, governance, repository structure, parser workflow, or document types. Canto-span may later supply one non-authoritative test case.

Project-management documents such as pull-request summaries and release notes are outside the core patterns. An optional project-documentation annex may address them later.

## How to use a pattern

1. Select the pattern that matches the document's principal communicative purpose.
2. Add another pattern when the document has a second substantial purpose.
3. Follow the required information order unless another order is necessary for comprehension or a field convention.
4. Preserve the required distinctions even when headings or formatting differ.
5. Omit an element only when it is inapplicable, supplied by an immediate cross-reference, or unnecessary for the stated purpose.
6. Record a waiver when a required element is intentionally absent and the absence could affect interpretation.

A journal article, grammar chapter, dictionary entry, dataset guide, or annotation manual can combine patterns. Combining patterns does not require duplicating the same information.

## Shared information order

Most SLE documents should make the following sequence recoverable:

1. **Purpose or question** — what the document, section, or entry addresses.
2. **Scope** — language, variety, population, register, dataset, time, document part, or operational domain.
3. **Material and method** — what was examined or done.
4. **Direct result or instruction** — what was observed, produced, decided, or required.
5. **Interpretation or rationale** — how the author understands the result or requirement.
6. **Boundaries** — limitations, alternatives, counterevidence, exceptions, and unresolved questions.
7. **Support and navigation** — citations, identifiers, examples, tables, figures, or cross-references.

The exact headings are optional. The information relations are primary.

## Shared distinctions

An applicable pattern must preserve these distinctions when confusing them could change interpretation:

- recorded material versus analytical representation;
- observation versus interpretation;
- attestation versus a stronger claim such as productivity or grammatical status;
- participant or annotator response versus the author's conclusion;
- language behavior versus tool behavior;
- proposal or hypothesis versus accepted conclusion;
- requirement versus recommendation, permission, or capability;
- current coverage versus intended future coverage;
- source text versus normalization, adaptation, reconstruction, or translation;
- known limitation versus absence of investigation.

## Shared example and citation practices

When examples are central to a claim:

- use stable identifiers when an example is referenced more than once;
- state relevant provenance dimensions under SLE-RULE-0011;
- define judgment symbols and project-specific gloss abbreviations;
- distinguish object-language material from segmentation, glossing, translation, and analysis;
- identify adaptations that can affect interpretation;
- connect central claims to exact supporting examples, tables, figures, or sources.

## Shared uncertainty and alternatives practice

A document must state uncertainty, alternatives, or counterevidence when omission could cause a reader to interpret a central claim as broader or stronger than intended.

The author may state these locally, in a limitations section, in an alternatives section, or through an explicit cross-reference. A distant generic disclaimer does not replace a limitation that materially changes a specific claim.

# Pattern catalogue

## SLE-PATTERN-0001 — Descriptive grammar section

### Purpose

Describe a form, category, construction, or distribution in a language or variety.

### Expected information order

1. phenomenon and scope;
2. defining or diagnostic properties;
3. form and distribution;
4. meaning or function where relevant;
5. examples and provenance;
6. variation, restrictions, and exceptions;
7. relation to nearby phenomena and prior descriptions;
8. unresolved questions.

### Required distinctions

- descriptive observation versus analytical category;
- attested distribution versus claimed grammatical possibility;
- synchronic description versus historical explanation;
- language-wide claim versus variety-, register-, speaker-, or dataset-bounded claim.

### Minimum editorial checks

- Can a reader identify the described language and variety?
- Are diagnostics distinguished from definitions or assumptions?
- Does each broad generalization have an explicit domain?
- Are counterexamples, variation, and uncertain boundaries visible?

### Permitted omissions

A short grammar subsection may omit method details when the containing work states them and the cross-reference is immediate. A section need not discuss every competing theory when it makes no theory-dependent claim.

### Example

**Uncontrolled**

> The suffix marks plural and cannot occur with numerals.

**Controlled draft**

> In the recorded village variety, the suffix occurs with plural human nouns in Examples (14)–(19). No suffix-plus-numeral token occurred in the elicitation set. The current data do not establish that the combination is impossible.

## SLE-PATTERN-0002 — Construction or phenomenon description

### Purpose

Give a bounded account of one linguistic pattern, alternation, process, or phenomenon.

### Expected information order

1. working name and scope;
2. observable form or configuration;
3. inclusion and exclusion criteria;
4. attested examples and contrasts;
5. proposed interpretation;
6. productivity, frequency, acceptability, or variation evidence where claimed;
7. negative boundaries and competing analyses;
8. status of unresolved cases.

### Required distinctions

- name versus definition;
- identification criteria versus theoretical explanation;
- attestation versus productivity, frequency, acceptability, or grammatical status;
- core cases versus uncertain, lexicalized, historical, or superficially similar cases.

### Minimum editorial checks

- Could another analyst identify the same candidate set?
- Are excluded interpretations stated?
- Is a stronger claim supported by evidence beyond occurrence?
- Are edge cases classified without forcing a false binary?

### Permitted omissions

A phenomenon description may defer full theoretical analysis to SLE-PATTERN-0003 when it states that boundary explicitly.

## SLE-PATTERN-0003 — Theoretical analysis

### Purpose

Present an explanation, formalization, derivation, model, or argument under stated assumptions.

### Expected information order

1. analytical question;
2. assumptions, framework, and notation;
3. empirical target and scope;
4. proposed analysis;
5. derivation or reasoning;
6. predictions and supporting cases;
7. alternatives, counterarguments, and unresolved consequences;
8. conclusion limited to the stated assumptions.

### Required distinctions

- empirical record versus analytical representation;
- framework-internal consequence versus language-independent fact;
- assumption versus derived result;
- descriptive adequacy versus explanatory preference;
- compatibility with evidence versus unique support.

### Minimum editorial checks

- Are theory-specific terms defined or linked?
- Can the reader identify each assumption needed for a central inference?
- Does the conclusion exceed the tested empirical domain?
- Are serious alternatives represented accurately rather than as weaker paraphrases of the preferred analysis?

### Permitted omissions

A paper may assume a well-defined framework for its specialist audience when it cites the controlling formulation and identifies any local departure.

### Example

**Uncontrolled**

> The agreement pattern proves that the feature moves to C.

**Controlled draft**

> Under Analysis A, movement of the feature to C derives the agreement pattern in the tested matrix clauses. Analysis B can also generate these clauses through feature sharing. The present contrast does not distinguish the two analyses.

## SLE-PATTERN-0004 — Corpus study report

### Purpose

Report a search, sample, annotation, quantitative analysis, or qualitative analysis of corpus material.

### Expected information order

1. research question and claim scope;
2. corpus identity, release, access state, and relevant composition;
3. query, sampling, preprocessing, and exclusion procedures;
4. annotation or coding method;
5. direct counts, examples, or distributions;
6. analysis and uncertainty;
7. sensitivity limits, missing data, and alternative explanations;
8. bounded conclusion and reproducibility information.

### Required distinctions

- corpus composition versus target population;
- query result versus language frequency;
- token count versus type productivity;
- annotation decision versus observed source form;
- absence in the search result versus nonexistence in the language.

### Minimum editorial checks

- Can a reader identify the exact input corpus and material transformations?
- Is the denominator available for every reported proportion?
- Are duplicate, uncertain, and excluded cases accounted for?
- Does a negative claim state what the search could miss?

### Permitted omissions

A short report may link to a stable method or dataset record instead of repeating full procedures. The local report must still state deviations that affect the result.

## SLE-PATTERN-0005 — Elicitation or judgment study report

### Purpose

Report speaker, participant, consultant, annotator, or expert responses collected through a stated task.

### Expected information order

1. research question and population scope;
2. participant or consultant description relevant to interpretation;
3. task, stimuli, context, and response system;
4. exclusions and quality controls;
5. direct responses or summary results;
6. analysis and uncertainty;
7. individual variation, task effects, and limitations;
8. conclusion bounded to the participants and method.

### Required distinctions

- participant response versus author classification;
- task behavior versus unrestricted language behavior;
- acceptability, grammaticality, interpretation, preference, and familiarity;
- group summary versus individual pattern;
- missing response versus negative judgment.

### Minimum editorial checks

- Is the collected response identifiable?
- Are population, item scope, and response categories stated?
- Are exclusions and nonresponses visible?
- Does the prose avoid converting a task-specific result into an unqualified speaker claim?

### Permitted omissions

Confidential participant details may be generalized or withheld. The report must state the privacy boundary and retain enough information to interpret the result.

## SLE-PATTERN-0006 — Fieldwork note or data commentary

### Purpose

Record a field observation, consultant session, text passage, elicitation result, analytical question, or provisional interpretation.

### Expected information order

1. date or session identity and communicative context where appropriate;
2. language and variety;
3. source or participant record and consent boundary;
4. recorded form and translation;
5. collection context and prompt where relevant;
6. analyst comments and uncertainty;
7. follow-up questions or verification needs;
8. access restrictions and citation conditions.

### Required distinctions

- recorded utterance versus normalized transcription;
- participant translation versus analyst translation;
- spontaneous production versus elicited response;
- contemporaneous note versus later interpretation;
- public evidence versus restricted or confidential material.

### Minimum editorial checks

- Can the reader tell what was directly recorded?
- Are later edits or analytical layers visible?
- Is uncertainty preserved rather than silently resolved?
- Are consent and access limits respected?

### Permitted omissions

Public versions may omit names, exact locations, sensitive cultural information, or restricted media references. The omission should not falsely imply that the underlying metadata never existed.

## SLE-PATTERN-0007 — Annotation guideline

### Purpose

Tell annotators how to identify units, apply labels, record uncertainty, and handle conflicts.

### Expected information order

1. annotation purpose and scope;
2. unit of annotation and prerequisites;
3. label definitions and decision boundaries;
4. ordered decision procedure;
5. positive, negative, and boundary examples;
6. uncertainty, abstention, and escalation procedure;
7. quality review and adjudication process;
8. version and change effects.

### Required distinctions

- source record versus annotation;
- descriptive label versus language fact;
- requirement, recommendation, permission, and capability;
- annotator uncertainty versus negative classification;
- ordinary decision versus adjudicated exception.

### Minimum editorial checks

- Does each instruction identify its condition before the action?
- Can two annotators apply each label to the same examples?
- Are overlapping labels, priority rules, and abstention cases defined?
- Are examples sufficient to expose the negative boundary?

### Permitted omissions

A guideline may link to a controlled label glossary. It must state local overrides and version-dependent behavior.

## SLE-PATTERN-0008 — Lexicographic entry or lexical note

### Purpose

Describe a lexical item, sense, form, usage, relation, or lexicographic decision.

### Expected information order

1. lemma or form and identifier;
2. language, variety, script, pronunciation, and morphology as relevant;
3. sense or function definition;
4. grammatical and distributional information;
5. usage labels and scope;
6. examples and citations;
7. semantic relations, variants, and cross-references;
8. uncertainty, historical notes, or editorial decisions.

### Required distinctions

- form versus sense;
- observed usage versus editorial recommendation;
- dialect, register, frequency, offensiveness, obsolescence, and domain labels;
- citation evidence versus invented illustration;
- lexical entry versus broader constructional analysis.

### Minimum editorial checks

- Can users distinguish each sense and usage label?
- Are labels defined and supported by an explicit scope?
- Are examples representative of the stated sense rather than only grammatical?
- Are variants and cross-references stable?

### Permitted omissions

The pattern does not require every dictionary field. A project may omit etymology, pronunciation, frequency, or translations when outside its purpose.

## SLE-PATTERN-0009 — Computational-linguistics system description

### Purpose

Describe a model, parser, classifier, pipeline, experiment, or tool and its evaluated behavior.

### Expected information order

1. task and target use;
2. linguistic and computational scope;
3. data identity and transformations;
4. system architecture or relevant components;
5. training, configuration, and comparison conditions;
6. evaluation measures and direct results;
7. error analysis, limitations, and population or language coverage;
8. distinction between system behavior and linguistic conclusion.

### Required distinctions

- input representation versus language data;
- training objective versus linguistic theory;
- system output versus speaker knowledge or language structure;
- held-out evaluation versus development observation;
- performance measure versus practical adequacy.

### Minimum editorial checks

- Are system state, data, configuration, and evaluation conditions identifiable?
- Are baselines and comparison measures explicit?
- Does the text avoid treating a model label as proof of a linguistic category?
- Are language, variety, domain, and dataset limitations stated?

### Permitted omissions

Proprietary or security-sensitive implementation details may be withheld. The report must state the resulting reproducibility or interpretation limit.

## SLE-PATTERN-0010 — Language-resource documentation

### Purpose

Document a corpus, lexicon, archive, treebank, annotation set, database, or reusable language resource.

### Expected information order

1. resource purpose and persistent identity;
2. language, variety, community, genre, time, and collection scope;
3. source and consent or rights conditions;
4. content, structure, formats, and identifiers;
5. annotation, normalization, and transformation history;
6. quality review and known issues;
7. version, access, citation, and compatibility information;
8. limitations and intended or prohibited uses.

### Required distinctions

- source material versus derived representation;
- metadata absence versus inapplicability;
- resource coverage versus language coverage;
- access permission versus ethical permission;
- current release versus mutable working state.

### Minimum editorial checks

- Can a user identify the exact release and content scope?
- Are transformations and annotation layers documented?
- Are rights, consent, and access conditions clear?
- Are known omissions and quality limits discoverable?

### Permitted omissions

Sensitive metadata may be restricted. A public record may point to an access process without exposing protected information.

## SLE-PATTERN-0011 — Methods or procedure document

### Purpose

Specify a repeatable linguistic research, transcription, annotation, review, or publication procedure.

### Expected information order

1. purpose and applicability;
2. prerequisites, materials, and roles;
3. definitions and normative verbal forms;
4. ordered conditions and actions;
5. expected outputs and decision records;
6. exception, waiver, and escalation paths;
7. quality review and completion criteria;
8. version and compatibility effects.

### Required distinctions

- mandatory step versus recommendation;
- condition versus action;
- method requirement versus explanatory rationale;
- successful completion versus scientific validity;
- ordinary exception versus rule change.

### Minimum editorial checks

- Can a qualified reader determine when each step applies?
- Is each principal action independently verifiable?
- Are responsibilities and handoffs explicit where needed?
- Are failure, uncertainty, and escalation outcomes defined?

### Permitted omissions

A procedure may refer to an external safety, ethics, or technical protocol. The local document must state which version controls the work.

## SLE-PATTERN-0012 — Research summary

### Purpose

Give a concise account of a study, analysis, resource, debate, or current evidence state.

### Expected information order

1. subject and scope;
2. principal question or purpose;
3. material and method in proportion to the summary's use;
4. principal direct result;
5. interpretation and significance;
6. limitations, uncertainty, and alternatives;
7. source or route to full documentation.

### Required distinctions

- result versus interpretation;
- study-specific finding versus field-wide consensus;
- author conclusion versus cited source conclusion;
- current evidence versus settled fact.

### Minimum editorial checks

- Can a reader identify whose result or claim is summarized?
- Are qualifiers removed only when they are genuinely immaterial?
- Is the conclusion no broader than the underlying work?
- Does the summary provide a route to supporting detail?

### Permitted omissions

A short abstract may omit procedural detail when the containing document supplies it. It must not omit a limitation that reverses or materially narrows the principal conclusion.

## SLE-PATTERN-0013 — Limitation and open-question record

### Purpose

Record an unresolved boundary, evidence gap, conflict, risk, or future research question without presenting it as a resolved claim.

### Expected information order

1. affected claim, resource, rule, or analysis;
2. observed limitation or unresolved question;
3. current evidence and what it does not establish;
4. consequence for scope, confidence, use, or conformance;
5. attempted alternatives or workarounds;
6. information needed for resolution;
7. review state and next decision point.

### Required distinctions

- known falsehood versus unresolved status;
- absence of evidence versus evidence of absence;
- local limitation versus general failure;
- temporary workaround versus accepted standard behavior.

### Minimum editorial checks

- Is the affected claim identifiable?
- Does the record state the practical consequence?
- Is the required resolution evidence explicit?
- Is a workaround prevented from silently becoming a rule?

### Permitted omissions

The record need not prescribe a next action when the necessary evidence or responsible party is unknown. It should state that absence directly.

## SLE-PATTERN-0014 — Editorial change or revision note

### Purpose

Explain a change to linguistic wording, structure, examples, terminology, scope, or normative content.

### Expected information order

1. changed artifact and version;
2. prior wording or state;
3. new wording or state;
4. reason and evidence;
5. meaning, scope, and compatibility effect;
6. migration or reader action where required;
7. unresolved risk, dissent, or follow-up review.

### Required distinctions

- editorial correction versus normative meaning change;
- changed wording versus changed linguistic conclusion;
- backward-compatible clarification versus migration-requiring change;
- accepted decision versus proposed revision.

### Minimum editorial checks

- Can a reader identify exactly what changed?
- Does the note state whether prior documents remain conformant?
- Is a scope or meaning change labelled rather than described as a typo?
- Are affected rule, term, pattern, and example identifiers listed?

### Permitted omissions

A patch-level typographic correction may omit extended rationale when it cannot affect meaning, cross-reference, data, or conformance.

# Conformance guidance

## Conformance object

Conformance applies to a declared document or document part. It does not automatically apply to an entire project, repository, publication series, dataset, theory, method, or software system.

## Proposed conformance states

### SLE-Prepared

The author applied the relevant proposed language rules and document pattern and completed a self-review.

This state does not require a public conformance declaration.

### SLE-Reviewed

A human reviewer who did not author the passage checked the applicable rules and pattern elements. The review record identifies material waivers and unresolved issues.

### SLE-Evaluated

The document or representative passages also underwent a defined reader, author-preservation, translation, or domain-expert evaluation.

SLE-Evaluated is an evaluation state, not a guarantee of linguistic truth or methodological quality.

Software output is not a conformance state. Optional tools may assist a human review.

## Optional conformance declaration

A declaration may use ordinary prose. It should identify:

- the SLE version;
- the document or part covered;
- the applicable pattern IDs;
- the conformance state;
- material waivers or extensions;
- the review date;
- any controlling terminology source when one is necessary for interpretation.

Example:

> Sections 2–4 were reviewed against SLE for Linguistics v0.1 using SLE-PATTERN-0004 and SLE-PATTERN-0012. SLE-RULE-0001 was waived for two conventional statistical model statements listed in Appendix A. The review was completed on 2026-07-27.

A declaration must not imply that SLE verified linguistic truth, speaker acceptability, ethical adequacy, statistical validity, or theoretical correctness.

## Waiver rule

A waiver permits a stated departure from a proposed or stable SLE control. It does not erase the rule or create a precedent automatically.

A material waiver must identify:

1. affected rule or pattern element;
2. affected text or document scope;
3. reason for the departure;
4. interpretation or consistency risk;
5. mitigation or alternative control;
6. approving role when the applicable profile requires approval;
7. review or expiry condition when appropriate.

A waiver must not be used to conceal a linguistic disagreement, unsupported claim, missing evidence, or method defect. Those matters must be stated as content limitations.

## Extension rule

A project, publisher, journal, community, or research group may define an extension for a documented need.

An extension must:

- identify the SLE version it extends;
- preserve core distinctions unless it states and justifies an incompatibility;
- distinguish required local conventions from SLE requirements;
- avoid presenting one theory, language, method, or workflow as universal;
- define how documents declare use of the extension.

## Versioning rule for patterns

Pattern IDs remain stable across versions. The version record states when a pattern is proposed, revised, stabilized, deprecated, or retired.

- A **major** change removes or changes a required distinction, changes the meaning of a conformance state, or makes previously conforming documents nonconforming.
- A **minor** change adds a pattern, optional element, example set, or backward-compatible requirement.
- A **patch** corrects wording, formatting, cross-references, or examples without changing intended normative meaning.

The public reference artifact must identify its version. Ordinary conforming documents do not require machine-readable version metadata.

# Editorial review checklist

For the selected pattern, confirm:

1. The purpose and conformance object are identifiable.
2. Scope is near the claims or instructions it limits.
3. The information order supports the reader's task.
4. Data, observation, analysis, hypothesis, system behavior, limitation, and conclusion remain distinguishable where relevant.
5. Central claims connect to exact support.
6. Examples, glosses, judgments, and adaptations are interpretable.
7. Alternatives, counterevidence, and uncertainty are not hidden.
8. Omitted pattern elements are inapplicable, cross-referenced, or covered by a recorded waiver.
9. Local extensions are not presented as universal SLE requirements.
10. A conformance statement, when present, does not certify linguistic truth.

# Evaluation requirements before stabilization

Evaluation must include documents or passages from:

- descriptive grammar and language documentation;
- formal and functional theoretical work;
- phonetics or laboratory phonology;
- corpus and historical linguistics;
- fieldwork and elicitation;
- sociolinguistics and discourse or conversation analysis;
- lexicography;
- annotation and language-resource documentation;
- computational linguistics;
- signed-language research;
- academic traditions and author communities that do not use English as their primary scholarly language.

The evaluation must test reader comprehension, author meaning preservation, authoring burden, theory neutrality, method neutrality, and the usefulness of permitted omissions.

The non-normative [[Canto-span Pilot Termbase v0.1]] may be used only as one later stress test. It cannot supply normative justification.