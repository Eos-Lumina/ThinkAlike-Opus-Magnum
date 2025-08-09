---
title: NarrativeViewer Component
document_status: Harmonized - Finalized
version: 1.1.0
last_updated: 2025-06-08
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
alignment_tags:
- narrative
- ai_interaction
- pet_compliant
- clarity_protocol
- symbolic_interface
- accessibility_AAA
related_components:
- AIWaveformIndicator
- AITriangleIndicator
visual_style_guide_ref:
- ../style/canonical_visual_style_guide.md
tags:
- viewer
---


![ThinkAlike Logo](/assets/logo.svg)

# NarrativeViewer

A core interactive element for exploring and interacting with AI-generated narratives.

<em>ThinkAlike: Connecting like minded individuals.</em>

---
<!-- METADATA LAYER -->
<div style="font-family: 'Courier New', monospace; font-size: 0.9em; color: #666666; margin-bottom: 2em; padding: 1em; border: 1px dashed #333333; background-color: #1a1a1a;">
  <p><strong>DOCUMENT STATUS</strong> ::: Harmonized - Finalized</p>
  <p><strong>VERSION</strong> ::: 1.1.0</p>
  <p><strong>LAST UPDATED</strong> ::: 2025-06-08</p>
  <p><strong>MAINTAINED BY</strong> ::: UI Systems Guild, Eos Lumina∴</p>
  <p><strong>ALIGNMENT TAGS</strong> ::: <code>[narrative]</code> <code>[ai_interaction]</code> <code>[pet_compliant]</code> <code>[clarity_protocol]</code> <code>[symbolic_interface]</code> <code>[accessibility_AAA]</code></p>
  <p><strong>RELATED COMPONENTS</strong> ::: <code>[AIWaveformIndicator]</code> <code>[AITriangleIndicator]</code></p>
  <p><strong>VISUAL STYLE GUIDE REF</strong> ::: <code>[../style/canonical_visual_style_guide.md]</code></p>
</div>

---

## ⚭ OVERVIEW

*   The NarrativeViewer enables users to explore, interact with, and reflect on AI-generated narratives within the ThinkAlike ecosystem.
*   It supports transparency, user agency, and symbolic interaction by making narrative structure, AI involvement, and user choices explicit and visually engaging.

## ✨ Overview & Purpose (2025 Harmonization)

The NarrativeViewer is the core interactive component for all narrative-driven experiences in ThinkAlike. It:
- Presents interactive, branching narratives guided by AI agents (primarily Eos Lumina∴), supporting both individual reflective journeys (Portal Realm) and two-persona compatibility tests (Narrative Duets).
- Enables ritualized, symbolic, and PET/Clarity-aligned storytelling, with explicit support for AI dialogue, user choices, symbolic dilemmas, and threshold rituals.

## 👁️‍🗨️ VISUAL RESONANCE & STATES

*   **Visual Embodiment:**
    *   Presents narratives as interactive, branching story paths or modular blocks, with dark mode as default and glowing accents for active paths and choices. Choices and narrative nodes may appear as glowing nodes/lines, evoking a node-graph or ritual map.
    *   Visualizes user choices, AI interventions, and narrative flow using ThinkAlike’s symbolic motifs (e.g., nodes, glyphs, ritual transitions).
    *   Typography: Montserrat for headers, Open Sans for narrative text and choices.
    *   <!-- Mockup: [Link to /docs/assets/visuals/narrative_viewer_mockup.png or Storybook entry] -->
