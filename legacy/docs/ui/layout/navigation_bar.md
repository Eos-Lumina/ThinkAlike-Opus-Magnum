---
title: Component: NavigationBar
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
tags: []
---

<!-- ∴ THINKALIKE COMPONENT MANIFEST ∴ -->
<!-- UID: /docs/ui_components/navigation_bar.md -->

<br/>

<p align="center">
  <!-- Placeholder for a prominent Component Glyph or ThinkAlike Sigil -->
  <span style="font-size: 3em; color: #00BFFF;"> ≡ </span> <!-- Example NavigationBar Glyph -->
</p>

<h1 align="center" style="font-family: 'Montserrat', Arial, sans-serif; font-weight: 700; color: #00BFFF; letter-spacing: 0.05em; border-bottom: 1px solid #666666; padding-bottom: 0.2em;">
  NAVIGATION BAR
</h1>

<p align="center" style="font-family: 'Open Sans', Arial, sans-serif; font-size: 1.1em; color: #CCCCCC; margin-bottom: 2em;">
  The global compass for traversing realms, journeys, and features in ThinkAlike.
</p>

---
<!-- METADATA LAYER -->
<div style="font-family: 'Courier New', monospace; font-size: 0.9em; color: #666666; margin-bottom: 2em; padding: 1em; border: 1px dashed #333333; background-color: #1a1a1a;">
  <p><strong>STATUS</strong> ::: Harmonized – Finalized</p>
  <p><strong>VERSION</strong> ::: 1.1.1</p>
  <p><strong>LAST PULSE</strong> ::: 2025-06-09</p>
  <p><strong>MAINTAINED_BY</strong> ::: UI Systems Guild</p>
  <p><strong>STEWARD(S)</strong> ::: UI Systems Guild | ClarityAgent∴</p>
  <p><strong>ALIGNMENT SIGNALS</strong> ::: <code>[navigation]</code> <code>[layout]</code> <code>[accessibility_landmark]</code> <code>[clarity_protocol]</code> <code>[pet_compliant]</code> <code>[ritual_axis]</code> <code>[symbolic_resonance]</code> <code>[error_red]</code></p>
  <p><strong>RESONATES WITH</strong> ::: <code>[../style/canonical_visual_style_guide.md]</code> <code>[AppLayout.md]</code> <code>[Sidebar.md]</code> <code>[LinkButton.md]</code> <code>[symbolic_myth_index.md]</code> <code>[ritual_as_interface_re_enchanting_digital_interaction.md]</code></p>
</div>

---

# Component: NavigationBar

**Purpose:** Serves as the primary, persistent global navigation interface, acting as a "global compass" and **ritual axis** to orient users within the ThinkAlike cosmos. The NavigationBar is not merely a utility, but a symbolic and functional anchor—a threshold guardian and compass rose for traversing the mythic realms of ThinkAlike. It embodies the "Ritual over Interface" philosophy, supporting PET/Clarity, and is a daily invocation of the project's values and mythos. See also: [ritual_as_interface_re_enchanting_digital_interaction.md].

**Symbolic Role:**
- The NavigationBar is the "ritual axis mundi"—the stable axis around which the user's journey unfolds. Its persistent presence is a grounding force, a symbolic compass that orients the Initiate as they traverse the alchemical landscape of realms and features.
- The ThinkAlike logo or sigil is the "mundane mandala"—a focal point for the user's attention and a visual invocation of the project's mythos. Its presence at the heart of the NavigationBar is a ritual act of orientation and belonging.
- The NavigationBar may subtly shift its visual aura (e.g., background shimmer, glyph accent, or border) when the user transitions between major realms, signifying a crossing of thresholds without causing confusion or disorientation. This reinforces the sense of journey and transformation.

**Last Updated:** June 9, 2025
**Version:** 1.1 (Harmonized for Alchemical Interface Initiative, symbolic/ritual framing, and PET/Clarity)
**Related Components:** `AppLayout`, `Sidebar`, `PageContainer`
**Core Principles Embodied:** Clarity, Accessibility, Orientation, Symbolic Resonance, Navigability, Ritual Presence

