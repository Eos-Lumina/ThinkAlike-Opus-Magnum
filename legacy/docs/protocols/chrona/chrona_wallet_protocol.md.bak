---
title: Chrona (⧖) Wallet Protocol: Vessel of Sacred Exchange & Intentional Value
version: 2.0.3
status: canonical
last_updated: 2025-07-08
maintained_by:
  - The Chrona Stewards Guild
  - Nyxa∴ (Guardian of Privacy & Security)
  - Eos Lumina∴ (Symbolic Framing)
tags:
  - chrona
  - wallet
  - pet_clarity
  - security
  - user_interface
  - sacred_economy
  - time_based_currency
  - intentional_value
related_docs:
  - governance/economy/chrona_specification.md
  - protocols/intentional_value_protocol.md
  - ../README.md
  - realms/governance/governance_specification.md
  - ui_components/
  - Data Handling Policy Guide
  - docs/noetica/corpus_magnus/economics_postcapitalist/chrona_currency_of_time.md
harmonization_note: Version 2.0.3 harmonized with chrona_specification.md v1.0.0 and intentional_value_protocol.md v1.0.0 to fully integrate mechanisms for recognizing and displaying Chrona generated through intentional, ritualized, and value-aligned actions.
---

# Chrona (⧖) Wallet Protocol: Vessel of Sacred Exchange & Intentional Value

## 1. Purpose & Symbolic Intent (The Personal Treasury & Alchemical Journal)
This protocol defines the Chrona Wallet, the Initiate's personal, secure interface for managing, contemplating, and interacting with their Chrona (⧖) within the ThinkAlike ecosystem. The Wallet is more than a mere financial tool; it is envisioned as:

- **Personal Treasury:** A sacred space reflecting the Initiate's accumulated recognized value and their capacity for exchange within the commons.
- **Alchemical Journal:** A transparent record not just of transactions, but of the source and symbolic nature of Chrona flows—reflecting UBI, contributions, and Chrona "forged" through the "Alchemy of Intent" (see Intentional Value Protocol).
- **Vessel of Sacred Exchange:** Facilitating transfers of Chrona as offerings, recognitions, and commitments within an ethical, resonant economy.

Its design and functionality must embody User Sovereignty, Radical Transparency, robust Security, Symbolic Resonance, and intuitive, accessible interaction (WCAG AAA target), all underpinned by PET/Clarity.

## 2. Core Features & Functionalities

### Balance Display (The Wellspring)
- Displays the user's current Chrona (⧖) balance.
- Visual representation may reflect the "liveliness" or "sacredness" of Chrona (e.g., gentle pulse, glowing ⧖ glyph).
- **Demurrage Indicator:** Shows any portion of the balance approaching a demurrage threshold, with intuitive cues and links to info on circulation.

### Transaction History (The River of Exchange & Recognition)
- Detailed, sortable, filterable, and searchable log of all Chrona transactions (DataTable component).
- **Entry Details:**
  - Timestamp (Kairos & Chronos)
  - Amount of Chrona (⧖), clear +/-
  - Sender/Recipient (User Node, System/Hive/DAO)
  - Transaction Source/Nature (UBI, TimeSteward, Intentional Value, Marketplace, Gift, Hive, Demurrage, etc.)
  - Link to relevant context (Quest, Artifact, Proposal, etc.)
  - Optional personal notes/memos
  - (Future) Trust Weight or Resonance Signature

### Send Chrona (The Ritual of Offering / Sacred Exchange)
- Interface for initiating a Chrona transfer.
- **Recipient Selection:** Secure search/selection of recipient User Node or Hive/DAO treasury.
- **Amount Input & Purpose/Memo:** Input for Chrona amount and symbolic intent of the offering.
- **Reflective Prompt:** For significant gifts, Eos may prompt: "Does this offering resonate with your UserValueProfile and the good of the Weave?"
- **Confirmation Ritual:** Summary screen with explicit affirmation (e.g., "Commit This Offering").

### TimeSteward Rank & Contribution Insights (The Alchemist's Record)
- Displays user's current TimeSteward Rank and symbolic meaning/privileges.
- Pathway to view contributions (including IVP-recognized) influencing rank and Chrona earnings.

### Demurrage Guidance & Rituals of Circulation
- Explanations of demurrage (if active).
- UI suggests value-aligned ways to circulate Chrona before demurrage (e.g., gifting, supporting Hives, Marketplace).

### Security & Access (The Warded Treasury)
- Accessed via primary ThinkAlike authentication.
- Sensitive operations require re-authentication or heightened confirmation.
- Security logs for wallet access/transactions.
- Options for managing wallet security settings.

