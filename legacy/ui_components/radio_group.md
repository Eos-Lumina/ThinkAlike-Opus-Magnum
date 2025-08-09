---
title: RadioGroup
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

<!-- ∴ THINKALIKE COMPONENT MANIFEST ∴ -->
<!-- UID: /docs/ui_components/radio_group.md -->

<br/>

<p align="center">
  <!-- Placeholder for a prominent Component Glyph or ThinkAlike Sigil -->
  <span style="font-size: 3em; color: #FF8C00;"> ◎ </span> <!-- Example Radio Button/Choice Glyph -->
</p>

<h1 align="center" style="font-family: 'Montserrat', Arial, sans-serif; font-weight: 700; color: #FF8C00; letter-spacing: 0.05em; border-bottom: 1px solid #666666; padding-bottom: 0.2em;">
  RADIO GROUP
</h1>

<p align="center" style="font-family: 'Open Sans', Arial, sans-serif; font-size: 1.1em; color: #CCCCCC; margin-bottom: 2em;">
  Enabling users to select one exclusive option from a set of choices.
</p>

---
<!-- METADATA LAYER -->
<div style="font-family: 'Courier New', monospace; font-size: 0.9em; color: #666666; margin-bottom: 2em; padding: 1em; border: 1px dashed #333333; background-color: #1a1a1a;">
  <p><strong>STATUS</strong> ::: Harmonized – Finalized</p>
  <p><strong>VERSION</strong> ::: 1.1.1</p>
  <p><strong>LAST PULSE</strong> ::: 2025-06-09</p>
  <p><strong>STEWARD(S)</strong> ::: UI Systems Guild | ClarityAgent∴</p>
  <p><strong>ALIGNMENT SIGNALS</strong> ::: <code>[input]</code> <code>[form_element]</code> <code>[accessibility_AAA]</code> <code>[pet_compliant]</code> <code>[clarity_protocol]</code> <code>[single_selection]</code> <code>[ritual_stance]</code> <code>[error_red]</code></p>
  <p><strong>RESONATES WITH</strong> ::: <code>[../style/canonical_visual_style_guide.md]</code> <code>[Form.md]</code> <code>[Checkbox.md]</code> <code>[../narrative_engine/canon/symbolic_myth_index.md]</code> <code>[../noetica/corpus_magnus/art_aesthetics_and_culture/ritual_as_interface_re_enchanting_digital_interaction.md]</code></p>
</div>

---

# RadioGroup

> **Purpose:**
> The RadioGroup component allows users to select one single option from a mutually exclusive set of choices. It is essential for scenarios requiring a definitive selection where only one option can be active at a time. Harmonized with ThinkAlike’s PET/Clarity protocols, it ensures choices are presented clearly, interactions are accessible, and user agency in selection is upheld. See also: [../noetica/corpus_magnus/art_aesthetics_and_culture/ritual_as_interface_re_enchanting_digital_interaction.md].

