---
title: "ThinkAlike Master API Endpoints Specification"
version: 3.0.0
status: Canonical
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
last_updated: 2025-07-09
replaces:
  - "docs/2/protocols/master_api_endpoints.md"
  - "docs/2/protocols/api_endpoints_portal.md"
  - "docs/2/protocols/api_endpoints_hives.md"
  - "docs/2/protocols/hives_api_endpoints.md"
  - "docs/2/protocols/resonance_api_contract.md"
  - "docs/2/protocols/resonance_graph_api.md"
related_docs:
  - ./api_design_guidelines.md
  - ../protocols/core/resonant_trust_protocol.md
  - ../protocols/data/data_traceability_protocol.md
tags: [api, endpoints, architecture, portal, hives, resonance, openapi, canonical]
harmonization_note: |
  This document is the single source of truth for all ThinkAlike API endpoints. It merges and supersedes multiple legacy endpoint documents into a unified, realm-based specification. All endpoints adhere to the canonical `api_design_guidelines.md`.
---

# ThinkAlike Master API Endpoints Specification

## 1. Introduction

This document provides a canonical list and detailed description of all FastAPI endpoints for the ThinkAlike platform, organized by realm. All endpoints must adhere to the guidelines defined in `api_design_guidelines.md` and are secured according to the `resonant_trust_protocol.md`. This is a living document and will be updated as new realm specifications are finalized.

## 2. General Conventions

- **Base URL:** `/api/v1`
- **Authentication:** All endpoints require JWT token authentication unless specified otherwise.
- **Responses:** Standard success and error responses as defined in `api_design_guidelines.md`.
- **Symbolic & Ritual Context:** Many endpoints include symbolic metadata (`ritual_phase`, `symbolic_status`, `trace_id`) to support the narrative and ethical layers of the platform.

---

## 3. Portal Realm API Endpoints

These endpoints manage the user's journey through the Portal, from initial registration to narrative choices.

### 3.1. User Account & Profile

#### POST /v1/register
- **Summary:** Register a new user account.
- **Description:** Initiates the user's journey. Symbolic context: "Crossing the Portal Threshold."
- **Request Body:** `UserCreate` (credentials, email, etc.)
- **Response:** `User` (with symbolic metadata: `ritual_phase: 'portal_entry'`, `trace_id`)
- **Authentication:** None
- **PET/Clarity:** Consent for data storage required.

#### GET /v1/profile/me
- **Summary:** Retrieve current user's profile.
- **Description:** Symbolic context: "Mirror of Self."
- **Response:** `Profile` (includes all UserValueProfile fields, symbolic metadata)
- **Authentication:** Required

#### PUT /v1/profile/me
- **Summary:** Update current user's profile.
- **Description:** Symbolic context: "Profile as Living Ritual."
- **Request Body:** `ProfileUpdate` (all UserValueProfile fields)
- **Response:** `Profile` (with symbolic metadata)
- **Authentication:** Required

### 3.2. Portal Onboarding Journey (Phases 1-6)

#### POST /v1/portal/submit_reflection/{question_id}
- **Summary:** Submit answer to a Portal reflective question.
- **Description:** Symbolic context: "Ritual of Self-Reflection."
- **Request Body:** `{ "answer": "string" }`
- **Response:** `{ "symbolic_status", "ritual_phase", "trace_id" }`
- **Authentication:** Required

#### POST /v1/portal/forge_glyph
- **Summary:** Trigger Initiation Glyph forging based on reflections.
- **Description:** Symbolic context: "Forging the Initiation Glyph."
- **Request Body:** `{ "confirmation": true }`
- **Response:** `{ "glyph_seed", "symbolic_status", "ritual_phase", "trace_id" }`
- **Authentication:** Required

#### POST /v1/portal/set_invocation_phrase
- **Summary:** Submit and confirm the Invocation Phrase.
- **Request Body:** `{ "invocation_phrase": "string" }`
- **Response:** `{ "symbolic_status", "ritual_phase", "trace_id" }`
- **PET/Clarity:** Phrase is hashed and stored; explicit consent required.

#### POST /v1/portal/record_narrative_choice
- **Summary:** Submit choice at a narrative fork.
- **Request Body:** `{ "choice": "string" }` (e.g., "build_thinkalike" or "continue_narrative")
- **Response:** `{ "symbolic_status", "ritual_phase", "trace_id" }`

#### POST /v1/portal/user/video-introduction
- **Summary:** Upload the user’s introductory video.
- **Request Body:** `multipart/form-data` with file field `video`.
- **Response:** `201 Created` with video metadata.

---

## 4. Hives Realm API Endpoints

These endpoints facilitate Hive discovery, activation, internal activities, and governance.

### 4.1. Hive Discovery & Activation

