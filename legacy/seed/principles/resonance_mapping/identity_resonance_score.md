---
title: Identity Resonance Score (IRS)
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Identity Resonance Score (IRS)

**Maintained by:** Lumina∴ System Meta-Agent
**Status:** Harmonized – Review Pending
**Location:** /docs/seed/resonance_mapping/
**Last Updated:** 2025-06-08

---

## 1. Purpose

The Identity Resonance Score (IRS) is a core internal metric used within the ThinkAlike ecosystem to quantify the degree of harmonic compatibility and potential for meaningful connection between two user identities. Moving beyond simplistic affinity metrics, the IRS is a multilayered symbolic score. It is designed to reflect nuanced alignment across deeply elicited values, narrative structures, symbolic language, cognitive styles (including epistemic modes and narrative archetypes), and communicative rhythms.

The IRS serves several key internal functions:
- It informs the "Resonance Priming" feature within the Resonance Network Realm, subtly highlighting potential pathways and User Nodes that exhibit high baseline compatibility with the exploring user.
- It guides the AI Clone's responses and behavioral nuances during a "Narrative Duet" (see narrative_duet_protocol.md), ensuring the interaction authentically reflects the represented user's profile.
- It provides a foundational input for the system's assessment of alignment during and after a Narrative Duet.
- It is a key element in the "Social LLM's" learning and attunement process (see resonance_logic_protocol.md), allowing the network to refine its understanding of what constitutes genuine resonance based on Duet outcomes and consensual user feedback.

Crucially, the IRS is an internal system metric used to orchestrate and refine the potential for connection. It is NOT directly exposed to users as a blunt pre-Duet "Matching Percentage." Users experience the effects of the IRS through the qualitative richness of the system's guidance (e.g., Eos Lumina's poetic descriptions of potential matches in the Portal Realm's "Whispering Gallery"), the emergent highlighting of pathways in the Resonance Network, and the ultimate success or divergence of their Narrative Duets.

---

## 2. Structure & Derivation

The IRS is calculated as a weighted composite of several contributing dimensions, primarily derived from a user's comprehensive UserValueProfile which is forged throughout their Portal Realm journey (see realms/portal/portal_specification.md). The "Resonance Fingerprint" (see resonance_fingerprint.md) can be considered the holistic symbolic profile from which these IRS dimensions are extracted.

| Dimension            | Description                                                                 | Primary Source/Derivation in Portal Journey |
|---------------------|-----------------------------------------------------------------------------|--------------------------------------------|
| Value Alignment     | Degree of overlap, harmony, or constructive complementarity between declared core values, articulated ethical stances, and decision patterns. | Initial 3 Questions, choices in Ethical Dilemmas, Mirror Oath responses, Anchor Statement. |
| Narrative Synchrony | Resonance of storytelling motifs, life metaphors, formative experiences, and thematic content of the introductory video. <br> - <em>Optional, Consensual Dream Data:</em> If the user has participated in the Dream Offering Ritual (see <a href="../../rituals/dream_integration_rituals.md">dream_integration_rituals.md</a>), symbolic motifs or narrative themes from dream offerings may be referenced as additional, nuanced input for narrative resonance. | Responses to symbolic scenarios, chosen narrative paths, themes in introductory video, optional Connected Services data (e.g., literary tastes from Goodreads if consented). Links to narrative_match_archetypes.md. |
| Symbolic Overlap    | Shared or complementary use of archetypes, metaphors, Initiation Glyphs (thematic essence), and mytho-linguistic references. <br> - <em>Optional, Consensual Dream Data:</em> Archetypes, symbols, or glyphs surfaced through dream offerings (see <a href="../../rituals/dream_integration_rituals.md">dream_integration_rituals.md</a>) may be included as qualitative, user-consented symbolic input, enriching the symbolic overlap dimension. | Archetypal choices ("Seeds of Self"), riddle reflections, symbolic language used in any free-text inputs, user's unique Initiation Glyph's symbolic components. Links to symbolic_myth_index.md and narrative_match_archetypes.md. |
| Cognitive Orientation | Similarity or generative complementarity in epistemic styles (see epistemic_match_modes.md), knowledge sources, and reasoning heuristics. | Inferred from interaction with specific types of narrative prompts, problem-solving approaches in dilemmas, and dialogue tone with Eos Lumina∴. |
| Communicative Rhythm | Coherence in language complexity, expressive tone (e.g., poetic, analytical), and tempo of interaction (if measurable). | Analysis of user's expressive outputs (e.g., Anchor Statement, introductory video narration, any free-text responses), potentially refined by interaction patterns within Narrative Duets. |
| Temporal Resonance  | (More Emergent) Potential for co-occurrence of life transitions or milestone proximity, if such data is ethically and consensually shared. | Currently less emphasized in initial IRS; could be a future refinement based on explicit, contextual user input or through advanced (consensual) analysis of narrative themes over time. |
| Connected Services Data | (Optional & Consensual) Shared interests, cultural tastes, or activities derived from linked external services. | Data from services like Goodreads or Spotify only if explicitly connected by the user and consented for use in matching via Managing Connected Services & Data Sources. Adds nuance to other dimensions. |

