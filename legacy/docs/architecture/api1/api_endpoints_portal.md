---
title: ThinkAlike Portal API Endpoints – Symbolic, Ritual, and PET/Clarity Aligned
version: 1.0.0
draft_status: Canonical Draft
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
last_updated: 2025-06-10
harmonization_note: Initial canonical draft. All endpoints harmonized for symbolic/ritual
  API patterns, PET/Clarity, and the Alchemical Interface Initiative. Supersedes any
  legacy portal endpoint docs.
tags:
- api
- portal
- endpoints
- symbolic_api
- pet_clarity
- ritual
- openapi
- swagger
- accessibility
---

# ThinkAlike Portal API Endpoints – Symbolic, Ritual, and PET/Clarity Aligned

This document defines the canonical API endpoints for the ThinkAlike Portal Realm. All endpoints are harmonized for symbolic/ritual context, PET/Clarity, and robust accessibility, and are designed to support the full 6-phase Portal journey. See [api_design_guidelines.md](../api_design_guidelines.md) and [api_documentation_guidelines.md](../api_documentation_guidelines.md) for full compliance requirements.

## Table of Contents
1. User Account & Profile Endpoints (Harmonized)
2. Portal Journey Endpoints (Phases 1–6)
3. Symbolic Metadata & PET/Clarity Notes
4. Example Request/Response Schemas

---

## 1. User Account & Profile Endpoints (Harmonized)

### POST /register
- **Summary:** Register a new user account.
- **Description:** Initiates the user's journey. Symbolic context: "Crossing the Portal Threshold."
- **Request Body:** `UserCreate` (credentials, email, etc.)
- **Response:** `User` (with symbolic metadata: `ritual_phase: 'portal_entry'`, `trace_id`)
- **Status Codes:** 201 (Created), 400 (Duplicate), 422 (Validation)
- **Authentication:** None
- **PET/Clarity:** Consent for data storage required.

### GET /profile/me
- **Summary:** Retrieve current user's profile.
- **Description:** Symbolic context: "Mirror of Self."
- **Response:** `Profile` (includes all UserValueProfile fields, symbolic metadata)
- **Status Codes:** 200, 404
- **Authentication:** Required

### PUT /profile/me
- **Summary:** Update current user's profile.
- **Description:** Symbolic context: "Profile as Living Ritual."
- **Request Body:** `ProfileUpdate` (all UserValueProfile fields, including archetypes, anchor statement, video metadata, dream consent, etc.)
- **Response:** `Profile` (with symbolic metadata)
- **Status Codes:** 200, 404, 403
- **Authentication:** Required

---

## 2. Portal Journey Endpoints (Phases 1–6)

### Phase 1: Eos Lumina's Introduction
#### POST /portal/submit_reflection/{question_id}
- **Summary:** Submit answer to a Portal reflective question.
- **Description:** Symbolic context: "Ritual of Self-Reflection."
- **Request Body:** `{ answer: str }`
- **Response:** `{ symbolic_status, ritual_phase, trace_id }`
- **Status Codes:** 200, 400
- **Authentication:** Required
- **PET/Clarity:** Consent for storing reflections.

### Phase 2: Initiation Glyph Forging
#### POST /portal/forge_glyph
- **Summary:** Trigger Initiation Glyph forging.
- **Description:** Symbolic context: "Forging the Initiation Glyph."
- **Request Body:** `{ confirmation: bool }`
- **Response:** `{ glyph_seed, symbolic_status, ritual_phase, trace_id }`
- **Status Codes:** 200, 400
- **Authentication:** Required
- **PET/Clarity:** Consent for symbolic data generation.

#### POST /portal/confirm_glyph
- **Summary:** Confirm and store Initiation Glyph parameters.
- **Request Body:** `{ glyph_seed: str, confirmation: bool }`
- **Response:** `{ symbolic_status, ritual_phase, trace_id }`

### Phase 3: Invocation Phrase
#### POST /portal/set_invocation_phrase
- **Summary:** Submit and confirm the Invocation Phrase.
- **Request Body:** `{ invocation_phrase: str }`
- **Response:** `{ symbolic_status, ritual_phase, trace_id }`
- **PET/Clarity:** Phrase is hashed and stored; explicit consent required.

### Phase 4: First Narrative Fork
#### POST /portal/record_narrative_choice
- **Summary:** Submit choice at the first narrative fork.
- **Request Body:** `{ choice: str }` (e.g., "build_thinkalike" or "continue_narrative")
- **Response:** `{ symbolic_status, ritual_phase, trace_id }`

