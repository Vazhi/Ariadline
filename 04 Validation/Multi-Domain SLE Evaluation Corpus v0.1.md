---
title: "Multi-Domain SLE Evaluation Corpus v0.1"
type: evaluation-corpus
status: proposed
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - sle
  - validation
  - evaluation-corpus
  - multi-domain
---
# Multi-Domain SLE Evaluation Corpus v0.1

## Status and authority

This corpus is constructed evaluation material for the proposed SLE for Linguistics reference artifact.

The passages are fictional unless an item explicitly identifies a stable external source. Named languages and research traditions provide evaluation contexts only. The fictional results must not be cited as facts about those languages, communities, theories, datasets, or methods.

A controlled alternative is not automatically better than its uncontrolled passage. Each pair requires semantic-equivalence review under [[SLE Semantic Equivalence Review Template v0.1]] and later reader or author testing under [[Evaluation Framework]].

The coverage and known gaps are recorded in [[Evaluation Corpus Coverage Matrix v0.1]] and [[SLE Evaluation Corpus Bias Assessment v0.1]]. The separately bounded [[Canto-span Evaluation Subset v0.1]] is non-authoritative and does not supply normative justification.

## Corpus design

- Corpus ID: `SLE-EVAL-CORPUS-0.1`
- Independent multi-domain items: 16
- Canto-span stress-test items: 2, stored separately
- Source status of the 16 items: project-constructed editorial test material
- Controlling proposed rules: `SLE-RULE-0001` through `SLE-RULE-0024`
- Controlling profile set: `SLE-PROFILE-SET-0.1`
- Semantic-equivalence state: provisional pending independent review

Each item records provenance, domain, method, theory or framework, language context, genre, uncontrolled text, controlled alternative, tested rules, structural change, semantic-equivalence review, and known risk.

# Independent evaluation items

## SLE-EVAL-0001 — Descriptive grammar scope

- **Provenance:** project-constructed; fictional Cantonese-oriented grammar note
- **Domain:** descriptive grammar
- **Method:** small recorded-text corpus
- **Theory or framework:** framework-neutral description
- **Language context:** Cantonese
- **Genre:** grammar section
- **Pattern:** `SLE-PATTERN-0001`
- **Rules tested:** `SLE-RULE-0003`, `0009`, `0019`, `0020`, `0021`, `0022`, `0023`

### Uncontrolled passage

> The classifier is obligatory in subordinate clauses, and speakers never omit it.

### Proposed controlled alternative

> In the fictional recorded-text sample, the classifier occurs in all 31 subordinate-clause tokens. The sample contains no omission. This result does not establish that every Cantonese speaker requires the classifier in every subordinate-clause context.

### Change record

- one sentence becomes three;
- dataset scope and token count are added from the item brief;
- *obligatory* and *never* are replaced with bounded corpus statements;
- the language-wide claim is removed.

### Equivalence review

- **Result:** provisionally equivalent to the intended bounded corpus claim, not equivalent to a literal universal claim;
- **Preserved:** all observed tokens contain the classifier;
- **Clarified:** corpus observation versus grammatical requirement;
- **Risk:** an author who truly intended a universal claim would reject this alternative.

## SLE-EVAL-0002 — Competing theoretical analyses

- **Provenance:** project-constructed; fictional English syntax argument
- **Domain:** theoretical syntax
- **Method:** analysis of a constructed interpretation contrast
- **Theory or framework:** generative Analysis A compared with type-driven Analysis B
- **Language context:** English
- **Genre:** theoretical analysis
- **Pattern:** `SLE-PATTERN-0003`
- **Rules tested:** `SLE-RULE-0001`, `0005`, `0019`, `0020`, `0022`, `0023`

### Uncontrolled passage

> Example (22) proves that the quantifier raises at LF.

### Proposed controlled alternative

> Under Analysis A, covert quantifier raising derives the reading in Example (22). Analysis B derives the same reading through type shifting. Example (22) is compatible with both analyses and does not distinguish them.

