---
title: "Evaluation Corpus Items 0009–0012 v0.1"
type: evaluation-corpus-part
status: proposed-internal-audit
version: "0.1"
created: 2026-07-28
updated: 2026-07-28
tags:
  - sle
  - validation
  - evaluation-corpus
---
# Evaluation Corpus Items 0009–0012 v0.1

These project-constructed items belong to [[Multi-Domain SLE Evaluation Corpus v0.1]]. Each authorized meaning brief is declared before the two passages. `Matches brief` is an internal construction check, not independent semantic-equivalence approval.

## SLE-EVAL-0009 — Signed-language resource access

- **Meaning brief:** `SLE-BRIEF-0009`
- **Brief authority:** project-constructed evaluation specification; no external source-author authority
- **Provenance:** project-constructed fictional editorial test item
- **Domain:** signed-language documentation
- **Method:** community-reviewed video corpus
- **Illustrative context:** Illustrative Signed Language J
- **Framework prompt:** language documentation
- **Genre:** resource documentation
- **Pattern:** `SLE-PATTERN-0010`
- **Rules tested:** `SLE-RULE-0003`, `SLE-RULE-0011`, `SLE-RULE-0013`, `SLE-RULE-0014`, `SLE-RULE-0019`, `SLE-RULE-0022`, `SLE-RULE-0023`

### Authorized meaning brief

> Fictional Release 1.2 has 84 hours from three regional adult participant groups recorded from 2019 to 2023. Searchable metadata are public; video access requires approval. Minors and ceremonial events are excluded.

### Uncontrolled draft

> The signed-language corpus is open and represents the whole signing community.

### Proposed controlled alternative

> Fictional Release 1.2 contains 84 hours of video from three regional adult participant groups recorded between 2019 and 2023. The release excludes participants under 18 and ceremonial community events. Metadata are publicly searchable, but video access requires approval under the fictional community deposit agreement.

### Pair audit

- **Length:** 11 → 45 words (+34); 1 → 3 sentences (+2)
- **Structure and terminology:** Replaces open and whole community with release scope, exclusions, and access conditions.
- **Uncontrolled-to-brief result:** does not match brief
- **Controlled-to-brief internal result:** matches brief
- **Literal passage-to-passage equivalence:** not equivalent by design when the uncontrolled draft overstates or obscures the authorized brief
- **Independent preservation result:** not determined
- **Risk:** Access approval does not imply ethical permission for every downstream use.

## SLE-EVAL-0010 — Annotation decision procedure

- **Meaning brief:** `SLE-BRIEF-0010`
- **Brief authority:** project-constructed evaluation specification; no external source-author authority
- **Provenance:** project-constructed fictional editorial test item
- **Domain:** annotation guidelines
- **Method:** rule-based annotation with adjudication
- **Illustrative context:** Illustrative multilingual annotation project
- **Framework prompt:** dependency annotation
- **Genre:** annotation guideline
- **Pattern:** `SLE-PATTERN-0007`
- **Rules tested:** `SLE-RULE-0001`, `SLE-RULE-0004`, `SLE-RULE-0005`, `SLE-RULE-0007`, `SLE-RULE-0008`, `SLE-RULE-0012`, `SLE-RULE-0013`, `SLE-RULE-0016`, `SLE-RULE-0017`, `SLE-RULE-0022`

### Authorized meaning brief

> Inspect a fixed local context when the target sentence is insufficient. Assign UNCERTAIN if context does not resolve the label. Escalate only when uncertainty affects a required downstream label.

### Uncontrolled draft

> Label uncertain tokens X, check the context, and send difficult cases to the lead annotator.

### Proposed controlled alternative

> If the token cannot be classified from the target sentence, inspect the two preceding and two following sentences. If the context does not resolve the classification, assign UNCERTAIN. Send the record to adjudication only when the uncertainty affects a required downstream label.

### Pair audit

