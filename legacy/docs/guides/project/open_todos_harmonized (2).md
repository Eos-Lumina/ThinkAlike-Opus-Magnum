---
title: 🚨 Publication Blockers & Outstanding Tasks — Harmonization Tracker (June 2025)
version: 1.3.0
status: Canonical
last_updated: 2025-06-22
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
tags: [todo, tracker, harmonization, publication-blocker, project-map, structure]
---

<!-- NOTE: This is a harmonization tracker for stubs and drafts. The canonical file index is in CANONICAL_FILE_INDEX.md. -->

# 🚨 Publication Blockers & Outstanding Tasks

This document tracks all remaining stubs, TODOs, and drafts across the ThinkAlike project. Each item is marked as:
- [ ] To be completed (specify owner or next step)
- [x] Complete or harmonized
- [~] Planned for future phase (not a blocker)

---

## Publication Blockers Triage Table

| Blocker Description | File/Area | Status | Notes |
|---------------------|-----------|--------|-------|
| Unfinished stubs for Manifesto, Vision, User Personas, Design Specs, Data Models, Traceability, Realms & Certification, Coding Standards, Dev Setup, Testing, Community Guidelines, Moderation, Deployment | See Outstanding Stubs below | ❌ | All must be created or filled in with at least minimal content before publication |
| Broken or missing cross-links in indices and READMEs | All major indices (README.md, canonical_file_index.md, docs/README.md, etc.) | ❌ | Run a link check and update all navigation/cross-links |
| Unreviewed or legacy files not harmonized or archived | legacy/ and filtered_legacy/ folders, any file marked 'Draft' or 'Review Needed' | ❌ | Review, migrate, or archive all legacy/unharmonized files |
| Accessibility and PET/Clarity compliance not verified for all UI, assets, and docs | UI components, assets, docs | ❌ | Confirm all meet WCAG AAA, PET/Clarity, and symbolic/ritual standards |
| No single source of truth for onboarding, contributor, and FAQ docs | Onboarding, CONTRIBUTING.md, FAQ, etc. | ❌ | Consolidate, cross-link, and verify all onboarding and contributor docs |
| README and navigation inconsistencies | All folders | ❌ | Ensure every major folder has a harmonized README/index |

---

## Major Gaps & Missing Files

- [ ] Data models, ERD, and schemas incomplete (`docs/architecture/data_models.md`, `database_schema.md`)
- [ ] Unified OpenAPI spec and protocol documentation not finished (`docs/api_specs/openapi.json`)
- [ ] Onboarding, user personas, and narrative flows incomplete (`docs/realms/portal/`, `docs/protocols/resonant_trust_protocol.md`)
- [ ] Chrona wallet UI and backend integration missing (`docs/ui_components/`, backend endpoints)
- [ ] Testing, validation, and coverage not unified or tracked (`tests/`, `testing_and_validation_plan.md`)
- [ ] CI/CD, deployment, and observability not implemented (scripts, pipeline config)
- [ ] Some UI components, backend endpoints, and agent migrations in progress
- [ ] Documentation indices, onboarding, and FAQ need harmonization
- [ ] Noetica meta files are placeholders (to be filled by owner)
- [ ] Some folders may lack README/index files

---

## High-Priority Stubs & TODOs
- [x] Create actionable stubs for Chrona wallet, parecon integration, restorative trust, onboarding guide, and unified API/DataTraceability docs (see SYSTEM_BLUEPRINT.md)
- [ ] Fill in detailed content for Chrona wallet, parecon integration, restorative trust, onboarding guide, and unified API/DataTraceability docs (community contributions welcome)
- [ ] Harmonize economic, trust, and narrative protocol docs (cross-link and clarify)
- [ ] Manifesto, Vision, User Personas: Ensure all are finalized and cross-linked in SYSTEM_BLUEPRINT.md
- [ ] Design Specs, Data Models, Traceability: Confirm all referenced files exist and are up to date
- [ ] Realms & Certification: Complete specs for all realms (including experimental/edge-case)
- [ ] Coding Standards, Dev Setup, Testing: Finalize and cross-link all developer onboarding docs
- [ ] Community Guidelines, Moderation, Deployment: Ensure all are mapped and accessible

