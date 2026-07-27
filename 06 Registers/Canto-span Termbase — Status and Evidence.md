---
title: "Canto-span Pilot Termbase v0.1 — Status and Evidence"
type: termbase-part
status: proposed
version: "0.1"
created: 2026-07-27
updated: 2026-07-27
tags:
  - sle
  - terminology
  - canto-span
  - termbase-part
---

# Canto-span Pilot Termbase v0.1 — Status and Evidence

Part of [[Canto-span Pilot Termbase v0.1]]. These meanings are project-scoped and do not form a universal linguistic ontology.

## CS-TERM-0011 — linguistic status

- **Concept ID:** `CS-CONCEPT-LINGUISTIC-STATUS`
- **Definition:** the current evidence disposition recorded by the canonical grammar note for a construction.
- **Scope:** one current note under grammar/<status>/.
- **Allowed variants:** status disposition.
- **Excluded interpretations:** runtime state; availability; readiness; merge state.
- **Example:** AA01 has linguistic status research_pending at the frozen baseline.
- **Canonical owner:** `one current note under grammar/<status>/`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:grammar/`
- **Change status:** `new_project_term`

## CS-TERM-0012 — supported_productive

- **Concept ID:** `CS-CONCEPT-SUPPORTED-PRODUCTIVE`
- **Definition:** the status for a bounded construction profile that has passed every applicable promotion and completion gate.
- **Scope:** Canto-span linguistic status vocabulary.
- **Allowed variants:** supported productive.
- **Excluded interpretations:** probably grammatical; attested; implemented.
- **Example:** A record may move to supported_productive only after the declared gates pass and the change is approved.
- **Canonical owner:** `docs/current/DEFINITION-OF-DONE.md`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:docs/current/DEFINITION-OF-DONE.md`
- **Change status:** `status_literal`

## CS-TERM-0013 — research_pending

- **Concept ID:** `CS-CONCEPT-RESEARCH-PENDING`
- **Definition:** the status for a language claim that remains under active research and has not satisfied the applicable promotion gates.
- **Scope:** Canto-span linguistic status vocabulary.
- **Allowed variants:** research pending.
- **Excluded interpretations:** unsupported in every respect; inactive; unavailable.
- **Example:** AA01 remains research_pending while source, panel, or boundary work is incomplete.
- **Canonical owner:** `one current note under grammar/<status>/`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:grammar/`
- **Change status:** `status_literal`

## CS-TERM-0014 — unsupported_generalization

- **Concept ID:** `CS-CONCEPT-UNSUPPORTED-GENERALIZATION`
- **Definition:** the status for a claimed generalization whose current breadth is not supported by the available evidence.
- **Scope:** Canto-span linguistic status vocabulary.
- **Allowed variants:** unsupported generalization.
- **Excluded interpretations:** unattested form; false example; retired identity.
- **Example:** A narrow attested subtype can remain inside an unsupported_generalization note while the broad claim is revised.
- **Canonical owner:** `one current note under grammar/<status>/`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:grammar/`
- **Change status:** `status_literal`

## CS-TERM-0015 — lexicalized_only

- **Concept ID:** `CS-CONCEPT-LEXICALIZED-ONLY`
- **Definition:** the status for a bounded lexical or formulaic inventory that must not be presented as an unrestricted productive pattern.
- **Scope:** Canto-span linguistic status vocabulary.
- **Allowed variants:** lexicalized only.
- **Excluded interpretations:** unproductive in every context; parser heuristic; retired.
- **Example:** FormulaDiscourseUnit is lexicalized_only at the frozen baseline.
- **Canonical owner:** `one current note under grammar/<status>/`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:grammar/`
- **Change status:** `status_literal`

## CS-TERM-0016 — parser_heuristic

- **Concept ID:** `CS-CONCEPT-PARSER-HEURISTIC`
- **Definition:** the status for an internal parser representation that is not asserted as a productive Cantonese construction.
- **Scope:** Canto-span linguistic status vocabulary and parser-representation records.
- **Allowed variants:** parser heuristic.
- **Excluded interpretations:** linguistic construction; productive pattern; verified language fact.
- **Example:** ClauseSpan is documented as a parser_heuristic.
- **Canonical owner:** `one current note under grammar/<status>/`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:grammar/`
- **Change status:** `status_literal`

## CS-TERM-0017 — attestation

