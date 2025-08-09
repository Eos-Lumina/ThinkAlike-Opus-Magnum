---
title: AIWaveformIndicator
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

<!-- ∴ THINKALIKE COMPONENT MANIFEST ∴ -->
<!-- UID: /docs/ui_components/ai_waveform_indicator.md -->

<br/>

<p align="center">
  <img src="/docs/assets/thinkalike_logo.svg" alt="ThinkAlike Logo" width="80"/>
</p>

<h1 align="center" style="font-family: 'Montserrat', Arial, sans-serif; font-weight: 700; color: #FF8C00; letter-spacing: 0.05em; border-bottom: 1px solid #666666; padding-bottom: 0.2em;">
  AIWaveformIndicator
</h1>

<p align="center" style="font-family: 'Open Sans', Arial, sans-serif; font-size: 1.1em; color: #CCCCCC; margin-bottom: 2em;">
  A core interactive element for transparent AI presence and feedback.<br/>
  <em>ThinkAlike: Connecting like minded individuals.</em>
</p>

---
<!-- METADATA LAYER -->
<div style="font-family: 'Courier New', monospace; font-size: 0.9em; color: #666666; margin-bottom: 2em; padding: 1em; border: 1px dashed #333333; background-color: #1a1a1a;">
  <p><strong>STATUS</strong> ::: Harmonized</p>
  <p><strong>VERSION</strong> ::: 1.1.0</p>
  <p><strong>LAST PULSE</strong> ::: 2025-06-08</p>
  <p><strong>STEWARD(S)</strong> ::: UI Systems Guild & Eos Lumina∴</p>
  <p><strong>ALIGNMENT SIGNALS</strong> ::: <code>[ai_feedback]</code> <code>[visualization]</code> <code>[symbolic_representation]</code> <code>[pet_compliant]</code> <code>[transparency]</code> <code>[clarity_protocol]</code> <code>[animation]</code></p>
  <p><strong>RESONATES WITH</strong> ::: <code>[../style/canonical_visual_style_guide.md#ai-agent-indicator]</code> <code>[AITriangleIndicator]</code> <code>[NarrativeViewer]</code> <code>[LoadingSpinner]</code></p>
</div>

---

# AIWaveformIndicator

## ✨ Overview & Purpose (2025 Harmonization)
The AIWaveformIndicator is the canonical, symbolic UI component for representing the presence and activity state of AI agents—especially Eos Lumina∴—in ThinkAlike. It provides immediate, transparent feedback on AI status during all narrative and ritual flows, supporting Radical Transparency, the Clarity Protocol, and the "Ritual over Interface" principle. Its visual language is central to Eos Lumina’s persona in the Portal Realm and during Narrative Duets.

---

## 👁️ Visual Representation & States
- **Visual:** Circular element with a central pulsating light and a sinusoidal waveform, echoing the "AI Agent Indicator" motif. Dark mode by default, with glowing orange (#FF8C00), amber (#FFC300), and blue accents. Animation and color shift by state.
- **States:**
  - **idle/listening:** Amber/Honey Yellow pulse, blue waveform. Used when Eos is present but not actively narrating.
  - **active/processing:** Deep Mandarine Orange pulse, blue waveform, pronounced animation. Used when Eos is generating, evaluating, or processing narrative/duet logic.
  - **communicating:** Blue-accented pulse or waveform. Used when Eos is narrating, presenting dialogue, or responding in real time.
  - **awaiting_input:** Gentle Amber pulse. Used when Eos is waiting for a user choice or input (e.g., at a choice point or after a question).
  - **error:** Error Red (#FF4136) flicker, border, or waveform. Always links to the Alert component for detailed error messages. Used for system or narrative errors.
- **Symbolic Alignment:** Strict adherence to ThinkAlike’s color, animation, and iconography standards. All states use high-contrast, glowing effects for accessibility and symbolic resonance.

---

## ⚙️ Functional Specifications (Props/Attributes)
| Name      | Type   | Required | Description |
|-----------|--------|----------|-------------|
| `aiState` | enum: 'idle' | 'active' | 'communicating' | 'awaiting_input' | 'error' | Yes | Controls visual state and animation. |
| `size`    | string/number | No | Diameter of the indicator. Default: '48px'. |
| `label`   | string | No | Accessibility label describing the AI's current state (e.g., "Eos Lumina is listening"). |
| `onClick` | function | No | Callback if made interactive. |

- **aiState Guidance:**
  - `idle`: Eos is present but not narrating.
  - `active`: Eos is processing/generating narrative or evaluating Duet logic.
  - `communicating`: Eos is narrating, presenting dialogue, or responding.
  - `awaiting_input`: Eos is waiting for user input/choice.
  - `error`: System/narrative error; always uses Error Red and links to Alert.

---

## 🧭 Usage Guidelines & Accessibility
- **Contextual Placement:** Use wherever Eos Lumina∴ or another AI agent is active—alongside dialogue in NarrativeViewer, in the Portal UI, or during Duets.
- **Real-time Updates:** Must update immediately to reflect AI state changes, reinforcing transparency and ritual presence.
- **ARIA Roles:** Always use `role="status"` and `aria-live="polite"` for state changes. The `label` prop should dynamically describe the current state (e.g., "Eos Lumina is processing your choice").
- **Motion Sensitivity:** Support `prefers-reduced-motion` for users sensitive to animation.
- **Color Contrast:** All states meet or exceed WCAG AAA contrast. Error state always uses Error Red (#FF4136).
- **Keyboard Accessibility:** If interactive, Tab to focus, Enter/Space to activate.

---

## ⚖️ Ethical & PET / Symbolic Alignment
- **Radical Transparency:** Clearly signals AI presence/activity; never manipulative or ambiguous.
- **Consent & Data Minimization:** Purely presentational; does not handle user data or consent directly.
- **Clarity Protocol:** Function and meaning are immediately clear and documented.
- **Persona Reflection:** Animation and color reinforce Eos Lumina’s persona—wise, clear, and energetically present.

---

## 💻 Example Usage
```jsx
<AIWaveformIndicator
  aiState="communicating"
  size="64px"
  label="Eos Lumina is narrating"
/>
```

---

## Changelog
- **2025-06-08 :: v1.1.0 :: HARMONIZED** – Confirmed and clarified all states, PET/Clarity, and symbolic alignment for restored Portal and Duet flows.
- **2025-06-07 :: v1.0.1 :: UPDATE** – Standardized error state visual cues to use Error Red (#FF4136).
- **2025-06-07 :: v1.0.0 :: GENESIS** – Standardized to canonical template, PET/Clarity/symbolic alignment. Initial harmonized version.
