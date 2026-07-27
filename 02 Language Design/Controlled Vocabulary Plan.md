---
title: "Controlled Vocabulary Plan"
type: design-plan
status: draft
created: 2026-07-27
updated: 2026-07-27
tags:
  - sle
  - language-design
  - vocabulary
---
# Controlled Vocabulary Plan

## Strategy

Do not begin with a fixed 900-word general dictionary. Linguistic prose requires a large technical vocabulary and many framework-specific terms.

Instead, build a layered vocabulary.

### Layer 1 — Core function words and evidence verbs

Control a small set of high-impact words and phrases:

- [[Normative Language|must, should, may, can]];
- [[Claim-Evidence Matrix|shows, supports, suggests, is consistent with]];
- all, each, some, most, no;
- only, at least, at most, exactly;
- before, after, during, if, when, unless.

### Layer 2 — General academic verbs

Prefer direct verbs such as:

- define;
- describe;
- compare;
- include;
- exclude;
- occur;
- contain;
- require;
- permit;
- identify;
- measure;
- annotate.

Evaluate alternatives such as *utilize*, *instantiate*, *operationalize*, and *problematize* by use case. Do not prohibit a technical term only because it is complex.

### Layer 3 — Core linguistic terms

Create controlled entries for cross-subfield terms that often vary in meaning. See [[Term Inventory]].

### Layer 4 — Profile termbases

Create optional term modules for:

- phonetics and phonology;
- morphology;
- syntax;
- semantics and pragmatics;
- sociolinguistics;
- language documentation;
- corpus linguistics;
- computational linguistics.

### Layer 5 — Project extensions

Permit a project termbase for language-specific categories, theory-specific terms, corpus labels, and software entities.

## Development method

1. Collect a representative corpus of linguistic writing.
2. Identify high-frequency and high-confusion terms.
3. Record real ambiguity incidents from review, annotation, or replication.
4. Draft entries with [[SLE Term Entry Template]].
5. Test definitions with target users.
6. approve only entries that improve interpretation or consistency.
7. publish machine-readable and Markdown forms.

## Machine-readable form

Each term should have a stable identifier and fields that can export to JSON, CSV, or a terminology format.

Minimum schema:

```yaml
id: SLE-TERM-0001
preferred: attested
part_of_speech: adjective
definition: "Recorded in an identified source or dataset."
scope: core
status: candidate
```

## Do not confuse simplification with word deletion

The objective is not to minimize vocabulary size. The objective is to control meaning where uncontrolled variation causes errors.
