---
title: "Canto-span Vocabulary Stress-Test Fixture v0.1 — Runtime and Verification"
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

# Canto-span Vocabulary Stress-Test Fixture v0.1 — Runtime and Verification

Part of [[Canto-span Pilot Termbase v0.1]]. **Non-normative test material:** these entries record Canto-span-specific meanings for stress-testing independently proposed Ariadline rules. They do not define Ariadline terminology or requirements.

## CS-TERM-0034 — runtime recognition

- **Concept ID:** `CS-CONCEPT-RUNTIME-RECOGNITION`
- **Definition:** parser behavior established for specified input, configuration, and code version
- **Scope:** canonical runtime source and executable tests
- **Allowed variants:** parser recognition
- **Excluded interpretations:** linguistic support; speaker acceptability; productivity
- **Example:** At commit abc123, the parser recognizes the fixture as ANotAQuestion.
- **Canonical owner:** `main.js and executable tests`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:main.js | Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:docs/current/TESTING.md`
- **Change status:** `new_project_term`

## CS-TERM-0035 — executable test

- **Concept ID:** `CS-CONCEPT-EXECUTABLE-TEST`
- **Definition:** a repeatable programmatic check with defined input, expected result, and code context
- **Scope:** test suites and verification profiles
- **Allowed variants:** automated test
- **Excluded interpretations:** linguistic evidence; manual assertion; promotion decision
- **Example:** The executable test checks that the detector excludes suppletive 有冇.
- **Canonical owner:** `docs/current/TESTING.md and executable tests`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:docs/current/TESTING.md`
- **Change status:** `new_project_term`

## CS-TERM-0036 — verification result

- **Concept ID:** `CS-CONCEPT-VERIFICATION-RESULT`
- **Definition:** the recorded outcome of a named verifier on a specified commit and configuration
- **Scope:** repository verification reports
- **Allowed variants:** check result, verifier result
- **Excluded interpretations:** general validity; merge approval; promotion
- **Example:** `npm run verify:research` passes at commit abc123.
- **Canonical owner:** `docs/current/TESTING.md and executable tests`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:docs/current/TESTING.md`
- **Change status:** `narrowed_from_core_sle`

## CS-TERM-0037 — implementation-document agreement

- **Concept ID:** `CS-CONCEPT-IMPLEMENTATION-DOCUMENT-AGREEMENT`
- **Definition:** the condition in which the implemented runtime scope and the current documentation describe the same bounded behavior
- **Scope:** completion and promotion gates
- **Allowed variants:** code-document agreement, runtime-research alignment
- **Excluded interpretations:** linguistic truth; source support
- **Example:** The detector and construction note exclude the same suppletive forms.
- **Canonical owner:** `docs/current/DEFINITION-OF-DONE.md`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:docs/current/DEFINITION-OF-DONE.md`
- **Change status:** `new_project_term`