### Change record

- one categorical claim becomes three bounded statements;
- two framework-specific mechanisms are named;
- *proves* is replaced with an explicit compatibility relation.

### Equivalence review

- **Result:** provisionally equivalent only when the author accepts that the example is not uniquely diagnostic;
- **Preserved:** Analysis A derives the reading;
- **Added from item brief:** Analysis B also derives it;
- **Risk:** the rewrite changes the argument if the original author had independent premises excluding Analysis B.

## SLE-EVAL-0003 — Interactional function and frequency

- **Provenance:** project-constructed; fictional Spanish conversation study
- **Domain:** discourse and interactional linguistics
- **Method:** sequential analysis of recorded conversation
- **Theory or framework:** conversation-analytic and functional interpretation
- **Language context:** Spanish
- **Genre:** phenomenon description with analysis
- **Patterns:** `SLE-PATTERN-0002`, `SLE-PATTERN-0003`
- **Rules tested:** `SLE-RULE-0003`, `0006`, `0019`, `0020`, `0022`, `0023`

### Uncontrolled passage

> Speakers use *pues* to manage turns, and it always marks disagreement.

### Proposed controlled alternative

> In the fictional twelve-conversation sample, *pues* occurs at 18 turn transitions. In 11 cases, the following turn displays disagreement with the prior speaker. The sequential analysis treats disagreement as one recurrent function in this sample; it does not classify disagreement as the form's only function.

### Change record

- observation, count, and interpretation are separated;
- *always* becomes a stated 11-of-18 distribution;
- the exclusive functional claim is withdrawn.

### Equivalence review

- **Result:** provisionally equivalent to the item brief;
- **Preserved:** disagreement is recurrent in the analyzed transitions;
- **Risk:** counting turns may oversimplify a qualitative sequential analysis if used without transcript context.

## SLE-EVAL-0004 — Corpus variation comparison

- **Provenance:** project-constructed; fictional Arabic variation study
- **Domain:** corpus and variationist linguistics
- **Method:** stratified corpus comparison
- **Theory or framework:** variationist
- **Language context:** Arabic varieties
- **Genre:** corpus study report
- **Pattern:** `SLE-PATTERN-0004`
- **Rules tested:** `SLE-RULE-0003`, `0006`, `0014`, `0019`, `0020`, `0022`, `0023`

### Uncontrolled passage

> Younger speakers use the innovative form much more often.

### Proposed controlled alternative

> In fictional Corpus D, speakers aged 18–29 produced 42 innovative tokens in 1,100 eligible contexts. Speakers aged 50–69 produced 18 tokens in 970 eligible contexts. The comparison describes this corpus sample and does not by itself establish community-wide age change.

### Change record

- comparison groups, counts, denominators, and corpus identity are added;
- *much more often* becomes a directly inspectable sample comparison;
- population inference is bounded.

### Equivalence review

- **Result:** provisionally equivalent to the sample-level comparison;
- **Preserved:** the younger group has a higher observed proportion;
- **Risk:** the rewrite does not state statistical uncertainty because the fictional brief supplies no model or interval.

## SLE-EVAL-0005 — Typological generalization

- **Provenance:** project-constructed; fictional Turkish–Japanese typology note
- **Domain:** linguistic typology
- **Method:** cross-language feature comparison
- **Theory or framework:** descriptive typology
- **Language context:** Turkish and Japanese
- **Genre:** research summary
- **Pattern:** `SLE-PATTERN-0012`
- **Rules tested:** `SLE-RULE-0003`, `0004`, `0005`, `0006`, `0019`, `0020`, `0022`, `0023`

### Uncontrolled passage

> Turkish and Japanese have the same word order because both are SOV languages.

### Proposed controlled alternative

> In the fictional comparison, both Turkish and Japanese place the object before the verb in the selected neutral transitive clauses. The comparison does not establish that the two languages have identical constituent order in every clause type or discourse context.

