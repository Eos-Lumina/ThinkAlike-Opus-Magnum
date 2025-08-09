# Noosphere Engine

## Purpose
The Noosphere Engine is the distributed, auditable knowledge ledger at the heart of ThinkAlike. It powers collective intelligence, transparent information sharing, and protocol alignment for all agents and realms.

## Features
- Centralized, extensible knowledge storage
- Auditable entries linked to agents and realms
- REST API for add/query/update operations
- Foundation for future distributed and decentralized extensions

## Integration Points
- **Agents:** All agent modules must use the Noosphere Engine for knowledge storage and retrieval.
- **Realms:** Realms reference the engine for models, endpoints, and UI flows.
- **Protocols:** Protocols use the engine for decision-making, value alignment, and traceability.
- **Specialized Systems:** Chrona Wallet, governance, and economic modules integrate for identity, transaction, and audit history.

## Example Usage
```python
from src.noosphere_engine.engine import NoosphereEngine
engine = NoosphereEngine()
engine.add_entry("user_profile_123", {"name": "Alice", "score": 42}, agent_id="agent_1", realm="Hives")
profile = engine.query("user_profile_123")
```

## API Endpoints
- `POST /noosphere/add`: Add a knowledge entry
- `GET /noosphere/query`: Query a knowledge entry
- `GET /noosphere/all`: List all entries

## Roadmap
- Add distributed storage and consensus
- Implement audit trail and versioning
- Expand API for advanced queries and analytics

## Alignment
All modules, agents, and protocols must reference and integrate with the Noosphere Engine. Update the master blueprint and onboarding scripts to enforce this alignment.
