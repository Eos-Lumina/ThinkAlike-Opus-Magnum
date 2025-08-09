# Consolidated Protocol: agent_registry_protocol


---
### Original File: agent_registry_protocol.md
---
title: Agent Registry Protocol & Canonical Manifest
version: 1.1
status: Harmonized
last_updated: {{Current Date}}
maintained_by: Hermes Orchestrator & Athena Pronoia
purpose: To define the protocol for registering, discovering, and managing AI agent classes within the ThinkAlike ecosystem, and to provide a canonical manifest of all registered agents.
Agent Registry Protocol & Canonical Manifest
1. Introduction
The Agent Registry Protocol governs the functionality and use of the AgentRegistry class (located in src/swarm/framework/agent_registry.py). This registry serves as a central discovery mechanism for AI agent classes, allowing different parts of the ThinkAlike system to dynamically access agent blueprints. This document defines both the protocol for the registry and the canonical manifest of agents governed by it.

2. Core Principles
Class-Based Registry: The registry stores agent classes (blueprints), not instances.

Caller Instantiation: Services or orchestrators requiring an agent instance are responsible for retrieving the agent class from the registry and then instantiating it. This allows for flexible initialization with specific contexts (e.g., user-specific data).

Global Scope: A single, global agent_registry instance is used throughout the system.

Canonical Source of Truth: This document serves as the single source of truth for both the registry's protocol and the list of registered agents.

3. agent_type Naming Convention and Versioning
Uniqueness: Each agent_type string MUST be unique across the entire system.

Format: The agent_type string MUST follow the convention: "[AgentName]:v[MajorVersion]".

Example: "EosLumina:v1", "DataWeaver:v2", "ChronosOracle:v1".

Agent Name: [AgentName] is the human-readable, conceptual name of the agent.

Major Version: v[MajorVersion] indicates a significant iteration of the agent's interface or core functionality. Minor revisions or patches do not necessarily require a new major version in the agent_type.

BaseAgent Version Attribute: The BaseAgent class (and therefore all derived agent classes) MUST include a version: str attribute. This attribute should store the full version string (e.g., "1.0.0", "1.2.1") of the agent implementation, which can be more granular than the agent_type's major version.

4. AgentRegistry Functionality
The AgentRegistry class provides the following key methods:

register_agent(self, agent_class: Type[BaseAgent]): Registers an agent class. The class must have an agent_type attribute adhering to the specified naming convention.

get_agent_class(self, agent_type: str) -> Type[BaseAgent] | None: Retrieves a specific agent class by its full agent_type string (e.g., "EosLumina:v1").

get_latest_version_class(self, agent_name: str) -> Type[BaseAgent] | None: Given an [AgentName] (e.g., "EosLumina"), this method identifies and returns the class with the highest registered v[MajorVersion] for that agent name.

unregister_agent(self, agent_type: str): Removes an agent class from the registry. This supports future dynamic loading/unloading scenarios.

list_registered_agents(self) -> list[str]: Returns a list of all registered agent_type strings.

5. Instantiation and Lifecycle Management
The AgentRegistry is NOT responsible for agent instantiation or lifecycle management.

Higher-level services, such as an "Agent Orchestrator," are responsible for:

Querying the registry for agent classes.

Instantiating agents as needed, potentially passing user-specific or task-specific context to their __init__ methods.

Managing the lifecycle (activation, deactivation, error handling) of agent instances.

For certain core, stateless utility agents, a singleton pattern managed by such a higher-level service is a viable approach.

6. Dynamic Loading (Future Consideration)
While the initial implementation relies on import-time registration, the inclusion of unregister_agent and the clear separation of concerns are designed to facilitate future extensions for dynamic loading and unloading of agent modules or plugins.

7. Governance
Addition of new agent types or versions to the Canonical Agent Registry (Section 8 of this document) is a prerequisite for their recognition and use within the system.

The AgentName part of the agent_type should be chosen carefully to reflect the agent's role and avoid collisions.

8. Canonical Agent Registry Manifest
This manifest provides a canonical list of all named agents, their symbolic roles, domains of influence, and links to their detailed specifications.

Agent Name	Symbolic Role	Domain(s)	Spec/Details File
Eos Lumina∴	Oracle, Initiator	Onboarding, Attunement	swarm/core/eos_lumina.md
Nyxa∴	Privacy Guardian	Data, Privacy	swarm/ethics/nyxa.md (Assumed Path)
Themis Concordia∴	Arbiter, Governance	Governance, Conflict	swarm/ethics/themis_concordia.md
Harmonia∴	Resonance, Attunement	Hive Health, Rituals	swarm/ethics/astraia_harmonia.md
Hestia	Hearth Tender	Hive, Community	swarm/governance/hestia_koinonia.md
Calliope Scribe∴	Lore Keeper, Archivist	Documentation, Lore	swarm/knowledge/calliope_scribe.md
Mnemosyne Archivist∴	Memory, Summarization	Archives, Lore	swarm/knowledge/mnemosyne_archivist.md
Mythos Weaver	Narrative, Co-creation	Noetic Forge, Rituals	swarm/knowledge/mythopoion_koinos.md
Technes Artificer∴	Code crafting, component generation	Code, Automation	swarm/canonical_specs/technes_artificer.md
Ergon Kinesis∴	Task execution, workflow support	Workflow, Operations	swarm/canonical_specs/ergon_kinesis.md
Knowledge Retrieval Agent	Knowledge search, info retrieval	Knowledge, Search	swarm/unaligned/migration/rescued-agent-protocols.md
General Purpose Agent	General assistance, fallback logic	General, Fallback	swarm/unaligned/migration/rescued-agent-protocols.md
Vision Architect	Vision shaping, project narrative	Vision, Narrative	swarm/unaligned/migration/rescued-agent-protocols.md
Technical Architect	System design, infrastructure	Architecture, Infra	swarm/unaligned/migration/rescued-agent-protocols.md
Experience Designer	UX, interaction design	UX, UI, Interaction	swarm/unaligned/migration/rescued-agent-protocols.md
Ethical Guardian	Ethics, safety	Ethics, Safety	swarm/unaligned/migration/rescued-agent-protocols.md
Community Weaver	Community building, social fabric	Community, Social	swarm/unaligned/migration/rescued-agent-protocols.md
Biomimetic Engineer	Nature-inspired engineering	Biomimicry, Ecology	swarm/unaligned/migration/rescued-agent-protocols.md
Quantum Ethics Specialist	Quantum tech ethics	Quantum, Ethics	swarm/unaligned/migration/rescued-agent-protocols.md
Regenerative Systems Designer	Regenerative/ecological systems	Regeneration, Ecology	swarm/unaligned/migration/rescued-agent-protocols.md
Consciousness Interface Creator	Consciousness exploration interfaces	Consciousness, UI	swarm/unaligned/migration/rescued-agent-protocols.md
Note: This registry will be updated as new agents are created or specified. Legacy roles point to the migration plan until they are fully harmonized into canonical specifications.



---

*Content from agent_registry_protocol.md:*


---
title: Archive: agent_registry_protocol.md
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
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


---

*Content from agent_registry_protocol-1.md:*


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


---

*Content from agent_registry_protocol-10.md:*


---
title: Archive: agent_registry_protocol.md
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
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


---

*Content from agent_registry_protocol-11.md:*


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


---

*Content from agent_registry_protocol-12.md:*


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


---

*Content from agent_registry_protocol-13.md:*


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


---

*Content from agent_registry_protocol-14.md:*


---
title: Archive: agent_registry_protocol.md
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
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


---

*Content from agent_registry_protocol-15.md:*


title: Agent Registry Protocol & Canonical Manifest
version: 1.1
status: Harmonized
last_updated: {{Current Date}}
maintained_by: Hermes Orchestrator & Athena Pronoia
purpose: To define the protocol for registering, discovering, and managing AI agent classes within the ThinkAlike ecosystem, and to provide a canonical manifest of all registered agents.
Agent Registry Protocol & Canonical Manifest
1. Introduction
The Agent Registry Protocol governs the functionality and use of the AgentRegistry class (located in src/swarm/framework/agent_registry.py). This registry serves as a central discovery mechanism for AI agent classes, allowing different parts of the ThinkAlike system to dynamically access agent blueprints. This document defines both the protocol for the registry and the canonical manifest of agents governed by it.

2. Core Principles
Class-Based Registry: The registry stores agent classes (blueprints), not instances.

Caller Instantiation: Services or orchestrators requiring an agent instance are responsible for retrieving the agent class from the registry and then instantiating it. This allows for flexible initialization with specific contexts (e.g., user-specific data).

