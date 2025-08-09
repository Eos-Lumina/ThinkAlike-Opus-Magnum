---
title: Project Structure Manifest
version: 1.0.0
status: Canonical
last_updated: 2025-06-21
maintained_by: Core Development Team
---

# ThinkAlike Project Structure Manifest

This document defines the canonical structure for the ThinkAlike project. All new development must follow these organizational guidelines.

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

## File Naming Conventions

1. Use lowercase with hyphens for file names
2. Use `.ts` or `.tsx` for TypeScript files
3. Use `.md` for documentation
4. Test files should end with `.test.ts` or `.spec.ts`

## Module Dependencies

- Core modules should not depend on frontend/backend
- Frontend can depend on shared
- Backend can depend on shared
- Shared should have minimal dependencies

## Documentation Standards

1. Every module must have a README.md
2. Code documentation in JSDoc format
3. Architecture decisions in ADR format
4. API documentation using OpenAPI/Swagger

## Configuration Management

1. Sensitive data in environment variables
2. Environment-specific configs in config/
3. Default values in default.json
4. Local overrides in .env (not committed)

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed contribution guidelines.

---

*This manifest is the source of truth for project organization. All structural changes must be approved and documented here.*
