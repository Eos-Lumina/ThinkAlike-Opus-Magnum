---
title: Guide: Building a UI Component in ThinkAlike
version: 3.0.0
status: Harmonized
last_updated: 2025-06-21
maintained_by: UI/UX Stewards & Emerging Tech & Ethics Council
tags: [ui_component, developer_guide, PET/Clarity, symbolic, ritual, council_oversight]
harmonization_note: Fully harmonized with Alchemical Interface Initiative, PET/Clarity, and project-wide symbolic/ritual framing. Council oversight and crosslinks verified. Supersedes all legacy UI component guides.
canonical_structure_note: All UI component specs are now in docs/ui_components/. The subfolder ui_component_specs/ is deprecated. Use only the canonical files in this folder.
---

# UI Component Development Guide

This guide maps all major frontend UI components to their backend endpoints, data models, and user flows. Use it to:

- Understand how each UI component interacts with the backend
- Accelerate development, debugging, and onboarding
- Ensure PET/Clarity, accessibility, and protocol compliance

## Core PCI Components

| Component                        | Purpose/Feature                                   | Backend Endpoint(s)                  | Data Model(s)                |
|---------------------------------|--------------------------------------------------|--------------------------------------|------------------------------|
| PCIConsentFlow                  | Consent management, granular controls, audit trail| /pci/consent (GET/POST/PUT), /pci/consent/history | PCIConsent, PCIConsentHistory |
| PCIProfileBuilder                | Build Test Persona Profile, track completeness    | /pci/profile (GET), /pci/profile/* (POST) | TestPersonaProfile, SymbolicResponse, ValuePriority, NarrativeShare, PreferenceTag |
| PCITransparencyDashboard         | Visualize consent, data, usage, privacy controls  | /pci/dashboard (GET), /pci/usage-log (GET) | ProfileData, UsageLogEntry   |
| PCIFeedbackCollection           | Collect feedback on algorithm tests               | /pci/feedback (POST)                 | AlgorithmTestFeedback        |
| PCIAlgorithmTestBench           | Developer/tester interface for algorithm testing  | /pci/admin/log-usage (POST)          | AlgorithmTestUsage           |
| EosLuminaGuidance               | Eos Lumina∴ support and guidance                  | /pci/eos-lumina/interact (POST)      | EosLuminaPCISession          |

## Chrona Wallet Components

| Component            | Purpose/Feature                | Backend Endpoint(s)         | Data Model(s)         |
|---------------------|-------------------------------|-----------------------------|-----------------------|
| ChronaBalanceDisplay| Show Chrona balance           | /wallet/balance (planned)   | UserChronaWallet      |
| DataTraceability    | Visualize data flow, audit    | /data/traceability (planned)| DataTraceabilityLog   |

## UI/UX Testing Requirements

- Test all flows end-to-end (consent, profile, wallet, feedback)
- Document bugs, blockers, and UX issues in GitHub Issues
- Ensure all UI is accessible and PET/Clarity compliant
- Follow the testing procedures in docs/protocols/testing_protocol.md

## References & Related Documents

- [System Blueprint](../../SYSTEM_BLUEPRINT.md) - Architecture and flows
- [UI Component Specifications](./README.md) - Individual component specs
- [Style Guide](../style/visual_identity.md) - Color palette and visual identity
- [Testing Protocol](../protocols/testing_protocol.md) - UI testing procedures
- [PET/Clarity Compliance](../protocols/pet_clarity_compliance.md) - Compliance requirements

## Maintenance Notes

- Update this guide when adding new components or endpoints
- Keep the component table synchronized with actual implementations
- Ensure all linked documents are in their canonical locations
- Follow anti-fragmentation rules when adding new documentation
