---
title: "Canto-span A-not-A Worked Example"
type: case-study
status: draft
created: 2026-07-27
updated: 2026-07-27
aliases:
  - "ANotAQuestion SLE Worked Example"
  - "Canto-span Construction Note Worked Example"
tags:
  - sle
  - case-study
  - canto-span
  - grammar-engineering
  - a-not-a
---

# Canto-span A-not-A Worked Example

> [!abstract] Purpose
> This note applies the target [[Simplified Linguistic English|SLE]] system to one live Canto-span construction record. It shows how SLE could make identity, linguistic scope, evidence, software behavior, and unresolved questions easier to distinguish without weakening Canto-span governance.

This note extends [[Canto-span Case Study]] with a construction-level example.

## Baseline

Baseline date: **2026-07-27**

Canto-span records reviewed:

- [`data/construction-identities.json`](https://github.com/Vazhi/canto-span/blob/main/data/construction-identities.json)
- [`grammar/research_pending/ANotAQuestion.md`](https://github.com/Vazhi/canto-span/blob/main/grammar/research_pending/ANotAQuestion.md)
- [`docs/current/PROJECT-STATE.md`](https://github.com/Vazhi/canto-span/blob/main/docs/current/PROJECT-STATE.md)
- [`docs/current/GOVERNANCE.md`](https://github.com/Vazhi/canto-span/blob/main/docs/current/GOVERNANCE.md)
- [`docs/current/DEFINITION-OF-DONE.md`](https://github.com/Vazhi/canto-span/blob/main/docs/current/DEFINITION-OF-DONE.md)

This is a documentation case study. It does not change Canto-span identity, status, evidence, runtime behavior, or promotion eligibility.

## Why this record is useful

The record currently has several independent state dimensions:

| Dimension | Baseline value | Canonical owner |
|---|---|---|
| Permanent identity | UUID `5e10dfc5-15a5-5f5a-b203-37c81a653330`; code `AA01` | construction identity registry |
| Canonical name | `M4MarkedANotAInterrogative` | accepted identity and adjudication data |
| Legacy runtime or note label | `ANotAQuestion` | compatibility and runtime records |
| Claim layer | `language_construction` | identity registry |
| Linguistic status | `research_pending` | current grammar note |
| Runtime state | active, with executable fixtures | parser source and tests |
| Source state | five verified sources are listed | grammar note and research records |
| Panel state | zero eligible responses and zero usable critical-item judgments | active panel records and grammar note |
| Code-document reconciliation | incomplete | grammar note |
| Promotion eligibility | no | [[Quality Metrics and Acceptance Gates|applicable gates]] |

A reader must keep these dimensions separate. This is exactly the type of task that motivates [[Claim-Evidence Matrix|claim classes]], [[Terminology Control|controlled terms]], and [[Profiles and Conformance|document profiles]].

## What Canto-span already does well

### Proposition and limitation pairs

Each listed source has:

- a locator;
- a verification state;
- a statement of what the source supports;
- a statement of what must not be inferred.

This structure is already close to SLE evidence records.

### Explicit implementation limits

The note states that implementation validation is separate from linguistic evidence. It also records that code-document reconciliation remains incomplete.

### Explicit panel deficiencies

The note reports zero eligible panel responses and zero usable judgments for critical contrasts. It does not treat one historical speaker record as sufficient panel evidence.

### Negative and boundary testing

The note identifies a standard executable test file and records positive and boundary counts. This supports implementation review without treating tests as independent linguistic evidence.

## Remaining communication problems

### CP-01 — The authoring title is not the canonical name

The note title is `ANotAQuestion`. The identity registry gives `M4MarkedANotAInterrogative` as the canonical name and retains `ANotAQuestion` as a legacy label.

A reader who opens only the grammar note can mistake the legacy label for the current ontology term.

**SLE improvement:** every construction note should show the permanent code, canonical name, and legacy display label together in the first human-readable section.

### CP-02 — The plain-language claim is not the exact profile

The note says that Cantonese may instantiate the structural family represented by `ANotAQuestion`. The identity registry gives a much narrower profile:

- an overt lexical predicate repeats around 唔;
- the profile can occur as a matrix or embedded interrogative;
- the profile excludes suppletive 有冇;
- the profile excludes lexical 得唔得 and 可唔可以;
- the profile excludes final-未 completion questions;
- the profile excludes arbitrary truncation of disyllabic predicates.

**SLE improvement:** a `[GEN]` statement must contain the bounded profile or link to a profile record that contains it.

### CP-03 — Metadata is precise but cognitively dense

The frontmatter contains many useful fields. A new reader must still know which fields concern:

- identity;
- linguistic support;
- panel evidence;
- corpus evidence;
- implementation;
- workflow;
- promotion.

**SLE improvement:** keep machine-readable fields, but group the human-readable report by claim function and state dimension.

### CP-04 — Counts can be misread as conclusions

The note lists five verified sources and twelve executable tests. Neither count states how many propositions directly support the exact canonical profile.

**SLE improvement:** counts must not substitute for proposition-level evidence statements. Every count should be followed by its direct conclusion and limitation.

### CP-05 — Historical judgment evidence can look current

The note reports one speaker record, but zero eligible panel responses under the current evidence model.

**SLE improvement:** distinguish a historical diagnostic judgment from current role-neutral panel evidence with separate terms and claim classes.

### CP-06 — Runtime success can overshadow unresolved linguistic work

The runtime is active and the standard tests pass, while the status remains `research_pending`, the negative-boundary inventory is incomplete, and code-document reconciliation is pending.

**SLE improvement:** every system-result block must end with a statement of what the result does not establish.

## Target SLE-GE declaration

A fully converted note could start with:

```yaml
sle:
  version: "1.0"
  profile: "SLE-GE"
  conformance_level: "B"
  termbase: "canto-span-1.0"
  document_class: "construction-note"
  claim_classes: [DEF, GEN, ATT, JUD, SYS, STA, LIM, HYP]
  baseline_date: "2026-07-27"
  canonical_identity_owner: "data/construction-identities.json"
  canonical_status_owner: "grammar/research_pending/ANotAQuestion.md"
  checker: "sle-check 1.0"
  waived_rules: []
```

This declaration would describe documentation conformance. It would not certify linguistic truth or promotion eligibility.

## Worked SLE rewrite

### Identity

> `AA01` is the permanent construction code. [DEF]  
> `5e10dfc5-15a5-5f5a-b203-37c81a653330` is the permanent UUID. [DEF]  
> `M4MarkedANotAInterrogative` is the canonical name at the 2026-07-27 baseline. [STA]  
> `ANotAQuestion` is a retained legacy label. [DEF]  
> The legacy label does not define the current linguistic scope. [LIM]

### Exact linguistic claim

> The current candidate profile contains an overt lexical predicate repeated around the negator 唔. [GEN]  
> The profile can function as a matrix interrogative or an embedded interrogative constituent. [GEN]  
> The profile excludes suppletive 有冇. [GEN]  
> The profile excludes the lexeme-specific 得唔得 and 可唔可以 patterns. [GEN]  
> The profile excludes final-未 completion questions. [GEN]  
> The profile does not license arbitrary truncation of disyllabic predicates. [GEN]

These statements describe the candidate scope. They do not state that the profile is productive.

### External-source result

> The note lists five verified external sources. [OBS]  
> The sources directly support selected A-not-A structures, discourse contrasts, attested truncation patterns, and the special negative behavior of 有. [ATT]  
> The source count does not establish that every source supports the complete canonical profile. [LIM]  
> A proposition-level source matrix is still required for promotion. [REQ]

### Panel result

> The current note reports one historical independent-speaker record. [OBS]  
> The current panel model reports zero eligible responses. [JUD]  
> The minimum usable judgment count for each critical item is zero. [JUD]  
> The historical record does not satisfy the current panel gate. [LIM]  
> The record does not establish productivity or complete boundary acceptance. [LIM]

### System result

> The runtime recognizes the legacy label at the baseline version. [SYS]  
> The construction test file contains ten positive cases and two boundary cases. [SYS]  
> All twelve listed executable cases pass according to the note. [SYS]  
> These results establish implementation behavior for the tested inputs. [OBS]  
> These results do not establish speaker acceptance, canonical analysis, or productivity. [LIM]

### Current disposition

> The canonical grammar note records the linguistic status as `research_pending`. [STA]  
> Productive acceptance is not eligible. [STA]  
> The code-document reconciliation is incomplete. [STA]  
> The current-standard reaudit is incomplete. [STA]  
> Runtime activity does not change these linguistic-state facts. [LIM]

### Open research question

> The project must determine which externally documented Cantonese constructions justify the exact scope and boundaries of `M4MarkedANotAInterrogative`. [HYP]  
> Evidence for suppletive, lexeme-specific, final-未, or arbitrary-truncation patterns must not transfer to this profile without a scope-matched decision. [REQ]

## Why the rewrite is better

The rewrite makes each inference boundary explicit:

```text
identity ≠ canonical linguistic scope
canonical name ≠ linguistic status
source count ≠ scope-matched support
attestation ≠ productivity
historical judgment ≠ current panel evidence
test success ≠ linguistic support
runtime activity ≠ promotion
```

The content does not become simpler in the sense of becoming less rigorous. The relationships become easier to inspect.

## Candidate checker rules

### CS-SLE-01 — Canonical identity header

A construction note MUST identify:

- permanent UUID;
- permanent code;
- canonical name;
- legacy labels;
- claim layer;
- canonical identity owner.

The checker should flag a title that uses a legacy label without a nearby canonical-name statement.

### CS-SLE-02 — Exact profile requirement

A `[GEN]` claim MUST identify:

- positive structural criteria;
- language or variety scope;
- important exclusions;
- known lexical or pragmatic restrictions;
- unresolved variation.

### CS-SLE-03 — Source-count limitation

A source count MUST NOT be treated as evidence strength by itself.

The note must provide proposition-level support and scope for each material claim.

### CS-SLE-04 — Judgment denominator

A `[JUD]` statement MUST report an item-level numerator and denominator or link to the canonical item table.

When the eligible denominator is zero, the document MUST NOT make a positive current-panel conclusion.

### CS-SLE-05 — System-language barrier

A `[SYS]` statement MUST NOT directly conclude that a construction is:

- grammatical;
- acceptable;
- attested;
- frequent;
- productive;
- canonical.

An independent evidence statement is required.

### CS-SLE-06 — Status and eligibility consistency

When the status is `research_pending`, the note MUST NOT state that productive acceptance is eligible.

### CS-SLE-07 — Current-state baseline

Every volatile value MUST identify:

- baseline date;
- canonical owner;
- relevant version or commit.

### CS-SLE-08 — Direct limitation

Each evidence block SHOULD end with a direct statement of what the evidence does not establish.

### CS-SLE-09 — Canonical-owner links

Each governed state dimension MUST link to its canonical owner. A copied value is not a new authority.

### CS-SLE-10 — Historical-evidence label

A judgment record that is not eligible under the current panel model MUST be described as historical, diagnostic, or legacy evidence.

## Construction-note target structure

A mature SLE-GE note could use this order:

1. **Identity**
2. **Exact claim**
3. **Current linguistic disposition**
4. **External evidence**
5. **Corpus evidence**
6. **Panel evidence**
7. **Negative and boundary cases**
8. **System behavior**
9. **Inference limits**
10. **Open questions**
11. **Required next evidence**
12. **Change and review history**

This order places the human interpretation path above the dense machine-readable metadata.

## Pilot test

### Materials

Use paired versions of:

- `ANotAQuestion`;
- eleven other notes sampled across all Canto-span statuses;
- one identity adjudication;
- one corpus packet;
- one panel report;
- one parser PR summary.

### Reader questions

Ask readers to identify:

1. the canonical name;
2. the legacy label;
3. the exact candidate profile;
4. the current linguistic status;
5. whether the parser recognizes the profile;
6. what the sources directly establish;
7. what the panel evidence establishes;
8. whether the construction is promotion-eligible;
9. which state owner controls each answer;
10. what evidence is still required.

### Measures

- answer accuracy;
- time to answer;
- confidence calibration;
- number of files opened;
- unsupported inference rate;
- reviewer disagreement;
- authoring time;
- checker false-positive rate.

### Acceptance condition

Adopt a candidate rule only when the SLE version improves reader performance without:

- changing Canto-span policy;
- removing a necessary linguistic distinction;
- materially increasing error-prone authoring work;
- creating unacceptable checker noise.

See [[Evaluation Framework]], [[Pilot Study Design]], and [[Quality Metrics and Acceptance Gates]].

## Recommended first implementation

1. Build the initial Canto-span termbase.
2. Add SLE identity and claim-class headers to twelve pilot construction notes.
3. Rewrite the plain-language claims with exact profile and exclusion statements.
4. Add explicit limitation sentences to source, panel, corpus, and system blocks.
5. Add a lightweight checker for identity, claim class, scope, denominator, baseline, and prohibited inference patterns.
6. Evaluate paired original and SLE versions.
7. Adopt only the rules that pass the pilot gates.

## Safeguards

SLE adoption MUST NOT:

- rename or split the construction without accepted Canto-span adjudication;
- move the linguistic status;
- change the parser;
- reinterpret historical evidence;
- promote the construction;
- duplicate canonical state;
- turn a documentation checker into a linguistic adjudicator.

## Conclusion

`ANotAQuestion` shows why Canto-span is a strong SLE reference implementation.

The project already records the necessary distinctions. A fully developed SLE would make those distinctions more visible, more consistent, and more mechanically reviewable.

The strongest initial benefit would come from three controls:

1. a versioned project termbase;
2. explicit claim classes;
3. mandatory separation of linguistic evidence from system behavior.

## Related notes

- [[Canto-span Case Study]]
- [[Claim-Evidence Matrix]]
- [[Terminology Control]]
- [[Grammar and Style Rule Plan]]
- [[Normative Language]]
- [[Profiles and Conformance]]
- [[Authoring and Conformance Tools]]
- [[Ambiguity and Referential Clarity]]
- [[Evaluation Framework]]
- [[Pilot Study Design]]
- [[Quality Metrics and Acceptance Gates]]
- [[Attestation and Productivity]]
