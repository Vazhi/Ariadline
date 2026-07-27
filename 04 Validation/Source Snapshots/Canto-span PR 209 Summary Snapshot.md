---
title: "Canto-span PR 209 Summary Snapshot"
type: source-snapshot
status: captured
created: 2026-07-27
updated: 2026-07-27
source_class: mutable-github-pr-body
source_repository: Vazhi/canto-span
source_pr: 209
source_head: b802410efc18959c4b539b49cfa24e7fd6d50638
source_merge_commit: c9dd631739734a5ab886f0b667db9888b0add13b
capture_sha256: b3f5983c10e39511e137a5cd1a38f3bff13ea7752246cf4f49a0880442b18d8b
tags:
  - sle
  - validation
  - source-snapshot
  - canto-span
---

# Canto-span PR 209 Summary Snapshot

> [!warning] Snapshot boundary
> This file preserves the pull-request body captured on 2026-07-27. It is not a canonical owner of Canto-span code, state, evidence, or authorization. The source PR can change after capture.

- Source: https://github.com/Vazhi/canto-span/pull/209
- Captured title: `Extract A-not-A and modal polar question detectors`
- Associated head: `b802410efc18959c4b539b49cfa24e7fd6d50638`
- Merge commit: `c9dd631739734a5ab886f0b667db9888b0add13b`
- SHA-256 of the exact captured body below: `b3f5983c10e39511e137a5cd1a38f3bff13ea7752246cf4f49a0880442b18d8b`
- Pilot baseline: [[SLE-GE Canto-span Pilot Baseline v0.1]]

## Captured body

```markdown
<!-- coordination-claim: #208 -->

Parent program: #161
Queue owner: #169
Intake issue: #190
Work claim: #208
Active worker: ChatGPT
Ownership revision: 1

Closes #190
Closes #208

## Outcome

Extract the existing A-not-A, modal/copular A-not-A, acceptability, and tightly coupled polar-question fallbacks into `src/parser/detectors/questions/a-not-a.js` without changing detector order, complement boundaries, spans, traces, parser output, or rendering.

## Final state

- exact head: `b802410efc18959c4b539b49cfa24e7fd6d50638`;
- base: current `main` at `b049dcfe0e8b1bc231725c825a3d42fa1d5da618`;
- one clean commit ahead, zero behind;
- changed files: three;
- `RUNTIME-MODULARIZATION.md` and other task-tracking documentation are unchanged;
- no temporary workflow, transformer, parity harness, source map, cache, or migration-only verifier remains.

The final source and generated-runtime blobs are byte-identical to the previously validated extraction. Rebasing changed only the parent commit, and the redundant documentation diff was removed.

## Changed files

- `src/parser/detectors/questions/a-not-a.js` — owns ordinary, desiderative, permission, copular, acceptability, 係咪, and sentence-final-咩 polar detector functions;
- `src/plugin-entry.js` — supplies the existing dependencies and preserves dispatch order and routing seams;
- `main.js` — deterministically generated deployment bundle.

## Validation

- pre-extraction unchanged `npm test`: PASS;
- exact source transformation: PASS;
- focused and complete old/new analysis/diagnostic parity: PASS;
- all regression and construction fixture source/context pairs included;
- focused ordinary, desiderative, permission, copular, acceptability, 係咪, sentence-final 咩, and negative-boundary probes included;
- `ANotAQuestion`, `ModalANotAQuestion`, `CopularANotAQuestion`, `AcceptabilityANotA`, and `PolarQuestionFrame` all exercised;
- deterministic build and committed-bundle parity: PASS;
- unchanged post-extraction `npm test`: PASS;
- runtime, package, and manifest versions remain `0.5.216`;
- final `git diff --check`: PASS;
- final GitHub coordination and discovery checks rerun on the current head.

## Explicit exclusions

- general transitive-VP ownership beyond the question-owned child;
- wh/completion/experiential/scalar questions owned by #191;
- terminal particle ownership beyond the existing final-咩 routing call seam;
- parser expectation, construction identity/status, evidence, corpus, survey, documentation-state, version, or release changes.

## Merge gate

Do not merge without explicit user approval for PR #209 at the unchanged exact head `b802410efc18959c4b539b49cfa24e7fd6d50638`.
```