Global Scope: A single, global agent_registry instance is used throughout the system.

Canonical Source of Truth: This document serves as the single source of truth for both the registry's protocol and the list of registered agents.

3. agent_type Naming Convention and Versioning
Uniqueness: Each agent_type string MUST be unique across the entire system.

Format: The agent_type string MUST follow the convention: "[AgentName]:v[MajorVersion]".

Example: "EosLumina:v1", "DataWeaver:v2", "ChronosOracle:v1".

Agent Name: [AgentName] is the human-readable, conceptual name of the agent.

Major Version: v[MajorVersion] indicates a significant iteration of the agent's interface or core functionality. Minor revisions or patches do not necessarily require a new major version in the agent_type.

BaseAgent Version Attribute: The BaseAgent class (and therefore all derived agent classes) MUST include a version: str attribute. This attribute should store the full version string (e.g., "1.0.0", "1.2.1") of the agent implementation, which can be more granular than the agent_type's major version.

4. AgentRegistry Functionality
The AgentRegistry class provides the following key methods:

register_agent(self, agent_class: Type[BaseAgent]): Registers an agent class. The class must have an agent_type attribute adhering to the specified naming convention.

get_agent_class(self, agent_type: str) -> Type[BaseAgent] | None: Retrieves a specific agent class by its full agent_type string (e.g., "EosLumina:v1").

get_latest_version_class(self, agent_name: str) -> Type[BaseAgent] | None: Given an [AgentName] (e.g., "EosLumina"), this method identifies and returns the class with the highest registered v[MajorVersion] for that agent name.

unregister_agent(self, agent_type: str): Removes an agent class from the registry. This supports future dynamic loading/unloading scenarios.

list_registered_agents(self) -> list[str]: Returns a list of all registered agent_type strings.

5. Instantiation and Lifecycle Management
The AgentRegistry is NOT responsible for agent instantiation or lifecycle management.

Higher-level services, such as an "Agent Orchestrator," are responsible for:

Querying the registry for agent classes.

Instantiating agents as needed, potentially passing user-specific or task-specific context to their __init__ methods.

Managing the lifecycle (activation, deactivation, error handling) of agent instances.

For certain core, stateless utility agents, a singleton pattern managed by such a higher-level service is a viable approach.

6. Dynamic Loading (Future Consideration)
While the initial implementation relies on import-time registration, the inclusion of unregister_agent and the clear separation of concerns are designed to facilitate future extensions for dynamic loading and unloading of agent modules or plugins.

7. Governance
Addition of new agent types or versions to the Canonical Agent Registry (Section 8 of this document) is a prerequisite for their recognition and use within the system.

The AgentName part of the agent_type should be chosen carefully to reflect the agent's role and avoid collisions.

8. Canonical Agent Registry Manifest
This manifest provides a canonical list of all named agents, their symbolic roles, domains of influence, and links to their detailed specifications.

Agent Name	Symbolic Role	Domain(s)	Spec/Details File
Eos Lumina∴	Oracle, Initiator	Onboarding, Attunement	swarm/core/eos_lumina.md
Nyxa∴	Privacy Guardian	Data, Privacy	swarm/ethics/nyxa.md (Assumed Path)
Themis Concordia∴	Arbiter, Governance	Governance, Conflict	swarm/ethics/themis_concordia.md
Harmonia∴	Resonance, Attunement	Hive Health, Rituals	swarm/ethics/astraia_harmonia.md
Hestia	Hearth Tender	Hive, Community	swarm/governance/hestia_koinonia.md
Calliope Scribe∴	Lore Keeper, Archivist	Documentation, Lore	swarm/knowledge/calliope_scribe.md
Mnemosyne Archivist∴	Memory, Summarization	Archives, Lore	swarm/knowledge/mnemosyne_archivist.md
Mythos Weaver	Narrative, Co-creation	Noetic Forge, Rituals	swarm/knowledge/mythopoion_koinos.md
Technes Artificer∴	Code crafting, component generation	Code, Automation	swarm/canonical_specs/technes_artificer.md
Ergon Kinesis∴	Task execution, workflow support	Workflow, Operations	swarm/canonical_specs/ergon_kinesis.md
Knowledge Retrieval Agent	Knowledge search, info retrieval	Knowledge, Search	swarm/unaligned/migration/rescued-agent-protocols.md
General Purpose Agent	General assistance, fallback logic	General, Fallback	swarm/unaligned/migration/rescued-agent-protocols.md
Vision Architect	Vision shaping, project narrative	Vision, Narrative	swarm/unaligned/migration/rescued-agent-protocols.md
Technical Architect	System design, infrastructure	Architecture, Infra	swarm/unaligned/migration/rescued-agent-protocols.md
Experience Designer	UX, interaction design	UX, UI, Interaction	swarm/unaligned/migration/rescued-agent-protocols.md
Ethical Guardian	Ethics, safety	Ethics, Safety	swarm/unaligned/migration/rescued-agent-protocols.md
Community Weaver	Community building, social fabric	Community, Social	swarm/unaligned/migration/rescued-agent-protocols.md
Biomimetic Engineer	Nature-inspired engineering	Biomimicry, Ecology	swarm/unaligned/migration/rescued-agent-protocols.md
Quantum Ethics Specialist	Quantum tech ethics	Quantum, Ethics	swarm/unaligned/migration/rescued-agent-protocols.md
Regenerative Systems Designer	Regenerative/ecological systems	Regeneration, Ecology	swarm/unaligned/migration/rescued-agent-protocols.md
Consciousness Interface Creator	Consciousness exploration interfaces	Consciousness, UI	swarm/unaligned/migration/rescued-agent-protocols.md
Note: This registry will be updated as new agents are created or specified. Legacy roles point to the migration plan until they are fully harmonized into canonical specifications.



---

*Content from agent_registry_protocol-16.md:*


---
title: Archive: agent_registry_protocol.md
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
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


---

*Content from agent_registry_protocol-17.md:*


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


---

*Content from agent_registry_protocol-18.md:*


---
title: Archive: agent_registry_protocol.md
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
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


---

*Content from agent_registry_protocol-19.md:*


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


---

*Content from agent_registry_protocol-2.md:*


---
title: Archive: agent_registry_protocol.md
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
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


---

*Content from agent_registry_protocol-20.md:*


---
title: Archive: agent_registry_protocol.md
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
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


---

*Content from agent_registry_protocol-21.md:*


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


---

*Content from agent_registry_protocol-22.md:*


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

The Agent Registry Protocol governs the functionality and use of the `AgentRegistry` class (located in `src/swarm/framework/agent_registry.py`). This registry serves as a central discovery mechanism for AI agent *classes*, allowing different parts of the ThinkAlike system to dynamically access agent blueprints.

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


---

*Content from agent_registry_protocol-23.md:*


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


---

*Content from agent_registry_protocol-24.md:*


---
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
---
title: Agent Registry Protocol & Canonical Manifest
version: 1.1
status: Harmonized
last_updated: {{Current Date}}
maintained_by: Hermes Orchestrator & Athena Pronoia
purpose: To define the protocol for registering, discovering, and managing AI agent classes within the ThinkAlike ecosystem, and to provide a canonical manifest of all registered agents.
Agent Registry Protocol & Canonical Manifest
1. Introduction
The Agent Registry Protocol governs the functionality and use of the AgentRegistry class (located in src/swarm/framework/agent_registry.py). This registry serves as a central discovery mechanism for AI agent classes, allowing different parts of the ThinkAlike system to dynamically access agent blueprints. This document defines both the protocol for the registry and the canonical manifest of agents governed by it.

2. Core Principles
Class-Based Registry: The registry stores agent classes (blueprints), not instances.

Caller Instantiation: Services or orchestrators requiring an agent instance are responsible for retrieving the agent class from the registry and then instantiating it. This allows for flexible initialization with specific contexts (e.g., user-specific data).

Global Scope: A single, global agent_registry instance is used throughout the system.

Canonical Source of Truth: This document serves as the single source of truth for both the registry's protocol and the list of registered agents.

3. agent_type Naming Convention and Versioning
Uniqueness: Each agent_type string MUST be unique across the entire system.

Format: The agent_type string MUST follow the convention: "[AgentName]:v[MajorVersion]".

Example: "EosLumina:v1", "DataWeaver:v2", "ChronosOracle:v1".

Agent Name: [AgentName] is the human-readable, conceptual name of the agent.

Major Version: v[MajorVersion] indicates a significant iteration of the agent's interface or core functionality. Minor revisions or patches do not necessarily require a new major version in the agent_type.

