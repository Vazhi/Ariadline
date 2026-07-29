---
title: "Ariadline Rule Deferral Register v0.1"
type: evaluation-register
status: proposed-test-scope
version: "0.1"
created: 2026-07-28
updated: 2026-07-29
tags: [ariadline, profiles, deferral, narrowing]
---
# Ariadline Rule Deferral Register v0.1

## Purpose

This register gives every current rule exactly one primary disposition for the issue #39 audit. A non-core disposition is not a final rejection. [[Ariadline Profile Applicability Register v0.1]] remains the controlling proposed profile mapping until human governance changes it.

The four audit dispositions are:

- **core candidate** — included in the 12-rule adversarial test core;
- **domain profile** — potentially useful in a bounded genre, method, data practice, or task;
- **local extension** — dependent on a project, publisher, language, theory, terminology authority, or community;
- **defer** — not justified for the reader-benefit core at this stage; retain without promotion, or later retire after evidence and human review.

## Complete 24-rule primary disposition

| Rule | Primary disposition | Destination or rationale |
|---|---|---|
| `SLE-RULE-0001` | defer | The one-principal-message control may create fragmentation and repetition. Test sentence-level burden only after the smaller core is evaluated. |
| `SLE-RULE-0002` | core candidate | Test referential ambiguity as a durable cross-document communication risk. |
| `SLE-RULE-0003` | core candidate | Test recovery of the population, dataset, variety, time, or other claim boundary. |
| `SLE-RULE-0004` | local extension | Preferred-term governance depends on a project's, publisher's, language community's, or theory's legitimate terminology authority and may suppress purposeful contrasts. |
| `SLE-RULE-0005` | core candidate | Test whether locally important definitions reduce material terminological misinterpretation without imposing a universal ontology. |
| `SLE-RULE-0006` | core candidate | Test reconstruction of compared items, dimensions, and measures. |
| `SLE-RULE-0007` | core candidate | Test materially different readings caused by negation, quantifier, restriction, or exception scope. |
| `SLE-RULE-0008` | domain profile | Normative and procedural documents need declared requirement forms; ordinary descriptive or argumentative prose often does not. |
| `SLE-RULE-0009` | domain profile | The attestation/productivity boundary is most relevant to corpus, descriptive, and productivity-claim reporting and depends on locally defined stronger properties. |
| `SLE-RULE-0010` | domain profile | Judgment-reporting fields depend on elicitation, experimental, annotation, and community-governed methods. |
| `SLE-RULE-0011` | core candidate | Test provenance dimensions when example origin, context, modification, or production affects interpretation. |
| `SLE-RULE-0012` | domain profile | Judgment symbols and category labels require method- or publication-specific conventions. |
| `SLE-RULE-0013` | domain profile | Stable identifiers are a document-navigation and publication-infrastructure control, not a universal prose rule. |
| `SLE-RULE-0014` | core candidate | Test dataset/version and transformation identity where evidence depends on a language resource. |
| `SLE-RULE-0015` | core candidate | Test the boundary between named system behavior and claims about speaker knowledge or language structure. |
| `SLE-RULE-0016` | domain profile | Condition-before-action is relevant to instructions and annotation procedures; mandatory order may be unnatural in other rhetorical traditions. |
| `SLE-RULE-0017` | domain profile | One-action steps may help procedures but can increase length and burden when actions form one integrated operation. |
| `SLE-RULE-0018` | defer | Retain as a governance safeguard outside the reader-benefit core. It prevents false certification but is not itself a reader-benefit rule for the P/S comparison. |
| `SLE-RULE-0019` | domain profile | Observation/interpretation separation is method- and epistemology-sensitive and belongs first in research-reporting profiles. |
| `SLE-RULE-0020` | core candidate | Test whether evidential wording avoids stronger force than the stated method and assumptions support. |
| `SLE-RULE-0021` | core candidate | Test bounded negative claims when a search or test space and sensitivity limit materially constrain interpretation. |
| `SLE-RULE-0022` | core candidate | Test whether limitations and counterevidence that change a central claim remain recoverable. |
| `SLE-RULE-0023` | core candidate | Test whether readers can connect a central claim to its actual supporting record or analysis. |
| `SLE-RULE-0024` | domain profile | Interlinear glossing declarations belong in example, documentation, grammar, and glossing profiles using community- or publication-appropriate conventions. |

## Disposition counts

- core candidate: 12;
- domain profile: 9;
- local extension: 1;
- defer: 2;
- total: 24.

`SLE-RULE-0018` is counted as `defer` for the four-way issue #39 audit and remains separately identified as a governance safeguard. This accounting does not remove or weaken the safeguard.

## Proposed bounded profile and extension mapping

| Destination | Rules | Boundary |
|---|---|---|
| Corpus, resource, and software reporting profile | `0009`, with interactions from core candidates `0014`, `0015`, `0021`, `0023` | Attestation, resource identity, system behavior, search sensitivity, and support mapping apply only when the passage makes those claims. |
| Judgment, elicitation, annotation, and experimental reporting profile | `0010`, `0012`, `0019` | Required fields, notation, and observation/interpretation distinctions must follow the declared task, population, method, and community practice. |
| Normative procedure and annotation-instruction profile | `0008`, `0016`, `0017` | Requirement forms and action ordering apply to instructions, not ordinary descriptive or argumentative prose. |
| Document navigation and publication profile | `0013` | Stable identifiers depend on document scale, repeated reference, medium, and publication infrastructure. |
| Linguistic examples and interlinear glossing profile | `0012`, `0024`, with core candidate `0011` when provenance matters | Notation and glossing conventions remain declared and flexible; provenance is tested separately. |
| Local terminology extension | `0004` | A legitimate project, publisher, theory, language, or community authority controls preferred terms and permitted variation. |
| Deferred sentence-structure experiment | `0001` | Do not promote unless benefit over ordinary editing exceeds fragmentation, repetition, and naturalness costs. |
| Governance safeguard outside benefit core | `0018` | Apply to Ariadline conformance claims; do not score it as reader benefit or treat conformance as truth certification. |

## Later profile-test order

1. Corpus, resource, and software reporting.
2. Judgment, elicitation, annotation, and experimental reporting.
3. Normative procedures and annotation instructions.
4. Examples, notation, and interlinear glossing.
5. Navigation and terminology-management aids.
6. Sentence-structure controls only if the minimal core shows sufficient value to justify further testing.

The order limits simultaneous variables. It does not grant authority to one subfield or predetermine promotion.

## Promotion and retirement boundary

A deferred or profiled rule does not enter the universal core merely because it helps one practice. Universal promotion requires cross-document need, advantage beyond ordinary editing, preserved meaning, low burden, and neutrality across theories, methods, languages, accessibility needs, and rhetorical traditions.

Retirement requires an evidence-linked human decision. A rule may be retired when it duplicates a better control, adds no important benefit over ordinary editing, causes material harm or burden, or cannot be narrowed enough to avoid systematic bias.

This register does not change rule text, stabilize a disposition, or amend controlling profile mappings.