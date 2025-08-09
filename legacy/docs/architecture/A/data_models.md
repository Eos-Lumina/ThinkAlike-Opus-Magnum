---
title: Canonical Data Models & Schemas
version: 2.1
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
status: Harmonized
last_updated: 2025-07-11
tags:
- data
- data_systems
- database
- entity
- model
- relationship
- schema
---

# 🧬 Canonical Data Models & Schemas

This document defines the canonical data models and schemas for the ThinkAlike ecosystem. It is the source of truth for all persistent data structures, guiding backend development, API design, and database architecture. All entities defined herein must be reflected in the `prisma/schema.prisma` file, the OpenAPI specification, and all related backend services.

## 1. Core Principles

- **Clarity & Consistency:** Models are designed to be self-explanatory and consistently named.
- **Scalability:** Schemas are structured to support millions of users and complex interactions.
- **Extensibility:** The design accommodates future features and modules with minimal disruption.
- **Traceability:** Key entities include fields for tracking data provenance and user consent, aligning with the `data_traceability_protocol.md`.

## 2. Entity Relationship Diagram (ERD)

```mermaid
erDiagram
    User {
        UUID id PK
        String username
        String email
        DateTime created_at
        Boolean is_active
        String resonance_fingerprint
        String persona_archetype
    }
    ValueProfile {
        UUID id PK
        UUID user_id FK
        String[] values
        String[] archetypes
        Float resonance_score
        DateTime updated_at
    }
    NarrativeDuet {
        UUID id PK
        UUID user_id FK
        UUID agent_id FK
        DateTime started_at
        DateTime completed_at
        String quest_type
    }
    Message {
        UUID id PK
        UUID duet_id FK
        String sender
        String content
        DateTime timestamp
    }
    Connection {
        UUID id PK
        UUID source_id FK
        UUID target_id FK
        String type "user-user, user-agent"
        String status "pending, active, blocked"
        DateTime created_at
    }
    Hive {
        UUID id PK
        String name
        String description
        DateTime created_at
        String hive_type
    }
    HiveMember {
        UUID id PK
        UUID hive_id FK
        UUID user_id FK
        String role
        DateTime joined_at
        Boolean is_admin
    }
    ChronaWallet {
        UUID id PK
        UUID user_id FK
        Float balance
    }
    ChronaTransaction {
        UUID id PK
        UUID wallet_id FK
        Float amount
        String type "earn, spend, transfer"
        String description
        DateTime timestamp
        String ritual_flow
    }
    Consent {
        UUID id PK
        UUID user_id FK
        String scope
        DateTime granted_at
        DateTime revoked_at
        Boolean active
    }
    PCIProfile {
        UUID id PK
        UUID user_id FK
        String calibration_data
    }
    PCIConsent {
        UUID id PK
        UUID pci_profile_id FK
        String scope
        String details
    }
    AgentSession {
        UUID id PK
        UUID user_id FK
        UUID agent_id FK
        DateTime start_time
        DateTime end_time
        String session_type
    }
    TraceabilityRecord {
        UUID id PK
        UUID user_id FK
        UUID data_id FK
        String action
        DateTime timestamp
        String details
    }
    MythicRole {
        UUID id PK
        String name
        String description
        String guild
    }
    Ritual {
        UUID id PK
        String name
        String description
        String flow_type
    }
    GovernanceProposal {
        UUID id PK
        String title
        String description
        UUID proposer_id FK
        DateTime created_at
        String status
    }
    Vote {
        UUID id PK
        UUID proposal_id FK
        UUID voter_id FK
        String choice
        DateTime timestamp
    }
    OnboardingJourney {
        UUID id PK
        UUID user_id FK
        String status
        DateTime started_at
        DateTime completed_at
    }
    PersonaCalibration {
        UUID id PK
        UUID user_id FK
        String calibration_data
        DateTime updated_at
    }
    User ||--o{ ValueProfile : "has one"
    User ||--o{ NarrativeDuet : "participates in"
    User ||--o{ Connection : "initiates"
    User ||--o{ HiveMember : "is a"
    User ||--o{ ChronaWallet : "owns"
    User ||--o{ Consent : "grants"
    User ||--o{ PCIProfile : "calibrates"
    User ||--o{ AgentSession : "interacts with"
    User ||--o{ TraceabilityRecord : "triggers"
    User ||--o{ OnboardingJourney : "undertakes"
    User ||--o{ PersonaCalibration : "calibrates"
    NarrativeDuet ||--o{ Message : "contains"
    Hive ||--o{ HiveMember : "has many"
    ChronaWallet ||--o{ ChronaTransaction : "records"
    PCIProfile ||--o{ PCIConsent : "has"
    GovernanceProposal ||--o{ Vote : "receives"

## 3. Canonical Entity Table

| Entity | Purpose/Description | Key Fields / Relationships |
|---|---|---|
| **User** | The core identity for any individual interacting with the ThinkAlike ecosystem. Represents the sovereign digital self. | `id (UUID)`, `username (str)`, `email (str)`, `resonance_fingerprint (str)`, `persona_archetype (str)`, `created_at (datetime)`, `is_active (bool)` |
| **ValueProfile** | A detailed representation of a user's core values, archetypal alignments, and resonance scores. | `id (UUID)`, `user_id (FK)`, `values (list[str])`, `archetypes (list[str])`, `resonance_score (float)`, `updated_at (datetime)` |
| **NarrativeDuet** | An interactive, AI-guided session for onboarding, self-reflection, or specific narrative quests. | `id (UUID)`, `user_id (FK)`, `agent_id (FK)`, `transcript (list[Message])`, `started_at (datetime)`, `completed_at (datetime)`, `quest_type (str)` |
| **Message** | A single utterance within a `NarrativeDuet`, sent by either the user or an AI agent. | `id (UUID)`, `duet_id (FK)`, `sender (enum: user, agent)`, `content (text)`, `timestamp (datetime)` |
| **Connection** | Represents a persistent, directional link between two entities, such as a friendship, mentorship, or follow. | `id (UUID)`, `source_id (FK)`, `target_id (FK)`, `type (enum: user-user, user-agent)`, `status (enum: pending, active, blocked)` |
| **Hive** | A self-organized community or group focused on a shared interest, project, or goal. | `id (UUID)`, `name (str)`, `description (text)`, `created_at (datetime)`, `hive_type (str)` |
| **HiveMember** | A record of a user's membership within a `Hive`, including their role and status. | `id (UUID)`, `hive_id (FK)`, `user_id (FK)`, `role (str)`, `joined_at (datetime)`, `is_admin (bool)` |
| **ChronaWallet** | A user's personal wallet for managing `Chrona (⧖)`, the internal time-based currency. | `id (UUID)`, `user_id (FK)`, `balance (float)`, `transactions (list[ChronaTransaction])` |
| **ChronaTransaction** | A record of a single `Chrona` transaction, whether earned, spent, or transferred. | `id (UUID)`, `wallet_id (FK)`, `amount (float)`, `type (enum: earn, spend, transfer)`, `description (str)`, `timestamp (datetime)`, `ritual_flow (str)` |
| **Consent** | A granular record of a user's explicit consent for data processing, sharing, or interaction within a specific scope. | `id (UUID)`, `user_id (FK)`, `scope (str)`, `granted_at (datetime)`, `revoked_at (datetime, nullable)`, `active (bool)` |
| **PCIProfile** | (Personal Consciousness Interface) A specialized profile for deep, calibrated interaction with AI systems. | `id (UUID)`, `user_id (FK)`, `calibration_data (str)` |
| **PCIConsent** | A specific consent record related to the `PCIProfile`. | `id (UUID)`, `pci_profile_id (FK)`, `scope (str)`, `details (str)` |
| **AgentSession** | A record of a user's interaction with a specific AI agent outside of a `NarrativeDuet`. | `id (UUID)`, `user_id (FK)`, `agent_id (FK)`, `start_time (datetime)`, `end_time (datetime)`, `session_type (str)` |
| **TraceabilityRecord** | A log entry that traces the origin, transformation, and use of a piece of data. | `id (UUID)`, `user_id (FK)`, `data_id (FK)`, `action (str)`, `timestamp (datetime)`, `details (str)` |
| **MythicRole** | Represents a mythic persona or agent role (e.g., Eos Lumina, Hermes Orchestrator) and its guild. | `id (UUID)`, `name (str)`, `description (str)`, `guild (str)` |
| **Ritual** | Encodes symbolic or narrative rituals, flows, and their types. | `id (UUID)`, `name (str)`, `description (str)`, `flow_type (str)` |
| **GovernanceProposal** | A proposal for governance, protocol change, or community decision. | `id (UUID)`, `title (str)`, `description (str)`, `proposer_id (FK)`, `status (str)` |
| **Vote** | A record of a user's vote on a proposal. | `id (UUID)`, `proposal_id (FK)`, `voter_id (FK)`, `choice (str)` |
| **OnboardingJourney** | Tracks a user's onboarding journey, status, and completion. | `id (UUID)`, `user_id (FK)`, `status (str)`, `started_at (datetime)`, `completed_at (datetime)` |
| **PersonaCalibration** | Stores calibration data for user personas and agent alignment. | `id (UUID)`, `user_id (FK)`, `calibration_data (str)`, `updated_at (datetime)` |
| **Profile** | User profile details, preferences, and metadata (distinct from ValueProfile). | `id (UUID)`, `user_id (FK)`, `bio (str)`, `avatar (str)`, `settings_id (FK)` |
| **Community** | Open/public groupings, events, or spaces (beyond Hive). | `id (UUID)`, `name (str)`, `type (str)`, `members (list[User])` |
| **Match** | Match records for onboarding, discovery, or quests. | `id (UUID)`, `user_id (FK)`, `target_id (FK)`, `match_type (str)`, `status (str)` |
| **Interaction** | Log of all user/agent/system interactions (not just messages). | `id (UUID)`, `user_id (FK)`, `agent_id (FK)`, `type (str)`, `timestamp (datetime)` |
| **AIModel** | Registry of AI models and their usage. | `id (UUID)`, `name (str)`, `version (str)`, `metrics (json)`, `last_used (datetime)` |
| **Settings** | Configuration for users, agents, and system. | `id (UUID)`, `owner_id (FK)`, `type (str)`, `config (json)` |
| **UIComponent** | Mapping of UI components to data models/endpoints. | `id (UUID)`, `name (str)`, `type (str)`, `data_model (str)`, `api_endpoint (str)` |
| **DataValidationError** | Tracks validation errors in workflows. | `id (UUID)`, `source_id (FK)`, `error_type (str)`, `details (str)`, `timestamp (datetime)` |
| **SecurityAlert** | Real-time security notifications. | `id (UUID)`, `user_id (FK)`, `alert_type (str)`, `details (str)`, `timestamp (datetime)` |
| **DataProvenance** | Tracks data sources and origins. | `id (UUID)`, `data_id (FK)`, `source (str)`, `provenance_details (str)`, `timestamp (datetime)` |

## 4. Cross-References

- **Implementation:** The canonical implementation of these models resides in `prisma/schema.prisma`.
- **API:** The public interface for interacting with these models is defined in `docs/api_specs/openapi.json`.
- **Ontology:** For the conceptual and semantic layer underpinning these models, see `data_ontology.md`.
- **Architecture:** For how these models fit into the broader system, see `architecture_overview.md`.

## 5. Architectural Data Flow & Layers

```mermaid
graph TD;
    UI[User Interface] -->|Input| API[API Layer]
    API -->|Request| AI[AI Processing]
    API -->|Request| DB[Database Storage]
    AI -->|Response| API
    DB -->|Data| API
    API -->|Response| UI
    subgraph "Data Flow"
        UI --> API
        API --> AI
        API --> DB
        AI --> API
        DB --> API
        API --> UI
    end
```

### Layers
- **UI (React):** DataDisplay, UserForm, APIValidator, DataTraceability, WorkflowProgress, ActionButton, SecurityFeedback, AIModelPerformance, RunTestsButton, CoreValuesValidator, DataModifier.
- **API (Node.js/Express, Python/FastAPI):** RESTful endpoints, OpenAPI/Swagger docs, validation, authentication, CORS.
- **Database (PostgreSQL/Prisma):** All persistent entities.
- **AI (Python/HuggingFace, etc.):** Model registry, performance metrics, explainability.

## 6. Data Validation & Ethical Guidelines

- **Validation Workflows:** UI-driven, API validation, schema enforcement, error tracking (DataValidationError).
- **Ethical Guidelines:** Privacy, bias mitigation, transparency, audit logging, security alerts.

## 7. Implementation Mandates

- All new entities and relationships must be reflected in backend code, API docs, and UI components.
- Cross-reference all canonical docs: `source_of_truth.md`, `api_specs/openapi_template.yaml`, `architecture/database/database_schema.md`, `architecture/agent_framework/agent_ecosystem_design.md`, etc.
