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

SLE controls how a linguistic claim is written. SLE conformance does not establish that the claim is true, theoretically correct, ethically acceptable, or methodologically sound.

The evidence basis for this draft is recorded in [[Independent SLE Rule Evidence Register v0.1]]. Decisions about optional claim functions are recorded in [[Claim Function Decision Register v0.1]].

## Normative verbal forms

In this document:

- **must** states a requirement for SLE conformance;
- **must not** states a prohibition;
- **should** states a recommendation that can have a documented exception;
- **should not** states a discouraged practice;
- **may** states permission;
- **can** states capability or factual possibility.

These meanings are local to SLE. They follow the consistency principle in [[Normative Language]], but SLE does not copy another standard's choice of requirement verb.

## Rule format

Each rule contains:

- a stable rule ID;
- normative text;
- scope and rationale;
- compliant and noncompliant examples;
- exceptions or boundary conditions;
- an editorial check;
- evidence references.

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

**Editorial check:** Ask what single message the reader must retain from the sentence. Rewrite when two independent answers are possible.

**Evidence:** ER-01, ER-02, ER-04.

## SLE-RULE-0002 — Clear reference

**Rule:** A pronoun, demonstrative, or other referring expression must identify one intended antecedent in the local context.

**Noncompliant**

> The suffix follows the clitic, but it is optional.

**Compliant**

> The suffix follows the clitic. The suffix is optional.

**Exception:** A pronoun may remain when grammatical agreement or local context makes only one antecedent possible.

**Editorial check:** Replace the referring expression with each plausible antecedent. Rewrite when more than one replacement produces a coherent reading.

**Evidence:** ER-01, ER-04.

## SLE-RULE-0004 — Stable preferred term

**Rule:** A document must use one preferred term for one controlled concept.

A writer must not alternate technical synonyms only for stylistic variety.

**Noncompliant**

> The construction, pattern, format, and template are productive.

**Compliant**

> The construction is productive.

**Exception:** A historical term, quoted term, or external label may appear when the relationship to the preferred term is explicit.

**Editorial check:** Search the document for competing labels and confirm that each label has a distinct meaning or an explicit equivalence statement.

**Evidence:** ER-01, ER-04, ER-08.

## SLE-RULE-0005 — Defined technical term

**Rule:** A technical term must be defined before the term is used in a conformance-critical or claim-critical passage, unless the document links to a controlling definition.

A definition must state the relevant scope and the criteria that distinguish the concept from nearby concepts.

**Noncompliant**

> The form is productive.

**Compliant**

> In this study, *productive* means that speakers extend the pattern to novel eligible verbs in the stated task.

**Exception:** A broadly established term may remain undefined when the document uses its ordinary field meaning and no competing interpretation affects the claim.

**Editorial check:** Ask whether a reader from another linguistic subfield could apply the term consistently.

**Evidence:** ER-01, ER-04, ER-08.

## SLE-RULE-0006 — Explicit comparison

**Rule:** A comparative claim must identify the compared items, the comparison dimension, and the relevant measure or basis.

**Noncompliant**

> Form A is more acceptable.

**Compliant**

> Participants gave Form A a higher mean rating than Form B in Task 2.

**Exception:** A table heading may supply one of these elements when the relationship is immediate and unambiguous.

**Editorial check:** Identify the answer to “more or less than what, on which measure?”

**Evidence:** ER-06, ER-07.

## SLE-RULE-0007 — Clear logical scope

**Rule:** The scope of negation, quantification, restriction, and exception must be unambiguous.

**Noncompliant**

> The participants did not rate all examples.

**Compliant**

> No participant rated every example.

or

> Some examples received no rating.

**Exception:** A formal expression may carry the scope when the notation is defined and the prose states how to read it.

**Editorial check:** Paraphrase the sentence with explicit quantifier and negation order.

**Evidence:** ER-01, ER-04.

# B. Procedures and normative text

## SLE-RULE-0016 — Condition before action

