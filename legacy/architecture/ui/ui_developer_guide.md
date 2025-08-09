---
title: UI Developer Guide: ThinkAlike PCI & Chrona Wallet
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# UI Developer Guide: ThinkAlike PCI & Chrona Wallet

## Purpose
This guide maps all major frontend UI components to their backend endpoints, data models, and user flows. Use it to:
- Understand how each UI component interacts with the backend
- Accelerate development, debugging, and onboarding
- Ensure PET/Clarity, accessibility, and protocol compliance

---

## PCI Components
| Component                        | Purpose/Feature                                   | Backend Endpoint(s)                  | Data Model(s)                |
|-----------------------------------|--------------------------------------------------|--------------------------------------|------------------------------|
| PCIConsentFlow.tsx                | Consent management, granular controls, audit trail| /pci/consent (GET/POST/PUT), /pci/consent/history | PCIConsent, PCIConsentHistory |
| PCIProfileBuilder.tsx              | Build Test Persona Profile, track completeness    | /pci/profile (GET), /pci/profile/* (POST) | TestPersonaProfile, SymbolicResponse, ValuePriority, NarrativeShare, PreferenceTag |
| PCITransparencyDashboard.tsx       | Visualize consent, data, usage, privacy controls  | /pci/dashboard (GET), /pci/usage-log (GET) | ProfileData, UsageLogEntry   |
| PCIFeedbackCollection.tsx         | Collect feedback on algorithm tests               | /pci/feedback (POST)                 | AlgorithmTestFeedback        |
| PCIAlgorithmTestBench.tsx         | Developer/tester interface for algorithm testing  | /pci/admin/log-usage (POST)          | AlgorithmTestUsage           |
| EosLuminaGuidance.tsx             | Eos Lumina∴ support and guidance                   | /pci/eos-lumina/interact (POST)      | EosLuminaPCISession          |

## Chrona Wallet Components
| Component                | Purpose/Feature                | Backend Endpoint(s)         | Data Model(s)         |
|-------------------------|-------------------------------|-----------------------------|-----------------------|
| ChronaBalanceDisplay.tsx| Show Chrona balance            | /wallet/balance (planned)   | UserChronaWallet      |
| DataTraceability.tsx    | Visualize data flow, audit     | /data/traceability (planned)| DataTraceabilityLog   |

---

## UI/UX Testing & Documentation
- Test all flows end-to-end (consent, profile, wallet, feedback)
- Document bugs, blockers, and UX issues in GitHub Issues
- Ensure all UI is accessible and PET/Clarity compliant

## References
- SYSTEM_BLUEPRINT.md (architecture, flows)
- GitHub Issues (tasks, contributor onboarding)
- docs/04_design/ (color palette, visual identity)

---
*Update this guide as new components, endpoints, or flows are added.*