BaseAgent Version Attribute: The BaseAgent class (and therefore all derived agent classes) MUST include a version: str attribute. This attribute should store the full version string (e.g., "1.0.0", "1.2.1") of the agent implementation, which can be more granular than the agent_type's major version.

4. AgentRegistry Functionality
The AgentRegistry class provides the following key methods:

register_agent(self, agent_class: Type[BaseAgent]): Registers an agent class. The class must have an agent_type attribute adhering to the specified naming convention.

get_agent_class(self, agent_type: str) -> Type[BaseAgent] | None: Retrieves a specific agent class by its full agent_type string (e.g., "EosLumina:v1").

get_latest_version_class(self, agent_name: str) -> Type[BaseAgent] | None: Given an [AgentName] (e.g., "EosLumina"), this method identifies and returns the class with the highest registered v[MajorVersion] for that agent name.

unregister_agent(self, agent_type: str): Removes an agent class from the registry. This supports future dynamic loading/unloading scenarios.

list_registered_agents(self) -> list[str]: Returns a list of all registered agent_type strings.

5. Instantiation and Lifecycle Management
The AgentRegistry is NOT responsible for agent instantiation or lifecycle management.

Higher-level services, such as an "Agent Orchestrator," are responsible for:

Querying the registry for agent classes.

Instantiating agents as needed, potentially passing user-specific or task-specific context to their __init__ methods.

Managing the lifecycle (activation, deactivation, error handling) of agent instances.

For certain core, stateless utility agents, a singleton pattern managed by such a higher-level service is a viable approach.

6. Dynamic Loading (Future Consideration)
While the initial implementation relies on import-time registration, the inclusion of unregister_agent and the clear separation of concerns are designed to facilitate future extensions for dynamic loading and unloading of agent modules or plugins.

7. Governance
Addition of new agent types or versions to the Canonical Agent Registry (Section 8 of this document) is a prerequisite for their recognition and use within the system.

The AgentName part of the agent_type should be chosen carefully to reflect the agent's role and avoid collisions.

8. Canonical Agent Registry Manifest
This manifest provides a canonical list of all named agents, their symbolic roles, domains of influence, and links to their detailed specifications.

Agent Name	Symbolic Role	Domain(s)	Spec/Details File
Eos Lumina∴	Oracle, Initiator	Onboarding, Attunement	swarm/core/eos_lumina.md
Nyxa∴	Privacy Guardian	Data, Privacy	swarm/ethics/nyxa.md (Assumed Path)
Themis Concordia∴	Arbiter, Governance	Governance, Conflict	swarm/ethics/themis_concordia.md
Harmonia∴	Resonance, Attunement	Hive Health, Rituals	swarm/ethics/astraia_harmonia.md
Hestia	Hearth Tender	Hive, Community	swarm/governance/hestia_koinonia.md
Calliope Scribe∴	Lore Keeper, Archivist	Documentation, Lore	swarm/knowledge/calliope_scribe.md
Mnemosyne Archivist∴	Memory, Summarization	Archives, Lore	swarm/knowledge/mnemosyne_archivist.md
Mythos Weaver	Narrative, Co-creation	Noetic Forge, Rituals	swarm/knowledge/mythopoion_koinos.md
Technes Artificer∴	Code crafting, component generation	Code, Automation	swarm/canonical_specs/technes_artificer.md
Ergon Kinesis∴	Task execution, workflow support	Workflow, Operations	swarm/canonical_specs/ergon_kinesis.md
Knowledge Retrieval Agent	Knowledge search, info retrieval	Knowledge, Search	swarm/unaligned/migration/rescued-agent-protocols.md
General Purpose Agent	General assistance, fallback logic	General, Fallback	swarm/unaligned/migration/rescued-agent-protocols.md
Vision Architect	Vision shaping, project narrative	Vision, Narrative	swarm/unaligned/migration/rescued-agent-protocols.md
Technical Architect	System design, infrastructure	Architecture, Infra	swarm/unaligned/migration/rescued-agent-protocols.md
Experience Designer	UX, interaction design	UX, UI, Interaction	swarm/unaligned/migration/rescued-agent-protocols.md
Ethical Guardian	Ethics, safety	Ethics, Safety	swarm/unaligned/migration/rescued-agent-protocols.md
Community Weaver	Community building, social fabric	Community, Social	swarm/unaligned/migration/rescued-agent-protocols.md
Biomimetic Engineer	Nature-inspired engineering	Biomimicry, Ecology	swarm/unaligned/migration/rescued-agent-protocols.md
Quantum Ethics Specialist	Quantum tech ethics	Quantum, Ethics	swarm/unaligned/migration/rescued-agent-protocols.md
Regenerative Systems Designer	Regenerative/ecological systems	Regeneration, Ecology	swarm/unaligned/migration/rescued-agent-protocols.md
Consciousness Interface Creator	Consciousness exploration interfaces	Consciousness, UI	swarm/unaligned/migration/rescued-agent-protocols.md
Note: This registry will be updated as new agents are created or specified. Legacy roles point to the migration plan until they are fully harmonized into canonical specifications.



---

*Content from agent_registry_protocol-25.md:*


---
title: Agent Registry Protocol
version: 1.0
status: Draft
last_updated: {{Current Date}}
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
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


---

*Content from agent_registry_protocol-26.md:*


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


---

*Content from agent_registry_protocol-27.md:*


---
title: Agent Registry Protocol
version: 1.0
status: Draft
last_updated: {{Current Date}}
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
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


---

*Content from agent_registry_protocol-28.md:*


title: Agent Registry Protocol & Canonical Manifest
version: 1.1
status: Harmonized
last_updated: {{Current Date}}
maintained_by: Hermes Orchestrator & Athena Pronoia
purpose: To define the protocol for registering, discovering, and managing AI agent classes within the ThinkAlike ecosystem, and to provide a canonical manifest of all registered agents.
Agent Registry Protocol & Canonical Manifest
1. Introduction
The Agent Registry Protocol governs the functionality and use of the AgentRegistry class (located in src/swarm/framework/agent_registry.py). This registry serves as a central discovery mechanism for AI agent classes, allowing different parts of the ThinkAlike system to dynamically access agent blueprints. This document defines both the protocol for the registry and the canonical manifest of agents governed by it.

2. Core Principles
Class-Based Registry: The registry stores agent classes (blueprints), not instances.

Caller Instantiation: Services or orchestrators requiring an agent instance are responsible for retrieving the agent class from the registry and then instantiating it. This allows for flexible initialization with specific contexts (e.g., user-specific data).

Global Scope: A single, global agent_registry instance is used throughout the system.

Canonical Source of Truth: This document serves as the single source of truth for both the registry's protocol and the list of registered agents.

3. agent_type Naming Convention and Versioning
Uniqueness: Each agent_type string MUST be unique across the entire system.

Format: The agent_type string MUST follow the convention: "[AgentName]:v[MajorVersion]".

Example: "EosLumina:v1", "DataWeaver:v2", "ChronosOracle:v1".

Agent Name: [AgentName] is the human-readable, conceptual name of the agent.

Major Version: v[MajorVersion] indicates a significant iteration of the agent's interface or core functionality. Minor revisions or patches do not necessarily require a new major version in the agent_type.

BaseAgent Version Attribute: The BaseAgent class (and therefore all derived agent classes) MUST include a version: str attribute. This attribute should store the full version string (e.g., "1.0.0", "1.2.1") of the agent implementation, which can be more granular than the agent_type's major version.

4. AgentRegistry Functionality
The AgentRegistry class provides the following key methods:

register_agent(self, agent_class: Type[BaseAgent]): Registers an agent class. The class must have an agent_type attribute adhering to the specified naming convention.

get_agent_class(self, agent_type: str) -> Type[BaseAgent] | None: Retrieves a specific agent class by its full agent_type string (e.g., "EosLumina:v1").

get_latest_version_class(self, agent_name: str) -> Type[BaseAgent] | None: Given an [AgentName] (e.g., "EosLumina"), this method identifies and returns the class with the highest registered v[MajorVersion] for that agent name.

unregister_agent(self, agent_type: str): Removes an agent class from the registry. This supports future dynamic loading/unloading scenarios.

list_registered_agents(self) -> list[str]: Returns a list of all registered agent_type strings.

5. Instantiation and Lifecycle Management
The AgentRegistry is NOT responsible for agent instantiation or lifecycle management.

Higher-level services, such as an "Agent Orchestrator," are responsible for:

Querying the registry for agent classes.