### Change record

- the comparison domain is restricted to selected clause types;
- *same word order* is replaced with the observed shared property;
- causal *because* is removed.

### Equivalence review

- **Result:** provisionally equivalent to the intended limited comparison;
- **Preserved:** object-before-verb order in the selected examples;
- **Risk:** the alternative may underrepresent legitimate typological use of the conventional `SOV` label unless the label is defined elsewhere.

## SLE-EVAL-0006 — Elicited translation and analyst gloss

- **Provenance:** project-constructed; fictional Swahili fieldwork note
- **Domain:** field linguistics and elicitation
- **Method:** picture-prompt elicitation
- **Theory or framework:** descriptive field analysis
- **Language context:** Swahili
- **Genre:** fieldwork note
- **Pattern:** `SLE-PATTERN-0006`
- **Rules tested:** `SLE-RULE-0003`, `0010`, `0011`, `0012`, `0013`, `0019`, `0022`, `0023`

### Uncontrolled passage

> The consultant said the verb means “carry,” so the gloss is CARRY.

### Proposed controlled alternative

> During fictional Session F12, Consultant C translated the recorded verb as “carry” after an object-picture prompt. The analyst later assigned the tentative gloss `carry.by.hand`. A follow-up task is required to test whether the verb excludes carrying on the back.

### Change record

- participant translation is separated from analyst gloss;
- session, prompt, and later modification are identified;
- an unresolved semantic boundary is added from the item brief.

### Equivalence review

- **Result:** provisionally equivalent to the documented elicitation event;
- **Preserved:** the participant supplied “carry”;
- **Risk:** the analyst gloss is more specific than the participant translation and must remain tentative.

## SLE-EVAL-0007 — Judgment-task result

- **Provenance:** project-constructed; fictional Korean judgment study
- **Domain:** experimental and judgment research
- **Method:** five-point contextual acceptability task
- **Theory or framework:** framework-neutral experimental report
- **Language context:** Korean
- **Genre:** elicitation or judgment study report
- **Pattern:** `SLE-PATTERN-0005`
- **Rules tested:** `SLE-RULE-0003`, `0006`, `0010`, `0012`, `0019`, `0020`, `0022`, `0023`

### Uncontrolled passage

> Korean speakers reject Sentence (8).

### Proposed controlled alternative

> In the fictional five-point task, 17 of 22 eligible participants rated Sentence (8) as 1 or 2 in the stated context. Three rated it as 4 or 5, and two responses were excluded under the stated attention criterion. The result describes this task and participant sample.

### Change record

- population, task, scale, item, result, and exclusions are made explicit;
- categorical *reject* is replaced with the response distribution.

### Equivalence review

- **Result:** provisionally equivalent to the recorded task result;
- **Preserved:** most eligible participants gave low ratings;
- **Risk:** the controlled wording does not infer categorical unacceptability outside the task.

## SLE-EVAL-0008 — Lexicographic usage label

- **Provenance:** project-constructed; fictional Māori dictionary evidence
- **Domain:** lexicography
- **Method:** interview-corpus review
- **Theory or framework:** corpus-informed lexicography
- **Language context:** Māori
- **Genre:** lexical note
- **Pattern:** `SLE-PATTERN-0008`
- **Rules tested:** `SLE-RULE-0003`, `0004`, `0005`, `0011`, `0013`, `0014`, `0019`, `0020`, `0022`, `0023`

### Uncontrolled passage

> **rere** — rare informal verb meaning “to move quickly.”

### Proposed controlled alternative

> **rere**, fictional Sense 4: ‘to move quickly across a short distance.’ Usage label: informal in the fictional urban-interview subset. Evidence: 9 tokens from 7 speakers recorded between 2018 and 2022. The available subset is insufficient to classify the sense as rare in the wider speech community.

### Change record

- form, sense, definition, usage scope, and evidence are separated;
- *rare* is withdrawn because the fictional evidence cannot support community frequency.

