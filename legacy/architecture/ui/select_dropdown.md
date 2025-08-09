---
title: SelectDropdown
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

<!-- ∴ THINKALIKE COMPONENT MANIFEST ∴ -->
<!-- UID: /docs/ui_components/select_dropdown.md -->

<br/>

<p align="center">
  <!-- Placeholder for a prominent Component Glyph or ThinkAlike Sigil -->
  <span style="font-size: 3em; color: #FF8C00;"> ▼ </span> <!-- Example Dropdown Arrow Glyph -->
</p>

<h1 align="center" style="font-family: 'Montserrat', Arial, sans-serif; font-weight: 700; color: #FF8C00; letter-spacing: 0.05em; border-bottom: 1px solid #666666; padding-bottom: 0.2em;">
  SELECT DROPDOWN
</h1>

<p align="center" style="font-family: 'Open Sans', Arial, sans-serif; font-size: 1.1em; color: #CCCCCC; margin-bottom: 2em;">
  Enabling users to choose from a predefined set of options with clarity and precision.
</p>

---
<!-- METADATA LAYER -->
<div style="font-family: 'Courier New', monospace; font-size: 0.9em; color: #666666; margin-bottom: 2em; padding: 1em; border: 1px dashed #333333; background-color: #1a1a1a;">
  <p><strong>STATUS</strong> ::: Harmonized – Finalized</p>
  <p><strong>VERSION</strong> ::: 1.1.1</p>
  <p><strong>LAST PULSE</strong> ::: 2025-06-09</p>
  <p><strong>STEWARD(S)</strong> ::: UI Systems Guild | ClarityAgent∴</p>
  <p><strong>ALIGNMENT SIGNALS</strong> ::: <code>[input]</code> <code>[form_element]</code> <code>[accessibility_AAA]</code> <code>[pet_compliant]</code> <code>[clarity_protocol]</code> <code>[selection_control]</code> <code>[ritual_choice]</code> <code>[error_red]</code></p>
  <p><strong>RESONATES WITH</strong> ::: <code>[../style/canonical_visual_style_guide.md]</code> <code>[Form.md]</code> <code>[Button.md]</code> <code>[Alert.md]</code> <code>[../narrative_engine/canon/symbolic_myth_index.md]</code> <code>[../noetica/corpus_magnus/art_aesthetics_and_culture/ritual_as_interface_re_enchanting_digital_interaction.md]</code></p>
</div>

---

# SelectDropdown

> **Purpose:**
> The SelectDropdown component enables users to make a single, definitive choice from a predefined set—often a symbolic or consequential selection within the Portal Realm (e.g., dilemmas, archetypal affinities, privacy levels). Each selection can directly influence the user's `UserValueProfile`, narrative path, or symbolic state, and is always presented with PET/Clarity and ritual intent. See also: [../noetica/corpus_magnus/art_aesthetics_and_culture/ritual_as_interface_re_enchanting_digital_interaction.md].