#### GET /v1/hives/discover
- **Summary:** Discover Hives the user is passively associated with.
- **Description:** Part of the "Awakening Ritual." Returns Hives where the user's `UserValueProfile` has high resonance.
- **Response:** `List[HiveProfileCompact]`
- **Symbolic Metadata:** `ritual_phase: 'hive_awakening_invitation'`, `trace_id`.

#### POST /v1/hives/{hive_id}/activate_membership
- **Summary:** Activate membership in a discovered Hive.
- **Description:** The "Pledge of Attunement" ritual.
- **Request Body:** `{ "pledge_affirmed": true, "reflective_answers"?: {} }`
- **Response:** `{ "membership_status": "ActiveMember", "symbolic_status": "attunement_complete" }`
- **Authentication:** Required.

### 4.2. Hive Creation & Management

#### POST /v1/hives/kindle
- **Summary:** Propose the formation (Kindling) of a new Hive.
- **Description:** Initiates the "Kindling Ritual" for a new Hive.
- **Request Body:** `HiveCreate` schema (`name`, `mission`, `core_values`, etc.).
- **Response:** `HiveProfile`
- **Authentication:** Required (Trust Level dependent).

#### GET /v1/hives/{hive_id}/members
- **Summary:** Get the member roster for a Hive.
- **Response:** `List[ProfileCard]`
- **Authentication:** Required (member-only).

### 4.3. Internal Hive Activity ("The Honeycomb")

#### GET /v1/hives/{hive_id}/discussions
- **Summary:** Get discussion channels or threads.
- **Response:** `List[DiscussionThread]`
- **Authentication:** Required (member-only).

#### POST /v1/hives/{hive_id}/discussions/threads
- **Summary:** Create a new discussion thread.
- **Request Body:** `{ "title": "string", "content": "string", "symbolic_tags"?: ["string"] }`
- **Response:** `DiscussionThread`
- **Authentication:** Required (member-only).

#### POST /v1/hives/{hive_id}/treasury/propose_transfer
- **Summary:** Propose a Chrona transfer from the Hive's treasury.
- **Description:** Interacts with the "Flow Cell" and Governance Portal.
- **Request Body:** `{ "recipient_id": "string", "amount": "float", "reason_memo": "string", "symbolic_intent": "string" }`
- **Response:** `HiveProposal`
- **Authentication:** Required (member-only, role-based restrictions may apply).

### 4.4. Hive Governance ("The Nexus Cell")

#### GET /v1/hives/{hive_id}/proposals
- **Summary:** Get a list of active and past proposals for the Hive.
- **Response:** `List[HiveProposal]`
- **Authentication:** Required (member-only).

#### POST /v1/hives/{hive_id}/proposals/{proposal_id}/signal
- **Summary:** Cast a signal or vote on a proposal.
- **Description:** Implements the Hive's chosen governance model (e.g., consensus signaling, voting).
- **Request Body:** `{ "signal": "string", "justification"?: "string" }`
- **Response:** `ProposalSignalConfirmation`

---

## 5. Resonance Realm API Endpoints

This API powers the value-alignment graph, enabling symbolic matchmaking and discovery.

### 5.1. Core Resonance Operations

#### GET /v1/resonance/profile/{user_id}
- **Summary:** Retrieve a user's current resonance vector.
- **Description:** Provides structured access to a user’s resonance vector for matchmaking and agent interpretation.
- **Response:** `ResonanceProfile`
- **Authentication:** Required, with consent context.

#### POST /v1/resonance/update
- **Summary:** Submit new fork path or tag weights to update a user's resonance profile.
- **Description:** Allows a user's resonance profile to evolve based on their interactions and choices.
- **Request Body:** `{ "updates": [ { "tag": "string", "weight": "float" } ] }`
- **Response:** `UpdateConfirmation`
- **Authentication:** Required.

#### GET /v1/resonance/match/{user_id}
- **Summary:** Return top N resonance matches for a user.
- **Description:** The core matchmaking endpoint. Matches can be between profiles, ideas, or communities.
- **Query Params:** `limit=10`
- **Response:** `List[MatchResult]`
- **Privacy:** All matches are opt-in and filtered through PET overlays.

### 5.2. Resonance Control & Configuration

#### POST /v1/resonance/mask
- **Summary:** Hide selected resonance traits from being used in matching.
- **Description:** Empowers users to control their data by masking or locking specific resonance tags.
- **Request Body:** `{ "masked_tags": ["string"] }`
- **Response:** `MaskingConfirmation`
- **Authentication:** Required.

#### GET /v1/resonance/archetype/{cluster_name}
- **Summary:** Query archetypal mappings within the resonance graph.
- **Description:** Allows for exploration of the collective consciousness and emergent archetypes.
- **Response:** `ArchetypeDefinition`
- **Authentication:** Required.
