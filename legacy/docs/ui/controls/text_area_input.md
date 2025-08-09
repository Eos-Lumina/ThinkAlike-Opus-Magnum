---
title: TextAreaInput Component
document_status: Harmonized – Finalized
version: 1.1.1
last_updated: 2025-06-09
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
alignment_tags:
- UI
- Input
- Form
- TextArea
- PET
- Clarity
- Symbolic
- Minimalist
- accessibility_AAA
- ritual_expression
- narrative_input
- symbolic_resonance
resonates_with:
- ../narrative_engine/canon/symbolic_myth_index.md
- ../rituals/ritual_as_interface_re_enchanting_digital_interaction.md
- ../realms/portal/portal_specification.md
- ../style/canonical_visual_style_guide.md
- ../seed/symbolic_alignment/symbolic_alignment_manifesto.md
related_components:
- Form
- TextInput
- SelectDropdown
- Checkbox
- RadioGroup
- Button
visual_style_guide_ref:
- ../style/canonical_visual_style_guide.md
tags:
- components
---


<!-- ∴ THINKALIKE COMPONENT MANIFEST ∴ -->
<!-- UID: /docs/ui_components/text_area_input.md -->

<p align="center">
  <span style="font-size: 3em; color: #00BFFF;"> 📝 </span>
</p>

<h1 align="center" style="font-family: 'Montserrat', Arial, sans-serif; font-weight: 700; color: #00BFFF; letter-spacing: 0.05em; border-bottom: 1px solid #666666; padding-bottom: 0.2em;">
  TextAreaInput
</h1>

<p align="center" style="font-family: 'Open Sans', Arial, sans-serif; font-size: 1.1em; color: #CCCCCC; margin-bottom: 2em;">
  Facilitating multi-line text entry for narratives, reflections, and detailed descriptions.
</p>

---
<!-- METADATA LAYER -->
<div style="font-family: 'Courier New', monospace; font-size: 0.9em; color: #666666; margin-bottom: 2em; padding: 1em; border: 1px dashed #333333; background-color: #1a1a1a;">
  <p><strong>STATUS</strong> ::: Harmonized – Finalized</p>
  <p><strong>VERSION</strong> ::: 1.1.1</p>
  <p><strong>LAST PULSE</strong> ::: 2025-06-09</p>
  <p><strong>STEWARD(S)</strong> ::: UI Systems Guild | ClarityAgent∴</p>
  <p><strong>ALIGNMENT SIGNALS</strong> ::: <code>[input]</code> <code>[form_element]</code> <code>[accessibility_AAA]</code> <code>[pet_compliant]</code> <code>[clarity_protocol]</code> <code>[multi_line_text]</code> <code>[narrative_input]</code> <code>[ritual_expression]</code> <code>[symbolic_resonance]</code></p>
  <p><strong>RESONATES WITH</strong> ::: <code>[symbolic_myth_index.md]</code> <code>[ritual_as_interface_re_enchanting_digital_interaction.md]</code> <code>[portal_specification.md]</code> <code>[canonical_visual_style_guide.md]</code> <code>[symbolic_alignment_manifesto.md]</code></p>
  <p><strong>RELATED COMPONENTS</strong> ::: <code>[Form]</code> <code>[TextInput]</code> <code>[SelectDropdown]</code> <code>[Checkbox]</code> <code>[RadioGroup]</code> <code>[Button]</code></p>
  <p><strong>VISUAL STYLE GUIDE REF</strong> ::: <code>[../style/canonical_visual_style_guide.md]</code></p>
</div>

---

# 🪶 OVERVIEW & PURPOSE (2025 Harmonization)

> **Purpose:**
> The TextAreaInput component is a vessel for the "Ritual of Expression"—a symbolic act of narrative weaving and value articulation. It is essential for capturing longer-form content such as personal stories, reflections, proposals, or descriptive fields, directly contributing to the user's "Resonance Fingerprint" and the collective mythos (see [symbolic_myth_index.md]). It upholds PET/Clarity, accessibility, and ritual intent (see [ritual_as_interface_re_enchanting_digital_interaction.md]).

