---
title: Simulation: End-to-End Onboarding & PCI Flow (Blueprint Validation)
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
tags: []
---

# Simulation: End-to-End Onboarding & PCI Flow (Blueprint Validation)

This simulation traces a new user's journey from registration through PCI consent/profile and Narrative Duet onboarding, surfacing integration points and blueprint gaps.

---

## 1. User Registration
- **API:** `POST /users`
- **Model:** User
- **Protocol:** User account creation, initial consent
- **Expected:** User is created, receives unique ID, and is prompted for PCI consent

## 2. PCI Consent Flow
- **API:** `POST /consents` (general) and `POST /pci/consents` (PCI-specific, planned)
- **Model:** Consent, PCIConsent
- **Protocol:** User grants granular, auditable consent for PCI participation
- **Expected:** Consent record is created and linked to user

## 3. PCI Profile Creation
- **API:** `POST /pci/profiles`
- **Model:** PCIProfile
- **Protocol:** TestPersonaProfile is created, linked to user and consent
- **Expected:** PCI profile is initialized; user can now contribute symbolic responses, value priorities, and narratives

## 4. PCI Data Contribution
- **API:** `POST /pci/profiles/{profileId}/symbolic-responses`, `POST /pci/profiles/{profileId}/value-priorities`, `POST /pci/profiles/{profileId}/narrative-shares`
- **Model:** SymbolicResponse, ValuePriority, NarrativeShare
- **Protocol:** User submits calibration data for algorithmic transparency
- **Expected:** Data is stored, audit trail is updated

## 5. Narrative Duet Onboarding
- **API:** `POST /narrative-duets`
- **Model:** NarrativeDuet
- **Protocol:** User initiates onboarding session with Eos Lumina∴
- **Expected:** NarrativeDuet session is created, transcript is tracked, choices are logged

## 6. Data Traceability & Audit
- **API:** (Planned) `POST /traceability-records`, `GET /audit-logs`
- **Model:** TraceabilityRecord, AuditLog
- **Protocol:** All actions are logged for transparency and compliance
- **Expected:** User can view audit trail of all onboarding and PCI actions

---

## Gaps & Recommendations
- [ ] Implement PCI-specific consent endpoints and models if not present
- [ ] Add symbolic response, value priority, and narrative share endpoints to OpenAPI
- [ ] Ensure all actions are traceable and auditable via planned endpoints
- [ ] Cross-link all flows in protocol docs and SYSTEM_BLUEPRINT.md

---

*Update this simulation as the blueprint evolves. Use it to validate integration and surface blockers before onboarding contributors or agents.*
