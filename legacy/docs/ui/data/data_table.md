---
title: Data Table Component
type: Canonical UI Component
document_status: Harmonized
version: 1.1.0
last_updated: 2025-06-09
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
location: /docs/ui_components/data_table.md
alignment_tags:
- clarity_protocol
- pet_compliant
- accessibility_AAA
- core_interaction
- symbolic_interface
- value_display
related_components:
- DataTraceability
- ValidationWorkflow
- Alert
- LoadingSpinner
visual_style_guide_ref:
- ../style/visual_style_guide.md
tags:
- data
---


<!-- ∴ THINKALIKE COMPONENT MANIFEST ∴ -->
<!-- UID: /docs/ui_components/data_table.md -->

<br/>

<p align="center">
  <img src="/docs/assets/thinkalike_logo.svg" alt="ThinkAlike Logo" width="80"/>
</p>

<h1 align="center" style="font-family: 'Montserrat', Arial, sans-serif; font-weight: 700; color: #FF8C00; letter-spacing: 0.05em; border-bottom: 1px solid #666666; padding-bottom: 0.2em;">
  Data Table
</h1>

<p align="center" style="font-family: 'Open Sans', Arial, sans-serif; font-size: 1.1em; color: #CCCCCC; margin-bottom: 2em;">
  A core interactive element for structured data display, validation, and ethical transparency.<br/>
  <em>ThinkAlike: Connecting like minded individuals.</em>
</p>

---
<!-- METADATA LAYER -->
<div style="font-family: 'Courier New', monospace; font-size: 0.9em; color: #666666; margin-bottom: 2em; padding: 1em; border: 1px dashed #333333; background-color: #1a1a1a;">
  <p><strong>STATUS</strong> ::: Harmonized</p>
  <p><strong>VERSION</strong> ::: 1.1.0</p>
  <p><strong>LAST PULSE</strong> ::: 2025-06-09</p>
  <p><strong>STEWARD(S)</strong> ::: UI Systems Guild | Eos Lumina∴</p>
  <p><strong>ALIGNMENT SIGNALS</strong> ::: <code>[clarity_protocol]</code> <code>[pet_compliant]</code> <code>[accessibility_AAA]</code> <code>[core_interaction]</code> <code>[symbolic_interface]</code> <code>[value_display]</code></p>
  <p><strong>RESONATES WITH</strong> ::: <code>[../style/canonical_visual_style_guide.md]</code> <code>[DataTraceability]</code></p>
</div>

---

# Data Table

> **Purpose:**
> The Data Table component is a foundational ThinkAlike UI element for structured, ethical, and transparent data display. It embodies the "UI as Validation Framework" principle, integrating robust validation, PET/Clarity, and symbolic/ritual protocols. It empowers users with agency, radical transparency, and cognitive liberty, while serving as a bridge to DataTraceability and validation workflows.