### Equivalence review

- **Result:** provisionally equivalent to the intended sense and local register label;
- **Preserved:** proposed meaning and informal use in the subset;
- **Risk:** the named form and sense are fictional and must not be treated as Māori lexicographic evidence.

## SLE-EVAL-0009 — Signed-language resource and access

- **Provenance:** project-constructed; fictional ASL documentation resource
- **Domain:** signed-language documentation
- **Method:** community-reviewed video corpus
- **Theory or framework:** language documentation
- **Language context:** American Sign Language
- **Genre:** language-resource documentation
- **Pattern:** `SLE-PATTERN-0010`
- **Rules tested:** `SLE-RULE-0003`, `0011`, `0013`, `0014`, `0019`, `0022`, `0023`

### Uncontrolled passage

> The ASL corpus is open and represents the whole signing community.

### Proposed controlled alternative

> Fictional Release 1.2 contains 84 hours of video from three regional participant groups recorded between 2019 and 2023. The release does not include participants under 18 or ceremonial community events. Metadata are publicly searchable, but video access requires approval under the fictional community deposit agreement.

### Change record

- release, temporal scope, participant coverage, exclusions, and access conditions are added;
- *open* and *whole community* are replaced with bounded statements.

### Equivalence review

- **Result:** provisionally equivalent to the intended resource description in the item brief;
- **Preserved:** a substantial resource exists and some metadata are public;
- **Risk:** access permission must not be confused with ethical permission for every downstream use.

## SLE-EVAL-0010 — Annotation decision procedure

- **Provenance:** project-constructed; fictional multilingual dependency annotation guide
- **Domain:** annotation guidelines
- **Method:** rule-based annotation with adjudication
- **Theory or framework:** dependency annotation
- **Language context:** multilingual
- **Genre:** annotation guideline
- **Pattern:** `SLE-PATTERN-0007`
- **Rules tested:** `SLE-RULE-0001`, `0004`, `0005`, `0007`, `0008`, `0012`, `0013`, `0016`, `0017`, `0022`

### Uncontrolled passage

> Label uncertain tokens `X`, check the context, and send difficult cases to the lead annotator.

### Proposed controlled alternative

> If the token cannot be classified from the target sentence, inspect the two preceding and two following sentences. If the context does not resolve the classification, assign `UNCERTAIN`. Send the record to adjudication only when the uncertainty affects a required downstream label.

### Change record

- conditions precede actions;
- three independent actions become separate steps;
- `X`, *difficult*, and *lead annotator* are replaced with defined operational terms.

### Equivalence review

- **Result:** provisionally equivalent to the intended workflow;
- **Preserved:** inspect context, mark unresolved cases, escalate material cases;
- **Risk:** the fixed two-sentence window is item-specific and must not become a universal SLE rule.

## SLE-EVAL-0011 — Computational model claim

- **Provenance:** project-constructed; fictional multilingual NLP experiment
- **Domain:** computational linguistics
- **Method:** held-out benchmark and cue-conflict test
- **Theory or framework:** model evaluation without cognitive equivalence claim
- **Language context:** multilingual benchmark
- **Genre:** system description
- **Pattern:** `SLE-PATTERN-0009`
- **Rules tested:** `SLE-RULE-0003`, `0006`, `0014`, `0015`, `0019`, `0020`, `0022`, `0023`

### Uncontrolled passage

> The model understands long-distance agreement because it gets 93% accuracy.

### Proposed controlled alternative

> Fictional Model M achieved 93% accuracy on Test Set T under Configuration C. Accuracy fell to 61% when the nearest noun phrase contained conflicting agreement cues. These results describe model behavior on the stated test sets; they do not establish human-like understanding of long-distance agreement.

### Change record

- model, test set, configuration, result, and contrast are identified;
- cognitive *understands* is replaced with bounded system behavior.

### Equivalence review

