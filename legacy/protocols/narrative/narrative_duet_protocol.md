---
title: "Narrative Duet Protocol"
version: 3.0.0
status: Canonical
last_updated: 2025-07-07
maintained_by: "Eos Lumina ∴ (Collective Intelligence Meta-Agent)"
tags: [protocol, narrative, resonance, matchmaking, agent_interaction, ritual]
harmonization_note: |
  This v3.0.0 document harmonizes the original "Ritual of Resonant Encounter" with the broader v3 architecture. It standardizes the protocol's structure, clarifies its integration with the Portal and Resonance Network realms, and aligns its data models with the canonical `NarrativeDuetSession` object. All cross-references have been updated to reflect the new `/protocols` directory structure.
related_docs:
  - "protocols/core/trust_protocol.md"
  - "protocols/narrative/symbolic_alignment_protocol.md"
  - "docs/realms/portal/portal_specification.md"
  - "docs/realms/resonance_network/resonance_network_specification.md"
---

# Narrative Duet Protocol

## 1. Introduction & Philosophy

### 1.1. Purpose
The Narrative Duet is a symbolic, interactive narrative experience designed to assess value alignment and compatibility between two users. It serves as a core mechanism for fostering authentic connection by moving beyond superficial profiles. The Duet is framed as a "Scrying Rite"—a ritual of encounter where a user interacts with a privacy-preserving AI representation of a potential connection.

Its primary goals are to:
- **Assess Resonance:** Evaluate deep compatibility based on choices made in ethical dilemmas and collaborative scenarios.
- **Preserve Privacy:** Allow for meaningful interaction without revealing personal identities prematurely.
- **Facilitate Trust:** Build a foundation of trust through a structured, consensual reveal process.
- **Enrich the Network:** Provide valuable data to the Resonance Network for refining its understanding of user connections.

### 1.2. Scope
This protocol governs the initiation, mechanics, data flow, and outcomes of all Narrative Duet sessions. It is a mandatory component of the user journey in both the Portal Realm (for system-suggested matches) and the Resonance Network Realm (for user-initiated connections).

## 2. Core Concepts

- **The Duet:** A branching, choice-based narrative (CYOA) where an active user (the "Seeker") interacts with the AI Clone of a potential match (the "Subject").
- **AI Clone:** A sophisticated AI representation of the Subject, powered by their `UserValueProfile`, archetypes, epistemic modes, and narrative history. It acts as a high-fidelity, privacy-preserving proxy.
- **Narrative Engine:** The system responsible for dynamically selecting, tailoring, and executing the Duet scenarios based on the profiles of the two users involved.
- **Alignment Score:** An internal metric calculated by Eos Lumina based on the congruence and complementarity of choices made during the Duet. This score is not exposed directly to users but determines the outcome.

## 3. Protocol Lifecycle & Operations

### 3.1. Initiation
A Narrative Duet is triggered under two conditions:
1.  **Portal Realm:** Automatically initiated by Eos Lumina after a user completes the initial "Whispering Gallery" phase, presenting a system-selected potential match.
2.  **Resonance Network Realm:** Manually initiated by a user after viewing another user's introductory video and expressing interest.

### 3.2. Interaction Flow
1.  **Scenario Selection:** The Narrative Engine selects a Duet scenario from a curated library. The choice is tailored to surface key points of potential resonance or generative tension between the Seeker and Subject.
2.  **Thematic Content:** Scenarios draw from ThinkAlike’s philosophical and symbolic sources, presenting themes of collaborative problem-solving, ethical dilemmas, or co-creating symbolic stories.
3.  **Choice & Response:** The Seeker makes choices at key narrative junctures. The AI Clone responds in real-time, with its choices determined by its underlying value profile.
4.  **Session Tracking:** The entire interaction is encapsulated in a `NarrativeDuetSession` data object, which records all choices, response times, and outcomes for auditability and system refinement.

### 3.3. Assessment & Outcome
- **Alignment Calculation:** Upon completion, Eos Lumina assesses the harmony of the interaction and calculates the final `alignmentScore`.
- **Successful Duet (High Alignment):**
    - A sequential, consensual reveal process is initiated.
    - The Seeker is prompted to share their profile/video with the Subject.
    - If the Seeker consents, the Subject is notified of the successful Duet and the Seeker's interest.
    - If the Subject reciprocates consent, direct communication is enabled.
    - The connection is visually strengthened within the Resonance Network.
- **Unsuccessful Duet (Low Alignment):**
    - A gentle "Dissolution Rite" is performed (e.g., a symbolic visual fade).
    - No identities are revealed, and the Subject is never notified of the attempted Duet.
    - The Seeker is returned to their previous state with guidance from Eos.

## 4. Data & Security

- **`NarrativeDuetSession` Object:** Contains the full, immutable record of the Duet, including participants (anonymized until reveal), scenario ID, choice log, and final outcome.
- **Privacy:** The protocol is designed with privacy as a core principle. The AI Clone ensures the Subject's personal data and value profile are never directly exposed during the Duet.
- **Consent:** Explicit, granular consent is required at each stage of the post-Duet reveal process. All consent actions are logged and auditable via the **Trust Protocol**.

## 5. Ethical Considerations
- **AI Representation:** It is made explicitly clear to the Seeker that they are interacting with an AI representation, not the user in real-time.
- **No "Failure" State:** An unsuccessful Duet is framed as a "misalignment of paths" rather than a personal rejection or failure, minimizing negative emotional impact.
- **Auditability:** All Duet sessions and subsequent consent actions are logged for ethical review and system tuning, ensuring the process remains fair and transparent.

## 6. Integration Points
- **Trust Protocol:** Manages the cryptographic consent receipts for the post-Duet reveal process.
- **Symbolic Alignment Protocol:** Informs the selection of narrative themes and the interpretation of symbolic choices.
- **Portal & Resonance Network Realms:** Provide the user-facing context and entry points for initiating Duets.
- **Agent Persona Protocol:** The AI Clone's persona is governed by the standards set in this protocol.
