---
title: "SLE for Linguistics Language Rules v0.1"
type: normative-draft
status: proposed
version: "0.1"
created: 2026-07-27
updated: 2026-07-27
tags:
  - sle
  - language-rules
  - normative-draft
  - linguistics
---
# SLE for Linguistics Language Rules v0.1

## Status and purpose

This document is the first prose-first normative draft for the SLE for Linguistics reference specification.

The rules are proposed requirements and recommendations. They are not yet a published standard. A rule can become stable only after cross-domain review and human evaluation under [[Evaluation Framework]].

SLE controls how linguistic content is communicated. SLE conformance does not establish that a claim is true, theoretically correct, ethically acceptable, or methodologically sound.

The evidence basis is recorded in [[Independent SLE Rule Evidence Register v0.1]]. Decisions about optional claim functions are recorded in [[Claim Function Decision Register v0.1]].

## Draft-local normative verbal forms

This draft uses the following verbal forms so that its own rule statements are internally consistent:

- **must** states a proposed requirement;
- **must not** states a proposed prohibition;
- **should** states a proposed recommendation that can have a documented exception;
- **should not** states a discouraged practice;
- **may** states permission;
- **can** states capability or factual possibility.

This is a draft-local editorial convention, not a final decision that all SLE-conforming documents must use **must** rather than **shall** or another declared requirement form. ISO practice uses **shall** for requirements, while IETF BCP 14 permits **MUST** and **SHALL** as requirement terms. SLE-RULE-0008 therefore controls declared meaning and consistency. The final preferred requirement form remains an evaluation question.

## Rule format

Each rule contains a stable rule ID, normative text, rationale, examples, exceptions or boundaries, an editorial check, and an evidence reference.

Visible claim labels are not required. Authors may use optional labels during drafting or review.

# A. Sentence, reference, and terminology

## SLE-RULE-0001 — One principal message

**Rule:** Each sentence must have one identifiable principal assertion, question, or instruction.

A sentence may contain a condition, qualification, or contrast when that material is necessary to interpret the principal message.

**Noncompliant**

> The construction occurs in the corpus, is infrequent, may be limited to older speakers, and therefore is not productive.

**Compliant**

> The construction occurs in the corpus. It is infrequent in this dataset. The current data suggest a possible age restriction. The data do not establish that the construction is unproductive.

**Exception:** A conventional definition or tightly integrated contrast may contain more than one clause when the relation is unambiguous.

**Editorial check:** Ask what single message the reader must retain. Rewrite when two independent answers are possible.

**Evidence:** ER-01, ER-04; exact locators and evidence type are in the evidence register.

## SLE-RULE-0002 — Clear reference

**Rule:** A pronoun, demonstrative, or other referring expression must identify one intended antecedent in the local context.

**Noncompliant**

> The suffix follows the clitic, but it is optional.

**Compliant**

> The suffix follows the clitic. The suffix is optional.

**Exception:** A pronoun may remain when agreement or local context makes only one antecedent possible.

**Editorial check:** Replace the expression with each plausible antecedent. Rewrite when more than one replacement produces a coherent reading.

**Evidence:** ER-01, ER-04.

## SLE-RULE-0003 — Scope of generalization

**Rule:** A generalization must identify the population, language variety, register, dataset, time period, or other domain that limits the claim.

A scope statement must be near the claim that it limits.

**Noncompliant**

> Cantonese has five examples of this form.

**Compliant**

> In the stated HKCanCor release and query, the search returned five tokens of this form.

**Exception:** A section-level scope statement may govern multiple claims when no local scope change occurs.

**Editorial check:** Ask where, for whom, in which data, and under which conditions the claim is intended to hold.

**Evidence:** ER-06, ER-07, ER-08, ER-09.

## SLE-RULE-0004 — Stable preferred term

**Rule:** A document must use one preferred term for one controlled concept.

A writer must not alternate technical synonyms only for stylistic variety.

**Noncompliant**

> The construction, pattern, format, and template are productive.

**Compliant**

> The construction is productive.

**Exception:** A historical term, quotation, or external label may appear when its relationship to the preferred term is explicit.

**Editorial check:** Search for competing labels and confirm that each has a distinct meaning or an explicit equivalence statement.

**Evidence:** ER-01, ER-04, ER-08.

## SLE-RULE-0005 — Defined technical term

**Rule:** A technical term must be defined before it is used in a conformance-critical or claim-critical passage, unless the document links to a controlling definition.

A definition must state the relevant scope and distinguishing criteria.

**Noncompliant**

> The form is productive.

**Compliant**

> In this study, *productive* means that speakers extend the pattern to novel eligible verbs in the stated task.

**Exception:** A broadly established term may remain undefined when no competing interpretation affects the claim.