**Rule:** In an instruction, a condition that determines whether an action applies must appear before the action or in a clearly labelled applicability statement.

**Noncompliant**

> Assign the label X if the token is a clitic.

**Compliant**

> If the token is a clitic, assign the label X.

**Exception:** A short table may place conditions and actions in separate labelled columns.

**Editorial check:** Confirm that a reader encounters the applicability condition before acting.

**Evidence:** ER-01, ER-06.

## SLE-RULE-0017 — One action per instruction

**Rule:** A procedural step should require one principal action.

When actions must occur as one inseparable operation, the instruction may contain the necessary subactions in their required order.

**Noncompliant**

> Segment the token, assign the feature bundle, correct the source text, and update the adjudication log.

**Compliant**

> 1. Segment the token.  
> 2. Assign the feature bundle.  
> 3. Record any source-text correction.  
> 4. Update the adjudication log.

**Editorial check:** Ask whether one action can fail or be skipped independently of another action.

**Evidence:** ER-01, ER-06, ER-10.

## SLE-RULE-0008 — Consistent normative verbs

**Rule:** Normative text must use **must**, **must not**, **should**, **should not**, **may**, and **can** only with the meanings defined in this document.

A writer must not use **may** to mean capability or **can** to mean permission in normative text.

**Noncompliant**

> An annotator can omit this field with approval.

**Compliant**

> An annotator may omit this field with approval.

**Exception:** A quotation preserves the source wording.

**Editorial check:** Classify each modal as requirement, recommendation, permission, or capability.

**Evidence:** ER-01, ER-03.

# C. Claims, evidence, and scope

## SLE-RULE-0019 — Observation separate from interpretation

**Rule:** A document must distinguish a directly recorded result from an interpretation of that result.

The distinction may be expressed in separate sentences, clauses, headings, or table columns.

**Noncompliant**

> The three tokens demonstrate a grammatical rule.

**Compliant**

> The query returned three tokens. Under Analysis A, these tokens are compatible with the proposed rule.

**Editorial check:** Identify which words report the record and which words add an analytical inference.

**Evidence:** ER-06, ER-07, ER-10.

## SLE-RULE-0020 — Evidence verb matches force

**Rule:** A writer must select an evidence verb whose stated force does not exceed the relationship between the evidence and the conclusion.

Use these default distinctions:

- **shows**: the conclusion follows directly under the stated method and scope;
- **supports**: the evidence increases confidence but is not sufficient alone;
- **suggests**: the evidence provides preliminary reason for consideration;
- **is consistent with**: the evidence does not contradict the claim, and alternatives remain;
- **does not establish**: the evidence is insufficient for the conclusion;
- **contradicts**: the evidence conflicts with a stated prediction under the stated assumptions.

**Noncompliant**

> Three corpus tokens prove that the construction is productive.

**Compliant**

> Three corpus tokens show that the construction is attested in this corpus. The tokens do not establish productivity.

**Exception:** *Prove* may be used for a formal proof or a field-specific inferential procedure that licenses that term.

**Editorial check:** Ask whether a reasonable alternative explanation remains.

**Evidence:** ER-06, ER-07.

## SLE-RULE-0003 — Scope of generalization

**Rule:** A generalization must identify the population, language variety, register, dataset, time period, or other domain that limits the claim.

A scope statement must be near the claim that it limits.

**Noncompliant**

> Cantonese has five examples of this form.

**Compliant**

> In the stated HKCanCor release and query, the search returned five tokens of this form.

**Exception:** A section-level scope statement may govern multiple claims when no local scope change occurs.

**Editorial check:** Ask where, for whom, in which data, and under which conditions the statement is claimed to hold.

**Evidence:** ER-06, ER-07, ER-08, ER-09.

## SLE-RULE-0010 — Judgment method

**Rule:** A reported speaker or annotator judgment must identify the task, response scale or categories, participant or annotator population, item scope, and reported result.

**Noncompliant**

> Speakers accept the sentence.