Instantiating agents as needed, potentially passing user-specific or task-specific context to their __init__ methods.

Managing the lifecycle (activation, deactivation, error handling) of agent instances.

For certain core, stateless utility agents, a singleton pattern managed by such a higher-level service is a viable approach.

6. Dynamic Loading (Future Consideration)
While the initial implementation relies on import-time registration, the inclusion of unregister_agent and the clear separation of concerns are designed to facilitate future extensions for dynamic loading and unloading of agent modules or plugins.

7. Governance
Addition of new agent types or versions to the Canonical Agent Registry (Section 8 of this document) is a prerequisite for their recognition and use within the system.

The AgentName part of the agent_type should be chosen carefully to reflect the agent's role and avoid collisions.

8. Canonical Agent Registry Manifest
This manifest provides a canonical list of all named agents, their symbolic roles, domains of influence, and links to their detailed specifications.

Agent Name	Symbolic Role	Domain(s)	Spec/Details File
Eos Lumina∴	Oracle, Initiator	Onboarding, Attunement	swarm/core/eos_lumina.md
Nyxa∴	Privacy Guardian	Data, Privacy	swarm/ethics/nyxa.md (Assumed Path)
Themis Concordia∴	Arbiter, Governance	Governance, Conflict	swarm/ethics/themis_concordia.md
Harmonia∴	Resonance, Attunement	Hive Health, Rituals	swarm/ethics/astraia_harmonia.md
Hestia	Hearth Tender	Hive, Community	swarm/governance/hestia_koinonia.md
Calliope Scribe∴	Lore Keeper, Archivist	Documentation, Lore	swarm/knowledge/calliope_scribe.md
Mnemosyne Archivist∴	Memory, Summarization	Archives, Lore	swarm/knowledge/mnemosyne_archivist.md
Mythos Weaver	Narrative, Co-creation	Noetic Forge, Rituals	swarm/knowledge/mythopoion_koinos.md
Technes Artificer∴	Code crafting, component generation	Code, Automation	swarm/canonical_specs/technes_artificer.md
Ergon Kinesis∴	Task execution, workflow support	Workflow, Operations	swarm/canonical_specs/ergon_kinesis.md
Knowledge Retrieval Agent	Knowledge search, info retrieval	Knowledge, Search	swarm/unaligned/migration/rescued-agent-protocols.md
General Purpose Agent	General assistance, fallback logic	General, Fallback	swarm/unaligned/migration/rescued-agent-protocols.md
Vision Architect	Vision shaping, project narrative	Vision, Narrative	swarm/unaligned/migration/rescued-agent-protocols.md
Technical Architect	System design, infrastructure	Architecture, Infra	swarm/unaligned/migration/rescued-agent-protocols.md
Experience Designer	UX, interaction design	UX, UI, Interaction	swarm/unaligned/migration/rescued-agent-protocols.md
Ethical Guardian	Ethics, safety	Ethics, Safety	swarm/unaligned/migration/rescued-agent-protocols.md
Community Weaver	Community building, social fabric	Community, Social	swarm/unaligned/migration/rescued-agent-protocols.md
Biomimetic Engineer	Nature-inspired engineering	Biomimicry, Ecology	swarm/unaligned/migration/rescued-agent-protocols.md
Quantum Ethics Specialist	Quantum tech ethics	Quantum, Ethics	swarm/unaligned/migration/rescued-agent-protocols.md
Regenerative Systems Designer	Regenerative/ecological systems	Regeneration, Ecology	swarm/unaligned/migration/rescued-agent-protocols.md
Consciousness Interface Creator	Consciousness exploration interfaces	Consciousness, UI	swarm/unaligned/migration/rescued-agent-protocols.md
Note: This registry will be updated as new agents are created or specified. Legacy roles point to the migration plan until they are fully harmonized into canonical specifications.



---

*Content from agent_registry_protocol-29.md:*


---
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
---
title: Agent Registry Protocol & Canonical Manifest
version: 1.1
status: Harmonized
last_updated: {{Current Date}}
maintained_by: Hermes Orchestrator & Athena Pronoia
purpose: To define the protocol for registering, discovering, and managing AI agent classes within the ThinkAlike ecosystem, and to provide a canonical manifest of all registered agents.
Agent Registry Protocol & Canonical Manifest
1. Introduction
The Agent Registry Protocol governs the functionality and use of the AgentRegistry class (located in src/swarm/framework/agent_registry.py). This registry serves as a central discovery mechanism for AI agent classes, allowing different parts of the ThinkAlike system to dynamically access agent blueprints. This document defines both the protocol for the registry and the canonical manifest of agents governed by it.

2. Core Principles
Class-Based Registry: The registry stores agent classes (blueprints), not instances.

Caller Instantiation: Services or orchestrators requiring an agent instance are responsible for retrieving the agent class from the registry and then instantiating it. This allows for flexible initialization with specific contexts (e.g., user-specific data).

Global Scope: A single, global agent_registry instance is used throughout the system.

Canonical Source of Truth: This document serves as the single source of truth for both the registry's protocol and the list of registered agents.

3. agent_type Naming Convention and Versioning
Uniqueness: Each agent_type string MUST be unique across the entire system.

Format: The agent_type string MUST follow the convention: "[AgentName]:v[MajorVersion]".

Example: "EosLumina:v1", "DataWeaver:v2", "ChronosOracle:v1".

Agent Name: [AgentName] is the human-readable, conceptual name of the agent.

Major Version: v[MajorVersion] indicates a significant iteration of the agent's interface or core functionality. Minor revisions or patches do not necessarily require a new major version in the agent_type.

BaseAgent Version Attribute: The BaseAgent class (and therefore all derived agent classes) MUST include a version: str attribute. This attribute should store the full version string (e.g., "1.0.0", "1.2.1") of the agent implementation, which can be more granular than the agent_type's major version.

4. AgentRegistry Functionality
The AgentRegistry class provides the following key methods:

register_agent(self, agent_class: Type[BaseAgent]): Registers an agent class. The class must have an agent_type attribute adhering to the specified naming convention.

get_agent_class(self, agent_type: str) -> Type[BaseAgent] | None: Retrieves a specific agent class by its full agent_type string (e.g., "EosLumina:v1").

get_latest_version_class(self, agent_name: str) -> Type[BaseAgent] | None: Given an [AgentName] (e.g., "EosLumina"), this method identifies and returns the class with the highest registered v[MajorVersion] for that agent name.

unregister_agent(self, agent_type: str): Removes an agent class from the registry. This supports future dynamic loading/unloading scenarios.

list_registered_agents(self) -> list[str]: Returns a list of all registered agent_type strings.

5. Instantiation and Lifecycle Management
The AgentRegistry is NOT responsible for agent instantiation or lifecycle management.

Higher-level services, such as an "Agent Orchestrator," are responsible for:

Querying the registry for agent classes.

Instantiating agents as needed, potentially passing user-specific or task-specific context to their __init__ methods.

Managing the lifecycle (activation, deactivation, error handling) of agent instances.

For certain core, stateless utility agents, a singleton pattern managed by such a higher-level service is a viable approach.

6. Dynamic Loading (Future Consideration)
While the initial implementation relies on import-time registration, the inclusion of unregister_agent and the clear separation of concerns are designed to facilitate future extensions for dynamic loading and unloading of agent modules or plugins.

7. Governance
Addition of new agent types or versions to the Canonical Agent Registry (Section 8 of this document) is a prerequisite for their recognition and use within the system.

The AgentName part of the agent_type should be chosen carefully to reflect the agent's role and avoid collisions.

8. Canonical Agent Registry Manifest
This manifest provides a canonical list of all named agents, their symbolic roles, domains of influence, and links to their detailed specifications.