**Editorial check:** Ask whether a reader from another linguistic subfield could apply the term consistently.

**Evidence:** ER-01, ER-04, ER-08.

## SLE-RULE-0006 — Explicit comparison

**Rule:** A comparative claim must identify the compared items, the comparison dimension, and the relevant measure or basis.

**Noncompliant**

> Form A is more acceptable.

**Compliant**

> Participants gave Form A a higher mean rating than Form B in Task 2.

**Exception:** A table heading may supply an element when the relationship is immediate and unambiguous.

**Editorial check:** Answer “more or less than what, on which measure?”

**Evidence:** ER-06, ER-07; the exact three-part control remains a proposed SLE formulation.

## SLE-RULE-0007 — Clear logical scope

**Rule:** The scope of negation, quantification, restriction, and exception must be unambiguous.

**Noncompliant**

> The participants did not rate all examples.

**Compliant**

> No participant rated every example.

or

> Some examples received no rating.

**Exception:** Defined formal notation may carry the scope when the prose states how to read it.

**Editorial check:** Paraphrase the sentence with explicit quantifier and negation order.

**Evidence:** ER-01, ER-04; the paraphrase test is an SLE-local editorial method.

# B. Procedures and normative text

## SLE-RULE-0008 — Declared normative verbal forms

**Rule:** A normative document must declare the verbal forms that express requirements, prohibitions, recommendations, permissions, and capabilities, or link to a controlling declaration.

Within that declared system, one form must not be used for two different normative functions when the difference affects conformance.

SLE v0.1 does not yet require **must** rather than **shall**. The final SLE requirement form must be selected only after comparison and reader evaluation.

**Noncompliant**

> The guide uses *can* sometimes for permission and sometimes for capability without defining either use.

**Compliant**

> In this guide, *must* states a requirement, *should* states a recommendation, *may* states permission, and *can* states capability.

or

> This guide uses the declared ISO verbal forms, including *shall* for requirements.

**Exception:** A quotation preserves source wording.

**Editorial check:** Classify every normative verb by function and confirm that the declared mapping is consistent.

**Evidence:** ER-01, ER-03, ER-11. The choice between **must** and **shall** remains a proposed design decision, not direct source inheritance.

## SLE-RULE-0016 — Condition before action

**Rule:** In an instruction, a condition that determines whether an action applies must appear before the action or in a clearly labelled applicability statement.

**Noncompliant**

> Assign the label X if the token is a clitic.

**Compliant**

> If the token is a clitic, assign the label X.

**Exception:** A short table may place conditions and actions in separate labelled columns.

**Editorial check:** Confirm that a reader encounters the applicability condition before acting.

**Evidence:** ER-01, ER-06; ordering is a proposed control for evaluation.

## SLE-RULE-0017 — One action per instruction

**Rule:** A procedural step should require one principal action.

Actions that form one inseparable operation may remain together in their required order.

**Noncompliant**

> Segment the token, assign the feature bundle, correct the source text, and update the adjudication log.

**Compliant**

> 1. Segment the token.  
> 2. Assign the feature bundle.  
> 3. Record any source-text correction.  
> 4. Update the adjudication log.

**Editorial check:** Ask whether one action can fail or be skipped independently of another action.

**Evidence:** ER-01, ER-06, ER-10; the independence test is an SLE-local hypothesis.

# C. Claims, evidence, and scope

## SLE-RULE-0009 — Attestation does not establish stronger properties

**Rule:** A document must not infer productivity, frequency, acceptability, or grammatical status from attestation alone.

**Noncompliant**

> The corpus contains the form, so the pattern is productive.

**Compliant**

> The form is attested in this corpus. A separate analysis or test is required to evaluate productivity.

**Editorial check:** Identify the additional evidence needed for the stronger claim.

**Evidence:** ER-06, ER-07, ER-08 provide the general evidence-boundary problem. The specific attestation distinction is an SLE-local linguistic hypothesis for cross-domain testing.

## SLE-RULE-0010 — Judgment method

**Rule:** A reported speaker or annotator judgment must identify enough information for the reader to interpret the result, including the task, response format, relevant population, item scope, and reported result when those elements apply.

**Noncompliant**

> Speakers accept the sentence.

**Compliant**

> In the five-point rating task, 18 of 22 eligible participants rated Sentence 12 as 4 or 5.

**Exception:** A compact table may provide the information through headings and a methods reference.

**Editorial check:** Confirm that a reader can determine what response was collected, from whom, for which items, and by which procedure.

**Evidence:** ER-06 and ER-07 support method and population reporting. The exact judgment fields are proposed SLE guidance pending fieldwork and experimental-linguistics review.

## SLE-RULE-0015 — System behavior is not a language fact

**Rule:** A statement about software output must identify the relevant system, version or state, input, and configuration when those details affect the result.

