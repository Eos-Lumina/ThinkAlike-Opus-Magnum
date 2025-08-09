---
title: Component: Sidebar
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

<!-- ∴ THINKALIKE COMPONENT MANIFEST ∴ -->
<!-- UID: /docs/ui_components/sidebar.md -->

<br/>

<p align="center">
  <!-- Placeholder for a prominent Component Glyph or ThinkAlike Sigil -->
  <span style="font-size: 3em; color: #00BFFF;"> │⋮│ </span> <!-- Example Sidebar/Vertical Menu Glyph -->
</p>

<h1 align="center" style="font-family: 'Montserrat', Arial, sans-serif; font-weight: 700; color: #00BFFF; letter-spacing: 0.05em; border-bottom: 1px solid #666666; padding-bottom: 0.2em;">
  SIDEBAR
</h1>

<p align="center" style="font-family: 'Open Sans', Arial, sans-serif; font-size: 1.1em; color: #CCCCCC; margin-bottom: 2em;">
  A contextual navigation and action panel, anchoring realm-specific journeys.
</p>

---
<!-- METADATA LAYER -->
<div style="font-family: 'Courier New', monospace; font-size: 0.9em; color: #666666; margin-bottom: 2em; padding: 1em; border: 1px dashed #333333; background-color: #1a1a1a;">
  <p><strong>STATUS</strong> ::: Harmonized – Finalized</p>
  <p><strong>VERSION</strong> ::: 1.1.1</p>
  <p><strong>LAST PULSE</strong> ::: 2025-06-09</p>
  <p><strong>STEWARD(S)</strong> ::: UI Systems Guild | ClarityAgent∴</p>
  <p><strong>ALIGNMENT SIGNALS</strong> ::: <code>[navigation]</code> <code>[layout]</code> <code>[contextual_menu]</code> <code>[accessibility_landmark]</code> <code>[clarity_protocol]</code> <code>[pet_compliant]</code> <code>[threshold_guardian]</code> <code>[symbolic_resonance]</code> <code>[error_red]</code></p>
  <p><strong>RESONATES WITH</strong> ::: <code>[../style/canonical_visual_style_guide.md]</code> <code>[AppLayout.md]</code> <code>[NavigationBar.md]</code> <code>[LinkButton.md]</code> <code>[../narrative_engine/canon/symbolic_myth_index.md]</code> <code>[../noetica/corpus_magnus/art_aesthetics_and_culture/ritual_as_interface_re_enchanting_digital_interaction.md]</code></p>
</div>

---

# Component: Sidebar

**Purpose:** Serves as the persistent, contextual navigation and action interface, acting as the "Threshold Guardian" and "Pathfinder"—a ritual guide for traversing the deeper domains of ThinkAlike. The Sidebar is not merely a utility, but a symbolic and functional threshold, marking the user's readiness to cross into focused realms and micro-journeys. It embodies the "Ritual over Interface" philosophy, supporting PET/Clarity, and is a daily invocation of the project's values and mythos. See also: [ritual_as_interface_re_enchanting_digital_interaction.md].

**Symbolic Role:**
- The Sidebar is the "Threshold Guardian"—it marks the entry into more specific sub-realms, functionalities, or detailed views. Interacting with the Sidebar is a ritual act, a conscious step into a more focused context, and a symbolic crossing of a threshold.
- As "Pathfinder," the Sidebar guides micro-journeys, illuminating available paths and tools for the current task or exploration. Its glyphs and structure echo the mythic and symbolic language of ThinkAlike (see [symbolic_myth_index.md]).
- The Sidebar may subtly shift its visual aura (e.g., background shimmer, glyph accent, or border) when the user transitions between sub-realms, signifying a crossing of thresholds and reinforcing the sense of journey and transformation.

**Last Updated:** June 9, 2025
**Version:** 1.1.1 (Harmonized for Alchemical Interface Initiative, symbolic/ritual framing, and PET/Clarity)
**Related Components:** `AppLayout`, `NavigationBar`, `PageContainer`, `LinkButton`
**Core Principles Embodied:** Clarity, Accessibility, Contextual Guidance, Symbolic Resonance, Modularity, Ritual Presence

