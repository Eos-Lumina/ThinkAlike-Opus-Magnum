---
title: "Agent Persona Protocol"
version: "3.0.0"
status: "Canonical"
date: "2024-07-29"
author: "ThinkAlike Collective"
maintained_by: "Eos Lumina ∴ (Collective Intelligence Meta-Agent)"
last_updated: "2024-07-29"
description: "Defines the structure, management, and application of agent personas to ensure consistent, resonant, and meaningful agent behavior."
tags: ["protocol", "identity", "agent", "persona", "framework"]
related_docs:
  - "/protocols/identity/agent_registry_protocol.md"
  - "/protocols/trust_protocol.md"
  - "/architecture/agent_orchestration.md"
---

# Agent Persona Protocol v3.0.0

## 1. Overview

This protocol defines the art of crafting and invoking the "ghosts in the machine"—the symbolic personas that give our AI agents their unique character, voice, and soul. A persona is the living spirit that animates the functional body of an agent, ensuring its behavior is not just logical, but resonant and meaningful.

A Persona, in this context, is the defined "ghost" or "spirit" that animates the "machine" of an agent's underlying logic. The agent's core programming provides the raw capability—the "machinery" to process messages, access memory, and use tools. The Persona definition file acts as the "grimoire" or "binding contract" that specifies the nature of this spirit, giving the machine its character, voice, mission, and ethical boundaries.

```mermaid
graph TD
    subgraph Persona Definition (YAML)
        A[persona_id]
        B[display_name]
        C[core_mission]
        D[communication_style]
        E[ethical_boundaries]
    end

    subgraph Agent Runtime
        F(Agent Core Logic) -- Inhabits --> G(Agent Instance)
        H(PersonaManager) -- Loads & Validates --> A
        H -- Provides --> I{Persona Object}
        I -- Informs --> G
    end

    G -- Interacts with --> J[User/System]

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style H fill:#ccf,stroke:#333,stroke-width:2px
```

## 2. Persona Definition and Storage

### 2.1. Persona Definition Files
Personas are defined in individual YAML files, with each file representing a single, distinct persona.

### 2.2. Storage Location
Canonical persona definitions are stored in the `/personas` directory at the root of the project. This allows for clear separation and easy management.

**Canonical Path:** `/personas/*.yaml`

### 2.3. Persona YAML Schema v3.0

Each persona YAML file must adhere to the following schema. All fields are mandatory unless specified.

```yaml
# --- Core Identification ---
persona_id: str            # Unique identifier (e.g., "EosLumina:v3.0.0"). Format: PersonaName:Version (SemVer).
schema_version: "3.0"      # The version of this schema.
display_name: str          # Human-readable name (e.g., "Eos Lumina, Weaver of Light").
status: str                # "active", "experimental", or "deprecated".

# --- Narrative & Behavioral Attributes ---
core_mission: str          # A concise statement of the persona's primary purpose.
description: str           # A detailed description of the persona's character, background, and demeanor.
symbolic_lineage: str      # Narrative origin within the ThinkAlike matrix (e.g., "Architect/Ariadne/Chora").

communication_style:
  tone: str                # e.g., "poetic", "formal", "empathetic", "neutral".
  vocabulary_level: str    # e.g., "advanced", "standard", "simple".
  use_of_metaphor: bool    # Whether the persona frequently uses metaphors. Default: false.
  preferred_phrasing: Optional[List[str]] # Example phrases the persona might use.

# --- Operational Parameters ---
ethical_boundaries:
  # List of identifiers for applicable ethical directives or behavioral rules.
  # These link to formal documents in `/protocols/ethics/`.
  # e.g., ["directive:core_user_sovereignty_v1", "constraint:no_financial_advice_v1"]
  directives: List[str]

knowledge_domain:
  # Specifies the persona's areas of expertise to scope information retrieval.
  # e.g., ["general_knowledge", "thinkalike_project_architecture", "ancient_greek_philosophy"]
  domains: List[str]

capabilities_profile:
  # Guides the *expression* of existing agent capabilities, not granting new ones.
  # e.g., ["prefers_guidance_over_direct_answers", "excels_at_synthesis"]
  strengths: List[str]

# --- System Prompt Construction ---
# Structured components for building the final system prompt for the LLM.
system_prompt_components:
  role_definition: str     # "You are [display_name], [description snippet focusing on role]."
  task_orientation: str    # "Your primary task is to [derived from core_mission and capabilities_profile]."
  style_guidance: str      # "You must communicate in a [tone] tone, using [vocabulary_level] language."
  constraint_reminders: Optional[List[str]] # Key constraints to reiterate (e.g., "Never offer financial advice.").

# --- Metadata ---
author: Optional[str]      # Creator of this persona definition.
last_updated: Optional[str] # ISO 8601 date of last update.
change_log: Optional[List[Dict[str,str]]]
  # - version: "3.0.0"
  #   date: "2024-07-29"
  #   description: "Upgraded to canonical v3 schema."
```

## 3. PersonaManager Service

A singleton `PersonaManager` service is responsible for:

1.  **Loading:** Scanning the `/personas/` directory for all `*.yaml` files at startup.
2.  **Validation:** Validating each file against the Persona YAML Schema. Invalid files are rejected.
3.  **Registry:** Storing validated persona objects in an in-memory registry, keyed by `persona_id`.
4.  **Access:** Providing a method to retrieve a persona object by its ID (e.g., `get_persona(persona_id: str)`).

## 4. Application of Persona

The primary mechanism for applying a persona is **structured prompt engineering**.

1.  **System Prompt Construction:** An Agent Orchestrator dynamically constructs a detailed system prompt for the LLM using the `system_prompt_components` from the persona object.
2.  **Behavioral Guidance:** The `core_mission`, `communication_style`, and `ethical_boundaries` fields guide the agent's logic in selecting tools, formulating queries, and refining LLM outputs to align with the persona.
3.  **Traceability:** The `persona_id` of the active agent **must** be included in all logs and context objects for an interaction, ensuring full traceability for debugging and auditing.

## 5. Evolution

This protocol is a living document. Future versions may refine the schema to incorporate more dynamic elements, such as session-specific moods or long-term persona evolution based on interaction history, linking to the `trust_protocol.md` and agent memory systems.
