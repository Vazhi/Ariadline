---
title: "Normative Language"
type: design
status: revised
created: 2026-07-27
updated: 2026-07-27
aliases:
  - "Ariadline Modality"
tags:
  - ariadline
  - language-design
  - modality
---
# Normative Language

## Purpose

[[Normative Language]] supports consistent distinctions among requirements, prohibitions, recommendations, permissions, capabilities, and factual possibilities.

The proposed normative rule is SLE-RULE-0008 in [[Ariadline Language Rules v0.1]].

## Function before form

A normative document must first declare which verbal forms express these functions:

| Function | Meaning |
|---|---|
| requirement | necessary for declared conformance |
| prohibition | forbidden for declared conformance |
| recommendation | preferred, but a justified exception is possible |
| discouraged practice | normally avoided, but a justified exception is possible |
| permission | an allowed option |
| capability or possibility | what an actor, system, or situation can do or permit factually |

The declared forms must be used consistently when a difference affects conformance.

## Requirement-form decision

Ariadline v0.1 uses **must** and **must not** inside its own draft rule statements. This is a draft-local editorial convention, not a final universal Ariadline requirement.

Two established alternatives are under comparison:

- ISO drafting practice uses **shall** for a requirement, **should** for a recommendation, **may** for permission, and **can** for capability or possibility.
- IETF BCP 14 treats **MUST** and **SHALL** as requirement terms, **SHOULD** as a recommendation term, and **MAY** as permission or optionality.

The final Ariadline reference artifact must select a preferred requirement form only after reader testing, translation review, and comparison across linguistic document types. A profile may link to another declared normative-language system when that choice is explicit.

## Permission and capability

Do not use the same form for permission and capability when the distinction affects interpretation.

**Ambiguous**

> An annotator can omit this field with approval.

**Declared permission**

> An annotator may omit this field with approval.

A quotation may preserve source wording.

## Evidence wording

SLE-RULE-0020 requires evidence wording not to overstate the relationship between evidence and conclusion.

Ariadline v0.1 does **not** define a universal lexical hierarchy for:

- *shows*;
- *supports*;
- *suggests*;
- *is consistent with*;
- *does not establish*;
- *contradicts*.

These expressions can vary by discipline, method, argument type, and local convention. A document should define an evidence expression when its intended force is important and not clear from context.

Editors should ask:

1. What result was directly obtained?
2. What inference connects that result to the conclusion?
3. Which assumptions are required?
4. Which reasonable alternatives remain?
5. Does the chosen wording conceal those alternatives?

## Review expressions

Review these expressions when they lack a defined basis:

- clearly;
- obviously;
- undoubtedly;
- proves;
- seems;
- appears;
- generally;
- typically;
- commonly;
- often;
- rarely.

They are not automatically prohibited. They require a defined comparison, measure, source, or uncertainty function when interpretation depends on one.

## Quantification

Prefer explicit counts, proportions, ranges, or defined categories when available and relevant.

**Weak**

> Speakers generally accept the form.

**Controlled draft**

> Eight of ten participants rated the form 4 or 5 on the five-point scale.

A qualitative study may use a non-numeric description when its method and basis are stated.

## Formal proof

Use *prove* for a formal proof or when a declared inferential method licenses that term.

For empirical claims, state the bounded result and the inference without importing an untested universal evidence-verb scale.
