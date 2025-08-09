---
title: Button Component
document_status: Harmonized - Finalized
version: 1.1.1
last_updated: 2025-06-09
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
alignment_tags:
- UI
- Input
- Form
- Button
- PET
- Clarity
- Symbolic
- Minimalist
- accessibility_AAA
related_components:
- Form
- TextInput
- SelectDropdown
- Checkbox
- RadioGroup
visual_style_guide_ref:
- ../style/canonical_visual_style_guide.md
tags:
- controls
---


<!-- METADATA LAYER -->
<div style="font-family: 'Courier New', monospace; font-size: 0.9em; color: #666666; margin-bottom: 2em; padding: 1em; border: 1px dashed #333333; background-color: #1a1a1a;">
  <p><strong>STATUS</strong> ::: Harmonized – Finalized</p>
  <p><strong>VERSION</strong> ::: 1.1.1</p>
  <p><strong>LAST PULSE</strong> ::: 2025-06-09</p>
  <p><strong>STEWARD(S)</strong> ::: UI Systems Guild | ClarityAgent∴</p>
  <p><strong>ALIGNMENT SIGNALS</strong> ::: <code>[UI]</code> <code>[Input]</code> <code>[Form]</code> <code>[Button]</code> <code>[PET]</code> <code>[Clarity]</code> <code>[Symbolic]</code> <code>[Minimalist]</code> <code>[accessibility_AAA]</code> <code>[ritual_commitment]</code> <code>[error_red]</code></p>
  <p><strong>RESONATES WITH</strong> ::: <code>[../style/canonical_visual_style_guide.md]</code> <code>[Form]</code> <code>[TextInput]</code> <code>[SelectDropdown]</code> <code>[Checkbox]</code> <code>[RadioGroup]</code> <code>[../narrative_engine/canon/symbolic_myth_index.md]</code> <code>[../noetica/corpus_magnus/art_aesthetics_and_culture/ritual_as_interface_re_enchanting_digital_interaction.md]</code></p>
</div>

---

# Button Component

> **Purpose:**
> The Button component is a core interactive element for triggering actions, submitting forms, and guiding user flow through actions. It is strictly for actions (never navigation), always rendered as a native `<button>`, and is visually and semantically distinct from the navigation-only `LinkButton` (which renders as `<a>`). Button is the ritual "Act of Commitment" or "Threshold Crossing" in ThinkAlike. See also: [../noetica/corpus_magnus/art_aesthetics_and_culture/ritual_as_interface_re_enchanting_digital_interaction.md].

