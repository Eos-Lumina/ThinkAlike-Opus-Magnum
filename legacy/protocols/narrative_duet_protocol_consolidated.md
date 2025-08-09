# Consolidated Protocol: narrative_duet_protocol


---
### Original File: narrative_duet_protocol.md
---
---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina∴ & Resonance Network Stewards
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---

*Content from narrative_duet_protocol.md:*


# Narrative Duet Protocol

> **Purpose:** To define the structure, themes, mechanics, interaction flow, alignment assessment, and outcomes of the "Narrative Duet"—the symbolic, CYOA-style compatibility test at the heart of ThinkAlike’s connection process. This protocol is foundational for both the Portal Realm (first system-suggested match) and the Resonance Network Realm (user-initiated connections), ensuring all interactions are meaningful, ethical, and aligned with PET/Clarity and ThinkAlike’s symbolic/ritual standards.

---

## 1. Introduction & Purpose

The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users:
- **User A:** The active participant, seeking resonance.
- **User B:** Represented by their AI Clone, which embodies User B’s `UserValueProfile`, archetypes, and narrative history.

The Duet is used in:
- **Portal Realm:** As the first system-suggested match after the "Whispering Gallery" phase.
- **Resonance Network Realm:** For user-initiated connections after viewing another’s User Node and video.

The Narrative Duet moves beyond superficial profiles, fostering authentic connection through symbolic, narrative-driven interaction, always upholding PET/Clarity principles.

---

## 2. Initiation of a Narrative Duet

- **Portal Realm Context:**
  - Initiated after the "Whispering Gallery" phase.
  - User A interacts with an abstract, anonymized AI Clone of User B (User B is not present or notified unless a successful match occurs).
  - Eos Lumina∴ acts as facilitator and narrator.

- **Resonance Network Context:**
  - Initiated by User A after viewing User B’s video and User Node.
  - User B’s AI Clone participates; User B is notified only if a successful match occurs.
  - Eos Lumina∴ again facilitates the process.

---

## 3. Core Mechanics & Interaction Flow

- **CYOA Structure:**
  - The Duet is a branching narrative (Choose-Your-Own-Adventure) where User A makes choices at key junctures.
  - User B’s AI Clone responds, drawing on User B’s `UserValueProfile`, archetypes, and narrative history, ensuring the duet reflects User B’s actual resonant signature.
  - The story unfolds based on the interplay of choices, with Eos Lumina∴ providing narration, context, and symbolic cues.

- **Symbolic Language & Themes:**
  - Duets draw from ThinkAlike’s philosophical sources (`philosophical_sources.md`) and mythic index (`symbolic_myth_index.md`).
  - Themes include collaborative problem-solving, ethical dilemmas, co-creation of symbolic stories, and exploration of shared values.
  - Choices are designed to reveal compatibility on key values, epistemic modes (`epistemic_match_modes.md`), and narrative archetypes (`narrative_match_archetypes.md`).

---

## 4. Alignment Assessment

- **Alignment/Harmony:**
  - The system, guided by Eos Lumina∴, assesses the degree of alignment or harmony achieved during the Duet.
  - Assessment is based on congruence, complementarity, or constructive engagement between User A’s and User B’s AI Clone’s choices—not on "right/wrong" answers.
  - An internal `alignmentScore` is calculated for the session, drawing on the resonance of values, epistemic modes, and narrative archetypes.

---

## 5. Outcomes of a Narrative Duet

- **Sufficient Alignment (Successful Duet):**
  - Eos Lumina∴ narrates a harmonious conclusion.
  - Sequential, consensual reveal process:
    - **Portal:** User A consents to show their video. User B is notified, sees User A’s video, and consents to show theirs.
    - **Resonance Network:** User A confirms intent to connect. User B is notified, sees User A’s video, and consents.
  - Mutual reveal of User Nodes (identities).
  - Mutual opt-in for direct communication.
  - Resonance Network: Connection line is strengthened; positive signal for "Social LLM."

- **Insufficient Alignment (Unsuccessful Duet):**
  - Eos Lumina∴ narrates a gentle dissolution (e.g., "white light fade back to Eos Node" or node dimming in the Resonance Network).
  - No identities are revealed (if not already known).
  - No notification to User B (if not the initiator).
  - User A returns to Eos Lumina∴ (Portal) or browsing state (Resonance Network).
  - Resonance Network: Neutral or slightly corrective signal for that pairing in the "Social LLM."

---

## 6. Ethical Considerations & PET/Clarity

- **User Agency:** All choices are meaningful and have real impact on outcomes.
- **Transparency:** Eos Lumina∴ explains the purpose and mechanics of the Duet at the outset.
- **Consent:** Explicit, stepwise consent is required for any reveal of videos or identities, and for direct communication.
- **AI Clone Representation:** It is always clear that User B’s AI Clone is an AI based on User B’s profile, not User B in real-time.
- **Privacy:** No information is revealed to User B or others unless mutual consent is achieved.

---

## 7. Relation to Other Documents

