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

This catalog supplies pass, fail, provisional borderline, and boundary cases for every proposed rule in [[SLE for Linguistics Language Rules v0.1]].

The cases are constructed editorial prompts. They are not linguistic evidence and have no independent meaning-preservation confirmation. The controlling rule text remains in the language-rule draft.

Reviewers use [[SLE Editorial Conformance Checklist v0.1]] and [[Human Review Boundary Register v0.1]]. They must not copy an example when doing so changes the authorized meaning of the passage under review.

## Classification

- **Pass** — straightforward compliant communication form.
- **Fail** — the targeted communication risk is present.
- **Borderline** — a provisional prompt requiring context, meaning authority, clarification, or adjudication; it is not a final item outcome.
- **Boundary case** — illustrates one declared subtype:
  - **explicit exception** — the controlling rule expressly permits an exception;
  - **recommendation exception** — a **should**-level control permits a documented departure;
  - **permitted presentation** — the rule allows another compliant form or location;
  - **non-applicability** — the rule's trigger is absent;
  - **ordinary bounded compliance** — the example remains within the rule and is not an exception.

A boundary case does not automatically receive the final checklist outcome **Justified exception**. Only an explicit or recommendation exception can receive that outcome.

# Rule-by-rule cases

| Rule | Pass | Fail | Borderline | Boundary case |
|---|---|---|---|---|
| `SLE-RULE-0001` | The analysis predicts a scope difference. The corpus result is reported in the next sentence. | The analysis predicts a scope difference, the corpus result is weak, the speakers vary, and the construction is therefore impossible. | The analysis predicts a scope difference because the operator takes wider scope in the stated derivation. | **Explicit exception:** A clitic is a phonologically dependent form that has syntactic distribution beyond an ordinary affix. |
| `SLE-RULE-0002` | The suffix follows the clitic. The suffix is optional. | The suffix follows the clitic, but it is optional. | After the noun phrase enters the local domain, it cannot move again. | **Explicit exception:** Maria_i said that she_i would return. Indexing defines the antecedent. |
| `SLE-RULE-0003` | In the 2025 classroom corpus, speakers aged 18–25 used the form in 7 of 840 relevant turns. | Young speakers use this form. | In this corpus, the form is rare. | **Explicit exception:** Unless otherwise stated, all claims in this section concern the northern variety in recorded interviews from 2024. |
| `SLE-RULE-0004` | This guide uses *dependency relation* throughout. | The dependency relation, link, connection, and arc are assigned in Step 3. | The paper uses *construction* in the analysis and *pattern* in participant instructions. | **Explicit exception:** Earlier work called this category *adjunct*. This paper uses *modifier* for the same category. |
| `SLE-RULE-0005` | In this study, *productive* means extension of the pattern to novel eligible verbs in Task 3. | The pattern is productive. | We use the standard definition of *morpheme*. | **Explicit exception:** The report uses *vowel* in its ordinary phonetic sense; no competing interpretation affects the procedure. |
| `SLE-RULE-0006` | Form A received a higher mean rating than Form B in Task 2. | Form A was better. | The northern group used the form more often. | **Explicit exception:** Column: Mean F0 difference from baseline (Hz). Row: Condition B, +18. |
| `SLE-RULE-0007` | No participant rated every example. | The participants did not rate all examples. | Only two speakers did not reject the form. | **Explicit exception:** Under the declared notation, ¬∀x P(x) means that not every x has property P. |
| `SLE-RULE-0008` | In this guide, *must* states a requirement, *should* a recommendation, *may* permission, and *can* capability. | Annotators can record the label, and they can not skip this step. The first *can* grants permission; the second is intended as prohibition. | Follow the publisher's normative-language policy. | **Explicit exception:** The quoted policy states, “Editors shall record every exception.” |
| `SLE-RULE-0009` | The form is attested in this corpus. The corpus result alone does not establish productivity. | The corpus contains the form, so the pattern is productive. | The form occurs in six independent texts and appears productive. | **Ordinary bounded compliance:** The corpus establishes attestation; a separate nonce-word task supplies the stated evidence for productive extension. |
| `SLE-RULE-0010` | In a five-point rating task, 18 of 22 eligible participants rated Item 12 as 4 or 5. | Speakers accept Item 12. | Most participants accepted the sentence in the rating task. | **Explicit exception:** Table 3 reports task, scale, eligible population, item count, and response distribution; the prose links to Table 3. |
| `SLE-RULE-0011` | Example 12 is a participant response from Elicitation Task E3; orthography was normalized. | Example 12: The child goed home. | Example 12 is constructed. | **Non-applicability:** A formal schematic variable needs no language-example provenance record when the document makes clear that it is notation rather than language data. |
| `SLE-RULE-0012` | An asterisk marks items that all consulted speakers rejected in the stated task. | *The child goed home. No notation definition is supplied. | We use standard acceptability symbols. | **Permitted presentation:** Judgment symbols follow the journal's linked notation guide, version 3. |
| `SLE-RULE-0013` | Example (12) shows the alternation. | The example above shows the alternation after several intervening examples. | This example shows the alternation, but the review record does not show whether later references occur. | **Non-applicability:** The following single example illustrates the notation. No later reference occurs. |
| `SLE-RULE-0014` | We used Dataset D, release 2. We excluded files without speaker metadata and normalized Unicode to NFC before tokenization. | We used the corpus and removed bad data. | We used the current public release after standard preprocessing. | **Permitted presentation:** All analyses in this section use the dataset and transformation pipeline defined in Methods 2.3. |
| `SLE-RULE-0015` | Parser P version 2.1 labels the input A_NOT_A under Configuration C. This describes parser behavior and does not establish the linguistic analysis. | The sentence is an A-not-A question because the parser labels it A_NOT_A. | The model recognizes the construction. | **Ordinary bounded compliance:** On Benchmark B under Configuration C, System P achieved 91% label accuracy. |
| `SLE-RULE-0016` | If the token is a clitic, assign label CL. | Assign label CL if the token is a clitic. | Assign label CL only to clitics; the document does not show whether a prior applicability statement controls the step. | **Explicit exception:** Table columns: Condition; Required action. |
| `SLE-RULE-0017` | 1. Segment the token. 2. Assign the feature bundle. 3. Record any source-text correction. | Segment the token, assign features, correct the source, and update the log. | Open the file and select the target tier; the workflow does not show whether these are independently verifiable actions. | **Recommendation exception:** Press and hold the key. The verbs describe one inseparable operation. |
| `SLE-RULE-0018` | This section conforms to SLE v0.1 for the declared rules. The result does not validate the analysis. | This SLE-conforming analysis is linguistically correct. | The document passed SLE review. | **Ordinary bounded compliance:** The document conforms to SLE and separately received ethics approval under a named record. |
| `SLE-RULE-0019` | The query returned three tokens. Under Analysis A, these tokens are compatible with the proposed rule. | The three tokens demonstrate a grammatical rule. | The result indicates a grammatical rule. | **Permitted presentation:** Table columns: Recorded result; Interpretation under Analysis A. |
| `SLE-RULE-0020` | The three tokens establish attestation in this corpus. They do not by themselves establish productivity. | Three tokens prove that the construction is productive. | The result shows that the analysis is preferred. | **Explicit exception:** The proof establishes Theorem 2 under Assumptions A–C. |
| `SLE-RULE-0021` | The query found no tokens in Corpus C, release 3. It does not detect variants outside the normalization list. | The construction does not occur. | We found no examples in the corpus. | **Explicit exception:** The formal proof establishes that no model satisfying A–C has property P. |
| `SLE-RULE-0022` | The analysis covers affirmative matrix clauses. It does not cover embedded clauses or negative forms. | The analysis covers the construction. | Several limitations remain. | **Permitted presentation:** Claim C is qualified by Limitations L1–L3 in Section 6, and the claim cites that section. |
| `SLE-RULE-0023` | The nonce-word results in Table 4 support the productivity claim for the tested verb class. | The construction is productive. Several results appear below. | The results support the analysis. | **Permitted presentation:** Table columns: Claim ID; Supporting record; Limitation. |
| `SLE-RULE-0024` | The document declares Leipzig-style glossing, defines PST and 1SG, and separates object-language text, gloss, and free translation. | mi-na go 1SG-PST go ‘I went.’ No convention or abbreviation declaration is supplied. | Glosses follow common practice. | **Explicit exception:** A dictionary entry omits the free-translation line because the headword translation is already given and the omission is declared. |

## Decision instructions

- **Pass:** the targeted communication requirement is satisfied.
- **Fail:** the targeted risk is present and no valid exception or waiver resolves it.
- **Borderline:** preserve the provisional flag, request context or authorized-meaning clarification, and resolve it to a final checklist outcome before closing the review.
- **Boundary case:** apply its stated subtype. Do not record **Justified exception** for permitted presentation, non-applicability, or ordinary bounded compliance.
- Do not copy a case when doing so changes polarity, quantification, scope, evidence force, theory, example status, access boundary, or normative force.

## Coverage boundary

The cases prompt several domains and methods but remain English project-constructed editorial material. They do not create authentic multilingual, source-author, community, or independent-preservation coverage.

Canto-span supplies no controlling test case. [[Canto-span Evaluation Subset v0.1]] remains supplementary.

Known gaps include independent adjudication, authentic documents, full-document interaction, rejected rewrites, and independently reviewed interlinear glosses. See [[SLE Evaluation Corpus Bias Assessment v0.1]] and [[Evaluation Corpus Coverage Matrix v0.1]].