## File-Specific TODOs & Drafts
- [ ] `src/swarm/implementations/eos_lumina_agent.py`: Complete agent logic, NLP, and sub-agent routing
- [ ] `src/backend/voice/invoke_service.py`: Finalize STT model/client and transcription logic
- [ ] `src/frontend/components/PostNewListing.jsx`: Complete submit logic
- [ ] `src/frontend/components/pci/PCIProfileBuilder.tsx`: Finalize component imports
- [ ] `src/swarm/unaligned/migration/unaligned_agents_migration_todo.md`: Track and complete agent migration
- [ ] `docs/seed/symbolic_alignment/` and `docs/ui_components/`: Harmonize all drafts and mark as complete or planned
- [ ] `docs/architecture/agent_framework/agent_persona_protocol.md`: Ensure all persona YAMLs and code are cross-linked

## Outstanding Stubs and Review-Needed Items
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

## General
- [ ] Regularly update SYSTEM_BLUEPRINT.md and master_reference.md as new modules/specs are added or harmonized
- [ ] Maintain navigation notes and README consistency as new folders/files are created
- [ ] Periodically run consistency checks for TODOs, drafts, and broken links

## Reference: Living Blueprints & Known Gaps
- For GDPR, archival, and disaster recovery: see 'Known Gaps & Next Steps' in `docs/architecture/data_systems/gdpr_archival_disaster_recovery_strategy.md`
- For experimental/edge-case realms and digital legacy: see 'Known Gaps & Next Steps' in `docs/realms/experimental_realms_digital_legacy_outline.md`
- For advanced data flows, security, and privacy: see 'Known Gaps & Next Steps' in `docs/architecture/security/advanced_data_flows_security_privacy.md`

---

# Canonical Project Structure

This section defines the canonical structure for the ThinkAlike project. All new development must follow these organizational guidelines.

## Project Root Structure

```
thinkalike/
├── app/                    # Next.js app directory
├── src/                    # Source code
│   ├── core/              # Core application logic
│   ├── frontend/          # Frontend application
│   ├── backend/           # Backend services
│   └── shared/            # Shared code
├── docs/                  # Documentation
├── tests/                 # Test files
├── config/                # Configuration
└── tools/                 # Development tools
```

## Detailed Structure

### Source Code (`src/`)

#### Core (`src/core/`)
- `agent_registry/` - Agent management system
- `alchemy/` - Core transformation logic
- `narrative_engine/` - Narrative processing
- `resonance_graph/` - Graph database interactions
- `ritual_engine/` - Ritual processing

#### Frontend (`src/frontend/`)
- `components/` - Reusable UI components
- `pages/` - Page definitions
- `hooks/` - Custom React hooks
- `styles/` - CSS/styling
- `utils/` - Frontend utilities

#### Backend (`src/backend/`)
- `api/` - API endpoints
- `services/` - Business logic
- `models/` - Data models
- `database/` - Database interactions
- `middleware/` - Express/HTTP middleware

#### Shared (`src/shared/`)
- `types/` - TypeScript types/interfaces
- `constants/` - Shared constants
- `utils/` - Shared utilities

### Documentation (`docs/`)

#### Guides (`docs/guides/`)
- `development/` - Development guides
  - `general/` - General development guidelines
  - `ai/` - AI-specific guides
  - `frontend/` - Frontend development
  - `backend/` - Backend development
  - `narrative/` - Narrative development
  - `operations/` - DevOps guides

#### Architecture (`docs/architecture/`)
- System design documents
- Data flow diagrams
- Security model

#### UI Components (`docs/ui_components/`)
- Component documentation
- UI development guides
- Accessibility guidelines

### Testing (`tests/`)

#### Unit Tests (`tests/unit/`)
- `frontend/` - Frontend component tests
- `backend/` - Backend service tests
- `shared/` - Shared code tests

#### Integration Tests (`tests/integration/`)
- `api/` - API integration tests
- `e2e/` - End-to-end tests

### Configuration (`config/`)
- `default.json` - Default configuration
- `development.json` - Development settings
- `production.json` - Production settings
- `test.json` - Test settings

### Tools (`tools/`)
- `scripts/` - Build/deployment scripts
- `generators/` - Code generators
- `debug/` - Debugging utilities

---

*Update this tracker as items are completed or new drafts are added. Use as a reference for harmonization and publication readiness.*
