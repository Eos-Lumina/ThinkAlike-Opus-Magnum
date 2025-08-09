---
title: 🚨 Publication Blockers: Harmonization Triage Table
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

<!-- NOTE: This is a triage/tracker file. The canonical file index is in CANONICAL_FILE_INDEX.md. -->

# 🚨 Publication Blockers: Harmonization Triage Table

| Blocker Description | File/Area | Status | Notes |
|---------------------|-----------|--------|-------|
| Unfinished stubs for Manifesto, Vision, User Personas, Design Specs, Data Models, Traceability, Realms & Certification, Coding Standards, Dev Setup, Testing, Community Guidelines, Moderation, Deployment | See Outstanding Stubs below | ❌ | All must be created or filled in with at least minimal content before publication |
| Broken or missing cross-links in indices and READMEs | All major indices (README.md, PROJECT_FILE_INDEX.md, docs/README.md, etc.) | ❌ | Run a link check and update all navigation/cross-links |
| Unreviewed or legacy files not harmonized or archived | legacy/ and filtered_legacy/ folders, any file marked 'Draft' or 'Review Needed' | ❌ | Review, migrate, or archive all legacy/unharmonized files |
| Accessibility and PET/Clarity compliance not verified for all UI, assets, and docs | UI components, assets, docs | ❌ | Confirm all meet WCAG AAA, PET/Clarity, and symbolic/ritual standards |
| No single source of truth for onboarding, contributor, and FAQ docs | Onboarding, CONTRIBUTING.md, FAQ, etc. | ❌ | Consolidate, cross-link, and verify all onboarding and contributor docs |
| README and navigation inconsistencies | All folders | ❌ | Ensure every major folder has a harmonized README/index |

---

# Open TODOs, Drafts, and Missing Specs Tracker

This document tracks all known TODOs, drafts, and "to be created" items across the ThinkAlike project. Update this list as items are completed or new drafts are added.

---

## High-Priority TODOs & Drafts

- [x] Create actionable stubs for Chrona wallet, parecon integration, restorative trust, onboarding guide, and unified API/DataTraceability docs (see SYSTEM_BLUEPRINT.md)
- [ ] Fill in detailed content for Chrona wallet, parecon integration, restorative trust, onboarding guide, and unified API/DataTraceability docs (community contributions welcome)
- [ ] Harmonize economic, trust, and narrative protocol docs (cross-link and clarify)

## File-Specific TODOs & Drafts

- `src/swarm/implementations/eos_lumina_agent.py`: Multiple TODOs for agent logic, NLP, and sub-agent routing
- `src/backend/voice/invoke_service.py`: TODOs for STT model/client and transcription logic
- `src/frontend/components/PostNewListing.jsx`: TODO for submit logic
- `src/frontend/components/pci/PCIProfileBuilder.tsx`: TODO for component imports
- `src/swarm/unaligned/migration/unaligned_agents_migration_todo.md`: Migration and harmonization of legacy agent roles
- `docs/seed/symbolic_alignment/` and `docs/ui_components/`: Multiple files marked as Draft or requiring further harmonization
- `docs/architecture/agent_framework/agent_persona_protocol.md`: Ensure all persona YAMLs and code are cross-linked

## General

- Regularly update SYSTEM_BLUEPRINT.md and master_reference.md as new modules/specs are added or harmonized
- Maintain navigation notes and README consistency as new folders/files are created
- Periodically run consistency checks for TODOs, drafts, and broken links

---

## Outstanding Stubs and Review-Needed Items (from master_reference.md)

- Manifesto: Expand with project-wide call to action and vision (`docs/seed/core/scintilla_conscientiae_harmonicae_nascentis.md`)
- Vision & Core Concepts: Expand with concise vision statement and key concepts (`docs/seed/core/core_concepts.md`)
- Target Audience & User Personas: Create (`docs/seed/core/user_personas.md`)
- Architectural Design Specifications: Create (`docs/architecture/design_specifications.md`)
- Data Models & Schemas: Create (`docs/architecture/data_models.md`)
- Data Traceability Component: Create (`docs/ui_components/data_traceability_component.md`)
- Realms & Certification: Create (`docs/architecture/realms_and_certification.md`)
- Coding Standards: Create (`docs/development_framework/coding_standards.md`)
- Development Setup: Create (`docs/development_framework/development_setup.md`)
- Testing Strategy: Create (`docs/development_framework/testing_strategy.md`)
- Community Guidelines: Create (`docs/reference/community_guidelines.md`)
- Moderation Policy: Create (`docs/reference/moderation_policy.md`)
- Deployment & Infrastructure: Create (`docs/reference/deployment_infrastructure.md`)
- Context Manifest (Archive): Create (Archive section)

*Last updated: 2025-06-18*

**Note:** All critical documentation stubs now exist and are ready for detailed content and harmonization. See the relevant stub files for outlines and next steps.
