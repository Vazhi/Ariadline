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

It does not create or stabilize rules, replace the controlling rule text, certify substantive content, or require software. Optional tooling is separated in [[Optional Automation Notes for SLE Review v0.1]].

## Required review record

Before applying the checklist, record:

- the bounded conformance object;
- the SLE version and profile-set version;
- the exact applicable rule IDs;
- the selected document pattern or patterns, if any;
- the review method;
- any declared waivers or extensions;
- the authorized meaning record when a passage will be revised or compared;
- the final result: **conforms**, **conforms with declared waivers**, **does not conform**, or **not determined**.

Use [[Profiles and Conformance]], [[SLE Profile Applicability Register v0.1]], and [[SLE Semantic Equivalence Review Template v0.1]] to define the review scope and meaning authority.

## Final item outcomes

For each applicable rule, the completed review record must use one final outcome:

- **Pass** — the applicable requirement or recommendation is met.
- **Fail** — the applicable control is not met and no valid exception or waiver covers it.
- **Not applicable** — the rule's applicability condition is absent.
- **Justified exception** — the controlling rule or its **should**-level recommendation permits the documented departure, and the departure does not mislead.
- **Waived** — a material unmet control is covered by a valid declared waiver.
- **Not determined** — scope, evidence, applicability, or authorized meaning is insufficient for a safe decision.

## Provisional Borderline flag

**Borderline** is a provisional review flag, not a final item outcome.

Use it when a plausible compliant and noncompliant reading remains and clarification or adjudication is still pending. Before the review closes, resolve the flag to **Pass**, **Fail**, **Not applicable**, **Justified exception**, **Waived**, or **Not determined**.

A recommendation expressed with **should** receives **Justified exception**, not **Pass**, when the recommended form is not followed under a documented permitted departure. A requirement expressed with **must** cannot pass merely because a reviewer prefers the existing wording.

## Review discipline

1. Review communication form, not scientific truth.
2. Preserve the authorized meaning, evidential force, theoretical commitment, uncertainty, and normative force.
3. Do not infer authentic author intent without an authorized meaning record.
4. Do not silently strengthen or weaken content while correcting wording.
5. Use **not determined** when meaning or applicability cannot be reconstructed safely.
6. Record disagreements instead of forcing consensus.
7. Link every finding to the exact passage and full rule ID.
8. Use [[Human Review Boundary Register v0.1]] whenever editorial review approaches substantive judgment.

# Checklist items

