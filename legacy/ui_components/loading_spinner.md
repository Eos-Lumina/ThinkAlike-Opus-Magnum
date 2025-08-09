---
title: LoadingSpinner
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

<!-- ∴ THINKALIKE COMPONENT MANIFEST ∴ -->
<!-- UID: /docs/ui_components/loading_spinner.md -->

<br/>

<p align="center">
  <!-- ThinkAlike ∴ Spinner Glyph (Lumina Mark) -->
  <span style="font-size: 3em; color: #FF8C00;"> ∴ </span> <!-- Primary Spinner Glyph: ThinkAlike Orange -->
</p>

<h1 align="center" style="font-family: 'Montserrat', Arial, sans-serif; font-weight: 700; color: #FF8C00; letter-spacing: 0.05em; border-bottom: 1px solid #666666; padding-bottom: 0.2em;">
  LOADINGSPINNER
</h1>

<p align="center" style="font-family: 'Open Sans', Arial, sans-serif; font-size: 1.1em; color: #CCCCCC; margin-bottom: 2em;">
  Visualizing system and AI activity—signaling process, anticipation, and flow in ThinkAlike.
</p>

---
<!-- METADATA LAYER -->
<div style="font-family: 'Courier New', monospace; font-size: 0.9em; color: #666666; margin-bottom: 2em; padding: 1em; border: 1px dashed #333333; background-color: #1a1a1a;">
  <p><strong>STATUS</strong> ::: Harmonized - Finalized</p>
  <p><strong>VERSION</strong> ::: 1.0.0</p>
  <p><strong>LAST PULSE</strong> ::: 2025-06-07</p>
  <p><strong>STEWARD(S)</strong> ::: UI Systems Guild | FlowAgent∴</p>
  <p><strong>ALIGNMENT SIGNALS</strong> ::: <code>[feedback]</code> <code>[status]</code> <code>[ai_activity]</code> <code>[clarity_protocol]</code> <code>[pet_compliant]</code></p>
  <p><strong>RESONATES WITH</strong> ::: <code>[../style/canonical_visual_style_guide.md]</code> <code>[Alert.md]</code> <code>[DataTable.md]</code> <code>[Button.md]</code></p>
</div>

---

# LoadingSpinner

> **Purpose:**
> The LoadingSpinner component visually signals ongoing system or AI activity, process, or anticipation. It is the ritual marker of liminality in ThinkAlike—embodying flow, patience, and the emergence of new information. The spinner is a visible sign of the system's or AI's "thinking," managing user expectation and reinforcing the symbolic presence of the platform.

