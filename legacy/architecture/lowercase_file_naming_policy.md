---
title: Lowercase File Naming Policy
version: 1.1.0
status: Active
last_updated: 2025-06-22
maintained_by: Lumina∴ System Meta-Agent
tags: [file_naming, policy, convention, canonical]
harmonization_note: "This document is the canonical source for file naming conventions, extracted from anti_fragmentation_rules.md to serve as a single, dedicated policy."
---

# File Naming Conventions

This document outlines the official file naming conventions for the ThinkAlike project to ensure consistency and prevent fragmentation.

## 1. Master Project Files (UPPERCASE with underscores)
- **Purpose:** Critical project-wide documentation that provides high-level overviews or status.
- **Examples:**
  - `SYSTEM_BLUEPRINT.md`
  - `ROADMAP.md`
  - `README.md`
  - `PROJECT_STATUS_DASHBOARD.md`
  - `RELEASE_NOTES.md`

## 2. Regular Documentation (lowercase with underscores)
- **Purpose:** The default convention for all standard documentation files.
- **Examples:**
  - `user_guide.md`
  - `api_reference.md`
  - `button_component.md`
  - `auth_flow.md`
  - `chrona_specification.md`

## 3. Code and Configuration Files (lowercase with dots)
- **Purpose:** Source code and configuration files, following standard practices for their respective languages or frameworks.
- **Examples:**
  - `index.ts`
  - `app.py`
  - `tsconfig.json`
  - `next.config.js`
  - `globals.css`

## 4. Scripts and Tools (lowercase with underscores)
- **Purpose:** Utility and automation scripts. The use of underscores is consistent with Python's PEP 8 style guide.
- **Examples:**
  - `structure_check.py`
  - `generate_docs.py`
  - `agent_persona_manager.py`

---

**Note:** These rules are enforced by automated checks. Any deviation should be considered an error and corrected.

**Exceptions:**
Some files cannot be renamed due to technical constraints, legacy dependencies, or risk of project fragmentation. These exceptions should be documented here with rationale, and reviewed periodically:
- Files referenced by external systems, frameworks, or imports that would break if renamed
- Build artifacts or auto-generated files
- Legacy files where renaming would cause loss of history or break integrations

For any new files, always follow the conventions above unless a documented exception applies.
