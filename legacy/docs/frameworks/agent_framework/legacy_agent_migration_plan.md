---
title: ARCHIVED: Legacy & Unaligned Agent Migration Plan (Blueprint Draft)
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
tags: []
---

# ARCHIVED: Legacy & Unaligned Agent Migration Plan (Blueprint Draft)

> **This document is archived and retained for historical reference only. All current agent protocols and specs are maintained in the canonical locations: `docs/architecture/agent_framework/ai_agents/` and `agent_registry.md`. Do not update or reference this file for new work.**

This document summarizes the current state of legacy/unaligned agent protocols and provides a concrete plan for harmonizing and migrating all agent specs to canonical, project-aligned documentation.

---

## 1. Current State
- Many agent roles and protocols remain in `src/swarm/unaligned/` and `src/swarm/unaligned/migration/` as legacy or in-progress files (e.g., `rescued_agent_protocols.md`, `unaligned_agents_migration_todo.md`).
- The canonical agent registry and specs are being updated in `docs/architecture/agent_framework/ai_agents/` and `agent_registry.md`.
- Some agent roles (e.g., Knowledge Retrieval Agent, Vision Architect, Quantum Ethics Specialist) are not yet mapped to canonical specs.

## 2. Migration & Harmonization Checklist
- [ ] Review all files in `src/swarm/unaligned/` and `src/swarm/unaligned/migration/` for unique agent roles and protocols.
- [ ] For each agent:
    - [ ] Assign a unique, symbolic, project-aligned name.
    - [ ] Draft a canonical spec in `docs/architecture/agent_framework/ai_agents/`.
    - [ ] Update `agent_registry.md` with the new entry and cross-links.
    - [ ] Mark legacy files as archived or migrated.
- [ ] Ensure all agent specs are harmonized with SYSTEM_BLUEPRINT.md and protocol docs.
- [ ] Remove or archive all deprecated/unaligned agent files after migration is complete.

## 3. Contributor Guidance
- Non-developers and new contributors should reference only the canonical agent registry and specs.
- Legacy/unaligned files are for migration and historical reference only.

## 4. Next Steps
- Assign migration tasks to contributors or agents.
- Track progress in `unaligned_agents_migration_todo.md` and update this plan as agents are harmonized.

---

*Update this plan as migration progresses. Use as a reference for agent system harmonization and onboarding.*
