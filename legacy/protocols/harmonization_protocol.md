# Harmonization Protocol for ThinkAlike Documentation

## Purpose
To provide a formal, canonical process for the migration, harmonization, and consolidation of all ThinkAlike documentation, ensuring zero data loss, full provenance, and a single source of truth.

## 1. Best Practices for Large-Scale Consolidation
- Treat documentation as a curated library restoration, not just a file move.
- **Appoint a Master Scribe:** One agent (guided by project leads) is responsible for final synthesis, preventing conflicting "Golden Master" versions.
- **Three-Bucket Staging System:**
  - `01_raw_fragments/`: All legacy files for a cluster are first moved here.
  - `02_synthesis_in_progress/`: The Master Scribe creates new canonical docs from the raw fragments here.
  - `03_ready_for_canon/`: Completed canonical docs are moved here for final review before migration to the main grimoire.
- **Prioritize by Dependency:** Start with foundational clusters (Identity & Onboarding, Ethics & Governance, Core Protocols, then Realms).

## 2. Maintaining Provenance and Cross-Linking
- **Assign UUIDs:** Each legacy file gets a UUID, tracked in `HARMONIZATION_MATRIX.md`. New canonical docs list the UUIDs of their "parent" files in their provenance block.
- **Link with Intent:** Use descriptive link text that explains relationships, not just file paths.
- **Broken Links Test:** Implement a link-checker in CI/CD to block merges with broken links.

## 3. Strategies for Deduplication and Harmonization
- **Scaffold and Fill:**
  - Create a new doc from the Canonical Template (the scaffold).
  - Read all legacy drafts.
  - Copy the best content from each into the scaffold, then synthesize into a single, coherent voice (the fill).
- **Glossary as Arbiter:** Canonical glossary terms override conflicting terminology.
- **Embrace the Archive:** Once a legacy file is harmonized into a canonical doc, move the original to `archive/` with a note in the matrix. Only one source of truth remains in the main structure.

## 4. Final Recommendation: The Path Forward
- Formalize this protocol in `grimoire/guides/harmonization_protocol.md`.
- Begin with the Identity & Onboarding cluster.
- Ensure all future contributors follow this sacred process for the Great Work.

---

*This protocol is the foundation for all future harmonization and migration efforts in ThinkAlike. All agents and contributors must adhere to these principles to maintain the integrity and clarity of the knowledge base.*