---

## 1. Overview & Purpose

The `NavigationBar` is a cornerstone of the ThinkAlike user experience, providing the primary, persistent interface for global navigation. Its fundamental purpose is to empower users to:

*   **Traverse Realms:** Seamlessly move between the distinct conceptual realms and functional areas of ThinkAlike. Each navigation act is a conscious ritual crossing, not a mere click.
*   **Access Core Features:** Quickly reach essential tools, resources, and sections, with each link representing a symbolic gateway or portal.
*   **Maintain Orientation:** Consistently understand their current location within the broader ThinkAlike ecosystem, reinforcing a sense of place, context, and ritual presence.

As an integral part of the `AppLayout`'s "ritual shell," the `NavigationBar` is more than a utility; it's a constant guide, ensuring users feel anchored and confident as they explore the depth and breadth of the platform. Its design and presence are a daily invocation of the project's values and mythos.

---

## 2. Visual & Symbolic Guidelines

### Style
The `NavigationBar` adheres to a **minimalist and clear design language**, as outlined in `canonical_visual_style_guide.md`. It prioritizes unobtrusive guidance, ensuring content remains the focus.

*   **Form:** Typically a horizontal bar at the top of the viewport, though adaptable for vertical orientations if future designs require.
*   **Separation:** Clear visual separation from the main content area, often achieved through subtle borders, elevation, or background color differentiation.
*   **Color Palette:** Utilizes canonical ThinkAlike colors:
    *   **Background:** Often a dark background (e.g., a deep, desaturated blue or near-black) to establish a sense of foundational stability, especially in the preferred dark mode.
    *   **Accents:** ThinkAlike Orange (`#FF9900`) for calls-to-action, active states, and focus indicators.
    *   **Text/Icons:** High-contrast, legible colors (e.g., off-white or light gray on dark backgrounds).
*   **Light/Dark Mode:** Must provide visually distinct and accessible presentations in both light and dark modes, with dark mode often being the default or preferred aesthetic to enhance the "cosmos" feel.
*   **Subtle Realm Transitions:** When the user crosses into a new major realm (e.g., Portal, Resonance Network, Community Hive), the NavigationBar may animate or shift its aura (e.g., a faint glyph, color shimmer, or border accent) to signify the crossing of a symbolic threshold. This should be subtle, accessible, and never disorienting.

### Core Elements
The following elements are typically present:

1.  **Logo/Sigil (Mandatory):**
    *   An accessible SVG representation of the ThinkAlike logo or primary sigil.
    *   Serves as a constant brand anchor and "mundane mandala," visually and symbolically centering the user. Must have descriptive alt text for screen readers.
    *   Often links back to the primary landing page or dashboard.
2.  **Project Name (Mandatory, if space allows and distinct from Logo):**
    *   Clearly states "ThinkAlike," reinforcing identity. Can be integrated with the logo.
3.  **Primary Navigation Links (Mandatory):**
    *   The core set of links to major realms or top-level sections.
    *   Text labels should be concise and clear. Icons (using ThinkAlike glyphs) can supplement labels for quick recognition.
    *   Each link is a symbolic gateway—a conscious act of entering a new sphere of operation.
4.  **User/Account Menu (Recommended):**
    *   Provides access to user profile, settings, sign-out, etc.
5.  **Contextual Actions (Optional):**
    *   May include a global search input or icons for notifications, if applicable to the overall application structure.

### Active State Indication
It is crucial to clearly indicate the user's current location within the navigation structure.

*   **Visual Cue:** The active link should be visually distinct, typically using a high-contrast color (e.g., ThinkAlike Orange `#FF9900`), a prominent bottom border, a background highlight, or a distinct icon state.
*   **Accessibility:** Programmatically indicated using `aria-current="page"`.

