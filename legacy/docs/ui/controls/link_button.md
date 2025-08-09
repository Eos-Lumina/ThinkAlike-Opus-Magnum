---
title: LinkButton Component
document_status: Harmonized – Finalized
version: 1.1.1
last_updated: 2025-06-09
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
alignment_tags:
- navigation
- link
- accessibility_landmark
- clarity_protocol
- pet_compliant
- ritual_portal
- symbolic_resonance
resonates_with:
- ../narrative_engine/canon/symbolic_myth_index.md
- ../rituals/ritual_as_interface_re_enchanting_digital_interaction.md
- ../realms/portal/portal_specification.md
- ../style/canonical_visual_style_guide.md
- ../seed/symbolic_alignment/symbolic_alignment_manifesto.md
related_components:
- NavigationBar
- Sidebar
- Button
- Alert
visual_style_guide_ref:
- ../style/canonical_visual_style_guide.md
tags:
- controls
---


<!-- ∴ THINKALIKE COMPONENT MANIFEST ∴ -->
<!-- UID: /docs/ui_components/link_button.md -->

<p align="center">
  <span style="font-size: 3em; color: #00BFFF;"> 🔗 </span>
</p>

<h1 align="center" style="font-family: 'Montserrat', Arial, sans-serif; font-weight: 700; color: #00BFFF; letter-spacing: 0.05em; border-bottom: 1px solid #666666; padding-bottom: 0.2em;">
  LINK BUTTON
</h1>

<p align="center" style="font-family: 'Open Sans', Arial, sans-serif; font-size: 1.1em; color: #CCCCCC; margin-bottom: 2em;">
  A symbolic, accessible navigation link—bridging realms, not just triggering actions.
</p>

---
<!-- METADATA LAYER -->
<div style="font-family: 'Courier New', monospace; font-size: 0.9em; color: #666666; margin-bottom: 2em; padding: 1em; border: 1px dashed #333333; background-color: #1a1a1a;">
  <p><strong>STATUS</strong> ::: Harmonized – Finalized</p>
  <p><strong>VERSION</strong> ::: 1.1.1</p>
  <p><strong>LAST PULSE</strong> ::: 2025-06-09</p>
  <p><strong>STEWARD(S)</strong> ::: UI Systems Guild | ClarityAgent∴</p>
  <p><strong>ALIGNMENT SIGNALS</strong> ::: <code>[navigation]</code> <code>[link]</code> <code>[accessibility_landmark]</code> <code>[clarity_protocol]</code> <code>[pet_compliant]</code> <code>[ritual_portal]</code> <code>[symbolic_resonance]</code></p>
  <p><strong>RESONATES WITH</strong> ::: <code>[symbolic_myth_index.md]</code> <code>[ritual_as_interface_re_enchanting_digital_interaction.md]</code> <code>[portal_specification.md]</code> <code>[canonical_visual_style_guide.md]</code> <code>[symbolic_alignment_manifesto.md]</code></p>
  <p><strong>RELATED COMPONENTS</strong> ::: <code>[NavigationBar]</code> <code>[Sidebar]</code> <code>[Button]</code> <code>[Alert]</code></p>
  <p><strong>VISUAL STYLE GUIDE REF</strong> ::: <code>[../style/canonical_visual_style_guide.md]</code></p>
</div>

---

# 🪶 OVERVIEW & PURPOSE (2025 Harmonization)

> **Purpose:**
> The LinkButton is a vessel for the "Ritual of Passage"—a symbolic, accessible navigation element for traversing realms, pages, or features. It is strictly for navigation (never actions), always rendered as an anchor (<a>), and visually distinct from Button. LinkButton is the ritual "portal" or "bridge" for movement between contexts (see [symbolic_myth_index.md], [ritual_as_interface_re_enchanting_digital_interaction.md]).

# 👁️‍🗨️ VISUAL RESONANCE & STATES (2025 Harmonization)
- **Style:** Minimalist, underlined by default for clear link affordance. Uses canonical link colors and visible focus ring.
- **Symbolic Role:** Represents a "portal" or "bridge"—the ritual act of traversing realms or contexts. Optional icons reinforce direction or purpose.
- **Error State:** Use Alert component with Error Red (#FF4136) for error/invalid visuals.

# ⚙️ FUNCTIONAL CORE & INTERACTION DYNAMICS (2025 Harmonization)
- All props support ritualized and everyday navigation. No changes needed.
- Always renders as a semantic <a> element, never as <button>.

# 🧭 USAGE PROTOCOLS & ACCESSIBILITY (2025 Harmonization)
- Fully keyboard accessible. Disabled links are skipped in tab order.
- Always uses aria-label (required). Screen readers announce link text and destination.
- Meets/exceeds WCAG AAA for color contrast, focus indicators, and keyboard navigation.
- External links use rel="noopener noreferrer" and indicate new tab.

# ⚖️ ETHICAL ALIGNMENT & PET (2025 Harmonization)
- **Transparency:** Destination must be visually and programmatically clear. No deceptive linking.
- **Privacy:** Do not expose sensitive data in URLs.
- **Ethics:** Never use for destructive or state-changing actions. All links must be clearly labeled and accessible.
- **No Dark Patterns:** All navigation is opt-in, non-coercive, and clearly labeled.

# ✨ SYMBOLIC RESONANCE & RITUAL INTEGRATION
- LinkButton is a "portal"—the act of clicking is a ritual transition. Icons reinforce symbolic direction or purpose.
- Symbolic overlays, glyphs, and color states echo the mythic language of ThinkAlike (see [symbolic_myth_index.md]).
- Ritual framing and PET/Clarity are inseparable—clarity is sacred.

# 💻 IMPLEMENTATION ECHOES (Examples)
```jsx
// Internal navigation
<LinkButton href="/about" ariaLabel="About ThinkAlike">About</LinkButton>

// With left icon
<LinkButton href="/community" leftIcon={<CommunityIcon />} ariaLabel="Go to Community">Community</LinkButton>

// With right icon
<LinkButton href="/data" rightIcon={<ArrowIcon />} ariaLabel="Explore Data">Data</LinkButton>

// External link (new tab, with rel)
<LinkButton href="https://external.site" target="_blank" rel="noopener noreferrer" ariaLabel="External Resource (opens in new tab)">
  External Resource
  <ExternalLinkIcon />
</LinkButton>

// Disabled link
<LinkButton href="/future" ariaLabel="Coming Soon" disabled>Coming Soon</LinkButton>
```

# 📝 Changelog
- 2025-06-09 :: v1.1.1 :: FINALIZED – Metadata update (status, version, last pulse, stewards, alignment signals, resonates_with), deepen symbolic/ritual framing (Ritual of Passage), confirm PET/Clarity, accessibility, and add changelog entry. Ensure references to symbolic_myth_index.md and ritual_as_interface_re_enchanting_digital_interaction.md are present.
- 2025-06-09 :: v1.1.0 :: Deepened distinction from Button, clarified visual/focus/disabled states, reinforced PET/Clarity and symbolic protocols, expanded accessibility, and added explicit examples for internal/external/disabled links and icons.
- 2025-06-07 :: v1.0.0 :: GENESIS – Initial harmonized documentation. Defines LinkButton as the canonical navigation link, aligned with PET/Clarity, symbolic, and accessibility protocols.

<div align="center">
<img src="../assets/thinkalike_logo.svg" alt="ThinkAlike Logo Placeholder" width="40" height="40" />
<br/>
<em>ThinkAlike — Harmonizing Human & Machine</em>
</div>
