---
title: "Ariadline Document Patterns v0.1"
type: normative-draft
status: proposed
version: "0.1"
created: 2026-07-27
updated: 2026-07-27
tags:
  - ariadline
  - document-patterns
  - conformance
  - linguistics
---
# Ariadline Document Patterns v0.1

## Status and purpose

This chapter proposes human-readable document patterns for the Ariadline reference specification.

A document pattern is a communication structure. It is not a mandatory file schema, repository layout, research method, linguistic theory, or software data model.

The patterns organize information so that readers can distinguish data, observation, analysis, hypothesis, system behavior, limitation, and conclusion when those distinctions are relevant. They apply the proposed rules in [[Ariadline Language Rules v0.1]].

All patterns in v0.1 remain **proposed**. They require cross-domain author and reader evaluation before stabilization.

## Authority boundary

The patterns are designed for linguistic writing generally.

They do not derive from Canto-span terminology, governance, repository structure, parser workflow, or document types. The non-normative [[Canto-span Pilot Termbase v0.1]] may later supply one bounded test case only.

Project-management documents such as pull-request summaries and release notes are outside the core patterns. An optional project-documentation annex may address them later.

## How to use a pattern

1. Select the pattern that matches the document's principal communicative purpose.
2. Add another pattern when the document has a second substantial purpose.
3. Treat each listed sequence as a recommended default, not a mandatory English rhetorical order.
4. Use another order when it better supports comprehension or a field, language, publisher, or scholarly tradition.
5. Preserve the required information relationships and distinctions even when headings, sequence, or formatting differ.
6. Omit an element only when it is inapplicable, supplied by an immediate cross-reference, or unnecessary for the stated purpose.
7. Record a waiver only when an applicable required relationship or distinction is intentionally absent and the absence can affect interpretation.

Reordering alone does not require a waiver when the required information remains recoverable.

A journal article, grammar chapter, dictionary entry, dataset guide, or annotation manual can combine patterns. Combining patterns does not require duplicating the same information.

## Shared information relationships and recommended sequence

Most Ariadline documents should make the following information recoverable. The order below is a recommended default:

1. **Purpose or question** — what the document, section, or entry addresses.
2. **Scope** — language, variety, population, register, dataset, time, document part, or operational domain.
3. **Material and method** — what was examined or done.
4. **Direct result or instruction** — what was observed, produced, decided, or required.
5. **Interpretation or rationale** — how the author understands the result or requirement.
6. **Boundaries** — limitations, alternatives, counterevidence, exceptions, and unresolved questions.
7. **Support and navigation** — citations, identifiers, examples, tables, figures, or cross-references.

Conformance depends on the recoverability of applicable relationships, not on copying this sequence or its headings.

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
- state relevant provenance dimensions under `SLE-RULE-0011`;
- define judgment symbols and project-specific gloss abbreviations;
- distinguish object-language material from segmentation, glossing, translation, and analysis;
- identify adaptations that can affect interpretation;
- connect central claims to exact supporting examples, tables, figures, or sources.

## Shared uncertainty and alternatives practice

A document must state uncertainty, alternatives, or counterevidence when omission could cause a reader to interpret a central claim as broader or stronger than intended.

The author may state these locally, in a limitations section, in an alternatives section, or through an explicit cross-reference. A distant generic disclaimer does not replace a limitation that materially changes a specific claim.

# Pattern catalogue

Each **recommended sequence** below can be reordered. The listed distinctions and applicable information relationships are the conformance-relevant elements.

## SLE-PATTERN-0001 — Descriptive grammar section

**Purpose:** Describe a form, category, construction, or distribution in a language or variety.

**Recommended sequence:** phenomenon and scope; diagnostics; form and distribution; meaning or function; examples and provenance; variation and exceptions; relation to nearby phenomena; unresolved questions.

**Required distinctions:** observation versus analytical category; attested distribution versus grammatical possibility; synchronic description versus historical explanation; language-wide versus bounded claim.

**Editorial checks:** Identify language and variety; expose assumptions; bound generalizations; show counterexamples and uncertain cases.

