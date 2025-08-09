---
title: ThinkAlike Real-Time Collaboration Architecture
status: Draft - Living Document
date: 2025-06-19
---

# Real-Time Collaboration & Swarm Presence

## Vision
Enable live, multi-user collaboration and swarm presence across all core modules (rituals, narratives, agents, resonance, sybil). Contributors see each other’s actions, presence, and system events in real time, making ThinkAlike a living, participatory platform.

## Core Components
- **WebSocket Gateway**: Central event bus for rituals, narratives, agent actions, and presence updates.
- **Presence Service**: Tracks online contributors, updates dashboard in real time.
- **Event Streams**: Rituals, narrative forks, agent invocations, and resonance matches broadcast as events.
- **Client Subscriptions**: Dashboard and VS Code extension subscribe to relevant event streams.
- **Provenance Log Sync**: All real-time events are logged for PET/Clarity and replay.

## Example Event Types
- `ritual_invoked`, `narrative_forked`, `agent_invoked`, `resonance_matched`, `user_joined`, `user_left`

## Implementation Notes
- Use Next.js API routes or a Node.js microservice as a WebSocket server (e.g., socket.io, ws, or tRPC subscription).
- All dashboard modules should be able to subscribe to and emit events.
- PET/Clarity overlays and provenance logs update in real time.
- Swarm Presence panel updates as users join/leave.

## Next Steps
- Scaffold a simple WebSocket server and client connection in the codebase.
- Refactor dashboard modules to emit and listen for events.
- Extend VS Code extension to subscribe to live event streams.

---
*This document is a living blueprint for real-time, participatory collaboration in ThinkAlike.*
