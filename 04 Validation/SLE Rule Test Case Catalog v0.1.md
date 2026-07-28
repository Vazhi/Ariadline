---
title: "SLE Rule Test Case Catalog v0.1"
type: validation-catalog
status: proposed
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - sle
  - validation
  - test-cases
  - editorial-review
---
# SLE Rule Test Case Catalog v0.1

## Purpose

This catalog supplies pass, fail, borderline, and justified-exception cases for every proposed rule in [[SLE for Linguistics Language Rules v0.1]].

The cases are constructed editorial test material. They are not evidence about the named languages, theories, methods, speakers, datasets, or systems.

The controlling rule text remains in the language-rule draft. Reviewers apply the questions in [[SLE Editorial Conformance Checklist v0.1]] and consult [[Human Review Boundary Register v0.1]] when a case crosses into substantive linguistic judgment.

## How to use the cases

- A **pass** case illustrates a straightforward compliant communication form.
- A **fail** case illustrates the communication risk targeted by the rule.
- A **borderline** case requires the reviewer to request context, clarification, or adjudication.
- A **justified exception** illustrates a boundary permitted by the controlling rule.
- A case does not establish that its linguistic content is true.
- A reviewer must not copy a controlled example when it would change the author's intended meaning.

# Rule-by-rule cases