**Symbolic Role:**
- The Button is the ritual "Act of Commitment"—a symbolic threshold crossing. Its color, iconography, and feedback reinforce the mythic and ritual language of ThinkAlike (see [../narrative_engine/canon/symbolic_myth_index.md]).
- The use of **Error Red (#FF4136)** for all danger/destructive visuals is a ritual standard, never to be substituted.

**Last Updated:** June 9, 2025
**Version:** 1.1.1 (Harmonized for Alchemical Interface Initiative, symbolic/ritual framing, and PET/Clarity)
**Related Components:** `Form`, `TextInput`, `SelectDropdown`, `Checkbox`, `RadioGroup`
**Core Principles Embodied:** Clarity, Accessibility, PET/Clarity, Symbolic Resonance, Ritual Presence

## Visual Resonance & States
- **Style:** Minimalist, dark theme, high-contrast, glowing accents for focus/hover/active.
- **Shape:** Rounded corners (radius: 6px).
- **Color Variants:**
  - `primary`: Orange background (#FF9900), white text, orange glow/focus ring.
  - `secondary`: Blue background (#00BFFF), white text, blue glow/focus ring.
  - `danger`: **Strictly Error Red (#FF4136)** for background, border, glow, and focus ring. All visual aspects of the danger state (background, border, highlights, focus ring) use Error Red.
  - `ghost`: Transparent background, orange/blue border/text, glow on focus.
- **Typography:** Montserrat for label.
- **Focus Ring:** 2px glowing (orange, blue, or Error Red matching variant), always visible on keyboard focus.
- **Iconography:** Supports left/right icons (ThinkAlike glyphs preferred).
- **Loading State:** When `isLoading` is true, the button is disabled and the label/icon is replaced with a `LoadingSpinner` (variant="small", aria-label matches button label).

## Functional Core & Interaction Dynamics (Props)
| Name         | Type                | Required | Description                                                                 |
|--------------|---------------------|----------|-----------------------------------------------------------------------------|
| `children`   | `ReactNode`         | Yes*     | Button label or content. Required unless using `aria-label` for icon-only.  |
| `onClick`    | `() => void`        | No       | Click handler.                                                              |
| `variant`    | `primary` `secondary` `danger` `ghost` | No | Visual style. Defaults to `primary`.                        |
| `disabled`   | `boolean`           | No       | Disables the button.                                                        |
| `isLoading`  | `boolean`           | No       | Shows loading spinner, disables button, replaces label/icon.                |
| `leftIcon`   | `ReactNode`         | No       | Icon or glyph to display on the left.                                       |
| `rightIcon`  | `ReactNode`         | No       | Icon or glyph to display on the right.                                      |
| `aria-label` | `string`            | No       | Accessible label for icon-only buttons.                                     |
| `type`       | `button` `submit` `reset` | No  | Button type. Defaults to `button`.                                          |

**Type Definition:**
```typescript
interface ButtonProps {
  children?: React.ReactNode; // Required unless aria-label for icon-only
  onClick?: () => void;
  variant?: 'primary' | 'secondary' | 'danger' | 'ghost';
  disabled?: boolean;
  isLoading?: boolean;
  leftIcon?: React.ReactNode;
  rightIcon?: React.ReactNode;
  'aria-label'?: string;
  type?: 'button' | 'submit' | 'reset';
}
```

## Usage Protocols & Accessibility
- **Actions Only:** Never use for navigation—use `LinkButton` for navigation, `Button` for actions.
- **Labeling:** Always provide a visible label or `aria-label` for icon-only buttons.
- **Native Button:** Always use native `<button>` for best accessibility. If not, use `role="button"` and `tabIndex=0`.
- **Focus Ring:** 2px glowing (orange, blue, or Error Red) matching variant, always visible on keyboard focus.
- **Color Contrast:** All states (default, hover, focus, disabled) meet or exceed WCAG AAA contrast.
- **ARIA Attributes:**
  - `aria-label` for icon-only.
  - `aria-pressed` for toggle buttons.
  - `aria-busy` when `isLoading` is true.
- **Loading State:**
  - When `isLoading`, button is disabled, `aria-busy="true"`, and a `LoadingSpinner` (small, aria-label matches button) replaces label/icon.
- **Keyboard Accessible:** Tab, Enter, Space.

## PET/Clarity & Symbolic Protocols
- **Cognitive Liberty:** Labels must be clear, honest, and accurately represent the action. No manipulative or ambiguous text.
- **Transparency:** Visual feedback for all states (hover, focus, disabled, loading).
- **Ethics:** Destructive actions (danger variant) must be clearly labeled and use Error Red. Confirmation for destructive actions is recommended (handled outside the button).
- **Symbolic:** The act of clicking a button, especially primary or danger, is a ritual "Act of Commitment" or "Crossing a Threshold." Icons and color reinforce symbolic meaning (orange for creation/progression, Error Red for irreversible/warning actions).

## Examples
```jsx
// Primary button
<Button variant="primary" onClick={handleAction}>Save</Button>

// Secondary button
<Button variant="secondary" onClick={handleSecondary}>Cancel</Button>

// Danger button (Error Red)
<Button variant="danger" onClick={deleteItem} leftIcon={<TrashIcon />}>Delete</Button>

// Ghost button (icon-only)
<Button variant="ghost" aria-label="More options" leftIcon={<DotsIcon />} />

// Disabled button
<Button variant="primary" disabled>Disabled</Button>

// Loading state
<Button variant="primary" isLoading>Saving...</Button>
<Button variant="danger" isLoading leftIcon={<TrashIcon />}>Deleting</Button>
```

## Migration Notes
- Replace legacy action buttons with Button for PET/Clarity and symbolic alignment.
- Never use Button for navigation—use LinkButton instead.
- Ensure all destructive actions use the danger variant and Error Red.
- Harmonize all button visuals and states with the canonical style guide.

## Changelog
2025-06-09 :: v1.1.1 :: COMPREHENSIVE HARMONIZATION – Aligned with Alchemical Interface Initiative, PET/Clarity, symbolic/ritual standards, Error Red error states, and WCAG AAA accessibility targets. Ensured full support for restored Portal & Resonance Network flows.
2025-06-09 :: v1.1.0 :: Deepened distinction from LinkButton, mandated Error Red for all danger visuals, added isLoading prop and guidance, expanded accessibility and PET/Clarity, reinforced symbolic/ritual framing, and added clear examples for all variants and states.
2025-06-07 :: v1.0.1 :: Updated all error/danger state visuals and documentation to use Error Red (#FF4136) in accordance with the canonical visual style guide.
2025-06-07 :: v1.0.0 :: FINALIZED – Dual-metadata, template, PET/Clarity, symbolic, accessibility alignment.

<div align="center">
  <img src="../assets/thinkalike_logo.svg" alt="ThinkAlike Logo Placeholder" width="40" height="40" />
  <br/>
  <em>ThinkAlike — Harmonizing Human & Machine</em>
</div>
