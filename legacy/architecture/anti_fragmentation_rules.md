---
title: Anti-Fragmentation Rules
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Anti-Fragmentation Rules

This document outlines the rules and practices to prevent project fragmentation and maintain a single source of truth.

## Core Principles

1. **Single Source of Truth**: Each concept or specification has exactly one canonical location.
2. **No Duplicate Documentation**: Information should not be duplicated across multiple files or locations.
3. **Structured Organization**: All content belongs in designated canonical folders.
4. **Version Control Over File Versions**: Use git for versioning, not file naming.
5. **Clear Documentation Hierarchy**: Follow the established directory structure for all documentation:
   - UI Components → `docs/ui_components/`
   - Development Guides → `docs/guides/development/{general|frontend|backend|ai}/`
   - Operations Guides → `docs/guides/operations/`
   - Architecture Docs → `docs/architecture/`
   - Protocol Specs → `docs/protocols/`
   - Ethics Guidelines → `docs/ethics/`

## Canonical Sources

| Type | Location | Purpose |
|------|----------|---------|
| System Blueprint | `SYSTEM_BLUEPRINT.md` | High-level system architecture and design |
| Project Manifest | `project_manifest.yaml` | Project structure and requirements |
| Source of Truth | `docs/source_of_truth.md` | Core project specifications |
| Archive | `docs/archive/` | Single location for archived content |

## Canonical Domains

| Domain | Location | Purpose |
|--------|----------|---------|
| UI Components | `docs/ui_components/` | UI component documentation |
| Onboarding | `docs/onboarding/` | Onboarding documentation |
| Contributors | `docs/contributors/` | Contributor guidelines |
| Protocols | `docs/protocols/` | Protocol specifications |
| Style | `docs/style/` | Style guides |
| Templates | `docs/templates/` | Document templates |
| Data | `data/` | Data files |
| Assets | `assets/` | Media and assets |
| Scripts | `scripts/` | Utility scripts |

## Forbidden Patterns

The following patterns are automatically blocked to prevent fragmentation:

1. Custom archive folders (`*_archive*`)
2. Additional sources of truth (`*source*of*truth*`)
3. Blueprint copies (`*blueprint*copy*`)
4. Backup folders (`*_backup*`)
5. Nested archives (`*/archive/*/archive/*`)
6. Files with version numbers (`*_v1*`, etc.)
7. Draft files (`*_draft*`)
8. Old/new version markers (`*_old*`, `*_new*`)
9. Duplicate indicators (`*_duplicate*`)

## Best Practices

1. **Adding New Content**:
   - Check existing canonical locations first
   - Place content in the appropriate canonical folder
   - Update the relevant index/manifest files

2. **Modifying Content**:
   - Edit the canonical source directly
   - Use git branches for drafts and revisions
   - Update all references to the modified content

3. **Archiving Content**:
   - Use only the canonical archive location
   - Maintain the original folder structure within the archive
   - Update indices and references

4. **Version Control**:
   - Use git branches for work in progress
   - Use git tags for versions
   - Never create "_v2" or similar files

## File Naming Conventions

The official file naming conventions for this project are defined in the [Lowercase File Naming Policy](./lowercase_file_naming_policy.md). All contributors must adhere to these rules to ensure consistency and prevent fragmentation.

## Enforcement

These rules are automatically enforced through:

1. Pre-commit hooks that validate the project structure
2. The `structure_check.py` script that validates:
   - Canonical source locations
   - Forbidden patterns
   - Deprecated paths
   - Content organization

## Handling Violations

If you encounter a violation:

1. Use `git mv` to move content to its canonical location
2. Update all references to the moved content
3. Remove any duplicate content
4. Run `pre_commit` to validate changes
