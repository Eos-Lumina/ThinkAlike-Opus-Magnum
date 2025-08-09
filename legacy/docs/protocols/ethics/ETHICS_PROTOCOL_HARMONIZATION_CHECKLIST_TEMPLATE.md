# Ethics Protocol Harmonization Checklist Template

For each protocol in the ethics cluster, use the following checklist to ensure a thorough, provenance-preserving harmonization process:

---

## [Protocol Name]

- [ ] Inventory all legacy and canonical versions of this protocol
- [ ] Compare canonical and legacy versions for unique content, rationale, or implementation notes
- [ ] Update canonical file to:
    - [ ] Include up-to-date frontmatter (authors, version, last_updated, tags, references)
    - [ ] Incorporate valuable legacy rationale, diagrams, or implementation notes
    - [ ] Add a migration note referencing legacy provenance if significant changes were made
- [ ] Archive all legacy protocol drafts to `_legacy/archived_protocols/` (if not already present)
- [ ] Log migration and harmonization actions in `migration_log.yaml` and `migration_log_entry_2025-07-08.md`
- [ ] Update `manifest.yaml` and `STRUCTURE_MANIFEST.md` if protocol list or structure changes
- [ ] Add redirect/README notes in legacy locations if needed
- [ ] Update `protocols_index.md` and `protocols_overview.md` to reflect harmonized state

---

Repeat for each protocol in the ethics cluster. When complete, proceed to the next protocol cluster (e.g., data, etc.).
