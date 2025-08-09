---
title: Archive: ai_agents_README.md
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Archive: ai_agents_README.md

This file was moved from docs/architecture/agent_framework/ai_agents/ as part of the project archive consolidation.

---

# AI Agents: Canonical Specifications

This directory contains harmonized, canonical specifications for all implemented AI agents in the ThinkAlike ecosystem. Each spec should include:

- Purpose and narrative/ethical role
- Protocol and architecture alignment
- Key methods and integration points
- Versioning and persona references
- Links to code and persona YAML files

## Agent Specs
- `eos_lumina_agent_spec.md`: Eos Lumina (orchestrator, ethical guardian)

## Related Documentation
- **Agent Framework Protocols:** See parent directory for protocols (context, memory, persona, registry, etc.)
- **Unaligned/Legacy Agents:** For legacy, unaligned, or in-migration agent protocols, see [`src/swarm/unaligned/`](../../../../src/swarm/unaligned/)
    - Core directives and registry: [`core/`](../../../../src/swarm/unaligned/core/)
    - Migration tracker and legacy protocols: [`migration/`](../../../../src/swarm/unaligned/migration/)

## TODO
- Add specs for all additional agents as they are implemented (e.g., Harmonia, Diogenes, etc.)
- Ensure each spec is cross-linked to its code and persona definition
- Keep this README and all specs harmonized with the SYSTEM_BLUEPRINT.md and agent framework protocols
