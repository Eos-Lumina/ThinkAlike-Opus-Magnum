---
title: ThinkAlike API Specifications
version: 1.0.0
status: Active
last_updated: 2023-10-27
maintained_by: ['API Development Team']
tags: ['api', 'openapi', 'specification', 'documentation']
---

# ThinkAlike API Specifications

This directory contains the canonical, machine-readable API specifications for the ThinkAlike project, primarily defined using the **OpenAPI 3.0 standard**. These files are the single source of truth for all API endpoints, schemas, and contracts.

For general best practices that guide the design of these APIs, please refer to [`docs/architecture/api_design_guidelines.md`](../architecture/api_design_guidelines.md).

---

## Canonical API Specifications

Each major Realm or Service has its own API specification file.

### 🏛️ **Portal Realm API**
-   **Specification File:** [`portal_api.yaml`](./portal_api.yaml)
-   **Description:** Governs the user initiation journey, including registration, profile creation, value elicitation, and the forging of symbolic anchors (Initiation Glyph & Invocation Phrase).
-   **Status:** `v1.0.0 - Stable`

### 🕸️ **Resonance Graph API**
-   **Specification File:** [`resonance_graph_api.md`](./resonance_graph_api.md)
-   **Description:** Defines the contract for interacting with the Resonance Graph, the core data structure for mapping relationships and values.
-   **Status:** `v1.0.0 - Stable`

### 📜 **Resonance API Contract**
-   **Specification File:** [`resonance_api_contract.md`](./resonance_api_contract.md)
-   **Description:** A markdown-based contract outlining the principles and data models for the Resonance API.
-   **Status:** `v1.0.0 - Stable`

---

## Tooling & Usage

These OpenAPI specifications can be used with a variety of tools to enhance development:

-   **Interactive Documentation:** Use tools like [Swagger UI](https://swagger.io/tools/swagger-ui/) or [Redoc](https://github.com/Redocly/redoc) to generate interactive API documentation that developers can use to explore and test endpoints.
-   **Code Generation:** Use [OpenAPI Generator](https://openapi-generator.tech/) to automatically generate client SDKs (for frontend consumption) or server stubs.
-   **Automated Testing:** Integrate with testing frameworks to create contract tests that ensure the implementation never deviates from the specification.

---
*This index will be updated as new API specifications are created and canonized.*
