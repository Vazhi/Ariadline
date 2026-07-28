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

All entries are fictional procedure tests. They do not represent authentic linguistic writing, real editors, real authorities, real approvals, or human judgments.

## Valid fixture cases

| Case | Fictional communication risk | Expected structural result |
|---|---|---|
| `KTR-001` | theoretical claim with unclear scope | complete P/S records use separate editors, one shared packet, distinct output hashes, clean scorer metadata, and a pre-output scoring-key hash; both preservation records derive to `preserved`; the pair is explicitly selected and may enter simulated reader exposure |
| `KTR-002` | computational report that confuses system output with a language claim | S contains a major claim-content loss; overall result derives to `not preserved`; the pair is not selected or exposed; the adverse result remains visible |
| `KTR-003` | community-governed description with unresolved terminology authority | S contains unresolved material meaning; overall result derives to `not determined`; the pair is not selected or exposed; no success promotion is allowed |

The valid fixture marks all human gates `approved` only as fictional state values to exercise launch-selection logic. It shows that retained excluded records do not automatically block a different eligible selected pair. It does not record real approval.

## Deliberate invalid mutations

The negative fixture introduces:

- missing fixture identity;
- a false non-synthetic flag;
- an advanced human-study state and human-evidence claim;
- a missing gate and an invalid gate state;
- duplicate or incomplete case records;
- missing P/S condition fields and output hashes;
- the same editor in P and S for one meaning record;
- mismatched or missing P/S shared-packet hashes;
- scorer exposure to restricted metadata;
- missing or late scoring-key freeze information;
- missing preservation dimensions and invalid aggregation;
- invalid comparability;
- contaminated, failed, or unresolved pairs marked benefit-eligible;
- ineligible pairs selected for launch;
- reader exposure for unselected, ineligible, or launch-unready pairs;
- hidden adverse outcomes;
- promotion of `not determined` to success;
- attempted launch and parent issue #9 advancement.

## Expected diagnostic classes

1. `ADVERSE_RESULT_NOT_RETAINED`
2. `CASE_ID_INVALID`
3. `CASE_RECORD_INCOMPLETE`
4. `COMPARABILITY_INVALID`
5. `CONDITION_RECORD_INCOMPLETE`
6. `FIXTURE_ID_REQUIRED`
7. `HUMAN_EVIDENCE_CLAIMED`
8. `HUMAN_GATE_MISSING`
9. `HUMAN_GATE_STATE_INVALID`
10. `LAUNCH_SELECTION_INELIGIBLE`
11. `LAUNCH_SELECTION_INVALID`
12. `LAUNCH_WITH_INELIGIBLE_RECORDS`
13. `LAUNCH_WITH_UNRESOLVED_HUMAN_GATES`
14. `NOT_DETERMINED_PROMOTED`
15. `PAIR_ELIGIBILITY_INVALID`
16. `PARENT_STUDY_ADVANCED`
17. `PRESERVATION_AGGREGATION_INVALID`
18. `PRESERVATION_DIMENSIONS_INCOMPLETE`
19. `READER_EXPOSURE_WITH_INELIGIBLE_PAIR`
20. `READER_EXPOSURE_WITH_UNREADY_LAUNCH`
21. `READER_EXPOSURE_WITH_UNSELECTED_PAIR`
22. `SAME_EDITOR_SAME_RECORD`
23. `SCORER_METADATA_LEAK`
24. `SCORING_FREEZE_INVALID`
25. `SHARED_PACKET_HASH_MISMATCH`
26. `STUDY_STATE_ADVANCED`
27. `SYNTHETIC_FLAG_REQUIRED`

The machine-readable manifest records all 50 expected `(code, path)` identities. The self-test compares the full list rather than only the 27 class names.

## Boundary

A synthetic case may demonstrate that a validator accepts or rejects a record shape. It cannot demonstrate that a real passage is eligible, that an edit preserves meaning, that an outcome is beneficial or harmful, or that Ariadline should continue.
