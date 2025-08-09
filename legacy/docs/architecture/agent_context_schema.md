---
title: "Agent Context Schema"
version: 3.0.0
status: Canonical
last_updated: 2025-07-08
authors:
  - "Eos Lumina ∴ (Collective Intelligence Meta-Agent)"
tags: [architecture, schema, agent, context, data_model]
spec_for: [Backend Developers, Agent Developers]
harmonization_note: |
  Canonicalized from the v1.1 draft of the Agent Context Protocol. This document was reclassified as an architectural schema, as it defines a critical data structure, not a procedural protocol. It specifies the standard `context` object passed to and between agents, ensuring consistent and sufficient information for processing requests.
---

# Agent Context Schema

## 1. Vision & Purpose

This document specifies the standard structure and content of the `context` object that accompanies messages and interactions throughout the ThinkAlike agent framework. A standardized context schema is essential for interoperability, ensuring that agents have consistent and sufficient information to process requests, maintain state, evaluate relevance, and interact coherently within the broader narrative and symbolic environment.

This schema is the blueprint for the primary data object used by the Agent Orchestrator to manage and direct agent activity.

## 2. Context Object Schema Definition

The `context` object MUST be a JSON-serializable dictionary adhering to the following structure. Fields are OPTIONAL unless otherwise specified, but core fields are strongly RECOMMENDED for most interactions.

```json
{
  "context_id": "uuid",
  "session_id": "uuid",
  "message_id": "uuid",
  "request_id": "uuid",
  "timestamp_utc": "iso_datetime_string",
  "source_entity": {
    "id": "string",
    "type": "string"
  },
  "target_agent_id": "uuid",
  "active_persona_id": "string",
  "user_profile": {
    "user_id": "uuid",
    "archetypal_alignment": {
      "primary_archetype": "string",
      "secondary_archetype": "string",
      "alignment_strength": "float"
    },
    "resonance_fingerprint_summary": "object"
  },
  "narrative_state": {
    "current_thread_id": "string",
    "current_realm": "string",
    "current_ritual_id": "string",
    "symbolic_focus": ["string"],
    "mythic_overlay_active": "string"
  },
  "interaction_history_summary": {
    "previous_exchange_summary": "string",
    "relevant_message_ids": ["uuid"]
  },
  "system_state": {
    "current_system_load": "string",
    "active_anomalies": ["string"]
  },
  "processing_directives": {
    "requested_action": "string",
    "response_constraints": {
      "max_length": "integer",
      "format": "string"
    },
    "priority": "integer"
  },
  "custom_data": {}
}
```

## 3. Key Field Descriptions

*   **`context_id` (Required):** A UUID for this specific context snapshot. Generated each time a context is constructed.
*   **`session_id` (Required):** The persistent identifier for the overarching user session, used to retrieve the full `ConversationContext` from the memory store.
*   **`message_id`:** The ID of the primary message this context relates to.
*   **`timestamp_utc` (Required):** The UTC timestamp of context creation.
*   **`source_entity` (Required):** An object identifying the entity generating the context (e.g., `{ "id": "user-123", "type": "user" }`).
*   **`target_agent_id`:** The ID of the agent primarily intended to process this context.
*   **`active_persona_id` (Required):** The ID of the persona the target agent is currently embodying. See [`/protocols/core/agent_persona_protocol.md`](/protocols/core/agent_persona_protocol.md).
*   **`user_profile`:** Key information about the user, crucial for personalization and resonance.
*   **`narrative_state`:** Situates the interaction within the ThinkAlike's dynamic narrative framework.
*   **`interaction_history_summary`:** Provides a window into the immediate conversational past. This is a *summary* and does not contain the full message history, which resides in the memory store and is accessed via `session_id`.
*   **`processing_directives`:** Specific instructions for the receiving agent.
*   **`custom_data`:** An open object for agent-specific or task-specific contextual data.

## 4. Relationship to Other Documents

-   This schema is the data payload managed by the **Agent Orchestrator** ([`/architecture/agent_orchestration.md`](/architecture/agent_orchestration.md)).
-   The `session_id` is the key used to retrieve full conversation histories via the **Agent Memory Protocol** ([`/protocols/core/agent_memory_protocol.md`](/protocols/core/agent_memory_protocol.md)).
-   The `active_persona_id` is resolved using the **Agent Persona Protocol** ([`/protocols/core/agent_persona_protocol.md`](/protocols/core/agent_persona_protocol.md)).
-   The structure of the data within fields like `user_profile` and `narrative_state` is defined in the main **Data Architecture** document ([`/architecture/data_architecture.md`](/architecture/data_architecture.md)).
