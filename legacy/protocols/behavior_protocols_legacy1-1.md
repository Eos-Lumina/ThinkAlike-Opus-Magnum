# behavior_protocols

Behavior protocols for mythic agents in ThinkAlike. Defines expected behaviors, fallback logic, and collaboration rules for all agent classes.

---

## Core Protocols

- All agents must log actions to the trace engine.
- Fallback to swarm consensus if a protocol fails.
- No agent may overwrite another’s log without explicit merge.
- All onboarding and handoff events must be auditable.

---

migration_note: Migrated from old_ThinkAlike/docs/ai_agents/.
