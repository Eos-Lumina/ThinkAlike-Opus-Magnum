---
title: Canonical Onboarding & Persona Flow
status: Draft – Harmonization in Progress
last_updated: 2025-06-18
maintained_by: Documentation Team & Persona Stewards
related_docs:
  - ../realms/portal/portal_specification.md
  - ../realms/resonance_network/resonance_network_specification.md
  - ../protocols/narrative_duet_protocol.md
  - ../architecture/agent_framework/agent_persona_protocol.md
---

# Canonical Onboarding & Persona Flow

This document unifies the onboarding journey and persona assignment process in ThinkAlike, cross-linking all major realms and protocols.

## 1. Onboarding Journey Overview

1. **Portal Realm:**
   - User enters the system, guided by Eos Lumina∴.
   - Completes value elicitation, Initiation Glyph, and Invocation Phrase.
   - Forms their UserValueProfile and digital identity.
2. **Narrative Duet (Portal):**
   - System-suggested first match via Narrative Duet protocol.
   - Outcome determines initial resonance and connection.
3. **Resonance Network Realm:**
   - User explores the constellation map, discovers other users.
   - Can initiate further Narrative Duets for compatibility testing.
   - Successful duets and mutual consent form new connections.
4. **Persona Assignment:**
   - Agent personas (see Agent Persona Protocol) guide, facilitate, and record onboarding and narrative flows.
   - Persona YAMLs define agent behavior, style, and ethical boundaries throughout the journey.

## 2. Data Models & Protocols
- All onboarding and persona flows are reflected in the canonical data models (`../architecture/data_models.md`) and OpenAPI spec (`../api_specs/openapi.json`).
- NarrativeDuetSession, UserValueProfile, and Persona are key entities.

## 3. Integration Points
- **Portal Realm:** Onboarding UI, value elicitation, glyph/phrase creation, Eos Lumina persona.
- **Resonance Network:** Constellation map, Narrative Duet initiation, connection management.
- **Agent System:** PersonaManager, persona YAMLs, agent orchestration.

## 4. Cross-References
- [Portal Realm Specification](../realms/portal/portal_specification.md)
- [Resonance Network Realm Specification](../realms/resonance_network/resonance_network_specification.md)
- [Narrative Duet Protocol](../protocols/narrative_duet_protocol.md)
- [Agent Persona Protocol](../architecture/agent_framework/agent_persona_protocol.md)

---
*This document is a living specification. Update as onboarding, persona, and narrative flows evolve.*
