# Consolidated Protocol: model_context_protocol_specification


---
### Original File: model_context_protocol_specification.md
---
# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification (2)-1.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags:
- technical
---


# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification-1.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags:
- technical
---


# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification-10.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification-11.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification-12.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification-13.md:*


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

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification-14.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification-15.md:*


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

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification-2.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification-3.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags:
- technical
---


# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification-4.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification-5.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification-6.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification-7.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification-8.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags:
- technical
---


# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification-9.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags:
- technical
---


# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---
### Original File: model_context_protocol_specification_legacy1.md
---
---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification_legacy1-1.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification_legacy1-2.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags:
- technical
---


# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification_legacy1-3.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification_legacy1-4.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification_legacy1-5.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification_legacy1-6.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification_legacy1-7.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags:
- technical
---


# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification_legacy1-8.md:*


# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification_legacy1-9.md:*


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

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---
### Original File: model_context_protocol_specification_legacy2.md
---
---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification_legacy2-1.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification_legacy2-2.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags:
- technical
---


# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification_legacy2-3.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification_legacy2-4.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification_legacy2-5.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---
### Original File: model_context_protocol_specification_legacy3.md
---
---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification_legacy3-1.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags:
- technical
---


# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification_legacy3-2.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---
### Original File: model_context_protocol_specification_1.md
---
---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags:
- technical
---


# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---

*Content from model_context_protocol_specification_1-1.md:*


---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---
### Original File: model_context_protocol_specification_21248b23.md
---
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

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---
### Original File: model_context_protocol_specification_fa40f8ab.md
---
---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags:
- technical
---


# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---
### Original File: model_context_protocol_specification_2.md
---
---
title: Model Context Protocol (MCP) Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.


---
### Original File: model_context_protocol_specification_b81cd2ed.md
---
# Model Context Protocol (MCP) Specification

**Version:** 1.0.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Introduction

The Model Context Protocol (MCP) is a framework designed to manage the lifecycle of contextual data used by AI agents and PCI (Pervasive Coherent Intelligence) components within the ThinkAlike ecosystem. It ensures secure, auditable, and ethically sound context management, providing a unified approach to context propagation, validation, and user data sovereignty.

This document specifies the core principles, data structures, operations, and architectural considerations of MCP.

## 2. Core Principles

MCP is built upon the following fundamental principles:

*   **Transparency**: All context changes, accesses, and propagations are logged and, where appropriate, made visible to the user. The flow of context should be understandable and traceable.
*   **Consent**: Contextual data is not shared or utilized without explicit user consent. Users have granular control over what context is shared and with which agents or components.
*   **Reversibility**: Context state changes should be reversible where feasible, allowing users or the system to roll back to previous states, particularly within a defined timeframe (e.g., 24 hours for certain operations).
*   **Auditability**: All operations involving context data are meticulously logged, creating a comprehensive audit trail. This supports traceability, accountability, and debugging.
*   **Modularity**: The protocol is designed to be extensible, allowing for the integration of new types of agents, context sources, and validation mechanisms without requiring fundamental changes to the core protocol.
*   **Ethical Oversight**: Context handling is subject to ethical validation processes, ensuring alignment with predefined ethical guidelines and minimizing bias.
*   **User Sovereignty**: Users retain ultimate control over their data, including the right to access, export, and revoke context associated with them.

## 3. Data Structures

The following data structures are central to MCP:

### 3.1. `MCPContextObject`

Represents a distinct unit of contextual information.

```typescript
interface MCPContextObject {
    context_id: string;          // Unique identifier for the context object (e.g., "pci-algorithm-test-user123-timestamp")
    owner_id: string;            // Identifier of the user who owns this context
    agent_id: string;            // Identifier of the agent or system component that last modified or created the context
    timestamp: string;           // ISO8601 formatted timestamp of the last update or creation
    state: Record<string, any>;  // The current state of the context, a flexible key-value store
                                 // Includes 'ethical_validation: MCPEthicalValidation' after validation
    history: MCPContextState[];  // A chronological record of previous states
    consent_status: 'opted-in' | 'opted-out' | 'pending'; // User's consent status for this context
    trace_log: MCPAuditEntry[];  // Audit trail specific to this context object
}
```

