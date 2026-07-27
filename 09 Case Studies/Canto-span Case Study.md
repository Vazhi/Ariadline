---
title: "Canto-span Case Study"
type: case-study
status: draft
created: 2026-07-27
updated: 2026-07-27
aliases:
  - "Canto-span SLE Case Study"
  - "Canto Span Case Study"
tags:
  - sle
  - case-study
  - canto-span
  - grammar-engineering
  - governance
---
# Canto-span Case Study

> [!abstract] Purpose
> This case study evaluates how the Canto-span Cantonese grammar-engineering project could improve by adopting a mature form of [[Simplified Linguistic English|Simplified Linguistic English (SLE)]]. It treats Canto-span as an advanced pilot project, not as an example of weak governance.

## Status of this case study

SLE is still a development project. This note therefore describes a **target-state application** of a future SLE standard. It does not claim that Canto-span currently conforms to SLE.

Baseline reviewed: **2026-07-27**

Repository: [Vazhi/canto-span](https://github.com/Vazhi/canto-span)

Primary documents reviewed:

- [Start here — mandatory project contract](https://github.com/Vazhi/canto-span/blob/main/docs/current/00-START-HERE.md)
- [Project state](https://github.com/Vazhi/canto-span/blob/main/docs/current/PROJECT-STATE.md)
- [Governance, evidence, surveys, and release workflow](https://github.com/Vazhi/canto-span/blob/main/docs/current/GOVERNANCE.md)
- [Definition of Done](https://github.com/Vazhi/canto-span/blob/main/docs/current/DEFINITION-OF-DONE.md)

## Executive conclusion

Canto-span already has strong controls for:

- permanent construction identity;
- linguistic status;
- external evidence;
- corpus review;
- native-panel evidence;
- parser behavior;
- testing;
- workflow ownership;
- merge authorization;
- release consistency.

Its main communication risk is not missing policy. The risk is that a reader must combine many dense, project-specific distinctions before the reader can correctly interpret a claim.

A mature SLE could reduce this risk in five ways:

1. give every important statement an explicit claim function;
2. define project terms in one controlled termbase;
3. separate linguistic support from system behavior in the sentence structure;
4. standardize the form of requirements, evidence reports, limitations, and dispositions;
5. make a useful subset of the documentation mechanically checkable.

The recommended outcome is a reusable **SLE Grammar Engineering Profile**, with Canto-span as its first reference implementation and evaluation corpus.

## Why Canto-span is a strong test case

Canto-span combines several document types that a linguistic controlled language must support:

| Canto-span activity | Communication problem for SLE to solve |
|---|---|
| Linguistic analysis | Separate observations, analyses, hypotheses, and generalizations. |
| Parser development | Separate runtime behavior from claims about Cantonese. |
| Corpus extraction | Separate retrieval, classification, attestation, frequency, and productivity. |
| Speaker-judgment research | Report instrument, item, population, result, and limitations. |
| Construction governance | Keep identity, status, readiness, availability, and implementation distinct. |
| Multi-agent coordination | Write testable instructions with explicit authority and scope. |
| Release management | Prevent public descriptions from exceeding the implemented and evidenced scope. |

This mix makes Canto-span more useful than a simple prose corpus. It tests whether SLE can control both linguistic argumentation and technical procedure without confusing them.

## Baseline strengths

### 1. Canonical state ownership

Canto-span identifies a canonical owner for each state dimension. For example, current project state, linguistic status, runtime recognition, permanent identity, and merge authorization have different owners.

This design is already compatible with [[Design Principles|SLE's separation principle]]. SLE would make the ownership relationship visible in each document that reports a state, rather than requiring the reader to reconstruct it from the project hierarchy.

### 2. Strong evidence boundaries

The project explicitly distinguishes:

- occurrence from productivity;
- parser output from linguistic evidence;
- extraction from expert classification;
- source support from topic relevance;
- panel submission totals from usable item-level judgments;
- passing verification from promotion.

These distinctions closely match the purpose of the [[Claim-Evidence Matrix]].

### 3. Controlled linguistic statuses

Canto-span uses a bounded status vocabulary:

- `supported_productive`
- `provisional_reaudit`
- `provisional`
- `research_pending`
- `unsupported_generalization`
- `lexicalized_only`
- `parser_heuristic`

This is a strong foundation for [[Terminology Control]]. The remaining SLE task is to define what each status asserts, what it does not assert, and which evidence records must accompany it.

### 4. Explicit completion gates

The Definition of Done gives separate gates for:

- identity and ontology;
- source verification;
- corpus review;
- panel evidence;
- negative and boundary tests;
- implementation-document agreement;
- held-out validation;
- public description.

This is more rigorous than a general instruction to “add evidence and tests.” It can be converted into an SLE conformance checklist with minimal conceptual change.

### 5. Recognition of multiple validation dimensions

Canto-span evaluates linguistic support, implementation correctness, subsystem correctness, ontology consistency, evidence quality, and release consistency separately.

This is exactly the type of distinction that SLE should preserve. SLE must not simplify these dimensions into one generic word such as *valid*.

## Communication costs that remain

### CC-01 — High semantic load per sentence

Some policy sentences distinguish several state dimensions at once. The content is correct, but readers must retain multiple contrasts while also interpreting the requirement.

A future SLE rule should normally assign one principal function to each sentence:

- state a fact;
- state a requirement;
- state a limitation;
- explain a rationale;
- identify an owner;
- give a disposition.

### CC-02 — Important claim classes are often implicit

A sentence can describe any of the following:

- a corpus observation;
- an interpretation of that observation;
- a software result;
- a project requirement;
- a governance decision;
- a current-state fact;
- a limitation.

Canto-span usually keeps these meanings conceptually separate. SLE would also make the class visible in the wording and, where useful, in metadata.

### CC-03 — Project-local terms require substantial prior knowledge

Terms such as *promotion*, *readiness*, *available*, *parked*, *adjudicated*, *supported*, and *runtime label* have precise project meanings.

A new reader can incorrectly apply an ordinary-language meaning. For example:

- *available* concerns eligibility for bounded work, not linguistic support;
- *readiness* exposes evidence gaps, not promotion;
- *supported_productive* is a gated project status, not a casual synonym for “probably grammatical”;
- *parser_heuristic* describes a software representation, not a productive language construction.

SLE would require these meanings in a versioned termbase.

### CC-04 — Readers must assemble meaning across canonical documents

The canonical-document system prevents duplicated and contradictory policy. This is a strength. It also means that a reader sometimes needs several documents to answer one question.

SLE would not duplicate the policy. It would require a local statement to identify:

- the state dimension;
- its canonical owner;
- the directly reported value;
- the applicable limitation;
- the relevant cross-reference.

### CC-05 — Current facts and durable rules can look similar

Canto-span correctly separates `PROJECT-STATE.md` from durable governance. SLE could reinforce this separation with explicit document classes:

- **current-state report**;
- **normative policy**;
- **historical provenance**;
- **research record**;
- **system report**.

A linter could then warn when a durable policy document contains an unscoped volatile count or version.

### CC-06 — Normative effect can be distributed across prose

The project uses strong instructions, but a paragraph can contain a requirement, exception, rationale, and prohibition together.

The [[Normative Language]] module would require the writer to identify each effect separately:

- **MUST** — testable requirement;
- **MUST NOT** — testable prohibition;
- **SHOULD** — recommended practice with an allowed exception;
- **MAY** — permission;
- **CAN** — capability only.

### CC-07 — A reader can still collapse adjacent dimensions

Even with explicit governance, these invalid inferences remain easy for an unfamiliar reader:

- test passes → construction is linguistically supported;
- corpus hit exists → construction is productive;
- adjudication recommends a name → status changed;
- readiness score is high → promotion is authorized;
- construction is available → construction is supported;
- PR is green → merge is authorized.

A mature SLE checker could detect some of these inference patterns in summaries and release notes.

## Proposed SLE Grammar Engineering Profile

The proposed profile would extend the profiles in [[Profiles and Conformance]].

### Profile name

**SLE-GE — Grammar Engineering Profile**

### Intended documents

SLE-GE would apply to:

- grammar and construction notes;
- research summaries;
- parser-behavior reports;
- annotation rules;
- corpus-review reports;
- judgment-study reports;
- governance documents;
- issue specifications;
- pull-request summaries;
- release notes.

### Required SLE modules

| Module | Requirement in SLE-GE |
|---|---|
| SLE-Core | Required |
| SLE-Research | Required for linguistic claims |
| SLE-Data | Required for corpus, example, and panel records |
| SLE-Procedure | Required for workflows and annotation instructions |
| System-behavior extension | Required for parser, test, and verifier reports |
| Governance-decision extension | Required for status, identity, disposition, and authorization statements |

### Example conformance declaration

> This document conforms to SLE 1.0, Grammar Engineering Profile, Level B, with Canto-span Termbase 1.0. Project extensions: CS-Identity, CS-Status, and CS-Workflow. Checker: SLE Checker 1.0. Review date: 2026-07-27.

This declaration does not certify that the linguistic analysis is true. It certifies only that the document satisfies the declared language and documentation controls.

## Claim classes for Canto-span

The core classes come from [[Claim-Evidence Matrix]]. Canto-span needs three project extensions.

| Code | Class | Required information | Example use |
|---|---|---|---|
| OBS | Observation | source, method, unit, and scope | A reviewed packet contains two genuine candidates. |
| ATT | Attestation | exact form, source, context, and retrieval method | An example occurs in a named corpus source. |
| JUD | Judgment result | instrument, item, population, numerator, denominator, and result | A critical item received 27 acceptable responses from 30 usable judgments. |
| GEN | Generalization | population or dataset, boundary, and counterevidence policy | A pattern is productive in a declared variety and construction scope. |
| ANA | Analysis | framework, assumptions, alternatives, and evidence | A token receives a specific syntactic analysis. |
| HYP | Hypothesis | prediction and possible falsifier | A proposed boundary predicts rejection under a controlled contrast. |
| NEG | Negative result | search space, method, and sensitivity | No matching candidate was found in a frozen corpus distribution. |
| SYS | System behavior | version or commit, input, configuration, and output | The parser recognizes a fixture. |
| DEF | Definition | term, scope, and distinguishing criteria | `parser_heuristic` is defined as an internal software representation. |
| LIM | Limitation | affected claim and consequence | The corpus packet establishes attestation but not productivity. |
| REQ | Project requirement | actor, action, condition, verification, and exception | A status move MUST update the canonical note. |
| DEC | Governance decision | authority, object, decision, date, and effect | An accepted adjudication changes the canonical name. |
| STA | Current-state fact | canonical owner, timestamp, value, and expiry condition | Runtime version is v0.5.216 at the baseline date. |

### Separation rule

A statement must not use evidence from one class as if it directly establishes another class.

Examples:

- `[SYS]` does not directly establish `[GEN]`.
- `[ATT]` does not directly establish productivity in `[GEN]`.
- `[DEC]` does not directly establish `[SYS]`.
- `[STA]` must not be copied into a durable policy without a date and owner.
- `[REQ]` must not be phrased as if it were a description of current behavior.

## Seed Canto-span termbase

The following entries illustrate the minimum termbase needed for SLE adoption.

| Preferred term | Controlled meaning | Do not infer |
|---|---|---|
| **construction identity** | The permanent UUID and short-code record for a construction or retained record. | Identity does not establish linguistic support or runtime recognition. |
| **canonical name** | The currently accepted name assigned through UUID-keyed adjudication. | A name change does not automatically change status or runtime. |
| **linguistic status** | The current evidence disposition recorded in the canonical status note. | Status does not describe workflow availability or parser behavior. |
| **runtime recognition** | Parser behavior established by source code and executable tests. | Recognition does not establish acceptability, grammaticality, or productivity. |
| **attestation** | Documented occurrence of a form in a specified context. | Attestation does not establish frequency, broad naturalness, or productivity. |
| **productivity** | A bounded generalization that satisfies the declared productivity gates. | Multiple tokens alone do not establish productivity. |
| **available construction** | A current construction that is not in the parking registry and can receive bounded work. | Availability does not mean supported or promotion-ready. |
| **parked construction** | A construction temporarily excluded from normal work selection by the canonical parking registry. | Parking does not change identity, evidence, status, or runtime. |
| **discovery readiness** | A deterministic indication of evidence or boundary gaps. | Readiness does not authorize promotion, assignment, or implementation. |
| **promotion** | A reviewed change to a higher linguistic status after all applicable gates pass. | A test, score, adjudication, or corpus count alone does not promote. |
| **adjudication** | An accepted expert decision about identity or ontology. | Adjudication does not silently move status or change runtime. |
| **parser heuristic** | An internal software representation that is not asserted as a productive Cantonese construction. | The label must not be presented as a language generalization. |
| **external source support** | Verified proposition-level support with an exact locator and matched scope. | Topic relevance or copied examples do not count as direct support. |
| **corpus candidate** | A mechanically retrieved item awaiting or retaining expert classification. | A candidate is not automatically a genuine construction instance. |
| **usable judgment** | An eligible, quality-checked, adjudicated response for one item. | Total submissions do not substitute for item-level usable judgments. |
| **merge authorization** | Explicit user approval for one PR at an unchanged head. | Passing checks, ownership, or elapsed time do not authorize merge. |

Each full term entry should use [[SLE Term Entry Template]] and record prohibited substitutions, scope, examples, and change history.

## Candidate SLE rules derived from the case study

### SLE-GE-01 — State one state dimension per sentence

**Rule:** A sentence that reports project state MUST report one principal state dimension.

**Rationale:** Identity, status, runtime, readiness, availability, and authorization can change independently.

**Compliant**

> The accepted adjudication changes the canonical name. [DEC]  
> The linguistic status remains `research_pending`. [STA]  
> Runtime behavior does not change. [LIM]

**Noncompliant**

> The adjudication accepts the construction and updates it everywhere.

### SLE-GE-02 — Identify the direct evidence type

**Rule:** A material linguistic statement MUST identify whether its direct basis is a source, corpus attestation, judgment result, analysis, or system result.

**Verification:** The claim record contains one claim-class code and one evidence link.

### SLE-GE-03 — Put the scope in the claim

**Rule:** A generalization MUST identify the language variety, construction profile, population or dataset, and important exclusions.

**Noncompliant**

> This construction is productive.

**Compliant**

> In the declared Hong Kong Cantonese profile, the reviewed evidence supports the construction only with the listed lexical and discourse restrictions. [GEN]

### SLE-GE-04 — Block system-to-language promotion

**Rule:** A `[SYS]` statement MUST NOT use *prove*, *confirm*, *validate*, or *support* with a linguistic object unless an independent linguistic evidence statement follows.

**Compliant**

> The parser recognizes all 18 positive fixtures at commit `abc123`. [SYS]  
> This result establishes implementation coverage only. [LIM]

### SLE-GE-05 — Separate retrieval from classification

**Rule:** A corpus report MUST distinguish retrieved candidates from reviewed genuine instances.

**Compliant**

> The query retrieved 1,730 candidates. [OBS]  
> Expert classification is incomplete. [STA]  
> The candidate total is not evidence for construction frequency. [LIM]

### SLE-GE-06 — Use item-level judgment quantities

**Rule:** A judgment result MUST report the usable numerator and denominator for each critical item or explicitly link to the item-level table.

### SLE-GE-07 — Mark current-state statements

**Rule:** A volatile value MUST identify its canonical owner and baseline date.

**Compliant**

> At the 2026-07-27 baseline, `PROJECT-STATE.md` reports runtime v0.5.216. [STA]

### SLE-GE-08 — Separate requirement, rationale, and exception

**Rule:** A procedural paragraph SHOULD use separate sentences for the required action, its rationale, and any exception.

**Compliant**

> The author MUST record the exact source locator. [REQ]  
> The locator permits independent verification. [ANA]  
> The author MAY use a stable section identifier when the source has no page numbers. [REQ]

### SLE-GE-09 — Identify the canonical owner

**Rule:** A statement that changes or reports governed state MUST identify the canonical record that owns that state.

### SLE-GE-10 — State negative boundaries

**Rule:** A promoted construction MUST include executable nonmatching cases and a prose statement of the excluded scope.

### SLE-GE-11 — Distinguish current and historical material

**Rule:** A historical record MUST identify itself as provenance and MUST NOT use unqualified present-tense wording for superseded state.

### SLE-GE-12 — Report disposition explicitly

**Rule:** A completed work report MUST end with one declared disposition and list the dimensions that changed and did not change.

Possible dispositions can include:

- ACCEPT;
- IMPLEMENTED INFRASTRUCTURE;
- REVISE;
- QUARANTINE;
- SPLIT;
- MERGE;
- SUPERSEDE;
- RETIRE.

## Worked rewrites

The following examples are illustrative SLE rewrites. They are not quotations from the repository.

### Example 1 — Corpus evidence and readiness

**Compressed form**

> AB30 has five reviewed examples, so it is partly ready, and the parser tests pass.

**SLE form**

> The canonical AB30 packet contains five reviewed candidates. [OBS]  
> Two candidates are classified as genuine. [OBS]  
> Three candidates are classified as false positives. [OBS]  
> The two genuine candidates establish attestation in two small user-supplied conversation sources. [ATT]  
> They do not establish broad corpus diversity or productivity. [LIM]  
> The readiness effect is `partial_only` at the 2026-07-27 baseline. [STA]  
> Applicable parser tests pass in the stated runtime version. [SYS]  
> Test success has no independent linguistic-evidence weight. [LIM]

**Improvement**

The reader can identify what was observed, what was inferred, what remains unsupported, and what the software did.

### Example 2 — Adjudication, status, and runtime

**Compressed form**

> Batch 18 internalized two records and narrowed another construction.

**SLE form**

> Accepted Batch 18 changes the ontology disposition of AB18 and AB21 to internalized. [DEC]  
> It retains AB19 and AB20 as retired records. [DEC]  
> It narrows the canonical profile of AB22. [DEC]  
> These decisions do not automatically move a linguistic-status note. [LIM]  
> These decisions do not automatically change parser behavior. [LIM]

**Improvement**

The text prevents a reader from treating an ontology decision as a status migration or code change.

### Example 3 — Verification result

**Compressed form**

> All checks pass, so the change is valid.

**SLE form**

> `npm run verify` passes at commit `abc123`. [SYS]  
> The result establishes that the checked repository invariants pass for that commit. [OBS]  
> The result does not establish linguistic support, promotion, or merge authorization. [LIM]  
> The linguistic disposition remains `research_pending`. [STA]  
> Merge requires explicit approval for the unchanged PR head. [REQ]

**Improvement**

The word *valid* is replaced with the exact dimension that passed.

### Example 4 — Promotion report

**Compressed form**

> The construction now has enough evidence to be supported.

**SLE form**

> The exact claim is limited to the declared construction profile and variety. [GEN]  
> The source ledger contains scope-matched support with exact locators. [OBS]  
> Every corpus candidate used as evidence has a reviewed classification. [OBS]  
> Every critical positive and negative panel item satisfies the declared usable-judgment threshold. [JUD]  
> Negative and boundary cases pass in executable tests. [SYS]  
> The implementation matches the accepted profile. [SYS]  
> Held-out validation passes under the sealed protocol. [OBS]  
> The reviewer approves the status change to `supported_productive`. [DEC]

**Improvement**

The report exposes the evidence chain instead of relying on the vague phrase *enough evidence*.

### Example 5 — Current project state

**Compressed form**

> Canto-span has 133 labels and no promotion-ready constructions.

**SLE form**

> At the 2026-07-27 baseline, the canonical project-state document reports 133 runtime labels. [STA]  
> At the same baseline, it reports zero promotion-ready constructions. [STA]  
> These values are a dated case-study baseline and must not be treated as current after the canonical state changes. [LIM]

**Improvement**

The values remain useful without turning a case study into a competing current-state ledger.

## SLE construction-note schema

A Canto-span construction note that follows SLE-GE should have these sections.

### 1. Identity

- permanent UUID;
- permanent short code;
- canonical name;
- legacy aliases;
- claim layer;
- family;
- predecessor and successor links.

### 2. Current disposition

- linguistic status;
- canonical status owner;
- status decision date;
- status rationale;
- workflow availability;
- runtime recognition state.

These fields must remain separate.

### 3. Exact linguistic claim

- claim-class code;
- language and variety;
- construction profile;
- semantic or pragmatic conditions;
- lexical restrictions;
- excluded analyses;
- known variation.

### 4. External evidence

For each proposition-level record:

- source identifier;
- exact locator;
- directly supported proposition;
- matched scope;
- restrictions;
- contradictions;
- competing analysis;
- verification status.

### 5. Corpus evidence

- frozen source boundary;
- query version;
- candidate namespace;
- total candidates;
- classification totals;
- genuine examples;
- false positives;
- ambiguous and unusable cases;
- direct conclusion;
- limitations.

### 6. Judgment evidence

- instrument identifier and version;
- lock state;
- population and eligibility;
- item identifier;
- task and scale;
- usable numerator and denominator;
- exclusions;
- adjudication status;
- direct conclusion;
- limitations.

### 7. System behavior

- runtime version or commit;
- parser path;
- positive fixtures;
- negative and boundary fixtures;
- shared-subsystem checks;
- held-out status;
- direct result;
- explicit statement of zero independent linguistic-evidence weight.

### 8. Disposition and open questions

- accepted disposition;
- dimensions changed;
- dimensions unchanged;
- unresolved questions;
- next evidence needed;
- reviewer and date.

## SLE pull-request summary schema

A substantive Canto-span PR could use this SLE-GE summary.

```text
Object:
UUID and canonical name:

Purpose:
One-sentence bounded purpose.

Claim classes affected:
ATT / JUD / GEN / ANA / SYS / REQ / DEC / STA / LIM

Canonical owners changed:
List each state dimension and owning file.

Linguistic result:
State only the evidence-supported conclusion.

System result:
State parser, test, or verifier behavior separately.

Scope:
Language variety, construction profile, data boundary, and exclusions.

Evidence:
Exact source, corpus, and panel records.

Validation:
Commands and direct results.

Disposition:
One approved disposition.

Unchanged dimensions:
Identity / status / runtime / readiness / availability / survey / release.

Risks and limitations:
List unresolved questions and non-established conclusions.

Merge authority:
State whether explicit approval is still required.
```

## SLE release-note schema

A release note MUST distinguish:

1. **implemented behavior** — what the released parser does;
2. **linguistic status** — what the project claims about Cantonese;
3. **evidence changes** — what new source, corpus, or panel records exist;
4. **ontology changes** — what names, families, profiles, or identities changed;
5. **limitations** — what remains unsupported or unresolved;
6. **compatibility** — what aliases or retired records remain;
7. **verification** — which profiles passed;
8. **authorization** — which reviewed release decision applies.

This structure directly supports the Canto-span requirement that public documentation must not describe a cleaner, broader, stronger, or newer state than the canonical data and runtime implement.

## Authoring and conformance tools

The [[Authoring and Conformance Tools]] plan could produce a Canto-span-aware checker.

### Machine-checkable controls

The checker could test:

- required document class and conformance metadata;
- approved claim-class codes;
- defined status and governance terms;
- one canonical meaning for each controlled term;
- use of `MUST`, `SHOULD`, `MAY`, and `CAN`;
- missing dates on `[STA]` statements;
- missing scope on `[GEN]` statements;
- missing version, input, or output on `[SYS]` statements;
- missing item-level quantities on `[JUD]` statements;
- missing source locator on external-evidence statements;
- unqualified uses of *valid*, *confirmed*, *proved*, *supported*, and *ready*;
- a system-result sentence followed by an unsupported linguistic conclusion;
- volatile counts copied outside the canonical project-state document;
- a status term used as workflow availability;
- a readiness term used as authorization;
- historical records written as current state;
- release prose that exceeds declared implementation or evidence scope.

### Human-review controls

Software cannot reliably determine:

- whether a source truly supports the proposition;
- whether two sources are independent;
- whether the scope is linguistically appropriate;
- whether a competing analysis is serious;
- whether a constructed contrast is well designed;
- whether a generalization is theoretically justified.

These controls remain human review gates. See [[Quality Metrics and Acceptance Gates]].

### Suggested machine-readable header

```yaml
sle:
  version: "1.0"
  profile: "SLE-GE"
  conformance_level: "B"
  termbase: "canto-span-1.0"
  document_class: "construction-note"
  claim_classes: [ATT, GEN, ANA, SYS, LIM]
  canonical_state_owner: "grammar/research_pending/AB30-....md"
  baseline_date: "2026-07-27"
  checker: "sle-check 1.0"
  waived_rules: []
```

## Adoption plan

### Phase 0 — Preserve the baseline

1. Select one commit as the pilot baseline.
2. Record the current canonical documents and term inventory.
3. Do not change linguistic status or parser behavior during the documentation baseline.
4. Measure current reader performance before rewriting.

### Phase 1 — Build the Canto-span termbase

Start with approximately 40 high-risk terms:

- identity and ontology terms;
- linguistic-status terms;
- evidence terms;
- corpus terms;
- panel terms;
- runtime and verification terms;
- workflow and authorization terms.

Each term must include a preferred designation, definition, scope, prohibited inference, and examples.

### Phase 2 — Draft SLE-GE

1. Select the applicable SLE-Core, SLE-Research, SLE-Data, and SLE-Procedure rules.
2. Add the REQ, DEC, and STA claim classes.
3. Define Canto-span extensions;
4. create conformance and exception records;
5. review the profile for theoretical neutrality.

### Phase 3 — Rewrite a controlled pilot set

Rewrite, without changing policy:

- `00-START-HERE.md`;
- `PROJECT-STATE.md`;
- `GOVERNANCE.md`;
- `DEFINITION-OF-DONE.md`;
- twelve construction notes sampled across all current statuses;
- one corpus-review packet;
- one native-panel packet;
- five substantive PR summaries;
- one release note.

Keep paired original and SLE versions for evaluation.

### Phase 4 — Add a checker

Implement checks in this order:

1. metadata and document class;
2. controlled terminology;
3. normative verbs;
4. claim-class requirements;
5. scope and version fields;
6. prohibited cross-dimension inference patterns;
7. canonical-owner links;
8. stale current-state references.

### Phase 5 — Evaluate

Use the methods in [[Evaluation Framework]] and [[Pilot Study Design]].

### Phase 6 — Adopt incrementally

Adopt SLE-GE first for:

1. new governance documents;
2. new construction notes;
3. substantive PR summaries;
4. release notes;
5. revised legacy documents.

Do not require a repository-wide rewrite before the pilot demonstrates benefit.

## Evaluation design

### Participants

Recruit at least three reader groups:

- project maintainers;
- linguists who do not know Canto-span;
- technically skilled contributors who are not Cantonese specialists.

### Reader tasks

Ask participants to determine:

1. the current linguistic status of a construction;
2. whether the parser recognizes it;
3. what direct evidence supports it;
4. what the evidence does not establish;
5. which record owns the reported state;
6. whether a status move is authorized;
7. whether a PR is merge-authorized;
8. which claim is an observation, analysis, system result, or limitation.

### Primary measures

- answer accuracy;
- time to answer;
- confidence calibration;
- disagreement between reviewers;
- number of documents opened;
- number of unsupported inferences;
- time required to review a PR;
- missing evidence fields;
- authoring time;
- checker precision and recall.

### Acceptance targets

A pilot rule should proceed only when it:

- improves interpretation accuracy or review speed;
- does not remove a necessary linguistic distinction;
- does not create an unacceptable authoring burden;
- can be applied consistently by trained reviewers;
- has acceptable checker false-positive rates when automated.

Exact thresholds should be set before the pilot and recorded in [[Quality Metrics and Acceptance Gates]].

## Expected improvements

### Faster onboarding

A reader could learn the controlled meanings of *status*, *readiness*, *availability*, *runtime recognition*, and *promotion* from one termbase.

### Fewer category errors

Explicit claim classes would reduce accidental movement from parser results to linguistic conclusions and from corpus occurrence to productivity.

### More efficient review

Reviewers could check each sentence against its declared function and required evidence fields.

### Better traceability

A claim could be followed through:

> statement → claim class → evidence record → canonical owner → test or review gate → disposition

### Safer automation

A checker could enforce structural rules without pretending to adjudicate linguistic truth.

### More reliable release communication

Release notes could state exactly what changed in runtime, evidence, identity, status, and limitations.

### Reuse beyond Canto-span

The profile could support other grammar engineering, corpus annotation, parser documentation, and language-resource projects.

## Risks and safeguards

| Risk | Safeguard |
|---|---|
| Claim tags make prose visually heavy. | Require visible tags only where the claim class is not obvious; retain machine-readable metadata elsewhere. |
| Controlled terms freeze disputed analyses. | Control the designation and declared definition, not the theory that must be adopted. |
| Authors write to satisfy the checker rather than communicate. | Keep human comprehension as the primary acceptance measure. |
| The profile duplicates Canto-span governance. | Link to canonical owners and control expression; do not create parallel policy. |
| The termbase becomes too large. | Begin with high-risk terms and add entries only for documented communication failures. |
| SLE produces false confidence. | State that language conformance does not certify linguistic truth. |
| Legacy documents become inconsistent during migration. | Use versioned adoption and explicit conformance declarations. |
| Rewriting changes policy accidentally. | Review paired versions and require semantic-equivalence checks. |

## Non-goals

SLE adoption must not:

- select a Cantonese linguistic theory;
- promote a construction;
- change parser behavior;
- replace source verification;
- replace corpus classification;
- replace native-panel adjudication;
- replace executable tests;
- replace explicit merge authorization;
- make historical material current;
- turn every research uncertainty into a binary rule.

## Recommendation

Use Canto-span as the first reference implementation for SLE-GE.

The pilot should begin with terminology and claim-class controls. These controls address the highest-risk misunderstandings while requiring the least change to Canto-span's underlying governance.

The first empirical question should be:

> Can trained readers determine Canto-span status, evidence, runtime behavior, scope, and authorization more accurately and quickly from SLE-GE documents than from semantically equivalent uncontrolled documents?

A positive result would provide evidence for SLE adoption. A negative or mixed result would identify which controls are unnecessary, too costly, or insufficiently precise.

## Related SLE notes

- [[Project Charter]]
- [[Design Principles]]
- [[SLE Architecture]]
- [[Terminology Control]]
- [[Controlled Vocabulary Plan]]
- [[Grammar and Style Rule Plan]]
- [[Normative Language]]
- [[Claim-Evidence Matrix]]
- [[Linguistic Examples and Glossing]]
- [[Ambiguity and Referential Clarity]]
- [[Profiles and Conformance]]
- [[Authoring and Conformance Tools]]
- [[Corpus and Annotation Interoperability]]
- [[Evaluation Framework]]
- [[Pilot Study Design]]
- [[Quality Metrics and Acceptance Gates]]
- [[Governance and Change Control]]
- [[SLE Rule Proposal Template]]
- [[SLE Term Entry Template]]
- [[SLE Test Case Template]]
- [[Controlled Natural Language]]
- [[Attestation and Productivity]]
