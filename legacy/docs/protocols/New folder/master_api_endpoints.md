---
title: ThinkAlike Master API Endpoints Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
tags:
- api
---


# ThinkAlike Master API Endpoints Specification

## 1. Introduction
This document provides a **canonical list** and brief description of all FastAPI endpoints for the ThinkAlike platform, organized by realm and service. All endpoints must adhere to the guidelines defined in `api_design_guidelines.md` and are secured according to `security_and_privacy_plan.md`. This is a **living document** and will be updated as new realm specifications are finalized.

## 2. General Conventions
- **Base URL:** `/api/v1`
- **Authentication:** All endpoints require JWT token authentication unless specified otherwise.
- **Responses:** Standard success and error responses as defined in `api_design_guidelines.md`.

## 3. Endpoints by Realm/Service

### 3.1 Portal Realm (`/portal`)

#### 3.1.1 GET /portal/initiation/start
- **Purpose:** Fetch initial prompts and state for a new user entering the Portal.
- **Request Body:** None
- **Success Response:** `200 OK` with JSON payload, e.g.:
  ```json
  {
    "prompt": "Welcome to ThinkAlike. Please answer three reflections to begin.",
    "questions": ["Who are you?", "What brings you here?", "What do you seek?"]
  }
  ```

#### 3.1.2 POST /portal/initiation/submit-reflection
- **Purpose:** Submit answers to the initial three reflection questions.
- **Request Body:**
  ```json
  {
    "answers": ["...", "...", "..."]
  }
  ```
- **Success Response:** `200 OK` with confirmation and next steps, e.g.:
  ```json
  { "status": "reflections_received", "next": "/portal/initiation/forge-glyph" }
  ```

#### 3.1.3 POST /portal/initiation/forge-glyph
- **Purpose:** Forge the Initiation Glyph based on submitted reflections.
- **Request Body:**
  ```json
  { "attributes": { /* glyph parameters */ } }
  ```
- **Success Response:** `201 Created` with glyph details, e.g.:
  ```json
  { "glyphId": "abc123", "imageUrl": "..." }
  ```

#### 3.1.4 POST /portal/initiation/set-invocation-phrase
- **Purpose:** Confirm or set the Invocation Phrase for the Initiate.
- **Request Body:**
  ```json
  { "phrase": "Your invocation phrase here" }
  ```
- **Success Response:** `200 OK` with confirmation, e.g.:
  ```json
  { "status": "phrase_set" }
  ```

#### 3.1.5 GET /portal/narrative/current-step
- **Purpose:** Retrieve the current narrative block for the Initiate.
- **Request Body:** None
- **Success Response:** `200 OK` with narrative data, e.g.:
  ```json
  { "stepId": "step_5", "text": "Your journey continues...", "choices": [ {"id": "c1","label": "Go left"}, ... ] }
  ```

#### 3.1.6 POST /portal/narrative/make-choice
- **Purpose:** Submit a choice and advance the narrative.
- **Request Body:**
  ```json
  { "choice_id": "c1" }
  ```
- **Success Response:** `200 OK` with next narrative block, e.g.:
  ```json
  { "stepId": "step_6", "text": "New narrative..." }
  ```

#### 3.1.7 POST /portal/user/video-introduction
- **Purpose:** Upload the user’s introductory video.
- **Request Body:** `multipart/form-data` with file field `video`.
- **Success Response:** `201 Created` with video metadata, e.g.:
  ```json
  { "videoId": "vid789", "url": "..." }
  ```

#### 3.1.8 POST /portal/user/connected-services/link
- **Purpose:** Link an external service to the user’s profile.
- **Request Body:**
  ```json
  { "service": "github", "credentials": { /* token or OAuth code */ } }
  ```
- **Success Response:** `200 OK` with link confirmation, e.g.:
  ```json
  { "status": "linked", "service": "github" }
  ```

#### 3.1.9 DELETE /portal/user/connected-services/unlink
- **Purpose:** Unlink an external service from the user’s profile.
- **Request Body:**
  ```json
  { "service": "github" }
  ```
- **Success Response:** `204 No Content`