| Rule | Pass | Fail | Borderline | Justified exception | Substantive boundary |
|---|---|---|---|---|---|
| SLE-RULE-0001 — One principal message | The analysis predicts a scope difference. The corpus result is reported in the next sentence. | The analysis predicts a scope difference, the corpus result is weak, the speakers vary, and the construction is therefore impossible. | The analysis predicts a scope difference because the operator takes wider scope in the stated derivation. | A clitic is a phonologically dependent form that has syntactic distribution beyond an ordinary affix. | The reviewer checks information load and recoverability, not whether the assertion is scientifically correct. |
| SLE-RULE-0002 — Clear reference | The suffix follows the clitic. The suffix is optional. | The suffix follows the clitic, but it is optional. | After the noun phrase enters the local domain, it cannot move again. | Maria_i said that she_i would return. [Indexing defines the antecedent.] | The reviewer resolves textual reference, not discourse reference that the author intentionally leaves open as an object of analysis. |
| SLE-RULE-0003 — Scope of generalization | In the 2025 classroom corpus, speakers aged 18–25 used the form in 7 of 840 relevant turns. | Young speakers use this form. | In this corpus, the form is rare. | Unless otherwise stated, all claims in this section concern the northern variety in recorded interviews from 2024. | The reviewer checks whether scope is stated, not whether the chosen sample supports the scientific generalization. |
| SLE-RULE-0004 — Stable preferred term | This guide uses *dependency relation* throughout. | The dependency relation, link, connection, and arc are assigned in Step 3. | The paper uses *construction* in the analysis and *pattern* in the participant instructions. | Earlier work called this category *adjunct*. This paper uses *modifier* for the same category. | The reviewer checks terminology control, not which theoretical term the field should prefer. |
| SLE-RULE-0005 — Defined technical term | In this study, *productive* means extension of the pattern to novel eligible verbs in Task 3. | The pattern is productive. | We use the standard definition of *morpheme*. | The report uses *vowel* in its ordinary phonetic sense; no competing interpretation affects the procedure. | The reviewer checks whether the intended meaning is recoverable, not whether the definition is theoretically correct. |
| SLE-RULE-0006 — Explicit comparison | Form A received a higher mean rating than Form B in Task 2. | Form A was better. | The northern group used the form more often. | Column heading: Mean F0 difference from baseline (Hz). Row: Condition B, +18. | The reviewer checks comparison completeness, not whether the metric is scientifically appropriate. |
| SLE-RULE-0007 — Clear logical scope | No participant rated every example. | The participants did not rate all examples. | Only two speakers did not reject the form. | Under the declared notation, ¬∀x P(x) means that not every x has property P. | The reviewer checks the expression of logical relations, not which logical analysis is correct. |
| SLE-RULE-0008 — Declared normative verbal forms | In this guide, *must* states a requirement, *should* states a recommendation, *may* grants permission, and *can* states capability. | Annotators can record the label, and they can not skip this step. [The first *can* grants permission; the second is intended as prohibition.] | Follow the publisher's normative-language policy. | The quoted policy states, “Editors shall record every exception.” | The reviewer checks declared function and consistency, not whether the document should adopt *must* or *shall* universally. |
| SLE-RULE-0009 — Attestation does not establish stronger properties | The form is attested in this corpus. The corpus result alone does not establish productivity. | The corpus contains the form, so the pattern is productive. | The form occurs in six independent texts and appears productive. | The corpus establishes attestation; a separate nonce-word task provides the stated evidence for productive extension. | The reviewer checks whether the evidence type licenses the stated relation, not whether the stronger property is actually true. |
| SLE-RULE-0010 — Judgment method | In a five-point rating task, 18 of 22 eligible participants rated Item 12 as 4 or 5. | Speakers accept Item 12. | Most participants accepted the sentence in the rating task. | Table 3 reports task, scale, eligible population, item count, and response distribution; the prose links directly to Table 3. | The reviewer checks reportability and interpretability, not whether the participants' judgments are linguistically authoritative. |
| SLE-RULE-0011 — Example provenance dimensions | Example 12 is a participant response from Elicitation Task E3; orthography was normalized. | Example 12: The child goed home. | Example 12 is constructed. | A formal schematic variable such as X-bar notation needs no attestation label when the document makes clear that it is notation rather than language data. | The reviewer checks provenance disclosure, not whether the example is grammatical or acceptable. |
| SLE-RULE-0012 — Defined judgment notation | An asterisk marks items that all consulted speakers rejected in the stated task. | *The child goed home. [No notation definition.] | We use standard acceptability symbols. | Judgment symbols follow the journal's linked notation guide, version 3. | The reviewer checks declared meaning, not whether the marked example deserves that judgment. |
| SLE-RULE-0013 — Stable example identifier | Example (12) shows the alternation. | The example above shows the alternation. | This example shows the alternation. [The example is referenced only once and is immediately adjacent.] | The following single example illustrates the notation. [No later reference occurs.] | The reviewer checks referential stability, not the content of the example or figure. |
| SLE-RULE-0014 — Dataset and transformation identity | We used Dataset D, release 2. We excluded files without speaker metadata and normalized Unicode to NFC before tokenization. | We used the corpus and removed bad data. | We used the current public release after standard preprocessing. | All analyses in this section use the dataset and transformation pipeline defined in Methods 2.3. | The reviewer checks identity and disclosed transformation, not whether the preprocessing was methodologically justified. |
| SLE-RULE-0015 — System behavior is not a language fact | Parser P version 2.1 labels the input A_NOT_A under Configuration C. This result describes parser behavior and does not establish the linguistic analysis. | The sentence is an A-not-A question because the parser labels it A_NOT_A. | The model recognizes the construction. | On Benchmark B under Configuration C, System P achieved 91% label accuracy. | The reviewer checks category separation, not whether the linguistic analysis or the system output is correct. |
| SLE-RULE-0016 — Condition before action | If the token is a clitic, assign label CL. | Assign label CL if the token is a clitic. | Assign label CL only to clitics. | Table columns: Condition \| Required action. | The reviewer checks instruction order, not whether the condition is scientifically or operationally correct. |
| SLE-RULE-0017 — One action per instruction | 1. Segment the token. 2. Assign the feature bundle. 3. Record any source-text correction. | Segment the token, assign features, correct the source, and update the log. | Open the file and select the target tier. | Press and hold the key. [The two verbs describe one inseparable physical operation.] | The reviewer checks action structure, not whether the workflow itself is efficient or valid. |
| SLE-RULE-0018 — Conformance does not certify truth | This section conforms to SLE v0.1 for the declared rules. The result does not validate the analysis. | This SLE-conforming analysis is linguistically correct. | The document passed SLE review. | The document conforms to SLE and separately received ethics approval from Committee E under record 123. | This rule is itself the boundary between communication review and substantive judgment. |
| SLE-RULE-0019 — Observation separate from interpretation | The query returned three tokens. Under Analysis A, these tokens are compatible with the proposed rule. | The three tokens demonstrate a grammatical rule. | The result indicates a grammatical rule. | Table columns: Recorded result \| Interpretation under Analysis A. | The reviewer checks whether the distinction is visible, not whether the interpretation is correct. |
| SLE-RULE-0020 — Evidence wording does not overstate force | The three tokens establish attestation in this corpus. They do not by themselves establish productivity. | Three tokens prove that the construction is productive. | The result shows that the analysis is preferred. | The proof establishes Theorem 2 under Assumptions A–C. | The reviewer checks alignment between stated support and wording, not whether one universal hierarchy of evidence verbs exists. |
| SLE-RULE-0021 — Bounded negative claim | The query found no tokens in Corpus C, release 3. It does not detect spelling variants outside the normalization list. | The construction does not occur. | We found no examples in the corpus. | The formal proof establishes that no model satisfying A–C has property P. | The reviewer checks boundaries and sensitivity, not whether the negative conclusion is ultimately true. |
| SLE-RULE-0022 — Limitations and counterevidence | The analysis covers affirmative matrix clauses. It does not cover embedded clauses or negative forms. | The analysis covers the construction. | Several limitations remain. | Claim C is qualified by Limitations L1–L3 in Section 6, which this paragraph cites. | The reviewer checks disclosure and attachment, not whether every conceivable objection must be included. |
| SLE-RULE-0023 — Claim-support connection | The nonce-word results in Table 4 support the productivity claim for the tested verb class. | The construction is productive. Several results appear below. | The results support the analysis. | Table columns: Claim ID \| Supporting record \| Limitation. | The reviewer checks connection and traceability, not whether the evidence is sufficient or correct. |
| SLE-RULE-0024 — Interlinear glossing declaration | The document declares Leipzig-style glossing, defines PST and 1SG, and separates object-language text, gloss, and free translation. | mi-na go 1SG-PST go ‘I went.’ [No convention or abbreviation declaration.] | Glosses follow common practice. | A dictionary entry omits the free-translation line because the headword translation is already given and the omission is declared. | The reviewer checks declared presentation convention, not whether the segmentation or gloss analysis is linguistically correct. |

