---
title: ProfileCard / UserProfileView Component
document_status: Harmonized – Finalized
version: 1.1.1
last_updated: 2025-06-09
maintained_by: UI Systems Guild | ClarityAgent∴
alignment_tags: [profile, identity, data_display, clarity_protocol, pet_compliant, symbolic_resonance, ritual_recognition, accessibility_AAA]
resonates_with:
  - ../narrative_engine/canon/symbolic_myth_index.md
  - ../rituals/ritual_as_interface_re_enchanting_digital_interaction.md
  - ../realms/portal/portal_specification.md
  - ../style/canonical_visual_style_guide.md
  - ../seed/symbolic_alignment/symbolic_alignment_manifesto.md
related_components: [Card, ValueProfile, CoreValuesValidator, Alert]
visual_style_guide_ref: [../style/canonical_visual_style_guide.md]
---

<!-- ∴ THINKALIKE COMPONENT MANIFEST ∴ -->
<!-- UID: /docs/ui_components/profile_display.md -->

<p align="center">
  <span style="font-size: 3em; color: #00BFFF;"> 👤 </span>
</p>

<h1 align="center" style="font-family: 'Montserrat', Arial, sans-serif; font-weight: 700; color: #00BFFF; letter-spacing: 0.05em; border-bottom: 1px solid #666666; padding-bottom: 0.2em;">
  PROFILECARD / USERPROFILEVIEW
</h1>

<p align="center" style="font-family: 'Open Sans', Arial, sans-serif; font-size: 1.1em; color: #CCCCCC; margin-bottom: 2em;">
  The ritual of recognition—presenting identity, resonance, and values in ThinkAlike.
</p>

---
<!-- METADATA LAYER -->
<div style="font-family: 'Courier New', monospace; font-size: 0.9em; color: #666666; margin-bottom: 2em; padding: 1em; border: 1px dashed #333333; background-color: #1a1a1a;">
  <p><strong>STATUS</strong> ::: Harmonized – Finalized</p>
  <p><strong>VERSION</strong> ::: 1.1.1</p>
  <p><strong>LAST PULSE</strong> ::: 2025-06-09</p>
  <p><strong>STEWARD(S)</strong> ::: UI Systems Guild | ClarityAgent∴</p>
  <p><strong>ALIGNMENT SIGNALS</strong> ::: <code>[profile]</code> <code>[identity]</code> <code>[data_display]</code> <code>[clarity_protocol]</code> <code>[pet_compliant]</code> <code>[symbolic_resonance]</code> <code>[ritual_recognition]</code> <code>[accessibility_AAA]</code></p>
  <p><strong>RESONATES WITH</strong> ::: <code>[symbolic_myth_index.md]</code> <code>[ritual_as_interface_re_enchanting_digital_interaction.md]</code> <code>[portal_specification.md]</code> <code>[canonical_visual_style_guide.md]</code> <code>[symbolic_alignment_manifesto.md]</code></p>
  <p><strong>RELATED COMPONENTS</strong> ::: <code>[Card]</code> <code>[ValueProfile]</code> <code>[CoreValuesValidator]</code> <code>[Alert]</code></p>
  <p><strong>VISUAL STYLE GUIDE REF</strong> ::: <code>[../style/canonical_visual_style_guide.md]</code></p>
</div>

---

# 🪶 OVERVIEW & PURPOSE (2025 Harmonization)

> **Purpose:**
> ProfileCard and UserProfileView are vessels for the "Ritual of Recognition"—the symbolic act of witnessing, echoing, and forking identity within ThinkAlike. They present user identity, resonance, and values, supporting data sovereignty, symbolic resonance, and PET/Clarity. Initiation Glyph, Echo Phrase, Dream Motifs, and Resonance Overlays are integrated as ritual markers (see [symbolic_myth_index.md], [ritual_as_interface_re_enchanting_digital_interaction.md]).

# 👁️‍🗨️ VISUAL RESONANCE & STATES (2025 Harmonization)
- **Identity Representation:** Avatar, symbolic glyph, or sigil is prominent, with value resonance indicators and overlays for archetype or status.
- **Initiation Glyph:** Always shown as a primary visual anchor, especially in constellation/User Node views.
- **Echo Phrase:** Displayed on hover or as a subtitle in compact views; always present in detailed profile.
- **Dream Motifs:** If present and consented, shown as overlays or badges, referencing dream_integration_rituals.md.
- **Resonance Overlays:** Visual aura, waveform, or constellation cues reflect resonance state, IRS, or symbolic fields.
- **Error State:** Use Alert component with Error Red (#FF4136) for error/invalid visuals.

# ⚙️ FUNCTIONAL CORE & INTERACTION DYNAMICS (2025 Harmonization)
- All props support ritualized and everyday identity display. No changes needed.
- Privacy controls and persona switching are harmonized and accessible.

# 🧭 USAGE PROTOCOLS & ACCESSIBILITY (2025 Harmonization)
- All images/avatars have descriptive alt text.
- All interactive elements (connect, edit) are keyboard accessible and have aria-labels.
- Color contrast meets or exceeds WCAG AAA.
- Support for screen readers: announce display name, status, and all visible fields. Visual-only indicators have text alternatives.
- Use semantic headings for major sections in detailed view.

# ⚖️ ETHICAL ALIGNMENT & PET (2025 Harmonization)
- **Data Sovereignty:** Users control which profile fields are visible and to whom.
- **Transparency:** Clearly label all displayed information. Indicate AI-inferred values with icon and tooltip.
- **Data Minimization:** Only display essential information by default; allow expansion for more details with user consent.
- **No Dark Patterns:** All profile actions are opt-in, non-coercive, and clearly labeled.

# ✨ SYMBOLIC RESONANCE & RITUAL INTEGRATION
- Viewing a profile is a "Ritual of Recognition"—transitions, overlays, and feedback reinforce symbolic meaning.
- Symbolic overlays, glyphs, and color states echo the mythic language of ThinkAlike (see [symbolic_myth_index.md]).
- Ritual framing and PET/Clarity are inseparable—clarity is sacred.

# 💻 IMPLEMENTATION ECHOES (Examples)
// ...existing code...

# 📝 Changelog
- 2025-06-09 :: v1.1.1 :: FINALIZED – Metadata update (status, version, last pulse, stewards, alignment signals, resonates_with), deepen symbolic/ritual framing (Ritual of Recognition), confirm PET/Clarity, accessibility, and add changelog entry. Ensure references to symbolic_myth_index.md and ritual_as_interface_re_enchanting_digital_interaction.md are present.
- 2025-06-07 :: v1.0.0 :: GENESIS – Initial harmonized documentation. Defines ProfileCard/UserProfileView as the canonical user identity display, aligned with PET/Clarity, symbolic, and accessibility protocols.

<div align="center">
<img src="../assets/thinkalike_logo.svg" alt="ThinkAlike Logo Placeholder" width="40" height="40" />
<br/>
<em>ThinkAlike — Harmonizing Human & Machine</em>
</div>