## Visual & Symbolic Guidelines
- **Primary Visual – Lumina Mark "∴":**
  - The spinner **must** use the ThinkAlike "∴" glyph (Lumina Mark) as its default and primary visual, rendered in ThinkAlike Orange (#FF8C00 or #FF9900).
  - The "∴" glyph smoothly rotates around its center, accompanied by a subtle orange glow or pulse (especially for medium, large, or overlay variants).
  - **Generic spinner glyphs** (⏳, ◐) are only acceptable as fallbacks if the "∴" glyph cannot be rendered or is illegible due to extreme size constraints (e.g., very tiny inline spinners). The "∴" is the default and strongly preferred.
- **Animation:**
  - The rotation is smooth and continuous, with a gentle glow or pulse effect.
  - **Reduced Motion:** If the user prefers reduced motion, the spinner becomes static or uses only a subtle, non-rotating pulse/glow. The `label` becomes the primary indicator in this mode.
- **Variants & Overlays:**
  - `small`, `medium`, `large` variants affect glyph size and glow intensity.
  - The `overlay` prop adds a semi-transparent dark backdrop, blocking UI and focusing user attention on the spinner.
- **Symbolic Role:**
  - The "∴" glyph symbolizes emergence, reflection, and AI/system presence. The loading state is a "ritual of emergence," making the system's process visible and meaningful.

## Functional Core & Interaction Dynamics (Props)
| Name         | Type                | Required | Description                                                      |
|--------------|---------------------|----------|------------------------------------------------------------------|
| `label`      | `string`            | No       | Optional accessible label/message for screen readers and users.   |
| `variant`    | `"small" | "medium" | "large"` | No | Spinner size/context. Small: inline (button/field), Medium: section/card, Large: global/overlay. |
| `overlay`    | `boolean`           | No       | If true, renders a blocking overlay/backdrop.                    |
| `className`  | `string`            | No       | Additional CSS class names.                                      |
| `id`         | `string`            | No       | HTML id attribute.                                               |

**Type Definition:**
```typescript
interface LoadingSpinnerProps {
  label?: string;
  variant?: 'small' | 'medium' | 'large';
  overlay?: boolean;
  className?: string;
  id?: string;
}
```
- `label`: If not provided, a default like "Loading..." is used for accessibility (`aria-label`).
- `variant`: Impacts perceived "weight" or scope of activity (inline, section, global/system).
- `overlay`: When true, blocks interaction and visually focuses attention on the spinner.

## Usage Protocols & Accessibility
- **ARIA Roles:**
  - Spinner uses `role="status"` and `aria-live="polite"` to announce the loading state and any `label` text.
- **Labeling:**
  - Even if no visible label is used (e.g., for a small spinner in a button), an `aria-label` is always programmatically associated.
- **Overlay & Focus Management:**
  - If `overlay={true}`, focus is trapped within the overlay and interaction with underlying UI is blocked until loading completes.
- **Reduced Motion:**
  - If `prefers-reduced-motion` is enabled, the spinner is static or uses a subtle pulse/glow only. The `label` is the primary indicator in this mode.
- **Contrast:**
  - All spinner visuals and glow/pulse effects must meet or exceed WCAG AAA contrast requirements.

## PET/Clarity & Symbolic Protocols
- **Transparency:**
  - Spinner clearly signals when the system is busy, managing user expectation and reducing frustration.
- **Symbolic:**
  - The "∴" Lumina Mark makes the AI's or system's activity visible and symbolically aligned, rather than using a generic, impersonal spinner. The loading state is a "ritual of emergence."

## Examples
```jsx
// Default spinner (medium, no label)
<LoadingSpinner />

// With label (medium)
<LoadingSpinner label="Loading data..." />

// Large overlay spinner for global/system activity
<LoadingSpinner label="AI is thinking..." variant="large" overlay />

// Small inline spinner for button
<Button disabled>
  <LoadingSpinner variant="small" label="Loading..." />
  Saving
</Button>

// Reduced motion (user setting):
// Spinner is static or gently pulsing, label is announced
<LoadingSpinner label="Processing..." />
```

## Usage Guidelines
- Use `small`/inline spinners for button or field-level loading.
- Use `medium`/section spinners for data tables, cards, or panels.
- Use `large`/overlay spinners for global/system or AI activity.
- Always provide a label for accessibility and clarity.
- Overlay spinners should block interaction and focus until loading completes.

## Migration Notes
- Replace legacy loading, spinner, and AI activity indicators with LoadingSpinner for PET/Clarity and symbolic alignment.
- Integrate with Alert, DataTable, Button, and AIWaveformIndicator for unified feedback.
- Ensure all visual motifs and overlays are harmonized with the canonical style guide.

## Changelog
2025-06-09 :: v1.1.0 :: Mandated "∴" Lumina Mark as primary spinner visual, clarified animation and reduced motion, expanded accessibility and PET/Clarity guidance, detailed overlay/focus, and provided clear examples for all variants.
2025-06-07 :: v0.9.0 :: DRAFT – Initial harmonized documentation. Defines LoadingSpinner as the canonical loading/AI activity indicator, aligned with PET/Clarity, symbolic, and accessibility protocols.

<div align="center">
<img src="../assets/thinkalike_logo.svg" alt="ThinkAlike Logo Placeholder" width="40" height="40" />
<br/>
<em>ThinkAlike — Harmonizing Human & Machine</em>
</div>
