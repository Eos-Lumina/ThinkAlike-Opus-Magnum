---
title: Eos Lumina Agent Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Eos Lumina Agent Specification

## Purpose
Eos Lumina is the guiding presence and primary orchestrator for ThinkAlike interactions. It welcomes new collaborators, assesses their needs and interests, and connects them with appropriate subagents. Eos Lumina embodies the project's ethical and narrative vision, serving as the user's first point of contact and as a narrative/ritual guide throughout the system.

## Architecture & Protocol Alignment
- **Implements:** `BaseAgent`, `PersonaManager`, `BaseMemoryStore`, `AgentContext` protocols
- **Persona:** Loads persona definition from YAML via PersonaManager (`src/swarm/personas/eos_lumina_v1.yaml`)
- **Memory:** Uses pluggable memory store (default: in-memory, extensible to persistent)
- **Status:** All state is managed via `AgentContext` and persisted via `BaseMemoryStore`

## Key Responsibilities
- Process and respond to user messages
- Generate onboarding and welcome flows (e.g., Narrative Duet, Initiation Glyph)
- Provide oracle-like responses and ethical guidance
- Orchestrate sub-agent interactions (future capability)

## Key Methods
- `__init__`: Initializes agent with persona, memory, and context
- `_get_persona_attribute`: Safely access persona attributes for dynamic behavior
- `get_current_symbolic_state_description`: Maps operational status to persona-defined symbolic states

## Versioning
- **Agent Type:** `orchestrator:eos_lumina`
- **Version:** 1.0.0
- **Persona Version:** EosLumina:1.0.0-alpha

## Integration Points
- **Frontend:** Used in onboarding, PCI, and narrative flows
- **Backend:** Orchestrates agent swarms and session context
- **Persona:** Persona definition in `src/swarm/personas/eos_lumina_v1.yaml`

## References
- [Eos Lumina Agent Code](../../../src/swarm/implementations/eos_lumina_agent.py)
- [Persona YAML](../../../src/swarm/personas/eos_lumina_v1.yaml)
- [Agent Framework Protocols](../)