## Visual & Symbolic Guidelines
- **Style:** Minimalist, node-graph inspired grid with glowing accent lines and dark mode as default. Table edges and interactive elements use luminous amber/orange glows for focus/active states. Error/validation states use **Error Red (#FF4136)** for all error visuals (borders, highlights, overlays).
- **Typography:** Montserrat (headers), Open Sans (body).
- **States:**
  - Default: Clean, high-contrast, node-graph grid.
  - Hover/Focus: Glowing accent on row/column, subtle node highlight.
  - Active/Engaged: Luminous border, sort/filter icons glow.
  - Disabled/Latent: Dimmed, reduced glow.
  - Error/Dissonance: **Error Red (#FF4136)** border, Alert overlays.
  - Loading/Processing: LoadingSpinner overlays with semi-transparent dark layer.
  - Validation: Data type glyphs, error/warning highlights use Error Red, tooltips with PET/Clarity-compliant feedback.

## Functional Core & Interaction Dynamics (Props)
| Name         | Type                | Required | Description                                                                 |
|--------------|---------------------|----------|-----------------------------------------------------------------------------|
| `data`       | `Array<Object>`     | Yes      | Data to display (rows).                                                     |
| `columns`    | `Array<ColumnDefinition>` | Yes | Column definitions (see below).                                             |
| `options`    | `object`            | No       | Table options: sorting, filtering, pagination, etc.                         |
| `onRowClick` | `(row: object) => void` | No   | Row click handler.                                                          |

**ColumnDefinition:**
```typescript
interface ColumnDefinition {
  key: string;
  title: string;
  dataType: 'string' | 'number' | 'boolean' | 'date' | 'imageUrl' | 'symbolic_glyph';
  validator?: (value: any, rowData: any) => boolean | string; // true or error message
  formatter?: (value: any, rowData: any) => React.ReactNode;
  sortable?: boolean;
  filterable?: boolean;
  ethicalMetadataKey?: string;
}
```

## Usage Protocols & Accessibility
- **Contextual Deployment:** Use for structured, auditable, and ethically transparent data display (profiles, logs, AI outputs, etc.). Integrate with DataTraceability for node-graph lineage and validation workflow.
- **ARIA Roles:** grid, row, columnheader, gridcell. Keyboard navigation: Tab, Arrow keys, Enter/Space for actions; focus rings use glowing accent. Screen reader: aria-label/aria-describedby for all indicators/messages.
- **Contrast & Motion:** High contrast, motion sensitivity (prefers-reduced-motion), and descriptive titles for all columns. All validation and symbolic cues must be perceivable by assistive tech.
- **Error/Validation:** All error/validation states use Error Red (#FF4136) for borders, highlights, and overlays. Use Alert for error summaries.

## PET/Clarity & Symbolic Protocols
- **Cognitive Liberty:** No manipulative formatting; user can reveal/hide original data (tooltip/expand).
- **Radical Transparency:** Node-graph lineage via DataTraceability links; ethicalMetadataKey for source/consent. All validation errors are explicit, constructive, and PET/Clarity-aligned.
- **Consent Weaving:** Data shown only with prior consent; visual cue/link for granular consent if available.
- **Data Minimization:** Only essential columns/data shown by default; configuration required for more.
- **Clarity Protocol:** Unambiguous headers, consistent formats, plain language feedback.
- **Symbolic:** Data type and validation status use glyphs from symbol_mappings_index.md. Node-graph and glowing accents evoke ThinkAlike's ritual of revelation. Sorting/filtering as acts of inquiry; validation as ritual transparency.

## Examples
```jsx
<DataTable
  data={rows}
  columns={[
    { key: 'name', title: 'Name', dataType: 'string', sortable: true },
    { key: 'score', title: 'Score', dataType: 'number', validator: (v) => v >= 0 || 'Score must be positive' },
    { key: 'joined', title: 'Joined', dataType: 'date', formatter: (v) => formatDate(v) },
    { key: 'consent', title: 'Consent', dataType: 'boolean', ethicalMetadataKey: 'consentGiven' }
  ]}
  options={{ enableSorting: true, enableFiltering: true, enablePagination: true, rowsPerPage: 10 }}
  onRowClick={handleRowClick}
/>
```

## Migration Notes
- Refactor legacy tables to use DataTable for PET/Clarity, symbolic, and accessibility alignment.
- Integrate DataTraceability for lineage/consent overlays.
- Ensure all error/validation visuals use Error Red (#FF4136).

## Changelog
2025-06-09 :: v1.1.0 :: Deepened PET/Clarity, symbolic, and accessibility guidance. Clarified error/validation states, reinforced DataTraceability, and updated changelog.
2025-06-07 :: v1.0.2 :: Standardized error state visuals (e.g., validation feedback) to use Error Red (#FF4136).
2025-06-07 :: v1.0.1 :: Refined for PET/Clarity, symbolic, and visual alignment (dark mode, glowing accents, node-graph, DataTraceability integration, accessibility AAA).
2025-06-07 :: v1.0.0 :: Initial harmonized definition based on legacy synthesis and canonical style guide.

---

*This document is tracked in project_status.md and legacy_component_matrix.md. For updates, see the migration matrix.*