A writer must not present system behavior alone as direct evidence of speaker knowledge, acceptability, or language structure.

**Noncompliant**

> The sentence is an A-not-A question because the parser labels it A_NOT_A.

**Compliant**

> Parser P at version 2.1 labels the input as A_NOT_A under Configuration C. This result describes parser behavior and does not establish the linguistic analysis.

**Editorial check:** Replace “the language” with “the system” and confirm whether the statement remains accurate.

**Evidence:** ER-06, ER-07, ER-08, ER-10 support system and data identification. The language-fact boundary is an SLE-local cross-domain hypothesis.

## SLE-RULE-0019 — Observation separate from interpretation

**Rule:** A document must distinguish a directly recorded result from an interpretation of that result.

The distinction may appear in separate sentences, clauses, headings, or table columns.

**Noncompliant**

> The three tokens demonstrate a grammatical rule.

**Compliant**

> The query returned three tokens. Under Analysis A, these tokens are compatible with the proposed rule.

**Editorial check:** Identify which words report the record and which add an analytical inference.

**Evidence:** ER-06, ER-07, ER-10; the exact prose separation remains a proposed control.

## SLE-RULE-0020 — Evidence wording does not overstate force

**Rule:** Evidence wording must not state a stronger relation between evidence and conclusion than the declared method, assumptions, and support justify.

SLE v0.1 does not define a universal hierarchy for *shows*, *supports*, *suggests*, *is consistent with*, *does not establish*, or *contradicts*. Their force can vary by discipline and argument type. A document should define an evidence term when its interpretation is important and not clear from context.

**Noncompliant**

> Three corpus tokens prove that the construction is productive.

**Compliant**

> Three corpus tokens establish that the form is attested in this corpus. These tokens do not by themselves establish productivity.

**Exception:** *Prove* may be used for a formal proof or a method that explicitly licenses that conclusion.

**Editorial check:** State the inference in neutral terms, list reasonable alternatives, and verify that the chosen verb does not erase those alternatives.

**Evidence:** ER-07 directly requires claims to be adequately supported. The lexical hierarchy from the earlier draft is withdrawn and deferred for evaluation.

## SLE-RULE-0021 — Bounded negative claim

**Rule:** A claim that a form, pattern, result, or effect was not found must state the search or test space and a relevant sensitivity limit.

**Noncompliant**

> The construction does not occur.

**Compliant**

> The query found no tokens in Corpus C, release 3. The query does not detect spelling variants outside the normalization list.

**Exception:** A formal proof of nonexistence follows the relevant formal conventions.

**Editorial check:** Identify what was searched or tested and what the method could have missed.

**Evidence:** ER-06, ER-07, ER-10; the sensitivity statement is a proposed SLE control.

## SLE-RULE-0022 — Limitations and counterevidence

**Rule:** A document must state a known limitation or material counterexample when omission could change the interpretation of a central claim.

The statement must identify which claim is affected and how its scope or strength changes.

**Noncompliant**

> The analysis covers the construction.

**Compliant**

> The analysis covers affirmative matrix clauses. It does not cover embedded clauses or negative forms.

**Editorial check:** Ask whether a reasonable reader would otherwise make a broader inference.

**Evidence:** ER-07; the local attachment requirement is a proposed SLE control.

## SLE-RULE-0023 — Claim-support connection

**Rule:** A central claim must identify its supporting evidence or analysis through local prose, a citation, a stable identifier, a table or figure reference, or another explicit cross-reference.

A reader must not have to infer which evidence supports which claim.

**Noncompliant**

> The construction is productive. Several results appear below.

**Compliant**

> The nonce-word results in Table 4 support the productivity claim for the tested verb class.

**Editorial check:** Point from each central claim to the exact supporting record.

**Evidence:** ER-05, ER-06, ER-07; the local-mapping rule is a proposed SLE control.

# D. Linguistic examples and data

## SLE-RULE-0011 — Example provenance dimensions

**Rule:** When provenance affects interpretation, a linguistic example must identify the relevant provenance dimensions. The dimensions are independent and multiple descriptors may apply to one example.

Use these dimensions as applicable:

1. **Source or origin:** published source, corpus record, participant response, author-created item, or system-produced item.
2. **Collection context:** naturally occurring, corpus-extracted, elicited, experimental, introspective, or otherwise specified.
3. **Modification status:** unchanged, orthographically normalized, resegmented, adapted, reconstructed, translated, or otherwise modified.
4. **Production method:** participant-produced, author-written, template- or rule-produced, or produced by a named software system or model.

A **system-produced item** is output created by a named software system or model. This descriptor does not by itself state whether the item is attested, acceptable, or analytically valid.

**Noncompliant**

> (12) The child goed home.

The reader cannot tell whether this is a participant response, an author-created stimulus, or a cited attestation.

