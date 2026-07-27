---
title: "Grammar and Style Rule Plan"
type: design-plan
status: draft
created: 2026-07-27
updated: 2026-07-27
tags:
  - sle
  - language-design
  - grammar
  - style
---
# Grammar and Style Rule Plan

## Rule-development policy

Sentence-length and grammar restrictions are hypotheses until user testing supports them. The pilot can use provisional limits, but the final standard must not copy a limit from another domain without evidence.

## Candidate core rules

### G-01 — State one principal claim per sentence

A sentence can contain necessary conditions or qualifications, but it must have one identifiable main assertion.

**Uncontrolled**

> Although the construction occurs in the corpus, it is infrequent and may be restricted to older speakers, which shows that it is not productive.

**Candidate SLE**

> The construction occurs in the corpus.  
> It is infrequent in this dataset.  
> The current data suggest a possible age restriction.  
> The data do not establish that the construction is unproductive.

### G-02 — Give each pronoun a clear antecedent

Do not use *it*, *this*, *that*, *they*, or *which* when more than one antecedent is plausible. See [[Ambiguity and Referential Clarity]].

### G-03 — Put conditions before instructions or annotation actions

> If the token is a clitic, apply Rule M-12.

### G-04 — Use active voice when the agent is important

> Two annotators reviewed each token.

Passive voice remains permitted when the agent is unknown, irrelevant, or intentionally backgrounded.

### G-05 — Avoid hidden coordination

Do not use one verb to make different claims about coordinated objects when the relationship is unclear.

### G-06 — Repeat a technical noun when repetition prevents ambiguity

Do not replace a controlled term with a loose synonym only for stylistic variety.

### G-07 — Mark comparison sets

State what two forms, populations, datasets, or analyses are compared.

### G-08 — Make negation scope clear

Prefer separate sentences when *not*, *only*, or *unless* can have more than one scope.

### G-09 — Avoid noun stacks that conceal relations

Replace a long noun sequence with explicit prepositional or clausal relations.

### G-10 — Use finite clauses for central claims

Dense nominalizations can hide the agent, evidence, or degree of certainty.

## Sentence-length pilot

Test, rather than assume, the following provisional thresholds:

- procedures and annotation instructions: target 20 words;
- descriptive prose: target 25 words;
- definitions: target 30 words when necessary.

A sentence over the target is not automatically nonconforming. The checker should request review when the sentence also contains multiple clauses, unclear reference, or more than one claim.

## Rule evidence

Each rule proposal must include:

- documented failure cases;
- expected benefit;
- known costs;
- exceptions;
- human evaluation;
- checker feasibility.

Use [[SLE Rule Proposal Template]].
