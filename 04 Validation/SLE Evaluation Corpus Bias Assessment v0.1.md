---
title: "SLE Evaluation Corpus Bias Assessment v0.1"
type: validation-assessment
status: proposed
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - sle
  - validation
  - bias
  - representativeness
---
# SLE Evaluation Corpus Bias Assessment v0.1

## Purpose

This assessment identifies design bias in [[Multi-Domain SLE Evaluation Corpus v0.1]], [[Evaluation Corpus Coverage Matrix v0.1]], and [[Canto-span Evaluation Subset v0.1]].

The assessment prevents a broad-looking constructed corpus from being mistaken for representative evidence.

## Overall judgment

The v0.1 corpus is suitable for internal rule auditing, semantic-equivalence procedure testing, and preparation of later human studies.

It is not suitable for:

- claiming that SLE improves comprehension;
- claiming that SLE preserves meaning across linguistics generally;
- stabilizing a rule or document pattern;
- choosing a universal rhetorical order;
- validating translations or multilingual use;
- treating any named language, theory, or method as adequately represented.

## Source-construction bias

All 16 independent items are project-constructed. Their uncontrolled passages were intentionally written to expose current rules.

Consequences:

- the corpus may make current rules appear more useful than they are;
- missing rules are less likely to appear;
- uncontrolled passages may be less natural than authentic scholarly prose;
- controlled alternatives may contain details that real authors would not have available;
- semantic-equivalence review depends on fictional item briefs created by the same project.

Mitigation:

1. label every item constructed;
2. prohibit effectiveness claims from v0.1;
3. add authentic permission-compatible passages in later versions;
4. require independent authors to confirm intended meaning;
5. preserve rejected rewrites and rule failures.

## English-language and rhetorical bias

Every item is written in English. Named-language contexts do not replace original writing in those languages.

Risks:

- English sentence boundaries may favor `SLE-RULE-0001`;
- English subject and pronoun patterns may overstate referential problems;
- English academic order may make the recommended pattern sequences appear universal;
- normative verbal-form guidance may not transfer directly;
- translated linguistic terminology may hide category distinctions.

Mitigation:

- add non-English-original passages;
- test translated alternatives in both directions;
- record translator decisions separately from linguistic-analysis decisions;
- permit alternative rhetorical order when information relationships remain recoverable;
- do not score naturalness across languages with one English rubric.

## Domain and genre bias

Research reporting, resource documentation, and procedure writing dominate the corpus.

Underrepresented areas include:

- community-authored documentation;
- sociolinguistic ethnography;
- historical linguistics and philology;
- language acquisition;
- clinical and applied linguistics;
- linguistic accessibility materials;
- peer review and editorial correspondence;
- full dictionaries, grammars, articles, and manuals;
- multimodal signed-language examples;
- public-facing linguistic communication.

Mitigation:

- recruit domain owners rather than inventing additional synthetic coverage;
- add full-document and mixed-pattern samples;
- record when a pattern is absent instead of assuming combination solves the gap.

## Theory bias

The corpus names multiple frameworks, but most controlled alternatives favor cautious empirical separation between observation and interpretation.

That separation may be useful across traditions, but it can still conflict with traditions in which description and analysis are intentionally integrated.

Risks:

- theoretical prose may be weakened by excessive qualification;
- framework-internal proof or deduction may be misclassified as empirical overstatement;
- conventional category names may be replaced with awkward neutral paraphrases;
- theory-neutral wording may conceal rather than remove theoretical assumptions.

Mitigation:

- require theory experts to review meaning preservation;
- retain framework terms when defined and necessary;
- test formal proofs, model-theoretic arguments, and qualitative interpretations separately;
- record when a rule should be profile-limited rather than universal.

## Method bias

Many controlled alternatives add counts, denominators, versions, or exclusion rules.

Risks:

- quantitative transparency may be privileged over qualitative adequacy;
- interactional, ethnographic, archival, and formal evidence may be forced into inappropriate record structures;
- unavailable details may make a legitimate passage appear nonconforming;
- short summaries may become overloaded.

Mitigation:

- apply fields only when relevant to interpretation;
- test permitted omissions and immediate cross-references;
- include qualitative and formal methods in independent review;
- measure authoring burden and cohesion, not only claim reconstruction.

## Language and community bias

The corpus names several languages, but no language community supplied or approved the fictional passages.

The ASL and Māori contexts are especially sensitive because naming a community can create a false appearance of representation.

Mitigation:

- retain the explicit fictional-data warning;
- do not use the items as evidence about the named languages;
- seek community review before adding authentic or community-controlled material;
- preserve access, consent, attribution, and governance restrictions;
- permit anonymized or restricted review records where public disclosure is inappropriate.

## Canto-span bias

The Canto-span subset contains 2 of 18 items and is stored separately.

Residual risks:

- project familiarity may lead reviewers to give the subset disproportionate attention;
- Canto-span statuses and parser workflow may appear more operationally complete than other domains;
- repository-based examples may bias SLE toward versioned technical documentation.

Mitigation:

- keep the `SLE-EVAL-CS-*` namespace;
- exclude Canto-span from independent coverage requirements;
- report its findings as adoption or stress-test findings;
- require independent evidence before any Canto-span finding changes SLE.

## Reviewer and authority bias

The current provisional equivalence judgments were authored within the project. They are not independent reviews.

Before an item enters a formal evaluation:

- one reviewer must understand the relevant linguistic domain or method;
- one reviewer must check SLE rule application;
- the source author or an authorized proxy must confirm intended meaning for authentic passages;
- disagreements must remain visible;
- a `not determined` result is acceptable when expertise or source authority is unavailable.

## Selection and publication bias

A corpus can become biased if only successful rewrites remain visible.

The project must retain:

- alternatives rejected for meaning loss;
- items for which no safe rewrite is found;
- rules that add burden without benefit;
- passages that become less natural or less coherent;
- cases where plain editing performs as well as SLE;
- cases where an SLE rule does not apply.

## Minimum gates for corpus v0.2

A later version should not claim improved representativeness until it includes:

1. at least 16 authentic, permission-compatible independent passages;
2. at least 8 passages originally written in languages other than English;
3. at least 4 translated pairs with independent translation review;
4. at least 2 community-authored or community-governed contributions;
5. at least 4 full-document or multi-section samples;
6. at least 4 rejected or unresolved rewrite cases;
7. direct tests of interlinear glossing and a non-Canto-span limitation record;
8. no source project contributing more than 20% of authentic items.

These numbers are corpus-development gates, not normative SLE language rules.

## Disposition

The v0.1 corpus remains **proposed internal evaluation material**. Its diversity is intentional but synthetic. The recorded gaps are part of the deliverable, not reasons to describe the corpus as representative.