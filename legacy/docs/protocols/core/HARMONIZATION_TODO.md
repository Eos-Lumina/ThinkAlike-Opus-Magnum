# Core Protocols Harmonization To Do

This file lists the actions required to harmonize the core protocol cluster, based on comparison of canonical and legacy protocols.

## 1. Inventory & Comparison
- Canonical protocols present: agent_context_protocol, agent_handoff_protocol, agent_memory_protocol, agent_persona_protocol, agent_registry_protocol, ai_driven_workflow_protocol, alchemical_development_protocol, architecture_fork_protocol, consent_protocol, contradiction_flagging_protocol, epistemic_reflection_protocol, fork_resistance_protocol, global_agent_bootstrap_protocol, interaction_protocol, resonance_logic_protocol, resonance_matching_protocol, temporal_dynamics_protocol, temporal_resonance_protocol, trust_protocol
- Legacy/alternate protocols found: multiple versions of each above, with v1.0/v1.1 drafts, some with unique content or alternate maintainers.

## 2. Harmonization Actions Needed
- [ ] Review all legacy protocol versions for unique content, rationale, or implementation notes not present in canonical v3.0.0 files.
- [ ] For each protocol, ensure canonical file:
    - Has up-to-date frontmatter (authors, version, last_updated, tags, references)
    - Incorporates any valuable legacy rationale, diagrams, or implementation notes
    - References legacy provenance in a migration note if significant changes were made
- [ ] Archive all legacy protocol drafts to `_legacy/archived_protocols/` if not already present, with a migration log entry
- [ ] For protocols with major changes (e.g., agent_memory_protocol, agent_persona_protocol), propose a harmonized canonical version that merges best of both
- [ ] Update manifest.yaml and STRUCTURE_MANIFEST.md if protocol list or structure changes
- [ ] Add redirect/README notes in legacy locations if needed

## 3. Documentation & Logging
- [ ] Log all migrations, harmonizations, and archival actions in migration_log.yaml and migration_log_entry_2025-07-08.md
- [ ] Update protocols_index.md and protocols_overview.md to reflect harmonized state

---

Repeat this process for each protocol in the core cluster. When complete, proceed to the next cluster (e.g., identity, chrona, governance, etc.).