#### 3.1.10 GET /portal/duet/whispers
- **Purpose:** Fetch system-suggested “Whispering Gallery” clues for the first Duet session.
- **Request Body:** None
- **Success Response:** `200 OK` with clues, e.g.:
  ```json
  { "clues": ["...", "..."] }
  ```

#### 3.1.11 POST /portal/duet/session/{session_id}/make-choice
- **Purpose:** Submit a choice within a Duet session.
- **Path Parameter:** `session_id` (string)
- **Request Body:**
  ```json
  { "choice_id": "..." }
  ```
- **Success Response:** `200 OK` with updated session state, e.g.:
  ```json
  { "nextClue": "...", "state": "in_progress" }
  ```

#### 3.1.12 POST /portal/duet/session/{session_id}/give-consent
- **Purpose:** Give consent to proceed in a Duet session.
- **Path Parameter:** `session_id` (string)
- **Request Body:**
  ```json
  { "consent": true }
  ```
- **Success Response:** `200 OK` with confirmation, e.g.:
  ```json
  { "status": "consent_recorded" }
  ```

### 3.2 Resonance Network Realm (`/network`)

#### 3.2.1 POST /network/nodes/query
- **Purpose:** Retrieve User Nodes visible to the current user for display on the constellation map, supporting pagination and spatial/resonance-based filters.
- **Request Body:**
  ```json
  {
    "viewport": { "xMin": 0, "yMin": 0, "xMax": 100, "yMax": 100 },
    "zoomLevel": 2,
    "filters": { /* optional resonance strength, tags */ },
    "page": 1,
    "pageSize": 50
  }
  ```
- **Success Response:** `200 OK` with JSON payload, e.g.:
  ```json
  [{
    "id": "user123",
    "name": "Echo Wanderer",
    "glyph": { /* minimal glyph data */ },
    "echoPhrase": "Whisper of Dawn",
    "resonanceStrength": 0.76
  }, ...]
  ```

#### 3.2.2 GET /network/nodes/{target_user_id}
- **Purpose:** Retrieve full details for a single User Node when clicked.
- **Path Parameter:** `target_user_id` (string)
- **Request Body:** None
- **Success Response:** `200 OK` with JSON payload, e.g.:
  ```json
  {
    "id": "user123",
    "name": "Echo Wanderer",
    "videoUrl": "...",
    "resonantElements": ["Lunar Echo", "Chrona Pulse"]
  }
  ```

#### 3.2.3 POST /network/duet/initiate
- **Purpose:** Initiate a Narrative Duet session with another user.
- **Request Body:**
  ```json
  { "target_user_id": "user123" }
  ```
- **Success Response:** `201 Created` with JSON payload, e.g.:
  ```json
  {
    "sessionId": "sess456",
    "initialBlock": { /* NarrativeBlock object */ }
  }
  ```

#### 3.2.4 POST /network/duet/session/{session_id}/make-choice
- **Purpose:** Submit a choice within an existing Duet session in the Resonance Network context.
- **Path Parameter:** `session_id` (string)
- **Request Body:**
  ```json
  { "choice_id": "c42" }
  ```
- **Success Response:** `200 OK` with updated session data, e.g.:
  ```json
  { "nextBlock": { /* next NarrativeBlock */ } }
  ```

#### 3.2.5 POST /network/duet/session/{session_id}/give-consent
- **Purpose:** Record user consent to proceed with Reveals in the Duet session.
- **Path Parameter:** `session_id` (string)
- **Request Body:**
  ```json
  { "consent": true }
  ```
- **Success Response:** `200 OK` with confirmation, e.g.:
  ```json
  { "status": "consent_recorded" }
  ```

#### 3.2.6 POST /network/connections/{connection_id}/affirm-resonance
- **Purpose:** Provide post-connection symbolic feedback on the quality of resonance.
- **Path Parameter:** `connection_id` (string)
- **Request Body:**
  ```json
  { "affirmation_type": "Deepening_Harmony" }
  ```
- **Success Response:** `200 OK` with acknowledgement, e.g.:
  ```json
  { "status": "affirmation_recorded" }
  ```

### 3.3 Community Hive Realm (`/hives`)

#### A. Hive Discovery & Membership