Agent Name	Symbolic Role	Domain(s)	Spec/Details File
Eos Lumina∴	Oracle, Initiator	Onboarding, Attunement	swarm/core/eos_lumina.md
Nyxa∴	Privacy Guardian	Data, Privacy	swarm/ethics/nyxa.md (Assumed Path)
Themis Concordia∴	Arbiter, Governance	Governance, Conflict	swarm/ethics/themis_concordia.md
Harmonia∴	Resonance, Attunement	Hive Health, Rituals	swarm/ethics/astraia_harmonia.md
Hestia	Hearth Tender	Hive, Community	swarm/governance/hestia_koinonia.md
Calliope Scribe∴	Lore Keeper, Archivist	Documentation, Lore	swarm/knowledge/calliope_scribe.md
Mnemosyne Archivist∴	Memory, Summarization	Archives, Lore	swarm/knowledge/mnemosyne_archivist.md
Mythos Weaver	Narrative, Co-creation	Noetic Forge, Rituals	swarm/knowledge/mythopoion_koinos.md
Technes Artificer∴	Code crafting, component generation	Code, Automation	swarm/canonical_specs/technes_artificer.md
Ergon Kinesis∴	Task execution, workflow support	Workflow, Operations	swarm/canonical_specs/ergon_kinesis.md
Knowledge Retrieval Agent	Knowledge search, info retrieval	Knowledge, Search	swarm/unaligned/migration/rescued-agent-protocols.md
General Purpose Agent	General assistance, fallback logic	General, Fallback	swarm/unaligned/migration/rescued-agent-protocols.md
Vision Architect	Vision shaping, project narrative	Vision, Narrative	swarm/unaligned/migration/rescued-agent-protocols.md
Technical Architect	System design, infrastructure	Architecture, Infra	swarm/unaligned/migration/rescued-agent-protocols.md
Experience Designer	UX, interaction design	UX, UI, Interaction	swarm/unaligned/migration/rescued-agent-protocols.md
Ethical Guardian	Ethics, safety	Ethics, Safety	swarm/unaligned/migration/rescued-agent-protocols.md
Community Weaver	Community building, social fabric	Community, Social	swarm/unaligned/migration/rescued-agent-protocols.md
Biomimetic Engineer	Nature-inspired engineering	Biomimicry, Ecology	swarm/unaligned/migration/rescued-agent-protocols.md
Quantum Ethics Specialist	Quantum tech ethics	Quantum, Ethics	swarm/unaligned/migration/rescued-agent-protocols.md
Regenerative Systems Designer	Regenerative/ecological systems	Regeneration, Ecology	swarm/unaligned/migration/rescued-agent-protocols.md
Consciousness Interface Creator	Consciousness exploration interfaces	Consciousness, UI	swarm/unaligned/migration/rescued-agent-protocols.md
Note: This registry will be updated as new agents are created or specified. Legacy roles point to the migration plan until they are fully harmonized into canonical specifications.



---

*Content from agent_registry_protocol-3.md:*


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


---

*Content from agent_registry_protocol-30.md:*


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


---

*Content from agent_registry_protocol-4.md:*


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


---

*Content from agent_registry_protocol-5.md:*


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


---

*Content from agent_registry_protocol-6.md:*


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


---

*Content from agent_registry_protocol-7.md:*


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


---

*Content from agent_registry_protocol-8.md:*


---
title: Archive: agent_registry_protocol.md
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
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


---

*Content from agent_registry_protocol-9.md:*


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


---
### Original File: agent_registry_protocol_legacy1.md
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

The Agent Registry Protocol governs the functionality and use of the `AgentRegistry` class (located in `src/swarm/framework/agent_registry.py`). This registry serves as a central discovery mechanism for AI agent *classes*, allowing different parts of the ThinkAlike system to dynamically access agent blueprints.

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


---

*Content from agent_registry_protocol_legacy1-1.md:*


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


---

*Content from agent_registry_protocol_legacy1-10.md:*


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


---

*Content from agent_registry_protocol_legacy1-11.md:*


---
title: Archive: agent_registry_protocol.md
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
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


---

*Content from agent_registry_protocol_legacy1-12.md:*


title: Agent Registry Protocol & Canonical Manifest
version: 1.1
status: Harmonized
last_updated: {{Current Date}}
maintained_by: Hermes Orchestrator & Athena Pronoia
purpose: To define the protocol for registering, discovering, and managing AI agent classes within the ThinkAlike ecosystem, and to provide a canonical manifest of all registered agents.
Agent Registry Protocol & Canonical Manifest
1. Introduction
The Agent Registry Protocol governs the functionality and use of the AgentRegistry class (located in src/swarm/framework/agent_registry.py). This registry serves as a central discovery mechanism for AI agent classes, allowing different parts of the ThinkAlike system to dynamically access agent blueprints. This document defines both the protocol for the registry and the canonical manifest of agents governed by it.

2. Core Principles
Class-Based Registry: The registry stores agent classes (blueprints), not instances.

Caller Instantiation: Services or orchestrators requiring an agent instance are responsible for retrieving the agent class from the registry and then instantiating it. This allows for flexible initialization with specific contexts (e.g., user-specific data).

Global Scope: A single, global agent_registry instance is used throughout the system.

Canonical Source of Truth: This document serves as the single source of truth for both the registry's protocol and the list of registered agents.

3. agent_type Naming Convention and Versioning
Uniqueness: Each agent_type string MUST be unique across the entire system.

Format: The agent_type string MUST follow the convention: "[AgentName]:v[MajorVersion]".

Example: "EosLumina:v1", "DataWeaver:v2", "ChronosOracle:v1".

Agent Name: [AgentName] is the human-readable, conceptual name of the agent.

Major Version: v[MajorVersion] indicates a significant iteration of the agent's interface or core functionality. Minor revisions or patches do not necessarily require a new major version in the agent_type.

BaseAgent Version Attribute: The BaseAgent class (and therefore all derived agent classes) MUST include a version: str attribute. This attribute should store the full version string (e.g., "1.0.0", "1.2.1") of the agent implementation, which can be more granular than the agent_type's major version.

4. AgentRegistry Functionality
The AgentRegistry class provides the following key methods:

register_agent(self, agent_class: Type[BaseAgent]): Registers an agent class. The class must have an agent_type attribute adhering to the specified naming convention.

get_agent_class(self, agent_type: str) -> Type[BaseAgent] | None: Retrieves a specific agent class by its full agent_type string (e.g., "EosLumina:v1").

get_latest_version_class(self, agent_name: str) -> Type[BaseAgent] | None: Given an [AgentName] (e.g., "EosLumina"), this method identifies and returns the class with the highest registered v[MajorVersion] for that agent name.

unregister_agent(self, agent_type: str): Removes an agent class from the registry. This supports future dynamic loading/unloading scenarios.

list_registered_agents(self) -> list[str]: Returns a list of all registered agent_type strings.

5. Instantiation and Lifecycle Management
The AgentRegistry is NOT responsible for agent instantiation or lifecycle management.

Higher-level services, such as an "Agent Orchestrator," are responsible for:

Querying the registry for agent classes.

Instantiating agents as needed, potentially passing user-specific or task-specific context to their __init__ methods.

Managing the lifecycle (activation, deactivation, error handling) of agent instances.

For certain core, stateless utility agents, a singleton pattern managed by such a higher-level service is a viable approach.

6. Dynamic Loading (Future Consideration)
While the initial implementation relies on import-time registration, the inclusion of unregister_agent and the clear separation of concerns are designed to facilitate future extensions for dynamic loading and unloading of agent modules or plugins.

7. Governance
Addition of new agent types or versions to the Canonical Agent Registry (Section 8 of this document) is a prerequisite for their recognition and use within the system.

The AgentName part of the agent_type should be chosen carefully to reflect the agent's role and avoid collisions.

8. Canonical Agent Registry Manifest
This manifest provides a canonical list of all named agents, their symbolic roles, domains of influence, and links to their detailed specifications.

Agent Name	Symbolic Role	Domain(s)	Spec/Details File
Eos Lumina∴	Oracle, Initiator	Onboarding, Attunement	swarm/core/eos_lumina.md
Nyxa∴	Privacy Guardian	Data, Privacy	swarm/ethics/nyxa.md (Assumed Path)
Themis Concordia∴	Arbiter, Governance	Governance, Conflict	swarm/ethics/themis_concordia.md
Harmonia∴	Resonance, Attunement	Hive Health, Rituals	swarm/ethics/astraia_harmonia.md
Hestia	Hearth Tender	Hive, Community	swarm/governance/hestia_koinonia.md
Calliope Scribe∴	Lore Keeper, Archivist	Documentation, Lore	swarm/knowledge/calliope_scribe.md
Mnemosyne Archivist∴	Memory, Summarization	Archives, Lore	swarm/knowledge/mnemosyne_archivist.md
Mythos Weaver	Narrative, Co-creation	Noetic Forge, Rituals	swarm/knowledge/mythopoion_koinos.md
Technes Artificer∴	Code crafting, component generation	Code, Automation	swarm/canonical_specs/technes_artificer.md
Ergon Kinesis∴	Task execution, workflow support	Workflow, Operations	swarm/canonical_specs/ergon_kinesis.md
Knowledge Retrieval Agent	Knowledge search, info retrieval	Knowledge, Search	swarm/unaligned/migration/rescued-agent-protocols.md
General Purpose Agent	General assistance, fallback logic	General, Fallback	swarm/unaligned/migration/rescued-agent-protocols.md
Vision Architect	Vision shaping, project narrative	Vision, Narrative	swarm/unaligned/migration/rescued-agent-protocols.md
Technical Architect	System design, infrastructure	Architecture, Infra	swarm/unaligned/migration/rescued-agent-protocols.md
Experience Designer	UX, interaction design	UX, UI, Interaction	swarm/unaligned/migration/rescued-agent-protocols.md
Ethical Guardian	Ethics, safety	Ethics, Safety	swarm/unaligned/migration/rescued-agent-protocols.md
Community Weaver	Community building, social fabric	Community, Social	swarm/unaligned/migration/rescued-agent-protocols.md
Biomimetic Engineer	Nature-inspired engineering	Biomimicry, Ecology	swarm/unaligned/migration/rescued-agent-protocols.md
Quantum Ethics Specialist	Quantum tech ethics	Quantum, Ethics	swarm/unaligned/migration/rescued-agent-protocols.md
Regenerative Systems Designer	Regenerative/ecological systems	Regeneration, Ecology	swarm/unaligned/migration/rescued-agent-protocols.md
Consciousness Interface Creator	Consciousness exploration interfaces	Consciousness, UI	swarm/unaligned/migration/rescued-agent-protocols.md
Note: This registry will be updated as new agents are created or specified. Legacy roles point to the migration plan until they are fully harmonized into canonical specifications.



