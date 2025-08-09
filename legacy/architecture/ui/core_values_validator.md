---
title: CoreValuesValidator Component
document_status: Harmonized - Draft
version: 0.1.0
last_updated: 2025-06-09
maintained_by: UI Systems Guild | ClarityAgent∴
alignment_tags: [UI, DataDisplay, Validation, CoreValues, PET, Clarity, Symbolic, Minimalist, accessibility_AAA]
related_components: [Alert, DataValidationError, DataTable, Badge, ProfileCard]
visual_style_guide_ref: [../style/canonical_visual_style_guide.md]
---

<!-- ∴ THINKALIKE COMPONENT MANIFEST ∴ -->
<!-- UID: /docs/ui_components/core_values_validator.md -->

<br/>

<p align="center">
  <span style="font-size: 3em; color: #00BFFF;">🛡️</span>
</p>

<h1 align="center" style="font-family: 'Montserrat', Arial, sans-serif; font-weight: 700; color: #00BFFF; letter-spacing: 0.05em; border-bottom: 1px solid #666666; padding-bottom: 0.2em;">
  CoreValuesValidator
</h1>

<p align="center" style="font-family: 'Open Sans', Arial, sans-serif; font-size: 1.1em; color: #CCCCCC; margin-bottom: 2em;">
  Visualizes and validates alignment with ThinkAlike’s core values, surfacing ethical resonance and actionable feedback.
</p>

---
<!-- METADATA LAYER -->
<div style="font-family: 'Courier New', monospace; font-size: 0.9em; color: #666666; margin-bottom: 2em; padding: 1em; border: 1px dashed #333333; background-color: #1a1a1a;">
  <p><strong>STATUS</strong> ::: Harmonized – Finalized</p>
  <p><strong>VERSION</strong> ::: 1.1.1</p>
  <p><strong>LAST PULSE</strong> ::: 2025-06-09</p>
  <p><strong>STEWARD(S)</strong> ::: UI Systems Guild | ClarityAgent∴</p>
  <p><strong>ALIGNMENT SIGNALS</strong> ::: <code>[core_values]</code> <code>[validation]</code> <code>[pet_compliant]</code> <code>[clarity_protocol]</code> <code>[symbolic_affordance]</code> <code>[accessibility_AAA]</code> <code>[ritual_marker]</code> <code>[error_red]</code></p>
  <p><strong>RESONATES WITH</strong> ::: <code>[../style/canonical_visual_style_guide.md]</code> <code>[Alert.md]</code> <code>[DataValidationError.md]</code> <code>[ProfileCard.md]</code> <code>[../narrative_engine/canon/symbolic_myth_index.md]</code> <code>[../noetica/corpus_magnus/art_aesthetics_and_culture/ritual_as_interface_re_enchanting_digital_interaction.md]</code></p>
</div>

---

# CoreValuesValidator

> **Purpose:**
> The CoreValuesValidator component visually and interactively communicates the degree of alignment between user actions, data, or proposals and ThinkAlike’s core values. It provides transparent, actionable feedback, surfacing both resonance and misalignment, and supports ethical, PET-compliant decision-making. The component is a ritual marker of ethical alignment, making value resonance visible and actionable. See also: [../noetica/corpus_magnus/art_aesthetics_and_culture/ritual_as_interface_re_enchanting_digital_interaction.md].

