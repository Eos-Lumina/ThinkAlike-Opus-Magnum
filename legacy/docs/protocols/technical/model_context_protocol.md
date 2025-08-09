---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
tags:
- technical
---


# Model Context Protocol (MCP) Specification

**Version:** 1.0
**Status:** Draft
**Last Updated:** 2025-06-18
**Owner:** The Core Stewards

---

## 1. Introduction & Philosophy

### 1.1 Purpose
The Model Context Protocol (MCP) is the central nervous system for all data that informs AI agent and Persona Calibration Initiative (PCI) actions within the ThinkAlike ecosystem. Its primary purpose is to provide a unified, ethical, and fully auditable framework for managing and propagating contextual information.

The MCP ensures that every AI-driven action is:
- **Transparent:** The data influencing an outcome is clearly traceable.
- **Consensual:** All data usage is explicitly tied to user consent.
- **Reversible:** The state of the context can be understood and, where appropriate, reverted.
- **Auditable:** A complete, immutable history of context changes is maintained.
- **Sovereign:** The user remains the ultimate owner and controller of their data.

### 1.2 Scope
This protocol governs the structure, lifecycle, and handling of all contextual data passed to, between, and from AI agents and related systems. It is a mandatory integration for all new and existing agent-based features, particularly those involving the DGM/Swarm AI, Narrative Duets, and the PCI.

### 1.3 Core Principles
- **Clarity over Obscurity:** Data structures are explicit and human-readable.
- **Consent by Default:** No data is used without a corresponding, active consent record.
- **Immutability of History:** The audit log cannot be altered.
- **Modularity & Extensibility:** The protocol is designed to evolve without breaking existing integrations.

---

## 2. Core Data Structures

The MCP is built around two primary data structures: the `MCPContextObject`, which represents the entire context container, and the `MCPContextState`, which represents a snapshot of the context at a specific point in time.

### 2.1 `MCPContextObject`
This is the main container that is passed between services. It encapsulates the full state, history, and metadata of a given contextual interaction.

**Fields:**
- `context_id` (UUID): A unique identifier for this context object.
- `owner_id` (UUID): The user ID of the individual who owns the data.
- `agent_id` (String): The unique identifier of the primary agent interacting with this context (e.g., `EosLumina:v1`).
- `current_state` (MCPContextState): The most recent state of the context.
- `state_history` (List[MCPContextState]): An ordered list of all previous states, forming the context's history.
- `consent_snapshot` (Object): A snapshot of the relevant `PCIConsent` object at the time of the context's creation, ensuring that subsequent actions are bound by the consent given at that moment.
- `audit_log` (List[String]): A human-readable log of significant events related to this context object (e.g., "Context created," "State updated by Agent X," "Archived").
- `created_at` (Timestamp): The timestamp of the context's creation.
- `updated_at` (Timestamp): The timestamp of the last update to the context.

### 2.2 `MCPContextState`
This object represents a snapshot of the context's data at a specific moment. A new state is created for each significant operation.

**Fields:**
- `state_id` (UUID): A unique identifier for this specific state.
- `timestamp` (Timestamp): The time at which this state was created.
- `operation` (String): A descriptor of the action that led to this state (e.g., `USER_INPUT`, `AGENT_RESPONSE`, `TOOL_CALL`, `SYSTEM_UPDATE`).
- `data` (Object): The actual payload of the context. This can be any JSON-serializable object, such as user input, an agent's thoughts, or the output of a tool.
- `triggering_agent_id` (String): The ID of the agent that performed the operation.
- `validation_status` (String): The status of the data's validation (`PENDING`, `VALIDATED`, `INVALID`).
- `schema_version` (String): The version of the data schema used, ensuring backward compatibility.

---

## 3. Protocol Lifecycle & Operations

### 3.1 Creation
- An `MCPContextObject` is created whenever a new, context-dependent interaction begins (e.g., a user starts a Narrative Duet, an agent is invoked for a complex task).
- A `PCIConsent` object for the user must exist and be active. A snapshot of this consent is embedded in the new context object.
- The initial `MCPContextState` is created with an `operation` of `CONTEXT_CREATED`.

### 3.2 Propagation & Updates
- When an agent or service performs an action, it does not modify the `current_state`. Instead, it creates a *new* `MCPContextState` with the results of its operation.
- This new state is appended to the `state_history` list.
- The `current_state` field of the `MCPContextObject` is then updated to point to this new state.
- This process ensures a fully traceable, immutable history of how the context evolved.

### 3.3 Validation
- Before being used, the data within a state can be validated against a predefined schema or business rules.
- The `validation_status` is updated accordingly. This is crucial for ensuring data integrity, especially in complex agent swarms.

### 3.4 Archival & Deletion
- Upon completion of an interaction, the `MCPContextObject` can be archived for long-term storage and analysis.
- True deletion is subject to the project's data retention policies and the user's right to be forgotten. When a user requests data deletion, all associated `MCPContextObject`s must be located and permanently erased.

---

## 4. Integration with ThinkAlike Systems

### 4.1 Agent Swarms
In a swarm interaction, the `MCPContextObject` is the "baton" passed between agents. Each agent adds a new state to the history, allowing for a complete reconstruction of the swarm's "thought process."

### 4.2 Persona Calibration Initiative (PCI)
The MCP is the backbone of the PCI. When a contributor interacts with the PCI system (e.g., answering symbolic questions), the entire interaction is encapsulated in an `MCPContextObject`. This provides the transparency necessary for the contributor to audit exactly how their data is being used to calibrate algorithms.

### 4.3 Akashic Record
Upon archival, key events from the `MCPContextObject`'s audit log are committed to the Akashic Record, creating a permanent, high-level ledger of significant system events without storing the raw contextual data itself.

---

## 5. Ethical Considerations & Compliance
- **Data Minimization:** Only the data strictly necessary for an operation should be included in the context.
- **Anonymization:** Where possible, user identifiers should be pseudonymized in logs and analytical data derived from MCP objects.
- **User Access & Control:** Users must have a clear interface (e.g., the PCITransparencyDashboard) to view their context objects, audit their usage, and revoke the consent that underpins them.