- **Result:** provisionally equivalent to the empirical performance claim, not to the literal cognitive claim;
- **Preserved:** 93% benchmark accuracy;
- **Risk:** if the author's research question is specifically about model cognition, the theoretical criterion for *understanding* must be stated rather than deleted.

## SLE-EVAL-0012 — Speech-corpus release documentation

- **Provenance:** project-constructed; fictional Finnish speech corpus
- **Domain:** language-resource documentation
- **Method:** curated speech-corpus release
- **Theory or framework:** resource documentation
- **Language context:** Finnish
- **Genre:** resource guide
- **Pattern:** `SLE-PATTERN-0010`
- **Rules tested:** `SLE-RULE-0003`, `0004`, `0013`, `0014`, `0021`, `0022`, `0023`

### Uncontrolled passage

> The new corpus fixes the old data and includes all Finnish speech styles.

### Proposed controlled alternative

> Fictional Release 2.0 corrects 417 timestamp boundaries and 63 speaker-metadata records from Release 1.4. It adds conversational and broadcast speech recorded from 2017 to 2024. The release does not include child speech, parliamentary debate, or clinical recordings.

### Change record

- *fixes* is replaced with enumerated corrections;
- *all speech styles* is replaced with included and excluded genres;
- both release identities are stated.

### Equivalence review

- **Result:** provisionally equivalent to the intended release summary;
- **Preserved:** corrections and coverage expansion;
- **Risk:** the controlled version may require a separate migration note if identifiers or annotations changed incompatibly.

## SLE-EVAL-0013 — Learner-facing linguistic explanation

- **Provenance:** project-constructed; fictional Japanese learner explanation
- **Domain:** teaching and learner-facing linguistics
- **Method:** pedagogical explanation with bounded examples
- **Theory or framework:** descriptive pedagogy
- **Language context:** Japanese
- **Genre:** learner-facing explanation
- **Pattern:** `SLE-PATTERN-0012`
- **Rules tested:** `SLE-RULE-0001`, `0002`, `0004`, `0005`, `0007`, `0022`

### Uncontrolled passage

> *wa* is the topic marker, and it tells you what the sentence is about, but it can also mean contrast, so use it when you change the topic.

### Proposed controlled alternative

> In this lesson, *wa* marks the phrase treated as the current discourse topic. In some contexts, *wa* also supports a contrastive interpretation. Changing the discourse topic is one context in which learners may encounter *wa*; it is not a complete usage rule.

### Change record

- definition, contrastive use, and pedagogical advice are separated;
- the final imperative becomes a bounded learner note.

### Equivalence review

- **Result:** provisionally equivalent to the intended introductory explanation;
- **Preserved:** topic and contrast functions;
- **Risk:** the simplified account may still be insufficient for advanced learners or analyses that reject a single topic-marker category.

## SLE-EVAL-0014 — Phonetic measurement procedure

- **Provenance:** project-constructed; fictional Spanish voice-onset-time protocol
- **Domain:** phonetics
- **Method:** acoustic measurement
- **Theory or framework:** laboratory phonetics
- **Language context:** Spanish
- **Genre:** methods or procedure document
- **Pattern:** `SLE-PATTERN-0011`
- **Rules tested:** `SLE-RULE-0004`, `0005`, `0008`, `0013`, `0016`, `0017`, `0022`

### Uncontrolled passage

> Measure VOT at the burst, exclude bad tokens, and average the rest for every speaker.

### Proposed controlled alternative

> For each eligible stop token, mark the release burst and the onset of periodic voicing. Calculate voice onset time as the interval between those landmarks. Exclude a token only when one landmark cannot be identified under the stated acoustic criteria. Then calculate the speaker-level mean from the remaining eligible tokens.

### Change record

- terms and landmarks are defined operationally;
- conditions precede exclusions;
- independent actions become ordered steps;
- *bad tokens* is replaced with an explicit criterion.

### Equivalence review

