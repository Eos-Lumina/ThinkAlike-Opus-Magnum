---
title: ThinkAlike Canonical File Index
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# ThinkAlike Canonical File Index

_Last updated: June 19, 2025_

This index lists the single source of truth for every major module, protocol, and documentation set in ThinkAlike. Use this as your map for navigation, harmonization, and contributor onboarding.

---

## Core Project Blueprints
- SYSTEM_BLUEPRINT.md (system map, roadmap, integration)
- AGENT_BOOTSTRAP.md (machine-readable entry point)
- project_manifest.yaml (project structure, modules)

## Main Documentation
- README.md (project overview)
- CONTRIBUTOR_DASHBOARD.md (status, onboarding, quests)
- QUEST_BOARD.md (open tasks, featured quests)
- QUICKSTART_FOR_NONDEVELOPERS.md (non-technical intro)
- UI_DEVELOPER_GUIDE.md (frontend/UI guidance)

## Protocols & Specs
- docs/protocols/chrona_economic_protocol.md (Chrona economy)
- docs/protocols/resonant_trust_protocol.md (Trust system)
- docs/protocols/narrative_duet_protocol.md (Narrative engine)
- docs/protocols/model_context_protocol.md (MCP)
- docs/protocols/initiation_glyph_protocol.md (Onboarding)
- docs/protocols/invocation_phrase_protocol.md (Onboarding)

## Architecture & Data
- docs/architecture/data_models.md (data models)
- docs/architecture/database/database_schema.md (ERD/schema)
- docs/architecture/agent_framework/ (agent protocols)
- docs/architecture/data_traceability_protocol.md (traceability)
- docs/api_specs/openapi.json (API spec)

## Backend & API
- src/backend/app/ (FastAPI app, routers, models, schemas)
- src/backend/app/schemas/pci_schemas.py (PCI data models)

## Frontend & UI
- app/ (Next.js app entry)
- src/frontend/components/ (React components)
- docs/ui_components/ (UI specs)

## Agent/Swarm System
- src/swarm/ (agent framework, personas, registry)
- docs/architecture/agent_framework/ (protocols/specs)

## Economic & Governance
- docs/realms/governance/ (governance specs)
- docs/realms/marketplace/ (marketplace specs)
- docs/protocols/chrona_economic_protocol.md (Chrona)

## Testing & Validation
- tests/ (all tests)
- docs/testing_and_validation_plan.md (test plan)

## Onboarding & Contributor Guides
- docs/guides/onboarding/README.md (onboarding hub)
- docs/guides/contributor_guides/human_contributor_quickstart.md
- docs/guides/contributor_guides/code_of_conduct.md

## Academic & Research
- docs/noetica/ (Corpus Magnus, research hub)

## Protocols & Integration
- docs/architecture/protocols/protocols_overview.md

## Internationalization (i18n) & Multilingual Support
- docs/architecture/protocols/protocols_overview.md#7-internationalization-i18n--multilingual-protocols

## User-Friendly Guides (Plain Language)
- Onboarding & PCI: `docs/architecture/protocols/onboarding_pci_plain_language.md`
- Chrona Wallet: `docs/architecture/protocols/chrona_wallet_plain_language.md`
- Governance & Trust: `docs/architecture/protocols/governance_trust_plain_language.md`
- Agent/Narrative: `docs/architecture/protocols/agent_narrative_plain_language.md`

## Outstanding Stubs & TODOs
- `docs/project_open_todos_harmonized.md`

---

# Canonical File Index

This document provides a single source of truth for the project's directory layout and core modules. Use this as the definitive map before making any structural changes.

## 1. Source Code

- `src/`
  ├── `__init__.py`            # Top-level package
  ├── `backend/`
  │   ├── `__init__.py`        # Backend package
  │   ├── `app/`               # FastAPI application (routers, schemas, CRUD)
  │   ├── `services/`          # Business logic modules
  │   ├── `translation/`       # Translation service (Azure integration)
  │   └── `voice/`             # Voice/invoke service
  ├── `framework/`             # Shared agent and persona frameworks
  ├── `swarm/`                 # Swarm agent implementations
  └── `shared_utils/`          # Utility modules (e.g., document_utils)

## 2. Frontend

- `app/`                      # Next.js application entrypoints (pages, layout, globals)
- `components/`               # Shared UI components
- `assets/`                   # Static assets and icons

## 3. Documentation

- `docs/architecture/`        # Technical architecture diagrams and models
- `docs/seed/`                # Initiation pathway and core philosophy
- `docs/guides/`              # Development, UI, narrative guides
- `docs/project/`             # Project-level blueprints, masterplans, roadmaps

## 4. Scripts & Tooling

- `scripts/`                  # Maintenance and generation scripts
  - `cleanup_duplicate_files.py`
  - `enforce_naming_convention.py`
  - `reorganize_docs.py`

## 5. Tests

- `tests/`                    # Unit and integration tests
  ├── `backend/`              # Backend API tests (auth, translation, voice)
  ├── `test_document_utils.py` # Document utilities
  └── `test_add_numbers.py`    # Example test

---

> ⚠️ Before deleting or moving any file, confirm its role against this index. Archive deprecated modules under `docs/project/archive/` and remove empty placeholders (except legitimate `__init__.py` stubs).

For any module or feature not listed here, check SYSTEM_BLUEPRINT.md or ask in the Contributor Dashboard. This index is updated as the project evolves.