**Symbolic Role:**
- CoreValuesValidator is a ritual marker of ethical alignment—surfacing resonance, misalignment, and the path to restoration. Its glyphs, color, and feedback reinforce the mythic and ritual language of ThinkAlike (see [../narrative_engine/canon/symbolic_myth_index.md]).
- The use of **Error Red (#FF4136)** for all misalignment/error visuals is a ritual standard, never to be substituted.

**Last Updated:** June 9, 2025
**Version:** 1.1.1 (Harmonized for Alchemical Interface Initiative, symbolic/ritual framing, and PET/Clarity)
**Related Components:** `Alert`, `DataValidationError`, `DataTable`, `Badge`, `ProfileCard`
**Core Principles Embodied:** Clarity, Accessibility, PET/Clarity, Symbolic Resonance, Ritual Presence

---

## Visual & Symbolic Guidelines
- **Style:** Minimalist, high-contrast, dark theme. Uses ThinkAlike’s canonical shield glyph (🛡️ Shield of Themis) for all states, with overlays:
  - **Aligned:** Blue/green highlights, shield + animated resonance waves/aura (positive, harmonious).
  - **Partial/Uncertain:** Amber/yellow highlights, shield + wavy/tilde lines or questioning glyph (❔), constructive suggestions.
  - **Misaligned/Error:** **Error Red (#FF4136)** for border, icon, and message. Shield + cross (❌) or exclamation mark (❗) overlay. All error/misalignment states use Error Red per the canonical visual style guide.
- **Layout:** Can be inline (e.g., next to a field) or as a summary panel. May include a list of validated values, icons, and feedback messages.
- **Legend/Help Overlay:** Accessible legend explaining all icons, color codes, and value definitions. Example:
  - 🛡️ (blue/green): Aligned
  - 🛡️❔ (amber): Partial/uncertain
  - 🛡️❌ (Error Red): Misaligned/error
- **Accessibility:** All feedback is accessible via ARIA, color contrast meets WCAG AAA, and icons have descriptive labels. Color is never the sole indicator; icons and text reinforce meaning.

## Usage
```jsx
<CoreValuesValidator
  values={["Transparency", "Consent", "Data Sovereignty"]}
  userInput={userProposal}
  validationResult={result}
  onReviewClick={handleReview}
  inline={false}
/>
```

## Props
| Name              | Type                | Required | Description                                                                 |
|-------------------|---------------------|----------|-----------------------------------------------------------------------------|
| `values`          | `string[]`          | Yes      | List of core values being validated.                                        |
| `userInput`       | `any`               | Yes      | Data or action to validate (e.g., proposal, profile, etc.). Intentionally generic to support multiple data types. |
| `validationResult`| `ValidationResult`  | Yes      | Result object with alignment status, messages, and details. See interface below. |
| `onReviewClick`   | `() => void`        | No       | Handler for user-initiated review or details (e.g., open modal, link to PET guide, or DataTraceability node).     |
| `inline`          | `boolean`           | No       | If true, renders inline; otherwise as a panel.                              |

**ValidationResult interface:**
```ts
interface ValidationDetail {
  value: string; // The core value being validated
  isAligned: boolean;
  reason?: string; // Explanation for misalignment
  suggestion?: string; // For partial alignment
  evidenceLink?: string; // Link to DataTraceability node, PET doc, or userInput excerpt
}
interface ValidationResult {
  overallStatus: 'aligned' | 'partial' | 'misaligned';
  summaryMessage?: string;
  details?: ValidationDetail[];
}
```

## PET/Clarity & Symbolic Protocols
- **Transparency:** Validation rules and value definitions are sourced from canonical documents (e.g., `docs/ethics/core_ethics.md`). The component may provide direct links for user review. Clearly communicates which values are aligned/misaligned and why. Offers links to value definitions and PET/Clarity resources.
- **Constructive Feedback:** Feedback for misalignment is constructive, guiding towards learning and alignment, not punitive. Suggestions and evidence links help users understand and improve.
- **UserValueProfile Integration:** Validation results may be persisted to or reflect the user’s UserValueProfile, surfacing ongoing alignment trends and supporting narrative transparency (with consent).
- **Symbolic:** Uses glyphs, color, and language to reinforce the ritual of ethical alignment. May include ritual affordances (e.g., "Affirm Alignment" button, resonance animation).

## Accessibility
- All feedback is accessible via ARIA roles and labels.
- Color is never the sole indicator; icons and text reinforce meaning.
- All states (aligned, partial, misaligned) meet WCAG AAA contrast.
- Interactive elements (e.g., review button) are keyboard accessible.
- Each alignment state is announced with explicit text (e.g., “Aligned: Transparency”, “Misaligned: Consent – Reason…”). Feedback updates use `aria-live` regions for dynamic announcements.
- If used as a summary panel, use `role="region"` or `role="alert"` for critical misalignment. Inline usage should use `aria-describedby` for field-level feedback.
- Legend/help overlay is accessible and labeled.

## Implementation Echoes (Examples)
```jsx
// Example 1: Aligned
<CoreValuesValidator
  values={["Transparency", "Consent"]}
  userInput={proposal}
  validationResult={{
    overallStatus: "aligned",
    summaryMessage: "Your proposal aligns with all core values.",
    details: [
      { value: "Transparency", isAligned: true },
      { value: "Consent", isAligned: true }
    ]
  }}
/>

// Example 2: Partial
<CoreValuesValidator
  values={["Transparency", "Consent"]}
  userInput={proposal}
  validationResult={{
    overallStatus: "partial",
    summaryMessage: "Some values need attention.",
    details: [
      { value: "Transparency", isAligned: true },
      { value: "Consent", isAligned: false, reason: "Consent mechanism unclear.", suggestion: "Add explicit consent step.", evidenceLink: "/docs/ui_components/data_traceability.md#consent1" }
    ]
  }}
/>

// Example 3: Misaligned
<CoreValuesValidator
  values={["Transparency", "Consent"]}
  userInput={proposal}
  validationResult={{
    overallStatus: "misaligned",
    summaryMessage: "Proposal misaligned with core values.",
    details: [
      { value: "Transparency", isAligned: false, reason: "Data usage not disclosed.", suggestion: "Clarify data flow.", evidenceLink: "/docs/ethics/core_ethics.md#transparency" },
      { value: "Consent", isAligned: false, reason: "No consent step.", suggestion: "Add user consent checkbox.", evidenceLink: "/docs/ui_components/data_traceability.md#consent1" }
    ]
  }}
  onReviewClick={() => openPETGuide()}
/>
```

## Migration Notes
- Replace legacy value validation banners or alerts with CoreValuesValidator.
- Ensure all value alignment feedback uses Error Red for misalignment/error states.
- Link to PET/Clarity documentation for further learning.
- Integrate with DataTraceability and UserValueProfile for richer feedback and transparency.

## Changelog
- 2025-06-09 :: v1.1.1 :: COMPREHENSIVE HARMONIZATION – Aligned with Alchemical Interface Initiative, PET/Clarity, symbolic/ritual standards, Error Red error states, and WCAG AAA accessibility targets. Ensured full support for restored Portal & Resonance Network flows.
- 2025-06-09 :: v1.0.0 :: HARMONIZED – Expanded symbolic glyph guidance, accessibility, constructive feedback, and PET/Clarity integration. Added evidenceLink, richer examples, and legend. Error Red and value transparency reaffirmed.
- 2025-06-07 :: v0.1.0 :: DRAFT – Initial harmonized documentation, Error Red standard, dual-metadata, PET/Clarity, symbolic, and accessibility alignment.

<div align="center">
<img src="../assets/thinkalike_logo.svg" alt="ThinkAlike Logo Placeholder" width="40" height="40" />
<br/>
<em>ThinkAlike — Harmonizing Human & Machine</em>
</div>
