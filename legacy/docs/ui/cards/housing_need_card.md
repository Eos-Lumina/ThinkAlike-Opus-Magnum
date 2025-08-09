---
title: HousingNeedCard UI Component
document_status: Harmonized - Finalized
version: 1.0.0
last_updated: 2025-06-07
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
alignment_tags:
- housing
- UI component
- PET/Clarity
- accessibility
- symbolic
- resonance
- trust
- non-extractive
related_components:
- HousingOfferCard
- ProfileBadge
- ConsentMatrixOverlay
- ChronaTransactionModal
- RitualOnboardingFlow
visual_style_guide_ref: ../style/canonical_visual_style_guide.md
tags:
- cards
---


<!-- ∴ THINKALIKE COMPONENT MANIFEST ∴ -->
# ☗ HOUSING NEED CARD
<small>"To seek shelter is to invite resonance."</small>

<div class="metadata-layer">
  <b>Status:</b> Harmonized - Finalized<br>
  <b>Version:</b> 1.0.0<br>
  <b>Last Updated:</b> 2025-06-07<br>
  <b>Maintained by:</b> ThinkAlike UI/UX Team<br>
  <b>Alignment Tags:</b> housing, PET/Clarity, symbolic, trust, non-extractive<br>
  <b>Related Components:</b> HousingOfferCard, ProfileBadge, ConsentMatrixOverlay, ChronaTransactionModal, RitualOnboardingFlow<br>
  <b>Visual Style Guide:</b> canonical_visual_style_guide.md
</div>

---

## ⚭ OVERVIEW
The HousingNeedCard is the canonical UI element for expressing a need for housing in the ThinkAlike Housing Realm. It enables ethical, resonance-driven discovery, ritualized vulnerability, and trust-building. The card is designed to:
- Present all essential details for resonance-based matching and ethical response.
- Visually communicate trust, accessibility, and symbolic/ritual context.
- Support PET/Clarity, non-extractive principles, and accessibility at every layer.
- Serve as the primary element in housing need discovery, search, onboarding, and ritual flows.

---