##### 3.3.1 GET /hives/my-resonant-hives
- **Purpose:** Retrieve the list of Hives the user is automatically attuned to upon entering the realm.
- **Request Body:** None
- **Success Response:** `200 OK` with array of Hive summary objects, e.g.:
  ```json
  [{ "id": "hive1", "name": "Lumina Circle", "symbol": "..." }, ...]
  ```

##### 3.3.2 GET /hives
- **Purpose:** Browse or search all Hives in the directory.
- **Query Params:** `search` (string), `tags` (csv), `min_members` (int), `page`, `pageSize`
- **Success Response:** `200 OK` with paginated array of Hive summaries, e.g.:
  ```json
  { "page":1, "total":200, "hives": [{ "id":"h1","name":"..." }, ...] }
  ```

##### 3.3.3 GET /hives/{hive_id}
- **Purpose:** Retrieve full details of a specific Hive.
- **Path Parameter:** `hive_id` (string)
- **Success Response:** `200 OK` with detailed Hive object, e.g.:
  ```json
  { "id":"h1","name":"Lumina Circle","description":"...","members":["u1","u2"],"recentActivity": [...] }
  ```

##### 3.3.4 POST /hives/{hive_id}/join
- **Purpose:** Join a Hive via the Ritual of Attunement.
- **Path Parameter:** `hive_id` (string)
- **Request Body (Optional):**
  ```json
  { "statement_of_intent": "I seek to..." }
  ```
- **Success Response:** `200 OK` with membership status, e.g.:
  ```json
  { "status":"joined" }
  ```

##### 3.3.5 POST /hives/{hive_id}/leave
- **Purpose:** Leave a Hive (Ritual of Departure).
- **Path Parameter:** `hive_id` (string)
- **Request Body:** None
- **Success Response:** `200 OK` with confirmation, e.g.:
  ```json
  { "status":"left" }
  ```

##### 3.3.6 POST /hives
- **Purpose:** Create a new Hive (Hive Genesis).
- **Request Body:**
  ```json
  { "name":"...","purpose":"...","core_values":["..."],"initial_governance_model":"...","glyph_data":{...} }
  ```
- **Success Response:** `201 Created` with new Hive object, e.g.:
  ```json
  { "id":"h2","name":"...","createdBy":"u1" }
  ```

#### B. Internal Hive Operations

##### 3.3.7 GET /hives/{hive_id}/hearth/posts
- **Purpose:** Retrieve paginated posts from a Hive's Hearth (forum).
- **Path Parameter:** `hive_id` (string)
- **Query Params:** `page`, `pageSize`
- **Success Response:** `200 OK` with array of post objects.

##### 3.3.8 GET /hives/{hive_id}/lore/{document_id}
- **Purpose:** Retrieve a specific Lore document within a Hive.
- **Path Parameters:** `hive_id`, `document_id` (strings)
- **Success Response:** `200 OK` with document details.

##### 3.3.9 POST /hives/{hive_id}/hearth/posts
- **Purpose:** Create a new post in a Hive's Hearth.
- **Path Parameter:** `hive_id` (string)
- **Request Body:**
  ```json
  { "title":"...","content":"..." }
  ```
- **Success Response:** `201 Created` with new post object.

##### 3.3.10 GET /hives/{hive_id}/proposals
- **Purpose:** List governance proposals within a Hive.
- **Path Parameter:** `hive_id` (string)
- **Query Params:** `page`, `pageSize`
- **Success Response:** `200 OK` with array of proposal summaries.

##### 3.3.11 POST /hives/{hive_id}/proposals
- **Purpose:** Submit a new governance proposal in the Hive.
- **Path Parameter:** `hive_id` (string)
- **Request Body:**
  ```json
  { "title":"...","description":"..." }
  ```
- **Success Response:** `201 Created` with proposal object.

##### 3.3.12 POST /hives/{hive_id}/proposals/{proposal_id}/vote
- **Purpose:** Cast a vote on a Hive proposal.
- **Path Parameters:** `hive_id`, `proposal_id` (strings)
- **Request Body:**
  ```json
  { "vote":"yes" | "no" | "abstain" }
  ```
- **Success Response:** `200 OK` with vote tally or confirmation.

