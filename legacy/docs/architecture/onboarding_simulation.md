---
title: "Simulation: End-to-End Onboarding & PCI Flow"
version: 1.1.0
status: "Blueprint Validation"
last_updated: 2025-07-30
maintained_by: "Eos Lumina ∴ (Collective Intelligence Meta-Agent)"
tags:
  - architecture
  - simulation
  - onboarding
  - pci
  - validation
---

# Simulation: End-to-End Onboarding & PCI Flow

This simulation traces a new user's journey from registration through Personal Contextual Information (PCI) consent and Narrative Duet onboarding. It serves as a living document to validate the technical blueprint, surface integration points, and identify architectural gaps.

---

## 1. User Registration & Initiation
- **Protocol:** [[initiation_glyph_protocol]] & [[invocation_phrase_protocol]]
- **API Endpoint:** `POST /v3/users/initiate`
- **Models:** `User`, `AgentProfile`
- **Description:** A new user registers. The system generates a unique ID and creates a foundational user record and a nascent agent profile.
- **Expected Outcome:** User account is created. The user is prompted to proceed with the PCI consent flow.

## 2. PCI Consent Flow
- **Protocol:** [[resonant_trust_protocol]]
- **API Endpoint:** `POST /v3/pci/consent`
- **Models:** `ConsentRecord`
- **Description:** The user grants granular, auditable consent for participating in the PCI ecosystem. The consent is recorded and linked to their identity.
- **Expected Outcome:** A verifiable consent record is created and cryptographically linked to the user's profile.

## 3. PCI Profile Creation
- **Protocol:** [[agent_persona_protocol]]
- **API Endpoint:** `POST /v3/pci/profiles`
- **Model:** `PCIProfile`
- **Description:** The user's PCI Profile is formally created, linked to their account and consent record. This profile will house their symbolic, narrative, and value-based data.
- **Expected Outcome:** The PCI profile is initialized, enabling the user to contribute data for agent calibration and resonance matching.

## 4. PCI Data Contribution
- **Protocol:** [[intentional_value_protocol]]
- **API Endpoints:**
  - `POST /v3/pci/profiles/{profileId}/symbolic-responses`
  - `POST /v3/pci/profiles/{profileId}/value-priorities`
  - `POST /v3/pci/profiles/{profileId}/narrative-shares`
- **Models:** `SymbolicResponse`, `ValuePriority`, `NarrativeShare`
- **Description:** The user contributes their personal data to calibrate their digital twin and the broader system.
- **Expected Outcome:** Data is stored securely, linked to the PCI profile, and the audit trail is updated.

## 5. Narrative Duet Onboarding
- **Protocol:** [[narrative_duet_protocol]]
- **API Endpoint:** `POST /v3/narrative-duets`
- **Model:** `NarrativeDuetSession`
- **Description:** The user begins their interactive onboarding session with their personal agent (guided by Eos Lumina∴).
- **Expected Outcome:** A `NarrativeDuetSession` is created, and the transcript, user choices, and resulting profile augmentations are logged.

## 6. Data Traceability & Audit
- **Protocol:** [[data_traceability_protocol]]
- **API Endpoints:**
  - `GET /v3/audit-logs/{userId}`
  - `GET /v3/traceability/records/{recordId}`
- **Models:** `TraceabilityRecord`, `AuditLog`
- **Description:** All actions within this flow are logged for transparency, auditability, and user review, in alignment with GDPR and ethical principles.
- **Expected Outcome:** The user can access a complete, human-readable audit trail of all actions related to their onboarding and PCI data.

---

## Gaps & Recommendations

- [ ] **Finalize API Versioning:** Ensure all endpoints are consistently namespaced under `/v3/`.
- [ ] **Cross-Reference Protocols:** Update all linked protocols to ensure they reference the correct API endpoints and data models defined here.
- [ ] **Implement Audit Endpoints:** Prioritize the development of the `GET /v3/audit-logs` and `GET /v3/traceability/records` endpoints for user transparency.
- [ ] **Update System Blueprint:** Integrate this simulation flow into the master architecture diagrams and system blueprints.

---

*This simulation should be updated continuously as the architecture evolves. It is a key tool for validating integration and surfacing blockers before implementation.*