---

## 1. Overview & Purpose

The `Sidebar` component serves as a crucial element for secondary or contextual navigation and actions within the ThinkAlike interface. Typically displayed as a vertical panel, it complements the global `NavigationBar` by offering more granular options, tools, and pathways specific to the user's current realm, task, or focus area.

Its primary functions are to:
*   **Provide Contextual Navigation:** Offer links and controls relevant to the current view or selected item, allowing for deeper exploration within a specific domain.
*   **Surface Realm-Specific Actions:** House buttons and tools that perform actions pertinent to the current context.
*   **Organize Sub-Sections:** Structure and provide access to sub-sections or related content within a larger realm.
*   **Enhance User Workflow:** Streamline tasks by keeping relevant options readily accessible without cluttering the main content area or global navigation.

Within the `AppLayout`'s "ritual shell," the `Sidebar` acts as a focused guide, helping users navigate the intricacies of specific domains and perform relevant actions with clarity and purpose.

---

## 2. Visual & Symbolic Guidelines

### Style
The `Sidebar` maintains a minimalist, mythopoetic aesthetic, distinct yet harmonious with the main content and the global `NavigationBar`.

*   **Form:** A vertical bar or panel, typically positioned to the left or right of the main content area.
*   **Separation:** Clear visual distinction from the `PageContainer` content, using a subtle border, a different background shade, or slight elevation.
*   **Color Palette (Canonical):**
    *   **Background:** `#181A1B` (Surface - a dark, muted tone that recedes slightly).
    *   **Icons/Text (Default):** `#CCCCCC` (for good readability on the dark background).
    *   **Icons/Text (Focus/Hover):** `#00BFFF` (ThinkAlike's vibrant blue for interactive states).
    *   **Icons/Text (Active):** `#FF9900` (ThinkAlike Orange for clear indication of the current active item).
    *   **Error State:** **Error Red (#FF4136)** for all error, danger, or critical validation states (borders, icons, text, glows, backgrounds). No other color is permitted for error states.
    *   **Dividers:** `#222222` (subtle lines for sectioning).
*   **Typography:** Legible and consistent with the global style guide. Labels are concise and ritualistically clear.

### Focus Indicators
- All focusable elements must display a visible focus indicator: a 3px solid outline in ThinkAlike Orange (`#FF9900`), Blue (for info), or **Error Red (#FF4136)** for error/critical states, matching the variant.

### Transitions & Animations
- All transitions (e.g., hover, active, expansion/collapse, realm shift) must be smooth, meaningful, and contribute to the ritual feel (e.g., gentle pulse, luminous glow, graceful fade). Always respect `prefers-reduced-motion` for accessibility.

### Symbolic Role: "Threshold Guardian" & "Pathfinder"
The `Sidebar` embodies the symbolic roles of a **"Threshold Guardian"** and a **"Pathfinder"**:

*   **Threshold Guardian:** It marks the entry into more specific sub-sections, functionalities, or detailed views within a realm. Interacting with the `Sidebar` signifies a deliberate step into a more focused context. It "guards" these deeper paths, revealing them when the user indicates readiness to explore further.
*   **Pathfinder:** Once within a context, the `Sidebar` guides micro-journeys. Its links and actions illuminate the available paths and tools for the current task or exploration.
*   **Contextual Scent:** The `Sidebar`'s content, particularly the icons/glyphs used, can subtly change or become more prominent to reflect the "scent" or symbolic nature of the current context. For example, if a user is in an "Agent Creation" realm, the sidebar icons might subtly emphasize creation, configuration, or connection glyphs. This reinforces the user's sense of place and purpose.
*   **Ritual Triggers:** The `Sidebar` can house "Ritual Triggers" – specific links or action buttons that initiate symbolic processes, workflows, or transitions relevant to the current view (e.g., "Begin Contemplation Session," "Activate Resonance Protocol").

### Responsiveness
*   **Small Screens:** On smaller viewports (e.g., mobile), the `Sidebar` is typically hidden by default to maximize content visibility.
*   **Toggle Mechanism:** A clearly identifiable and accessible toggle button (often a "hamburger" icon or similar, placed in the `NavigationBar` or a fixed position) should be used to reveal/hide the `Sidebar` as an overlay or by pushing content.
*   The `aria-controls` attribute on the toggle can link to the `Sidebar`'s `id`, and `aria-expanded` should reflect its state.

---

## 3. Functional Core & Interaction Dynamics (Props)

| Prop             | Type                                                                 | Default        | Description                                                                                                                                                           |
|------------------|----------------------------------------------------------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `items`          | `Array<SidebarItem>`                                                 | `[]`           | An array of objects defining the content and structure of the sidebar.                                                                                                |
| `collapsed`      | `boolean`                                                            | `false`        | Controls the collapsed (icon-only) or expanded (icon+label) state of the sidebar.                                                                                     |
| `onItemClick`    | `(event: React.MouseEvent, item: SidebarItem) => void`               | `undefined`    | Optional callback function triggered when a clickable sidebar item (link or action) is clicked.                                                                       |
| `onToggleCollapse`| `() => void`                                                         | `undefined`    | Optional callback to handle the expansion/collapse toggle, allowing parent control if needed.                                                                         |
| `width`          | `string` or `number`                                                 | `'240px'`      | The width of the sidebar when expanded.                                                                                                                               |
| `collapsedWidth` | `string` or `number`                                                 | `'60px'`       | The width of the sidebar when collapsed (icon-only).                                                                                                                  |
| `ariaLabel`      | `string`                                                             | `"Contextual navigation"` | **Mandatory.** The ARIA label for the underlying semantic element (`<nav>` or `<aside>`), providing context for assistive technologies.                                 |
| `as`             | `'nav'` or `'aside'`                                                | `'nav'`        | The HTML semantic element to render the sidebar as. Use `'nav'` if it's the primary navigation for a section, `'aside'` if supplementary.                               |
| `className`      | `string`                                                             | `''`           | Allows for additional CSS classes to be applied for custom styling.                                                                                                   |
| `id`             | `string`                                                             | `undefined`    | Assigns an HTML `id` attribute to the sidebar, useful for `aria-controls`.                                                                                             |

### `SidebarItem` Type Definition:

```typescript
type SidebarItem = {
  id: string; // Unique identifier for the item (e.g., for keys, testing)
  label: string; // Accessible text label for the item
  icon?: React.ReactNode; // Optional icon (e.g., SVG component). Ensure accessibility.
  href?: string; // URL for navigation links
  onClick?: (event: React.MouseEvent) => void; // Action for buttons or non-navigational items
  active?: boolean; // For programmatic highlighting; aria-current is preferred for active links
  disabled?: boolean; // If the item is disabled
  type?: 'link' | 'action' | 'divider' | 'heading'; // Defines the rendering and behavior
  children?: SidebarItem[]; // For nested/collapsible sections
  defaultOpen?: boolean; // If a children section should be open by default
  target?: string; // For links, e.g., '_blank'
  ariaLabel?: string; // Specific aria-label if label prop isn't sufficient or for icon-only items
};
```

**Notes on `SidebarItem`:**
*   **`children`:** This allows for nested sections within the sidebar. The UX for expanding/collapsing these nested sections needs to be clear and accessible (e.g., using disclosure patterns with `aria-expanded`).
*   **`type`:**
    *   `'link'`: Renders as a navigation link (`<a>`).
    *   `'action'`: Renders as a button (`<button>`).
    *   `'divider'`: Renders a visual separator.
    *   `'heading'`: Renders a non-interactive heading for a section.
*   **Accessibility of Icons:** If an icon is used, `label` still provides the primary accessible name. If `label` is not visually displayed (e.g., in collapsed mode), the `icon` itself should have an `aria-label` or be accompanied by `aria-labelledby` pointing to a hidden label, or the `SidebarItem` itself can have an `ariaLabel` prop.

---

## 4. Usage Protocols & Accessibility

The `Sidebar` must be highly accessible and PET/Clarity-aligned:

*   **Semantic HTML:**
    *   Render as a `<nav>` element (via `as="nav"`) if it provides primary navigation for a page section or a distinct region.
    *   Render as an `<aside>` element (via `as="aside"`) if it provides complementary content or actions that are related to the main content but not primary navigation.
    *   The `ariaLabel` prop is mandatory to describe its purpose.
*   **Keyboard Navigation & Focus:**
    *   All interactive items (links, buttons, expand/collapse toggles for parent sidebar and nested sections) must be focusable and operable via keyboard.
    *   Logical focus order (top-to-bottom).
    *   **Visible Focus Indicators:** A clear, high-contrast focus indicator (`3px solid` ThinkAlike Orange `#FF9900` outline) on the focused element.
*   **Active Link Indication (`aria-current`):**
    *   For `SidebarItem`s of `type: 'link'`, the currently active link must have `aria-current="page"` (or `aria-current="true"`/`"location"` as appropriate for the context).
*   **Collapsible Sections (`aria-expanded`):**
    *   If `SidebarItem`s have `children` (nested sections), the toggle controlling their visibility must use `aria-expanded` to indicate state (`true` for open, `false` for closed).
    *   The toggle should also use `aria-controls` to point to the `id` of the collapsible region.
*   **Expand/Collapse Toggle (Main Sidebar):**
    *   The main toggle for the sidebar's expanded/collapsed state must have an `aria-label` (e.g., "Collapse sidebar") and `aria-expanded` state.
*   **Color Contrast:**
    *   All text and meaningful icons must meet WCAG AAA color contrast ratios against their background for all states (default, hover, focus, active, error).
*   **Hidden Sidebar (Responsive):**
    *   When the sidebar is hidden off-screen on small viewports, ensure it's truly hidden from assistive technologies (e.g., using `display: none` or `visibility: hidden`) or managed correctly with `aria-hidden="true"` if it's merely visually off-screen but could still be focusable. The toggle button becomes the primary means of access.

---

## 5. PET/Clarity & Symbolic Protocols Alignment

*   **Transparency & Clarity (Clarity Protocol):**
    *   The purpose and action of each `SidebarItem` must be immediately clear from its label and/or icon.
    *   Active states are clearly indicated, helping users understand their current context or selection within the sidebar's scope.
    *   Logical grouping of items (via headings, dividers, or nesting) enhances scannability and understanding.
*   **Symbolic Resonance (Threshold Guardian & Pathfinder):**
    *   **Icons/Glyphs:** Thoughtful use of ThinkAlike glyphs reinforces the meaning and symbolic weight of each item, guiding users through contextual "thresholds." Reference: [symbolic_myth_index.md].
    *   **Ritual Transitions:** The `Sidebar` as a whole facilitates "ritual transitions" into specific functionalities or deeper levels of engagement within a realm. Its structure can mirror the steps of a contextual workflow.
    *   **Ritual Triggers:** Items within the sidebar can act as "Ritual Triggers" – clearly labeled buttons or links that initiate specific processes, analyses, or contemplative states relevant to the current view (e.g., "Initiate Agent Dialogue," "View Resonance Patterns," "Begin Ethical Audit"). These should be designed to feel like meaningful invocations rather than mere clicks.
*   **Ethical Alignment:**
    *   Navigation and actions are always non-deceptive, never manipulative. All actions are opt-in and clearly labeled. No dark patterns.
    *   The Sidebar does not collect or expose user data unless explicitly consented to by the user.
    *   All error, danger, or critical states must use **Error Red (#FF4136)** and be programmatically linked to error descriptions with `aria-describedby`.

---

## 6. Symbolic Resonance & Ritual Integration

- The Sidebar is the ritual threshold and pathfinder, grounding the user in the symbolic cosmos of ThinkAlike.
- Each navigation act is a ritual crossing, and the Sidebar's design, transitions, and glyphs (from symbolic_myth_index.md) reinforce this.
- The Sidebar may shift its aura (e.g., shimmer, glyph accent) to mark the crossing of sub-realm thresholds, echoing the rites described in portal_specification.md and resonance_network_specification.md.
- Ritual Triggers within the Sidebar are designed as meaningful invocations, not mere clicks.

---

## 7. Implementation Echoes (Examples)

### Example 1: Sidebar with Various Item Types

```typescript jsx
// filepath: components/layout/AppLayout.tsx (Conceptual Placement)
import Sidebar, { SidebarItem } from '''@/components/ui_components/Sidebar'''; // Assuming path
// Import necessary icons (e.g., from ThinkAlike glyph library)
// import { RealmIcon, SettingsIcon, ActionIcon, InfoIcon, DividerLine, SectionHeaderGlyph } from '''@/assets/icons''';

const sidebarItems: SidebarItem[] = [
  { type: 'heading', id: 'realm-details-header', label: 'Realm Details' /* icon: <SectionHeaderGlyph /> */ },
  { id: 'nav-overview', label: 'Overview', href: '/current-realm/overview', icon: {/* <InfoIcon /> */}, type: 'link' },
  { id: 'nav-settings', label: 'Settings', href: '/current-realm/settings', icon: {/* <SettingsIcon /> */}, type: 'link' },
  { type: 'divider', id: 'actions-divider' },
  { id: 'action-perform', label: 'Perform Action', onClick: () => console.log('Action!'), icon: {/* <ActionIcon /> */}, type: 'action' },
  {
    id: 'nav-advanced',
    label: 'Advanced Options',
    icon: {/* <RealmIcon /> */},
    type: 'link', // Could be a non-href item that just toggles children
    defaultOpen: true,
    children: [
      { id: 'nav-advanced-1', label: 'Sub Option 1', href: '/current-realm/advanced/1', type: 'link' },
      { id: 'nav-advanced-2', label: 'Sub Option 2', href: '/current-realm/advanced/2', type: 'link' },
    ],
  },
];

// In your AppLayout component's render method, potentially alongside PageContainer:
<Sidebar
  ariaLabel="Current Realm Navigation"
  as="aside" // Or "nav" depending on its role
  items={sidebarItems}
  collapsed={isSidebarCollapsed} // State managed by AppLayout or context
  onToggleCollapse={() => setIsSidebarCollapsed(!isSidebarCollapsed)}
/>
```

### Example 2: Collapsed Sidebar State

*(Visually, this would show only icons. The `Sidebar` component's internal logic would handle rendering based on the `collapsed` prop.)*

The `Sidebar` component, when `collapsed={true}`, would render `sidebarItems` showing only their `icon` (if provided) and ensure tooltips or other mechanisms provide the `label` on hover/focus for accessibility.

---

## 8. Changelog

*   **2025-06-09 :: v1.1.1 :: COMPREHENSIVE HARMONIZATION – Aligned with Alchemical Interface Initiative, PET/Clarity, symbolic/ritual standards, Error Red error states, and WCAG AAA accessibility targets. Ensured full support for restored Portal & Resonance Network flows.**
*   **2025-06-09 (v1.1):**
    *   Harmonized for Alchemical Interface Initiative and symbolic/ritual framing.
    *   Deepened language on Sidebar as "Threshold Guardian" and "Pathfinder."
    *   Clarified PET/Clarity, accessibility, and ethical navigation protocols.
    *   Updated implementation echoes and accessibility notes.
*   **2025-06-09 (v1.0):**
    *   Initial draft created.
    *   Established role as "Threshold Guardian" and "Pathfinder," complementing `NavigationBar`.
    *   Defined visual style (including canonical colors), structure, icon usage, and expansion/collapse behavior.
    *   Detailed `SidebarProps` and the `SidebarItem` type, including support for nesting (`children`).
    *   Outlined comprehensive accessibility requirements: semantic HTML (`<nav>`/`<aside>`), keyboard navigation, focus indicators, `aria-current`, `aria-expanded`.
    *   Addressed responsiveness for small screens.
    *   Aligned with PET/Clarity and Symbolic Protocols, introducing "Ritual Triggers."
    *   Provided initial implementation examples.

---

<div align="center">
<img src="../assets/thinkalike_logo.svg" alt="ThinkAlike Logo Placeholder" width="40" height="40" />
<br/>
<em>ThinkAlike — Harmonizing Human & Machine</em>
</div>