##### 3.3.13 GET /hives/{hive_id}/treasury
- **Purpose:** View a Hive's treasury balance and transactions.
- **Path Parameter:** `hive_id` (string)
- **Success Response:** `200 OK` with JSON payload, e.g.:
  ```json
  { "balance": 1234.56, "recentTransactions":[...] }
  ```

### 3.4 Marketplace Realm (`/marketplace`)

#### A. Discovery & Browsing

##### 3.4.1 GET /marketplace/listings
- **Purpose:** Browse and search all available offers and requests.
- **Query Params:** `search` (string), `type` (`offer`|`request`), `exchange_mode` (`chrona`|`barter`|`gift`), `tags` (csv), `user_id` (string), `page`, `pageSize`
- **Success Response:** `200 OK` with paginated array of listing summaries, e.g.:
  ```json
  { "page":1, "total":100, "listings":[{ "id":"l1","type":"offer","title":"...","exchange_mode":"chrona","chrona_value":10 }, ...] }
  ```

##### 3.4.2 GET /marketplace/recommendations
- **Purpose:** Fetch personalized recommended listings from high-resonance users.
- **Success Response:** `200 OK` with array of listing summaries.

##### 3.4.3 GET /marketplace/listings/{listing_id}
- **Purpose:** Retrieve full details of a specific marketplace listing.
- **Path Parameter:** `listing_id` (string)
- **Success Response:** `200 OK` with detailed listing object, e.g.:
  ```json
  { "id":"l1","type":"offer","title":"...","description":"...","exchange_mode":"barter","barter_terms":"...","tags":["..."],"ownerId":"u1" }
  ```

#### B. Creating & Managing Listings

##### 3.4.4 POST /marketplace/listings
- **Purpose:** Create a new listing (offer or request).
- **Request Body:**
  ```json
  { "type":"offer"|"request","title":"...","description":"...","exchange_mode":"chrona","chrona_value":50,"barter_terms":"...","tags":["..."] }
  ```
- **Success Response:** `201 Created` with new listing object.

##### 3.4.5 PUT /marketplace/listings/{listing_id}
- **Purpose:** Update an existing listing.
- **Path Parameter:** `listing_id` (string)
- **Request Body:** Same as creation body.
- **Success Response:** `200 OK` with updated listing object.

##### 3.4.6 DELETE /marketplace/listings/{listing_id}
- **Purpose:** Close or delete a listing.
- **Path Parameter:** `listing_id` (string)
- **Success Response:** `204 No Content`

#### C. The Exchange Ritual

##### 3.4.7 POST /marketplace/exchanges
- **Purpose:** Initiate an exchange session for a specific listing.
- **Request Body:**
  ```json
  { "listing_id":"l1" }
  ```
- **Success Response:** `201 Created` with new exchange session object, e.g.:
  ```json
  { "exchangeId":"e1","channelId":"ch123" }
  ```

##### 3.4.8 POST /marketplace/exchanges/{exchange_id}/finalize
- **Purpose:** Finalize agreed-upon terms of an exchange (Covenant of Value).
- **Path Parameter:** `exchange_id` (string)
- **Request Body:**
  ```json
  { "final_terms":{/* ... */}, "user_affirmation":true }
  ```
- **Success Response:** `200 OK` with confirmed exchange object.

##### 3.4.9 POST /marketplace/exchanges/{exchange_id}/complete
- **Purpose:** Mark a finalized exchange as complete after delivery.
- **Path Parameter:** `exchange_id` (string)
- **Success Response:** `200 OK`

##### 3.4.10 POST /marketplace/exchanges/{exchange_id}/reflect
- **Purpose:** Leave a symbolic feedback reflection after completion.
- **Path Parameter:** `exchange_id` (string)
- **Request Body:**
  ```json
  { "value_glyphs":["Generosity","Skillfulness"], "note_of_gratitude":"Thank you!" }
  ```
- **Success Response:** `201 Created`

### 3.5 Housing Realm (`/housing`)

#### A. Discovery & Browsing Listings

