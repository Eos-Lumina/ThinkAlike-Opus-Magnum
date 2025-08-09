---
title: AITriangleIndicator Component
document_status: Harmonized
version: 1.0.1
last_updated: 2025-06-07
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
alignment_tags:
- clarity_protocol
- pet_compliant
- accessibility_AAA
- ai_presence
- symbolic_interface
related_components:
- AIWaveformIndicator
- NarrativeViewer
- LoadingSpinner
visual_style_guide_ref:
- ../style/canonical_visual_style_guide.md
tags:
- indicators
---


![ThinkAlike Logo](../../assets/logo.svg)

# AI Triangle Indicator

A core interactive element for AI-driven feature awareness.

<em>ThinkAlike: Connecting like minded individuals.</em>

---
<!-- METADATA LAYER -->
<div style="font-family: 'Courier New', monospace; font-size: 0.9em; color: #666666; margin-bottom: 2em; padding: 1em; border: 1px dashed #333333; background-color: #1a1a1a;">
  <p><strong>DOCUMENT STATUS</strong> ::: Harmonized - Finalized</p>
  <p><strong>VERSION</strong> ::: 1.0.1</p>
  <p><strong>LAST UPDATED</strong> ::: 2025-06-07</p>
  <p><strong>MAINTAINED BY</strong> ::: UI Systems Guild, Eos Lumina∴</p>
  <p><strong>ALIGNMENT TAGS</strong> ::: <code>[clarity_protocol]</code> <code>[pet_compliant]</code> <code>[accessibility_AAA]</code> <code>[ai_presence]</code> <code>[symbolic_interface]</code></p>
  <p><strong>RELATED COMPONENTS</strong> ::: <code>[AIWaveformIndicator]</code> <code>[NarrativeViewer]</code> <code>[LoadingSpinner]</code></p>
  <p><strong>VISUAL STYLE GUIDE REF</strong> ::: <code>[../style/canonical_visual_style_guide.md]</code></p>
</div>

---

## Overview
The AITriangleIndicator is a symbolic UI marker that highlights AI-driven features, recommendations, or actions within the ThinkAlike ecosystem. It supports transparency, user agency, and symbolic interaction by making AI involvement visually explicit, in line with ThinkAlike’s PET/Clarity protocols and ritual requirements.