*   **Color Harmonics & Typography:**
    *   Uses canonical palette for narrative, choice, and AI highlights (see style guide). Choices and AI interventions use high-contrast, glowing effects (e.g., Neon Orange #FF8C00, Deep Ruby #800000, Amber #FFC300) for accessibility and symbolic resonance.
    *   <span style="color: #FF4136; font-weight: bold;">All error/alert states (e.g., narrative load/generation errors) must use Error Red (#FF4136) for text, icons, and highlights, per the canonical visual style guide.</span>
    *   Montserrat for headers, Open Sans for narrative text and choices.
*   **States of Being:**
    *   Default: Narrative display, user can read and scroll.
    *   Choice Point: Highlights available user choices, animates on hover/focus.
    *   AI Intervention: Distinct color/glyph for AI-generated or suggested narrative branches.
    *   Reflection/Review: Allows users to revisit previous choices and see narrative consequences.
    *   Loading/Processing: Subtle spinner or waveform indicator during AI generation.
    *   Error: Clear, symbolic alert if narrative cannot be loaded/generated. <span style="color: #FF4136; font-weight: bold;">Error visuals use Error Red (#FF4136).</span>

## ⚙️ FUNCTIONAL CORE & INTERACTION DYNAMICS

*   **Behavioral Blueprint:**
    *   Displays narrative content, user choices, and AI interventions in a clear, interactive format.
    *   Supports branching, backtracking, and reflection on narrative paths.
    *   Animates transitions between narrative states and choices.
*   **Interface Contract (Props/Attributes):**
    *   `narrative`: `NarrativeBlock[]` – The structured narrative data to display.
    *   `onChoice`: `(choiceId: string) => void` – Callback when a user makes a choice.
    *   `currentStep`: `number` – The current position in the narrative.
    *   `aiState?`: `string` – Current AI status (for displaying AI activity indicators).
    *   `personaContext?`: `string` – Enum for narrative context (e.g., onboarding, duet facilitator).
    *   `showSpeakerIndicator?`: `boolean` – If true, shows speaker indicators (avatar/glyph/name).
    *   `interactiveElements?`: `Array<{ type: 'text_choice' | 'symbolic_glyph_choice' | 'reflective_input_field', label: string, glyph?: string }>` – Defines user choices, including symbolic and reflective input types.
    *   `isLoadingNextBlock?`: `boolean` – If true, shows loading state for the next narrative block.
    *   `className?`: `string` – Additional CSS class names.
    *   `id?`: `string` – HTML id attribute.
*   **Signal Emissions (Events):**
    *   `choiceMade`: `(choiceId: string)` – Emitted when a user selects a narrative choice.
    *   `narrativeAdvanced`: `(step: number)` – Emitted when the narrative progresses.
    *   `aiIntervention`: `(details: object)` – Emitted when AI generates or suggests a branch.

**NarrativeBlock Type Example:**
```typescript
interface NarrativeBlock {
  id: string;
  type: 'EosDialogue' | 'UserChoicePrompt' | 'AICloneResponse' | 'SymbolicDilemma' | 'RitualTransition';
  speaker?: string; // e.g., 'Eos Lumina', 'AI Clone', 'System'
  text?: string;
  glyphs?: string[]; // Symbolic glyphs inline or as choice icons
  choices?: Array<{ id: string; label: string; glyph?: string }>;

  inputField?: { label: string; placeholder: string };
  ritualId?: string; // For threshold rituals
}
```

## 🧭 USAGE PROTOCOLS & ACCESSIBILITY

*   **Contextual Deployment:**
    *   Use in Narrative Mode, onboarding journeys, and any context where user/AI co-creation is central.
    *   Avoid using for static or non-interactive content.
*   **Universal Access (Accessibility - WCAG AAA Target):**
    *   All narrative text and choices must be screen reader accessible.
    *   Keyboard navigation for all interactive elements (Tab, Arrow keys, Enter/Space).
    *   ARIA roles: `button` for choices, `article`/`region` for narrative blocks, `application` for the viewer if highly interactive.
    *   Live regions (`aria-live="polite"` or `assertive"`) announce new narrative content and state changes.
    *   Speaker indicators and symbolic glyphs have descriptive alt text/ARIA labels.
    *   All color/animation cues meet or exceed WCAG AAA contrast and are perceivable by assistive tech.

## ⚖️ ETHICAL ALIGNMENT & PET (Privacy, Ethics, Transparency)

*   **Cognitive Liberty:**
    *   User choices are explicit, reversible, and never coerced.
    *   AI interventions are clearly marked and explained.
*   **Radical Transparency:**
    *   All AI-generated content and logic are visually distinct and, where possible, linkable to AI Transparency Log.
*   **Consent Weaving:**
    *   If narrative content involves user data, consent is requested and can be revoked.
*   **Data Minimization Field:**
    *   Only essential narrative and choice data are displayed.
*   **Clarity Protocol Embodiment:**
    *   Narrative structure, choices, and AI involvement are always clear and auditable.

## ✨ SYMBOLIC RESONANCE & RITUAL INTEGRATION

*   **Glyphic & Mythic Embodiment:**
    *   Uses ThinkAlike glyphs for nodes, choices, and AI interventions.
*   **"Ritual over Interface" Contribution:**
    *   Transitions and feedback are designed to feel meaningful and contemplative, not mechanical.
*   **AI Agent Reflection (If AI-Specific):**
    *   Visual and behavioral cues reflect the persona and ethical boundaries of the guiding AI agent (e.g., Eos Lumina∴).
*   **Pacing and Transition Rituals:**
    *   Text reveal, transitions, and overlays are paced to reinforce the ritual experience.
    *   Supports display of "Threshold Gate Rituals" when moving between major narrative sections.

## 💻 IMPLEMENTATION ECHOES (Optional)

```jsx
// Conceptual React/TSX Example
export function NarrativeViewer({ narrative, onChoice, currentStep, aiState, personaContext, showSpeakerIndicator, interactiveElements, isLoadingNextBlock, className, id }) {
  // ...render narrative blocks, choices, AI interventions, and review UI
  return <div className={`narrative-viewer ${className}`} id={id}>{/* ... */}</div>;
}
```

**Eos Lumina∴ Riddle Example:**
```jsx
<NarrativeViewer
  narrative={[
    { id: '1', type: 'EosDialogue', speaker: 'Eos Lumina', text: 'I am the gate and the mirror. What do you seek?' },
    { id: '2', type: 'UserChoicePrompt', choices: [
      { id: 'a', label: 'Truth', glyph: '👁️' },
      { id: 'b', label: 'Transformation', glyph: '🔥' },
      { id: 'c', label: 'Connection', glyph: '🕸️' }
    ] }
  ]}
  onChoice={choiceId => handleChoice(choiceId)}
  currentStep={1}
  aiState="idle"
  personaContext="EosLuminaOnboarding"
  showSpeakerIndicator
/>
```

**Narrative Duet Example:**
```jsx
<NarrativeViewer
  narrative={[
    { id: '1', type: 'EosDialogue', speaker: 'Eos Lumina', text: 'Welcome to the Duet. What will you reveal?' },
    { id: '2', type: 'UserChoicePrompt', choices: [
      { id: 'a', label: 'Share a memory', glyph: '📜' },
      { id: 'b', label: 'Offer a dream', glyph: '🌌' }
    ] },
    { id: '3', type: 'AICloneResponse', speaker: 'AI Clone', text: 'I see your dream. Here is my echo...' }
  ]}
  onChoice={choiceId => handleDuetChoice(choiceId)}
  currentStep={2}
  aiState="active"
  personaContext="EosLuminaDuetFacilitator"
  showSpeakerIndicator
  isLoadingNextBlock={isLoading}
/>
```