### 3.2. `MCPContextState`

Represents a snapshot of the context's state at a particular point in time.

```typescript
interface MCPContextState {
    timestamp: string;           // ISO8601 formatted timestamp of when this state was recorded
    operation: string;           // Description of the operation that led to this state (e.g., "initial_creation", "user_update", "agent_inference")
    data: Record<string, any>;   // The data payload of this state
    agent_id: string;            // Identifier of the agent or system responsible for this state change
    validated: boolean;          // Indicates if this state was ethically validated at the time
}
```

### 3.3. `MCPAuditEntry`

Represents a single entry in the audit trail, logging an operation on a context object.

```typescript
interface MCPAuditEntry {
    timestamp: string;           // ISO8601 formatted timestamp of the audited event
    agent_id: string;            // Identifier of the agent or system performing the operation
    operation: 'create' | 'read' | 'write' | 'delete' | 'share' | 'validate' | 'revoke'; // Type of operation performed
    context_id: string;          // ID of the context object involved
    data_hash: string;           // A hash of the data involved in the operation (for integrity checking, not for reconstructing data)
    ethical_score?: number;      // Ethical score assigned during a 'validate' operation
    user_consented: boolean;     // Indicates if user consent was active for this operation
    reversible: boolean;         // Indicates if this specific operation is designed to be reversible
    details?: Record<string, any>; // Optional additional details about the operation
}
```

### 3.4. `MCPAgentRole`

Defines the role, permissions, and access level of an agent interacting with MCP.

```typescript
interface MCPAgentRole {
    agent_id: string;            // Unique identifier for the agent
    agent_type: string;          // Type of agent (e.g., 'ResonanceAgent', 'ClarityAgent', 'PrivacyAgent', 'NavigatorAgent', 'EosLumina', 'CustomAgent')
    permissions: string[];       // List of specific permissions granted to the agent (e.g., "context:read", "context:write", "ethical:validate")
    context_access_level: 'read' | 'write' | 'admin'; // General access level to context data
}
```
*Default Agent Types:*
*   `ResonanceAgent`: Involved in matching, discovery, and context propagation.
*   `ClarityAgent`: Responsible for ethical validation, bias detection, and transparency enforcement.
*   `PrivacyAgent`: Enforces privacy policies, manages consent, and applies PETs.
*   `NavigatorAgent`: Guides users through context flows and transitions.
*   `EosLumina`: Oversees audit trails, compliance, and provides guidance on MCP usage.

### 3.5. `MCPPropagationEvent`

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

### 3.6. `MCPEthicalValidation`

Contains the results of an ethical validation process performed on a context object or operation.

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

## 4. Key Operations & API (Conceptual)

The MCP Service (`MCPService.ts`) provides the primary interface for interacting with the protocol. Key operations include:

### 4.1. Context Creation
*   `createPCIContext(owner_id, pci_component, initial_state, consent_status)`: Creates a new `MCPContextObject`, typically for a PCI workflow. Initializes state, history, and trace log. Triggers an initial ethical validation.

### 4.2. Context Update
*   `updateContext(context_id, agent_id, operation, state_updates, require_consent)`: Modifies an existing `MCPContextObject`.
    *   Verifies agent permissions.
    *   Checks consent status if required.
    *   Archives the previous state to history.
    *   Updates the current state and timestamp.
    *   Adds an audit entry to the trace log.
    *   Triggers ethical validation of the new state.
    *   Propagates the update to subscribed/relevant agents.

### 4.3. Context Query
*   `queryContext(context_id, agent_id, query_type, specific_fields)`: Retrieves context information.
    *   Verifies agent permissions.
    *   Adds a 'read' operation to the audit trail.
    *   Returns data based on `query_type` (`full`, `summary`, `specific`) and agent permissions, potentially filtering sensitive data.

### 4.4. Context Revocation (User Sovereignty)
*   `revokeContext(context_id, owner_id)`: Allows a user (owner) to revoke consent and effectively "delete" a context.
    *   Verifies ownership.
    *   Marks the context as revoked (e.g., `state.revoked = true`, `consent_status = 'opted-out'`) rather than physically deleting, to maintain audit integrity.
    *   Adds a 'revoke' operation to the audit trail.