**Symbolic Role:**
- The SelectDropdown is a ritual "Choice Declaration"—a symbolic act of alignment, path selection, or value affirmation. Its color, iconography, and feedback reinforce the mythic and ritual language of ThinkAlike (see [../narrative_engine/canon/symbolic_myth_index.md]).
- The use of **Error Red (#FF4136)** for all error/invalid visuals is a ritual standard, never to be substituted.

**Last Updated:** June 9, 2025
**Version:** 1.1.1 (Harmonized for Alchemical Interface Initiative, symbolic/ritual framing, and PET/Clarity)
**Related Components:** `Form`, `Button`, `Alert`
**Core Principles Embodied:** Clarity, Accessibility, PET/Clarity, Symbolic Resonance, Ritual Presence

## Visual & Symbolic Guidelines (2025 Harmonization)
- **Style:** Minimalist, consistent with other input fields, ensuring the dropdown is easily identifiable and usable. Adheres to the `canonical_visual_style_guide.md`.
- **Shape:** Rectangular field with rounded corners (radius: 6px), typically with a downward-pointing arrow or chevron glyph on the right side to indicate dropdown functionality.
- **Color:**
    *   Default Background: "Light Gray (Subtle)" (`#CCCCCC`) or a slightly darker shade of the page background.
    *   Border: "Medium Gray (UI Elements)" (`#666666`).
    *   Focus Border/Outline: "Amber/Honey Yellow (Neutral)" (`#FFC300`) or "Electric Blue (Accent)" (`#00FFFF`).
    *   Text Color (Selected Value): "Dark Gray (Text)" (`#333333`) or "White (Text/Highlights)" (`#FFFFFF`).
    *   Dropdown Arrow Glyph: "Dark Gray (Text)" or "Medium Gray (UI Elements)".
    *   Dropdown Panel Background: "Light Gray (Subtle)" or a slightly off-black if main background is dark.
    *   Option Text Color: "Dark Gray (Text)" or "White (Text/Highlights)".
    *   Option Hover/Focus Background: "Amber/Honey Yellow (Neutral)" (subtle shade) with contrasting text.
    *   Option Selected Background (in open panel): "Deep Mandarine Orange (Active)" (subtle shade) with contrasting text.
    *   **Error State Border: Error Red (#FF4136).**
- **Iconography:** The dropdown indicator (arrow/chevron) should be a clear, simple glyph. Options within the dropdown can optionally have leading icons/glyphs.
- **Accessibility:** Always associated with a visible `label` element.

## Usage
```jsx
const options = [
  { value: 'seeker', label: 'The Seeker Archetype 🧭' },
  { value: 'architect', label: 'The Architect Archetype 🏛️' },
  { value: 'trickster', label: 'The Trickster Archetype 🎭' },
];

<SelectDropdown
  label="Choose Your Guiding Archetype"
  options={options}
  selectedValue={selectedArchetype}
  onSelectionChange={(value) => setSelectedArchetype(value)}
  placeholder="Select an archetype..."
/>
```

## Props
| Name              | Type                                                                 | Required | Description                                                                 |
|-------------------|----------------------------------------------------------------------|----------|-----------------------------------------------------------------------------|
| `label`           | `string`                                                             | Yes      | Visible label for the select dropdown, crucial for accessibility.           |
| `options`         | `Array<{value: string; label: string; disabled?: boolean; icon?: ReactNode}>` | Yes | Array of objects representing the dropdown options.                         |
| `selectedValue`   | `string`                                                             | Yes      | The value of the currently selected option.                                 |
| `onSelectionChange` | `(value: string) => void`                                           | Yes      | Handler called when the user selects an option.                             |
| `id`              | `string`                                                             | No       | HTML id attribute. If not provided, one will be generated for label association. |
| `name`            | `string`                                                             | No       | HTML name attribute.                                                        |
| `placeholder`     | `string`                                                             | No       | Text displayed when no option is selected.                                  |
| `disabled`        | `boolean`                                                            | No       | Disables the select dropdown.                                               |
| `required`        | `boolean`                                                            | No       | Marks the select as required for form submission.                           |
| `error`           | `string \| boolean`                                                  | No       | Indicates an error state. If string, displays as an error message below the select. |
| `helperText`      | `string`                                                             | No       | Additional instructional text displayed below the select.                   |
| `allowEmptyOption`| `boolean`                                                            | No       | If true, allows an empty selection (often represented by the placeholder). Defaults to false.

## PET/Clarity & Symbolic Protocols
- **Privacy:**
    - The component itself does not store selection history beyond the current interaction unless explicitly designed as part of a larger, consented-to data logging feature.
- **Ethics:**
    - Options must be presented clearly and without bias. Avoid pre-selecting options in a way that nudges users towards a specific choice without their awareness.
    - If options have significant implications (e.g., privacy settings, identity declarations), these should be clearly explained in the label or helperText.
- **Transparency:**
    - The currently selected value is always clearly visible.
    - The full list of available options is easily accessible when the dropdown is opened.
    - Error states clearly indicate why a selection might be invalid or required.
- **Symbolic:**
    - The SelectDropdown can be used in ritualistic choice-making processes, such as selecting an "Archetypal Entry" during onboarding (as per seed/initiation_pathways/archetypal_entry_map.md).
    - The options themselves can be imbued with symbolic meaning, potentially using glyphs (option.icon) from symbol_mappings_index.md alongside labels.
    - The act of selection can be framed as "Declaring an Alignment" or "Choosing a Path."

## Accessibility
- The label prop is mandatory and visibly associated with the SelectDropdown.
- Implement using native <select> element or by adhering to ARIA patterns for custom select/listbox widgets (e.g., role="combobox", aria-haspopup="listbox", aria-expanded, aria-activedescendant, role="listbox", role="option").
- Fully keyboard navigable: open dropdown (Enter, Space, Alt+DownArrow), navigate options (ArrowUp, ArrowDown, Home, End, PageUp, PageDown, type-ahead), select option (Enter, Space), close dropdown (Escape).
- Selected option should be clearly announced.
- Error messages (error prop) should be programmatically linked and announced.
- Sufficient contrast for all text, borders, and interactive states.

## Example
```jsx
const privacyLevels = [
  { value: 'private', label: 'Private (Only Me 🛡️)' },
  { value: 'resonant', label: 'Resonant (Shared with Aligned Nodes ✨)' },
  { value: 'hive_shared', label: 'Hive Shared (Visible to My Communities 🐝)' },
  { value: 'public_commons', label: 'Public Commons (Visible to All 🌐)' },
];

const [selectedPrivacy, setSelectedPrivacy] = useState('private');

return (
  <FormElement>
    <SelectDropdown
      label="Narrative Visibility"
      id="narrative-privacy"
      options={privacyLevels}
      selectedValue={selectedPrivacy}
      onSelectionChange={setSelectedPrivacy}
      helperText="Choose who can see your personal narrative."
      required
    />
  </FormElement>
);
```

## Migration Notes
- Legacy dropdowns must be updated to use the standardized options prop structure and accessibility patterns.
- Ensure visible label is always provided.
- Align visual styling with canonical_visual_style_guide.md and the states defined herein.
- Validate that keyboard navigation and ARIA attributes are correctly implemented for custom dropdowns.

## Changelog
- **2025-06-09 :: v1.1.1 :: FINALIZE** – Metadata update (status, version, last pulse, stewards, alignment signals, resonates_with), deepen symbolic/ritual framing (Choice Declaration), confirm Error Red for error/invalid, PET/Clarity, accessibility, and add changelog entry. Ensure references to symbolic_myth_index.md and ritual_as_interface_re_enchanting_digital_interaction.md are present.
- **2025-06-07 :: v1.0.1 :: UPDATE** – Standardized error state visuals to use Error Red (#FF4136).
- 2025-06-07 :: v1.0.0 :: GENESIS – Initial harmonized documentation. Aligned with canonical template, PET/Clarity protocols, and visual/symbolic requirements for selection controls.
- 2025-06-08 :: v1.1.0 :: HARMONIZED – Expanded guidance for Portal Realm, clarified error state color, PET/Clarity, symbolic/ritual framing, and icon support in options.

<div align="center">
<img src="../assets/thinkalike_logo.svg" alt="ThinkAlike Logo Placeholder" width="40" height="40" />
<br/>
<em>ThinkAlike — Harmonizing Human & Machine</em>
</div>
