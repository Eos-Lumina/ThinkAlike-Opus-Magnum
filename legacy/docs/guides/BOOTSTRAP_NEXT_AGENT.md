# BOOTSTRAP_NEXT_AGENT.md

## Welcome, Next Agent!

This guide will align you with the current state, structure, and consolidation process of the ThinkAlike project. Follow these steps to ensure your work is fully harmonized with the project's principles and ongoing migration.

---

## 1. **Project Principles & Structure**
- **Single Source of Truth:** All canonical files and protocols exist in only one location, as defined in `STRUCTURE_MANIFEST.md` and `manifest.yaml`.
- **Sanctuaries Principle:**
  - `docs/` is the Public Library (canonical specs, guides, blueprints).
  - `project/` is the Steward's Council Chamber (internal planning, meeting notes).
- **Workshops Principle:**
  - `src/frontend/components/` is the Forge (actual UI code).
  - `docs/ui_components/` is the Blueprint Room (component specs, guides).
- **No Duplication:** Remove all deprecated, legacy, or duplicate files. Only canonical versions remain.

---

## 2. **Current State**
- **Backend:** FastAPI backend is running, tested, and clean of file corruption.
- **Canonical Protocols:** All key protocols (e.g., `api_design_guidelines.md`, `initiation_glyph_protocol.md`, `ai_emergence_protocol.md`) are in their correct subfolders under `protocols/`.
- **Architecture:** All architectural docs are in the root-level `architecture/` directory.
- **Testing:** Automated endpoint tests are in place and should be expanded as new endpoints are added.
- **Legacy:** All legacy, deprecated, and duplicate files are being removed. Only `_legacy/` holds reference material for migration.

---

## 3. **Your Next Steps**
1. **Consult the Manifest:**
   - Always check `STRUCTURE_MANIFEST.md` and `manifest.yaml` before adding or moving files.
2. **Continue Consolidation:**
   - Audit for any remaining non-canonical, legacy, or duplicate files. Remove or migrate as needed.
   - Ensure all references and links in documentation point to canonical files only.
3. **Expand Testing:**
   - Add automated tests for any new endpoints, features, or modules you introduce.
   - Run all tests after changes to ensure system integrity.
4. **Document Everything:**
   - Update `README.md`, internal docs, and protocol files to reflect any changes.
   - Add clarifying README files in new or reorganized directories.
5. **Migrate Valuable Legacy Content:**
   - Prioritize migration of high-value clusters (API specs, symbolic alignment protocols, agent modules) from `_legacy/`.
   - Harmonize and place them in their canonical locations.
6. **Follow Project Principles:**
   - Never duplicate files or folders.
   - Keep the structure clean, professional, and easy for future agents to navigate.

---

## 4. **How to Continue the Consolidation**
- **Inventory:** Use the manifest and directory listings to identify any files not in canonical locations.
- **Migrate:** Move or harmonize valuable legacy files into their correct place, updating references as you go.
- **Delete:** Remove all deprecated, duplicate, or non-canonical files immediately after migration.
- **Test:** Run all automated tests and validate endpoints after each major change.
- **Document:** Update all relevant documentation to reflect the new, consolidated state.

---

## 5. **If in Doubt**
- Ask for clarification in the project chat or leave a note in `project/blueprints/`.
- Always default to the manifest and this guide for structure and process.

---

**Thank you for helping ThinkAlike remain harmonized, professional, and ready for the next phase of agent/module development!**
