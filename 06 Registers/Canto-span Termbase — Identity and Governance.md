---
title: "Canto-span Vocabulary Stress-Test Fixture v0.1 — Identity and Governance"
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

# Canto-span Vocabulary Stress-Test Fixture v0.1 — Identity and Governance

Part of [[Canto-span Pilot Termbase v0.1]]. **Non-normative test material:** these entries record Canto-span-specific meanings for stress-testing independently proposed Ariadline rules. They do not define Ariadline terminology or requirements.

## CS-TERM-0001 — construction identity

- **Concept ID:** `CS-CONCEPT-CONSTRUCTION-IDENTITY`
- **Definition:** the permanent record that binds one construction or retained record to its UUID and short code.
- **Scope:** Canto-span identity records; identity persists through ordinary renaming, narrowing, status movement, and runtime changes.
- **Allowed variants:** identity record.
- **Excluded interpretations:** linguistic support; runtime recognition; current name alone.
- **Example:** AA01 keeps the same construction identity after its canonical name changes.
- **Canonical owner:** `docs/current/CONSTRUCTION-IDENTITY.md and data/construction-identities.json`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:data/construction-identities.json`
- **Change status:** `new_project_term`

## CS-TERM-0002 — construction UUID

- **Concept ID:** `CS-CONCEPT-CONSTRUCTION-UUID`
- **Definition:** the globally unique identifier assigned permanently to one construction identity.
- **Scope:** UUID-keyed construction records.
- **Allowed variants:** UUID.
- **Excluded interpretations:** construction code; canonical name; runtime label.
- **Example:** The adjudication applies to UUID 5e10dfc5-15a5-5f5a-b203-37c81a653330.
- **Canonical owner:** `docs/current/CONSTRUCTION-IDENTITY.md and data/construction-identities.json`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:data/construction-identities.json`
- **Change status:** `new_project_term`

## CS-TERM-0003 — construction code

- **Concept ID:** `CS-CONCEPT-CONSTRUCTION-CODE`
- **Definition:** the permanent short code assigned to one construction identity.
- **Scope:** Canto-span short codes such as AA01 and AB30.
- **Allowed variants:** short code.
- **Excluded interpretations:** status label; family ID; version number.
- **Example:** AB30 identifies the same record across documentation revisions.
- **Canonical owner:** `docs/current/CONSTRUCTION-IDENTITY.md and data/construction-identities.json`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:data/construction-identities.json`
- **Change status:** `new_project_term`

## CS-TERM-0004 — canonical name

- **Concept ID:** `CS-CONCEPT-CANONICAL-NAME`
- **Definition:** the currently accepted descriptive name assigned to a construction identity by accepted adjudication.
- **Scope:** UUID-keyed ontology records.
- **Allowed variants:** accepted name.
- **Excluded interpretations:** legacy label; learner label; status.
- **Example:** M4MarkedANotAInterrogative is the canonical name for AA01 at the frozen baseline.
- **Canonical owner:** `docs/current/CONSTRUCTION-ADJUDICATION.md and accepted UUID-keyed adjudication records`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:docs/current/CONSTRUCTION-ADJUDICATION.md`
- **Change status:** `new_project_term`

## CS-TERM-0005 — legacy label

- **Concept ID:** `CS-CONCEPT-LEGACY-LABEL`
- **Definition:** an earlier or compatibility label retained for lookup, runtime compatibility, migration, or provenance.
- **Scope:** legacy note labels and runtime labels.
- **Allowed variants:** legacy runtime label, former name.
- **Excluded interpretations:** canonical name; construction identity; current status.
- **Example:** ANotAQuestion remains a legacy label for AA01.
- **Canonical owner:** `docs/current/CONSTRUCTION-IDENTITY.md and data/construction-identities.json`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:data/construction-identities.json`
- **Change status:** `new_project_term`

## CS-TERM-0006 — construction family

- **Concept ID:** `CS-CONCEPT-CONSTRUCTION-FAMILY`
- **Definition:** a named grouping used to organize related construction identities without transferring evidence or status between them.
- **Scope:** Canto-span family_name fields.
- **Allowed variants:** family.
- **Excluded interpretations:** single construction; evidence inheritance group.
- **Example:** AA01 belongs to the ANotAInterrogatives construction family.
- **Canonical owner:** `docs/current/CONSTRUCTION-IDENTITY.md and data/construction-identities.json`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:data/construction-identities.json`
- **Change status:** `new_project_term`

