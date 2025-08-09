---
title: Chrona - The Currency of Time
version: 1.1.0
status: Ratified Foundational Text
last_updated: 2025-06-22
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
tags:
- chrona
- economics
- postcapitalist
- time_currency
- governance
- digital_citizenship
---

# Chrona: The Currency of Time

## 1. Core Principle: Rewarding Presence, Not Just Production

Chrona is a time-based currency system designed to recognize and reward the intrinsic value of human presence, attention, and contribution within the ThinkAlike ecosystem. It fundamentally decouples reward from traditional metrics of output or productivity.

Instead of earning for *what* you produce, you earn Chrona for the *time* you consciously contribute. This includes time spent in reflection, in dialogue, in ritual, in governance, and in creative expression.

## 2. Features

- **Time Ledger:** A secure, transparent ledger logs hours contributed. This can be done through active session tracking or manual, verified logging for offline contributions.
- **Hour Tokens (Chrona):** For every verified hour of contribution, a user earns one Chrona token. These tokens are non-transferable for fiat currency.
- **Utility & Redemption:** Chrona can be used to:
    - Propose and vote on platform features and governance issues.
    - Gift to other users as a sign of recognition and appreciation.
    - Access special platform privileges, roles, or cosmetic features.
    - Steward swarms or moderate community spaces.
- **Digital Citizenship:** Sustained engagement and Chrona accumulation unlock levels of digital citizenship. Citizens gain greater rights and responsibilities within the ecosystem's governance.
- **Weighted Governance:** While Chrona grants voting power, the system is not a pure plutocracy. Proposal and voting influence is weighted by a combination of Chrona holdings, engagement diversity, and peer-verified reputation to prevent power concentration.

## 3. API & Data Model

- **Core Models:** `TimeLedger`, `ChronaToken`, `GovernanceProposal`, `VoteRecord`, `CitizenProfile`
- **Key Endpoints:**
    - `GET /chrona/ledger`: View personal time ledger.
    - `POST /chrona/log`: Log or verify contributed time.
    - `GET /chrona/balance`: View current Chrona balance.
    - `POST /chrona/gift`: Gift Chrona to another user.
    - `GET /governance/proposals`: View active and past proposals.
    - `POST /governance/proposals`: Create a new proposal (requires Chrona).
    - `POST /governance/vote`: Vote on an active proposal.

## 4. Security & Ethical Considerations

- **Non-Commodification:** Chrona is explicitly forbidden from being traded on external exchanges or for fiat currency. It is a currency of reputation and influence *within* the ecosystem only.
- **Transparency:** All governance actions, proposals, and vote counts are public and auditable.
- **Voluntary Participation:** All aspects of the Chrona system are opt-in. Users can fully participate in ThinkAlike without engaging with the governance layer.
- **Revocability:** Citizenship and its associated responsibilities can be revoked by the user at any time.

## 5. Example User Flow

1.  A contributor spends two hours participating in a facilitated group reflection ritual.
2.  The session time is automatically logged to their Time Ledger, and they earn 2 Chrona.
3.  They see a governance proposal they support for a new accessibility feature.
4.  They use 1 Chrona to cast their vote in favor of the proposal, amplifying their voice in the platform's evolution.