### Error State Visuals
- All error, danger, or critical validation states (borders, icons, text, glows, backgrounds) must use **Error Red (#FF4136)**, as defined in the canonical visual style guide. No other color is permitted for error states.

### Focus Indicators
- All focusable elements must display a visible focus indicator: a 3px solid outline in ThinkAlike Orange (`#FF9900`), Blue (for info), or **Error Red (#FF4136)** for error/critical states, matching the variant.

### Transitions & Animations
- All transitions (e.g., hover, active, realm shift) must be smooth, meaningful, and contribute to the ritual feel (e.g., gentle pulse, luminous glow, graceful fade). Always respect `prefers-reduced-motion` for accessibility.

### Symbolic Role: The Compass and Ritual Axis
The `NavigationBar` is symbolically envisioned as the **"global compass"** or **"ritual axis"** of the ThinkAlike experience.

*   **Anchoring Presence:** Its persistent visibility and stable design anchor the user, providing a constant point of reference amidst the potentially vast informational landscape. It counters disorientation and fosters a sense of control.
*   **Gravity of the Cosmos:** The visual design can subtly hint at the "gravity" of the ThinkAlike project. This might be achieved through:
    *   **Subtle Background Textures:** A very faint, almost imperceptible texture on the bar's background could evoke a sense of depth or the fabric of the cosmos.
    *   **Transitions:** Smooth, understated transitions when navigation links are hovered or activated, or even subtle animations when moving between major realms, can provide a sense of graceful movement through the ecosystem.
*   **Interconnectedness of Realms:** The arrangement and grouping of navigation links should thoughtfully reflect the conceptual hierarchy and interconnectedness of ThinkAlike's realms. The bar itself becomes a map of the possible, guiding the user's journey through this symbolic universe.

---

## 3. Functional Core & Interaction Dynamics (Props)

| Prop            | Type                                                                                                | Default        | Description                                                                                                                                                              |
|-----------------|-----------------------------------------------------------------------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `links`         | `Array<{ label: string; href: string; icon?: ReactNode; id?: string; active?: boolean; target?: string; rel?: string; isExternal?: boolean }>` | `[]`           | An array of objects defining the primary navigation links. `id` for testing/keys, `active` for programmatic override (though `aria-current` is preferred for actual state). `target` for `_blank` etc. `isExternal` triggers an external link icon and `rel="noopener noreferrer"`. |
| `logo`          | `ReactNode`                                                                                         | `null`         | Custom ReactNode for the logo/sigil. Typically an SVG component. Must be accessible and have descriptive alt text.                                                        |
| `projectName`   | `string`                                                                                            | `''`           | The display name of the project, if separate from the logo.                                                                                                              |
| `userMenu`      | `ReactNode`                                                                                         | `null`         | Custom ReactNode for the user/account menu.                                                                                                                              |
| `onLinkClick`   | `(event: React.MouseEvent<HTMLAnchorElement>, link: LinkObject) => void`                             | `undefined`    | Optional callback function triggered when a navigation link is clicked. `LinkObject` refers to an item from the `links` array.                                           |
| `ariaLabel`     | `string`                                                                                            | `"Main navigation"` | **Mandatory.** The ARIA label for the underlying `<nav>` element, providing context for assistive technologies.                                                              |
| `className`     | `string`                                                                                            | `''`           | Allows for additional CSS classes to be applied for custom styling.                                                                                                      |
| `children`      | `ReactNode`                                                                                         | `null`         | Allows for additional custom elements to be placed within the navigation bar (e.g., search input, notification icons). Use with care to maintain clarity.             |

### Notes on Props:
*   **`links` prop:**
    *   `label`: Clear, concise text for the link.
    *   `href`: The URL path for the link.
    *   `icon`: Optional `ReactNode` (e.g., an SVG icon component from ThinkAlike's glyph library) to visually accompany the label.
    *   `id`: Useful for unique keys in rendering lists and for targeting elements in end-to-end tests.
    *   `active`: Can be used to programmatically suggest an active state, but the component should primarily rely on route matching or context to set `aria-current="page"` correctly.
    *   `isExternal`: If true, renders an external link icon and sets `rel="noopener noreferrer"`.
*   **`ariaLabel`:** This prop is critical for accessibility. Ensure it accurately describes the navigation bar's purpose (e.g., "Primary navigation," "Site navigation").
*   **`logo`:** Must be an accessible SVG or image with descriptive alt text, as it is a ritual and orientation anchor.

---

## 4. Usage Protocols & Accessibility

Accessibility is paramount for the `NavigationBar`. It must be usable by everyone, regardless of ability.

*   **Semantic HTML:**
    *   The component must render as a `<nav>` HTML5 element.
    *   The `ariaLabel` prop is used to provide a descriptive label for this `<nav>` element.
*   **"Skip to main content" Link:**
    *   A "Skip to main content" link should be the **very first focusable element** within the `NavigationBar` (or even preceding it in the DOM order if `AppLayout` handles it globally).
    *   This link is visually hidden by default but becomes visible on focus, allowing keyboard users to bypass the navigation and jump directly to the `PageContainer`'s content.
    *   The skip link is a ritual threshold, honoring accessibility as a sacred principle.
*   **Keyboard Navigation & Focus:**
    *   All navigation links and interactive elements (logo link, user menu button) must be focusable and operable via keyboard (Enter/Space keys).
    *   Logical focus order (left-to-right, top-to-bottom, or as visually presented).
    *   **Visible Focus Indicators:** A clear, high-contrast focus indicator must be present on the focused element. Per ThinkAlike guidelines, this should be a `3px solid` outline in ThinkAlike Orange (`#FF9900`).
*   **Active Link Indication (`aria-current`):**
    *   The currently active navigation link (representing the current page) must have `aria-current="page"` set. This is crucial for screen reader users to understand their location.
*   **Color Contrast:**
    *   All text and meaningful icons must meet WCAG AAA color contrast ratios against their background to ensure readability for users with low vision. This applies to default, hover, focus, and active states.
*   **Icons:**
    *   If icons are used without visible text labels (not generally recommended for primary navigation), they must have appropriate `aria-label` or visually hidden text to convey their meaning.
*   **ARIA Roles & Attributes:**
    *   All navigation links must use `aria-current="page"` for the active link.
    *   All icon-only or ambiguous controls must have `aria-label`.
    *   If the navigation bar is busy (e.g., loading links), use `aria-busy="true"`.
    *   If the user menu is expandable, use `aria-expanded` and `aria-controls`.
    *   All error states must set `aria-invalid="true"` and link to error descriptions with `aria-describedby`.
*   **Screen Reader Experience:**
    *   The navigation bar, skip link, and all states (active, error, busy) must be clearly announced. Error states must be described with clear, non-alarming language.

---

## 5. PET/Clarity & Ethical Alignment

**Privacy:**
- The NavigationBar does not collect or expose user data. If user/account menu is present, only display data the user has explicitly consented to share.

**Ethics:**
- Navigation is always non-deceptive, never manipulative. All actions are opt-in and clearly labeled. No dark patterns.

**Transparency:**
- The user's current location, available paths, and the implications of navigation are always clear. The skip link and focus indicators reinforce transparency and agency.

**Clarity Protocol:**
- All labels, icons, and states must be immediately understandable. Ambiguity is avoided.

---

## 6. Symbolic Resonance & Ritual Integration

- The NavigationBar is the ritual axis and compass, grounding the user in the symbolic cosmos of ThinkAlike.
- Each navigation act is a ritual crossing, and the bar's design, transitions, and glyphs (from symbolic_myth_index.md) reinforce this.
- The logo/sigil is the "mundane mandala," a daily invocation of belonging and orientation.
- Subtle realm transitions (e.g., shimmer, glyph accent) mark the crossing of thresholds, echoing the rites described in portal_specification.md and resonance_network_specification.md.
- The skip link is a ritual threshold, honoring accessibility as a sacred act.

---

## 7. Implementation Echoes (Examples)

### Example 1: Basic NavigationBar Setup

```typescript jsx
// filepath: app/components/layout/AppLayout.tsx (Conceptual Placement)
import NavigationBar from '@/components/ui_components/NavigationBar'; // Assuming path
import LogoIcon from '@/assets/icons/LogoIcon'; // Example SVG icon component

const navLinks = [
  { label: 'Dashboard', href: '/dashboard', id: 'nav-dashboard' },
  { label: 'Realms', href: '/realms', id: 'nav-realms' },
  { label: 'Agents', href: '/agents', id: 'nav-agents' },
  { label: 'Corpus Magnus', href: '/corpus-magnus', id: 'nav-corpus' },
];

// In your AppLayout component's render method:
<NavigationBar
  ariaLabel="Main site navigation"
  logo={<LogoIcon aria-label="ThinkAlike Home" />}
  projectName="ThinkAlike"
  links={navLinks}
  // userMenu={<UserMenuComponent />} // Example
>
  {/* Optional: <GlobalSearchInput /> */}
</NavigationBar>
```

*(Note: Active link state (`aria-current="page"`) would typically be handled internally by the `NavigationBar` or a routing-aware wrapper by comparing `link.href` with the current browser path.)*

### Example 2: NavigationBar with Skip Link (Conceptual)

The "Skip to main content" link is often implemented at the `AppLayout` level to be truly the first item or handled within `NavigationBar` if it's the first rendered interactive block.

```typescript jsx
// Conceptual structure for a skip link
// This might be part of NavigationBar.tsx or a global AppLayout feature

// In NavigationBar.tsx or a wrapper:
const SkipLink = () => (
  <a href="#main-content" className="sr-only focus:not-sr-only focus:fixed focus:top-2 focus:left-2 focus:p-2 focus:bg-orange-500 focus:text-white focus:z-50">
    Skip to main content
  </a>
);

// ... then in NavigationBar's render:
// <SkipLink />
// <nav aria-label={ariaLabel}> ... </nav>

// And PageContainer would have: <PageContainer id="main-content" ... />
```

### Example 3: Error State (Conceptual)

```typescript jsx
// Example: NavigationBar with error state (e.g., failed to load links)
<NavigationBar
  ariaLabel="Main site navigation"
  logo={<LogoIcon aria-label="ThinkAlike Home" />}
  projectName="ThinkAlike"
  links={[]}
  className="error-state"
  aria-busy="false"
  aria-invalid="true"
  aria-describedby="nav-error-desc"
>
  <div id="nav-error-desc" style={{ color: '#FF4136', fontWeight: 'bold' }}>
    Navigation links could not be loaded. Please try again or contact support.
  </div>
</NavigationBar>
```

---

## 8. Changelog

*   **2025-06-09 :: v1.1.1 :: COMPREHENSIVE HARMONIZATION – Aligned with Alchemical Interface Initiative, PET/Clarity, symbolic/ritual standards, Error Red error states, and WCAG AAA accessibility targets. Ensured full support for restored Portal & Resonance Network flows.**
*   **2025-06-09 (v1.1):**
    *   Harmonized for Alchemical Interface Initiative and symbolic/ritual framing.
    *   Deepened language on NavigationBar as "ritual axis mundi," compass, and threshold guardian.
    *   Clarified logo/sigil as "mundane mandala" and ritual anchor.
    *   Added guidance on subtle visual shifts for realm transitions.
    *   Reaffirmed PET/Clarity, accessibility, and ethical navigation protocols.
    *   Updated implementation echoes and accessibility notes.
*   **2025-06-09 (v1.0):**
    *   Initial draft created.
    *   Established role as "global compass" and "ritual axis" within AppLayout's "ritual shell."
    *   Defined core visual style, elements, and symbolic considerations (gravity, interconnected realms).
    *   Outlined props (`links`, `logo`, `ariaLabel`, etc.).
    *   Detailed crucial accessibility requirements: semantic HTML, skip link, keyboard navigation, focus indicators, `aria-current`, color contrast.
    *   Aligned with PET/Clarity and Symbolic Protocols, emphasizing transparency and navigable universe.
    *   Provided initial implementation examples.

---

<div align="center">
<img src="../assets/thinkalike_logo.svg" alt="ThinkAlike Logo Placeholder" width="40" height="40" />
<br/>
<em>ThinkAlike — Harmonizing Human & Machine</em>
</div>
