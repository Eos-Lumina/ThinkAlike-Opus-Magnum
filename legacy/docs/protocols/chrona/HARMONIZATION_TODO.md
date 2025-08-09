# Chrona Protocols Harmonization To Do

This file lists the actions required to harmonize the chrona protocol cluster, based on comparison of canonical and legacy protocols.

## 1. Inventory & Comparison
- Canonical protocols present: chrona_economic_protocol, chrona_valuation_protocol, chrona_wallet_protocol
- Legacy/alternate protocols found: multiple versions and drafts of the above, with unique content or alternate maintainers in _legacy/protocols/bulk

## 2. Harmonization Actions Needed
- [ ] Review all legacy protocol versions for unique content, rationale, or implementation notes not present in canonical files
- [ ] For each protocol, ensure canonical file:
    - Has up-to-date frontmatter (authors, version, last_updated, tags, references)
    - Incorporates any valuable legacy rationale, diagrams, or implementation notes
    - References legacy provenance in a migration note if significant changes were made
- [ ] Archive all legacy protocol drafts to `_legacy/archived_protocols/` if not already present, with a migration log entry
- [ ] For protocols with major changes, propose a harmonized canonical version that merges best of both
- [ ] Update manifest.yaml and STRUCTURE_MANIFEST.md if protocol list or structure changes
- [ ] Add redirect/README notes in legacy locations if needed

## 3. Documentation & Logging
- [ ] Log all migrations, harmonizations, and archival actions in migration_log.yaml and migration_log_entry_2025-07-08.md
- [ ] Update protocols_index.md and protocols_overview.md to reflect harmonized state

---

Repeat this process for each protocol in the chrona cluster. When complete, proceed to the next cluster (e.g., governance, resonance, etc.).
