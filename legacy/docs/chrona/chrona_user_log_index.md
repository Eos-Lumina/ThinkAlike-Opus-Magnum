---
title: Time-Based Currency & Digital Citizenship Specification
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Time-Based Currency & Digital Citizenship Specification

## Purpose
Reward contributors with “Hour Tokens” for time spent, not output; enable digital citizenship and participatory governance.

## Features
* Time ledger logs hours contributed (manual or session-based)
* Earn non-transferable “Hour Tokens” for time spent
* Tokens can be exchanged for recognition, privileges, or gifted
* Contributors with sustained engagement can propose/vote on features, moderate, or steward swarms
* Rights and responsibilities are transparent and opt-in
* Proposals and voting weighted by engagement and diversity, not just time

## API & Data Model
* `TimeLedger`, `HourToken`, `Proposal`, `Vote`, `CitizenProfile`
* `/ledger` (view, log hours)
* `/tokens` (view, gift, redeem)
* `/governance/proposals` (create, vote)

## UI/UX Notes
* Dashboard for tracking hours and tokens
* Governance portal for proposals and voting
* All participation is opt-in and privacy-respecting

## Security/Ethics
* No transfer of tokens for money
* All governance actions are transparent and auditable
* Participation is voluntary and revocable

## Example User Flow
1. Contributor logs hours via dashboard or session tracking
2. Earns Hour Tokens, visible in their profile
3. Uses tokens to propose a new feature or vote on an initiative

---

# Chrona User Log Index

## Purpose

Maintains a symbolic and accessible record of each user’s time-bound contributions, reflections, rituals, and identity changes.

---

## Structure

Each user log is stored as a chain of symbolic events, cross-linked by archetype and glyph activity.

---

## Example Log Entry

```json
{
  "timestamp": "⧖2025-05-21T03:18Z",
  "type": "glyph_alignment",
  "glyphs": ["The Mask", "The Phoenix", "Water"],
  "context": "Shared with user//mythos-mirror",
  "echo_index": 2
}
```

Semantic Views
Timeline Mode (linear chronological)

Constellation Mode (symbolic clusters)

Reflection Mode (only internal/private entries)

Accessibility
Always visible to the user

Entries can be anonymized for public viewing

Reflections can be spoken, drawn, or ritual-logged

Developer Notes
Allow export as poetic archive or ritual script

Auto-generate resonance summary every 30 days

yaml
Copy
Edit

---

### 📄 `ritual_temporality_engine.md`

```markdown
# Ritual Temporality Engine

## Purpose
Models how rituals alter time perception, resonance accumulation, and symbolic memory flow in the Chrona system.

---

## Ritual Time Types

| Type               | Description                                 |
|--------------------|---------------------------------------------|
| Linear Ritual      | Sequential, time-anchored                   |
| Looping Ritual     | Recurs in cycles (e.g. lunar, solstice)     |
| Asynchronous Echo  | Fragments emerge across different users     |
| Transcendent Merge | Temporally fused symbolic experiences       |

---

## Time-Bending Properties

- Some rituals bend memory decay (freeze or amplify)
- Rituals may shift Chrona event causal weight
- Peak resonance moments “compress” time (higher symbolic intensity)

---

## Example

A user performs a Dream Mirror ritual on solstice:
- Time slows in UI feedback
- Chrona logs “temporal dilation”
- Memory gains extra 7-day half-life

---

## Developer Notes

- Define ritual templates with temporal affordances
- Link with symbolic_ecology_map to localize effects
```
