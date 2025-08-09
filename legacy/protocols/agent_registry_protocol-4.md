---
title: Archive: agent_registry_protocol.md
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
tags: []
---

# Archive: agent_registry_protocol.md

This file was moved from docs/architecture/agent_framework/ as part of the project archive consolidation.

---

---
title: Agent Registry Protocol
version: 1.0
status: Draft
last_updated: {{Current Date}}
maintained_by: Hermes Orchestrator & Athena Pronoia
purpose: To define the protocol for registering, discovering, and managing AI agent classes within the ThinkAlike ecosystem.
---

# Agent Registry Protocol

## 1. Introduction

The Agent Registry Protocol governs the functionality and use of the `AgentRegistry` class (located in `src/framework/swarm/agent_registry.py`). This registry serves as a central discovery mechanism for AI agent *classes*, allowing different parts of the ThinkAlike system to dynamically access agent blueprints.

## 2. Core Principles

*   **Class-Based Registry:** The registry stores agent classes (blueprints), not instances.
*   **Caller Instantiation:** Services or orchestrators requiring an agent instance are responsible for retrieving the agent class from the registry and then instantiating it. This allows for flexible initialization with specific contexts (e.g., user-specific data).
*   **Global Scope:** A single, global `agent_registry` instance is used throughout the system.
*   **Source of Truth for `agent_type`:** The canonical list of valid `agent_type` strings and their corresponding agent classes is maintained in the human-readable document: `docs/agents/core/agent_registry.md`. This document serves as the governance point for agent type naming and registration.

## 3. `agent_type` Naming Convention and Versioning

*   **Uniqueness:** Each `agent_type` string MUST be unique across the entire system.
*   **Format:** The `agent_type` string MUST follow the convention: `"[AgentName]:v[MajorVersion]"`.
    *   Example: `"EosLumina:v1"`, `"DataWeaver:v2"`, `"ChronosOracle:v1"`.
*   **Agent Name:** `[AgentName]` is the human-readable, conceptual name of the agent.
*   **Major Version:** `v[MajorVersion]` indicates a significant iteration of the agent's interface or core functionality. Minor revisions or patches do not necessarily require a new major version in the `agent_type`.
*   **BaseAgent Version Attribute:** The `BaseAgent` class (and therefore all derived agent classes) MUST include a `version: str` attribute. This attribute should store the full version string (e.g., "1.0.0", "1.2.1") of the agent implementation, which can be more granular than the `agent_type`'s major version.

## 4. AgentRegistry Functionality

The `AgentRegistry` class provides the following key methods:

*   `register_agent(self, agent_class: Type[BaseAgent])`: Registers an agent class. The class must have an `agent_type` attribute adhering to the specified naming convention.
*   `get_agent_class(self, agent_type: str) -> Type[BaseAgent] | None`: Retrieves a specific agent class by its full `agent_type` string (e.g., `"EosLumina:v1"`).
*   `get_latest_version_class(self, agent_name: str) -> Type[BaseAgent] | None`: Given an `[AgentName]` (e.g., `"EosLumina"`), this method identifies and returns the class with the highest registered `v[MajorVersion]` for that agent name.
*   `unregister_agent(self, agent_type: str)`: Removes an agent class from the registry. This supports future dynamic loading/unloading scenarios.
*   `list_registered_agents(self) -> list[str]`: Returns a list of all registered `agent_type` strings.

## 5. Instantiation and Lifecycle Management

*   The `AgentRegistry` is NOT responsible for agent instantiation or lifecycle management.
*   Higher-level services, such as an "Agent Orchestrator," are responsible for:
    1.  Querying the registry for agent classes.
    2.  Instantiating agents as needed, potentially passing user-specific or task-specific context to their `__init__` methods.
    3.  Managing the lifecycle (activation, deactivation, error handling) of agent instances.
*   For certain core, stateless utility agents, a singleton pattern managed by such a higher-level service is a viable approach.

## 6. Dynamic Loading (Future Consideration)

While the initial implementation relies on import-time registration, the inclusion of `unregister_agent` and the clear separation of concerns are designed to facilitate future extensions for dynamic loading and unloading of agent modules or plugins.

## 7. Governance

*   Addition of new agent types or versions to the `docs/agents/core/agent_registry.md` document is a prerequisite for their recognition and use within the system.
*   The `AgentName` part of the `agent_type` should be chosen carefully to reflect the agent's role and avoid collisions.

---
This protocol ensures a consistent, version-aware, and scalable approach to managing and discovering AI agent capabilities within ThinkAlike.
