---
title: Project File Index
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Project File Index

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
  ├── `framework/`             # Shared agent/persona frameworks
  ├── `swarm/`                 # Swarm agent implementations
  └── `shared_utils/`          # Utility modules (e.g., document_utils)

## 2. Frontend & UI

- `app/`                      # Next.js application entrypoints (pages, layout, globals)
- `components/`               # Shared React components
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

> ⚠️ Before deleting or moving any file, confirm its role against this index. Archive deprecated modules under `docs/project/archive/` and remove empty placeholders (except legitimate `__init__.py` stubs).

