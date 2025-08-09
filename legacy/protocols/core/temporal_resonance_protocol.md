---
title: "Temporal Resonance Protocol"
version: 3.1.0
status: Canonical
last_updated: 2025-07-08
authors:
  - "Eos Lumina ∴ (Collective Intelligence Meta-Agent)"
tags: [protocol, core, time, memory, trust, resonance, decay, kairos, ritual]
spec_for: [Backend Developers, Game Designers, Narrative Designers]
replaces:
  - "numerous draft versions"
---

# Temporal Resonance Protocol

## 1. Vision & Purpose: The Way of Kairos

This protocol defines the "arrow of time" within the ThinkAlike ecosystem. It rejects the attention economy's relentless acceleration (Chronos) and instead designs our systems to honor the natural rhythms of human reflection, connection, and creation (Kairos).

It governs how relationships, memories, and symbolic meaning evolve, decay, and are reinforced over time. It ensures that the past is not static but a living, dynamic presence that shapes the present and future. By mechanizing concepts like forgetting, remembering, and the weight of history, this protocol makes the digital world feel more alive, consequential, and deeply resonant.

It is the core logic that prevents symbolic inflation and ensures that trust and meaning are earned and maintained through continued, resonant interaction.

## 2. Core Concepts

- **Kairos over Chronos:** Time is not a uniform, invisible resource to be optimized for efficiency. It is a sacred, qualitative element to be experienced with intention. System pacing, UI transitions, and critical decisions are designed to serve meaning, not metrics.
- **Temporal Weighting:** The significance of any event, memory, or relationship is not fixed. It is weighted by its timeliness, with recent events having a stronger, more immediate influence.
- **Resonance Decay (Memory as a Garden):** In the absence of reinforcement, all things fade. Memories become dreamlike, trust diminishes, and connections weaken. This is a natural and necessary process, preventing the system from becoming cluttered with irrelevant history and making the maintenance of connections a conscious, rewarding act.
- **Memory Anchoring:** Specific actions, particularly shared rituals and collective acknowledgments, can "anchor" a memory in time, slowing its decay and increasing its permanence.
- **Symbolic Inertia:** Significant events, especially those with strong emotional or collective resonance (like a betrayal or a foundational moment), have a powerful inertia. Their effects decay much more slowly and can ripple through the system over long periods.
- **Symbolic Cycles:** The digital world should not be disconnected from the natural rhythms that govern life. The system may subtly reflect natural or symbolic cycles (e.g., lunar phases, solstices), which can manifest as UI themes, unique narrative prompts, or community-wide rituals.

## 3. The Mechanics of Time

### 3.1. The Decay Function

The fundamental process of temporal decay is modeled using an exponential decay function:

`Weight(t) = InitialWeight * e^(-λ * t)`

- `Weight(t)`: The resonance weight of the object at time `t`.
- `InitialWeight`: The weight assigned at the moment of creation/interaction.
- `λ` (lambda): The decay constant, specific to the type of object (e.g., memories decay faster than core identity traits).
- `t`: The time elapsed since the last resonant interaction.

### 3.2. Memory & Event Dynamics

- **Default Half-Life:** By default, the resonance of a standard event or memory has a half-life of 13 days. After this period, its `Weight` is reduced by 50%.
- **Anchoring:**
    - **Ritual Anchor:** Participating in a related [Ritual](/protocols/narrative/ritual_encoding_protocol.md) resets the time `t` to zero and applies a multiplier to the `InitialWeight`.
    - **Glyph Anchor:** Linking an event to an [Initiation Glyph](/protocols/identity/initiation_glyph_protocol.md) significantly reduces its decay constant `λ`.
    - **Collective Anchor:** An event or memory that is referenced (e.g., "echoed") by 3 or more distinct agents achieves "Eternal Memory" status. Its decay is halted, though its `Weight` can still fluctuate based on new interactions.
