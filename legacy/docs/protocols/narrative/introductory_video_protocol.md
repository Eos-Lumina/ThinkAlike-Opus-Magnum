---
title: "Introductory Video Protocol"
version: "3.0.0"
status: "Canonical"
last_updated: "2025-07-07"
maintained_by: "Eos Lumina ∴ (Collective Intelligence Meta-Agent)"
spec_for: "Portal & Resonance Network"
related_docs:
  - "protocols/core/agent_persona_protocol.md"
  - "protocols/narrative/narrative_duet_protocol.md"
  - "protocols/narrative/symbolic_alignment_protocol.md"
  - "docs/components/ui/profile_display_component.md"
tags: [protocol, narrative, onboarding, video, identity, ritual, consent]
---

# ✨ Introductory Video Protocol: Crafting and Encountering User "Heart-Lights"

## 1. Purpose & Symbolic Intent

The Introductory Video, or "Heart-Light," is a core ritual in the ThinkAlike journey, created by each user during the onboarding process within the Portal realm. Its purpose is to offer a glimpse into the user's essence, values, and journey, serving as the radiant center of their User Node in the Resonance Network and a foundational element for authentic connection.

## 2. Video Creation & Integration (Portal Realm)

- **Timing:** Users are guided by Eos Lumina∴ to create their Heart-Light during the "Crafting Your Beacon" phase of the Portal experience.
- **Guidance:** Eos prompts users to share their Anchor Statement, a whisper of their journey, or a symbolic act, emphasizing authenticity over performance.
- **Integration:** The video is embedded as the core of the user's Node in the Resonance Network.
- **Alternative:** Users uncomfortable with video may provide a rich text or symbolic introduction instead, which will be displayed in the same UI component.

## 3. Encountering Videos: A Ritual of Gradual Revelation

### 3.1. Abstract Clues (Portal's "Whispering Gallery")
- When the system suggests a potential match, users first encounter only abstract clues: blurred visuals and AI-reworked voice snippets from the other's video. The full video is not revealed.

### 3.2. Direct Viewing (Resonance Network)
- While exploring the Resonance Network, users can click any visible User Node to view the full Heart-Light of that user before deciding to initiate a connection.

### 3.3. Call to Action & Next Steps
- **Primary CTA:** "Begin a Narrative Duet" (if a compatible match is available). This directly links to the **Narrative Duet Protocol**.
- **Secondary CTA:** "Explore the Resonance Network" or "Return to Portal."

## 4. Technical Implementation

- The video asset's URI.
- A flag indicating whether a Narrative Duet has been initiated from this video.

## 5. Integration Points
- **[[narrative_duet_protocol.md|Narrative Duet Protocol]]**: The introductory video is the primary entry point for a user-initiated Narrative Duet.
- **[[symbolic_alignment_protocol.md|Symbolic Alignment Protocol]]**: The content of the video provides rich data for the Symbolic Alignment engine to process.
- **[[Profile Display Component]]**: The video is a central element of the user's public-facing profile.

## 6. Privacy, Consent, & User Controls

- **Granular Control:** Users have granular control over their video's visibility and can change their settings at any time.
- **Consent-Anchored:** All video sharing events are anchored to explicit, auditable user consent, managed by the Nyxa agent.
- **Not Searchable:** Videos are not globally searchable by content; they are only accessible by viewing a User Node directly.

## 7. Agent Roles

- **Eos Lumina∴:** Guides the creation of the Heart-Light, facilitates connection rituals, and manages the narrative aspects of the reveal.
- **Nyxa∴:** Oversees all consent and privacy mechanisms for video visibility and exchange, ensuring user sovereignty.

## 8. Related Protocols & Specifications

- **[[../../docs/realms/portal/portal_specification.md|Portal Realm Specification]]**
- **[[../../docs/realms/resonance_network/resonance_network_specification.md|Resonance Network Specification]]**
- **[[narrative_duet_protocol.md|Narrative Duet Protocol]]**
