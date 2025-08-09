# Resonance Network Data Model & Matching Algorithm

This document describes the data structures and matching algorithm for the Resonance Network in ThinkAlike.

## Resonance Network Data Structures
- **UserNode**: Represents a user in the network.
    - `user_id`: Unique identifier
    - `value_profile`: UserValueProfile object
    - `intro_video`: Link or metadata
    - `connections`: List of Connection objects
    - `location`: Optional geolocation/affinity cluster
- **Connection**: Represents a potential or established relationship.
    - `source_id`: UserNode initiating connection
    - `target_id`: UserNode being approached
    - `resonance_score`: Numeric value (0-1)
    - `status`: [potential, active, declined, retired]
    - `consent`: Boolean
    - `history`: List of interaction events
- **ResonanceMap**: Graph structure of all UserNodes and Connections.
    - `nodes`: List of UserNode objects
    - `edges`: List of Connection objects
    - `clusters`: Optional affinity/geolocation clusters

## Matching Algorithm (Outline)
1. For each UserNode, retrieve their `value_profile` and preferences.
2. Calculate resonance scores between UserNode and all other nodes using:
    - Value alignment (profile similarity)
    - Shared affinities (clusters, interests)
    - Historical interactions
3. Filter connections by consent and status.
4. Recommend top matches based on highest resonance scores and mutual consent.
5. Initiate Narrative Duet protocol for compatibility testing.

## Next Steps
- Implement data structures in `src/algorithms/`.
- Integrate with onboarding, portal, and agent modules.
- Document API and data flow for matching and resonance network operations.
