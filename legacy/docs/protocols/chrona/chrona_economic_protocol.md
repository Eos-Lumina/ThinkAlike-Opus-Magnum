---
title: Chrona Economic Protocol
version: 3.0.0
status: Canonical
maintainer: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
last_updated: 2024-07-22
authors:
  - The Chrona Stewards∴
tags:
  - protocol
  - economic
  - chrona
  - parecon
  - post-capitalism
  - ubi
  - pet
related_docs:
  - "[[../../docs/realms/governance/governance_specification.md|governance_specification]]"
  - "[[../../docs/realms/hives/hives_specification.md|hives_specification]]"
  - "[[../economic/chrona_wallet_protocol.md|chrona_wallet_protocol]]"
  - "[[../economic/contributor_recognition_protocol.md|contributor_recognition_protocol]]"
  - "[[../../docs/realms/marketplace/marketplace_specification.md|marketplace_specification]]"
canonical_data_models: "[[canonical_data_models]]"
api_spec: "[[openapi_master_specification]]"
---

# Chrona Economic Protocol

## 1. Core Philosophy: The Currency of Being

Chrona (⧖) is not money. It is the symbolic representation of sacred time, creative energy, and meaningful contributions to the commons. It is a medium of exchange and a tool for acknowledging and facilitating the flow of value in a post-capitalist context, designed to be non-extractive and fundamentally aligned with the well-being of the collective.

**Core Principles:**

*   **Non-Extractive:** Chrona cannot be hoarded for speculative gain or used to exert coercive power. Its value is in its flow and its application toward pro-social ends.
*   **Holistic Value:** The protocol recognizes and rewards a wide spectrum of contributions, including creative work, emotional labor, community stewardship, resource sharing, knowledge creation, and ecological regeneration.
*   **Time-Based Foundation:** Rooted in the principle that an individual's focused time and life-energy are a fundamental source of value.
*   **Gift & Reciprocity:** Blends gift economy principles with a transparent, equitable, and consensual system of exchange.

## 2. Chrona Generation & Flow (The Wellspring)

Chrona enters circulation through transparent and governed mechanisms.

*   **Universal Basic Income (UBI):** A foundational stream of Chrona is regularly generated and distributed to all verified members of the collective. The initial parameters, distribution frequency, and adjustment mechanisms are determined and evolved through the [[governance_specification|Governance Protocol]].
*   **Earning via Contribution:** Agents earn Chrona through active participation and value creation:
    *   **Quests & Bounties:** Completing tasks defined in realm-specific or system-wide roadmaps.
    *   **Recognition & Endorsement:** Receiving "Echoes" or other forms of recognition via the [[contributor_recognition_protocol|Contributor Recognition Protocol]].
    *   **Marketplace Exchange:** Providing goods, services, or creative works in the [[marketplace_specification|Marketplace]].
    *   **Realm-Specific Roles:** Fulfilling roles such as hosting in the Housing realm, facilitating rituals within Hives, or guiding experiences in the Travel realm.
*   **Circulation Incentive (Formerly "Decay"):** To encourage active participation and prevent stagnation, hoarded or inactive Chrona may be subject to a "demurrage" or circulation charge. This is a collectively managed parameter designed to keep value flowing through the ecosystem, not to punish individuals.

## 3. The Marketplace Realm

The Marketplace is the primary hub for the exchange of goods and services using Chrona.

*   **Purpose:** An interface for agents and Hives to post and discover offers for goods, services, skills, or creative works. Exchanges can be valued in Chrona, offered as gifts, or arranged through barter.
*   **Listings:** Utilize standardized `Card` components, featuring clear descriptions, the proposed Chrona value, and the agent's `ProfileBadge` to build trust and provide context.
*   **Discovery:** Agents can find offers through semantic search, category filters, and resonance-based recommendations powered by the [[resonance_network_specification|Resonance Network]].
*   **Transaction Ritual:** The process of accepting an offer, transferring Chrona via the [[chrona_wallet_protocol|Chrona Wallet]], and confirming completion is designed as a consensual, transparent, and auditable ritual.

## 4. The Chrona Wallet

The Chrona Wallet is the agent's personal interface for managing their economic activity within the ThinkAlike ecosystem.

*   **Functionality:** View balance, review detailed transaction history, send/receive Chrona, and manage recurring payments or contributions.
*   **Specification:** For a detailed technical breakdown, see the **[[chrona_wallet_protocol]]**.

## 5. Integration with Core Realms & Protocols

The Chrona Economic Protocol is deeply interwoven with the entire ThinkAlike architecture.

| Realm / Protocol                               | Integration Point                                                                                                                            |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **[[governance_specification]]**               | Economic parameters (UBI rate, circulation charge, etc.) are proposed, debated, and ratified through the governance process.                   |
| **[[hives_specification]]**                    | Hives manage collective treasuries, fund internal projects, and can distribute Chrona to members based on their own internal governance.         |
| **[[housing_specification]]**                  | Chrona is used for rental agreements, service exchanges, and contributions to a household's shared resources.                                  |
| **[[jobs_and_services_specification]]**        | The primary protocol for defining work, setting bounties, and rewarding the completion of tasks with Chrona.                                   |
| **[[contributor_recognition_protocol]]**       | Provides a non-monetary layer of value recognition that can be correlated with Chrona grants from community-stewarded funds.                  |
| **[[noetic_forge_specification]]**             | Exceptional contributions to the collective's knowledge base or creative output can be recognized with significant Chrona grants.              |

## 6. Economic Governance & Participatory Economics (Parecon)

The economic model is subject to continuous, democratic oversight.

*   **Parameter Adjustment:** Key economic levers are not fixed but are adjustable via community governance to ensure the system remains fair, stable, and aligned with collective values.
*   **Equitable by Design:** The system is designed to prevent extreme wealth disparity and ensure that all participants have access to the resources they need to thrive. The integration of Parecon principles informs the valuation of different forms of labor.

## 7. Privacy, Ethics, and Transparency (PET)

*   **Traceability & Anonymity:** All transactions are recorded on a distributed ledger for integrity and auditability. Public views of the ledger are pseudonymized to protect individual privacy, while agents have full, unredacted access to their own transaction history.
*   **Fairness & Access:** The UBI and the broad definition of "valuable contribution" are designed to promote equity and accessibility for all members.
*   **Discouraging Speculation:** The combination of the circulation incentive and the non-transferability of Chrona outside the system is designed to mitigate speculative behavior and financialization.
