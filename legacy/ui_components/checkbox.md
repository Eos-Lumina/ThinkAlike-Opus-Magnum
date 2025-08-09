---
title: Checkbox
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

<!-- ∴ THINKALIKE COMPONENT MANIFEST ∴ -->
<!-- UID: /docs/ui_components/checkbox.md -->

<br/>

<p align="center">
  <!-- Placeholder for a prominent Component Glyph or ThinkAlike Sigil -->
  <span style="font-size: 3em; color: #FF8C00;"> ✅ </span> <!-- Example Checkmark Glyph -->
</p>

<h1 align="center" style="font-family: 'Montserrat', Arial, sans-serif; font-weight: 700; color: #FF8C00; letter-spacing: 0.05em; border-bottom: 1px solid #666666; padding-bottom: 0.2em;">
  CHECKBOX
</h1>

<p align="center" style="font-family: 'Open Sans', Arial, sans-serif; font-size: 1.1em; color: #CCCCCC; margin-bottom: 2em;">
  A binary choice element for selecting or deselecting an option.
</p>

---
<!-- METADATA LAYER -->
<div style="font-family: 'Courier New', monospace; font-size: 0.9em; color: #666666; margin-bottom: 2em; padding: 1em; border: 1px dashed #333333; background-color: #1a1a1a;">
  <p><strong>STATUS</strong> ::: Harmonized – Finalized</p>
  <p><strong>VERSION</strong> ::: 1.1.1</p>
  <p><strong>LAST PULSE</strong> ::: 2025-06-09</p>
  <p><strong>STEWARD(S)</strong> ::: UI Systems Guild | ClarityAgent∴</p>
  <p><strong>ALIGNMENT SIGNALS</strong> ::: <code>[input]</code> <code>[form_element]</code> <code>[accessibility_AAA]</code> <code>[pet_compliant]</code> <code>[clarity_protocol]</code> <code>[boolean_input]</code> <code>[ritual_affirmation]</code> <code>[error_red]</code></p>
  <p><strong>RESONATES WITH</strong> ::: <code>[../style/canonical_visual_style_guide.md]</code> <code>[Form.md]</code> <code>[RadioGroup.md]</code> <code>[../narrative_engine/canon/symbolic_myth_index.md]</code> <code>[../noetica/corpus_magnus/art_aesthetics_and_culture/ritual_as_interface_re_enchanting_digital_interaction.md]</code></p>
</div>

---

# Checkbox

# 🪶 OVERVIEW & PURPOSE (2025 Harmonization)

> **Purpose:**
> The Checkbox component enables users to make a clear, binary choice (on/off, select/deselect), essential for consent, preference toggles, and affirmations throughout ThinkAlike. It is especially critical for PET/Clarity-compliant consent actions in the Portal Realm and must always default to unchecked (opt-in) for privacy or non-essential features. See also: [../noetica/corpus_magnus/art_aesthetics_and_culture/ritual_as_interface_re_enchanting_digital_interaction.md].

