---
title: "SLE Editorial Conformance Checklist v0.1"
type: implementation
status: proposed
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - sle
  - conformance
  - editorial-checklist
  - human-review
---
# SLE Editorial Conformance Checklist v0.1

## Status and authority

This checklist translates the 24 proposed controls in [[SLE for Linguistics Language Rules v0.1]] into questions that a trained human reviewer can answer.

The checklist is support material for the proposed reference artifact. It does not create new rules, stabilize any rule, or replace the controlling rule text.

The checklist does not require software. Optional automation ideas are separated in [[Optional Automation Notes for SLE Review v0.1]].

## Required review record

Before applying the checklist, record:

- the bounded conformance object;
- the SLE version and profile-set version;
- the exact applicable rule IDs;
- the selected document pattern or patterns, if any;
- the review method;
- any declared waivers or extensions;
- the final result: **conforms**, **conforms with declared waivers**, **does not conform**, or **not determined**.

Use [[Profiles and Conformance]] and [[SLE Profile Applicability Register v0.1]] to define the review scope.

## Item outcomes

For each applicable rule, record one outcome:

- **Pass** — the applicable requirement is met.
- **Fail** — the applicable requirement is not met and no valid waiver covers it.
- **Borderline** — the reviewer can identify a plausible compliant and noncompliant reading; clarification or adjudication is required.
- **Not applicable** — the rule's applicability condition is not present.
- **Justified exception** — the controlling rule permits the stated exception and the exception does not mislead.
- **Waived** — a material unmet requirement is covered by a valid waiver under [[Profiles and Conformance]].
- **Not determined** — the reviewer lacks the scope, evidence, or authority needed to decide.

A recommendation expressed with **should** can pass with a documented justified exception. A requirement expressed with **must** cannot pass merely because the reviewer prefers the existing wording.

## Review discipline

1. Review the communication form, not the scientific truth.
2. Preserve the author's intended claim, evidential force, theoretical commitment, and uncertainty.
3. Do not silently strengthen a claim while correcting its wording.
4. Use **not determined** when the controlling meaning or applicability cannot be reconstructed.
5. Record disagreements rather than forcing consensus.
6. Link each finding to the exact passage and rule ID.
7. Use [[Human Review Boundary Register v0.1]] when the finding could be confused with linguistic, methodological, ethical, or software judgment.

# Checklist items

