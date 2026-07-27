---
title: "Vault Validation Report"
type: report
status: complete
created: 2026-07-27
updated: 2026-07-27
tags:
  - sle
  - validation
  - vault
---

# Vault Validation Report

- Markdown notes: 57
- Wikilinks checked: 311
- Duplicate note basenames: 0
- Broken wikilinks: 0

## Result

PASS — all current wikilinks resolve and all note basenames are unique.

## Validation scope

This report describes the branch after the first independent, prose-first SLE for Linguistics language-rule draft and its review repairs.

The branch adds:

- [[SLE for Linguistics Language Rules v0.1]];
- [[Independent SLE Rule Evidence Register v0.1]];
- [[Claim Function Decision Register v0.1]].

It also revises the rule inventory, rule-proposal template, grammar and style plan, claim-evidence matrix, normative-language note, linguistic-example guidance, and map of content.

## Count method

Merged `main` contained 54 Markdown notes and 286 wikilinks.

This branch adds three uniquely named Markdown notes containing 13 wikilinks. Revised existing notes add a net 12 wikilinks. The resulting totals are 57 Markdown notes and 311 wikilinks.

External web references in the evidence register are ordinary Markdown links and are not included in the wikilink total.

## Rule-set validation

- The normative draft contains 24 proposed rule IDs from `SLE-RULE-0001` through `SLE-RULE-0024`.
- The rule inventory contains the same 24 IDs exactly once.
- No competing `SLE-LR-*` namespace remains.
- Every rule remains `proposed`; no rule is represented as stable or published.
- Every rule has normative text, a boundary or rationale, an editorial check, and a traceable evidence disposition.

## Review-repair validation

### Evidence traceability

The evidence register now contains 11 independent source records with exact heading, section, or page locators.

Each rule mapping distinguishes:

1. evidence that a communication problem exists;
2. evidence for an equivalent control;
3. an SLE-local hypothesis or unresolved design choice.

The register no longer labels a rule `direct` or `cross-domain` solely from a broad source summary. Sources from one research community are not counted as independent cross-domain convergence by themselves.

### Normative verbal forms

SLE-RULE-0008 now controls declaration and consistent function mapping. It does not require all SLE documents to choose **must** rather than **shall**.

The draft records ISO’s **shall** convention and IETF BCP 14’s **MUST/SHALL** convention as alternatives. The final preferred requirement form remains an evaluation question.

### Evidence wording

SLE-RULE-0020 now controls overstatement of inferential force without defining a universal hierarchy for *shows*, *supports*, *suggests*, *is consistent with*, *does not establish*, and *contradicts*.

The earlier fixed lexical hierarchy is withdrawn and explicitly deferred for cross-domain evaluation.

### Example provenance

SLE-RULE-0011 now uses four independent dimensions:

- source or origin;
- collection context;
- modification status;
- production method.

Multiple descriptors may apply to one example. `System-produced item` is defined without implying attestation, acceptability, grammaticality, or analytical validity.

## Authority and scope validation

- Canto-span is named only as a later non-normative stress test.
- No Canto-span term, status, ontology, workflow, or governance rule supplies normative justification.
- Visible claim labels are optional.
- Machine-readable headers and automated checking are not required.
- The rule inventory and proposal template use human editorial and evaluation procedures.
- SLE conformance is explicitly separated from linguistic truth, analytical correctness, ethical adequacy, and methodological validity.

## Duplicate basenames

```json
{}
```

## Broken wikilinks

```json
[]
```