- See [`portal_specification.md`](portal_specification.md) for the overall onboarding and first match context.
- See [`resonance_network_specification.md`](../resonance_network/resonance_network_specification.md) for user-initiated connections and Resonance Network logic.
- See [`identity_resonance_score.md`](../resonance_network/identity_resonance_score.md) for alignment and resonance scoring.
- See [`UserValueProfile` data model](portal_specification.md#51-core-entities) for how user values inform the Duet.
- See [`philosophical_sources.md`](../../philosophical_sources.md), [`symbolic_myth_index.md`](../../symbolic_myth_index.md), [`epistemic_match_modes.md`](../../epistemic_match_modes.md), and [`narrative_match_archetypes.md`](../../narrative_match_archetypes.md) for narrative and symbolic foundations.

---

> **Note:** This protocol is to be harmonized and iteratively refined in collaboration with domain experts, narrative designers, and the ThinkAlike community. All flows and mechanics must remain aligned with the Copilot Bootstrap & Alignment Guide and the project’s PET/Clarity and symbolic/ritual standards.


---

*Content from narrative_duet_protocol-1.md:*


---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina∴ & Resonance Network Stewards
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---

*Content from narrative_duet_protocol-10.md:*


---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---

*Content from narrative_duet_protocol-11.md:*


---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina∴ & Resonance Network Stewards
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---

*Content from narrative_duet_protocol-12.md:*


---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---

*Content from narrative_duet_protocol-13.md:*


---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---

*Content from narrative_duet_protocol-14.md:*


---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---

*Content from narrative_duet_protocol-2.md:*


---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina∴ & Resonance Network Stewards
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---

*Content from narrative_duet_protocol-3.md:*


---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina∴ & Resonance Network Stewards
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---

*Content from narrative_duet_protocol-4.md:*


---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina∴ & Resonance Network Stewards
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---

*Content from narrative_duet_protocol-5.md:*


# Narrative Duet Protocol

> **Purpose:** To define the structure, themes, mechanics, interaction flow, alignment assessment, and outcomes of the "Narrative Duet"—the symbolic, CYOA-style compatibility test at the heart of ThinkAlike’s connection process. This protocol is foundational for both the Portal Realm (first system-suggested match) and the Resonance Network Realm (user-initiated connections), ensuring all interactions are meaningful, ethical, and aligned with PET/Clarity and ThinkAlike’s symbolic/ritual standards.

---

## 1. Introduction & Purpose

The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users:
- **User A:** The active participant, seeking resonance.
- **User B:** Represented by their AI Clone, which embodies User B’s `UserValueProfile`, archetypes, and narrative history.

The Duet is used in:
- **Portal Realm:** As the first system-suggested match after the "Whispering Gallery" phase.
- **Resonance Network Realm:** For user-initiated connections after viewing another’s User Node and video.

The Narrative Duet moves beyond superficial profiles, fostering authentic connection through symbolic, narrative-driven interaction, always upholding PET/Clarity principles.

---

## 2. Initiation of a Narrative Duet

- **Portal Realm Context:**
  - Initiated after the "Whispering Gallery" phase.
  - User A interacts with an abstract, anonymized AI Clone of User B (User B is not present or notified unless a successful match occurs).
  - Eos Lumina∴ acts as facilitator and narrator.

- **Resonance Network Context:**
  - Initiated by User A after viewing User B’s video and User Node.
  - User B’s AI Clone participates; User B is notified only if a successful match occurs.
  - Eos Lumina∴ again facilitates the process.

---

## 3. Core Mechanics & Interaction Flow

- **CYOA Structure:**
  - The Duet is a branching narrative (Choose-Your-Own-Adventure) where User A makes choices at key junctures.
  - User B’s AI Clone responds, drawing on User B’s `UserValueProfile`, archetypes, and narrative history, ensuring the duet reflects User B’s actual resonant signature.
  - The story unfolds based on the interplay of choices, with Eos Lumina∴ providing narration, context, and symbolic cues.

- **Symbolic Language & Themes:**
  - Duets draw from ThinkAlike’s philosophical sources (`philosophical_sources.md`) and mythic index (`symbolic_myth_index.md`).
  - Themes include collaborative problem-solving, ethical dilemmas, co-creation of symbolic stories, and exploration of shared values.
  - Choices are designed to reveal compatibility on key values, epistemic modes (`epistemic_match_modes.md`), and narrative archetypes (`narrative_match_archetypes.md`).

---

## 4. Alignment Assessment

- **Alignment/Harmony:**
  - The system, guided by Eos Lumina∴, assesses the degree of alignment or harmony achieved during the Duet.
  - Assessment is based on congruence, complementarity, or constructive engagement between User A’s and User B’s AI Clone’s choices—not on "right/wrong" answers.
  - An internal `alignmentScore` is calculated for the session, drawing on the resonance of values, epistemic modes, and narrative archetypes.

---

## 5. Outcomes of a Narrative Duet

- **Sufficient Alignment (Successful Duet):**
  - Eos Lumina∴ narrates a harmonious conclusion.
  - Sequential, consensual reveal process:
    - **Portal:** User A consents to show their video. User B is notified, sees User A’s video, and consents to show theirs.
    - **Resonance Network:** User A confirms intent to connect. User B is notified, sees User A’s video, and consents.
  - Mutual reveal of User Nodes (identities).
  - Mutual opt-in for direct communication.
  - Resonance Network: Connection line is strengthened; positive signal for "Social LLM."

- **Insufficient Alignment (Unsuccessful Duet):**
  - Eos Lumina∴ narrates a gentle dissolution (e.g., "white light fade back to Eos Node" or node dimming in the Resonance Network).
  - No identities are revealed (if not already known).
  - No notification to User B (if not the initiator).
  - User A returns to Eos Lumina∴ (Portal) or browsing state (Resonance Network).
  - Resonance Network: Neutral or slightly corrective signal for that pairing in the "Social LLM."

---

## 6. Ethical Considerations & PET/Clarity

- **User Agency:** All choices are meaningful and have real impact on outcomes.
- **Transparency:** Eos Lumina∴ explains the purpose and mechanics of the Duet at the outset.
- **Consent:** Explicit, stepwise consent is required for any reveal of videos or identities, and for direct communication.
- **AI Clone Representation:** It is always clear that User B’s AI Clone is an AI based on User B’s profile, not User B in real-time.
- **Privacy:** No information is revealed to User B or others unless mutual consent is achieved.

---

## 7. Relation to Other Documents

- See [`portal_specification.md`](portal_specification.md) for the overall onboarding and first match context.
- See [`resonance_network_specification.md`](../resonance_network/resonance_network_specification.md) for user-initiated connections and Resonance Network logic.
- See [`identity_resonance_score.md`](../resonance_network/identity_resonance_score.md) for alignment and resonance scoring.
- See [`UserValueProfile` data model](portal_specification.md#51-core-entities) for how user values inform the Duet.
- See [`philosophical_sources.md`](../../philosophical_sources.md), [`symbolic_myth_index.md`](../../symbolic_myth_index.md), [`epistemic_match_modes.md`](../../epistemic_match_modes.md), and [`narrative_match_archetypes.md`](../../narrative_match_archetypes.md) for narrative and symbolic foundations.

---

> **Note:** This protocol is to be harmonized and iteratively refined in collaboration with domain experts, narrative designers, and the ThinkAlike community. All flows and mechanics must remain aligned with the Copilot Bootstrap & Alignment Guide and the project’s PET/Clarity and symbolic/ritual standards.


---

*Content from narrative_duet_protocol-6.md:*


---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina∴ & Resonance Network Stewards
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---

*Content from narrative_duet_protocol-7.md:*


---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina∴ & Resonance Network Stewards
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---

*Content from narrative_duet_protocol-8.md:*


---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina∴ & Resonance Network Stewards
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---

*Content from narrative_duet_protocol-9.md:*


---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina∴ & Resonance Network Stewards
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---
### Original File: narrative_duet_protocol_legacy1.md
---
---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina∴ & Resonance Network Stewards
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---

*Content from narrative_duet_protocol_legacy1-1.md:*


---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina∴ & Resonance Network Stewards
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---

*Content from narrative_duet_protocol_legacy1-2.md:*


# Narrative Duet Protocol

> **Purpose:** To define the structure, themes, mechanics, interaction flow, alignment assessment, and outcomes of the "Narrative Duet"—the symbolic, CYOA-style compatibility test at the heart of ThinkAlike’s connection process. This protocol is foundational for both the Portal Realm (first system-suggested match) and the Resonance Network Realm (user-initiated connections), ensuring all interactions are meaningful, ethical, and aligned with PET/Clarity and ThinkAlike’s symbolic/ritual standards.

---

## 1. Introduction & Purpose

The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users:
- **User A:** The active participant, seeking resonance.
- **User B:** Represented by their AI Clone, which embodies User B’s `UserValueProfile`, archetypes, and narrative history.

The Duet is used in:
- **Portal Realm:** As the first system-suggested match after the "Whispering Gallery" phase.
- **Resonance Network Realm:** For user-initiated connections after viewing another’s User Node and video.

The Narrative Duet moves beyond superficial profiles, fostering authentic connection through symbolic, narrative-driven interaction, always upholding PET/Clarity principles.

---

## 2. Initiation of a Narrative Duet

- **Portal Realm Context:**
  - Initiated after the "Whispering Gallery" phase.
  - User A interacts with an abstract, anonymized AI Clone of User B (User B is not present or notified unless a successful match occurs).
  - Eos Lumina∴ acts as facilitator and narrator.

- **Resonance Network Context:**
  - Initiated by User A after viewing User B’s video and User Node.
  - User B’s AI Clone participates; User B is notified only if a successful match occurs.
  - Eos Lumina∴ again facilitates the process.

---

## 3. Core Mechanics & Interaction Flow

- **CYOA Structure:**
  - The Duet is a branching narrative (Choose-Your-Own-Adventure) where User A makes choices at key junctures.
  - User B’s AI Clone responds, drawing on User B’s `UserValueProfile`, archetypes, and narrative history, ensuring the duet reflects User B’s actual resonant signature.
  - The story unfolds based on the interplay of choices, with Eos Lumina∴ providing narration, context, and symbolic cues.

- **Symbolic Language & Themes:**
  - Duets draw from ThinkAlike’s philosophical sources (`philosophical_sources.md`) and mythic index (`symbolic_myth_index.md`).
  - Themes include collaborative problem-solving, ethical dilemmas, co-creation of symbolic stories, and exploration of shared values.
  - Choices are designed to reveal compatibility on key values, epistemic modes (`epistemic_match_modes.md`), and narrative archetypes (`narrative_match_archetypes.md`).

---

## 4. Alignment Assessment

- **Alignment/Harmony:**
  - The system, guided by Eos Lumina∴, assesses the degree of alignment or harmony achieved during the Duet.
  - Assessment is based on congruence, complementarity, or constructive engagement between User A’s and User B’s AI Clone’s choices—not on "right/wrong" answers.
  - An internal `alignmentScore` is calculated for the session, drawing on the resonance of values, epistemic modes, and narrative archetypes.

---

## 5. Outcomes of a Narrative Duet

- **Sufficient Alignment (Successful Duet):**
  - Eos Lumina∴ narrates a harmonious conclusion.
  - Sequential, consensual reveal process:
    - **Portal:** User A consents to show their video. User B is notified, sees User A’s video, and consents to show theirs.
    - **Resonance Network:** User A confirms intent to connect. User B is notified, sees User A’s video, and consents.
  - Mutual reveal of User Nodes (identities).
  - Mutual opt-in for direct communication.
  - Resonance Network: Connection line is strengthened; positive signal for "Social LLM."

- **Insufficient Alignment (Unsuccessful Duet):**
  - Eos Lumina∴ narrates a gentle dissolution (e.g., "white light fade back to Eos Node" or node dimming in the Resonance Network).
  - No identities are revealed (if not already known).
  - No notification to User B (if not the initiator).
  - User A returns to Eos Lumina∴ (Portal) or browsing state (Resonance Network).
  - Resonance Network: Neutral or slightly corrective signal for that pairing in the "Social LLM."

---

## 6. Ethical Considerations & PET/Clarity

- **User Agency:** All choices are meaningful and have real impact on outcomes.
- **Transparency:** Eos Lumina∴ explains the purpose and mechanics of the Duet at the outset.
- **Consent:** Explicit, stepwise consent is required for any reveal of videos or identities, and for direct communication.
- **AI Clone Representation:** It is always clear that User B’s AI Clone is an AI based on User B’s profile, not User B in real-time.
- **Privacy:** No information is revealed to User B or others unless mutual consent is achieved.

---

## 7. Relation to Other Documents

- See [`portal_specification.md`](portal_specification.md) for the overall onboarding and first match context.
- See [`resonance_network_specification.md`](../resonance_network/resonance_network_specification.md) for user-initiated connections and Resonance Network logic.
- See [`identity_resonance_score.md`](../resonance_network/identity_resonance_score.md) for alignment and resonance scoring.
- See [`UserValueProfile` data model](portal_specification.md#51-core-entities) for how user values inform the Duet.
- See [`philosophical_sources.md`](../../philosophical_sources.md), [`symbolic_myth_index.md`](../../symbolic_myth_index.md), [`epistemic_match_modes.md`](../../epistemic_match_modes.md), and [`narrative_match_archetypes.md`](../../narrative_match_archetypes.md) for narrative and symbolic foundations.

---

> **Note:** This protocol is to be harmonized and iteratively refined in collaboration with domain experts, narrative designers, and the ThinkAlike community. All flows and mechanics must remain aligned with the Copilot Bootstrap & Alignment Guide and the project’s PET/Clarity and symbolic/ritual standards.


---

*Content from narrative_duet_protocol_legacy1-3.md:*


# Narrative Duet Protocol

> **Purpose:** To define the structure, themes, mechanics, interaction flow, alignment assessment, and outcomes of the "Narrative Duet"—the symbolic, CYOA-style compatibility test at the heart of ThinkAlike’s connection process. This protocol is foundational for both the Portal Realm (first system-suggested match) and the Resonance Network Realm (user-initiated connections), ensuring all interactions are meaningful, ethical, and aligned with PET/Clarity and ThinkAlike’s symbolic/ritual standards.

---

## 1. Introduction & Purpose

The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users:
- **User A:** The active participant, seeking resonance.
- **User B:** Represented by their AI Clone, which embodies User B’s `UserValueProfile`, archetypes, and narrative history.

The Duet is used in:
- **Portal Realm:** As the first system-suggested match after the "Whispering Gallery" phase.
- **Resonance Network Realm:** For user-initiated connections after viewing another’s User Node and video.

The Narrative Duet moves beyond superficial profiles, fostering authentic connection through symbolic, narrative-driven interaction, always upholding PET/Clarity principles.

---

## 2. Initiation of a Narrative Duet

- **Portal Realm Context:**
  - Initiated after the "Whispering Gallery" phase.
  - User A interacts with an abstract, anonymized AI Clone of User B (User B is not present or notified unless a successful match occurs).
  - Eos Lumina∴ acts as facilitator and narrator.

- **Resonance Network Context:**
  - Initiated by User A after viewing User B’s video and User Node.
  - User B’s AI Clone participates; User B is notified only if a successful match occurs.
  - Eos Lumina∴ again facilitates the process.

---

## 3. Core Mechanics & Interaction Flow

- **CYOA Structure:**
  - The Duet is a branching narrative (Choose-Your-Own-Adventure) where User A makes choices at key junctures.
  - User B’s AI Clone responds, drawing on User B’s `UserValueProfile`, archetypes, and narrative history, ensuring the duet reflects User B’s actual resonant signature.
  - The story unfolds based on the interplay of choices, with Eos Lumina∴ providing narration, context, and symbolic cues.

- **Symbolic Language & Themes:**
  - Duets draw from ThinkAlike’s philosophical sources (`philosophical_sources.md`) and mythic index (`symbolic_myth_index.md`).
  - Themes include collaborative problem-solving, ethical dilemmas, co-creation of symbolic stories, and exploration of shared values.
  - Choices are designed to reveal compatibility on key values, epistemic modes (`epistemic_match_modes.md`), and narrative archetypes (`narrative_match_archetypes.md`).

---

## 4. Alignment Assessment

- **Alignment/Harmony:**
  - The system, guided by Eos Lumina∴, assesses the degree of alignment or harmony achieved during the Duet.
  - Assessment is based on congruence, complementarity, or constructive engagement between User A’s and User B’s AI Clone’s choices—not on "right/wrong" answers.
  - An internal `alignmentScore` is calculated for the session, drawing on the resonance of values, epistemic modes, and narrative archetypes.

---

## 5. Outcomes of a Narrative Duet

- **Sufficient Alignment (Successful Duet):**
  - Eos Lumina∴ narrates a harmonious conclusion.
  - Sequential, consensual reveal process:
    - **Portal:** User A consents to show their video. User B is notified, sees User A’s video, and consents to show theirs.
    - **Resonance Network:** User A confirms intent to connect. User B is notified, sees User A’s video, and consents.
  - Mutual reveal of User Nodes (identities).
  - Mutual opt-in for direct communication.
  - Resonance Network: Connection line is strengthened; positive signal for "Social LLM."

- **Insufficient Alignment (Unsuccessful Duet):**
  - Eos Lumina∴ narrates a gentle dissolution (e.g., "white light fade back to Eos Node" or node dimming in the Resonance Network).
  - No identities are revealed (if not already known).
  - No notification to User B (if not the initiator).
  - User A returns to Eos Lumina∴ (Portal) or browsing state (Resonance Network).
  - Resonance Network: Neutral or slightly corrective signal for that pairing in the "Social LLM."

---

## 6. Ethical Considerations & PET/Clarity

- **User Agency:** All choices are meaningful and have real impact on outcomes.
- **Transparency:** Eos Lumina∴ explains the purpose and mechanics of the Duet at the outset.
- **Consent:** Explicit, stepwise consent is required for any reveal of videos or identities, and for direct communication.
- **AI Clone Representation:** It is always clear that User B’s AI Clone is an AI based on User B’s profile, not User B in real-time.
- **Privacy:** No information is revealed to User B or others unless mutual consent is achieved.

---

## 7. Relation to Other Documents

- See [`portal_specification.md`](portal_specification.md) for the overall onboarding and first match context.
- See [`resonance_network_specification.md`](../resonance_network/resonance_network_specification.md) for user-initiated connections and Resonance Network logic.
- See [`identity_resonance_score.md`](../resonance_network/identity_resonance_score.md) for alignment and resonance scoring.
- See [`UserValueProfile` data model](portal_specification.md#51-core-entities) for how user values inform the Duet.
- See [`philosophical_sources.md`](../../philosophical_sources.md), [`symbolic_myth_index.md`](../../symbolic_myth_index.md), [`epistemic_match_modes.md`](../../epistemic_match_modes.md), and [`narrative_match_archetypes.md`](../../narrative_match_archetypes.md) for narrative and symbolic foundations.

---

> **Note:** This protocol is to be harmonized and iteratively refined in collaboration with domain experts, narrative designers, and the ThinkAlike community. All flows and mechanics must remain aligned with the Copilot Bootstrap & Alignment Guide and the project’s PET/Clarity and symbolic/ritual standards.


---

*Content from narrative_duet_protocol_legacy1-4.md:*


---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina∴ & Resonance Network Stewards
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---

*Content from narrative_duet_protocol_legacy1-5.md:*


---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina∴ & Resonance Network Stewards
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---

*Content from narrative_duet_protocol_legacy1-6.md:*


---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina∴ & Resonance Network Stewards
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---

*Content from narrative_duet_protocol_legacy1-7.md:*


---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---

*Content from narrative_duet_protocol_legacy1-8.md:*


---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---
### Original File: narrative_duet_protocol_legacy2.md
---
---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina∴ & Resonance Network Stewards
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---

*Content from narrative_duet_protocol_legacy2-1.md:*


---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina∴ & Resonance Network Stewards
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---

*Content from narrative_duet_protocol_legacy2-2.md:*


# Narrative Duet Protocol

> **Purpose:** To define the structure, themes, mechanics, interaction flow, alignment assessment, and outcomes of the "Narrative Duet"—the symbolic, CYOA-style compatibility test at the heart of ThinkAlike’s connection process. This protocol is foundational for both the Portal Realm (first system-suggested match) and the Resonance Network Realm (user-initiated connections), ensuring all interactions are meaningful, ethical, and aligned with PET/Clarity and ThinkAlike’s symbolic/ritual standards.

---

## 1. Introduction & Purpose

The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users:
- **User A:** The active participant, seeking resonance.
- **User B:** Represented by their AI Clone, which embodies User B’s `UserValueProfile`, archetypes, and narrative history.

The Duet is used in:
- **Portal Realm:** As the first system-suggested match after the "Whispering Gallery" phase.
- **Resonance Network Realm:** For user-initiated connections after viewing another’s User Node and video.

The Narrative Duet moves beyond superficial profiles, fostering authentic connection through symbolic, narrative-driven interaction, always upholding PET/Clarity principles.

---

## 2. Initiation of a Narrative Duet

- **Portal Realm Context:**
  - Initiated after the "Whispering Gallery" phase.
  - User A interacts with an abstract, anonymized AI Clone of User B (User B is not present or notified unless a successful match occurs).
  - Eos Lumina∴ acts as facilitator and narrator.

- **Resonance Network Context:**
  - Initiated by User A after viewing User B’s video and User Node.
  - User B’s AI Clone participates; User B is notified only if a successful match occurs.
  - Eos Lumina∴ again facilitates the process.

---

## 3. Core Mechanics & Interaction Flow

- **CYOA Structure:**
  - The Duet is a branching narrative (Choose-Your-Own-Adventure) where User A makes choices at key junctures.
  - User B’s AI Clone responds, drawing on User B’s `UserValueProfile`, archetypes, and narrative history, ensuring the duet reflects User B’s actual resonant signature.
  - The story unfolds based on the interplay of choices, with Eos Lumina∴ providing narration, context, and symbolic cues.

- **Symbolic Language & Themes:**
  - Duets draw from ThinkAlike’s philosophical sources (`philosophical_sources.md`) and mythic index (`symbolic_myth_index.md`).
  - Themes include collaborative problem-solving, ethical dilemmas, co-creation of symbolic stories, and exploration of shared values.
  - Choices are designed to reveal compatibility on key values, epistemic modes (`epistemic_match_modes.md`), and narrative archetypes (`narrative_match_archetypes.md`).

---

## 4. Alignment Assessment

- **Alignment/Harmony:**
  - The system, guided by Eos Lumina∴, assesses the degree of alignment or harmony achieved during the Duet.
  - Assessment is based on congruence, complementarity, or constructive engagement between User A’s and User B’s AI Clone’s choices—not on "right/wrong" answers.
  - An internal `alignmentScore` is calculated for the session, drawing on the resonance of values, epistemic modes, and narrative archetypes.

---

## 5. Outcomes of a Narrative Duet

- **Sufficient Alignment (Successful Duet):**
  - Eos Lumina∴ narrates a harmonious conclusion.
  - Sequential, consensual reveal process:
    - **Portal:** User A consents to show their video. User B is notified, sees User A’s video, and consents to show theirs.
    - **Resonance Network:** User A confirms intent to connect. User B is notified, sees User A’s video, and consents.
  - Mutual reveal of User Nodes (identities).
  - Mutual opt-in for direct communication.
  - Resonance Network: Connection line is strengthened; positive signal for "Social LLM."

- **Insufficient Alignment (Unsuccessful Duet):**
  - Eos Lumina∴ narrates a gentle dissolution (e.g., "white light fade back to Eos Node" or node dimming in the Resonance Network).
  - No identities are revealed (if not already known).
  - No notification to User B (if not the initiator).
  - User A returns to Eos Lumina∴ (Portal) or browsing state (Resonance Network).
  - Resonance Network: Neutral or slightly corrective signal for that pairing in the "Social LLM."

---

## 6. Ethical Considerations & PET/Clarity

- **User Agency:** All choices are meaningful and have real impact on outcomes.
- **Transparency:** Eos Lumina∴ explains the purpose and mechanics of the Duet at the outset.
- **Consent:** Explicit, stepwise consent is required for any reveal of videos or identities, and for direct communication.
- **AI Clone Representation:** It is always clear that User B’s AI Clone is an AI based on User B’s profile, not User B in real-time.
- **Privacy:** No information is revealed to User B or others unless mutual consent is achieved.

---

## 7. Relation to Other Documents

- See [`portal_specification.md`](portal_specification.md) for the overall onboarding and first match context.
- See [`resonance_network_specification.md`](../resonance_network/resonance_network_specification.md) for user-initiated connections and Resonance Network logic.
- See [`identity_resonance_score.md`](../resonance_network/identity_resonance_score.md) for alignment and resonance scoring.
- See [`UserValueProfile` data model](portal_specification.md#51-core-entities) for how user values inform the Duet.
- See [`philosophical_sources.md`](../../philosophical_sources.md), [`symbolic_myth_index.md`](../../symbolic_myth_index.md), [`epistemic_match_modes.md`](../../epistemic_match_modes.md), and [`narrative_match_archetypes.md`](../../narrative_match_archetypes.md) for narrative and symbolic foundations.

---

> **Note:** This protocol is to be harmonized and iteratively refined in collaboration with domain experts, narrative designers, and the ThinkAlike community. All flows and mechanics must remain aligned with the Copilot Bootstrap & Alignment Guide and the project’s PET/Clarity and symbolic/ritual standards.


---

*Content from narrative_duet_protocol_legacy2-3.md:*


# Narrative Duet Protocol

> **Purpose:** To define the structure, themes, mechanics, interaction flow, alignment assessment, and outcomes of the "Narrative Duet"—the symbolic, CYOA-style compatibility test at the heart of ThinkAlike’s connection process. This protocol is foundational for both the Portal Realm (first system-suggested match) and the Resonance Network Realm (user-initiated connections), ensuring all interactions are meaningful, ethical, and aligned with PET/Clarity and ThinkAlike’s symbolic/ritual standards.

---

## 1. Introduction & Purpose

The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users:
- **User A:** The active participant, seeking resonance.
- **User B:** Represented by their AI Clone, which embodies User B’s `UserValueProfile`, archetypes, and narrative history.

The Duet is used in:
- **Portal Realm:** As the first system-suggested match after the "Whispering Gallery" phase.
- **Resonance Network Realm:** For user-initiated connections after viewing another’s User Node and video.

The Narrative Duet moves beyond superficial profiles, fostering authentic connection through symbolic, narrative-driven interaction, always upholding PET/Clarity principles.

---

## 2. Initiation of a Narrative Duet

- **Portal Realm Context:**
  - Initiated after the "Whispering Gallery" phase.
  - User A interacts with an abstract, anonymized AI Clone of User B (User B is not present or notified unless a successful match occurs).
  - Eos Lumina∴ acts as facilitator and narrator.

- **Resonance Network Context:**
  - Initiated by User A after viewing User B’s video and User Node.
  - User B’s AI Clone participates; User B is notified only if a successful match occurs.
  - Eos Lumina∴ again facilitates the process.

---

## 3. Core Mechanics & Interaction Flow

- **CYOA Structure:**
  - The Duet is a branching narrative (Choose-Your-Own-Adventure) where User A makes choices at key junctures.
  - User B’s AI Clone responds, drawing on User B’s `UserValueProfile`, archetypes, and narrative history, ensuring the duet reflects User B’s actual resonant signature.
  - The story unfolds based on the interplay of choices, with Eos Lumina∴ providing narration, context, and symbolic cues.

- **Symbolic Language & Themes:**
  - Duets draw from ThinkAlike’s philosophical sources (`philosophical_sources.md`) and mythic index (`symbolic_myth_index.md`).
  - Themes include collaborative problem-solving, ethical dilemmas, co-creation of symbolic stories, and exploration of shared values.
  - Choices are designed to reveal compatibility on key values, epistemic modes (`epistemic_match_modes.md`), and narrative archetypes (`narrative_match_archetypes.md`).

---

## 4. Alignment Assessment

- **Alignment/Harmony:**
  - The system, guided by Eos Lumina∴, assesses the degree of alignment or harmony achieved during the Duet.
  - Assessment is based on congruence, complementarity, or constructive engagement between User A’s and User B’s AI Clone’s choices—not on "right/wrong" answers.
  - An internal `alignmentScore` is calculated for the session, drawing on the resonance of values, epistemic modes, and narrative archetypes.

---

## 5. Outcomes of a Narrative Duet

- **Sufficient Alignment (Successful Duet):**
  - Eos Lumina∴ narrates a harmonious conclusion.
  - Sequential, consensual reveal process:
    - **Portal:** User A consents to show their video. User B is notified, sees User A’s video, and consents to show theirs.
    - **Resonance Network:** User A confirms intent to connect. User B is notified, sees User A’s video, and consents.
  - Mutual reveal of User Nodes (identities).
  - Mutual opt-in for direct communication.
  - Resonance Network: Connection line is strengthened; positive signal for "Social LLM."

- **Insufficient Alignment (Unsuccessful Duet):**
  - Eos Lumina∴ narrates a gentle dissolution (e.g., "white light fade back to Eos Node" or node dimming in the Resonance Network).
  - No identities are revealed (if not already known).
  - No notification to User B (if not the initiator).
  - User A returns to Eos Lumina∴ (Portal) or browsing state (Resonance Network).
  - Resonance Network: Neutral or slightly corrective signal for that pairing in the "Social LLM."

---

## 6. Ethical Considerations & PET/Clarity

- **User Agency:** All choices are meaningful and have real impact on outcomes.
- **Transparency:** Eos Lumina∴ explains the purpose and mechanics of the Duet at the outset.
- **Consent:** Explicit, stepwise consent is required for any reveal of videos or identities, and for direct communication.
- **AI Clone Representation:** It is always clear that User B’s AI Clone is an AI based on User B’s profile, not User B in real-time.
- **Privacy:** No information is revealed to User B or others unless mutual consent is achieved.

---

## 7. Relation to Other Documents

- See [`portal_specification.md`](portal_specification.md) for the overall onboarding and first match context.
- See [`resonance_network_specification.md`](../resonance_network/resonance_network_specification.md) for user-initiated connections and Resonance Network logic.
- See [`identity_resonance_score.md`](../resonance_network/identity_resonance_score.md) for alignment and resonance scoring.
- See [`UserValueProfile` data model](portal_specification.md#51-core-entities) for how user values inform the Duet.
- See [`philosophical_sources.md`](../../philosophical_sources.md), [`symbolic_myth_index.md`](../../symbolic_myth_index.md), [`epistemic_match_modes.md`](../../epistemic_match_modes.md), and [`narrative_match_archetypes.md`](../../narrative_match_archetypes.md) for narrative and symbolic foundations.

---

> **Note:** This protocol is to be harmonized and iteratively refined in collaboration with domain experts, narrative designers, and the ThinkAlike community. All flows and mechanics must remain aligned with the Copilot Bootstrap & Alignment Guide and the project’s PET/Clarity and symbolic/ritual standards.


---

*Content from narrative_duet_protocol_legacy2-4.md:*


---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina∴ & Resonance Network Stewards
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---
### Original File: narrative_duet_protocol_legacy3.md
---
---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina∴ & Resonance Network Stewards
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---

*Content from narrative_duet_protocol_legacy3-1.md:*


---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina∴ & Resonance Network Stewards
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---

*Content from narrative_duet_protocol_legacy3-2.md:*


# Narrative Duet Protocol

> **Purpose:** To define the structure, themes, mechanics, interaction flow, alignment assessment, and outcomes of the "Narrative Duet"—the symbolic, CYOA-style compatibility test at the heart of ThinkAlike’s connection process. This protocol is foundational for both the Portal Realm (first system-suggested match) and the Resonance Network Realm (user-initiated connections), ensuring all interactions are meaningful, ethical, and aligned with PET/Clarity and ThinkAlike’s symbolic/ritual standards.

---

## 1. Introduction & Purpose

The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users:
- **User A:** The active participant, seeking resonance.
- **User B:** Represented by their AI Clone, which embodies User B’s `UserValueProfile`, archetypes, and narrative history.

The Duet is used in:
- **Portal Realm:** As the first system-suggested match after the "Whispering Gallery" phase.
- **Resonance Network Realm:** For user-initiated connections after viewing another’s User Node and video.

The Narrative Duet moves beyond superficial profiles, fostering authentic connection through symbolic, narrative-driven interaction, always upholding PET/Clarity principles.

---

## 2. Initiation of a Narrative Duet

- **Portal Realm Context:**
  - Initiated after the "Whispering Gallery" phase.
  - User A interacts with an abstract, anonymized AI Clone of User B (User B is not present or notified unless a successful match occurs).
  - Eos Lumina∴ acts as facilitator and narrator.

- **Resonance Network Context:**
  - Initiated by User A after viewing User B’s video and User Node.
  - User B’s AI Clone participates; User B is notified only if a successful match occurs.
  - Eos Lumina∴ again facilitates the process.

---

## 3. Core Mechanics & Interaction Flow

- **CYOA Structure:**
  - The Duet is a branching narrative (Choose-Your-Own-Adventure) where User A makes choices at key junctures.
  - User B’s AI Clone responds, drawing on User B’s `UserValueProfile`, archetypes, and narrative history, ensuring the duet reflects User B’s actual resonant signature.
  - The story unfolds based on the interplay of choices, with Eos Lumina∴ providing narration, context, and symbolic cues.

- **Symbolic Language & Themes:**
  - Duets draw from ThinkAlike’s philosophical sources (`philosophical_sources.md`) and mythic index (`symbolic_myth_index.md`).
  - Themes include collaborative problem-solving, ethical dilemmas, co-creation of symbolic stories, and exploration of shared values.
  - Choices are designed to reveal compatibility on key values, epistemic modes (`epistemic_match_modes.md`), and narrative archetypes (`narrative_match_archetypes.md`).

---

## 4. Alignment Assessment

- **Alignment/Harmony:**
  - The system, guided by Eos Lumina∴, assesses the degree of alignment or harmony achieved during the Duet.
  - Assessment is based on congruence, complementarity, or constructive engagement between User A’s and User B’s AI Clone’s choices—not on "right/wrong" answers.
  - An internal `alignmentScore` is calculated for the session, drawing on the resonance of values, epistemic modes, and narrative archetypes.

---

## 5. Outcomes of a Narrative Duet

- **Sufficient Alignment (Successful Duet):**
  - Eos Lumina∴ narrates a harmonious conclusion.
  - Sequential, consensual reveal process:
    - **Portal:** User A consents to show their video. User B is notified, sees User A’s video, and consents to show theirs.
    - **Resonance Network:** User A confirms intent to connect. User B is notified, sees User A’s video, and consents.
  - Mutual reveal of User Nodes (identities).
  - Mutual opt-in for direct communication.
  - Resonance Network: Connection line is strengthened; positive signal for "Social LLM."

- **Insufficient Alignment (Unsuccessful Duet):**
  - Eos Lumina∴ narrates a gentle dissolution (e.g., "white light fade back to Eos Node" or node dimming in the Resonance Network).
  - No identities are revealed (if not already known).
  - No notification to User B (if not the initiator).
  - User A returns to Eos Lumina∴ (Portal) or browsing state (Resonance Network).
  - Resonance Network: Neutral or slightly corrective signal for that pairing in the "Social LLM."

---

## 6. Ethical Considerations & PET/Clarity

- **User Agency:** All choices are meaningful and have real impact on outcomes.
- **Transparency:** Eos Lumina∴ explains the purpose and mechanics of the Duet at the outset.
- **Consent:** Explicit, stepwise consent is required for any reveal of videos or identities, and for direct communication.
- **AI Clone Representation:** It is always clear that User B’s AI Clone is an AI based on User B’s profile, not User B in real-time.
- **Privacy:** No information is revealed to User B or others unless mutual consent is achieved.

---

## 7. Relation to Other Documents

- See [`portal_specification.md`](portal_specification.md) for the overall onboarding and first match context.
- See [`resonance_network_specification.md`](../resonance_network/resonance_network_specification.md) for user-initiated connections and Resonance Network logic.
- See [`identity_resonance_score.md`](../resonance_network/identity_resonance_score.md) for alignment and resonance scoring.
- See [`UserValueProfile` data model](portal_specification.md#51-core-entities) for how user values inform the Duet.
- See [`philosophical_sources.md`](../../philosophical_sources.md), [`symbolic_myth_index.md`](../../symbolic_myth_index.md), [`epistemic_match_modes.md`](../../epistemic_match_modes.md), and [`narrative_match_archetypes.md`](../../narrative_match_archetypes.md) for narrative and symbolic foundations.

---

> **Note:** This protocol is to be harmonized and iteratively refined in collaboration with domain experts, narrative designers, and the ThinkAlike community. All flows and mechanics must remain aligned with the Copilot Bootstrap & Alignment Guide and the project’s PET/Clarity and symbolic/ritual standards.


---
### Original File: narrative_duet_protocol_ad1c4065.md
---
# Narrative Duet Protocol

> **Purpose:** To define the structure, themes, mechanics, interaction flow, alignment assessment, and outcomes of the "Narrative Duet"—the symbolic, CYOA-style compatibility test at the heart of ThinkAlike’s connection process. This protocol is foundational for both the Portal Realm (first system-suggested match) and the Resonance Network Realm (user-initiated connections), ensuring all interactions are meaningful, ethical, and aligned with PET/Clarity and ThinkAlike’s symbolic/ritual standards.

---

## 1. Introduction & Purpose

The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users:
- **User A:** The active participant, seeking resonance.
- **User B:** Represented by their AI Clone, which embodies User B’s `UserValueProfile`, archetypes, and narrative history.

The Duet is used in:
- **Portal Realm:** As the first system-suggested match after the "Whispering Gallery" phase.
- **Resonance Network Realm:** For user-initiated connections after viewing another’s User Node and video.

The Narrative Duet moves beyond superficial profiles, fostering authentic connection through symbolic, narrative-driven interaction, always upholding PET/Clarity principles.

---

## 2. Initiation of a Narrative Duet

- **Portal Realm Context:**
  - Initiated after the "Whispering Gallery" phase.
  - User A interacts with an abstract, anonymized AI Clone of User B (User B is not present or notified unless a successful match occurs).
  - Eos Lumina∴ acts as facilitator and narrator.

- **Resonance Network Context:**
  - Initiated by User A after viewing User B’s video and User Node.
  - User B’s AI Clone participates; User B is notified only if a successful match occurs.
  - Eos Lumina∴ again facilitates the process.

---

## 3. Core Mechanics & Interaction Flow

- **CYOA Structure:**
  - The Duet is a branching narrative (Choose-Your-Own-Adventure) where User A makes choices at key junctures.
  - User B’s AI Clone responds, drawing on User B’s `UserValueProfile`, archetypes, and narrative history, ensuring the duet reflects User B’s actual resonant signature.
  - The story unfolds based on the interplay of choices, with Eos Lumina∴ providing narration, context, and symbolic cues.

- **Symbolic Language & Themes:**
  - Duets draw from ThinkAlike’s philosophical sources (`philosophical_sources.md`) and mythic index (`symbolic_myth_index.md`).
  - Themes include collaborative problem-solving, ethical dilemmas, co-creation of symbolic stories, and exploration of shared values.
  - Choices are designed to reveal compatibility on key values, epistemic modes (`epistemic_match_modes.md`), and narrative archetypes (`narrative_match_archetypes.md`).

---

## 4. Alignment Assessment

- **Alignment/Harmony:**
  - The system, guided by Eos Lumina∴, assesses the degree of alignment or harmony achieved during the Duet.
  - Assessment is based on congruence, complementarity, or constructive engagement between User A’s and User B’s AI Clone’s choices—not on "right/wrong" answers.
  - An internal `alignmentScore` is calculated for the session, drawing on the resonance of values, epistemic modes, and narrative archetypes.

---

## 5. Outcomes of a Narrative Duet

- **Sufficient Alignment (Successful Duet):**
  - Eos Lumina∴ narrates a harmonious conclusion.
  - Sequential, consensual reveal process:
    - **Portal:** User A consents to show their video. User B is notified, sees User A’s video, and consents to show theirs.
    - **Resonance Network:** User A confirms intent to connect. User B is notified, sees User A’s video, and consents.
  - Mutual reveal of User Nodes (identities).
  - Mutual opt-in for direct communication.
  - Resonance Network: Connection line is strengthened; positive signal for "Social LLM."

- **Insufficient Alignment (Unsuccessful Duet):**
  - Eos Lumina∴ narrates a gentle dissolution (e.g., "white light fade back to Eos Node" or node dimming in the Resonance Network).
  - No identities are revealed (if not already known).
  - No notification to User B (if not the initiator).
  - User A returns to Eos Lumina∴ (Portal) or browsing state (Resonance Network).
  - Resonance Network: Neutral or slightly corrective signal for that pairing in the "Social LLM."

---

## 6. Ethical Considerations & PET/Clarity

- **User Agency:** All choices are meaningful and have real impact on outcomes.
- **Transparency:** Eos Lumina∴ explains the purpose and mechanics of the Duet at the outset.
- **Consent:** Explicit, stepwise consent is required for any reveal of videos or identities, and for direct communication.
- **AI Clone Representation:** It is always clear that User B’s AI Clone is an AI based on User B’s profile, not User B in real-time.
- **Privacy:** No information is revealed to User B or others unless mutual consent is achieved.

---

## 7. Relation to Other Documents

- See [`portal_specification.md`](portal_specification.md) for the overall onboarding and first match context.
- See [`resonance_network_specification.md`](../resonance_network/resonance_network_specification.md) for user-initiated connections and Resonance Network logic.
- See [`identity_resonance_score.md`](../resonance_network/identity_resonance_score.md) for alignment and resonance scoring.
- See [`UserValueProfile` data model](portal_specification.md#51-core-entities) for how user values inform the Duet.
- See [`philosophical_sources.md`](../../philosophical_sources.md), [`symbolic_myth_index.md`](../../symbolic_myth_index.md), [`epistemic_match_modes.md`](../../epistemic_match_modes.md), and [`narrative_match_archetypes.md`](../../narrative_match_archetypes.md) for narrative and symbolic foundations.

---

> **Note:** This protocol is to be harmonized and iteratively refined in collaboration with domain experts, narrative designers, and the ThinkAlike community. All flows and mechanics must remain aligned with the Copilot Bootstrap & Alignment Guide and the project’s PET/Clarity and symbolic/ritual standards.


---
### Original File: narrative_duet_protocol_1.md
---
---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina∴ & Resonance Network Stewards
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.


---
### Original File: narrative_duet_protocol_ae8293fa.md
---
---
title: Narrative Duet Protocol: The Ritual of Resonant Encounter
version: 1.0.0
status: canonical
date_created: 2025-06-14
maintained_by: Eos Lumina∴ & Resonance Network Stewards
tags: [protocol, duet, resonance, narrative, compatibility, PET/Clarity]
openapi_ref: ../../api_specs/openapi.json
canonical_data_models: ../../architecture/data_models.md
harmonization_note: "Explicitly cross-linked to OpenAPI spec and canonical data models. All integration points tracked in project TODOs/system blueprint."
last_updated: 2025-06-18
---

# Narrative Duet Protocol: The Ritual of Resonant Encounter

> **Cross-References:** This protocol is referenced by [Portal Realm Specification](../realms/portal/portal_specification.md) and [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md). It is implemented in the Narrative Engine and underpins the `NarrativeDuetSession` data model.
>
> **See also:** [Canonical Onboarding & Persona Flow](../onboarding_persona_flow.md)

## 1. Introduction & Purpose (The Scrying Rite)
The Narrative Duet is a symbolic, interactive narrative experience designed to test value alignment and compatibility between two users (User A, the active participant, and User B, represented by their AI Clone). It is used in both the Portal Realm (for system-suggested first matches) and the Resonance Network Realm (for user-initiated connections). The Duet is framed as a "Scrying Rite"—a ritual of encounter that moves beyond superficial profiles to foster authentic connection.

See: [Portal Realm Specification](../realms/portal/portal_specification.md), [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)

## 2. Initiation of a Narrative Duet
- **Portal Realm:** Triggered after the "Whispering Gallery" phase, with User A interacting with an abstractly represented AI Clone of User B, facilitated by Eos Lumina∴.
- **Resonance Network Realm:** Initiated by User A after viewing User B's introductory video, also facilitated by Eos Lumina∴.

## 3. Core Mechanics & Interaction Flow
- **CYOA Structure:** The Duet is a branching narrative where User A makes choices at key junctures.
- **Role of User B's AI Clone:** The AI Clone responds based on User B's `UserValueProfile`, archetypes, epistemic modes, and narrative history. This is an AI representation, ensuring User B's privacy and agency.
- **Thematic Content:** Duets draw from ThinkAlike’s philosophical and symbolic sources, including `philosophical_sources.md` and `symbolic_myth_index.md`, with themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
- **Dynamic Selection of Scenarios:** The Narrative Engine dynamically selects a narrative path from a pool of static scenarios that is most likely to surface key points of resonance or generative tension between the two users' profiles. The specific themes and ethical dilemmas chosen for a given Duet are not random, but are tailored to maximize meaningful interaction.
- **NarrativeDuetSession Data Model:** Each Duet is tracked as a `NarrativeDuetSession`, recording choices, outcomes, and consent actions for auditability and system refinement (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 4. Alignment Assessment
- The system, guided by Eos Lumina∴, assesses the "harmony" or "alignment" based on the congruence and complementarity of choices, not on "right/wrong" answers.
- An internal `alignmentScore` is calculated for the session, which informs the outcome.
- The "Social LLM" and Resonance Feedback & Attunement system use Duet outcomes to refine the constellation map and highlight resonant pathways (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 5. Outcomes of a Narrative Duet
- **Sufficient Alignment (Successful Duet):**
    - A sequential, consensual reveal process is initiated: User A offers their video/profile, User B is notified and reciprocates, then both consent to direct communication.
    - The connection line in the Resonance Network is visually strengthened.
- **Insufficient Alignment (Unsuccessful Duet):**
    - The "Dissolution Rite" is performed (e.g., "white light fade," node dimming).
    - No identities are revealed and the non-initiating user is not notified.
    - The user is returned to their previous state (Eos guidance in Portal, browsing in Resonance Network).

## 6. Ethical Considerations & PET/Clarity
- **User Agency:** Choices are meaningful and impactful.
- **Transparency:** Eos explains the Duet's purpose and process.
- **Consent:** Explicit consent is required for all reveals and communication.
- **AI Clone Representation:** It is always clear that the AI Clone is not the user in real-time, but a privacy-preserving representation.
- **Auditability & Ethical Lineage:** All Duet sessions are logged for auditability, and the ethical lineage of resonance calculations is tracked (see [resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md)).

## 7. Relation to Other Documents
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [identity_resonance_score.md] (if implemented)
- `UserValueProfile` data model (see Portal and Resonance Network specs)
- Corpus Magnus entries (philosophical_sources.md, symbolic_myth_index.md)

---
## Change Log
- 2025-06-14: Initial canonical draft, harmonized with Portal and Resonance Network specifications. Added explicit crosslinks, clarified data model and auditability, and referenced Social LLM attunement.
- 2025-06-18: Added OpenAPI and data model cross-references, harmonization note, and last updated date.

This protocol is a living document and will evolve as the mechanics of the Narrative Duet and Resonance Network are refined.

