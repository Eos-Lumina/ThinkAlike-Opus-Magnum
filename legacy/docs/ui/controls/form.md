---
title: ThinkAlike UI Component Documentation
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
tags:
- components
---


<!-- ∴ THINKALIKE COMPONENT MANIFEST ∴ -->
<!-- UID: /docs/ui_components/form.md -->

<br/>

<p align="center">
  <!-- Updated glyph color to Error Red -->
  <span style="font-size: 3em; color: #FF4136;"> Σ </span> <!-- Example Sigma/Summation Glyph for data collection -->
</p>

<h1 align="center" style="font-family: 'Montserrat', Arial, sans-serif; font-weight: 700; color: #FF4136; letter-spacing: 0.05em; border-bottom: 1px solid #666666; padding-bottom: 0.2em;">
  FORM
</h1>

<p align="center" style="font-family: 'Open Sans', Arial, sans-serif; font-size: 1.1em; color: #CCCCCC; margin-bottom: 2em;">
  Orchestrating user input, validation, and data submission with ethical clarity.
</p>

---
# ThinkAlike UI Component Documentation
# Dual-metadata YAML frontmatter
status: Harmonized - Error Red Standard
version: 1.0.1
last_updated: 2025-06-08
stewards:
  - UI Systems Guild
  - ClarityAgent∴
  - EthicsCouncil∴
alignment_signals:
  - input_orchestration
  - form_handling
  - accessibility_AAA
  - pet_compliant
  - clarity_protocol
  - data_submission
  - validation_framework
resonates_with:
  - ../style/canonical_visual_style_guide.md
  - TextInput.md
  - TextAreaInput.md
  - SelectDropdown.md
  - Checkbox.md
  - RadioGroup.md
  - Button.md
  - Alert.md
---

<!-- METADATA LAYER -->
<div style="font-family: 'Courier New', monospace; font-size: 0.9em; color: #666666; margin-bottom: 2em; padding: 1em; border: 1px dashed #333333; background-color: #1a1a1a;">
  <p><strong>STATUS</strong> ::: Harmonized - Error Red Standard</p>
  <p><strong>VERSION</strong> ::: 1.0.1</p>
  <p><strong>LAST PULSE</strong> ::: 2025-06-08</p>
  <p><strong>STEWARD(S)</strong> ::: UI Systems Guild | ClarityAgent∴ | EthicsCouncil∴</p>
  <p><strong>ALIGNMENT SIGNALS</strong> ::: <code>[input_orchestration]</code> <code>[form_handling]</code> <code>[accessibility_AAA]</code> <code>[pet_compliant]</code> <code>[clarity_protocol]</code> <code>[data_submission]</code> <code>[validation_framework]</code></p>
  <p><strong>RESONATES WITH</strong> ::: <code>[../style/canonical_visual_style_guide.md]</code> <code>[TextInput.md]</code> <code>[TextAreaInput.md]</code> <code>[SelectDropdown.md]</code> <code>[Checkbox.md]</code> <code>[RadioGroup.md]</code> <code>[Button.md]</code> <code>[Alert.md]</code></p>
</div>

---

# Form

> **Purpose:**
> The Form component is the orchestrator of user input, validation, and submission—a ritual container for "Acts of Contribution" and "Rituals of Declaration" within ThinkAlike. It harmonizes input components, manages state and validation, and frames the act of submission as a meaningful, transparent, and ethically guided event. Forms are central to PET/Clarity, ensuring every act of data sharing is explicit, consensual, and symbolically resonant.