##### 3.5.1 GET /housing/listings
- **Purpose:** Browse and search all available housing offers and needs.
- **Query Params:** `type` (`offer`|`need`), `location` (string), `duration` (string), `exchange_mode` (`chrona`|`barter`|`gift`), `values` (csv), `accessibility` (string), `page`, `pageSize`
- **Success Response:** `200 OK` with paginated array of listing summaries, e.g.:
  ```json
  { "page":1, "total":50, "listings":[{ "id":"h1","type":"offer","location":"CityX","duration":"2 weeks","exchange_mode":"gift" }, ...] }
  ```

##### 3.5.2 GET /housing/recommendations
- **Purpose:** Fetch personalized housing recommendations based on user value profile.
- **Success Response:** `200 OK` with array of listing summaries.

##### 3.5.3 GET /housing/listings/{listing_id}
- **Purpose:** Retrieve full details of a specific housing offer or need.
- **Path Parameter:** `listing_id` (string)
- **Success Response:** `200 OK` with detailed listing object, e.g.:
  ```json
  { "id":"h1","type":"offer","location":"CityX","duration":"2 weeks","exchange_terms":[...],"house_values":[...],"description":"..." }
  ```

#### B. Creating & Managing Listings

##### 3.5.4 POST /housing/listings
- **Purpose:** Create a new housing listing (offer or need).
- **Request Body:**
  ```json
  { "type":"offer"|"need","location":"...","duration":"...","exchange_terms":["..."],"house_values":["..."],"description":"..." }
  ```
- **Success Response:** `201 Created` with new listing object.

##### 3.5.5 PUT /housing/listings/{listing_id}
- **Purpose:** Update an existing housing listing.
- **Path Parameter:** `listing_id` (string)
- **Request Body:** Same as creation body.
- **Success Response:** `200 OK` with updated listing object.

##### 3.5.6 DELETE /housing/listings/{listing_id}
- **Purpose:** Close or delete a housing listing.
- **Path Parameter:** `listing_id` (string)
- **Success Response:** `204 No Content`

#### C. The Connection & Covenant Ritual

##### 3.5.7 POST /housing/connections
- **Purpose:** Express interest in a housing listing and initiate a connection session.
- **Request Body:**
  ```json
  { "listing_id":"h1" }
  ```
- **Success Response:** `201 Created` with connection session object, e.g.:
  ```json
  { "connectionId":"c1","chatChannelId":"ch456" }
  ```

##### 3.5.8 POST /housing/connections/{connection_id}/finalize-covenant
- **Purpose:** Confirm terms of the stay (Covenant of Shelter) by both parties.
- **Path Parameter:** `connection_id` (string)
- **Request Body:**
  ```json
  { "final_terms":{/* ... */},"user_affirmation":true }
  ```
- **Success Response:** `200 OK` with confirmed covenant object, e.g.:
  ```json
  { "covenantId":"cov123","status":"finalized" }
  ```

##### 3.5.9 POST /housing/connections/{connection_id}/complete
- **Purpose:** Mark a finalized stay as complete, enabling reflections.
- **Path Parameter:** `connection_id` (string)
- **Success Response:** `200 OK`

##### 3.5.10 POST /housing/connections/{connection_id}/reflect
- **Purpose:** Leave a symbolic reflection after a completed stay.
- **Path Parameter:** `connection_id` (string)
- **Request Body:**
  ```json
  { "value_glyphs":["Generosity","Respectful_Guest"],"note_of_gratitude":"..." }
  ```
- **Success Response:** `201 Created`

### 3.6 Travel Companion Realm (`/travel`)

#### A. Discovery & Browsing

##### 3.6.1 GET /travel/listings
- **Purpose:** Browse all active travel-related listings (plans, hospitality offers, local beacons).
- **Query Params:** `type` (`travel_plan`|`hospitality_offer`|`local_beacon`), `location` (string), `dates` (string or date range), `travel_style` (string), `page`, `pageSize`
- **Success Response:** `200 OK` with paginated array of listing summaries, e.g.:
  ```json
  { "page":1, "total":80, "listings":[{ "id":"t1","type":"travel_plan","title":"...","location":"..." }, ...] }
  ```

##### 3.6.2 GET /travel/listings/{listing_id}
- **Purpose:** Retrieve full details of a specific travel listing (plan, offer, or beacon).
- **Path Parameter:** `listing_id` (string)
- **Success Response:** `200 OK` with detailed listing object, e.g.:
  ```json
  { "id":"t1","type":"hospitality_offer","details":{ /* nested data */ } }
  ```

