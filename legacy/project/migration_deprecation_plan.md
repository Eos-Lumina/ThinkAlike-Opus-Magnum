---
title: Migration and Deprecation Plan
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Migration and Deprecation Plan

This document lists prioritized actions for migration, deprecation, or removal of non-canonical, ambiguous, and duplicate files/folders, based on the latest structure check report.

## Prioritization Criteria
- **High Priority**: Files/folders that are duplicates of canonical sources, or are ambiguous and likely to cause confusion.
- **Medium Priority**: Files/folders that are non-canonical but not immediately harmful.
- **Low Priority**: Files/folders that are legacy, archival, or informational, but not referenced by current systems.

---

## High Priority Actions
- **Duplicate/ambiguous README.md files**: Consolidate into canonical locations (e.g., root, `docs/`, and one per major domain only).
- **Multiple `PROJECT_FILE_INDEX.md` and similar index/status files**: Migrate all references to the canonical `PROJECT_FILE_INDEX.md` and remove or archive others.
- **Multiple `testing_and_validation_plan.md` and similar plans**: Merge content into canonical plan in `tests/testing_and_validation_plan.md`.
- **Ambiguous files in root (e.g., `project_file_list.txt`, `project_manifest.yaml`, `ROADMAP.md`, `QUEST_BOARD.md`, etc.)**: Migrate or archive to `docs/project/` or appropriate canonical subfolder.

## Medium Priority Actions
- **Legacy/archival files (e.g., `archive_legacy_file_list.txt`, `chatlog.txt`)**: Move to `docs/archive/` or similar.
- **Non-canonical scripts (e.g., `generate_file_list_script.py`)**: Move to `scripts/` or deprecate if superseded.
- **Ambiguous or duplicate guides (e.g., multiple onboarding, contributor, or UI guides)**: Merge and cross-link, deprecate outdated versions.

## Low Priority Actions
- **Informational or meta files not referenced by current systems**: Archive or mark as deprecated.

---

## Next Steps
1. Review and confirm canonical locations for all high-priority files.
2. Begin migration, deprecation, or removal as listed above.
3. Update all references, guides, and onboarding materials to point to canonical sources.
4. Maintain this plan as changes are made.

---

**References:**
- [Structure Check Report](../../structure_check_report.txt)
- [Harmonization Plan](harmonization_plan.md)
- [Canonical File Map](../../PROJECT_FILE_INDEX.md)
