---
title: Profile Display Component
version: 3.0.0
status: Canonical
last_updated: 2025-07-07
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
spec_id: COMP-UI-001
tags:
  - component
  - ui
  - profile
  - identity
  - transparency
---

# Profile Display Component

- **Version:** 3.0.0
- **Status:** Canonical
- **Date:** 2025-07-07
- **Related Documents:**
  - [[protocols/trust_protocol|Trust Protocol]]
  - [[guides/ethical_ui_ux_principles|Ethical UI/UX Principles]]
  - [[docs/style/visual_style_guide.md|Visual Style Guide]]

## 1. Overview & Purpose

The `ProfileDisplay` component is the canonical vessel for the "Ritual of Recognition"—the symbolic act of witnessing and understanding identity within ThinkAlike. It serves as the primary UI for presenting a user's profile, including their symbolic representations, core values, and trust indicators.

Its design is governed by the **Ethical UI/UX Principles**, prioritizing:
- **Data Sovereignty:** Users control which profile fields are visible and to whom.
- **Transparency:** All displayed information is clearly labeled. AI-inferred values are explicitly marked.
- **Data Minimization:** Only essential information is displayed by default, with options to expand for more details with user consent.

## 2. Visual & Functional Elements

The component has several key visual elements that represent different facets of a user's identity.

### 2.1. Core Identity
- **Avatar/Sigil:** The user's chosen primary visual representation.
- **Display Name:** The user's chosen name.
- **Initiation Glyph:** A primary visual anchor representing the user's archetypal journey.
- **Echo Phrase:** A user-defined motto or phrase, often displayed as a subtitle or on hover.

### 2.2. Trust & Reputation Badges
This is a dedicated area for displaying symbolic badges earned through the **Trust Protocol**. These are not "achievements" in a gamified sense, but visual attestations of community standing.

- **Vouching Badge:** Indicates that the user has been vouched for by others. The detail might show *who* vouched for them if the viewer is within the same trust network.
- **"Mended Weave" Badge:** A powerful symbol indicating successful completion of a restorative justice process, demonstrating accountability.
- **Hive Membership Badge:** Displays the sigil of the Hive(s) the user belongs to, indicating community affiliation.
- **Resonance Badges:** May indicate a high degree of resonance in specific areas (e.g., "Narrative Synchrony") with the *viewer*, calculated contextually.

### 2.3. Resonance Overlays
These are dynamic, often subtle visual cues that reflect the real-time resonance state between the viewer and the profile being viewed.
- **Visual Aura/Waveform:** A subtle visual effect whose color or intensity is based on the **Identity Resonance Score (IRS)** between the two users.
- **Constellation Cues:** Highlights shared connections within the Trust Network (e.g., "You share 5 trusted connections").

## 3. Accessibility
- All images and visual elements must have descriptive `alt` text.
- All interactive elements must be keyboard accessible and have appropriate `aria-labels`.
- Color contrast must meet or exceed WCAG AAA standards.
- Screen readers must be able to announce all visible fields, and visual-only indicators must have text alternatives.

## 4. Ethical Alignment & PET
- **No Dark Patterns:** All profile actions are opt-in, non-coercive, and clearly labeled.
- **User Control:** The user has final say over what is displayed on their profile via a dedicated management interface.