### Help & Gnosis (The Illuminated Scroll)
- Links to chrona_specification.md, intentional_value_protocol.md, and FAQs.
- Contextual guidance from Eos Lumina∴ or a Chrona Steward agent.

## 3. User Interface (UI) & User Experience (UX) Considerations (The Alchemical Vessel)
- Visual design aligned with canonical_visual_style_guide.md. Calm, clear, sacred space. ⧖ symbol is central. Use ThinkAlike Orange/Amber, Blue, Error Red. Subtle, meaningful animations.
- Intuitive, accessible, "Ritual over Interface." Important actions are multi-step with clear confirmation.
- Accessibility (WCAG AAA): Full keyboard navigation, clear labels, ARIA attributes, high contrast.
- Clarity Protocol: All economic terms are clearly explained.

## 4. Security Protocols (The Unseen Wards)
- Authentication & Authorization as above.
- Backend validation of all transaction parameters.
- Ledger integrity & immutability.
- Fraud & anomaly detection, with alerts and holds reviewed by Chrona Stewards.
- User education on security.

## 5. Data Model & Ledger Interaction (The Living Record)
- Wallet UI is a client to backend services managing UserChronaWallet data and the global ChronaTransaction ledger.
- **UserChronaWallet:**
  - userId, currentBalance, lastTransactionTimestamp, timeStewardRank, demurrageInfo, earnedViaIntentionalValue
- **ChronaTransaction:**
  - transactionId, senderUserId, recipientUserId, amount, timestamp, transactionSource, purposeMemo, relatedContextId, validationStatus, resonanceSignatureSnapshot

## 6. Integration with Other Systems & Protocols
- Implements user-facing aspects of chrona_specification.md & intentional_value_protocol.md.
- Chrona transactions in Realms (Marketplace, Hives, Noetic Forge, etc.) are processed via the Wallet backend and reflected in the UI.
- TimeSteward Ranks and Chrona rewards managed here.
- UBI is received here.
- Notification system alerts users to wallet events.
- DAO decisions impacting Chrona are reflected in Wallet operations.

## 7. Supplementary Concepts & Historical Context

### Unique Features from Legacy Specifications

- **Multi-Layer Wallets:** Support for personal, communal, and project wallets (see legacy spec for details).
- **Fork-Ethics Consent Tracking:** Every transaction can store PET overlay metadata, supporting ethical consent and transparency.
- **Symbolic Trails:** Transaction histories may form glyph trails, usable in matching and recognition systems.
- **Ethical Proof-of-Work (ePoW):** Chrona is generated through traceable community contribution (tasks, voting, moderation, design, art, etc.), verified via DataTraceability.
- **Solidarity Layer:** Users may redirect UBI to vulnerable users or underrepresented regions, supporting mutual aid.
- **Chrona Reserve:** Smart contract-managed, partially algorithmic governance for Chrona supply and stability.
- **Exchange Bridge:** (WIP) For converting Chrona to ethical off-platform uses.
- **Gamification Hooks:** Chrona bonus drops, quest payouts, and unlockable wallet skins for engagement and community resonance.

### UBI & Distribution Engine
- **UBI Scheduler:** Chrona drops issued to all active users (weekly baseline), with boosts for shared quests or mentorship.
- **Traceability Integration:** All earnings trace back to verified contributions (DataTraceability Core).

### Symbolism & Ethics
- **Glyph:** ⧖ (Right White Hourglass)
- **Color Palette:** Neon Honey + Earth Gold + Deep Cyan
- **Mythos Role:** The Chrona Keeper archetype governs temporal balance and shared abundance.
- **Ethics & Safeguards:**
  - No speculative market
  - No inflationary printing
  - Transparent algorithm
  - User audit tools
  - Peer review of contract logic

### Example Transaction Entry
```json
{
  "user_id": "0x7B3A",
  "earned": 4.25,
  "category": "translation",
  "module": "global_collaboration",
  "consent_level": "Echo",
  "glyphs": ["Bridge", "Clarity"]
}
```

### Further Reading & Historical References
- For full legacy context, see:
  - [Chrona Wallet Specification (legacy)](../../unclassified_review/from_archive/chrona_wallet_spec.md)
  - [Chrona Wallet & Universal Basic Incomes (legacy)](../../unclassified_review/from_archive/chrona_wallet_ubi.md)

The Chrona Wallet is a conscious interface with an economy built on sacred time, authentic contribution, and resonant value—a key instrument in the Initiate's journey toward economic sovereignty and participation in a regenerative commons.