- **Result:** provisionally equivalent to the intended measurement workflow;
- **Preserved:** burst-to-voicing measurement, exclusions, speaker mean;
- **Risk:** the protocol is fictional and does not settle field-specific choices for prevoicing, multiple bursts, or automated landmarks.

## SLE-EVAL-0015 — Sequential-analysis claim

- **Provenance:** project-constructed; fictional Spanish conversation-analysis note
- **Domain:** conversation analysis
- **Method:** turn-by-turn sequential analysis
- **Theory or framework:** conversation analysis
- **Language context:** Spanish
- **Genre:** data commentary
- **Pattern:** `SLE-PATTERN-0006`
- **Rules tested:** `SLE-RULE-0003`, `0011`, `0013`, `0019`, `0020`, `0022`, `0023`

### Uncontrolled passage

> The pause shows that Speaker B disagrees with Speaker A.

### Proposed controlled alternative

> In fictional Extract 7, a 1.2-second pause occurs before Speaker B gives a qualified response. The analysis treats the pause and qualification as evidence of interactional trouble at this point in the sequence. The extract alone does not establish Speaker B's private mental state.

### Change record

- recorded timing and response form are separated from interpretation;
- *shows disagreement* becomes an explicit sequential-analysis claim;
- mental-state inference is bounded.

### Equivalence review

- **Result:** provisionally equivalent to the stated interactional interpretation;
- **Preserved:** the analyst identifies trouble or resistance;
- **Risk:** replacing *disagreement* with *interactional trouble* may be too weak when later turns explicitly confirm disagreement.

## SLE-EVAL-0016 — Collaborative terminology decision

- **Provenance:** project-constructed; fictional multilingual research collaboration
- **Domain:** collaborative project documentation
- **Method:** editorial terminology decision
- **Theory or framework:** cross-framework collaboration
- **Language context:** multilingual scholarly team
- **Genre:** editorial change or revision note
- **Pattern:** `SLE-PATTERN-0014`
- **Rules tested:** `SLE-RULE-0004`, `0005`, `0008`, `0018`, `0022`, `0023`

### Uncontrolled passage

> We fixed *construction* so everyone should use it now.

### Proposed controlled alternative

> In Terminology Decision T-14, the team selected *construction* as the preferred project term for the defined form–function pairing. The decision does not require contributors to adopt a construction-grammar analysis. Existing passages that use *pattern* remain acceptable when *pattern* refers to a broader descriptive grouping.

### Change record

- changed term, controlled concept, scope, theoretical boundary, and compatibility effect are stated;
- *fixed* and *everyone should use it* are replaced with a bounded project decision.

### Equivalence review

- **Result:** provisionally equivalent to the intended editorial decision;
- **Preserved:** *construction* becomes preferred for one defined concept;
- **Risk:** the decision may still be read as theory-laden unless the definition and non-theoretical use are tested with multiple traditions.

# Corpus-wide semantic-equivalence status

All 16 controlled alternatives are **provisionally equivalent** only to the detailed fictional item briefs represented in their records. Several are deliberately not equivalent to a literal reading of the uncontrolled overstatement. This distinction is intentional: the uncontrolled passage models an ambiguous or unsupported formulation, while the item brief defines the intended bounded claim.

Before reader testing, an independent reviewer must confirm for each item:

1. the item brief genuinely licenses every detail added to the controlled alternative;
2. no evidential, theoretical, population, temporal, normative, or ethical claim was silently changed;
3. any disputed alternative is retained as a review finding rather than forced into the corpus;
4. named-language context is not mistaken for empirical evidence about that language.

# Use restrictions

- Do not cite the fictional data as linguistic evidence.
- Do not infer that an SLE rule is valid because a constructed pair appears clearer.
- Do not describe a controlled alternative as superior before evaluation.
- Do not use the Canto-span subset to define the independent corpus or the SLE rules.
- Do not convert this human-readable corpus into a mandatory machine-readable format.