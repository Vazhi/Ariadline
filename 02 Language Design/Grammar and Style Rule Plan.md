---
title: "Grammar and Style Rule Plan"
type: design-plan
status: revised
created: 2026-07-27
updated: 2026-07-27
tags:
  - ariadline
  - language-design
  - grammar
  - style
---
# Grammar and Style Rule Plan

## Current normative draft

The first independent rule tranche is in [[Ariadline Language Rules v0.1]].

The draft is prose-first and written for a future human reference artifact. It does not require software, machine-readable headers, or Canto-span practices.

## Rule-development policy

A grammar or style restriction remains a hypothesis until:

1. independent sources identify the communication problem;
2. the rule has cross-domain linguistic relevance;
3. reader testing shows improved interpretation or consistency;
4. author testing shows that intended meaning is preserved;
5. theoretical and methodological review finds no unjustified bias.

The final standard must not copy a rule or numeric limit from another domain without evidence that it works for linguistic writing.

## Candidate controls retained in v0.1

### One principal message

Each sentence has one identifiable principal assertion, question, or instruction.

### Clear reference

A referring expression identifies one intended antecedent.

### Conditions before actions

A reader encounters the applicability condition before the procedural action.

### Stable technical terms

A document uses one preferred term for one controlled concept.

### Explicit comparisons

A comparative claim identifies the compared items, dimension, and measure or basis.

### Clear logical scope

Negation, quantification, restriction, and exception have an unambiguous scope.

### Central claims in finite prose

Authors should prefer finite clauses when dense nominalization hides an actor, method, evidence relation, or degree of certainty.

This preference is guidance, not a universal prohibition on nominalization.

## Controls not adopted as universal rules

### Fixed sentence-length limit

Ariadline v0.1 does not define a maximum sentence length.

Sentence length can be an editorial review signal, but a long sentence is not nonconforming only because of its word count. A short sentence can still be ambiguous or overloaded.

### Mandatory active voice

Ariadline v0.1 does not require active voice in all contexts.

Active voice is useful when the actor matters. Passive voice is permitted when the actor is unknown, irrelevant, intentionally backgrounded, or already established.

### Universal nominalization ban

Nominalizations are permitted when they express an established concept clearly. Rewrite only when the nominalization hides a relation needed for interpretation.

### Mandatory visible claim labels

Visible labels can support drafting or teaching, but they are not required for basic conformance. See [[Claim Function Decision Register v0.1]].

## Candidate editing example

**Uncontrolled**

> Although the construction occurs in the corpus, it is infrequent and may be restricted to older speakers, which shows that it is not productive.

**Controlled draft**

> The construction occurs in the corpus.  
> It is infrequent in this dataset.  
> The current data suggest a possible age restriction.  
> The data do not establish that the construction is unproductive.

The revision separates attestation, frequency, a possible population restriction, and a productivity inference.

## Rule evidence

Each rule proposal must include:

- documented failure cases;
- independent cross-domain justification;
- expected reader benefit;
- known costs;
- exceptions and boundary cases;
- precision and neutrality risks;
- reader interpretation evidence;
- author meaning-preservation evidence;
- cross-domain expert review.

Optional tool support can be recorded, but tool feasibility is not an adoption criterion.

Use [[Ariadline Rule Proposal Template]] and record adopted rule IDs in [[Rule Inventory]].