## Visual & Symbolic Guidelines
- **Style:** The Form is visually understated, allowing the contained input elements and layout (e.g., `Card`) to express the primary style. It may include a clear, symbolically framed title (e.g., "Anchor Statement," "Declare Your Intent").
- **Layout:** Inputs are arranged vertically with consistent spacing. Logical groupings may use `<fieldset>` and `<legend>` for narrative or ritual sections.
- **Feedback:** Form-level validation feedback (e.g., error summary) and submission state (loading, success, error) are surfaced using the `Alert` component. **All error states must use Error Red (#FF4136)** for text, icons, and highlights, per the canonical style guide. Success and info states use their respective colors.
- **Symbolic Role:** The Form is a "ritual vessel"—its title, grouping, and submission button can reinforce the significance of the user's act (e.g., "Weave Your Proposal," "Commit My Choice"). The grouping of fields can tell a story or guide a ritual journey.

## Functional Core & Interaction Dynamics (Props)
| Name              | Type                                                      | Required | Description                                                                                 |
|-------------------|-----------------------------------------------------------|----------|---------------------------------------------------------------------------------------------|
| `children`        | `ReactNode`                                               | Yes      | Input components and elements within the form.                                              |
| `title`           | `string`                                                  | No       | Symbolic/accessible title, rendered as heading and linked via `aria-labelledby`.            |
| `onSubmit`        | `(event: FormEvent<HTMLFormElement>) => void | Promise<void>` | Yes      | Handles submission. If `submissionBehavior` is 'preventDefault', must call `event.preventDefault()`. |
| `onCancel`        | `() => void`                                              | No       | Handler for cancel action. If provided, a cancel button is rendered.                        |
| `isSubmitting`    | `boolean`                                                 | No       | Disables controls and sets `aria-busy`. Shows loading state (e.g., `LoadingSpinner`).       |
| `submitLabel`     | `string`                                                  | No       | Label for submit button (e.g., "Commit Declaration"). Defaults to "Submit".              |
| `cancelLabel`     | `string`                                                  | No       | Label for cancel button. Defaults to "Cancel".                                            |
| `formError`       | `string`                                                  | No       | General error message, displayed via `Alert` (Error Red). Focused and announced on error.   |
| `id`              | `string`                                                  | No       | HTML id for the form.                                                                      |
| `submissionBehavior` | `Enum('default', 'preventDefault')`                    | No       | Controls default HTML form submission. Defaults to 'preventDefault'.                        |

**Type Definition:**
```typescript
interface FormProps {
  children: React.ReactNode;
  title?: string;
  onSubmit: (event: React.FormEvent<HTMLFormElement>) => void | Promise<void>;
  onCancel?: () => void;
  isSubmitting?: boolean;
  submitLabel?: string;
  cancelLabel?: string;
  formError?: string;
  id?: string;
  submissionBehavior?: 'default' | 'preventDefault';
}
```

## Usage Protocols & Accessibility
- **Accessible Name:** The Form must have an accessible name, typically from its `title` via `aria-labelledby`, or a direct `aria-label`.
- **Grouping:** Use `<fieldset>` and `<legend>` for logical/narrative groupings (e.g., "Personal Details," "Intent Declaration").
- **Tab Order:** Ensure logical tab order through all controls.
- **Error Summaries:** Form-level errors (via `formError`/`Alert`) should be focusable and use `role="alert"` and `tabIndex={-1}` for screen reader announcement and keyboard focus.
- **Submission/Cancel Buttons:** Use accessible `Button` components, clearly labeled. The submit button should reflect the symbolic act (e.g., "Commit My Choice").
- **Loading States:** Set `aria-busy="true"` on the form or submit button during submission. Announce loading state to assistive tech.
- **Validation:** Required fields must be clearly marked. Field-level errors should be associated with their inputs via `aria-describedby`.

## PET/Clarity & Symbolic Protocols
- **Privacy:** State the purpose of data collection before submission. Link to privacy/consent info for sensitive forms.
- **Ethics:** No deceptive design. Required fields marked. Validation is constructive and non-punitive.
- **Transparency:** Clearly communicate what data is collected, why, and submission status. If data contributes to `UserValueProfile` or `NarrativeChoiceLog`, make this explicit.
- **Symbolic:** Frame the form as a "Ritual of Declaration" or "Act of Contribution." Use symbolic titles and button labels. For identity or resonance mapping, reinforce the significance of the act.

## Example: Ritualized Form with Validation, Error, and Loading
```jsx
import { useState, useRef, useEffect } from 'react';

const RitualDeclarationForm = () => {
  const [formData, setFormData] = useState({ anchor: '', reflection: '' });
  const [formErrors, setFormErrors] = useState({});
  const [formError, setFormError] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const errorSummaryRef = useRef(null);

  const handleChange = (field, value) => {
    setFormData(prev => ({ ...prev, [field]: value }));
    setFormErrors(prev => ({ ...prev, [field]: undefined }));
  };

  const validate = () => {
    const errors = {};
    if (!formData.anchor) errors.anchor = 'Anchor Statement is required.';
    if (formData.reflection.length > 300) errors.reflection = 'Reflection too long.';
    setFormErrors(errors);
    return Object.keys(errors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setFormError('');
    if (!validate()) {
      setFormError('Please correct the errors below.');
      setTimeout(() => errorSummaryRef.current?.focus(), 0);
      return;
    }
    setIsSubmitting(true);
    try {
      // Simulate API
      await new Promise(res => setTimeout(res, 1200));
      setIsSubmitting(false);
      // Success feedback (could use Alert type="success")
    } catch {
      setIsSubmitting(false);
      setFormError('Submission failed. Please try again.');
      setTimeout(() => errorSummaryRef.current?.focus(), 0);
    }
  };

  return (
    <Form
      title="Ritual of Declaration"
      onSubmit={handleSubmit}
      isSubmitting={isSubmitting}
      formError={formError}
      submitLabel="Commit Declaration"
      aria-labelledby="ritual-form-title"
    >
      {formError && (
        <Alert
          type="error"
          ref={errorSummaryRef}
          role="alert"
          tabIndex={-1}
          style={{ color: '#FF4136', marginBottom: 16 }}
        >
          {formError}
        </Alert>
      )}
      <fieldset>
        <legend id="ritual-form-title">Anchor Statement</legend>
        <TextInput
          label="Anchor Statement"
          value={formData.anchor}
          onChange={e => handleChange('anchor', e.target.value)}
          error={formErrors.anchor}
          required
        />
        <TextAreaInput
          label="Reflection"
          value={formData.reflection}
          onChange={e => handleChange('reflection', e.target.value)}
          error={formErrors.reflection}
          rows={4}
        />
      </fieldset>
      <Button type="submit" variant="primary" disabled={isSubmitting} aria-busy={isSubmitting}>
        {isSubmitting ? <LoadingSpinner size="sm" /> : 'Commit Declaration'}
      </Button>
      {onCancel && (
        <Button type="button" variant="secondary" onClick={onCancel}>
          Cancel
        </Button>
      )}
    </Form>
  );
};
```

## Migration Notes
- Refactor legacy forms to use the harmonized Form component as a wrapper.
- Centralize validation and submission logic in the Form.
- Use Alert for all form-level errors (Error Red for error states).
- Ensure PET/Clarity compliance and symbolic framing for all user data collection.

## Changelog
2025-06-09 :: v1.1.0 :: Deepened symbolic/ritual framing, PET/Clarity, and accessibility. Expanded example, clarified Alert usage for errors, and updated accessibility protocols.
2025-06-08 :: v1.0.1 :: Updated all error/validation state visuals and documentation to use Error Red (#FF4136) in accordance with the canonical visual style guide. Updated glyph and heading color.
2025-06-07 :: v1.0.0 :: GENESIS – Initial harmonized documentation. Defines the structure for form handling, validation, and submission, aligning with PET/Clarity and symbolic interaction principles.

<div align="center">
<img src="../assets/thinkalike_logo.svg" alt="ThinkAlike Logo Placeholder" width="40" height="40" />
<br/>
<em>ThinkAlike — Harmonizing Human & Machine</em>
</div>