**Compliant**

> (12) The child goed home. [author-created experimental item; unchanged]

or

> (12) ... [participant response in elicitation task E3; orthography normalized]

or

> (12) ... [adapted from Source S; lexical item replaced; segmentation revised]

**Editorial check:** Record origin, collection context, modification, and production method separately. Do not force the example into one exclusive category.

**Evidence:** ER-02 establishes that glosses are analytical and may be modified; ER-04 and ER-05 support declared conventions. The four-dimensional model is an SLE-local proposal for evaluation.

## SLE-RULE-0012 — Defined judgment notation

**Rule:** A document that uses judgment symbols or category labels must define their meanings or link to a controlling definition.

A document must not assume that `*`, `?`, `??`, and `#` have identical meanings across publications.

**Editorial check:** Ask what task, population, or analytical convention licenses each symbol.

**Evidence:** ER-02 and ER-04 show field-specific convention and variation. The explicit task/population check remains proposed guidance.

## SLE-RULE-0013 — Stable example identifier

**Rule:** A central linguistic example, dataset item, table, or figure must have a stable identifier when the document refers to it more than once.

A reference should use the identifier rather than only a relative expression such as *the example above*.

**Noncompliant**

> The example above shows the alternation.

**Compliant**

> Example (12) shows the alternation.

**Editorial check:** Confirm that the reference remains valid after material is inserted, removed, or reordered.

**Evidence:** ER-01, ER-05, ER-08.

## SLE-RULE-0014 — Dataset and transformation identity

**Rule:** A claim based on a dataset or language resource must identify the dataset, relevant version or access state, and material preprocessing, exclusion, normalization, or transformation steps.

**Noncompliant**

> We used the corpus and removed bad data.

**Compliant**

> We used Dataset D, release 2. We excluded files without speaker metadata and normalized Unicode to NFC before tokenization.

**Editorial check:** Ask whether a reader can identify the input data and the changes made before analysis.

**Evidence:** ER-06, ER-08, ER-09, ER-10.

## SLE-RULE-0024 — Interlinear glossing declaration

**Rule:** A document that uses interlinear morpheme-by-morpheme glosses must follow the Leipzig Glossing Rules or declare an alternative convention.

Project-specific abbreviations must be defined. Object-language material, segmentation, glossing, and translation must remain distinguishable.

**Exception:** A document may omit a layer when the omission suits its purpose and is not misleading. The Leipzig rules themselves permit declared flexibility and alternative conventions.

**Editorial check:** Confirm alignment, abbreviation definitions, omitted layers, and the analytical status of segmentation and glosses.

**Evidence:** ER-02, especially “About the rules,” “Preamble,” and Rule 1.

# E. Conformance boundary

## SLE-RULE-0018 — Conformance does not certify truth

**Rule:** A conformance statement must not imply that SLE has verified the truth, acceptability, grammaticality, theoretical correctness, ethical adequacy, or methodological validity of the linguistic content.

**Compliant**

> This report conforms to SLE for Linguistics v0.1 for claim scope and example provenance. The conformance statement does not validate the analysis.

**Editorial check:** Confirm that the statement refers only to declared communication requirements.

**Evidence:** ER-03, ER-06, ER-07. The full linguistic-truth boundary is an SLE-local safeguard.

# Non-rules and deferred controls

The following controls are not normative in v0.1:

- a fixed maximum sentence length;
- a universal active-voice requirement;
- a universal ban on passive voice or nominalization;
- mandatory visible claim-class labels;
- mandatory machine-readable headers;
- mandatory software checking;
- a universal evidence-verb hierarchy;
- a universal linguistic ontology;
- Canto-span terminology, statuses, or governance practices.

# Claim functions

The draft recognizes recurring communicative functions but does not require visible codes in normal prose. See [[Claim Function Decision Register v0.1]].

# Theoretical and methodological neutrality

These rules do not require a specific theory of grammar, definition of grammaticality, evidence method, language identifier, annotation schema, or software workflow.

A document must state its own assumptions, methods, and scope when those choices affect interpretation.

# Next evaluation

The next phase must test:

1. whether readers identify claims, support, and limitations more consistently;
2. whether authors preserve intended meaning;
3. whether rules create unnecessary repetition or fragmentation;
4. whether the rules work across descriptive, theoretical, experimental, corpus, fieldwork, lexicographic, annotation, signed-language, community-based, and computational documents;
5. whether **must**, **shall**, or another declared requirement form produces the clearest conformance judgments;
6. whether evidence verbs require profile-specific definitions;
7. whether the four example-provenance dimensions are sufficient and non-overlapping;
8. whether any rule creates English-specific or theory-specific bias.

The non-normative [[Canto-span Pilot Termbase v0.1]] may be used as one later stress test. It must not supply normative justification.