| Rule | Plain-language control | Communication risk | Human question | Permitted boundary | Substantive-review boundary |
|---|---|---|---|---|---|
| `SLE-RULE-0001` — One principal message | Each sentence has one identifiable principal assertion, question, or instruction. Necessary conditions, qualifications, and contrasts may remain when they support that message. | Several independent claims or actions become one unclear unit. | What single message must the reader retain? | A conventional definition or tightly integrated contrast may contain more than one clause when the relation is unambiguous. | Review information load, not scientific correctness. |
| `SLE-RULE-0002` — Clear reference | A pronoun, demonstrative, or referring expression identifies one intended antecedent locally. | Two plausible antecedents produce different claims. | Can this expression refer to more than one plausible antecedent here? | Agreement or immediate context may leave only one possible antecedent. | Do not resolve intentionally open reference that is itself under analysis. |
| `SLE-RULE-0003` — Scope of generalization | A generalization identifies the population, variety, register, dataset, period, or other limiting domain near the claim or in a controlling scope statement. | A bounded result appears universal. | Where, for whom, in which data, and under which conditions does the claim hold? | One section-level statement may govern unchanged scope. | Do not judge sampling adequacy. |
| `SLE-RULE-0004` — Stable preferred term | One preferred term identifies one controlled concept; technical synonyms do not alternate only for style. | Readers infer unintended distinctions or miss equivalence. | Do competing labels have different meanings or an explicit equivalence statement? | Historical labels, quotations, and external terms may appear with an explicit relationship. | Do not select the field's preferred theory term. |
| `SLE-RULE-0005` — Defined technical term | A claim-critical or conformance-critical technical term is defined before use or linked to a controlling definition. | Readers apply incompatible meanings. | Can a competent reader from another subfield apply the term consistently? | A broadly established term may remain undefined when no competing interpretation matters. | Do not certify theoretical correctness of the definition. |
| `SLE-RULE-0006` — Explicit comparison | A comparison identifies the items, dimension, and measure or basis. | The reader cannot reconstruct what differs or how. | More or less than what, on which dimension, and by which basis? | Immediate table headings may supply an element. | Do not validate the scientific metric. |
| `SLE-RULE-0007` — Clear logical scope | Negation, quantification, restriction, and exception scope are unambiguous. | Readers derive different truth conditions or applicability. | Can the passage be paraphrased in two materially different ways? | Declared formal notation may carry scope. | Do not adjudicate the correct formal analysis. |
| `SLE-RULE-0008` — Declared normative verbal forms | A normative document declares requirement, prohibition, recommendation, permission, and capability forms and uses them consistently. | Mandatory action, advice, permission, and capability are confused. | What function does each normative form have, and is the mapping consistent? | Quotations may preserve source wording. | Do not impose a universal *must* versus *shall* policy. |
| `SLE-RULE-0009` — Attestation does not establish stronger properties | Attestation alone is not presented as productivity, frequency, acceptability, or grammatical status. | One occurrence becomes proof of a broader property. | What separate evidence licenses the stronger claim? | A stronger claim may remain when separately supported; this is ordinary compliance, not an exception to the attestation boundary. | Do not decide whether the stronger property is true. |
| `SLE-RULE-0010` — Judgment method | A reported judgment states enough applicable task, response, population, item, and result information for interpretation. | “Speakers accept it” hides how the result was obtained. | What response was collected, from whom, for which items, and by which procedure? | Tables and methods references may supply the details. | Do not infer grammaticality from responses. |
| `SLE-RULE-0011` — Example provenance dimensions | Relevant origin, collection context, modification status, and production method are recorded independently. | Readers cannot distinguish attested, elicited, adapted, translated, authored, or system-produced material. | What is the example's origin, context, modification, and production method? | An irrelevant dimension may be omitted when omission cannot mislead. | Do not certify grammaticality, authenticity, or community acceptability. |
| `SLE-RULE-0012` — Defined judgment notation | Judgment symbols and category labels are defined or linked to a controlling definition. | Symbols receive incompatible interpretations. | What task, population, or analytical convention licenses each symbol or label? | A declared publication-wide convention may control. | Do not decide whether an item deserves the judgment. |
| `SLE-RULE-0013` — Stable example identifier | Repeatedly referenced examples, data items, tables, and figures have stable identifiers. | Relative references break after editing. | Will the reference remain valid after insertion, deletion, or reordering? | A one-time immediate reference is outside the repeated-reference trigger. | Do not evaluate the content of the item. |
| `SLE-RULE-0014` — Dataset and transformation identity | Dataset identity, version or state, and material transformations are stated. | Readers cannot reconstruct the input data state. | Can the reader identify the data and material changes before analysis? | A controlling methods or data statement may govern several claims. | Do not approve preprocessing choices. |
| `SLE-RULE-0015` — System behavior is not a language fact | Material system identity, state, input, and configuration are stated; output alone is not presented as speaker knowledge or language structure. | A model or parser label becomes a linguistic conclusion. | Does this passage describe system behavior or silently convert it into a language claim? | System output may support a bounded system-performance claim; this is ordinary compliance with the category boundary. | Do not certify system or linguistic correctness. |
| `SLE-RULE-0016` — Condition before action | An applicability condition appears before the action or in a clearly labelled applicability statement. | Readers act before seeing the condition. | Does the reader encounter the condition before acting? | A labelled condition/action table may be used. | Do not validate the condition itself. |
| `SLE-RULE-0017` — One action per instruction | A procedural step should contain one principal action; inseparable operations may remain together. | Bundled actions are skipped, reordered, or unverifiable. | Can one action fail, be skipped, or need separate verification? | One inseparable operation may use multiple verbs. | Do not decide whether the workflow is efficient or valid. |
| `SLE-RULE-0018` — Conformance does not certify truth | A conformance statement is limited to communication requirements. | Editorial conformance appears to certify truth, theory, method, ethics, or software. | Does the statement imply validation beyond declared communication controls? | Separate substantive reviews may be reported under their own authority; this is not an exception to the prohibition. | This rule is the core boundary itself. |
| `SLE-RULE-0019` — Observation separate from interpretation | Directly recorded results are visibly distinguished from interpretation. | An inference appears to be an observation. | Which words report the record, and which add analysis? | Labelled clauses, sentences, headings, or columns are permitted presentation methods, not exceptions. | Do not judge the interpretation's correctness. |
| `SLE-RULE-0020` — Evidence wording does not overstate force | Wording does not claim a stronger evidence–conclusion relation than the declared method and assumptions justify. | *Proves*, *shows*, or similar wording erases uncertainty or alternatives. | Does the chosen wording exceed the support the document itself declares? | *Prove* may be used for a formal proof or explicitly licensing method. | Do not impose a universal evidence-verb hierarchy. |
| `SLE-RULE-0021` — Bounded negative claim | A not-found claim states the search or test space and a relevant sensitivity limit. | Failure to find becomes proof of nonexistence. | What was searched or tested, and what could the method miss? | Formal nonexistence proofs follow their declared conventions. | Do not certify the negative conclusion. |
| `SLE-RULE-0022` — Limitations and counterevidence | A known material limitation or counterexample is linked to the affected central claim and its scope or strength effect. | Readers infer broader coverage than established. | Would omission cause a materially broader inference? | A controlling limitations section may govern explicitly linked claims; this is an allowed location, not an exception to disclosure. | Do not require every conceivable objection. |
| `SLE-RULE-0023` — Claim-support connection | A central claim points to its supporting evidence or analysis through prose, citation, identifier, table, figure, or explicit cross-reference. | Readers cannot identify which record supports the claim. | Can the reader point from the claim to the exact stated support? | Structured tables are permitted claim-support mappings, not exceptions. | Link presence does not establish sufficiency. |
| `SLE-RULE-0024` — Interlinear glossing declaration | Interlinear glosses follow the Leipzig Glossing Rules or a declared alternative; abbreviations and layers are distinguishable. | Data, segmentation, glossing, and translation become indistinguishable. | Are convention, alignment, abbreviations, omitted layers, and analytical status clear? | A layer may be omitted when the omission suits the purpose and is declared non-misleading. | Do not certify segmentation or gloss analysis. |

## Completion and traceability

For each applicable rule, record a final item outcome and link it to the exact passage. Preserve any provisional **Borderline** flag and its resolution in the review history.

- Independent rationale: [[Independent SLE Rule Evidence Register v0.1]]
- Rule and audit-material mapping: [[SLE Rule Traceability Matrix v0.1]]
- Classified constructed cases: [[SLE Rule Test Case Catalog v0.1]]
- Substantive-review limits: [[Human Review Boundary Register v0.1]]
- Conformance result model: [[Profiles and Conformance]]

A **conforms** result requires every applicable requirement to pass or have a controlling permitted exception. A **conforms with declared waivers** result requires a visible valid waiver for every unmet applicable requirement. Any unresolved **Borderline** flag or final **Not determined** item requires the whole declared conformance result to remain **not determined**. Review method, typed evaluation, and independent meaning-preservation status remain separate from conformance.