## 👁️‍🗨️ VISUAL RESONANCE & STATES
- **Visual Embodiment:** Built on Card.md, with specialized sections for desired location, type, duration, exchange, required values, trust glyphs, and symbolic overlays.
- **Color Harmonics & Typography:**
  - Dark theme base, orange/blue/gold accent palette (see canonical_visual_style_guide.md).
  - Montserrat (headings), Open Sans (body).
  - Trust glyphs: Gold accent (#FFD700) for verified/trusted, blue (#1E90FF) for feedback, orange (#FF9500) for new/ritual status.
  - Accessibility tags: Blue (#1E90FF) with white text for high contrast.
  - Resonance indicators: Glowing border in ThinkAlike Orange (#FF9500) when a strong match is detected.
  - Chrona, barter, and gift terms use distinct color chips/icons with PET/Clarity tooltips.
  - Error Red (#FF4136) for error or missing required fields.
- **Symbolic Overlays:**
  - Ritual status: Animated “open door” glyph in the top-right, glowing when onboarding is complete.
  - Seeking shelter glyph: Stylized “lantern” icon appears when a new need is posted.
  - Consent matrix: Overlay banner or icon cluster, clickable for details.
  - Resonance match: Glowing border and resonance glyph.
- **States:**
  - Default: All info visible, overlays present if relevant.
  - Hover: Card shadow intensifies, border color shifts to accent (orange for resonance, gold for trust).
  - Focus: Outline appears in blue, with subtle animation for accessibility.
  - Error: Error Red (#FF4136) border and message for missing required fields.
  - Pending Confirmation: Card dims, “awaiting response” overlay.

---

## ⚙️ FUNCTIONAL CORE & INTERACTION DYNAMICS
### Props Table
| Name                | Type                | Required | Description |
|---------------------|---------------------|----------|-------------|
| desiredLocation     | string              | Yes      | City, region, or map preview. |
| type                | string              | Yes      | Type of stay (temporary, communal, project, dream). |
| duration            | string              | Yes      | Dates or desired availability window. |
| exchange            | ExchangeTerm/ExchangeTerm[] | Yes | Chrona, barter, ritual gift, or combination. |
| requiredValues      | HouseValue[]        | No       | Desired community values, house rules, governance. |
| governanceType      | string              | No       | Preferred governance model (e.g., Consensus, Sociocracy, Liquid Democracy). |
| accessibility       | array of strings    | No       | Required accessibility features/tags. |
| trustGlyphs         | array of strings    | No       | DID-bound reputation, badges, feedback. |
| symbolicOverlays    | array of strings    | No       | Ritual status, onboarding, consent overlays. |
| onExpressInterest   | function            | No       | Handler for expressing interest. |
| onViewDetails       | function            | No       | Handler for viewing more details. |
| urgencyLevel        | 'low' | 'medium' | 'high' | No | Indicates urgency of the housing need; affects visual emphasis and filtering. |
| dateFlexibility     | string              | No       | Flexibility of dates (e.g., 'Flexible', 'Fixed', 'Negotiable'). |

#### Conceptual Data Interfaces
```ts
type ExchangeTerm = { type: 'Chrona' | 'Barter' | 'Gift', details?: string }
type HouseValue = { label: string, glyph?: string }
interface HousingNeedData {
  desiredLocation: string;
  type: string;
  duration: string;
  exchange: ExchangeTerm | ExchangeTerm[];
  requiredValues?: HouseValue[];
  governanceType?: string;
  accessibility?: string[];
  trustGlyphs?: string[];
  symbolicOverlays?: string[];
  urgencyLevel?: 'low' | 'medium' | 'high';
  dateFlexibility?: string;
}
```

---

## 🧭 USAGE PROTOCOLS & ACCESSIBILITY
- **Usage:**
  - Used in housing need discovery grids, search results, and onboarding flows.
  - May be embedded in profile views or project/Hive dashboards.
- **Accessibility:**
  - ARIA role: `article` with `aria-labelledby` for title.
  - All images, icons, and overlays have descriptive alt text and ARIA labels.
  - Keyboard navigation: All interactive elements (buttons, overlays, consent matrix) are tab-accessible, with logical tab order and visible focus states.
  - Trust glyphs and symbolic overlays use `aria-describedby` for detailed descriptions.
  - All data points are clearly labeled; color is never the sole means of conveying information.
  - Error states (missing required fields) are announced to screen readers and visually marked in Error Red (#FF4136).
  - WCAG AAA compliance targeted.

---

## ⚖️ ETHICAL ALIGNMENT & PET (Privacy, Ethics, Transparency)
- **Privacy/Consent:**
  - Sensitive details (exact address, contact) are masked by default and revealed only after mutual consent or match.
  - ConsentMatrixOverlay visually indicates which info is shared and under what conditions; clicking opens a modal or tooltip summarizing info sharing.
- **Transparency:**
  - All exchange terms, house rules, and governance are explicit and visually clear, with PET/Clarity tooltips for each exchange chip.
- **Non-Extractive Principle:**
  - Exchange terms are shown as “chips” with PET/Clarity tooltips explaining the meaning (e.g., “Chrona: time-backed, non-monetary exchange”).
  - No pricing or terms that violate ThinkAlike's non-extractive ethos; all needs are reviewed for compliance.

---

## ✨ SYMBOLIC RESONANCE & RITUAL INTEGRATION
- **Ritual of Seeking Shelter:**
  - Card visually encodes the act of seeking shelter as a ritual gesture (e.g., animated “open door” glyph, lantern icon).
- **Trust Glyphs & Value Alignment:**
  - Trust glyphs, value tags, and linked Hives reinforce resonance and shared purpose.
- **Ritual Flows:**
  - When a match is made, the card animates a “lantern” glyph and displays a message: “Welcome ritual initiated. Awaiting host response.”

---

## 💻 IMPLEMENTATION ECHOES (Optional)
- Built as a React functional component, extending Card.md.
- Uses context from Chrona, ProfileBadge, and ConsentMatrixOverlay components.
- Supports SSR and hydration for accessibility.

---

## ⏳ CHRONICLE OF EVOLUTION (Changelog)
- 1.0.0 (2025-06-07): Finalized, with urgencyLevel and dateFlexibility props added for finer-grained control and filtering. PET/Clarity, accessibility, and symbolic/ritual integration complete.
- 0.1.0 (2025-06-07): Initial harmonized draft, aligned with Housing Realm specification and PET/Clarity guidelines. Error Red (#FF4136) included for error states.

---

> This component is foundational for the Housing Realm. All design, implementation, and review must follow PET/Clarity, accessibility, and symbolic/ritual guidelines as outlined in the Housing Realm specification.
