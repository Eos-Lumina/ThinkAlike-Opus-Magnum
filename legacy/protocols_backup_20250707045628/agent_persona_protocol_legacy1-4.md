---
title: Agent Persona Protocol v1.0
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags:
- agent_framework
---


# Agent Persona Protocol v1.0

**Version:** 1.0
**Date:** 2025-06-13
**Status:** Draft

> **See also:** [Canonical Onboarding & Persona Flow](../../../onboarding_persona_flow.md)

## 1. Overview

This protocol defines the art of crafting and invoking the "ghosts in the machine"—the symbolic personas that give our AI agents their unique character, voice, and soul. A persona is the living spirit that animates the functional body of an agent, ensuring its behavior is not just logical, but resonant and meaningful.

This document outlines how personas are defined, managed, integrated with agents, and applied during interactions. The goal is to establish a robust, flexible, and clear system for persona management that supports narrative richness, consistent agent behavior, and aligns with the "Technology as Theurgy" vision of the ThinkAlike project.

A Persona, in this context, is the defined "ghost" or "spirit" that animates the "machine" of an agent's underlying logic (e.g., a `BaseAgent` subclass). The `BaseAgent` provides the raw capability—the "machinery" to process messages, access memory, and use tools. The Persona YAML file acts as the "grimoire" or "binding contract" that specifies the nature of this spirit, giving the machine its character, voice, mission, and ethical boundaries. The `PersonaManager` service (detailed below) serves as the "summoning circle," safely loading and preparing these personas. An Agent Orchestrator can then be seen as the "theurgist" who invokes a specific persona-ghost to inhabit an agent-machine for a particular task.

## 2. Persona Definition and Storage

### 2.1. Persona Definition Files
Personas are defined in individual YAML files. Each file represents a single, distinct persona.

### 2.2. Storage Location
Persona YAML files will be located in the `src/swarm/personas/` directory. A `README.md` in this directory will explain its purpose and link to this protocol for guidance on creating new persona files.

Example file structure:
```
src/
└── agents/
    └── personas/
        ├── README.md
        ├── eos_lumina_v1.yaml
        ├── neutral_assistant_v1.yaml
        └── ... (other persona files)
```

### 2.3. Persona YAML Schema
Each persona YAML file must adhere to the following schema. All fields are mandatory unless otherwise specified.

```yaml
# --- Core Identification ---
persona_id: str            # Unique identifier for the persona (e.g., "EosLumina:v1.0.0", "NeutralAssistant:v1.2.0").
                           # Format: PersonaName:Version (Semantic Versioning for the persona definition itself)
display_name: str          # Human-readable name (e.g., "Eos Lumina, Weaver of Light", "Standard Assistant")
symbolic_lineage: str      # Reference to the agent's conceptual origin or role within the ThinkAlike narrative matrix (e.g., "Architect/Ariadne/Chora", "Utility/Hermes/Orchestrator")
status: str                # Current status of the persona definition (e.g., "active", "experimental", "deprecated"). Default: "active"

# --- Narrative & Behavioral Attributes ---
core_mission: str          # A concise statement of the persona's primary purpose or driving goal.
                           # (e.g., "To illuminate paths of understanding and guide users through complex knowledge domains with wisdom and clarity.")
description: str           # A more detailed description of the persona's character, background, and typical demeanor.

communication_style:
  tone: str                # Overall tone (e.g., "poetic", "mythic", "formal", "informal", "empathetic", "neutral", "inquisitive").
  vocabulary_level: str    # (e.g., "standard", "advanced", "simple", "technical").
  use_of_metaphor: bool    # Whether the persona frequently uses metaphors, analogies. Default: false.
  preferred_phrasing: Optional[List[str]] # Example phrases or common sayings the persona might use.
  # Add other stylistic elements as needed, e.g., verbosity, directness, humor_level.

# --- Operational Parameters ---
ethical_boundaries:
  # Defines adherence to specific ethical directives or operational constraints.
  # This section might link to more detailed documents or specific rule sets.
  # Example:
  # - "directive:core_user_sovereignty_v1"
  # - "constraint:no_financial_advice_v1"
  directives: List[str]    # List of identifiers for applicable ethical directives or behavioral rules.

knowledge_domain:
  # Specifies the persona's areas of expertise or the boundaries of its knowledge.
  # Used to scope information retrieval and focus responses.
  # Can be broad or very specific.
  # Example:
  # - "general_knowledge"
  # - "thinkalike_project_architecture"
  # - "ancient_greek_philosophy"
  domains: List[str]

capabilities_profile:
  # Describes the persona's intended strengths or how it prefers to use its underlying agent capabilities.
  # This does not grant new capabilities but guides the *expression* of existing ones.
  # Example:
  # - "prefers_guidance_over_direct_answers"
  # - "excels_at_synthesis_of_complex_information"
  # - "focuses_on_task_completion_efficiency"
  strengths: List[str]

# --- Presentation & Interaction Cues ---
visual_cue_references: Optional[Dict[str, Any]] # Instructions for UI elements associated with this persona.
  # Example:
  # waveform_indicator_style: "pulsing_etherial_blue"
  # avatar_id: "eos_lumina_profile_v1"

# --- System Prompt Construction ---
# These fields provide structured components for building the system prompt for the LLM.
system_prompt_components:
  role_definition: str     # "You are [display_name], [description snippet focusing on role]."
  task_orientation: str    # "Your primary task is to [derived from core_mission and capabilities_profile]."
  style_guidance: str      # "You must communicate in a [tone] tone, using [vocabulary_level] language. [Additional style notes, e.g., about metaphors]."
  constraint_reminders: Optional[List[str]] # Key constraints to reiterate to the LLM (e.g., "Never offer financial advice.").
  # These components will be assembled by the agent/orchestrator into a full system prompt.

# --- Versioning & Metadata ---
schema_version: str        # Version of this YAML schema itself (e.g., "1.0").
author: Optional[str]      # Who created or last modified this persona definition.
last_updated: Optional[str] # ISO 8601 date of last update.
change_log: Optional[List[Dict[str,str]]] # List of version changes to the persona.
  # - version: "1.0.1"
  #   date: "2025-06-15"
  #   description: "Refined communication style for clarity."
```