## Decision instructions

- **Pass:** the targeted communication requirement is satisfied.
- **Fail:** the targeted risk is present and no valid exception or waiver resolves it.
- **Borderline:** request context or author clarification; use **not determined** when meaning cannot be reconstructed safely.
- **Justified exception:** accept only when the controlling rule expressly permits the boundary and the text remains non-misleading.
- Do not copy a controlled example when doing so would change polarity, quantification, scope, evidence force, theory, example status, or normative force.

## Cross-domain and Canto-span boundary

The constructed cases span grammar, theory, corpus research, fieldwork, experimentation, lexicography, signed-language and resource documentation, annotation, computational linguistics, pedagogy, phonetics, and collaborative editorial work.

Canto-span does not supply a controlling test case. The two items in [[Canto-span Evaluation Subset v0.1]] are supplementary difficult cases only.

## Known gaps

- No independently reviewed real interlinear-gloss block directly tests SLE-RULE-0024.
- Borderline cases have not yet been adjudicated by multiple reviewers.
- The cases are English editorial prose rather than authentic multilingual documents.
- Full-document interaction among multiple rules remains untested.
- Rejected rewrites and author-disagreement cases must be retained during evaluation.

See [[SLE Evaluation Corpus Bias Assessment v0.1]] and [[Evaluation Corpus Coverage Matrix v0.1]].