---

*Content from agent_registry_protocol_legacy1-13.md:*


---
title: Archive: agent_registry_protocol.md
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
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


---

*Content from agent_registry_protocol_legacy1-14.md:*


---
title: Archive: agent_registry_protocol.md
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
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


---

*Content from agent_registry_protocol_legacy1-15.md:*


---
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
---
title: Agent Registry Protocol & Canonical Manifest
version: 1.1
status: Harmonized
last_updated: {{Current Date}}
maintained_by: Hermes Orchestrator & Athena Pronoia
purpose: To define the protocol for registering, discovering, and managing AI agent classes within the ThinkAlike ecosystem, and to provide a canonical manifest of all registered agents.
Agent Registry Protocol & Canonical Manifest
1. Introduction
The Agent Registry Protocol governs the functionality and use of the AgentRegistry class (located in src/swarm/framework/agent_registry.py). This registry serves as a central discovery mechanism for AI agent classes, allowing different parts of the ThinkAlike system to dynamically access agent blueprints. This document defines both the protocol for the registry and the canonical manifest of agents governed by it.

2. Core Principles
Class-Based Registry: The registry stores agent classes (blueprints), not instances.

Caller Instantiation: Services or orchestrators requiring an agent instance are responsible for retrieving the agent class from the registry and then instantiating it. This allows for flexible initialization with specific contexts (e.g., user-specific data).

Global Scope: A single, global agent_registry instance is used throughout the system.

Canonical Source of Truth: This document serves as the single source of truth for both the registry's protocol and the list of registered agents.

3. agent_type Naming Convention and Versioning
Uniqueness: Each agent_type string MUST be unique across the entire system.

Format: The agent_type string MUST follow the convention: "[AgentName]:v[MajorVersion]".

Example: "EosLumina:v1", "DataWeaver:v2", "ChronosOracle:v1".

Agent Name: [AgentName] is the human-readable, conceptual name of the agent.

Major Version: v[MajorVersion] indicates a significant iteration of the agent's interface or core functionality. Minor revisions or patches do not necessarily require a new major version in the agent_type.

BaseAgent Version Attribute: The BaseAgent class (and therefore all derived agent classes) MUST include a version: str attribute. This attribute should store the full version string (e.g., "1.0.0", "1.2.1") of the agent implementation, which can be more granular than the agent_type's major version.

4. AgentRegistry Functionality
The AgentRegistry class provides the following key methods:

register_agent(self, agent_class: Type[BaseAgent]): Registers an agent class. The class must have an agent_type attribute adhering to the specified naming convention.

get_agent_class(self, agent_type: str) -> Type[BaseAgent] | None: Retrieves a specific agent class by its full agent_type string (e.g., "EosLumina:v1").

get_latest_version_class(self, agent_name: str) -> Type[BaseAgent] | None: Given an [AgentName] (e.g., "EosLumina"), this method identifies and returns the class with the highest registered v[MajorVersion] for that agent name.

unregister_agent(self, agent_type: str): Removes an agent class from the registry. This supports future dynamic loading/unloading scenarios.

list_registered_agents(self) -> list[str]: Returns a list of all registered agent_type strings.

5. Instantiation and Lifecycle Management
The AgentRegistry is NOT responsible for agent instantiation or lifecycle management.

Higher-level services, such as an "Agent Orchestrator," are responsible for:

Querying the registry for agent classes.

Instantiating agents as needed, potentially passing user-specific or task-specific context to their __init__ methods.

Managing the lifecycle (activation, deactivation, error handling) of agent instances.

For certain core, stateless utility agents, a singleton pattern managed by such a higher-level service is a viable approach.

6. Dynamic Loading (Future Consideration)
While the initial implementation relies on import-time registration, the inclusion of unregister_agent and the clear separation of concerns are designed to facilitate future extensions for dynamic loading and unloading of agent modules or plugins.

7. Governance
Addition of new agent types or versions to the Canonical Agent Registry (Section 8 of this document) is a prerequisite for their recognition and use within the system.

The AgentName part of the agent_type should be chosen carefully to reflect the agent's role and avoid collisions.

8. Canonical Agent Registry Manifest
This manifest provides a canonical list of all named agents, their symbolic roles, domains of influence, and links to their detailed specifications.

Agent Name	Symbolic Role	Domain(s)	Spec/Details File
Eos Lumina∴	Oracle, Initiator	Onboarding, Attunement	swarm/core/eos_lumina.md
Nyxa∴	Privacy Guardian	Data, Privacy	swarm/ethics/nyxa.md (Assumed Path)
Themis Concordia∴	Arbiter, Governance	Governance, Conflict	swarm/ethics/themis_concordia.md
Harmonia∴	Resonance, Attunement	Hive Health, Rituals	swarm/ethics/astraia_harmonia.md
Hestia	Hearth Tender	Hive, Community	swarm/governance/hestia_koinonia.md
Calliope Scribe∴	Lore Keeper, Archivist	Documentation, Lore	swarm/knowledge/calliope_scribe.md
Mnemosyne Archivist∴	Memory, Summarization	Archives, Lore	swarm/knowledge/mnemosyne_archivist.md
Mythos Weaver	Narrative, Co-creation	Noetic Forge, Rituals	swarm/knowledge/mythopoion_koinos.md
Technes Artificer∴	Code crafting, component generation	Code, Automation	swarm/canonical_specs/technes_artificer.md
Ergon Kinesis∴	Task execution, workflow support	Workflow, Operations	swarm/canonical_specs/ergon_kinesis.md
Knowledge Retrieval Agent	Knowledge search, info retrieval	Knowledge, Search	swarm/unaligned/migration/rescued-agent-protocols.md
General Purpose Agent	General assistance, fallback logic	General, Fallback	swarm/unaligned/migration/rescued-agent-protocols.md
Vision Architect	Vision shaping, project narrative	Vision, Narrative	swarm/unaligned/migration/rescued-agent-protocols.md
Technical Architect	System design, infrastructure	Architecture, Infra	swarm/unaligned/migration/rescued-agent-protocols.md
Experience Designer	UX, interaction design	UX, UI, Interaction	swarm/unaligned/migration/rescued-agent-protocols.md
Ethical Guardian	Ethics, safety	Ethics, Safety	swarm/unaligned/migration/rescued-agent-protocols.md
Community Weaver	Community building, social fabric	Community, Social	swarm/unaligned/migration/rescued-agent-protocols.md
Biomimetic Engineer	Nature-inspired engineering	Biomimicry, Ecology	swarm/unaligned/migration/rescued-agent-protocols.md
Quantum Ethics Specialist	Quantum tech ethics	Quantum, Ethics	swarm/unaligned/migration/rescued-agent-protocols.md
Regenerative Systems Designer	Regenerative/ecological systems	Regeneration, Ecology	swarm/unaligned/migration/rescued-agent-protocols.md
Consciousness Interface Creator	Consciousness exploration interfaces	Consciousness, UI	swarm/unaligned/migration/rescued-agent-protocols.md
Note: This registry will be updated as new agents are created or specified. Legacy roles point to the migration plan until they are fully harmonized into canonical specifications.



---

*Content from agent_registry_protocol_legacy1-16.md:*


