---
title: Model Context Protocol (MCP)
version: 3.1.0
status: Canonical
last_updated: 2025-07-07
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
tags: [protocol, context, mcp, agent_interaction, data_sovereignty, transparency, auditability, ethics, validation]
harmonization_note: |
  This document is the single canonical specification for the Model Context Protocol (MCP). It merges the philosophical foundations of `model_context_protocol.md` with the detailed technical specifications of `model_context_protocol_specification.md` into a unified standard. Version 3.1.0 incorporates the detailed `MCPEthicalValidation`, `MCPAgentRole`, and `MCPPropagationEvent` structures from a legacy draft to create a more complete and implementation-ready specification.
---

# Model Context Protocol (MCP)

## 1. Introduction & Philosophy

### 1.1. Purpose
The Model Context Protocol (MCP) is the central nervous system for all data that informs AI agent and Persona Calibration Initiative (PCI) actions within the ThinkAlike ecosystem. Its primary purpose is to provide a unified, ethical, and fully auditable framework for managing and propagating contextual information.

The MCP ensures that every AI-driven action is:
- **Transparent:** The data influencing an outcome is clearly traceable.
- **Consensual:** All data usage is explicitly tied to user consent.
- **Reversible:** The state of the context can be understood and, where appropriate, reverted.
- **Auditable:** A complete, immutable history of context changes is maintained.
- **Sovereign:** The user remains the ultimate owner and controller of their data.

### 1.2. Scope
This protocol governs the structure, lifecycle, and handling of all contextual data passed to, between, and from AI agents and related systems. It is a mandatory integration for all new and existing agent-based features.

### 1.3. Core Principles
- **Clarity over Obscurity:** Data structures are explicit and human-readable.
- **Consent by Default:** No data is used without a corresponding, active consent record.
- **Immutability of History:** The audit log cannot be altered.
- **Modularity & Extensibility:** The protocol is designed to evolve without breaking existing integrations.
- **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.

## 2. Data Structures

The following TypeScript interfaces define the core data structures for the MCP.

### 2.1. `MCPContextObject`
Represents the main container that is passed between services. It encapsulates the full state, history, and metadata of a given contextual interaction.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the primary agent interacting with this context
    timestamp: string;           // ISO8601 formatted timestamp of the last update
    current_state: MCPContextState; // The most recent state of the context
    state_history: MCPContextState[];  // An ordered list of all previous states
    consent_snapshot: object;    // A snapshot of the relevant consent object at the time of creation
    audit_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 2.2. `MCPContextState`
Represents a snapshot of the context's data at a specific moment. A new state is created for each significant operation.

```typescript
interface MCPContextState {
    state_id: string;            // Unique identifier for this specific state
    timestamp: string;           // ISO8601 formatted timestamp of when this state was created
    operation: string;           // Descriptor of the action that led to this state (e.g., 'USER_INPUT', 'AGENT_RESPONSE', 'TOOL_CALL')
    data: Record<string, any>;   // The actual payload of the context
    triggering_agent_id: string; // The ID of the agent that performed the operation
    validation_status: 'PENDING' | 'VALIDATED' | 'INVALID'; // The status of the data's validation
    ethical_validation?: MCPEthicalValidation; // Detailed results from the ethical validation process
    schema_version: string;      // The version of the data schema used
}
```

### 2.3. `MCPAuditEntry`
Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    entry_id: string;            // Unique ID for the audit entry
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'CREATE' | 'READ' | 'WRITE' | 'DELETE' | 'SHARE' | 'VALIDATE' | 'REVOKE'; // Type of operation
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved for integrity checking
    user_consented: boolean;     // Indicates if user consent was active for this operation
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 2.4. `MCPEthicalValidation`
Contains the results of an ethical validation process performed on a context object or operation. This is a critical component for ensuring alignment with ThinkAlike's core principles.