**Permitted omissions:** Method details may be supplied by an immediate cross-reference. Theory discussion may be omitted when no theory-dependent claim is made.

## SLE-PATTERN-0002 — Construction or phenomenon description

**Purpose:** Give a bounded account of one linguistic pattern, alternation, process, or phenomenon.

**Recommended sequence:** working name and scope; observable form; inclusion and exclusion criteria; examples and contrasts; proposed interpretation; evidence for stronger properties; negative boundaries; unresolved cases.

**Required distinctions:** name versus definition; identification versus explanation; attestation versus productivity, frequency, acceptability, or grammatical status; core cases versus edge cases.

**Editorial checks:** Make the candidate set reproducible; state excluded interpretations; support stronger claims separately; preserve uncertain classifications.

**Permitted omissions:** Full theoretical analysis may be deferred to `SLE-PATTERN-0003` through an immediate cross-reference.

## SLE-PATTERN-0003 — Theoretical analysis

**Purpose:** Present an explanation, formalization, derivation, model, or argument under stated assumptions.

**Recommended sequence:** question; assumptions and notation; empirical target; proposed analysis; reasoning; predictions; alternatives and counterarguments; bounded conclusion.

**Required distinctions:** empirical record versus representation; framework-internal consequence versus language-independent fact; assumption versus derived result; compatibility versus unique support.

**Editorial checks:** Define framework terms; identify assumptions; bound the conclusion; represent serious alternatives accurately.

**Permitted omissions:** A well-defined framework may be incorporated by citation when local departures remain explicit.

## SLE-PATTERN-0004 — Corpus study report

**Purpose:** Report a search, sample, annotation, quantitative analysis, or qualitative analysis of corpus material.

**Recommended sequence:** question and scope; corpus identity and composition; query and sampling; transformations and exclusions; annotation; direct results; analysis; sensitivity limits; bounded conclusion.

**Required distinctions:** corpus versus target population; query result versus language frequency; token count versus productivity; annotation versus source form; search absence versus language nonexistence.

**Editorial checks:** Identify exact input and transformations; provide denominators; account for exclusions and uncertain cases; state search sensitivity.

**Permitted omissions:** Stable method records may be cross-referenced, but local deviations must remain visible.

## SLE-PATTERN-0005 — Elicitation or judgment study report

**Purpose:** Report speaker, participant, consultant, annotator, or expert responses collected through a stated task.

**Recommended sequence:** question and population; participant information; task and stimuli; response system; exclusions; direct responses; analysis; variation and task effects; bounded conclusion.

**Required distinctions:** response versus author classification; task behavior versus unrestricted language behavior; acceptability versus grammaticality, interpretation, preference, or familiarity; group summary versus individual pattern; missing response versus negative judgment.

**Editorial checks:** Identify the collected response, population, item scope, response categories, exclusions, and task boundary.

**Permitted omissions:** Protected participant details may be generalized when the privacy boundary and interpretive consequence are stated.

## SLE-PATTERN-0006 — Fieldwork note or data commentary

**Purpose:** Record a field observation, consultant session, text passage, elicitation result, analytical question, or provisional interpretation.

**Recommended sequence:** record identity and context; language and variety; consent and access boundary; recorded form and translation; prompt or collection context; later edits; analyst comments; follow-up questions.

**Required distinctions:** recorded utterance versus normalized transcription; participant versus analyst translation; spontaneous versus elicited production; contemporaneous note versus later interpretation; public versus restricted evidence.

**Editorial checks:** Identify direct record, later layers, uncertainty, and access limits.

**Permitted omissions:** Public versions may omit protected details without implying that no underlying metadata exists.

## SLE-PATTERN-0007 — Annotation guideline

**Purpose:** Tell annotators how to identify units, apply labels, record uncertainty, and handle conflicts.

**Recommended sequence:** purpose and scope; unit and prerequisites; definitions and boundaries; decision procedure; positive and negative examples; uncertainty and abstention; escalation; quality review; version effects.

**Required distinctions:** source record versus annotation; label versus language fact; requirement versus recommendation; uncertainty versus negative classification; ordinary versus adjudicated decision.

**Editorial checks:** Put conditions before actions; test reproducibility; define overlap and priority; expose negative boundaries.