### Phase 5: Narrative Journey Sub-Phases
#### POST /portal/archetype_selection
- **Summary:** Submit archetypal scenario choices.
- **Request Body:** `{ archetype_choices: [str] }`
- **Response:** `{ symbolic_status, ritual_phase, trace_id }`

#### POST /portal/ethical_dilemma
- **Summary:** Submit response to an ethical dilemma.
- **Request Body:** `{ dilemma_id: str, response: str }`
- **Response:** `{ symbolic_status, ritual_phase, trace_id }`

#### POST /portal/anchor_statement
- **Summary:** Submit Anchor Statement.
- **Request Body:** `{ anchor_statement: str }`
- **Response:** `{ symbolic_status, ritual_phase, trace_id }`

#### POST /portal/video_metadata
- **Summary:** Submit introductory video metadata.
- **Request Body:** `{ video_url: str, duration: int, description: str }`
- **Response:** `{ symbolic_status, ritual_phase, trace_id }`

#### POST /portal/consent_connected_services
- **Summary:** Submit consent for connected services.
- **Request Body:** `{ consent: bool, service_ids: [str] }`
- **Response:** `{ symbolic_status, ritual_phase, trace_id }`

#### POST /portal/dream_offering
- **Summary:** Submit dream fragment/symbols and consent.
- **Request Body:** `{ dream_fragments: [str], consent: bool }`
- **Response:** `{ symbolic_status, ritual_phase, trace_id }`

### Phase 5.4 & 5.5: Whispering Gallery & Narrative Duet
#### POST /portal/view_clues
- **Summary:** Acknowledge viewing abstract clues for a match.
- **Request Body:** `{ acknowledged: bool }`
- **Response:** `{ symbolic_status, ritual_phase, trace_id }`

#### POST /portal/initiate_duet
- **Summary:** Initiate a Narrative Duet with a system-suggested counterpart.
- **Request Body:** `{}`
- **Response:** `{ duet_id, symbolic_status, ritual_phase, trace_id }`

#### POST /portal/duet/{duet_id}/submit_choice
- **Summary:** Submit a choice within an active Duet.
- **Request Body:** `{ choice: str }`
- **Response:** `{ symbolic_status, ritual_phase, trace_id }`

#### GET /portal/duet/{duet_id}/outcome
- **Summary:** Retrieve outcome/alignment assessment of a Duet.
- **Response:** `{ outcome: str, alignment_score: float, symbolic_status, ritual_phase, trace_id }`

#### POST /portal/duet/{duet_id}/consent_reveal
- **Summary:** Consent to reveal video/profile to counterpart.
- **Request Body:** `{ consent: bool }`
- **Response:** `{ symbolic_status, ritual_phase, trace_id }`

#### POST /portal/duet/{duet_id}/mutual_consent
- **Summary:** Mutual consent to open direct communication.
- **Request Body:** `{}`
- **Response:** `{ symbolic_status, ritual_phase, trace_id }`

### Phase 6: Portal Completion
#### POST /portal/complete
- **Summary:** Log completion of the Portal journey.
- **Request Body:** `{}`
- **Response:** `{ symbolic_status, ritual_phase, trace_id }`

---

## 3. Symbolic Metadata & PET/Clarity Notes
- All endpoints must include symbolic metadata in responses: `ritual_phase`, `symbolic_status`, `narrative_context` (if relevant), and `trace_id`.
- All endpoints must be documented for PET/Clarity: explicit consent, privacy, and auditability.
- See [api_documentation_guidelines.md](../api_documentation_guidelines.md) for OpenAPI/Swagger requirements.

## 4. Example Request/Response Schemas
- See [api_design_guidelines.md](../api_design_guidelines.md) for canonical schema definitions and symbolic overlays.
- Example:
```json
{
  "symbolic_status": "initiated",
  "ritual_phase": "glyph_forging",
  "trace_id": "abc123xyz",
  "narrative_context": "User has completed glyph forging."
}
```

---

**Document Details**
- Title: ThinkAlike Portal API Endpoints – Symbolic, Ritual, and PET/Clarity Aligned
- Type: API Reference
- Version: 1.0.0
- Last Updated: 2025-06-10
- Maintained By: API Stewards & Lumina∴ System Meta-Agent
- Harmonization Note: Initial canonical draft. All endpoints harmonized for symbolic/ritual API patterns, PET/Clarity, and the Alchemical Interface Initiative.

---