| Rule | Plain-language control | Communication risk | Typical genres | Human question | Exception | Boundary |
|---|---|---|---|---|---|---|
| SLE-RULE-0001 — One principal message | Each sentence has one identifiable principal assertion, question, or instruction. Necessary conditions, qualifications, and contrasts may remain when they support that message. | A reader cannot tell which claim or action controls the sentence, or treats several independent claims as one evidential unit. | all prose; especially research summaries, procedures, and limitation records | What single message must the reader retain from this sentence? | A conventional definition or tightly integrated contrast may contain more than one clause when the relationship is unambiguous. | The reviewer checks information load and recoverability, not whether the assertion is scientifically correct. |
| SLE-RULE-0002 — Clear reference | A pronoun, demonstrative, or other referring expression identifies one intended antecedent in the local context. | The reader can assign the reference to two or more plausible entities and obtain different claims or instructions. | all prose; especially dense analyses, annotation guidance, and learner explanations | Can this expression refer to more than one plausible antecedent here? | A pronoun may remain when agreement or immediate context leaves only one possible antecedent. | The reviewer resolves textual reference, not discourse reference that the author intentionally leaves open as an object of analysis. |
| SLE-RULE-0003 — Scope of generalization | A generalization identifies the population, variety, register, dataset, period, or other domain that limits the claim, near the claim or in a clearly controlling scope statement. | A bounded result is read as a universal statement about a language, population, or method. | research reports, grammars, field notes, resource guides, summaries | Where, for whom, in which data, and under which conditions is this claim intended to hold? | One section-level scope statement may control several claims when the scope does not change. | The reviewer checks whether scope is stated, not whether the chosen sample supports the scientific generalization. |
| SLE-RULE-0004 — Stable preferred term | A document uses one preferred term for one controlled concept and does not alternate technical synonyms only for stylistic variety. | Readers infer distinctions that the author did not intend or fail to connect repeated references to the same concept. | all technical and scholarly documents | Do competing labels have distinct meanings or an explicit equivalence statement? | Historical labels, quotations, and external terminology may appear when their relationship to the preferred term is explicit. | The reviewer checks terminology control, not which theoretical term the field should prefer. |
| SLE-RULE-0005 — Defined technical term | A technical term is defined before conformance-critical or claim-critical use, or the document links to a controlling definition. The definition states relevant scope and distinguishing criteria. | Readers apply different meanings to a central term and reach incompatible interpretations. | all documents using specialized or project-local terminology | Could a competent reader from another subfield apply this term consistently from the document? | A broadly established term may remain undefined when no competing interpretation affects the claim. | The reviewer checks whether the intended meaning is recoverable, not whether the definition is theoretically correct. |
| SLE-RULE-0006 — Explicit comparison | A comparative claim identifies the compared items, comparison dimension, and relevant measure or basis. | The reader cannot reconstruct what is greater, better, earlier, more acceptable, or otherwise different. | experimental, corpus, typological, phonetic, and system-evaluation reports | More or less than what, on which dimension, and by which measure or basis? | A table heading may supply an element when the relationship is immediate and unambiguous. | The reviewer checks comparison completeness, not whether the metric is scientifically appropriate. |
| SLE-RULE-0007 — Clear logical scope | The scope of negation, quantification, restriction, and exception is unambiguous. | Readers derive different truth conditions or apply an exception to the wrong material. | all analytical and procedural prose | Can the sentence be paraphrased in two materially different ways because of logical scope? | Defined formal notation may carry the scope when the prose explains how to read it. | The reviewer checks the expression of logical relations, not which logical analysis is correct. |
| SLE-RULE-0008 — Declared normative verbal forms | A normative document declares the verbal forms used for requirements, prohibitions, recommendations, permissions, and capabilities, or links to a controlling declaration. One form is not used for conflicting functions when conformance is affected. | Readers cannot distinguish mandatory action, advice, permission, and capability. | annotation guidelines, procedures, standards, policies, and project instructions | What normative function does each verbal form have, and is that mapping consistent? | Quotations may preserve source wording. | The reviewer checks declared function and consistency, not whether the document should adopt *must* or *shall* universally. |
| SLE-RULE-0009 — Attestation does not establish stronger properties | A document does not infer productivity, frequency, acceptability, or grammatical status from attestation alone. | One occurrence is treated as proof of a broader linguistic property. | corpus studies, grammars, lexicography, field notes, and resource documentation | What additional evidence is required for the stronger claim? | None for the inference itself; a document may make a stronger claim when it supplies a separate supporting method or analysis. | The reviewer checks whether the evidence type licenses the stated relation, not whether the stronger property is actually true. |
| SLE-RULE-0010 — Judgment method | A reported speaker or annotator judgment identifies enough applicable information to interpret the result, including task, response format, population, item scope, and result. | A statement such as “speakers accept it” hides who responded, what they did, and how the result was derived. | elicitation, experimental, fieldwork, annotation, and acceptability reporting | What response was collected, from whom, for which items, and by which procedure? | A compact table may supply fields through headings and a methods reference. | The reviewer checks reportability and interpretability, not whether the participants' judgments are linguistically authoritative. |
| SLE-RULE-0011 — Example provenance dimensions | When provenance affects interpretation, a linguistic example identifies relevant source or origin, collection context, modification status, and production method as independent dimensions. | A reader cannot tell whether an example is attested, elicited, adapted, translated, author-created, or system-produced. | grammars, experiments, field notes, dictionaries, documentation, and computational studies | What is the example's origin, context, modification status, and production method? | A dimension may be omitted when it is genuinely irrelevant and the omission cannot mislead. | The reviewer checks provenance disclosure, not whether the example is grammatical or acceptable. |
| SLE-RULE-0012 — Defined judgment notation | A document that uses judgment symbols or category labels defines their meanings or links to a controlling definition. | Symbols such as *, ?, ??, and # are interpreted differently across publications, tasks, or traditions. | grammars, theoretical papers, elicitation reports, annotation manuals | What task, population, or analytical convention licenses each symbol or category label? | A journal-wide convention may control when the document identifies it. | The reviewer checks declared meaning, not whether the marked example deserves that judgment. |
| SLE-RULE-0013 — Stable example identifier | A central example, dataset item, table, or figure has a stable identifier when the document refers to it more than once. | Relative references break after editing or point to the wrong item. | all documents with repeated reference to examples, tables, figures, or records | Will this reference remain valid if material is inserted, removed, or reordered? | A one-time immediate reference may remain relative when no ambiguity or maintenance risk exists. | The reviewer checks referential stability, not the content of the example or figure. |
| SLE-RULE-0014 — Dataset and transformation identity | A dataset-based claim identifies the dataset, relevant version or access state, and material preprocessing, exclusion, normalization, or transformation steps. | Readers cannot reconstruct the data state or determine whether transformations affect the claim. | corpus, computational, phonetic, lexicographic, and resource documentation | Can the reader identify the input data and the material changes made before analysis? | A controlling methods section or data statement may supply the details for multiple local claims. | The reviewer checks identity and disclosed transformation, not whether the preprocessing was methodologically justified. |
| SLE-RULE-0015 — System behavior is not a language fact | A statement about software output identifies the relevant system, version or state, input, and configuration when material, and does not present system behavior alone as direct evidence of speaker knowledge, acceptability, or language structure. | A parser, model, or tool label is treated as a linguistic conclusion. | computational reports, annotation documentation, parser-assisted research, resource guides | Does this statement describe the system, or does it silently convert system output into a claim about language? | System output may support a system-performance claim within the tested conditions. | The reviewer checks category separation, not whether the linguistic analysis or the system output is correct. |
| SLE-RULE-0016 — Condition before action | In an instruction, a condition that determines applicability appears before the action or in a clearly labelled applicability statement. | A reader acts before discovering that the step applies only under a condition. | annotation guidelines, laboratory procedures, editorial workflows, resource-processing instructions | Does the reader encounter the applicability condition before acting? | A compact table may place conditions and actions in clearly labelled columns. | The reviewer checks instruction order, not whether the condition is scientifically or operationally correct. |
| SLE-RULE-0017 — One action per instruction | A procedural step should require one principal action. Inseparable operations may remain together in their required order. | Readers skip, reorder, or cannot separately verify bundled actions. | procedures, annotation guidelines, laboratory protocols, editorial workflows | Can one action fail, be skipped, or require separate verification from another action in this step? | Inseparable actions that form one operation may remain together. | The reviewer checks action structure, not whether the workflow itself is efficient or valid. |
| SLE-RULE-0018 — Conformance does not certify truth | A conformance statement does not imply that SLE verified truth, acceptability, grammaticality, theoretical correctness, ethical adequacy, or methodological validity. | Readers mistake editorial conformance for scientific or ethical approval. | conformance declarations, review records, publication notes, project documentation | Does the statement claim only communication conformance, or does it imply validation of content? | None; separate scientific, ethical, or methodological review may be reported under its own authority. | This rule is itself the boundary between communication review and substantive judgment. |
| SLE-RULE-0019 — Observation separate from interpretation | A document distinguishes directly recorded results from interpretations of those results. | An inference is presented as if it were an observation. | all research, fieldwork, resource, and system reports | Which words report the record, and which words add an analytical inference? | A compact table may separate observation and interpretation in labelled columns. | The reviewer checks whether the distinction is visible, not whether the interpretation is correct. |
| SLE-RULE-0020 — Evidence wording does not overstate force | Evidence wording does not state a stronger relation between evidence and conclusion than the declared method, assumptions, and support justify. | Words such as *proves*, *shows*, or *demonstrates* erase uncertainty or alternative explanations. | all argumentation, results, summaries, and limitations | Does the chosen wording claim more support than the method and stated assumptions provide? | *Prove* may be used for a formal proof or a method that explicitly licenses that conclusion. | The reviewer checks alignment between stated support and wording, not whether one universal hierarchy of evidence verbs exists. |
| SLE-RULE-0021 — Bounded negative claim | A claim that a form, pattern, result, or effect was not found states the search or test space and a relevant sensitivity limit. | Failure to find something is read as proof that it does not exist. | corpus, fieldwork, experimental, resource, and system reports | What was searched or tested, and what could the method have missed? | A formal proof of nonexistence follows its field's declared formal conventions. | The reviewer checks boundaries and sensitivity, not whether the negative conclusion is ultimately true. |
| SLE-RULE-0022 — Limitations and counterevidence | A document states a known limitation or material counterexample when omission could change interpretation of a central claim, and identifies the affected claim and effect on scope or strength. | Readers infer broader or stronger coverage than the author has established. | research reports, grammars, resource guides, procedures, summaries | Would a reasonable reader make a materially broader inference if this limitation or counterexample were omitted? | A controlling limitations section may govern multiple claims when cross-references make the relationship clear. | The reviewer checks disclosure and attachment, not whether every conceivable objection must be included. |
| SLE-RULE-0023 — Claim-support connection | A central claim identifies its supporting evidence or analysis through local prose, citation, stable identifier, table or figure reference, or another explicit cross-reference. | Readers cannot determine which evidence supports which claim. | all research, documentation, and analytical prose | Can the reader point from this central claim to the exact supporting record? | A tightly structured table may pair claims and support through headings and row alignment. | The reviewer checks connection and traceability, not whether the evidence is sufficient or correct. |
| SLE-RULE-0024 — Interlinear glossing declaration | A document using interlinear morpheme-by-morpheme glosses follows the Leipzig Glossing Rules or declares an alternative convention; project abbreviations are defined and object language, segmentation, glossing, and translation remain distinguishable. | Readers cannot distinguish data from analysis or interpret alignment and abbreviations consistently. | grammars, fieldwork, typology, theoretical papers, dictionaries | Are the convention, alignment, abbreviations, omitted layers, and analytical status of segmentation and glosses clear? | A layer may be omitted when the omission suits the purpose and is not misleading. | The reviewer checks declared presentation convention, not whether the segmentation or gloss analysis is linguistically correct. |

## Completion and traceability

For each applicable item, record **Pass**, **Fail**, **Borderline**, **Not applicable**, **Justified exception**, **Waived**, or **Not determined**. Link the decision to the exact passage.

- Independent rationale: [[Independent SLE Rule Evidence Register v0.1]]
- Rule-to-corpus mapping: [[SLE Rule Traceability Matrix v0.1]]
- Classified examples: [[SLE Rule Test Case Catalog v0.1]]
- Substantive-review limits: [[Human Review Boundary Register v0.1]]
- Conformance result model: [[Profiles and Conformance]]

A **conforms** result requires every applicable requirement to pass or have a controlling permitted exception. A **conforms with declared waivers** result requires a visible valid waiver for every unmet applicable requirement. Review method and evaluation type remain separate from the conformance result.