**Compliant**

> In the five-point rating task, 18 of 22 eligible participants rated Sentence 12 as 4 or 5.

**Exception:** A compact table may provide the required information through linked headings and a methods reference.

**Editorial check:** Confirm that another reader can determine what response was collected and from whom.

**Evidence:** ER-06, ER-07.

## SLE-RULE-0021 — Bounded negative claim

**Rule:** A claim that a form, pattern, result, or effect was not found must state the search or test space and a relevant sensitivity limit.

**Noncompliant**

> The construction does not occur.

**Compliant**

> The query found no tokens in Corpus C, release 3. The query does not detect spelling variants outside the normalization list.

**Exception:** A formal proof of nonexistence follows the conventions of the relevant formal system.

**Editorial check:** Identify what was searched or tested and what the method could have missed.

**Evidence:** ER-06, ER-07, ER-10.

## SLE-RULE-0009 — Attestation is not productivity

**Rule:** A document must not infer productivity, frequency, acceptability, or grammatical status from attestation alone.

**Noncompliant**

> The corpus contains the form, so the pattern is productive.

**Compliant**

> The form is attested in this corpus. A separate test is required to evaluate productivity.

**Editorial check:** Identify the additional evidence required for the stronger claim.

**Evidence:** ER-06, ER-07, ER-08.

## SLE-RULE-0015 — System behavior is not a language fact

**Rule:** A statement about software output must identify the relevant system, version or state, input, and configuration when these details affect the result.

A writer must not present system behavior as direct evidence of speaker knowledge, acceptability, or language structure.

**Noncompliant**

> The sentence is an A-not-A question because the parser labels it A_NOT_A.

**Compliant**

> Parser P at version 2.1 labels the input as A_NOT_A under Configuration C. This result describes parser behavior and does not establish the linguistic analysis.

**Editorial check:** Replace “the language” with “the system” and confirm whether the claim remains accurate.

**Evidence:** ER-06, ER-07, ER-08, ER-10.

## SLE-RULE-0022 — Limitations and counterevidence

**Rule:** A document must state a known limitation or material counterexample when omitting it could change the interpretation of a central claim.

The statement must identify which claim is affected and how the limitation changes its scope or strength.

**Noncompliant**

> The analysis covers the construction.

**Compliant**

> The analysis covers affirmative matrix clauses. It does not cover embedded clauses or negative forms.

**Editorial check:** Ask whether a reasonable reader would make a broader inference without the limitation.

**Evidence:** ER-06, ER-07.

## SLE-RULE-0023 — Claim-support connection

**Rule:** A central claim must identify its supporting evidence or analysis through local prose, a citation, a stable example identifier, a table or figure reference, or another explicit cross-reference.

A reader must not have to infer which evidence supports which claim.

**Noncompliant**

> The construction is productive. Several results appear below.

**Compliant**

> The nonce-word results in Table 4 support the productivity claim for the tested verb class.

**Editorial check:** For each central claim, point to the exact supporting record.

**Evidence:** ER-01, ER-05, ER-06, ER-07.

# D. Linguistic examples and data

## SLE-RULE-0011 — Example provenance

**Rule:** A linguistic example must be identified as attested, constructed, adapted, elicited, or generated when the distinction affects interpretation.

An adapted example must state the material type of change.

**Noncompliant**

> (12) The child goed home.

**Compliant**

> (12) The child goed home. [constructed example]

or

> (12) ... [adapted from Source S; lexical item replaced]

**Editorial check:** Determine whether a reader could mistake the example for an unchanged attestation.

**Evidence:** ER-02, ER-04, ER-05.

## SLE-RULE-0012 — Defined judgment notation

**Rule:** A document that uses judgment symbols or category labels must define their meanings or link to a controlling definition.

A document must not assume that `*`, `?`, `??`, and `#` have identical meanings across publications.

**Editorial check:** Ask what task, population, or analytical convention licenses each symbol.

**Evidence:** ER-02, ER-04.