**Symbolic Role:**
- The Checkbox is a ritual "Affirmation" or "Pledge"—a symbolic act of consent, alignment, or value declaration. Its color, iconography, and feedback reinforce the mythic and ritual language of ThinkAlike (see [../narrative_engine/canon/symbolic_myth_index.md]).
- The use of **Error Red (#FF4136)** for all error/invalid visuals is a ritual standard, never to be substituted.

**Last Updated:** June 9, 2025
**Version:** 1.1.1 (Harmonized for Alchemical Interface Initiative, symbolic/ritual framing, and PET/Clarity)
**Related Components:** `Form`, `RadioGroup`
**Core Principles Embodied:** Clarity, Accessibility, PET/Clarity, Symbolic Resonance, Ritual Presence

## Visual & Symbolic Guidelines (2025 Harmonization)
- **Error State Color:** All error/invalid states (border, icon, text) use **Error Red (#FF4136)**, never Neon Orange. This is required for all error visuals and meets/exceeds WCAG AAA contrast.
- **Checked State:** Checked background uses "Amber/Honey Yellow" (#FFC300) or "Deep Mandarine Orange" (#F86B03); checkmark glyph is high-contrast (white or black as appropriate).
- **Focus Indicator:** Outline uses "Electric Blue (Accent)" (#00FFFF), always visible on keyboard focus.
- **Shape:** Square box with slightly rounded corners (radius: 3-4px).
- **Error Visuals:** If `error` is true or a string, the box border and/or label are highlighted in Error Red, and an error message is shown/announced via `aria-describedby`.

## Functional Core & Interaction Dynamics (2025 Harmonization)
- All existing props are sufficient. The `error` prop triggers visual error state on the box and label.
- The `label` is always interactive and toggles the checkbox.

## Usage Protocols & Accessibility (2025 Harmonization)
- Label is mandatory and toggles the checkbox.
- Fully keyboard accessible (Spacebar toggles).
- Uses `aria-checked` and, if disabled, `aria-disabled`.
- Error messages are programmatically linked and announced.

## Ethical Alignment & PET (2025 Harmonization)
- **Opt-In by Default:** For any data sharing, privacy, or non-essential features, checkboxes must default to unchecked. Users must actively opt-in.
- **Clarity of Labels:** Labels must be unambiguous, especially for consent. Avoid double negatives.
- **Transparency of Consequence:** HelperText or context must explain the effect of checking/unchecking, especially for significant choices.

## Symbolic Resonance & Ritual Integration
- Checking a box can be a "Ritual of Affirmation" or "Pledge." Used for critical consent steps (e.g., PET agreement, video consent, Narrative Duet data processing).
- May include a subtle symbolic animation (pulse/glow) on check/uncheck.

## Usage
```jsx
<Checkbox
  label="I agree to the Terms of Resonance"
  checked={agreedToTerms}
  onChange={(isChecked) => setAgreedToTerms(isChecked)}
  id="terms-agreement"
/>

<Checkbox
  label="Enable Advanced Symbolic Overlays"
  checked={advancedOverlaysEnabled}
  onChange={(isChecked) => setAdvancedOverlaysEnabled(isChecked)}
  disabled={!userHasProAccess}
/>
```

## Props
| Name        | Type                        | Required | Description                                                        |
|-------------|-----------------------------|----------|--------------------------------------------------------------------|
| `label`     | `string \| ReactNode`       | Yes      | Visible label for the checkbox. Clicking the label toggles the checkbox. |
| `checked`   | `boolean`                   | Yes      | Current checked state of the checkbox.                             |
| `onChange`  | `(isChecked: boolean) => void` | Yes   | Handler called when the checkbox state changes.                    |
| `id`        | `string`                    | No       | HTML id attribute. If not provided, one will be generated for label association. |
| `name`      | `string`                    | No       | HTML name attribute, useful in forms.                              |
| `disabled`  | `boolean`                   | No       | Disables the checkbox.                                             |
| `required`  | `boolean`                   | No       | Marks the checkbox as required (e.g., for terms agreement).        |
| `error`     | `string \| boolean`         | No       | Indicates an error state (e.g., if a required checkbox is not checked). |
| `helperText`| `string`                    | No       | Additional instructional text displayed near the checkbox.         |

## PET/Clarity & Symbolic Protocols
- **Privacy:**
    - Checkbox selections related to data sharing or privacy preferences must be explicitly opt-in (unchecked by default unless a strong user-centric reason dictates otherwise, transparently communicated).
- **Ethics:**
    - Labels must be unambiguous. Avoid double negatives or confusing phrasing that could lead to unintended selections.
    - Default states should prioritize user privacy and agency.
- **Transparency:**
    - The visual difference between checked and unchecked states must be stark and immediately clear.
    - If a checkbox selection has significant consequences or enables/disables major functionality, this should be communicated via helperText or surrounding context.
- **Symbolic:**
    - A checkbox selection can represent a "Pledge" or "Affirmation" within a ritualistic context (e.g., during onboarding or when joining a Hive).
    - The checkmark glyph itself can be styled to align with ThinkAlike's symbolic aesthetic (e.g., a subtle pulse animation on check, using symbolic colors for the checked state).
    - Can be used to signify consent for specific "Symbolic Alignments" or data to be used in "Resonance Mapping."

## Accessibility
- The label is mandatory and interactively tied to the checkbox state. Clicking the label should toggle the checkbox.
- The checkbox input itself should be focusable and operable via keyboard (Spacebar to toggle).
- Use aria-checked attribute to reflect the state.
- If part of a group, use fieldset and legend for grouping, or aria-labelledby if grouping is done by a visible heading.
- Error states (error prop) should be programmatically linked and announced.
- Disabled state must be clearly indicated visually and programmatically (aria-disabled="true").
- Ensure sufficient contrast for the checkbox, checkmark, label, and focus indicator.

## Example
```jsx
const [receiveNotifications, setReceiveNotifications] = useState(true);

return (
  <FormElement> {/* Assuming a FormElement wrapper */}
    <Checkbox
      label="Receive email notifications for new Resonance Matches"
      id="email-notifications"
      checked={receiveNotifications}
      onChange={setReceiveNotifications}
      helperText="You can manage notification preferences in your settings at any time."
    />
  </FormElement>
);
```

## Migration Notes
- Legacy checkbox components must be updated to ensure a visible, interactive label is always present.
- Standardize checked and onChange props.
- Ensure visual styles for checked, unchecked, focus, and disabled states align with canonical_visual_style_guide.md.
- Verify full keyboard accessibility and ARIA attribute usage.

## 📝 Changelog
- 2025-06-09 :: v1.1.1 :: FINALIZED – Metadata update (status, version, last pulse, stewards, alignment signals, resonates_with), deepen symbolic/ritual framing (Affirmation/Pledge), confirm Error Red for error/invalid, PET/Clarity, accessibility, and add changelog entry. Ensure references to symbolic_myth_index.md and ritual_as_interface_re_enchanting_digital_interaction.md are present.
- 2025-06-08 :: v1.1.0 :: HARMONIZED – Expanded PET/Clarity, opt-in by default, error visuals, accessibility, and symbolic/ritual guidance for Portal Realm and consent use cases.
- **2025-06-07 :: v1.0.1 :: UPDATE** – Standardized error state visuals to use Error Red (#FF4136).
- 2025-06-07 :: v1.0.0 :: GENESIS – Initial harmonized documentation. Aligned with canonical template, PET/Clarity protocols, and visual/symbolic requirements for binary choice inputs.

<div align="center">
<img src="../assets/thinkalike_logo.svg" alt="ThinkAlike Logo Placeholder" width="40" height="40" />
<br/>
<em>ThinkAlike — Harmonizing Human & Machine</em>
</div>