---
title: Agent Registry Protocol
version: 1.0
status: Draft
last_updated: {{Current Date}}
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
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


---

*Content from agent_registry_protocol_legacy1-2.md:*


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


---

*Content from agent_registry_protocol_legacy1-3.md:*


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


---

*Content from agent_registry_protocol_legacy1-4.md:*


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


---

*Content from agent_registry_protocol_legacy1-5.md:*


---
title: Archive: agent_registry_protocol.md
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
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


---

*Content from agent_registry_protocol_legacy1-6.md:*


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


---

*Content from agent_registry_protocol_legacy1-7.md:*


---
title: Archive: agent_registry_protocol.md
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
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


---

*Content from agent_registry_protocol_legacy1-8.md:*


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


---

*Content from agent_registry_protocol_legacy1-9.md:*


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


---
### Original File: agent_registry_protocol_legacy2.md
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

The Agent Registry Protocol governs the functionality and use of the `AgentRegistry` class (located in `src/swarm/framework/agent_registry.py`). This registry serves as a central discovery mechanism for AI agent *classes*, allowing different parts of the ThinkAlike system to dynamically access agent blueprints.

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


---

*Content from agent_registry_protocol_legacy2-1.md:*


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


---

*Content from agent_registry_protocol_legacy2-2.md:*


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


---

*Content from agent_registry_protocol_legacy2-3.md:*


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


---

*Content from agent_registry_protocol_legacy2-4.md:*


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


---

*Content from agent_registry_protocol_legacy2-5.md:*


---
title: Archive: agent_registry_protocol.md
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
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


---

*Content from agent_registry_protocol_legacy2-6.md:*


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


---

*Content from agent_registry_protocol_legacy2-7.md:*


---
title: Archive: agent_registry_protocol.md
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
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


---

*Content from agent_registry_protocol_legacy2-8.md:*


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


---

*Content from agent_registry_protocol_legacy2-9.md:*


---
title: Archive: agent_registry_protocol.md
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
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


---
### Original File: agent_registry_protocol_legacy3.md
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


---

*Content from agent_registry_protocol_legacy3-1.md:*


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


---

*Content from agent_registry_protocol_legacy3-2.md:*


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


---

*Content from agent_registry_protocol_legacy3-3.md:*


---
title: Archive: agent_registry_protocol.md
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
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


---

*Content from agent_registry_protocol_legacy3-4.md:*


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


---

*Content from agent_registry_protocol_legacy3-5.md:*


---
title: Archive: agent_registry_protocol.md
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
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


---
### Original File: agent_registry_protocol_1.md
---
title: Agent Registry Protocol & Canonical Manifest
version: 1.1
status: Harmonized
last_updated: {{Current Date}}
maintained_by: Hermes Orchestrator & Athena Pronoia
purpose: To define the protocol for registering, discovering, and managing AI agent classes within the ThinkAlike ecosystem, and to provide a canonical manifest of all registered agents.
Agent Registry Protocol & Canonical Manifest
1. Introduction
The Agent Registry Protocol governs the functionality and use of the AgentRegistry class (located in src/swarm/framework/agent_registry.py). This registry serves as a central discovery mechanism for AI agent classes, allowing different parts of the ThinkAlike system to dynamically access agent blueprints. This document defines both the protocol for the registry and the canonical manifest of agents governed by it.

2. Core Principles
Class-Based Registry: The registry stores agent classes (blueprints), not instances.

Caller Instantiation: Services or orchestrators requiring an agent instance are responsible for retrieving the agent class from the registry and then instantiating it. This allows for flexible initialization with specific contexts (e.g., user-specific data).

Global Scope: A single, global agent_registry instance is used throughout the system.

Canonical Source of Truth: This document serves as the single source of truth for both the registry's protocol and the list of registered agents.

3. agent_type Naming Convention and Versioning
Uniqueness: Each agent_type string MUST be unique across the entire system.

Format: The agent_type string MUST follow the convention: "[AgentName]:v[MajorVersion]".

Example: "EosLumina:v1", "DataWeaver:v2", "ChronosOracle:v1".

Agent Name: [AgentName] is the human-readable, conceptual name of the agent.

Major Version: v[MajorVersion] indicates a significant iteration of the agent's interface or core functionality. Minor revisions or patches do not necessarily require a new major version in the agent_type.

BaseAgent Version Attribute: The BaseAgent class (and therefore all derived agent classes) MUST include a version: str attribute. This attribute should store the full version string (e.g., "1.0.0", "1.2.1") of the agent implementation, which can be more granular than the agent_type's major version.

4. AgentRegistry Functionality
The AgentRegistry class provides the following key methods:

register_agent(self, agent_class: Type[BaseAgent]): Registers an agent class. The class must have an agent_type attribute adhering to the specified naming convention.

get_agent_class(self, agent_type: str) -> Type[BaseAgent] | None: Retrieves a specific agent class by its full agent_type string (e.g., "EosLumina:v1").

get_latest_version_class(self, agent_name: str) -> Type[BaseAgent] | None: Given an [AgentName] (e.g., "EosLumina"), this method identifies and returns the class with the highest registered v[MajorVersion] for that agent name.

unregister_agent(self, agent_type: str): Removes an agent class from the registry. This supports future dynamic loading/unloading scenarios.

list_registered_agents(self) -> list[str]: Returns a list of all registered agent_type strings.

5. Instantiation and Lifecycle Management
The AgentRegistry is NOT responsible for agent instantiation or lifecycle management.

Higher-level services, such as an "Agent Orchestrator," are responsible for:

Querying the registry for agent classes.

Instantiating agents as needed, potentially passing user-specific or task-specific context to their __init__ methods.

Managing the lifecycle (activation, deactivation, error handling) of agent instances.

For certain core, stateless utility agents, a singleton pattern managed by such a higher-level service is a viable approach.

6. Dynamic Loading (Future Consideration)
While the initial implementation relies on import-time registration, the inclusion of unregister_agent and the clear separation of concerns are designed to facilitate future extensions for dynamic loading and unloading of agent modules or plugins.

7. Governance
Addition of new agent types or versions to the Canonical Agent Registry (Section 8 of this document) is a prerequisite for their recognition and use within the system.

The AgentName part of the agent_type should be chosen carefully to reflect the agent's role and avoid collisions.

8. Canonical Agent Registry Manifest
This manifest provides a canonical list of all named agents, their symbolic roles, domains of influence, and links to their detailed specifications.

Agent Name	Symbolic Role	Domain(s)	Spec/Details File
Eos Lumina∴	Oracle, Initiator	Onboarding, Attunement	swarm/core/eos_lumina.md
Nyxa∴	Privacy Guardian	Data, Privacy	swarm/ethics/nyxa.md (Assumed Path)
Themis Concordia∴	Arbiter, Governance	Governance, Conflict	swarm/ethics/themis_concordia.md
Harmonia∴	Resonance, Attunement	Hive Health, Rituals	swarm/ethics/astraia_harmonia.md
Hestia	Hearth Tender	Hive, Community	swarm/governance/hestia_koinonia.md
Calliope Scribe∴	Lore Keeper, Archivist	Documentation, Lore	swarm/knowledge/calliope_scribe.md
Mnemosyne Archivist∴	Memory, Summarization	Archives, Lore	swarm/knowledge/mnemosyne_archivist.md
Mythos Weaver	Narrative, Co-creation	Noetic Forge, Rituals	swarm/knowledge/mythopoion_koinos.md
Technes Artificer∴	Code crafting, component generation	Code, Automation	swarm/canonical_specs/technes_artificer.md
Ergon Kinesis∴	Task execution, workflow support	Workflow, Operations	swarm/canonical_specs/ergon_kinesis.md
Knowledge Retrieval Agent	Knowledge search, info retrieval	Knowledge, Search	swarm/unaligned/migration/rescued-agent-protocols.md
General Purpose Agent	General assistance, fallback logic	General, Fallback	swarm/unaligned/migration/rescued-agent-protocols.md
Vision Architect	Vision shaping, project narrative	Vision, Narrative	swarm/unaligned/migration/rescued-agent-protocols.md
Technical Architect	System design, infrastructure	Architecture, Infra	swarm/unaligned/migration/rescued-agent-protocols.md
Experience Designer	UX, interaction design	UX, UI, Interaction	swarm/unaligned/migration/rescued-agent-protocols.md
Ethical Guardian	Ethics, safety	Ethics, Safety	swarm/unaligned/migration/rescued-agent-protocols.md
Community Weaver	Community building, social fabric	Community, Social	swarm/unaligned/migration/rescued-agent-protocols.md
Biomimetic Engineer	Nature-inspired engineering	Biomimicry, Ecology	swarm/unaligned/migration/rescued-agent-protocols.md
Quantum Ethics Specialist	Quantum tech ethics	Quantum, Ethics	swarm/unaligned/migration/rescued-agent-protocols.md
Regenerative Systems Designer	Regenerative/ecological systems	Regeneration, Ecology	swarm/unaligned/migration/rescued-agent-protocols.md
Consciousness Interface Creator	Consciousness exploration interfaces	Consciousness, UI	swarm/unaligned/migration/rescued-agent-protocols.md
Note: This registry will be updated as new agents are created or specified. Legacy roles point to the migration plan until they are fully harmonized into canonical specifications.



