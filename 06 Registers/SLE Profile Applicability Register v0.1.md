---
title: "SLE Profile Applicability Register v0.1"
type: applicability-register
status: proposed
version: "0.1"
created: 2026-07-27
updated: 2026-07-27
tags:
  - sle
  - profiles
  - conformance
  - applicability
---
# SLE Profile Applicability Register v0.1

## Purpose

This register maps each proposed SLE for Linguistics profile to exact rule IDs in [[SLE for Linguistics Language Rules v0.1]].

A profile name is shorthand only when a declaration also identifies this register version and preserves an auditable record of the rules that were applicable, not applicable, or waived.

The register is human-readable. It does not require software or machine-readable metadata.

## Profile-set identity

- Profile-set version: `SLE-PROFILE-SET-0.1`
- Rule-set version: `SLE for Linguistics Language Rules v0.1`
- Status: proposed

A change to a profile mapping must receive a new profile-set version. A declaration against an earlier profile-set version keeps its original meaning.

## Applicability principles

1. Every profile includes `SLE-Core`.
2. A profile selects an exact rule set; it does not replace the rule text.
3. A rule can contain its own applicability condition. A reviewer records such a rule as **applied** or **not applicable** for the declared conformance object.
4. A rule that applies but is not met is a nonconformity unless a valid waiver covers the departure.
5. A pattern can require additional information without changing the profile rule mapping.
6. A local extension must identify any added or replaced rules separately from this register.

## Exact profile mappings

### SLE-Core

`SLE-Core` contains:

- `SLE-RULE-0001`
- `SLE-RULE-0002`
- `SLE-RULE-0003`
- `SLE-RULE-0004`
- `SLE-RULE-0005`
- `SLE-RULE-0006`
- `SLE-RULE-0007`
- `SLE-RULE-0013`
- `SLE-RULE-0018`
- `SLE-RULE-0022`
- `SLE-RULE-0023`

### SLE-Research

`SLE-Research` contains all `SLE-Core` rules plus:

- `SLE-RULE-0009`
- `SLE-RULE-0010`
- `SLE-RULE-0011`
- `SLE-RULE-0012`
- `SLE-RULE-0014`
- `SLE-RULE-0015`
- `SLE-RULE-0019`
- `SLE-RULE-0020`
- `SLE-RULE-0021`
- `SLE-RULE-0024`

### SLE-Resource

`SLE-Resource` contains all `SLE-Core` rules plus:

- `SLE-RULE-0011`
- `SLE-RULE-0014`
- `SLE-RULE-0015`
- `SLE-RULE-0021`
- `SLE-RULE-0024`

### SLE-Procedure

`SLE-Procedure` contains all `SLE-Core` rules plus:

- `SLE-RULE-0008`
- `SLE-RULE-0016`
- `SLE-RULE-0017`

## Conditional-rule resolution

The following rules commonly require an explicit applicability decision:

| Rule | Apply when the conformance object... |
|---|---|
| `SLE-RULE-0008` | declares requirements, recommendations, permissions, prohibitions, or capabilities |
| `SLE-RULE-0010` | reports speaker, participant, consultant, annotator, or expert judgments |
| `SLE-RULE-0011` | uses linguistic examples whose provenance affects interpretation |
| `SLE-RULE-0012` | uses judgment symbols or category labels |
| `SLE-RULE-0013` | refers to a central example, item, table, or figure more than once |
| `SLE-RULE-0014` | bases a claim on a dataset or language resource |
| `SLE-RULE-0015` | reports software, model, parser, or tool behavior |
| `SLE-RULE-0021` | makes a negative search or test claim |
| `SLE-RULE-0024` | uses interlinear morpheme-by-morpheme glosses |

A review record must state **applied** or **not applicable** for each conditional rule included by the declared profile. A blank entry is not an applicability decision.

## Profile combinations

A conformance object may declare more than one profile. The applicable rule set is the union of the exact mappings.

Example:

`SLE-Research + SLE-Procedure` means all rules in both profiles. Duplicate rule IDs are reviewed once.

A combined profile declaration does not automatically make every conditional rule applicable. The review record still resolves each conditional rule against the actual text.

## Required audit record

A declaration that uses a profile must identify:

1. the SLE reference version;
2. `SLE-PROFILE-SET-0.1` or another controlling profile-set version;
3. the selected profile or profiles;
4. the exact conformance object;
5. each included conditional rule as applied or not applicable;
6. any additional local rule from an extension;
7. any waived applicable rule;
8. the conformance result and review method defined in [[Profiles and Conformance]].

The rule list may appear in the declaration, an appendix, a review form, or another stable referenced record.

## Example resolution record

> Conformance object: Sections 2–4.  
> Reference version: SLE for Linguistics v0.1.  
> Profile set: SLE-PROFILE-SET-0.1.  
> Profile: SLE-Research.  
> Conditional rules applied: SLE-RULE-0011, SLE-RULE-0013, SLE-RULE-0014, SLE-RULE-0021.  
> Conditional rules not applicable: SLE-RULE-0010, SLE-RULE-0012, SLE-RULE-0015, SLE-RULE-0024.  
> Waivers: SLE-RULE-0001 for two identified formula statements.  
> Result: conforms with declared waivers.  
> Review method: independent editorial review.

## Boundary

A profile mapping controls communication review scope only. It does not certify linguistic truth, research quality, ethical adequacy, speaker acceptability, or software correctness.