## CS-TERM-0007 — construction profile

- **Concept ID:** `CS-CONCEPT-CONSTRUCTION-PROFILE`
- **Definition:** the bounded structural or functional scope assigned to one construction identity.
- **Scope:** profile_name and profile_description fields.
- **Allowed variants:** profile.
- **Excluded interpretations:** family; runtime detector; unrestricted language pattern.
- **Example:** VerbM4VerbMatrixOrEmbedded identifies the bounded profile for AA01.
- **Canonical owner:** `docs/current/CONSTRUCTION-IDENTITY.md and data/construction-identities.json`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:data/construction-identities.json`
- **Change status:** `new_project_term`

## CS-TERM-0008 — claim layer

- **Concept ID:** `CS-CONCEPT-CLAIM-LAYER`
- **Definition:** the declared level at which a record makes its principal claim, such as language construction or parser representation.
- **Scope:** identity and research records.
- **Allowed variants:** claim level.
- **Excluded interpretations:** linguistic status; evidence grade; runtime state.
- **Example:** ClauseSpan has a parser-representation claim layer.
- **Canonical owner:** `docs/current/CONSTRUCTION-IDENTITY.md and data/construction-identities.json`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:data/construction-identities.json`
- **Change status:** `new_project_term`

## CS-TERM-0009 — lifecycle state

- **Concept ID:** `CS-CONCEPT-LIFECYCLE-STATE`
- **Definition:** the state that records whether an identity is current or retired.
- **Scope:** construction identity registry.
- **Allowed variants:** record lifecycle.
- **Excluded interpretations:** linguistic status; workflow availability; promotion readiness.
- **Example:** A retired record remains permanently resolvable but is not current.
- **Canonical owner:** `docs/current/CONSTRUCTION-IDENTITY.md and data/construction-identities.json`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:data/construction-identities.json`
- **Change status:** `new_project_term`

## CS-TERM-0010 — canonical owner

- **Concept ID:** `CS-CONCEPT-CANONICAL-OWNER`
- **Definition:** the narrowest authoritative record that controls one state dimension.
- **Scope:** all governed Canto-span state.
- **Allowed variants:** state owner, authoritative record.
- **Excluded interpretations:** most detailed record; latest comment; copied snapshot.
- **Example:** PROJECT-STATE.md is the canonical owner of present-tense work order.
- **Canonical owner:** `docs/current/00-START-HERE.md`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:docs/current/00-START-HERE.md`
- **Change status:** `new_project_term`

## CS-TERM-0023 — adjudication

- **Concept ID:** `CS-CONCEPT-ADJUDICATION`
- **Definition:** an accepted expert decision about construction identity, ontology, naming, profile boundaries, or record disposition.
- **Scope:** UUID-keyed adjudication records.
- **Allowed variants:** expert adjudication.
- **Excluded interpretations:** speaker judgment; status promotion; parser test.
- **Example:** The accepted adjudication changes the canonical name and preserves the UUID.
- **Canonical owner:** `docs/current/CONSTRUCTION-ADJUDICATION.md and accepted UUID-keyed adjudication records`
- **Frozen reference:** `Vazhi/canto-span@c9dd631739734a5ab886f0b667db9888b0add13b:docs/current/CONSTRUCTION-ADJUDICATION.md`
- **Change status:** `new_project_term`