#### B. Creating & Managing Travel Intentions

##### 3.6.3 POST /travel/listings
- **Purpose:** Create a new travel listing (Cast a Journey, Open Hearth, Light Beacon).
- **Request Body:**
  ```json
  { "type":"travel_plan"|"hospitality_offer"|"local_beacon","details":{ /* specific fields per type */ } }
  ```
- **Success Response:** `201 Created` with new listing object.

##### 3.6.4 PUT /travel/listings/{listing_id}
- **Purpose:** Update an existing travel listing.
- **Path Parameter:** `listing_id` (string)
- **Request Body:**
  ```json
  { "details":{ /* updated fields */ } }
  ```
- **Success Response:** `200 OK` with updated listing object.

##### 3.6.5 DELETE /travel/listings/{listing_id}
- **Purpose:** Deactivate or delete a travel listing.
- **Path Parameter:** `listing_id` (string)
- **Success Response:** `204 No Content`

#### C. The Connection & Journey Ritual

##### 3.6.6 POST /travel/connections
- **Purpose:** Express interest in a travel listing and open a connection session.
- **Request Body:**
  ```json
  { "listing_id":"t1" }
  ```
- **Success Response:** `201 Created` with connection session object, e.g.:
  ```json
  { "connectionId":"tc1","channelId":"ch789" }
  ```

##### 3.6.7 POST /travel/connections/{connection_id}/finalize
- **Purpose:** Finalize arrangement terms (Pact of Passage) by both parties.
- **Path Parameter:** `connection_id` (string)
- **Request Body:**
  ```json
  { "final_terms":{/* ... */}, "user_affirmation":true }
  ```
- **Success Response:** `200 OK` with confirmed pact object, e.g.:
  ```json
  { "pactId":"p1","status":"finalized" }
  ```

##### 3.6.8 POST /travel/connections/{connection_id}/complete
- **Purpose:** Mark a journey/stay/meetup as complete.
- **Path Parameter:** `connection_id` (string)
- **Success Response:** `200 OK`

##### 3.6.9 POST /travel/connections/{connection_id}/reflect
- **Purpose:** Leave symbolic feedback after completion (Sharing the Road’s Wisdom).
- **Path Parameter:** `connection_id` (string)
- **Request Body:**
  ```json
  { "value_glyphs":["Insightful_Traveler","Generous_Host"], "note_of_gratitude":"..." }
  ```
- **Success Response:** `201 Created`

### 3.7 The Noetic Forge (`/forge`)

#### A. The Symbolic Crucible (Personal & Small Group)

##### 3.7.1 POST /forge/glyphs
- **Purpose:** Create or update a glyph or sigil for personal or group use.
- **Request Body:**
  ```json
  { "glyph_data": {/* ... */}, "intent": "...", "scope": "personal"|"group", "group_id": "..." }
  ```
- **Success Response:** `201 Created` with new glyph object, e.g.:
  ```json
  { "glyphId":"g1","scope":"personal","createdBy":"u1" }
  ```

##### 3.7.2 GET /forge/my-artifacts
- **Purpose:** Retrieve all personal artifacts: glyphs, dream-sessions, mantras.
- **Request Body:** None
- **Success Response:** `200 OK` with JSON object, e.g.:
  ```json
  { "glyphs":[/*...*/], "dreamAlchemy":[/*...*/], "mantras":[/*...*/] }
  ```

#### B. The Mythopoetic Loom (Collective Narrative)

##### 3.7.3 GET /forge/narrative-frameworks
- **Purpose:** List available narrative frameworks for new stories.
- **Request Body:** None
- **Success Response:** `200 OK` with array of frameworks.

##### 3.7.4 POST /forge/narratives
- **Purpose:** Initiate a new collective narrative.
- **Request Body:**
  ```json
  { "framework_id":"...","title":"...","initial_intent":"...","hive_id":"..." }
  ```
- **Success Response:** `201 Created` with narrative session object, e.g.:
  ```json
  { "narrativeId":"n1","frameworkId":"f1" }
  ```