- **Concept ID:** `CS-CONCEPT-ATTESTATION`
- **Definition:** a documented occurrence of an exact form in a specified source and context.
- **Scope:** source and corpus evidence statements.
- **Allowed variants:** attested occurrence.
- **Excluded interpretations:** productivity; frequency; broad acceptability; preferred analysis.
- **Example:** The frozen source contains one attestation of the exact form in context.
- **Canonical owner:** `docs/current/GOVERNANCE.md`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:docs/current/GOVERNANCE.md`
- **Change status:** `narrowed_from_core_sle`

## CS-TERM-0018 — productivity

- **Concept ID:** `CS-CONCEPT-PRODUCTIVITY`
- **Definition:** a bounded generalization that extends to novel eligible items or contexts and satisfies the declared productivity gates.
- **Scope:** claims about extension beyond listed tokens.
- **Allowed variants:** productive use.
- **Excluded interpretations:** attestation; frequency; runtime recognition.
- **Example:** The productivity claim is limited to the declared variety, profile, and exclusions.
- **Canonical owner:** `docs/current/DEFINITION-OF-DONE.md`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:docs/current/DEFINITION-OF-DONE.md`
- **Change status:** `narrowed_from_core_sle`

## CS-TERM-0019 — external source support

- **Concept ID:** `CS-CONCEPT-EXTERNAL-SOURCE-SUPPORT`
- **Definition:** verified proposition-level support with an exact locator and a scope that matches the claim.
- **Scope:** published or otherwise independently checkable external sources.
- **Allowed variants:** source support.
- **Excluded interpretations:** topic relevance; bibliographic listing; copied example alone.
- **Example:** The source directly supports the stated boundary and provides an exact locator.
- **Canonical owner:** `docs/current/GOVERNANCE.md`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:docs/current/GOVERNANCE.md`
- **Change status:** `new_project_term`

## CS-TERM-0020 — source-scope match

- **Concept ID:** `CS-CONCEPT-SOURCE-SCOPE-MATCH`
- **Definition:** the relation in which a cited source directly supports the same proposition and bounded scope as the claim.
- **Scope:** claim-source records and promotion review.
- **Allowed variants:** scope match.
- **Excluded interpretations:** same topic; close terminology without boundary support.
- **Example:** The source-scope match is exact for the overt V-唔-V profile.
- **Canonical owner:** `docs/current/DEFINITION-OF-DONE.md`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:docs/current/DEFINITION-OF-DONE.md`
- **Change status:** `new_project_term`

## CS-TERM-0021 — promotion

- **Concept ID:** `CS-CONCEPT-PROMOTION`
- **Definition:** an approved change to a higher linguistic status after every applicable gate passes.
- **Scope:** status transitions.
- **Allowed variants:** status promotion.
- **Excluded interpretations:** implementation; renaming; readiness ranking; passing tests.
- **Example:** The reviewer approves promotion to supported_productive after all gates pass.
- **Canonical owner:** `docs/current/DEFINITION-OF-DONE.md`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:docs/current/DEFINITION-OF-DONE.md`
- **Change status:** `new_project_term`

## CS-TERM-0022 — promotion eligibility

- **Concept ID:** `CS-CONCEPT-PROMOTION-ELIGIBILITY`
- **Definition:** the condition in which all prerequisites for a proposed status promotion are satisfied, before the promotion decision itself.
- **Scope:** promotion review and readiness outputs.
- **Allowed variants:** promotion-ready state, eligible for promotion.
- **Excluded interpretations:** promotion; merge authorization; work availability.
- **Example:** The record is promotion-eligible, but no status change occurs until approval.
- **Canonical owner:** `docs/current/DEFINITION-OF-DONE.md`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:docs/current/DEFINITION-OF-DONE.md`
- **Change status:** `new_project_term`

## CS-TERM-0024 — negative boundary

- **Concept ID:** `CS-CONCEPT-NEGATIVE-BOUNDARY`
- **Definition:** a stated and, when applicable, executable nonmatching case that limits the scope of a claim or detector.
- **Scope:** construction notes, tests, and promotion gates.
- **Allowed variants:** boundary case, negative case.
- **Excluded interpretations:** absence of evidence; random failing input.
- **Example:** The note excludes suppletive 有冇 from the overt V-唔-V profile.
- **Canonical owner:** `docs/current/DEFINITION-OF-DONE.md`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:docs/current/DEFINITION-OF-DONE.md`
- **Change status:** `new_project_term`

## CS-TERM-0025 — held-out validation

- **Concept ID:** `CS-CONCEPT-HELD-OUT-VALIDATION`
- **Definition:** evaluation on sealed material that was not used to define, tune, or select the claim or implementation.
- **Scope:** final promotion and evaluation gates.
- **Allowed variants:** held-out test.
- **Excluded interpretations:** ordinary regression test; review of training examples.
- **Example:** The sealed held-out set passes under the preregistered protocol.
- **Canonical owner:** `docs/current/DEFINITION-OF-DONE.md`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:docs/current/DEFINITION-OF-DONE.md`
- **Change status:** `new_project_term`