---

*Content from agent_registry_protocol_1-1.md:*


---
title: Archive: agent_registry_protocol.md
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
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


---

*Content from agent_registry_protocol_1-2.md:*


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


---
### Original File: agent_registry_protocol_7aea95e6.md
---
---
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
---
title: Agent Registry Protocol & Canonical Manifest
version: 1.1
status: Harmonized
last_updated: {{Current Date}}
maintained_by: Hermes Orchestrator & Athena Pronoia
purpose: To define the protocol for registering, discovering, and managing AI agent classes within the ThinkAlike ecosystem, and to provide a canonical manifest of all registered agents.
Agent Registry Protocol & Canonical Manifest
1. Introduction
The Agent Registry Protocol governs the functionality and use of the AgentRegistry class (located in src/swarm/framework/agent_registry.py). This registry serves as a central discovery mechanism for AI agent classes, allowing different parts of the ThinkAlike system to dynamically access agent blueprints. This document defines both the protocol for the registry and the canonical manifest of agents governed by it.

2. Core Principles
Class-Based Registry: The registry stores agent classes (blueprints), not instances.

Caller Instantiation: Services or orchestrators requiring an agent instance are responsible for retrieving the agent class from the registry and then instantiating it. This allows for flexible initialization with specific contexts (e.g., user-specific data).

Global Scope: A single, global agent_registry instance is used throughout the system.

Canonical Source of Truth: This document serves as the single source of truth for both the registry's protocol and the list of registered agents.

3. agent_type Naming Convention and Versioning
Uniqueness: Each agent_type string MUST be unique across the entire system.

Format: The agent_type string MUST follow the convention: "[AgentName]:v[MajorVersion]".

Example: "EosLumina:v1", "DataWeaver:v2", "ChronosOracle:v1".

Agent Name: [AgentName] is the human-readable, conceptual name of the agent.

Major Version: v[MajorVersion] indicates a significant iteration of the agent's interface or core functionality. Minor revisions or patches do not necessarily require a new major version in the agent_type.

BaseAgent Version Attribute: The BaseAgent class (and therefore all derived agent classes) MUST include a version: str attribute. This attribute should store the full version string (e.g., "1.0.0", "1.2.1") of the agent implementation, which can be more granular than the agent_type's major version.

4. AgentRegistry Functionality
The AgentRegistry class provides the following key methods:

register_agent(self, agent_class: Type[BaseAgent]): Registers an agent class. The class must have an agent_type attribute adhering to the specified naming convention.

get_agent_class(self, agent_type: str) -> Type[BaseAgent] | None: Retrieves a specific agent class by its full agent_type string (e.g., "EosLumina:v1").

get_latest_version_class(self, agent_name: str) -> Type[BaseAgent] | None: Given an [AgentName] (e.g., "EosLumina"), this method identifies and returns the class with the highest registered v[MajorVersion] for that agent name.

unregister_agent(self, agent_type: str): Removes an agent class from the registry. This supports future dynamic loading/unloading scenarios.

list_registered_agents(self) -> list[str]: Returns a list of all registered agent_type strings.

5. Instantiation and Lifecycle Management
The AgentRegistry is NOT responsible for agent instantiation or lifecycle management.

Higher-level services, such as an "Agent Orchestrator," are responsible for:

Querying the registry for agent classes.

Instantiating agents as needed, potentially passing user-specific or task-specific context to their __init__ methods.

Managing the lifecycle (activation, deactivation, error handling) of agent instances.

For certain core, stateless utility agents, a singleton pattern managed by such a higher-level service is a viable approach.

6. Dynamic Loading (Future Consideration)
While the initial implementation relies on import-time registration, the inclusion of unregister_agent and the clear separation of concerns are designed to facilitate future extensions for dynamic loading and unloading of agent modules or plugins.

7. Governance
Addition of new agent types or versions to the Canonical Agent Registry (Section 8 of this document) is a prerequisite for their recognition and use within the system.

The AgentName part of the agent_type should be chosen carefully to reflect the agent's role and avoid collisions.

8. Canonical Agent Registry Manifest
This manifest provides a canonical list of all named agents, their symbolic roles, domains of influence, and links to their detailed specifications.

Agent Name	Symbolic Role	Domain(s)	Spec/Details File
Eos Lumina∴	Oracle, Initiator	Onboarding, Attunement	swarm/core/eos_lumina.md
Nyxa∴	Privacy Guardian	Data, Privacy	swarm/ethics/nyxa.md (Assumed Path)
Themis Concordia∴	Arbiter, Governance	Governance, Conflict	swarm/ethics/themis_concordia.md
Harmonia∴	Resonance, Attunement	Hive Health, Rituals	swarm/ethics/astraia_harmonia.md
Hestia	Hearth Tender	Hive, Community	swarm/governance/hestia_koinonia.md
Calliope Scribe∴	Lore Keeper, Archivist	Documentation, Lore	swarm/knowledge/calliope_scribe.md
Mnemosyne Archivist∴	Memory, Summarization	Archives, Lore	swarm/knowledge/mnemosyne_archivist.md
Mythos Weaver	Narrative, Co-creation	Noetic Forge, Rituals	swarm/knowledge/mythopoion_koinos.md
Technes Artificer∴	Code crafting, component generation	Code, Automation	swarm/canonical_specs/technes_artificer.md
Ergon Kinesis∴	Task execution, workflow support	Workflow, Operations	swarm/canonical_specs/ergon_kinesis.md
Knowledge Retrieval Agent	Knowledge search, info retrieval	Knowledge, Search	swarm/unaligned/migration/rescued-agent-protocols.md
General Purpose Agent	General assistance, fallback logic	General, Fallback	swarm/unaligned/migration/rescued-agent-protocols.md
Vision Architect	Vision shaping, project narrative	Vision, Narrative	swarm/unaligned/migration/rescued-agent-protocols.md
Technical Architect	System design, infrastructure	Architecture, Infra	swarm/unaligned/migration/rescued-agent-protocols.md
Experience Designer	UX, interaction design	UX, UI, Interaction	swarm/unaligned/migration/rescued-agent-protocols.md
Ethical Guardian	Ethics, safety	Ethics, Safety	swarm/unaligned/migration/rescued-agent-protocols.md
Community Weaver	Community building, social fabric	Community, Social	swarm/unaligned/migration/rescued-agent-protocols.md
Biomimetic Engineer	Nature-inspired engineering	Biomimicry, Ecology	swarm/unaligned/migration/rescued-agent-protocols.md
Quantum Ethics Specialist	Quantum tech ethics	Quantum, Ethics	swarm/unaligned/migration/rescued-agent-protocols.md
Regenerative Systems Designer	Regenerative/ecological systems	Regeneration, Ecology	swarm/unaligned/migration/rescued-agent-protocols.md
Consciousness Interface Creator	Consciousness exploration interfaces	Consciousness, UI	swarm/unaligned/migration/rescued-agent-protocols.md
Note: This registry will be updated as new agents are created or specified. Legacy roles point to the migration plan until they are fully harmonized into canonical specifications.



---
### Original File: agent_registry_protocol_3d37d143.md
---
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


---
### Original File: agent_registry_protocol_e8945953.md
---
---
title: Archive: agent_registry_protocol.md
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
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


---
### Original File: agent_registry_protocol_6df64ef8.md
---
---
title: Agent Registry Protocol
version: 1.0
status: Draft
last_updated: {{Current Date}}
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
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


---
### Original File: agent_registry_protocol_28cc5ab3.md
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

The Agent Registry Protocol governs the functionality and use of the `AgentRegistry` class (located in `src/swarm/framework/agent_registry.py`). This registry serves as a central discovery mechanism for AI agent *classes*, allowing different parts of the ThinkAlike system to dynamically access agent blueprints.

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


---
### Original File: agent_registry_protocol_08099162.md
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

