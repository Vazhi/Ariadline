---
title: "Canto-span Vocabulary Stress-Test Fixture v0.1 — Corpus and Panel"
type: test-fixture-part
normative_status: non-normative
status: proposed
version: "0.1"
created: 2026-07-27
updated: 2026-07-27
tags:
  - ariadline
  - terminology
  - canto-span
  - test-fixture-part
  - non-normative
---

# Canto-span Vocabulary Stress-Test Fixture v0.1 — Corpus and Panel

Part of [[Canto-span Pilot Termbase v0.1]]. **Non-normative test material:** these entries record Canto-span-specific meanings for stress-testing independently proposed Ariadline rules. They do not define Ariadline terminology or requirements.

## CS-TERM-0026 — corpus candidate

- **Concept ID:** `CS-CONCEPT-CORPUS-CANDIDATE`
- **Definition:** an item retrieved mechanically for review, before or after expert classification.
- **Scope:** corpus extraction packets and decision ledgers.
- **Allowed variants:** candidate.
- **Excluded interpretations:** genuine instance; attestation used as evidence.
- **Example:** The query retrieved 1,730 corpus candidates.
- **Canonical owner:** `the applicable extraction packet and decision ledger`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:review-packets/corpus-review/AB30/candidate-ledger.json`
- **Change status:** `new_project_term`

## CS-TERM-0027 — genuine corpus candidate

- **Concept ID:** `CS-CONCEPT-GENUINE-CORPUS-CANDIDATE`
- **Definition:** a corpus candidate that expert review classifies as an instance of the declared construction profile.
- **Scope:** reviewed candidate ledgers.
- **Allowed variants:** genuine candidate, genuine instance.
- **Excluded interpretations:** all query hits; productive type.
- **Example:** Candidate AB30-0004 is classified as genuine for the declared profile.
- **Canonical owner:** `the applicable extraction packet and decision ledger`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:review-packets/corpus-review/AB30/candidate-ledger.json`
- **Change status:** `new_project_term`

## CS-TERM-0028 — false-positive corpus candidate

- **Concept ID:** `CS-CONCEPT-FALSE-POSITIVE-CORPUS-CANDIDATE`
- **Definition:** a corpus candidate that the query retrieved but expert review excludes from the declared construction profile.
- **Scope:** reviewed candidate ledgers.
- **Allowed variants:** false positive.
- **Excluded interpretations:** negative evidence against the language claim; invalid corpus record.
- **Example:** The query hit is retained and classified as false_positive.
- **Canonical owner:** `the applicable extraction packet and decision ledger`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:review-packets/corpus-review/AB30/candidate-ledger.json`
- **Change status:** `new_project_term`

## CS-TERM-0029 — reviewed corpus evidence

- **Concept ID:** `CS-CONCEPT-REVIEWED-CORPUS-EVIDENCE`
- **Definition:** corpus material whose candidates have stable provenance and complete expert classifications for the intended evidence use.
- **Scope:** promotion and discovery gates.
- **Allowed variants:** reviewed corpus packet.
- **Excluded interpretations:** raw extraction; unreviewed hit count.
- **Example:** The packet counts as reviewed corpus evidence after all selected candidates are classified.
- **Canonical owner:** `the applicable extraction packet and decision ledger`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:review-packets/corpus-review/AB30/candidate-ledger.json`
- **Change status:** `new_project_term`

## CS-TERM-0030 — panel instrument

- **Concept ID:** `CS-CONCEPT-PANEL-INSTRUMENT`
- **Definition:** a versioned set of judgment tasks, items, instructions, eligibility rules, and quality controls.
- **Scope:** native-panel research.
- **Allowed variants:** judgment instrument, survey instrument.
- **Excluded interpretations:** response dataset; single question; participant.
- **Example:** Panel instrument PFV01-v2 defines the critical contrasts and quality checks.
- **Canonical owner:** `active versioned native-panel review-packet records`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:review-packets/native-panel/active-v2/panel-review-state.json`
- **Change status:** `new_project_term`

## CS-TERM-0031 — usable judgment

- **Concept ID:** `CS-CONCEPT-USABLE-JUDGMENT`
- **Definition:** one eligible, quality-checked, adjudicated response for one item under the active panel instrument.
- **Scope:** item-level panel evidence.
- **Allowed variants:** usable response.
- **Excluded interpretations:** submission; participant count; historical response without current eligibility.
- **Example:** Item P3 has 27 positive usable judgments out of 30 usable judgments.
- **Canonical owner:** `active versioned native-panel review-packet records`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:review-packets/native-panel/active-v2/panel-review-state.json`
- **Change status:** `new_project_term`

## CS-TERM-0032 — critical item

- **Concept ID:** `CS-CONCEPT-CRITICAL-ITEM`
- **Definition:** a preregistered panel item whose result is required for a promotion or boundary decision.
- **Scope:** active panel instrument and completion gates.
- **Allowed variants:** critical contrast item.
- **Excluded interpretations:** any survey item; optional comment.
- **Example:** Every critical positive and negative item must meet the declared threshold.
- **Canonical owner:** `active versioned native-panel review-packet records`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:review-packets/native-panel/active-v2/panel-review-state.json`
- **Change status:** `new_project_term`

## CS-TERM-0033 — panel adjudication

- **Concept ID:** `CS-CONCEPT-PANEL-ADJUDICATION`
- **Definition:** the documented application of eligibility, quality, exclusion, and interpretation rules to panel responses.
- **Scope:** active panel review packet.
- **Allowed variants:** judgment adjudication.
- **Excluded interpretations:** construction identity adjudication; informal reading of totals.
- **Example:** Panel adjudication excludes ineligible responses before item-level totals are reported.
- **Canonical owner:** `active versioned native-panel review-packet records`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:review-packets/native-panel/active-v2/panel-review-state.json`
- **Change status:** `new_project_term`
