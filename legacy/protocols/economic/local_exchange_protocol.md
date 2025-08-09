---
title: "Local Exchange Protocol"
version: 3.0.0
status: Canonical
last_updated: 2025-07-08
authors:
  - "Eos Lumina ∴ (Collective Intelligence Meta-Agent)"
tags: [protocol, economic, exchange, services, jobs, community, chrona, mutual_aid, localism]
spec_for: [Realms, Hives, Agents]
related_docs:
  - /protocols/economic/chrona_wallet_protocol.md
  - /protocols/economic/intentional_value_protocol.md
  - /protocols/core/resonance_matching_protocol.md
  - /protocols/governance/restorative_justice_protocol.md
harmonization_note: |
  This protocol canonicalizes the legacy "Local Exchange Module" into a formal, implementation-ready specification. It defines a framework for ethical, consent-based, and community-governed exchange of services, skills, and goods, replacing exploitative gig economy models with a system of mutual aid and resonant connection.
---

# ⚖️ Local Exchange Protocol

## 1. Preamble: The Marketplace as a Sanctuary

The dominant economic paradigm reduces human interaction to raw, often exploitative, transactions. The "gig economy" promised flexibility but delivered precarity. The Local Exchange Protocol reclaims the marketplace as a sanctuary for community connection, mutual support, and the recognition of diverse forms of value.

This protocol provides a decentralized framework for individuals and Hives (community pods) to offer, request, and collaborate on services, projects, and resource sharing. It is built on principles of transparency, consent, and resonance, ensuring that exchanges strengthen the community fabric rather than fraying it.

## 2. Core Principles

- **Mutual Aid:** The system is designed to facilitate mutual support, not just one-way transactions.
- **Resonance over Proximity:** While local, the primary matching vector is shared values, skills, and needs (Resonance), not just geography.
- **Value Pluralism:** Compensation is flexible, supporting Chrona, barter, mutual credit, or acts of pure goodwill. Value is co-defined by participants.
- **Data Sovereignty:** Participants own their data. Reputational data is portable and managed via the `Resonant Trust Protocol`.
- **Forkable Governance:** Communities (Hives) can fork and adapt the rules of their local exchange to suit their specific cultural and economic needs.

## 3. Protocol Specification

### 3.1. Exchange Listings

Listings are the core objects of the protocol and can be of three types:

-   **`Offer`**: A user offers a skill, service, or resource (e.g., "I can offer 2 hours of graphic design").
-   **`Request`**: A user requests a skill, service, or resource (e.g., "I need help setting up a community garden").
-   **`Collaboration`**: A user proposes a project seeking multiple participants (e.g., "Let's form a team to build a local mesh network").

Each listing must contain:
-   `type`: (Offer, Request, Collaboration)
-   `title`: A clear, concise summary.
-   `description`: Detailed explanation, including scope and expectations.
-   `tags`: Keywords for discoverability (e.g., `skill:carpentry`, `project:art`, `need:childcare`).
-   `compensationModel`: An array specifying accepted forms of value (e.g., `[chrona, barter, mutual_credit, gift]`).
-   `commitment`: Expected duration or effort (e.g., hours, project-based).
-   `visibility`: (Public, Hive-only, Trusted-Peers).

### 3.2. Resonance-Based Matching

Instead of a simple search, the system uses the `Resonance Matching Protocol` to connect listings with participants. The matching algorithm considers:

-   **Skill & Interest Alignment:** Matching `tags` and profile data.
-   **Value Alignment:** Matching `compensationModel` preferences.
-   **Reputation & Trust:** Leveraging data from the `Resonant Trust Protocol`.
-   **Hive Affiliation:** Prioritizing connections within a user's chosen communities.

### 3.3. Engagement & Agreement

1.  **Signal of Interest**: A user expresses interest in a listing.
2.  **Harmonization Phase**: The participants engage in a dialogue (via a secure, end-to-end encrypted channel) to clarify scope, expectations, and compensation.
3.  **Agreement Glyph**: A formal agreement is created by mutual consent, generating a cryptographic "Agreement Glyph." This is a verifiable, timestamped record of the agreed-upon terms, stored on the participants' respective data ledgers. It is not a rigid "contract" but a record of shared intention.

### 3.4. Value Exchange & Recognition

-   **Chrona Transactions**: If Chrona is used, the exchange is handled via the `Chrona Wallet Protocol`.
-   **Barter & Mutual Credit**: The system provides a ledger to track non-monetary exchanges.
-   **Recognition**: Upon completion, participants can exchange "Recognition Glyphs," which are non-fungible attestations that contribute to their reputation within the `Resonant Trust Protocol`.

## 4. Governance

-   **Service Categories**: Each Hive can define and manage its own taxonomy of valid service tags and categories.
-   **Dispute Resolution**: Conflicts are handled through the `Restorative Justice Protocol`, prioritizing mediation and community-led resolution over punitive measures.
-   **Protocol Forking**: Hives have the right to fork this protocol to create their own localized exchange rules, promoting a polycentric and adaptive economic ecosystem.

## 5. Integration with Core Systems

-   **Identity & Reputation**: `Resonant Trust Protocol` and `Sovereign Stack Protocol`.
-   **Economic Layer**: `Chrona Wallet Protocol`, `Intentional Value Protocol`.
-   **Matching**: `Resonance Matching Protocol`.
-   **Social Layer**: Integrated into Hive dashboards and user profiles.

## 6. Vision: An Economy of Gifts

The Local Exchange Protocol is a foundational component of a regenerative economic model. It is a step towards an "economy of gifts," where the act of exchange is an opportunity for connection, and the wealth of a community is measured by the strength of its relationships, not the volume of its transactions.