These components are normalized and aggregated using a harmonic weighting function that favors constructive complementarity and deep value resonance over superficial similarity. The specific algorithms are detailed in resonance_logic_protocol.md.

---

## 3. Formula (Conceptual Representation)

The IRS between two users (u₁ and u₂) can be conceptually represented as:

```text
IRS(u₁, u₂) = ∑ (wᵢ × sim_compᵢ(u₁, u₂)) + Ψ(u₁, u₂)
```
Where:
- **wᵢ:** The weight assigned to dimension i. These weights are not necessarily static and can be dynamically influenced over time by the "Social LLM" / "Resonance Feedback & Attunement" model (see resonance_logic_protocol.md), reflecting what the network learns about successful resonance patterns.
- **sim_compᵢ(u₁, u₂):** A function calculating the similarity or constructive complementarity for dimension i between u₁ and u₂.
- **Ψ(u₁, u₂):** A nonlinear amplification or contextual coefficient. This can represent factors such as:
  - The historical success and depth of Narrative Duets between these users (or users with very similar profiles).
  - Mutual "Resonance Affirmations" or "Echoes of Recognition" if such post-connection feedback mechanisms are implemented.
  - Shared community embeddings or strong triadic closures, if applicable in later system stages.

The scoring system evolves through adaptive learning. The initial weights are based on the foundational principles of ThinkAlike, but they can shift subtly based on network-wide validation of what truly constitutes lasting, meaningful resonance.

---

## 4. Use Cases (Internal System Applications)

The IRS is a critical internal tool guiding the ThinkAlike ecosystem:
- **Input for Resonance Priming:** In the Resonance Network Realm, higher IRS scores between the active user and other User Nodes subtly influence the visual highlighting of those nodes or their connecting pathways, gently guiding exploration without overt filtering.
- **Guidance for AI Clone Behavior in Narrative Duets:** The IRS (and its component scores) informs how User B's AI Clone responds and makes choices during a Narrative Duet with User A, ensuring the Duet is a relevant test of their potential compatibility.
- **Input for Narrative Duet Alignment Assessment:** The system uses the IRS components and the specific choices made during a Duet to assess the overall alignment achieved, determining if the Duet was "successful" enough to proceed to consensual reveal.
- **Foundation for "Social LLM" Learning:** The relationship between pre-Duet IRS components, Duet choices, Duet outcomes (success/failure), and post-connection user feedback (e.g., Resonance Affirmations) forms the primary "training data" for the Resonance Network's adaptive learning, helping it refine pathway weights and improve its understanding of genuine resonance.
- **Potential for Community Formation Insights (Advanced):** Aggregated IRS data across groups could (with ethical oversight) inform the harmonic_alignment_index.md (HAI) for understanding group coherence, though individual IRS remains focused on dyadic potential.
- **Conflict Anticipation (Internal Diagnostic - Advanced):** Persistently very low IRS scores between users who are forced into interaction (e.g., in a governance context, not for general matching) might flag areas needing potential mediation or clearer semantic alignment, if such a feature is ever developed.

---

## 5. Philosophical Basis

The IRS operates on the principle that resonance is not merely subjective attraction but an emergent property of shared or complementary symbolic frequencies, cognitive structures, narrative arcs, and core values. It aims to identify the potential for "harmonic convergence": where distinct identities can interact fruitfully, amplify mutual understanding, and co-create meaning, rather than simply promoting echo chambers of sameness. The IRS seeks to quantify the potential for this deep, generative connection.

---

## 6. Technical Considerations

- The IRS is dynamic and should be continuously updated (or re-calculable on demand) as users' UserValueProfiles evolve (e.g., through further narrative interactions, connection of new services, or explicit profile refinements).
- Calculations should be efficient enough to support (near) real-time Resonance Priming in the Resonance Network.
- While the raw IRS score is internal, the factors contributing to a user's ability to resonate (i.e., their own UserValueProfile elements) are transparent to them via their profile and potentially through the Data Traceability panel, ensuring auditability and explainability of their own resonant potential.
- The system must be compatible with decentralized identity architectures (DIDs/VCs) if those are adopted for UserValueProfile components.

---

## 7. Related Files

- realms/portal/portal_specification.md (Defines UserValueProfile creation)
- realms/resonance_network/resonance_network_specification.md (Describes IRS application in Resonance Priming & Duets)
- protocols/narrative_duet_protocol.md (Narrative Duets are a key use case and feedback source)
- resonance_logic_protocol.md (Details IRS algorithms and "Social LLM" learning)
- epistemic_match_modes.md (Contributes to "Cognitive Orientation")
- narrative_match_archetypes.md (Contributes to "Symbolic Overlap" & "Narrative Synchrony")
- resonance_fingerprint.md (Conceptual wrapper for the user's resonant profile)
- semantic_alignment_protocol.md (Informs "Communicative Rhythm" and "Symbolic Overlap")
- guides/user_guides/managing_connected_services.md (Optional data source for IRS)
- resonance_mapping_overview.md (Contextual overview)