**Permitted omissions:** A glossary may be incorporated by reference when local overrides are stated.

## SLE-PATTERN-0008 — Lexicographic entry or lexical note

**Purpose:** Describe a lexical item, sense, form, usage, relation, or lexicographic decision.

**Recommended sequence:** form and identifier; language and variety; sense or function; grammatical and distributional information; usage labels; examples and citations; variants and relations; uncertainty or history.

**Required distinctions:** form versus sense; observed usage versus editorial recommendation; scoped usage labels; citation versus invented illustration; entry versus constructional analysis.

**Editorial checks:** Distinguish senses and labels; state label scope; connect examples to sense; stabilize variants and cross-references.

**Permitted omissions:** Fields outside the entry's purpose may be omitted.

## SLE-PATTERN-0009 — Computational-linguistics system description

**Purpose:** Describe a model, parser, classifier, pipeline, experiment, or tool and its evaluated behavior.

**Recommended sequence:** task and target use; linguistic and computational scope; data identity; system and configuration; comparison conditions; measures and direct results; error analysis; limitations; language-claim boundary.

**Required distinctions:** input representation versus language data; training objective versus linguistic theory; output versus speaker knowledge; held-out versus development observation; metric versus practical adequacy.

**Editorial checks:** Identify system state and data; state baselines; avoid model-label circularity; expose language, variety, domain, and dataset limits.

**Permitted omissions:** Withheld implementation details must carry an explicit reproducibility or interpretation limit.

## SLE-PATTERN-0010 — Language-resource documentation

**Purpose:** Document a corpus, lexicon, archive, treebank, annotation set, database, or reusable language resource.

**Recommended sequence:** purpose and identity; language and collection scope; source, consent, rights, and access; content and formats; annotation and transformations; quality and known issues; version and citation; intended and restricted uses.

**Required distinctions:** source versus derived representation; metadata absence versus inapplicability; resource versus language coverage; access permission versus ethical permission; release versus working state.

**Editorial checks:** Identify release and scope; document transformations; state rights and access; expose omissions and quality limits.

**Permitted omissions:** Protected metadata may be restricted when an access route and interpretive boundary are stated.

## SLE-PATTERN-0011 — Methods or procedure document

**Purpose:** Specify a repeatable linguistic research, transcription, annotation, review, or publication procedure.

**Recommended sequence:** purpose and applicability; prerequisites and roles; definitions and normative forms; conditions and actions; outputs; exceptions and escalation; quality criteria; version effects.

**Required distinctions:** mandatory step versus recommendation; condition versus action; method requirement versus rationale; completion versus scientific validity; exception versus rule change.

**Editorial checks:** Make applicability, actions, roles, failures, and escalation independently recoverable.

**Permitted omissions:** External protocols may control when their exact versions are identified.

## SLE-PATTERN-0012 — Research summary

**Purpose:** Give a concise account of a study, analysis, resource, debate, or evidence state.

**Recommended sequence:** subject and scope; question or purpose; proportionate method; principal direct result; interpretation; limitations and alternatives; route to full documentation.

**Required distinctions:** result versus interpretation; study finding versus field consensus; author versus cited conclusion; current evidence versus settled fact.

**Editorial checks:** Identify whose claim is summarized; retain material qualifiers; bound the conclusion; provide supporting navigation.

**Permitted omissions:** Detail may be omitted, but not a limitation that reverses or materially narrows the principal conclusion.

## SLE-PATTERN-0013 — Limitation and open-question record

**Purpose:** Record an unresolved boundary, evidence gap, conflict, risk, or future question without presenting it as resolved.

**Recommended sequence:** affected claim or artifact; limitation or question; current evidence; consequence; attempted alternatives; evidence needed; review state and next decision point.

**Required distinctions:** falsehood versus unresolved status; absence of evidence versus evidence of absence; local limitation versus general failure; workaround versus accepted behavior.

**Editorial checks:** Identify affected claim, practical consequence, required evidence, and workaround status.

**Permitted omissions:** A next action may be absent when evidence or responsibility is unknown, provided that absence is explicit.

