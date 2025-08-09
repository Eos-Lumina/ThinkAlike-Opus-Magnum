---
folder_type: documentation
status: Active
last_updated: 2025-06-22
maintainers: [Architectural Stewards]
---

# Chrona - Temporal Architecture

## Purpose
This directory contains the architectural documents for **Chrona**, the ThinkAlike system that governs time, memory, and symbolic history. Chrona is more than a ledger; it's the framework that models how events, rituals, and trust evolve over time, forming the narrative backbone of the user experience.

## Key Documents

### Core Concepts & Protocols
- **[`chrona_currency_of_time.md`](./chrona_currency_of_time.md)**: The foundational specification for the platform's time-based currency, where users earn "Chrona" for their presence and contributions, not just their output.
- **[`temporal_resonance_protocol.md`](./temporal_resonance_protocol.md)**: Defines the mechanics of how trust, memory, and symbolic presence evolve. It outlines the rules for memory decay and the influence of events over time.
- **[`ritual_temporality_engine.md`](./ritual_temporality_engine.md)**: Describes how rituals can alter the perception and mechanics of time within the system, affecting memory decay and symbolic weight.

### Data & Security Models
- **[`chrona_event_model.md`](./chrona_event_model.md)**: Defines the standardized data structure for all events logged in the Chrona ledger, detailing the symbolic and technical fields.
- **[`chrona_user_log_index_spec.md`](./chrona_user_log_index_spec.md)**: The specification for the user-facing symbolic event log, which records an individual's journey through reflections, rituals, and identity changes.
- **[`chrona_security_privacy.md`](./chrona_security_privacy.md)**: Outlines the security principles and privacy models for protecting users' symbolic memories and ritual expressions.

## Usage
These documents are essential for developers working on the backend systems related to user history, governance, and any feature that interacts with the flow of time and memory in the platform.

## Dependencies
- `docs/realms/`
- `docs/rituals/`
- `docs/noetica/chrona_currency_of_time.md` (The philosophical paper)

---
For more information, see the specific documents linked above.
