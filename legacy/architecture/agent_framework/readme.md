---
folder_type: documentation
status: Active
last_updated: 2025-06-22
maintainers: [Architectural Stewards]
---

# Agent Framework Documentation

## Purpose
This directory contains the core architectural and protocol documents that define the ThinkAlike AI Agent Framework. These documents specify how agents are designed, how they behave, interact, remember, and are managed within the ecosystem.

## Contents
This directory provides the foundational specifications for all agent-related systems.

## Key Documents

- **[`agent_ecosystem_design.md`](./agent_ecosystem_design.md)**: The high-level blueprint for the agent ecosystem, outlining agent taxonomy, cognitive architecture, and swarm intelligence principles.
- **[`agent_persona_protocol.md`](./agent_persona_protocol.md)**: Defines how to create and manage agent "personas" using YAML files, giving each agent a unique character, voice, and ethical boundaries.
- **[`agent_context_protocol.md`](./agent_context_protocol.md)**: Specifies the standardized data schema (`context` object) passed to agents, ensuring they have consistent information for their tasks.
- **[`agent_interaction_patterns.md`](./agent_interaction_patterns.md)**: Describes the key collaborative topologies (e.g., Aggregate, Reflect, Debate) that orchestrate how agents work together in swarms.
- **[`agent_memory_protocol.md`](./agent_memory_protocol.md)**: Outlines the protocol for agent memory persistence, defining how conversation histories and agent states are stored and retrieved.
- **[`agent_registry_protocol.md`](./agent_registry_protocol.md)**: Defines the system for registering and discovering agent classes, making them available to the wider system.
- **[`matching_algorithm_guide.md`](./matching_algorithm_guide.md)**: A developer guide for the value-based user matching algorithm, a key system that agents may interact with.
- **[`legacy_agent_migration_plan.md`](./legacy_agent_migration_plan.md)**: (Archived) Historical document detailing the plan to migrate legacy agent designs to the current canonical framework.

## Usage
These documents are the primary reference for any developer building, maintaining, or interacting with AI agents in the ThinkAlike project. All new agent development must adhere to these protocols.

## Dependencies
This framework is a core component of the ThinkAlike system and has dependencies on and relationships with:
- `docs/architecture/system_blueprint.md`
- `docs/seed/` (for symbolic and narrative context)
- `src/swarm/` (for the corresponding implementation)

---
For more information, see the individual protocol documents linked above.