- **Length:** 15 → 42 words (+27); 1 → 3 sentences (+2)
- **Structure and terminology:** Defines the condition, context window, uncertainty label, escalation threshold, and adjudication role.
- **Uncontrolled-to-brief result:** ambiguous relative to brief
- **Controlled-to-brief internal result:** matches brief
- **Literal passage-to-passage equivalence:** not equivalent by design when the uncontrolled draft overstates or obscures the authorized brief
- **Independent preservation result:** not determined
- **Risk:** The fixed two-sentence window is local to the fictional project.

## SLE-EVAL-0011 — Computational model claim

- **Meaning brief:** `SLE-BRIEF-0011`
- **Brief authority:** project-constructed evaluation specification; no external source-author authority
- **Provenance:** project-constructed fictional editorial test item
- **Domain:** computational linguistics
- **Method:** held-out benchmark and cue-conflict test
- **Illustrative context:** Illustrative multilingual benchmark
- **Framework prompt:** model evaluation without an automatic cognition claim
- **Genre:** system description
- **Pattern:** `SLE-PATTERN-0009`
- **Rules tested:** `SLE-RULE-0003`, `SLE-RULE-0006`, `SLE-RULE-0014`, `SLE-RULE-0015`, `SLE-RULE-0019`, `SLE-RULE-0020`, `SLE-RULE-0022`, `SLE-RULE-0023`

### Authorized meaning brief

> Fictional Model M obtains 93% on Test Set T under Configuration C and 61% under a cue-conflict condition. The brief authorizes behavior claims, not a human-like understanding claim.

### Uncontrolled draft

> The model understands long-distance agreement because it gets 93% accuracy.

### Proposed controlled alternative

> Fictional Model M achieved 93% accuracy on Test Set T under Configuration C. Accuracy fell to 61% when the nearest noun phrase contained conflicting agreement cues. These results describe model behavior on the stated test sets; they do not establish human-like understanding of long-distance agreement.

### Pair audit

- **Length:** 10 → 45 words (+35); 1 → 3 sentences (+2)
- **Structure and terminology:** Names the system, test state, contrast, and boundary between performance and cognition.
- **Uncontrolled-to-brief result:** does not match brief
- **Controlled-to-brief internal result:** matches brief
- **Literal passage-to-passage equivalence:** not equivalent by design when the uncontrolled draft overstates or obscures the authorized brief
- **Independent preservation result:** not determined
- **Risk:** A cognition-focused study must define and defend its criterion for understanding.

## SLE-EVAL-0012 — Resource release scope

- **Meaning brief:** `SLE-BRIEF-0012`
- **Brief authority:** project-constructed evaluation specification; no external source-author authority
- **Provenance:** project-constructed fictional editorial test item
- **Domain:** language-resource documentation
- **Method:** curated speech-corpus release
- **Illustrative context:** Illustrative Language K speech corpus
- **Framework prompt:** resource documentation
- **Genre:** resource guide
- **Pattern:** `SLE-PATTERN-0010`
- **Rules tested:** `SLE-RULE-0003`, `SLE-RULE-0004`, `SLE-RULE-0013`, `SLE-RULE-0014`, `SLE-RULE-0021`, `SLE-RULE-0022`, `SLE-RULE-0023`

### Authorized meaning brief

> Fictional Release 2.0 corrects 417 timestamp boundaries and 63 speaker-metadata records from Release 1.4. It adds conversational and broadcast speech from 2017–2024. It excludes child, parliamentary, and clinical speech.

### Uncontrolled draft

> The new corpus fixes the old data and includes all speech styles.

### Proposed controlled alternative

> Fictional Release 2.0 corrects 417 timestamp boundaries and 63 speaker-metadata records from Release 1.4. It adds conversational and broadcast speech recorded from 2017 to 2024. The release does not include child speech, parliamentary debate, or clinical recordings.

### Pair audit

- **Length:** 12 → 39 words (+27); 1 → 3 sentences (+2)
- **Structure and terminology:** Replaces fixes and all speech styles with enumerated corrections, additions, and exclusions.
- **Uncontrolled-to-brief result:** does not match brief
- **Controlled-to-brief internal result:** matches brief
- **Literal passage-to-passage equivalence:** not equivalent by design when the uncontrolled draft overstates or obscures the authorized brief
- **Independent preservation result:** not determined
- **Risk:** Identifier or annotation changes may require a separate compatibility record.