# 👁️‍🗨️ VISUAL RESONANCE & STATES (2025 Harmonization)
- **Error State Color:** All error/invalid states (border, icon, text) use **Error Red (#FF4136)**, never Neon Orange. This is required for all error visuals and meets/exceeds WCAG AAA contrast.
- **Focus State:** 2px glowing border in "Amber/Honey Yellow" (#FFC300) or "Electric Blue" (#00FFFF), clearly defined and always visible on keyboard focus.
- **Symbolic Feel:** Minimalist, non-distracting styling supports the "Ritual over Interface" principle—allowing the user's intention and narrative to be the focus.
- **Glyphic Integration:** Optionally, a glyph from [symbolic_myth_index.md] may be shown as a prefix/suffix to reinforce the ritual context.

# ⚙️ FUNCTIONAL CORE & INTERACTION DYNAMICS (2025 Harmonization)
- All existing props are sufficient for capturing profound user input in the Portal. No changes needed.
- **Label is mandatory** and must be visibly associated (see Accessibility).
- **HelperText** and **Error** must be programmatically linked using `aria-describedby`.
- **aria-invalid="true"** is required for error states.

# 🧭 USAGE PROTOCOLS & ACCESSIBILITY (2025 Harmonization)
- Meets/exceeds WCAG AAA for color contrast, focus indicators, and keyboard navigation.
- All interactive states (focus, error, disabled) are visually and programmatically distinct.
- Ritual accessibility: The act of input is framed as a meaningful expression, not a mere transaction.

# ⚖️ ETHICAL ALIGNMENT & PET (2025 Harmonization)
- **Purpose of Data:** The `label` or `helperText` (or Eos Lumina's framing) must make the purpose of the input clear (e.g., "Your reflection will help shape your core values profile").
- **Transparency:** If input is logged in `NarrativeChoiceLog` or influences AI, this should be transparent in the UI context.
- **Data Minimization:** Prompts should encourage expressiveness but also conciseness where appropriate.
- **No Dark Patterns:** All input requests are opt-in, non-coercive, and clearly labeled.

# ✨ SYMBOLIC RESONANCE & RITUAL INTEGRATION
- The component is a vessel for "Ritual of Expression" or "Weaving Your Thread in the Collective Narrative." In the Portal, it is the user's tool for narrative articulation and value formation.
- Symbolic overlays, glyphs, and color states should echo the mythic language of ThinkAlike (see [symbolic_myth_index.md]).
- Ritual framing and PET/Clarity are inseparable—clarity is sacred.

# 💻 IMPLEMENTATION ECHOES (Examples)
```jsx
<TextAreaInput
  label="Your Reflection"
  value={reflection}
  onChange={(e) => setReflection(e.target.value)}
  placeholder="Share your thoughts, insights, or narrative fragments here..."
  rows={5}
  maxLength={1000}
/>
```

## Props
| Name           | Type                                      | Required | Description                                                        |
|----------------|-------------------------------------------|----------|--------------------------------------------------------------------|
| `label`        | `string`                                  | Yes      | Visible label for the textarea, crucial for accessibility.         |
| `value`        | `string`                                  | Yes      | Current value of the textarea.                                     |
| `onChange`     | `(event: ChangeEvent<HTMLTextAreaElement>) => void` | Yes | Handler for value changes.                                         |
| `id`           | `string`                                  | No       | HTML id attribute. If not provided, one will be generated.         |
| `name`         | `string`                                  | No       | HTML name attribute.                                               |
| `placeholder`  | `string`                                  | No       | Placeholder text displayed when the textarea is empty.             |
| `disabled`     | `boolean`                                 | No       | Disables the textarea.                                             |
| `required`     | `boolean`                                 | No       | Marks the textarea as required for form submission.                |
| `readOnly`     | `boolean`                                 | No       | Makes the textarea read-only.                                      |
| `error`        | `string \| boolean`                       | No       | Indicates an error state. If string, displays as an error message. |
| `rows`         | `number`                                  | No       | Specifies the visible height of the textarea in lines. Defaults to 3 or 4. |
| `maxLength`    | `number`                                  | No       | Maximum number of characters allowed. May include a visual character counter. |
| `resizable`    | `"vertical" \| "both" \| "none"`         | No       | Controls if/how the textarea can be resized by the user. Defaults to vertical. |
| `helperText`   | `string`                                  | No       | Additional instructional text displayed below the textarea.        |
| `autoComplete` | `string`                                  | No       | HTML autocomplete attribute (less common for textareas, but possible). |

## PET/Clarity & Symbolic Protocols
- **Privacy:**
    - Consider the sensitivity of information typically entered into textareas (reflections, narratives). Ensure no unintended logging or transmission occurs without explicit user consent.
    - If content might be shared, clear consent mechanisms must precede such sharing.
- **Ethics:**
    - Provide users with tools to save drafts if inputting extensive text, preventing data loss.
    - Error messages related to content (e.g., length limits) should be clear and non-punitive.
- **Transparency:**
    - Character count (if maxLength is set) should be visible to the user.
    - Any AI processing of the textarea content (e.g., for summarization, sentiment analysis – if such features exist) must be explicitly declared and consented to, with clear indicators when AI is active (e.g., AIWaveformIndicator).
- **Symbolic:**
    - The TextAreaInput is a primary vessel for users to contribute to the "Narrative as Identity" and "Forkable Identity" principles. It's where personal stories, reflections for Value Profile creation, and community proposals are articulated.
    - The act of writing can be framed as a "Ritual of Expression" or "Weaving Your Thread in the Collective Narrative."
    - In contexts like the NarrativeViewer or RitualForkArchive, the TextAreaInput becomes the tool for recording symbolic choices or reflections.

## Accessibility
- The label prop is mandatory and visibly associated with the textarea.
- Placeholder text is not a substitute for a visible label.
- Error messages (error prop) should be programmatically linked using aria-describedby and announced by screen readers.
- Ensure sufficient contrast for text, placeholder text, and borders. Focus state must be distinct.
- If resizable, ensure the resize handle is accessible via keyboard or that an alternative way to adjust size is provided if needed.
- Character counters should be announced by screen readers.

## Example
```jsx
const [proposalDetails, setProposalDetails] = useState('');
const MAX_CHARS = 2000;

return (
  <FormElement> {/* Assuming a FormElement wrapper for label, input, helper/error text */}
    <TextAreaInput
      label="Detailed Proposal Description"
      id="proposal-description"
      value={proposalDetails}
      onChange={(e) => setProposalDetails(e.target.value)}
      placeholder="Describe your proposal, its goals, and how it aligns with ThinkAlike's values..."
      rows={10}
      maxLength={MAX_CHARS}
      error={proposalDetails.length > MAX_CHARS ? `Description exceeds ${MAX_CHARS} characters.` : ''}
      helperText={`${MAX_CHARS - proposalDetails.length} characters remaining.`}
      required
    />
  </FormElement>
);
```

## Migration Notes
- Legacy multi-line inputs should be migrated to TextAreaInput.
- Standardize props like rows, maxLength, and error handling.
- Ensure visible labels are used consistently.
- Apply styles from canonical_visual_style_guide.md.

# 📝 Changelog
- 2025-06-09 :: v1.1.1 :: FINALIZED – Metadata update (status, version, last pulse, stewards, alignment signals, resonates_with), deepen symbolic/ritual framing (Ritual of Expression), confirm Error Red for error/invalid, PET/Clarity, accessibility, and add changelog entry. Ensure references to symbolic_myth_index.md and ritual_as_interface_re_enchanting_digital_interaction.md are present.
- 2025-06-08 :: v1.1.0 :: HARMONIZED – Expanded guidance for Portal Realm, clarified error state color, PET/Clarity, and symbolic/ritual framing.

<div align="center">
<img src="../assets/thinkalike_logo.svg" alt="ThinkAlike Logo Placeholder" width="40" height="40" />
<br/>
<em>ThinkAlike — Harmonizing Human & Machine</em>
</div>
