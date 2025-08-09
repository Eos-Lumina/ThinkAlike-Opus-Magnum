---
title: Hive Realm API Endpoints – Symbolic, Ritual, and PET/Clarity Aligned
version: 1.0.0
status: Canonical Draft
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
last_updated: 2025-06-30
harmonization_note: Canonical specification for the Community Hive Realm API endpoints.
  Aligns with the emergent, resonance-based Hive model, symbolic/ritual API patterns,
  PET/Clarity, and the Alchemical Interface Initiative. Supersedes any legacy 'community_mode_api_endpoints.md'.
tags:
- api
- hive
- community
- endpoints
- symbolic_api
- pet_clarity
- ritual
- openapi
---

# Hives Realm API Endpoints

This document defines the canonical API endpoints for the **Community Hive Realm**. All endpoints are designed to support the emergent, resonance-based Hive model, where users discover their Hives and consciously activate their membership. These endpoints facilitate Hive discovery, activation rituals, internal Hive activities, and governance, all in alignment with `api_design_guidelines.md` and `api_documentation_guidelines.md`.

## 1. Hive Discovery & Activation Endpoints

### GET /hives/discover
- **Summary:** Discover Hives the user is passively associated with.
- **Description:** This endpoint is part of the "Awakening Ritual." It returns a list of Hives where the user's `UserValueProfile` has a high resonance score, inviting them to consciously activate their membership. Eos Lumina∴ or Harmonia∴ would trigger the UI to call this.
- **Request:** None (uses authenticated user's context).
- **Response:** `List[HiveProfileCompact]` - A list of compact Hive profiles.
- **Symbolic Metadata:** `ritual_phase: 'hive_awakening_invitation'`, `trace_id`.

### POST /hives/{hive_id}/activate_membership
- **Summary:** Activate membership in a discovered Hive.
- **Description:** The "Pledge of Attunement" ritual. The user consciously affirms the resonance the system has detected.
- **Request Body:** `{ pledge_affirmed: bool, reflective_answers?: dict }` (if the Hive requires answers to attunement questions).
- **Response:** `{ membership_status: 'ActiveMember', symbolic_status: 'attunement_complete', ritual_phase: 'hive_awakening_complete', trace_id }`.
- **Authentication:** Required.

## 2. Hive Creation (Kindling Ritual) Endpoints

*(Note: These endpoints might be restricted to users with a certain trust level or tenure).*

### POST /hives/kindle
- **Summary:** Propose the formation (Kindling) of a new Hive.
- **Description:** Initiates the "Kindling Ritual" for a new Hive, typically after the system detects a potential emergent cluster. This endpoint creates the initial Hive entity.
- **Request Body:** `HiveCreate` schema (includes `name`, `tagline`, `mission`/`founding_myth`, initial `core_values`, `privacy_level`, `governance_model`).
- **Response:** `HiveProfile` (the newly created Hive, with the creator assigned as the first "Steward").
- **Authentication:** Required.

## 3. Internal Hive Activity Endpoints ("The Honeycomb")

### GET /hives/{hive_id}/members
- **Summary:** Get the member roster for a Hive.
- **Description:** Retrieves the list of active members for the "Constellation Cell." Respects user privacy settings for how their profile is displayed.
- **Response:** `List[ProfileCard]` (list of compact user profiles).
- **Authentication:** Required (user must be an active member of the Hive).

### GET /hives/{hive_id}/discussions
- **Summary:** Get discussion channels or threads.
- **Description:** Powers the "Discussion Channels" cell. Supports pagination.
- **Response:** `List[DiscussionThread]`.
- **Authentication:** Required (member-only).

### POST /hives/{hive_id}/discussions/threads
- **Summary:** Create a new discussion thread.
- **Request Body:** `{ title: str, content: str, symbolic_tags?: [str] }`.
- **Response:** `DiscussionThread` (the new thread).
- **Authentication:** Required (member-only).

### GET /hives/{hive_id}/knowledge_base/entries
- **Summary:** Get entries from the "Lore Cell."
- **Response:** `List[KnowledgeBaseEntry]`.
- **Authentication:** Required (member-only).

### POST /hives/{hive_id}/treasury/propose_transfer
- **Summary:** Propose a Chrona transfer from the Hive's treasury.
- **Description:** Interacts with the "Flow Cell" and the Governance Portal within the Hive.
- **Request Body:** `{ recipient_id: str, amount: float, reason_memo: str, symbolic_intent: str }`.
- **Response:** `HiveProposal` (the newly created proposal for the transfer).
- **Authentication:** Required (member-only, may have further role-based restrictions).

## 4. Hive Governance Endpoints ("The Nexus Cell")

### GET /hives/{hive_id}/proposals
- **Summary:** Get a list of active and past proposals for the Hive.
- **Response:** `List[HiveProposal]`.
- **Authentication:** Required (member-only).

### POST /hives/{hive_id}/proposals
- **Summary:** Submit a new proposal to the Hive.
- **Request Body:** `ProposalCreate` schema.
- **Response:** `HiveProposal`.
- **Authentication:** Required (member-only).

### POST /hives/{hive_id}/proposals/{proposal_id}/signal
- **Summary:** Cast a signal or vote on a proposal.
- **Description:** Implements the Hive's chosen governance model (e.g., consensus signaling, voting).
- **Request Body:** `{ signal: str, justification?: str }`.
- **Response:** `{ proposal_status, symbolic_status: 'signal_cast', trace_id }`.
- **Authentication:** Required (member-only).

---
Use code with caution.
Markdown