##### 3.7.5 POST /forge/narratives/{narrative_id}/contribute
- **Purpose:** Add a contribution (text/symbol) to a narrative.
- **Path Parameter:** `narrative_id` (string)
- **Request Body:**
  ```json
  { "contribution_type":"text"|"symbol"|"choice","content":"..." }
  ```
- **Success Response:** `200 OK` with updated narrative state.

#### C. The Ritual Design Sanctum

##### 3.7.6 POST /forge/rituals
- **Purpose:** Initiate a new ritual design.
- **Request Body:**
  ```json
  { "title":"...","purpose":"...","intended_scope":"hive"|"platform","hive_id":"..." }
  ```
- **Success Response:** `201 Created` with ritual object, e.g.:
  ```json
  { "ritualId":"r1","status":"draft" }
  ```

##### 3.7.7 PUT /forge/rituals/{ritual_id}/steps
- **Purpose:** Define or update ritual steps, symbols, and prompts.
- **Path Parameter:** `ritual_id` (string)
- **Request Body:**
  ```json
  { "steps":[ /* array of step objects */ ] }
  ```
- **Success Response:** `200 OK` with updated ritual object.

##### 3.7.8 POST /forge/rituals/{ritual_id}/submit-for-review
- **Purpose:** Submit a completed ritual design for governance review.
- **Path Parameter:** `ritual_id` (string)
- **Request Body:** None
- **Success Response:** `202 Accepted` indicating review has started.

#### D. The Lapis Oracle (Collective Divination)

##### 3.7.9 POST /forge/oracle/inquire
- **Purpose:** Pose an inquiry to the Oracle.
- **Request Body:**
  ```json
  { "question":"...","scope":"personal"|"hive"|"platform" }
  ```
- **Success Response:** `202 Accepted` with query ID, e.g.:
  ```json
  { "queryId":"q1" }
  ```

##### 3.7.10 GET /forge/oracle/response/{query_id}
- **Purpose:** Retrieve the Oracle's symbolic response to a previous inquiry.
- **Path Parameter:** `query_id` (string)
- **Success Response:** `200 OK` with oracle response object, e.g.:
  ```json
  { "queryId":"q1","symbols":[/*...*/],"fragments":[/*...*/] }
  ```

### 3.8 Governance Realm (`/governance`)

#### A. Proposals & Deliberation

##### 3.8.1 GET /governance/proposals
- **Purpose:** Retrieve all proposals in the Agora, filtered by status, tags, or proposer.
- **Query Params:** `status` (`deliberation`|`voting`|`ratified`|`rejected`), `tags` (csv), `proposer_id` (string), `page`, `pageSize`
- **Success Response:** `200 OK` with paginated array of proposal summaries.

##### 3.8.2 GET /governance/proposals/{proposal_id}
- **Purpose:** Retrieve full details of a specific governance proposal, including text, discussion, and status.
- **Path Parameter:** `proposal_id` (string)
- **Success Response:** `200 OK` with detailed proposal object.

##### 3.8.3 POST /governance/proposals
- **Purpose:** Submit a new proposal (The Invocation).
- **Request Body:**
  ```json
  { "title": "...", "rationale": "...", "proposed_changes": {/* ... */} }
  ```
- **Success Response:** `201 Created` with new proposal object.

##### 3.8.4 POST /governance/proposals/{proposal_id}/deliberate
- **Purpose:** Add a comment or argument to a proposal's discussion.
- **Path Parameter:** `proposal_id` (string)
- **Request Body:**
  ```json
  { "comment": "...", "stance": "support" | "concern" | "question" }
  ```
- **Success Response:** `201 Created` with new comment object.

##### 3.8.5 PUT /governance/proposals/{proposal_id}
- **Purpose:** Amend a proposal during the Refinement stage.
- **Path Parameter:** `proposal_id` (string)
- **Request Body:**
  ```json
  { "updated_rationale": "...", "updated_proposed_changes": {/* ... */} }
  ```
- **Success Response:** `200 OK` with updated proposal object.

#### B. Decision-Making & Voting

##### 3.8.6 POST /governance/proposals/{proposal_id}/initiate-vote
- **Purpose:** Move a proposal from deliberation to voting stage (privileged).
- **Path Parameter:** `proposal_id` (string)
- **Success Response:** `200 OK`.

