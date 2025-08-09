---
title: TextInput Component
document_status: Harmonized – Finalized
version: 1.1.1
last_updated: 2025-06-09
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
alignment_tags:
- input
- form_element
- accessibility_AAA
- pet_compliant
- clarity_protocol
- data_capture
- ritual_declaration
- symbolic_resonance
resonates_with:
- ../narrative_engine/canon/symbolic_myth_index.md
- ../rituals/ritual_as_interface_re_enchanting_digital_interaction.md
- ../realms/portal/portal_specification.md
- ../style/canonical_visual_style_guide.md
- ../seed/symbolic_alignment/symbolic_alignment_manifesto.md
related_components:
- Form
- TextAreaInput
- Alert
visual_style_guide_ref:
- ../style/canonical_visual_style_guide.md
tags:
- components
---


<p align="center">
  <span style="font-size: 3em; color: #FF8C00;">⌨️</span>
</p>

<h1 align="center" style="font-family: 'Montserrat', Arial, sans-serif; font-weight: 700; color: #FF8C00; letter-spacing: 0.05em; border-bottom: 1px solid #666666; padding-bottom: 0.2em;">
  TextInput
</h1>

<!-- METADATA LAYER -->
<div style="font-family: 'Courier New', monospace; font-size: 0.9em; color: #666666; margin-bottom: 2em; padding: 1em; border: 1px dashed #333333; background-color: #1a1a1a;">
  <p><strong>DOCUMENT STATUS</strong> ::: Harmonized – Finalized</p>
  <p><strong>VERSION</strong> ::: 1.1.1</p>
  <p><strong>LAST UPDATED</strong> ::: 2025-06-09</p>
  <p><strong>MAINTAINED BY</strong> ::: UI Systems Guild | ClarityAgent∴</p>
  <p><strong>ALIGNMENT TAGS</strong> ::: <code>[input]</code> <code>[form_element]</code> <code>[accessibility_AAA]</code> <code>[pet_compliant]</code> <code>[clarity_protocol]</code> <code>[data_capture]</code> <code>[ritual_declaration]</code> <code>[symbolic_resonance]</code></p>
  <p><strong>RESONATES WITH</strong> ::: <code>[symbolic_myth_index.md]</code> <code>[ritual_as_interface_re_enchanting_digital_interaction.md]</code> <code>[portal_specification.md]</code> <code>[canonical_visual_style_guide.md]</code> <code>[symbolic_alignment_manifesto.md]</code></p>
  <p><strong>RELATED COMPONENTS</strong> ::: <code>[Form]</code> <code>[TextAreaInput]</code> <code>[Alert]</code></p>
  <p><strong>VISUAL STYLE GUIDE REF</strong> ::: <code>[../style/canonical_visual_style_guide.md]</code></p>
</div>

---

# 🪶 OVERVIEW & PURPOSE (2025 Harmonization)

> **Purpose:**
> The TextInput component is a vessel for the "Ritual of Declaration"—a symbolic act of self-articulation and value formation. It captures user expressions that contribute to their `UserValueProfile` and "Resonance Fingerprint" (see [symbolic_myth_index.md]), especially within the Portal Realm's mythopoetic journeys (e.g., Eos Lumina's initial questions, Anchor Statement, or reflective dilemmas). It is designed to support both ritualized and everyday data entry, always upholding PET/Clarity and symbolic intent (see [ritual_as_interface_re_enchanting_digital_interaction.md]).