## SLE-RULE-0013 — Stable example identifier

**Rule:** A central linguistic example, dataset item, table, and figure must have a stable identifier when the document refers to it more than once.

A reference should use the identifier rather than only a relative expression such as *the example above*.

**Noncompliant**

> The example above shows the alternation.

**Compliant**

> Example (12) shows the alternation.

**Editorial check:** Confirm that the reference remains valid after material is inserted, removed, or reordered.

**Evidence:** ER-01, ER-02, ER-04, ER-05.

## SLE-RULE-0024 — Interlinear glossing declaration

**Rule:** A document that uses interlinear morpheme-by-morpheme glosses must follow the Leipzig Glossing Rules or declare the alternative convention.

Project-specific gloss abbreviations must be defined.

The object-language line, segmentation, gloss line, and translation must remain distinguishable.

**Exception:** A document may omit a layer when the omission is appropriate for its purpose and is not misleading.

**Editorial check:** Confirm line alignment, abbreviation definitions, and the status of any analytical segmentation.

**Evidence:** ER-02, ER-04.

## SLE-RULE-0014 — Dataset and transformation identity

**Rule:** A claim based on a dataset or language resource must identify the dataset, relevant version or access state, and material preprocessing, exclusion, normalization, or transformation steps.

**Noncompliant**

> We used the corpus and removed bad data.

**Compliant**

> We used Dataset D, release 2. We excluded files without speaker metadata and normalized Unicode to NFC before tokenization.

**Editorial check:** Ask whether a reader can identify the input data and the changes made before analysis.

**Evidence:** ER-06, ER-08, ER-09, ER-10.

# E. Conformance boundary

## SLE-RULE-0018 — Conformance does not certify truth

**Rule:** A conformance statement must not imply that SLE has verified the truth, acceptability, grammaticality, theoretical correctness, ethical adequacy, or methodological validity of the linguistic content.

**Compliant**

> This report conforms to SLE for Linguistics v0.1 for claim scope and example provenance. The conformance statement does not validate the analysis.

**Editorial check:** Confirm that the conformance statement refers only to declared communication requirements.

**Evidence:** ER-03, ER-06, ER-07.

# Non-rules and deferred controls

The following controls are not normative in v0.1:

- a fixed maximum sentence length;
- a universal requirement to use active voice;
- a universal ban on passive voice or nominalization;
- mandatory visible claim-class labels;
- mandatory machine-readable headers;
- mandatory software checking;
- a universal linguistic ontology;
- Canto-span terminology, statuses, or governance practices.

Long sentences, passive clauses, nominalizations, and visible labels may be useful or harmful depending on context. They remain editorial review topics until evaluation supports narrower rules.

# Claim functions

The draft recognizes recurring communicative functions, but it does not require visible codes in normal prose.

See [[Claim Function Decision Register v0.1]] for the decisions on `OBS`, `ATT`, `JUD`, `GEN`, `ANA`, `HYP`, `NEG`, `SYS`, `DEF`, `LIM`, `REQ`, `DEC`, and `STA`.

# Theoretical and methodological neutrality

These rules do not require:

- a specific theory of grammar;
- a specific definition of grammaticality or acceptability;
- corpus evidence for every claim;
- experiments for every claim;
- speaker judgments for every claim;
- a specific language identifier system;
- a specific annotation schema;
- a specific software workflow.

A document must state its own theoretical assumptions, evidence methods, and scope when those choices affect interpretation.

# Next evaluation

The next phase must test:

1. whether readers identify claims and limitations more consistently;
2. whether authors preserve intended meaning while applying the rules;
3. whether rules create unnecessary repetition or fragmentation;
4. whether the rules work across descriptive, theoretical, experimental, corpus, fieldwork, lexicographic, annotation, and computational documents;
5. whether any rule creates English-specific or theory-specific bias.

The non-normative [[Canto-span Pilot Termbase v0.1]] may be used as one later stress test. It must not supply normative justification.
