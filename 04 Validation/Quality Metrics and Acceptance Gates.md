---
title: "Quality Metrics and Acceptance Gates"
type: validation
status: draft
created: 2026-07-27
updated: 2026-07-27
tags:
  - sle
  - validation
  - quality
---
# Quality Metrics and Acceptance Gates

## Rule-level gates

A candidate rule can become **approved** only when:

- it addresses a documented ambiguity or consistency problem;
- it has compliant, noncompliant, and boundary examples;
- reviewers can apply it with adequate agreement;
- it does not cause a known material change of meaning;
- its exceptions are defined;
- its checker status is declared;
- evaluation shows benefit or a strong operational need.

## Term-level gates

A candidate term entry can become **approved** only when:

- the concept is defined without circularity;
- the scope is declared;
- near-synonyms and contrasts are documented;
- independent readers apply the term consistently;
- the entry does not erase necessary framework differences.

## Pilot release gates

SLE v0.1 requires:

- complete [[Rule Inventory]];
- complete [[Term Inventory]] for the pilot set;
- no unresolved critical link or schema errors;
- expert meaning-preservation review;
- documented evaluation protocol;
- open issue register;
- versioned release package.

## Candidate metrics

The project must set numerical thresholds after baseline measurement. Possible metrics include:

- claim-interpretation accuracy;
- antecedent-resolution accuracy;
- inter-reviewer agreement;
- annotation agreement;
- median revision time;
- checker precision;
- checker recall;
- false-positive rate;
- frequency of meaning-changing rewrites.

## Severity classes

- **Critical:** changes the linguistic claim or evidence force.
- **Major:** creates substantial ambiguity or prevents reproducibility.
- **Minor:** reduces consistency but does not change the core claim.
- **Editorial:** preference with no demonstrated interpretation effect.

Only critical and major issues should justify strict core restrictions.

## Stop rule

Do not promote a rule when evidence is insufficient. Keep the rule as **experimental**, narrow its scope, or remove it.
