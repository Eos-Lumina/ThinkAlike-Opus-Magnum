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
