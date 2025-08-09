---
title: Identity Resonance Score (IRS)
version: 3.0.0
status: Canonical
last_updated: 2025-07-07
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
spec_id: PROTO-IRS-001
tags:
  - protocol
  - resonance
  - identity
  - matching
  - trust
---

# Identity Resonance Score (IRS)

- **Version:** 3.0.0
- **Status:** Canonical
- **Date:** 2025-07-07
- **Related Documents:**
  - [[protocols/trust_protocol|Trust Protocol]]
  - [[protocols/resonance_logic_protocol|Resonance Logic Protocol]]
  - [[docs/realms/portal/portal_specification|Portal Realm]]
  - [[docs/realms/resonance_network/resonance_network_specification|Resonance Network]]

## 1. Purpose

The Identity Resonance Score (IRS) is a core internal metric used within the ThinkAlike ecosystem to quantify the degree of harmonic compatibility and potential for meaningful connection between two user identities. Moving beyond simplistic affinity metrics, the IRS is a multilayered symbolic score. It is designed to reflect nuanced alignment across deeply elicited values, narrative structures, symbolic language, and cognitive styles.

The IRS serves several key internal functions:
- It informs the **Resonance Priming** feature within the Resonance Network Realm, highlighting potential pathways and User Nodes that exhibit high baseline compatibility.
- It guides an agent's responses and behavioral nuances during a **Narrative Duet**, ensuring the interaction authentically reflects the represented user's profile.
- It provides a foundational input for assessing alignment during and after a Narrative Duet.
- It is a key element in the learning and attunement process of the core resonance logic, allowing the network to refine its understanding of what constitutes genuine resonance based on outcomes and consensual user feedback.

**Crucially, the IRS is an internal system metric used to orchestrate and refine the potential for connection. It is NOT directly exposed to users as a blunt "Matching Percentage."** Users experience the effects of the IRS through the qualitative richness of the system's guidance and the emergent highlighting of pathways in the Resonance Network.

## 2. Structure & Derivation

The IRS is calculated as a weighted composite of several contributing dimensions, primarily derived from a user's comprehensive `UserValueProfile` which is forged throughout their Portal Realm journey.

| Dimension | Description | Primary Source/Derivation in Portal Journey |
|---|---|---|
| **Value Alignment** | Degree of overlap, harmony, or constructive complementarity between declared core values, articulated ethical stances, and decision patterns. | Initial 3 Questions, choices in Ethical Dilemmas, Mirror Oath responses, Anchor Statement. |
| **Narrative Synchrony** | Resonance of storytelling motifs, life metaphors, formative experiences, and thematic content. | Responses to symbolic scenarios, chosen narrative paths, themes in introductory video. |
| **Symbolic Overlap** | Shared or complementary use of archetypes, metaphors, Initiation Glyphs, and mytho-linguistic references. | Archetypal choices ("Seeds of Self"), riddle reflections, symbolic language used in any free-text inputs. |
| **Cognitive Orientation** | Similarity or generative complementarity in epistemic styles and reasoning heuristics. | Inferred from interaction with specific types of narrative prompts and problem-solving approaches in dilemmas. |
| **Communicative Rhythm** | Coherence in language complexity, expressive tone (e.g., poetic, analytical), and tempo of interaction. | Analysis of user's expressive outputs (e.g., Anchor Statement, free-text responses). |

These components are normalized and aggregated using a harmonic weighting function that favors constructive complementarity and deep value resonance over superficial similarity. The specific algorithms are detailed in the **Resonance Logic Protocol**.

## 3. Conceptual Formula

The IRS between two users (u₁ and u₂) can be conceptually represented as:

**IRS(u₁, u₂) = Σ [ w_d * C_d(u₁, u₂) ]**

Where:
- `d` is a dimension from the table above (Value, Narrative, etc.).
- `w_d` is the weight assigned to that dimension.
- `C_d` is the compatibility function for that dimension.

This formula is a simplified representation. The actual implementation involves more complex, non-linear models as defined in the **Resonance Logic Protocol**.

## 4. Privacy & Ethics

- The calculation of the IRS is a read-only operation on the `UserValueProfile`.
- The score itself is ephemeral or stored with strict access controls, accessible only to the core Resonance Engine and authorized audit agents.
- Users have control over the inputs to their `UserValueProfile` and can modify them, which will in turn affect their IRS with others.
