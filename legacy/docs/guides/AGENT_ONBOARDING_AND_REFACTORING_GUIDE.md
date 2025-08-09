# Agent Onboarding & Refactoring Guide for Publication

Welcome to the ThinkAlike project! This guide provides step-by-step instructions for any agent (human or AI) joining the project to help refactor, harmonize, and prepare the codebase and documentation for public release.

## 0. Data Preservation & Safety Policy
- All agents and automation must follow the `DATA_PRESERVATION_AND_SAFETY_POLICY.md`.
- No important file may be deleted; archive and redirect instead.
- Log every move, merge, or archival action in the migration log.
- Use dry-run and human review for all automation.

## 1. Understand the Canonical Structure
- Study `manifest.yaml` and `STRUCTURE_MANIFEST.md` to learn the canonical file and directory structure.
- All work must conform to these manifests—no files or folders outside this structure.

## 2. Protocol Harmonization
- For each protocol cluster (core, identity, data, etc.):
  - Review the cluster's `HARMONIZATION_TODO.md` for inventory and required actions.
  - Compare canonical protocols with legacy/alternate versions in `_legacy/protocols/bulk/`.
  - Merge valuable content, rationale, and diagrams from legacy files into the canonical version.
  - Ensure all canonical protocols have up-to-date frontmatter (title, version, status, last_updated, maintainers, tags, related_docs, harmonization_note).
  - Archive all legacy/alternate drafts to `_legacy/archived_protocols/` and add redirect notices in their old locations.
  - Log all actions in migration logs.

## 3. Update Indexes and Documentation
- Update `manifest.yaml`, `STRUCTURE_MANIFEST.md`, and all protocol indexes to reference only canonical, harmonized files.
- Remove or redirect any duplicate, outdated, or misplaced files.
- Update README and overview files to reflect the harmonized, canonical structure.
- Clearly document the harmonization process and provenance in migration logs and harmonization notes.

## 4. Final Audit
- Confirm every protocol, doc, and module is in its canonical location and referenced in the manifest.
- Ensure no duplicates or orphaned files remain.
- Validate all cross-references (in docs, protocols, and code) point to canonical files.

## 5. Use the Final Consolidation Checklist
- Follow the steps in `FINAL_CONSOLIDATION_CHECKLIST.md` to ensure nothing is missed before publication.

## 6. Ask for Help or Clarification
- If you encounter ambiguity, missing files, or unclear structure, consult the migration logs, harmonization notes, or ask a project maintainer.

---

## Decisive Priorities for a Stable, Unified Project

### 1. Backend API and Data Model Consistency
- For each core resource (user, profile, item, agent, token, etc.):
  - Ensure there is only one canonical model, schema, CRUD, and endpoint file in the main `app` directory.
  - Remove or archive all duplicates, partials, or outdated versions from both the main and legacy trees.
  - Standardize naming, import paths, and business logic across all modules.
- This ensures your backend is maintainable, testable, and ready for future extension.

### 2. Agent Framework Integration
- The agent system is central to the project’s vision.
- Ensure the agent framework (registration, matching, protocols) is present, non-empty, and integrated with the backend API.
- Restore or rewrite any missing agent logic, and connect it to the main API as needed.

### 3. Documentation and Structure
- Migrate and update canonical documentation (README, blueprints, manifests) to the main tree.
- Add or update `README.md` files in all major folders to clarify their purpose and usage.
- Keep documentation in sync with the codebase and structure.

---

**Recommended Sequence:**  
Start with backend API and data model harmonization. Once stable, integrate the agent framework and protocols. Finally, finalize documentation and structure. This sequence will give you a solid, unified foundation for all future development.

---

By following this guide, every agent can contribute to a clean, canonical, and publish-ready ThinkAlike project.