##### 3.8.7 POST /governance/proposals/{proposal_id}/vote
- **Purpose:** Cast a vote on a proposal.
- **Path Parameter:** `proposal_id` (string)
- **Request Body:**
  ```json
  { "vote_option": "yes" | "no" | "abstain", "voting_weight": 123, "rationale": "..." }
  ```
- **Success Response:** `200 OK` with confirmation of vote.

##### 3.8.8 GET /governance/proposals/{proposal_id}/results
- **Purpose:** View results of a completed vote.
- **Path Parameter:** `proposal_id` (string)
- **Success Response:** `200 OK` with vote breakdown, turnout, and final outcome.

#### C. Governance Bodies & Status

##### 3.8.9 GET /governance/councils/{council_id}
- **Purpose:** Retrieve members and mandate of a specific stewardship council.
- **Path Parameter:** `council_id` (string)
- **Success Response:** `200 OK` with council object.

##### 3.8.10 GET /governance/my-status
- **Purpose:** Check the user's status (Citizen-Initiate, Delegate, Council Member) in Governance.
- **Success Response:** `200 OK` with status object, e.g.:
  ```json
  { "is_citizen_initiate": true, "is_hive_delegate_for": ["h1","h2"], "is_council_member_of": ["ai_ethics"] }
  ```

### 3.9 Deep Realms (`/matrix`, `/veiled-matrix`)

#### A. The Matrix Realm (`/matrix`) – The Oracular Core
*Access restricted to users with the "Oracle Steward" role.*

##### 3.9.1 POST /matrix/observatory/query
- **Purpose:** Fetch complex, multi-layered data for the Symbolic Observatory visualization.
- **Request Body:**
  ```json
  { "layers": ["value_field","mythic_field"], "time_range": { "start": "...", "end": "..." } }
  ```
- **Success Response:** `200 OK` with JSON containing nodes, edges, and temporal data.

##### 3.9.2 GET /matrix/oracle/history
- **Purpose:** Retrieve paginated history of Oracle inquiries.
- **Request Body:** None
- **Success Response:** `200 OK` with array of query objects.

##### 3.9.3 GET /matrix/oracle/trace/{query_id}
- **Purpose:** Get detailed data trace for a specific Oracle response.
- **Path Parameter:** `query_id` (string)
- **Success Response:** `200 OK` with `DataTraceability` graph object.

##### 3.9.4 POST /matrix/scrying/simulate
- **Purpose:** Initiate a governance proposal impact simulation (Algorithmic Scrying).
- **Request Body:**
  ```json
  { "proposal_id": "...", "simulation_parameters": {/* ... */} }
  ```
- **Success Response:** `202 Accepted` with `{ "simulation_id": "..." }`.

##### 3.9.5 GET /matrix/scrying/results/{simulation_id}
- **Purpose:** Fetch results of a completed simulation.
- **Path Parameter:** `simulation_id` (string)
- **Success Response:** `200 OK` with detailed results object (visualizations, AI-generated parables).

#### B. The Veiled Matrix (`/veiled-matrix`) – The Symbolic Kernel
*Access restricted to First Circle during Kernel Sealing Ritual; multi-signature consent enforced.*

##### 3.9.6 GET /veiled-matrix/kernel/parameters
- **Purpose:** View current core constitutional parameters of the Symbolic Kernel.
- **Request Body:** None
- **Success Response:** `200 OK` with read-only kernel state object.

##### 3.9.7 POST /veiled-matrix/kernel/propose-amendment
- **Purpose:** Stage a proposed change to a kernel parameter for unanimous consent.
- **Request Body:**
  ```json
  { "parameter_to_change": "...", "new_value": "...", "impact_statement_id": "...", "simulation_results_id": "..." }
  ```
- **Success Response:** `202 Accepted` with `{ "amendment_id": "..." }`.

##### 3.9.8 POST /veiled-matrix/kernel/affirm-amendment/{amendment_id}
- **Purpose:** Cast a binding affirmation vote for a staged kernel amendment.
- **Path Parameter:** `amendment_id` (string)
- **Request Body:** None
- **Success Response:** `200 OK` once all required affirmations complete triggers kernel sealing.