### 4.5. Audit Trail Access
*   `getAuditTrail(context_id?, agent_id?)`: Retrieves audit entries.
    *   Can be filtered by `context_id` (for a specific context's trace log) or `agent_id` (for all operations by a specific agent).
    *   If no filters, returns the global audit log.

### 4.6. User Context Retrieval
*   `getUserContexts(owner_id)`: Retrieves all non-revoked context objects owned by a specific user.

## 5. Ethical Validation Process

1.  **Trigger**: Ethical validation is triggered automatically upon context creation and significant updates, or can be invoked manually.
2.  **Execution**: The `ClarityAgent` (or a designated ethical validation module) performs the validation.
3.  **Assessment**: The context data, proposed operation, and relevant metadata are assessed against:
    *   Predefined ethical principles (see `docs/ethics/ethical_ui_ux_principles.md`).
    *   Bias detection algorithms.
    *   Privacy compliance rules (including consent verification).
    *   Transparency requirements.
4.  **Scoring & Reporting**: An `MCPEthicalValidation` object is generated, including an ethical score, details on bias, privacy, transparency, and any identified issues.
5.  **Integration**: The validation result is stored within the `MCPContextObject`'s state (e.g., `context.state.ethical_validation`).
6.  **Action**: Depending on the severity of issues found, the system might:
    *   Allow the operation.
    *   Allow with warnings/recommendations.
    *   Require user confirmation for potentially problematic operations.
    *   Block the operation if it critically violates ethical guidelines.

## 6. Context Propagation

1.  **Trigger**: When a context is updated (and ethically validated), the `MCPService` initiates propagation.
2.  **Relevance Determination**: The service determines which other agents or components are relevant recipients based on:
    *   The type of context.
    *   The nature of the update/operation.
    *   Predefined subscriptions or dependencies.
    *   Agent roles and permissions.
3.  **Event Creation**: An `MCPPropagationEvent` is created, containing the necessary data payload and the associated ethical validation.
4.  **Dispatch**: The event is dispatched to the target agents. (In a real system, this would involve message queues or direct API calls).
5.  **Logging**: The propagation itself can be logged in the audit trail if necessary, though the primary record is the `MCPPropagationEvent`.

## 7. Agent Registration and Permissions

*   Agents must be registered with the `MCPService` to interact with context data.
*   Registration involves defining an `MCPAgentRole`, specifying `agent_id`, `agent_type`, `permissions`, and `context_access_level`.
*   The `MCPService` enforces these permissions for all operations.

## 8. Security and Privacy Considerations

*   **Data Minimization**: Agents should only request and receive the minimal context necessary for their tasks.
*   **Encryption**: Sensitive context data should be encrypted at rest and in transit where appropriate.
*   **Access Control**: Robust access control mechanisms based on agent roles and permissions are enforced by the `MCPService`.
*   **Anonymization/Pseudonymization**: Privacy-Enhancing Technologies (PETs), including anonymization and pseudonymization, should be applied by the `PrivacyAgent` or similar components as per policy and user consent.
*   **Data Hash Integrity**: `data_hash` in `MCPAuditEntry` helps ensure that audited data hasn't been tampered with, though it's not a substitute for full cryptographic signatures in high-security scenarios.
*   **Secure Defaults**: The system should be configured with secure defaults, prioritizing user privacy.

## 9. Versioning

This specification will follow Semantic Versioning (SemVer).
*   **MAJOR** version for incompatible API changes.
*   **MINOR** version for adding functionality in a backward-compatible manner.
*   **PATCH** version for backward-compatible bug fixes.

The current version is indicated at the top of this document.

## 10. Future Considerations

*   Formal schema definitions (e.g., JSON Schema) for all data structures.
*   Standardized error codes and responses for API operations.
*   Mechanisms for context schema evolution and migration.
*   Advanced consent management features (e.g., purpose-based consent, time-limited consent).
*   Integration with external identity and access management (IAM) systems.

## 11. Related Documents

*   [Ethical UI/UX Principles](../ethics/ethical_ui_ux_principles.md)
*   [Architectural Overview](../architectural_overview.md)
*   [Visual Style Guide](../../style/visual_style_guide.md)

---

This document provides the foundational specification for the Model Context Protocol. It is intended to be a living document, evolving as the ThinkAlike project progresses.