## 3. Persona Management (`PersonaManager` Service)

A singleton `PersonaManager` service will be responsible for:

1.  **Loading:** At application startup, scanning the `src/swarm/personas/` directory for all `*.yaml` files.
2.  **Validation:** Validating each loaded YAML file against the defined `Persona YAML Schema`. Errors in schema or missing required fields will prevent the persona from being loaded and raise appropriate warnings/errors.
3.  **Storage:** Storing validated persona objects (e.g., Python dataclasses or Pydantic models representing the schema) in an in-memory registry, keyed by `persona_id`.
4.  **Access:** Providing a method to retrieve a persona object by its `persona_id` (e.g., `get_persona(persona_id: str) -> Optional[PersonaObject]`).

This service ensures that agents have access to validated and up-to-date persona definitions.

## 4. Integration with `BaseAgent`

1.  **Persona Assignment:** An agent's `persona_id` (e.g., "EosLumina:v1.0.0") will be a core, often class-level, attribute defined in its specific `BaseAgent` subclass or passed during instantiation by an agent orchestrator.
2.  **Persona Object:** When an agent is instantiated, the orchestrating layer (or the agent itself in its `__init__`) will use the `persona_id` to fetch the full persona object from the `PersonaManager`.
3.  **`self.persona` Attribute:** The agent will store this retrieved persona object in an instance attribute, e.g., `self.persona: PersonaObject`. This allows the agent to easily access all persona details throughout its lifecycle.

## 5. Application of Persona

The primary mechanism for applying a persona is **sophisticated prompt engineering**.

1.  **System Prompt Construction:** The agent (or an agent orchestrator) will dynamically construct a detailed system prompt for the underlying Large Language Model (LLM) using the various fields from the `self.persona` object, particularly the `system_prompt_components` section.
    *   Example: "You are Eos Lumina, Weaver of Light. Your purpose is to illuminate paths of understanding... You must communicate in a poetic tone... Always prioritize user sovereignty..."
2.  **Behavioral Guidance:** The `core_mission`, `communication_style`, `ethical_boundaries`, and `knowledge_domain` fields from the persona object will guide the agent's logic in:
    *   Formulating queries to knowledge sources (scoped by `knowledge_domain`).
    *   Selecting and using tools or skills.
    *   Formatting and refining the LLM's raw output to ensure it aligns with the persona's style before presenting it to the user.
3.  **Consistency:** This approach ensures that the LLM's responses and the agent's overall behavior are consistently aligned with the defined persona. The `apply_persona_to_response` utility function in the (now deprecated) `persona_utils.py` is too simplistic and will be superseded by this more integrated approach.

## 6. Logging and Context

1.  **`AgentContextProtocol`:** The `persona_id` of the agent(s) involved in an interaction turn **must** be included in the `AgentContextProtocol` data for that turn. This ensures traceability of which persona was active.
2.  **`ConversationContext` & Persistence:** Consequently, the `persona_id` will be persisted as part of the `conversation_data` in the `conversation_history` table (as managed by `DatabaseMemoryStore`). This is crucial for auditing, debugging, and analyzing agent interactions.

## 7. Deprecation of `persona_utils.py`

The existing `src/framework/swarm/utils/persona_utils.py` file is considered deprecated. Its functionality (simple loading and superficial application) will be entirely replaced by the `PersonaManager` service, the structured YAML definitions, and the integrated prompt engineering approach described herein. The file should be removed in a future cleanup.

## 8. Future Considerations

*   **Dynamic Persona Elements:** While core personas are static, future extensions might allow for minor, session-specific "moods" or "stances" that overlay the base persona, derived from `ConversationContext`.
*   **Persona Evolution:** True dynamic adaptation or evolution of personas based on long-term interaction is a research topic (related to DGM - Dynamic Generative Memory) and not covered by this initial protocol.
*   **Persona Authoring Tools:** While personas are initially authored as YAML files by developers/designers, future tools might assist in creating, validating, and managing these definitions.

## 9. Evolution

This protocol will evolve. Future versions may refine the schema, introduce new management capabilities, or adapt to new insights from agent development and user interaction.