# 👁️‍🗨️ VISUAL RESONANCE & STATES (2025 Harmonization)
- **Error State Color:** All error/invalid states (border, icon, text) use **Error Red (#FF4136)**, never Neon Orange. This is required for all error visuals and meets/exceeds WCAG AAA contrast.
- **Focus State:** 2px glowing border in "Amber/Honey Yellow" (#FFC300) or "Electric Blue" (#00FFFF), clearly defined and always visible on keyboard focus.
- **Symbolic Feel:** Minimalist, non-distracting styling supports the "Ritual over Interface" principle—allowing the user's intention and expression to be the focus.
- **Glyphic Integration:** Optionally, a glyph from [symbolic_myth_index.md] may be shown as a prefix/suffix to reinforce the ritual context.

# ⚙️ FUNCTIONAL CORE & INTERACTION DYNAMICS (2025 Harmonization)
- All existing props are sufficient for capturing profound user input in the Portal. No changes needed.
- **Label is mandatory** and must be visibly associated (see Accessibility).
- **HelperText** and **Error** must be programmatically linked using `aria-describedby`.
- **aria-invalid="true"** is required for error states.

# 🧭 USAGE PROTOCOLS & ACCESSIBILITY (2025 Harmonization)
- Meets/exceeds WCAG AAA for color contrast, focus indicators, and keyboard navigation.
- All interactive states (focus, error, disabled) are visually and programmatically distinct.
- Ritual accessibility: The act of input is framed as a meaningful declaration, not a mere transaction.

# ⚖️ ETHICAL ALIGNMENT & PET (2025 Harmonization)
- **Purpose of Data:** The `label` or `helperText` (or Eos Lumina's framing) must make the purpose of the input clear (e.g., "Your answer will help shape your core values profile").
- **Transparency:** If input is logged in `NarrativeChoiceLog` or influences AI, this should be transparent in the UI context.
- **Data Minimization:** Prompts should encourage expressiveness but also conciseness where appropriate.
- **No Dark Patterns:** All input requests are opt-in, non-coercive, and clearly labeled.

# ✨ SYMBOLIC RESONANCE & RITUAL INTEGRATION
- The component is a vessel for "Ritual of Declaration" or "Ritual of Expression." In the Portal, it is the user's tool for self-articulation and value formation.
- Symbolic overlays, glyphs, and color states should echo the mythic language of ThinkAlike (see [symbolic_myth_index.md]).
- Ritual framing and PET/Clarity are inseparable—clarity is sacred.

# 💻 IMPLEMENTATION ECHOES (Examples)
```jsx
<TextInput
  label="Username"
  value={username}
  onChange={(e) => setUsername(e.target.value)}
  placeholder="Enter your unique identifier"
  required
/>
<TextInput
  label="Search"
  value={searchTerm}
  onChange={(e) => setSearchTerm(e.target.value)}
  leadingIcon={<SearchIcon />}
  type="search"
/>
```

```jsx
const [email, setEmail] = useState('');
const [emailError, setEmailError] = useState('');

const handleEmailChange = (event) => {
  setEmail(event.target.value);
  if (!event.target.value.includes('@')) {
    setEmailError('Please enter a valid email address.');
  } else {
    setEmailError('');
  }
};

return (
  <TextInput
    label="Email Address"
    id="user-email"
    value={email}
    onChange={handleEmailChange}
    type="email"
    placeholder="your.name@example.com"
    error={emailError}
    required
    helperText="We will use this to send important notifications."
  />
);
```

# 📝 Changelog
- 2025-06-09 :: v1.1.1 :: FINALIZED – Metadata update (status, version, last pulse, stewards, alignment signals, resonates_with), deepen symbolic/ritual framing (Ritual of Declaration), confirm Error Red for error/invalid, PET/Clarity, accessibility, and add changelog entry. Ensure references to symbolic_myth_index.md and ritual_as_interface_re_enchanting_digital_interaction.md are present.
- 2025-06-08 :: v1.1.0 :: HARMONIZED – Expanded guidance for Portal Realm, clarified error state color, PET/Clarity, and symbolic/ritual framing.

<div align="center">
<img src="../assets/thinkalike_logo.svg" alt="ThinkAlike Logo Placeholder" width="40" height="40" />
<br/>
<em>ThinkAlike — Harmonizing Human & Machine</em>
</div>