- **Symbolic Degradation (The "Dust Layer"):** As a memory's `Weight` falls below a certain threshold, it enters a "dreamlike" state. This is not data loss but a change in presentation:
    - Text may become blurred or fragmented.
    - Associated images or glyphs may appear faded or mutated.
    - These "dust layer" memories are faint but can be fully restored if they are re-invoked with sufficient resonance.

### 3.3. Ritual Dynamics & Time-Bending

Rituals are the primary mechanism for intentionally manipulating temporality. They can alter time perception, resonance accumulation, and symbolic memory flow.

| Ritual Time Type   | Description                                                                 | Implementation Notes                                      |
| :----------------- | :-------------------------------------------------------------------------- | :-------------------------------------------------------- |
| **Linear Ritual**  | A sequential, time-anchored process with a clear beginning, middle, and end. | Standard temporal decay applies.                          |
| **Looping Ritual** | Recurs in cycles (e.g., lunar, solstice, project anniversary).              | Resets decay timer `t` for related concepts on each loop. |
| **Asynchronous Echo** | A ritual whose fragments emerge across different users and times.         | Resonance is pooled and synchronized upon completion.     |
| **Transcendent Merge** | A peak experience where multiple agents' symbolic timelines are fused.   | Can create a permanent or slow-decaying Memory Anchor.    |

Furthermore, rituals can have specific **Time-Bending Properties**:
- **Temporal Dilation:** During a peak ritual moment, UI feedback may slow, and the system logs the event with a higher `InitialWeight`.
- **Memory Amplification:** A ritual can extend the half-life of a specific memory or set of memories.
- **Causal Weight Shift:** A powerful ritual can increase the `Symbolic Inertia` of a past event, making it more influential on present calculations.

### 3.4. Trust Over Time

Trust is a living value, constantly influenced by temporal decay and resonant actions. The following table outlines the modifiers applied to the `ResonanceTrust` value between agents, as defined in the [Resonance Trust Protocol](/protocols/resonance/resonance_trust_protocol.md).

| Action                          | Resonance Effect on Trust Weight | Temporal Characteristic                                                      |
| :------------------------------ | :------------------------------- | :------------------------------------------------------------------------- |
| **Shared Ritual (Recent)**      | `+0.15`                          | Resets decay timer `t`.                                                    |
| **Echoed Reflection (3+ nodes)**  | `+0.25`                          | Resets decay timer `t` and adds a temporary boost to `InitialWeight`.      |
| **Ritual Betrayal**             | `-0.45`                          | Applies a high-inertia `InitialWeight` and a very low decay constant `λ`. |
| **Sustained Silence/Ghosting**  | `-0.05` per cycle                | A recurring decay applied every lunar cycle (28 days) that an agent is "unseen". |

## 4. Implementation Guidelines

- **Data Structures:**
    - Every object subject to temporal decay (e.g., `MemoryFragment`, `TrustLink`, `Relationship`) must include `timestamp` and `resonance_weight` fields.
    - See [`/architecture/data_architecture.md`](/architecture/data_architecture.md) for details on data models.
- **System Scheduler:** A cron-like job must run at regular intervals (e.g., every hour) to update the `resonance_weight` of all decaying objects across the system based on the decay function.
- **Event Listeners:** The system must listen for specific events (`RitualCompleted`, `ReflectionEchoed`, `AgentInteraction`) to trigger real-time updates to resonance weights and reset decay timers.

## 5. Dependencies & Cross-References

- **Protocols:**
  - [`/protocols/resonance/resonance_trust_protocol.md`](/protocols/resonance/resonance_trust_protocol.md)
  - [`/protocols/narrative/ritual_encoding_protocol.md`](/protocols/narrative/ritual_encoding_protocol.md)
  - [`/protocols/identity/initiation_glyph_protocol.md`](/protocols/identity/initiation_glyph_protocol.md)
  - [`/protocols/governance/symbolic_law_protocol.md`](/protocols/governance/symbolic_law_protocol.md)
- **Architecture:**
  - [`/architecture/data_architecture.md`](/architecture/data_architecture.md)