## SLE-PATTERN-0014 — Editorial change or revision note

**Purpose:** Explain a change to linguistic wording, structure, examples, terminology, scope, or normative content.

**Recommended sequence:** artifact and version; prior state; new state; reason and evidence; meaning and compatibility effect; migration; unresolved risk or dissent.

**Required distinctions:** editorial correction versus normative change; wording change versus linguistic conclusion change; clarification versus migration-requiring change; accepted versus proposed revision.

**Editorial checks:** Identify exact change, prior-conformance effect, affected identifiers, and migration need.

**Permitted omissions:** A typographic correction may omit extended rationale only when it cannot affect meaning, data, cross-reference, or conformance.

# Conformance guidance

Detailed conformance guidance is in [[Profiles and Conformance]]. Exact profile mappings are in [[Ariadline Profile Applicability Register v0.1]].

## Conformance result

Use one result for the declared conformance object:

- **conforms**;
- **conforms with declared waivers**;
- **does not conform**;
- **not determined**.

The result records whether applicable communication controls are met. It is separate from review method and evaluation activity.

## Review method

Record whether the result came from author self-review, independent editorial review, or another defined human review method.

A review method does not imply a passing result.

## Typed evaluation record

Reader comprehension, author meaning preservation, translation, accessibility, domain-expert review, and other evaluations must be recorded separately by type.

Each record must identify its exact evaluated document scope or sample. Evaluation of representative passages must not be represented as evaluation of the whole document.

## Optional conformance declaration

A declaration should identify:

- Ariadline version;
- conformance object;
- profile-set version and profiles, or exact rule IDs;
- exact conditional-rule resolution or stable review record;
- pattern IDs;
- conformance result;
- review method;
- material waivers and extensions;
- review date.

Typed evaluations appear as separate records.

A declaration must not imply that Ariadline verified linguistic truth, speaker acceptability, ethical adequacy, statistical validity, or theoretical correctness.

## Waiver rule

A waiver permits a stated departure from an applicable communication control. It does not erase the control or create a precedent automatically.

A material waiver must identify the control, text scope, reason, risk, mitigation, approval when required, and review condition.

A waiver must not conceal a linguistic disagreement, unsupported claim, missing evidence, ethical problem, data conflict, or method defect.

## Extension rule

An extension must identify its controlling Ariadline and profile-set versions, distinguish local requirements, list affected rule IDs, preserve core distinctions or declare incompatibility, and define its declaration method.

## Versioning rule for patterns

Pattern IDs remain stable across versions. Version class follows compatibility effect:

- **major** — changes required distinctions or obligations in a way that can change prior conformance outcomes;
- **minor** — adds optional or backward-compatible material without changing prior conformance outcomes;
- **patch** — corrects wording or examples without changing intended normative meaning or review results.

A new mandatory obligation for an existing profile is not automatically minor.

# Editorial review checklist

For the selected pattern, confirm:

1. The purpose and conformance object are identifiable.
2. Scope is near the claims or instructions it limits.
3. Applicable information relationships are recoverable in an order suitable for the document's readers and tradition.
4. Data, observation, analysis, hypothesis, system behavior, limitation, and conclusion remain distinguishable where relevant.
5. Central claims connect to exact support.
6. Examples, glosses, judgments, and adaptations are interpretable.
7. Alternatives, counterevidence, and uncertainty are not hidden.
8. Omitted required relationships are inapplicable, cross-referenced, or covered by a recorded waiver.
9. Local extensions are not presented as universal Ariadline requirements.
10. The conformance result is separate from review method and evaluation records.
11. A conformance statement does not certify linguistic truth.

# Evaluation requirements before stabilization

Evaluation must include documents or passages from descriptive grammar, formal and functional theory, phonetics, corpus and historical linguistics, fieldwork, sociolinguistics, discourse and conversation analysis, lexicography, annotation, computational linguistics, language resources, signed-language research, and scholarly communities beyond English-dominant publishing.

The evaluation must test reader comprehension, author meaning preservation, authoring burden, theory neutrality, method neutrality, translation, accessibility, alternative rhetorical orders, profile auditability, and waiver proportionality.
