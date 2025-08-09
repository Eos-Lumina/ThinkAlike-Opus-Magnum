---
id: "d9e8f7c6-5b4a-4938-8c1e-9a0b1c2d3e4f"
aliases:
  - "Harmonization Protocol"
  - "Documentation Canonicalization Process"
tags:
  - "protocol"
  - "meta"
  - "governance"
  - "documentation"
  - "migration"
version: "3.0.0"
status: "canonical"
created_date: "2024-07-08"
updated_date: "2024-07-08"
authors:
  - "ThinkAlike Team"
reviewers:
  - "Core Architecture Guild"
  - "Stewards of Lore"
---

# Protocol: Documentation Harmonization

## 1. Overview

This protocol establishes the formal, canonical process for the migration, harmonization, and consolidation of all ThinkAlike documentation. Its purpose is to ensure zero data loss, full provenance, and the creation of a single, unambiguous source of truth for every concept in the ecosystem. It treats documentation as a sacred library restoration, not a simple file transfer.

## 2. Core Principles

- **Single Source of Truth**: For any given protocol, concept, or component, only one canonical document may exist. All others must be archived or explicitly marked as superseded.
- **Immutable Provenance**: All canonical documents must trace their lineage back to the legacy sources they replace. This is non-negotiable.
- **Clarity and Coherence**: The goal is to produce a unified, coherent, and easily navigable body of knowledge, free from contradiction and ambiguity.
- **Ritualized Process**: Harmonization is a deliberate, structured ritual, not an ad-hoc cleanup. It must follow the defined stages to prevent chaos.

## 3. The Harmonization Process

### 3.1. Stage 1: Audit & Mapping

- **Identify a Cluster**: Select a logical group of related legacy documents for harmonization (e.g., all protocols related to agent identity).
- **Assign UUIDs**: Assign a unique identifier to every legacy file being processed.
- **Create Audit Log**: Maintain a central, version-controlled audit log (e.g., `migration_audit.md`) that tracks the UUID, original path, status (e.g., `migrated`, `superseded`, `duplicate`), and the ID of the new canonical document for every legacy file.

### 3.2. Stage 2: Synthesis & Canonicalization

- **Appoint a Scribe**: A single agent or contributor is designated as the Master Scribe for a given cluster to prevent conflicting versions.
- **Scaffold and Fill**: 
    1. Create a new, empty canonical document using the appropriate v3.0.0+ template (the "scaffold").
    2. Carefully review all related legacy documents.
    3. Synthesize the essential, non-redundant information from the legacy sources into the new scaffold, harmonizing terminology and structure (the "fill").
- **Embed Provenance**: In the frontmatter of the new canonical document, list the UUIDs of all legacy files it supersedes.

### 3.3. Stage 3: Review & Archival

- **Peer Review**: The newly created canonical document is submitted for review by the relevant guild (e.g., Core Architecture, Ethics).
- **Mark for Deletion**: Once approved, the legacy files are marked for deletion in the audit log. The physical files should not be deleted until the entire migration phase is complete and validated.
- **Update Master Index**: The new document is added to the project's master index or manifest.

## 4. Tooling and Enforcement

- **Link Integrity**: Automated checks (e.g., CI/CD pipeline steps) should be used to detect and prevent broken links within the documentation.
- **Glossary as Arbiter**: The `Canonical Glossary` is the final arbiter for all terminology. All documents must align with it.
- **Template Enforcement**: New documentation should be created from standard templates to ensure structural consistency.

## 5. Governance

This protocol is a foundational component of project governance. Any proposed deviations from this process must be formally reviewed and approved by the Core Architecture Guild and the Stewards of Lore.