## Visual Representation & States
- **Visual:** Stylized, equilateral triangle (typically right-pointing or upward) rendered in dark mode by default, with glowing accents. Uses "Neon Orange Highlight" (#FF8C00) or "Deep Ruby (Connection)" (#800000) for the triangle, as per the canonical_visual_style_guide.md and triangle motif mockups. May be contextualized within a node-graph or ritual UI. Typography for any associated text: Montserrat (headers), Open Sans (body).
- **States:**
  - Default: Static triangle, accent color.
  - Active: Animated pulse or glow for active AI processing/recommendation.
  - Disabled: Muted color, reduced opacity.
  - Error: **Error Red (#FF4136) border or color for error states.**
- **Mockup:** [Link to /docs/assets/visuals/ai_triangle_indicator_mockup.png or Storybook entry]
- **Alignment:** Strict adherence to ThinkAlike’s color, spacing, and iconography standards. All states use high-contrast, glowing effects for accessibility and symbolic resonance.

## Functional Specifications
- **Behavior:**
  - Appears near or within AI-driven UI elements (recommendations, auto-complete, AI-generated content).
  - May animate/pulse when AI is processing.
  - Tooltip or accessible label: "AI-driven feature" or context-specific description.
- **Props/Attributes:**
  - `active` (boolean, default: false): Active/animated state.
  - `disabled` (boolean, default: false): Muted/disabled state.
  - `error` (boolean, default: false): Error state.
  - `aria-label` (string, optional): Accessible label for screen readers.
  - `size` (string|number, default: 'md'): Size ('sm', 'md', 'lg', or px value).
- **Events:** None (presentational only).

## Usage Guidelines
- **When to Use:**
  - To mark features/content/actions as AI-generated or AI-assisted.
  - To reinforce user agency and transparency about AI involvement.
- **Best Practices:**
  - Always provide an accessible label or tooltip.
  - Use only for genuinely AI-driven elements.
  - Ensure color contrast and size for accessibility.
- **Accessibility:**
  - Must include `aria-label` or tooltip.
  - Use `role="img"` if presentational, or `role="button"` if interactive.
  - Keyboard focusable and Enter/Space to activate if interactive (rare).
  - Screen reader announces label and state.
  - All color/animation cues are perceivable by assistive tech and meet WCAG AAA contrast.

## Ethical & PET Considerations
- **Cognitive Liberty:** No manipulative formatting; clear, honest signaling of AI involvement.
- **Radical Transparency:** Symbolizes AI presence; tooltip/label clarifies context.
- **Consent Management:** Does not handle user data or consent directly.
- **Data Minimization:** Purely presentational; no data collection.
- **Clarity Protocol Adherence:** Function and purpose are immediately clear.

## Symbolic Alignment (Unique to ThinkAlike)
- Embodies the ThinkAlike triangle symbol for "AI presence" and "guidance."
- Placement/animation are subtle but unmistakable, supporting the "Ritual over Interface" experience.
- Reflects the persona and ethical boundaries of Eos Lumina (AI agent).

## ✨ Contextual Use Cases in Portal & Resonance Network (2025 Harmonization)

The AITriangleIndicator is reserved for marking **discrete, AI-driven features, recommendations, or content snippets**—not general AI narration (see AIWaveformIndicator). Its use is tightly scoped to maintain its PET/Clarity and symbolic significance.

### **Portal Realm**
- **AI-Suggested Choices:** If Eos Lumina∴ offers a choice that is *algorithmically suggested* based on the user's evolving `UserValueProfile` (beyond standard narrative branching), that choice is marked with the triangle (e.g., “AI-suggested reflective path”).
- **Profile Summaries:** When a summary or insight (e.g., “Your dominant archetype seems to be Seeker”) is *explicitly an AI inference*, the indicator is shown.
- **Connected Services:** If the system recommends specific services or integrations based on user data, those suggestions are marked.

### **Narrative Duets**
- **AI Clone Highlights:** If the AI Clone of User B makes a *system-highlighted bridging suggestion* or insight, the triangle marks it.
- **AI-Generated Summaries:** After a Duet, if Eos provides an *AI-generated summary of key alignment points* (with consent), the indicator is used.

### **Resonance Network**
- **Resonance Priming:** When the system highlights certain User Nodes or pathways as “AI-suggested resonant pathways,” the triangle is used as a visual cue.
- **Advanced Filtering:** If AI helps filter or sort nodes based on complex, user-defined criteria, the indicator marks those results.

**Best Practice:**
- **Do not overuse.** Only apply to genuinely AI-driven, discrete elements. Overuse dilutes its meaning and PET/Clarity value.
- **Accessible Labeling:** Always provide a context-specific `aria-label` (e.g., “AI-suggested reflective path,” “AI-generated summary,” “AI-enhanced search result”).

---

## 🔒 PET/Clarity & Symbolic Alignment (2025 Harmonization)
- **Explicit AI Signaling:** The triangle provides clear, honest signaling of *specific* AI involvement, supporting user agency and transparency.
- **Symbolic Meaning:** Embodies “AI presence for this specific item”—not general agent presence.
- **Consent & Data:** Never used to mark content involving user data without explicit, revocable consent.
- **Accessibility:**
  - `aria-label` must always be present and contextually descriptive.
  - Use `role="img"` unless interactive (rare).
  - All color/animation cues must meet or exceed WCAG AAA contrast and be perceivable by assistive tech.

---

## 🧭 Example Usage Scenarios

- **Portal:**
  - A choice in a narrative fork is marked with the triangle and `aria-label="AI-suggested reflective path"`.
  - A summary card reads “Your dominant archetype: Seeker” with the triangle and `aria-label="AI-inferred archetype"`.
- **Duet:**
  - An AI Clone’s suggestion is marked with the triangle and `aria-label="AI-bridging suggestion"`.
  - A post-Duet summary is marked with `aria-label="AI-generated alignment summary"`.
- **Resonance Network:**
  - A node or pathway is highlighted with the triangle and `aria-label="AI-suggested resonant pathway"`.

---

## Code Snippets / Implementation Details (Optional)
```jsx
import React from 'react';
import PropTypes from 'prop-types';

export function AITriangleIndicator({ active, disabled, error, ariaLabel, size = 'md' }) {
  return (
    <svg
      width={size === 'sm' ? 12 : size === 'lg' ? 32 : 20}
      height={size === 'sm' ? 12 : size === 'lg' ? 32 : 20}
      viewBox="0 0 20 20"
      aria-label={ariaLabel || 'AI-driven feature'}
      role="img"
      style={{
        opacity: disabled ? 0.4 : 1,
        filter: error ? 'drop-shadow(0 0 2px #FF4136)' : active ? 'drop-shadow(0 0 4px #00f6ff)' : 'none',
        transition: 'filter 0.2s',
        fill: error ? '#FF4136' : disabled ? '#bdbdbd' : '#00f6ff',
      }}
    >
      <polygon points="10,2 18,18 2,18" />
    </svg>
  );
}

AITriangleIndicator.propTypes = {
  active: PropTypes.bool,
  disabled: PropTypes.bool,
  error: PropTypes.bool,
  ariaLabel: PropTypes.string,
  size: PropTypes.oneOfType([
    PropTypes.string,
    PropTypes.number,
  ]),
};
```

## Changelog
- **2025-06-08 :: v1.1.0 :: HARMONIZED** – Expanded contextual use cases for Portal and Resonance Network. Clarified PET/Clarity, symbolic, and accessibility requirements. Added explicit best practices and example scenarios. Updated for 2025 harmonization and cross-realm alignment.
- **2025-06-07 :: v1.0.1 :: UPDATE** – Standardized error state visual cues to use Error Red (#FF4136).
- **2025-06-07 :: v1.0.0 :: GENESIS** – Initial harmonized documentation, standardized to canonical template, PET/Clarity/symbolic alignment.
