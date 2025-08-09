---
title: ThinkAlike Canonical Visual Identity & Style Guide
version: 4.0.0
status: Canonical
last_updated: 2025-06-19
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
tags:
- accessibility
- branding
- clarity_protocol
- pet_clarity
- style
- style_guide
- symbolic_ux
- visual_identity
harmonization_note: This document unifies all visual, branding, and aesthetic standards
  for ThinkAlike. It supersedes all previous visual identity and style guides.
---


# ThinkAlike Canonical Visual Identity & Style Guide

## 1. Aesthetic Philosophy: The Alchemical Interface
- **Symbolic & Mythopoetic:** The UI and docs are ritual spaces. Visuals are glyphic, meaningful, and evoke a cosmic, sacred tech feel.
- **Minimalist & Clear:** Prioritize clarity and focus, avoid clutter. Calm, clean, intentional design.
- **Resonant & Alive:** Use subtle, layered animations (light pulses, waveforms) for a sense of life and responsiveness.
- **Ethical & Accessible:** Design must be inclusive, transparent, and empowering, meeting or exceeding **WCAG AAA** standards.

## 2. Canonical Color Palette

| Category         | Name/Usage                | HEX       | Usage Notes                                                                 |
|------------------|--------------------------|-----------|-----------------------------------------------------------------------------|
| **Primary**      | ThinkAlike Orange        | `#F2681A` | Main branding color, logo, headers, key UI/document elements                |
| **Highlight**    | Neon Orange              | `#FF5E00` | Neon light effect, CTAs, notifications, errors, interactive elements (sparingly) |
| **Neutral**      | Amber/Honey Yellow       | `#FFBF00` | Neutral highlights, secondary UI, backgrounds                               |
| **Accent**       | Electric Blue            | `#00FFFF` | Accents, icons, waveform, links, never for body text                        |
| **Background**   | Cosmic Black             | `#000000` | Main background, document/page backgrounds                                  |
| **Text**         | White                    | `#FFFFFF` | Main text on dark backgrounds                                               |
| **Connection**   | Deep Ruby                | `#800000` | Trust, connection, special status, badges                                   |
| **Ruby Highlight** | Ruby Highlight         | `#E60000` | Visual highlights only, not for text, use very sparingly                    |
| **Ruby Shadow**  | Ruby Shadow              | `#3F0000` | Subtle gradients, outlines, shadow effects                                  |
| **Secondary**    | Dark Blue                | `#001F3F` | Waveform, subtle accents, backgrounds, dividers                             |
| **Special Accent** | Aetheric Magenta         | `#E60BAF` | For rare, high-impact notifications or unique UI states. Use very sparingly. |

**Neon Orange Note:** For a true neon effect, use `#FF5E00` as the base and add a glow (CSS: `text-shadow: 0 0 8px #FF8C00, 0 0 16px #FF5E00;`).

---

## 3. Typography
- **Headings:** Montserrat, bold, all-caps
- **Body:** Open Sans or Inter, regular
- **Code/Monospace:** Fira Mono or Consolas
- **Wordmark:** Neue Haas Grotesk (logo only)

---

## 4. Iconography & Glyphs
- Use custom glyphs for realms, agents, and protocols (see `/assets/` for SVGs)
- Use Lucide or Feather icons for UI elements
- Chrona symbol: ⧖ (U+29D6)
- All glyphs used as interactive elements MUST have an `aria-label` or accessible text alternative.

---

## 5. Motion & Animation
- Motion should be meaningful, guiding attention and enhancing the sense of a living system.
- Examples: Gentle pulse of the `AIWaveformIndicator`, flowing lines of the `DataTraceability` graph.
- All animations must respect the `prefers-reduced-motion` media query.

---

## 6. UI & Document Structure
- **Layout:** Flexible grid system. Spacing based on a consistent scale (4px, 8px, 16px, 24px, 32px).
- **Component Reference:** See `docs/ui_components/` and the [UI Component Development Guide](../guides/development/frontend/ui_component_guide.md).
- **Document Styling:** Use the canonical color palette for headings, highlights, and callouts. Match document backgrounds and headers to UI style for visual unity.

---

## 7. Logo Usage
- **Primary Logo (Horizontal):** `/assets/logo.svg` or `/assets/logo.png` (logo + wordmark right)
- **Stacked Logo (Square):** `/assets/logo_square.svg` or `/assets/logo_square.png` (logo + wordmark below)
- Use PNG for universal compatibility if SVG causes issues.
- Maintain clear space around the logo (at least the height of the "T" in "ThinkAlike").
- Do not alter, stretch, or re-color the logo. For monochrome, consult lead designers.

---

## 8. Infographic & Slide Design
- Use clear, minimal layouts with whitespace.
- Visual hierarchy: Title → Key Concept → Diagram → Call to Action.
- Always include the ThinkAlike logo and color bar.
- Use flowcharts, mind maps, and symbolic diagrams to explain complex ideas.

---

## 9. Example Infographic Concepts
- "How ThinkAlike Works" (User Journey Flow)
- "Chrona Economy at a Glance" (UBI, Wallet, Value Exchange)
- "Agent Swarm Protocols" (Aggregate, Reflect, Debate)
- "Noetica: The Living Academic Engine"

---

*This document is the single canonical source for ThinkAlike's visual identity and style. All new design, frontend, and document work must adhere to these standards. Archive or remove previous guides to avoid confusion.*