```typescript
interface MCPEthicalValidation {
    validation_id: string;       // Unique ID for this validation instance
    validated_by: string;        // ID of the ClarityAgent (or similar) that performed the validation
    context_id: string;          // ID of the context that was validated
    timestamp: string;           // ISO8601 formatted timestamp of the validation
    ethical_score: number;       // Numerical score (e.g., 0-100) representing overall ethical alignment
    bias_detection: {
        bias_detected: boolean;
        bias_types: string[];    // List of identified bias types (e.g., "gender_bias", "confirmation_bias")
        mitigation_applied: boolean;
        mitigation_details?: string;
    };
    privacy_compliance: {
        pet_applied: boolean;    // Privacy-Enhancing Technologies
        anonymization_level: 'none' | 'pseudonymized' | 'anonymized' | 'aggregated';
        consent_verified: boolean;
    };
    transparency_level: 'full' | 'partial' | 'minimal'; // Level of transparency provided to the user regarding this context/operation
    issues_found: EthicalIssue[]; // List of specific ethical concerns or violations identified
    recommendations: string[];   // Recommendations for addressing identified issues
}

interface EthicalIssue {
    issue_id: string;
    severity: 'low' | 'medium' | 'high' | 'critical';
    description: string;
    implicated_principles: string[]; // References to specific ethical principles (e.g., from ethical_ui_ux_principles.md)
}
```

### 2.5. `MCPAgentRole`
Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```

### 2.6. `MCPPropagationEvent`
Represents an event where context information is propagated from a source to target agents.

```typescript
interface MCPPropagationEvent {
    event_id: string;            // Unique ID for the propagation event
    context_id: string;          // ID of the context being propagated
    source_agent: string;        // ID of the agent initiating the propagation
    target_agents: string[];     // IDs of the agents receiving the propagated context
    operation: string;           // The operation that triggered the propagation (e.g., "context_updated", "new_insight_generated")
    data_payload: Record<string, any>; // The actual data being propagated (can be a subset or transformation of the full context)
    ethical_validation: MCPEthicalValidation; // The ethical validation status associated with this propagation
    timestamp: string;           // ISO8601 formatted timestamp of the propagation event
}
```

## 3. Protocol Lifecycle & Operations

### 3.1. Creation
- An `MCPContextObject` is created whenever a new, context-dependent interaction begins.
- A valid user consent object must exist and be active. A snapshot of this consent is embedded in the new context object.
- The initial `MCPContextState` is created with an `operation` of `CONTEXT_CREATED`.

### 3.2. Propagation & Updates
- When an agent or service performs an action, it **does not modify** the `current_state`.
- Instead, it creates a **new** `MCPContextState` with the results of its operation.
- This new state is appended to the `state_history` list.
- The `current_state` field of the `MCPContextObject` is then updated to reference this new state.
- This process ensures a fully traceable, immutable history of how the context evolved.

### 3.3. Ethical Validation Process
The ethical validation process is a non-negotiable step for significant context updates and creations.

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually by a privileged agent.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    -   Predefined ethical principles (see `guides/ethical_ui_ux_principles.md`).
    -   Bias detection algorithms.
    -   Privacy compliance rules (including consent verification).
    -   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextState`'s `ethical_validation` field, and the `validation_status` is updated accordingly.
6.  **Action**: Depending on the severity of issues found, the system might:
    -   Allow the operation (`validation_status: 'VALIDATED'`).
    -   Allow with warnings/recommendations.
    -   Require user confirmation for potentially problematic operations.
    -   Block the operation if it critically violates ethical guidelines (`validation_status: 'INVALID'`).

### 3.4. Context Propagation
1.  **Trigger**: When a context is updated and successfully validated, the MCP service can initiate propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on subscriptions, dependencies, agent roles, and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents (e.g., via a message queue or direct API calls).
5.  **Logging**: The propagation itself is logged in the `audit_log` of the source `MCPContextObject` as a `SHARE` operation.

## 4. Agent Roles & Registration
- All agents must be registered with the MCP Service to interact with context data.
- Registration involves defining an `MCPAgentRole`, specifying its type, permissions, and access levels.
- The MCP Service enforces these permissions for all operations, ensuring a `ClarityAgent` cannot perform the same actions as a `ResonanceAgent`, for example.