**Symbolic Role:**
- The RadioGroup is a ritual "Definitive Stance"—a symbolic act of exclusive alignment or commitment. Its color, iconography, and feedback reinforce the mythic and ritual language of ThinkAlike (see [../narrative_engine/canon/symbolic_myth_index.md]).
- The use of **Error Red (#FF4136)** for all error/invalid visuals is a ritual standard, never to be substituted.

**Last Updated:** June 9, 2025
**Version:** 1.1.1 (Harmonized for Alchemical Interface Initiative, symbolic/ritual framing, and PET/Clarity)
**Related Components:** `Form`, `Checkbox`
**Core Principles Embodied:** Clarity, Accessibility, PET/Clarity, Symbolic Resonance, Ritual Presence

## Visual & Symbolic Guidelines
- **Style:** Minimalist, with clear visual distinction for selected and unselected states. Each radio button within the group is typically accompanied by a label. Adheres to the `canonical_visual_style_guide.md`.
- **Shape:** Individual radio buttons are circular. A smaller inner circle or a solid fill indicates the selected state.
- **Color:**
    *   Circle Border (Unselected): "Medium Gray (UI Elements)" (`#666666`).
    *   Circle Background (Unselected): Transparent or "Light Gray (Subtle)" (`#CCCCCC`).
    *   Inner Circle/Fill (Selected): "Amber/Honey Yellow (Neutral)" (`#FFC300`) or "Deep Mandarine Orange (Active)" (`#F86B03`).
    *   Focus Indicator: Outline using "Electric Blue (Accent)" (`#00FFFF`).
    *   Label Text: "Dark Gray (Text)" (`#333333`) or "White (Text/Highlights)".
    *   Disabled State: Reduced opacity for circles and labels.
    *   **Error State Border/Outline: Error Red (#FF4136).**
- **Iconography:** The inner filled circle is the primary selection indicator.
- **Accessibility:** The group must have an overall `legend` or group label, and each radio button must have its individual `label`.

## Usage
```jsx
const roleOptions = [
  { value: 'weaver', label: 'The Weaver (Systems Design)' },
  { value: 'flamekeeper', label: 'The Flamekeeper (Ethics & Signal)' },
  { value: 'trickster', label: 'The Trickster (Semantics & Form)' },
];

<RadioGroup
  groupLabel="Select Your Primary Archetypal Domain"
  name="archetypeDomain"
  options={roleOptions}
  selectedValue={selectedDomain}
  onChange={(value) => setSelectedDomain(value)}
/>
```

## Props
| Name         | Type                                                                 | Required | Description                                                        |
|--------------|----------------------------------------------------------------------|----------|--------------------------------------------------------------------|
| `groupLabel` | `string`                                                             | Yes      | A visible label for the entire radio group (often rendered as a legend). |
| `name`       | `string`                                                             | Yes      | The common name attribute for all radio buttons in the group, ensuring exclusivity. |
| `options`    | `Array<{value: string; label: string; disabled?: boolean; id?: string}>` | Yes | Array of objects representing individual radio button options.      |
| `selectedValue` | `string`                                                          | Yes      | The value of the currently selected radio button.                  |
| `onChange`   | `(value: string) => void`                                            | Yes      | Handler called when the selected radio button changes.              |
| `idPrefix`   | `string`                                                             | No       | A prefix for generating unique IDs for each radio button if not provided in options. Defaults to name. |
| `disabled`   | `boolean`                                                            | No       | Disables the entire radio group.                                   |
| `error`      | `string \| boolean`                                                  | No       | Indicates an error state for the group (e.g., if a selection is required but none made). |
| `helperText` | `string`                                                             | No       | Additional instructional text displayed for the group.             |
| `layout`     | `'vertical' \| 'horizontal'`                                         | No       | Specifies the layout direction of radio options. Defaults to vertical.|

## PET/Clarity & Symbolic Protocols
- **Privacy:**
    - Selections should not be tracked or used for profiling beyond the explicit context of the choice (e.g., form submission, setting preference) without clear consent.
- **Ethics:**
    - Labels for each option must be clear and accurately represent the choice. Avoid leading or biased phrasing.
    - Ensure a meaningful default selection if appropriate, or require an active choice if no default is suitable. The default should be transparent and user-centric.
- **Transparency:**
    - It must be visually obvious which option is selected.
    - The exclusivity of choices (only one can be selected) is inherent to the component's behavior.
    - Error states or required indicators should be clearly communicated.
- **Symbolic:**
    - RadioGroup selections often represent a definitive commitment to one path or perspective within a "Forkable Identity" or narrative choice.
    - Used in "Ritual Affirmation" where a singular, clear stance is required (e.g., aligning with a core "Symbolic Law Protocol" or choosing an "Epistemic Match Mode").
    - The singular selected circle can symbolically represent a focused intent or a chosen "Resonance Field."

## Accessibility
- The groupLabel should be implemented as a legend within a fieldset that wraps the radio buttons.
- Each radio button (<input type="radio">) must have an associated label. Clicking the label should select the radio button.
- Use the same name attribute for all radio buttons within a group to ensure they are mutually exclusive.
- Each radio button should have a unique id attribute, linked to its label's htmlFor.
- Keyboard navigation:
    - Tab to enter the radio group.
    - Arrow keys (Up/Down for vertical, Left/Right for horizontal) to navigate between options and change selection.
    - The selected radio button should be focusable.
- Programmatically indicate the selected state using aria-checked="true".
- Error messages (error prop) should be programmatically linked and announced.
- Disabled state must be clearly indicated.

## Example
```jsx
const resonanceFrequencyOptions = [
  { value: 'low', label: 'Subtle Echo (Low Frequency)', id: 'freq-low' },
  { value: 'medium', label: 'Clear Signal (Medium Frequency)', id: 'freq-medium' },
  { value: 'high', label: 'Strong Resonance (High Frequency)', id: 'freq-high' },
];

const [currentFrequency, setCurrentFrequency] = useState('medium');

return (
  <FormElement> {/* Assuming a FormElement wrapper */}
    <RadioGroup
      groupLabel="Preferred Resonance Frequency"
      name="resonancePref"
      options={resonanceFrequencyOptions}
      selectedValue={currentFrequency}
      onChange={setCurrentFrequency}
      layout="vertical"
      helperText="This helps tailor your experience in the Resonance Network."
    />
  </FormElement>
);
```

## Migration Notes
- Legacy radio button groups must be wrapped in a fieldset with a legend (our groupLabel).
- Ensure consistent name attribute across all options in a group.
- Standardize selectedValue and onChange props for controlled state.
- Align visual styles with canonical_visual_style_guide.md.
- Verify full keyboard accessibility and ARIA attribute usage.

# 🪶 OVERVIEW & PURPOSE (2025 Harmonization)

> **Purpose:**
> The RadioGroup component enables users to make a mutually exclusive, definitive selection from a set of options—essential for forms, preference settings, and narrative choices where only one path can be chosen. It is harmonized for PET/Clarity, accessibility, and symbolic resonance, and is used wherever a singular, focused commitment is required in the Portal or Resonance Network.

## Visual & Symbolic Guidelines (2025 Harmonization)
- **Error State Color:** All error/invalid states (group label, border, error message) use **Error Red (#FF4136)**, never Neon Orange. This is required for all error visuals and meets/exceeds WCAG AAA contrast.
- **Selected State:** The selected radio button is visually distinct: circular, with an inner filled circle using "Amber/Honey Yellow" (#FFC300) or "Deep Mandarine Orange" (#F86B03).
- **Focus Indicator:** Outline uses "Electric Blue (Accent)" (#00FFFF), always visible on keyboard focus.
- **Layout:** The `layout` prop (`'vertical' | 'horizontal'`) controls option arrangement and is clearly documented.

## Functional Core & Interaction Dynamics (2025 Harmonization)
- All existing props are sufficient. The `options` prop supports `id` (optional, auto-generated if not provided).
- The `error` prop triggers visual error state on the group label/fieldset and displays an error message.
- `groupLabel` is required and implemented as a `<legend>` within a `<fieldset>` for accessibility.

## Usage Protocols & Accessibility (2025 Harmonization)
- Use `<fieldset>` and `<legend>` for grouping; each radio button has a `<label>`.
- Keyboard navigation: Tab to enter group, Arrow keys to move/select within group.
- All radio buttons share the same `name` attribute.
- Use `aria-checked` for the selected option.
- Error messages are programmatically linked and announced.

## Ethical Alignment & PET (2025 Harmonization)
- **Clarity of Options:** Each option label must be unambiguous.
- **Meaningful Default:** If a default is provided, it must be user-centric and transparent. If no default, require an active choice and use the `error` prop if needed.
- **Transparency of Consequence:** HelperText or context should explain the implications of the selection if significant.

## Symbolic Resonance & Ritual Integration
- Making a selection in a RadioGroup is a "Definitive Stance" or "Alignment with a Singular Path." Used for choices where mutual exclusivity is symbolically important (e.g., choosing a primary Epistemic Mode, a singular response to a dilemma).

## Implementation Echoes (Examples)
```jsx
const epistemicModeOptions = [
  { value: 'analytical', label: 'Analytical (Reason & Logic)' },
  { value: 'intuitive', label: 'Intuitive (Insight & Pattern)' },
  { value: 'mythic', label: 'Mythic (Symbol & Story)' },
];

const [selectedMode, setSelectedMode] = useState('');
const [error, setError] = useState('');

const handleSubmit = () => {
  if (!selectedMode) setError('Please select an epistemic mode.');
  else setError('');
};

<RadioGroup
  groupLabel="Choose Your Primary Epistemic Mode"
  name="epistemicMode"
  options={epistemicModeOptions}
  selectedValue={selectedMode}
  onChange={setSelectedMode}
  error={error}
  helperText="This choice will influence your Resonance Fingerprint."
  layout="vertical"
/>
```

## 📝 Changelog
- 2025-06-09 :: v1.1.1 :: FINALIZED – Metadata update (status, version, last pulse, stewards, alignment signals, resonates_with), deepen symbolic/ritual framing (Definitive Stance), confirm Error Red for error/invalid, PET/Clarity, accessibility, and add changelog entry. Ensure references to symbolic_myth_index.md and ritual_as_interface_re_enchanting_digital_interaction.md are present.
- 2025-06-08 :: v1.1.0 :: HARMONIZED – Expanded PET/Clarity, error visuals, accessibility, and symbolic/ritual guidance for Portal Realm and exclusive choice use cases.
- **2025-06-07 :: v1.0.1 :: UPDATE** – Standardized error state visuals to use Error Red (#FF4136).
- 2025-06-07 :: v1.0.0 :: GENESIS – Initial harmonized documentation. Aligned with canonical template, PET/Clarity protocols, and visual/symbolic requirements for single-choice selection from a group.

<div align="center">
<img src="../assets/thinkalike_logo.svg" alt="ThinkAlike Logo Placeholder" width="40" height="40" />
<br/>
<em>ThinkAlike — Harmonizing Human & Machine</em>
</div>
