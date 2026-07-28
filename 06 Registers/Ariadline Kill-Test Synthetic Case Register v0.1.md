---
title: "Ariadline Kill-Test Synthetic Case Register v0.1"
type: evaluation-register
status: planning-draft
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags: [ariadline, evaluation, rehearsal, cases]
---
# Ariadline Kill-Test Synthetic Case Register v0.1

All entries are fictional procedure tests. They do not represent authentic linguistic writing, real editors, real authorities, or human judgments.

## Valid fixture cases

| Case | Fictional communication risk | Expected structural result |
|---|---|---|
| `KTR-001` | theoretical claim with unclear scope | P and S use separate editors and the same shared packet; both preservation records derive to `preserved`; pair may be marked eligible inside the synthetic fixture |
| `KTR-002` | computational report that confuses system output with a language claim | S contains a major claim-content loss; overall result derives to `not preserved`; pair and reader exposure remain ineligible; adverse result remains visible |
| `KTR-003` | community-governed description with unresolved terminology authority | S contains unresolved material meaning; overall result derives to `not determined`; pair and reader exposure remain ineligible; no launch or success promotion is allowed |

The fixture itself remains non-launchable because human oversight, permission, authority, accessibility, statistical review, preregistration, and recruitment gates are unresolved.

## Deliberate invalid mutations

The negative fixture introduces:

- a false non-synthetic flag;
- an advanced human-study state;
- a human-evidence claim;
- a missing oversight gate;
- attempted launch with unresolved gates;
- attempted parent issue #9 advancement;
- the same editor in P and S for one meaning record;
- mismatched P/S shared-packet hashes;
- scorer exposure to restricted rule metadata;
- scoring-key freeze after condition-output access;
- preservation results that contradict their dimensions;
- benefit eligibility for failed or unresolved pairs;
- reader exposure for ineligible pairs;
- hidden adverse outcomes;
- promotion of `not determined` to success.

## Expected diagnostic classes

1. `ADVERSE_RESULT_NOT_RETAINED`
2. `HUMAN_EVIDENCE_CLAIMED`
3. `HUMAN_GATE_MISSING`
4. `LAUNCH_WITH_INELIGIBLE_RECORDS`
5. `LAUNCH_WITH_UNRESOLVED_HUMAN_GATES`
6. `NOT_DETERMINED_PROMOTED`
7. `PAIR_ELIGIBILITY_INVALID`
8. `PARENT_STUDY_ADVANCED`
9. `PRESERVATION_AGGREGATION_INVALID`
10. `READER_EXPOSURE_WITH_INELIGIBLE_PAIR`
11. `SAME_EDITOR_SAME_RECORD`
12. `SCORER_METADATA_LEAK`
13. `SCORING_FREEZE_AFTER_OUTPUT`
14. `SHARED_PACKET_HASH_MISMATCH`
15. `STUDY_STATE_ADVANCED`
16. `SYNTHETIC_FLAG_REQUIRED`

## Boundary

A synthetic case may demonstrate that a validator accepts or rejects a record shape. It cannot demonstrate that a real passage is eligible, that an edit preserves meaning, that an outcome is beneficial or harmful, or that Ariadline should continue.
