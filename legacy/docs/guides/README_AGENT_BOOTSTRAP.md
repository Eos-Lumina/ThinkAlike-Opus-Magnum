# ThinkAlike Protocols Harmonization & Migration – Agent Bootstrap Guide

## Project Overview
ThinkAlike is a complex, modular system with a large number of protocols, implementation plans, and supporting documents. The project is undergoing a major harmonization and migration effort to:
- Restore, standardize, and consolidate all protocol and documentation files.
- Ensure all files are present, canonical, logically usable, and have up-to-date, consistent frontmatter and content.
- Migrate useful protocols from `_legacy/protocols` to the main `protocols` directory, avoiding deletion and duplication.
- Place each protocol in its most appropriate subdirectory (e.g., `ethics/`, `governance/`, `data/`, etc.).
- Add redirect notices to legacy files and root-level stubs, pointing to canonical locations.
- Only canonical protocols are referenced in indexes and overviews; legacy and alternate versions are preserved for reference.

## What Has Been Done
- Canonical protocols have been moved to their correct subdirectories.
- Implementation plans, drafts, and legacy files are either moved to appropriate subfolders or replaced with redirect notices.
- All legacy files in `_legacy/protocols/` are being replaced with redirect notices pointing to their canonical or harmonized locations.
- No files are deleted; all legacy and alternate versions are preserved for reference.
- The process is systematic and ongoing, with each protocol domain (core, data, governance, ethics, identity, economic, etc.) being processed in turn.

## How to Continue
1. **Check for Duplicates:** Before migrating or harmonizing a file, check if a canonical or harmonized version already exists in the main `protocols/` directory or its subdirectories.
2. **Move and Redirect:** Move canonical protocols to their correct subdirectory. For legacy or duplicate files, replace their content with a redirect notice pointing to the canonical location.
3. **Update Indexes:** Ensure only canonical protocols are referenced in `protocols_overview.md` and other indexes.
4. **Preserve Legacy:** Do not delete legacy or alternate versions; always preserve them for reference, but make it clear which file is canonical.
5. **Frontmatter:** Ensure all harmonized files have up-to-date, consistent frontmatter (title, version, status, last_updated, maintained_by, tags, related_docs, legacy_docs, harmonization_note, etc.).
6. **Document Progress:** Update this bootstrap or a migration log with what has been completed and what remains.

## Relevant Context
- Redirect notices are simple HTML comments at the top of legacy or root-level files, e.g.:
  `<!-- This file has been moved to protocols/ethics/consent_protocol.md as part of the protocol harmonization and organization process. Please reference the canonical protocol in its new location. -->`
- No files are deleted; all history is preserved.
- The process is ongoing and systematic, working through all protocol domains.


## Canonical Consolidation Plan (for Agents and Humans)

### 1. Inventory and Mapping
- For each protocol cluster (e.g., core, identity, chrona, governance, resonance, narrative, ethics, data, etc.):
  - List all files in both `protocols/<cluster>/` and `_legacy/protocols/<cluster>/` (and `_legacy/protocols/bulk/` for scattered alternates).
  - Create a mapping of canonical, draft, and alternate versions for each protocol.

### 2. Comparison and Selection
- For each protocol in the cluster:
  - Compare canonical and legacy versions.
  - Select the most complete, up-to-date, and principle-aligned version as canonical.
  - If legacy files contain unique content, merge it into the canonical version.

### 3. Migration and Harmonization
- Move the canonical protocol to the correct subdirectory in `protocols/`.
- Ensure frontmatter is present and harmonized (title, version, status, last_updated, maintained_by, tags, related_docs, harmonization_note, etc.).
- Add a redirect notice to all legacy/duplicate files, pointing to the canonical version.
- Archive or clearly mark any files that are deprecated or for reference only.

### 4. Index and Documentation Update
- Update `protocols_index.md` and any overview files to reference only canonical protocols.
- Ensure all core philosophy and ethical docs in `seed/` are referenced in the main README or project overview.
- Update `README.md` to explain the project’s vision, architecture, and how to get involved.

### 5. Canonical Project Tree Example
```
protocols/
  core/
    agent_context_protocol.md
    agent_handoff_protocol.md
    agent_memory_protocol.md
    consent_protocol.md
    contradiction_flagging_protocol.md
    epistemic_reflection_protocol.md
    interaction_protocol.md
    trust_protocol.md
    ...
  identity/
    agent_persona_protocol.md
    agent_registry_protocol.md
    initiation_glyph_protocol.md
    sovereign_stack_protocol.md
    sybil_resistance_protocol.md
    ...
  chrona/
    chrona_economic_protocol.md
    chrona_valuation_protocol.md
    chrona_wallet_protocol.md
    ...
  governance/
    hive_governance_protocol.md
    contributor_recognition_protocol.md
    decentralized_oversight_protocol.md
    ...
  resonance/
    resonance_matching_protocol.md
    resonance_trust_protocol.md
    temporal_dynamics_protocol.md
    ...
  narrative/
    ritual_encoding_protocol.md
    ritual_protocols.md
    symbolic_alignment_protocol.md
    ...
  ...
protocols_index.md
README.md
seed/
  ethics/
  vision/
  ...
_legacy/
  protocols/
    bulk/
    <all legacy files, with redirect notices>
```

### 6. Repeat for Each Cluster
- Complete the above steps for one cluster before moving to the next.
- Document progress in a migration log or update `README_AGENT_BOOTSTRAP.md`.

### 7. Final Clean-Up
- Move unused/draft files to an archive folder.
- Ensure only canonical protocols are indexed and referenced.
- Add LICENSE, CONTRIBUTING.md, and CODE_OF_CONDUCT.md for open source readiness.
- Push to GitHub or your chosen platform.

---

**Ready to begin with the identity cluster? Inventory, compare, and propose a canonical set for each cluster, following this plan.**

---

**For questions or handoff, review this file and the current state of the `protocols/` and `_legacy/protocols/` directories.**
