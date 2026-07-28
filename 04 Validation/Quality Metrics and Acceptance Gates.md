---
title: "Quality Metrics and Acceptance Gates"
type: validation
status: revised
created: 2026-07-27
updated: 2026-07-28
tags:
  - ariadline
  - validation
  - quality
---
# Quality Metrics and Acceptance Gates

## Rule-level gates

A candidate rule can move from **proposed** toward **stable** only when:

- it addresses a documented ambiguity or consistency problem;
- it has pass, fail, provisional borderline, and appropriate boundary prompts;
- reviewers can apply it with adequate agreement;
- it does not cause a known material change of authorized meaning;
- its applicability, exceptions, and recommendation boundaries are defined;
- independent cross-domain justification is sufficient for the claimed scope;
- human evaluation shows benefit or a strong low-burden operational need;
- harmful, biased, burdensome, and inconclusive findings are resolved or remain visible.

No software checker is required.

## Term-level gates

A candidate controlled term can become **stable** only when:

- the communication concept is defined without circularity;
- scope is declared;
- near-synonyms and contrasts are documented;
- independent readers apply it consistently;
- it does not erase necessary framework differences;
- theory-sensitive linguistic definitions remain local or explicitly scoped;
- the term does not gain authority merely through glossary or project-fixture inclusion.

## Draft publication gates

A proposed reference-artifact draft requires:

- complete [[Rule Inventory]] for the proposed set;
- complete document-pattern and profile registers for the proposed package;
- no unresolved critical internal-link or authority-hierarchy errors;
- auditable independent rationale and exact traceability for every proposed rule;
- documented human evaluation protocol;
- open issue and deviation registers;
- a versioned readable publication package;
- explicit notice that cross-domain stabilization and effectiveness gates remain open.

## Confirmatory-study launch gates

Confirmatory recruitment requires:

- human-approved administrative, consent, privacy, accessibility, and authority routes;
- valid authentic materials and task-specific condition sets;
- independently reviewed P and S conditions for every publication-relevant comparison;
- authorized U baselines only where registered;
- frozen scoring keys and adjudication procedures;
- a justified sample target;
- exact estimands, models, thresholds, exclusions, subgroup rules, and multiplicity handling;
- immutable protocol, materials, and analysis-plan versions;
- a recorded preregistration identifier and date.

A freeze-ready draft does not satisfy these launch gates.

## Stable publication gates

Stable publication requires evidence beyond draft assembly:

- independent cross-domain justification for every stable normative rule;
- authentic authorized reader and author materials;
- expert or source-author meaning-preservation review;
- reader benefit and unsupported-inference results;
- author safety and burden results;
- reviewability and agreement results;
- multilingual, translation, rhetorical-order, and accessibility evidence appropriate to the claimed scope;
- full-document and combined-pattern evidence;
- adverse rule findings resolved through governance;
- explicit tested scope, limitations, compatibility, and migration information.

## Human evaluation metrics

Primary and supporting metrics include:

- claim-and-scope reconstruction accuracy;
- unsupported inference rate;
- material misinterpretation rate;
- antecedent and logical-scope accuracy;
- limitation and alternative detection;
- confidence calibration;
- reviewer agreement on applicability and final outcomes;
- procedure action accuracy;
- semantic-preservation failure;
- authoring and revision time;
- terminology consistency;
- burden, cohesion, naturalness, repetition, and fragmentation;
- theory, method, language, accessibility, and community bias reports;
- frequency and cause of `not determined` outcomes;
- qualitative failure and dissent cases.

Proposed thresholds and project-level disposition rules are in [[Preregistered Analysis and Decision Plan v0.1|Analysis and Decision Plan Draft v0.1]]. They have no confirmatory authority until human approval, freeze, and immutable preregistration are complete.

## Severity classes

- **Critical:** changes the linguistic claim, evidence force, normative force, access boundary, or another essential authorized meaning.
- **Major:** creates substantial ambiguity, false certainty, invalid conformance interpretation, or a serious reproducibility barrier.
- **Minor:** reduces consistency or efficiency without changing the core authorized meaning.
- **Editorial:** preference with no demonstrated interpretation, safety, or burden effect.

Only critical and major communication problems normally justify strict core restrictions. Repeated minor problems can justify an optional aid or bounded profile control when burden remains low.

## Rule disposition classes

Human evaluation classifies tested rules as:

- beneficial;
- neutral;
- harmful;
- biased;
- burdensome;
- inconclusive.

The classifications and actions are defined in [[Preregistered Analysis and Decision Plan v0.1|Analysis and Decision Plan Draft v0.1]].

## Stop rule

Do not stabilize or silently retain a rule when evidence is insufficient or adverse.

Keep it proposed, narrow it, make it optional, move it to an extension, revise it, suspend it, or remove it according to the observed evidence and governance record.

The current execution state is recorded in [[Evaluation Execution Status v0.1]].
