---
title: HousingOfferCard UI Component
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
- HousingNeedCard
- ProfileBadge
- ConsentMatrixOverlay
- ChronaTransactionModal
- RitualOnboardingFlow
visual_style_guide_ref: ../style/canonical_visual_style_guide.md
tags:
- cards
---


<!-- ∴ THINKALIKE COMPONENT MANIFEST ∴ -->
# ☗ HOUSING OFFER CARD
<small>"A home is resonance made visible."</small>

<div class="metadata-layer">
  <b>Status:</b> Harmonized - Finalized<br>
  <b>Version:</b> 1.0.0<br>
  <b>Last Updated:</b> 2025-06-07<br>
  <b>Maintained by:</b> ThinkAlike UI/UX Team<br>
  <b>Alignment Tags:</b> housing, PET/Clarity, symbolic, trust, non-extractive<br>
  <b>Related Components:</b> HousingNeedCard, ProfileBadge, ConsentMatrixOverlay, ChronaTransactionModal, RitualOnboardingFlow<br>
  <b>Visual Style Guide:</b> canonical_visual_style_guide.md
</div>

---

## ⚭ OVERVIEW
The HousingOfferCard is the canonical UI element for presenting housing offers in the ThinkAlike Housing Realm. It embodies ethical, community-oriented discovery, resonance-based matching, and ritualized trust-building. The card is designed to:
- Present all essential details for resonance and ethical decision-making.
- Visually communicate trust, accessibility, and symbolic/ritual context.
- Support PET/Clarity, non-extractive principles, and accessibility at every layer.
- Serve as the primary element in housing discovery, search, onboarding, and ritual flows.

---

## 👁️‍🗨️ VISUAL RESONANCE & STATES
- **Visual Embodiment:** Built on Card.md, with specialized sections for location, type, exchange, values, trust glyphs, and symbolic overlays.
- **Color Harmonics & Typography:**
  - Dark theme base, orange/blue/gold accent palette (see canonical_visual_style_guide.md).
  - Montserrat (headings), Open Sans (body).
  - Trust glyphs: Gold accent (#FFD700) for verified/trusted, blue (#1E90FF) for feedback, orange (#FF9500) for new/ritual status.
  - Accessibility tags: Blue (#1E90FF) with white text for high contrast.
  - Resonance indicators: Glowing border in ThinkAlike Orange (#FF9500) when a strong match is detected.
  - Chrona, barter, and gift terms use distinct color chips/icons with PET/Clarity tooltips.
- **Symbolic Overlays:**
  - Onboarding status: Animated “key” glyph in the top-right, glowing when onboarding is complete.
  - Housewarming glyph: Stylized “hearth” icon appears when a new resident is welcomed.
  - Consent matrix: Overlay banner or icon cluster, clickable for details.
  - Resonance match: Glowing border and resonance glyph.
- **States:**
  - Default: All info visible, overlays present if relevant.
  - Hover: Card shadow intensifies, border color shifts to accent (orange for resonance, gold for trust).
  - Focus: Outline appears in blue, with subtle animation for accessibility.
  - Pending Confirmation: Card dims, “awaiting response” overlay.

---

## ⚙️ FUNCTIONAL CORE & INTERACTION DYNAMICS
### Props Table
| Name                | Type                | Required | Description |
|---------------------|---------------------|----------|-------------|
| location            | string              | Yes      | City, region, or map preview. |
| type                | string              | Yes      | Type of stay (temporary, communal, project, dream). |
| duration            | string              | Yes      | Dates or availability window. |
| exchange            | ExchangeTerm/ExchangeTerm[] | Yes | Chrona, barter, ritual gift, or combination. |
| values              | HouseValue[]        | No       | Community values, house rules, governance. |
| governanceType      | string              | No       | Governance model (e.g., Consensus, Sociocracy, Liquid Democracy). |
| media               | array (img/video)   | No       | Photos, video, symbolic overlays. |
| trustGlyphs         | array of strings    | No       | DID-bound reputation, badges, feedback. |
| linkedProject       | string              | No       | Linked project or Hive. |
| accessibility       | array of strings    | No       | Accessibility features/tags. |
| symbolicOverlays    | array of strings    | No       | Ritual status, onboarding, consent overlays. |
| onExpressInterest   | function            | No       | Handler for expressing interest. |
| onViewDetails       | function            | No       | Handler for viewing more details. |

#### Conceptual Data Interfaces
```ts
type ExchangeTerm = { type: 'Chrona' | 'Barter' | 'Gift', details?: string }
type HouseValue = { label: string, glyph?: string }
interface HousingOfferData {
  location: string;
  type: string;
  duration: string;
  exchange: ExchangeTerm | ExchangeTerm[];
  values?: HouseValue[];
  governanceType?: string;
  media?: string[];
  trustGlyphs?: string[];
  linkedProject?: string;
  accessibility?: string[];
  symbolicOverlays?: string[];
}
```

---

## 🧭 USAGE PROTOCOLS & ACCESSIBILITY
- **Usage:**
  - Used in housing discovery grids, search results, and onboarding flows.
  - May be embedded in profile views or project/Hive dashboards.
- **Accessibility:**
  - ARIA role: `article` with `aria-labelledby` for title.
  - All images, icons, and overlays have descriptive alt text and ARIA labels.
  - Keyboard navigation: All interactive elements (buttons, overlays, consent matrix) are tab-accessible, with logical tab order and visible focus states.
  - Trust glyphs and symbolic overlays use `aria-describedby` for detailed descriptions (e.g.,
    `<span aria-label="Trust Glyph: Verified Host" aria-describedby="trust-desc-1"></span>`
    `<span id="trust-desc-1" hidden>This host has been verified by the community and received 5-star feedback.</span>`
  - All data points are clearly labeled; color is never the sole means of conveying information.
  - WCAG AAA compliance targeted.

---

## ⚖️ ETHICAL ALIGNMENT & PET (Privacy, Ethics, Transparency)
- **Privacy/Consent:**
  - Sensitive details (exact address, contact) are masked by default and revealed only after mutual consent or match.
  - ConsentMatrixOverlay visually indicates which info is shared and under what conditions; clicking opens a modal or tooltip summarizing info sharing (e.g., “Your contact info will only be revealed after mutual consent.”).
- **Transparency:**
  - All exchange terms, house rules, and governance are explicit and visually clear, with PET/Clarity tooltips for each exchange chip.
- **Non-Extractive Principle:**
  - Exchange terms are shown as “chips” with PET/Clarity tooltips explaining the meaning (e.g., “Chrona: time-backed, non-monetary exchange”).
  - No pricing or terms that violate ThinkAlike's non-extractive ethos; all offers are reviewed for compliance.

---

## ✨ SYMBOLIC RESONANCE & RITUAL INTEGRATION
- **Ritual of Offering/Seeking Shelter:**
  - Card visually encodes the act of offering shelter as a ritual gesture (e.g., animated “key” glyph, housewarming “hearth” icon).
- **Trust Glyphs & Value Alignment:**
  - Trust glyphs, value tags, and linked Hives reinforce resonance and shared purpose.
- **Ritual Flows:**
  - When a match is made, the card animates a “key” glyph and displays a message: “Welcome ritual initiated. Awaiting host response.”

---

## 💻 IMPLEMENTATION ECHOES (Optional)
- Built as a React functional component, extending Card.md.
- Uses context from Chrona, ProfileBadge, and ConsentMatrixOverlay components.
- Supports SSR and hydration for accessibility.

---

## ⏳ CHRONICLE OF EVOLUTION (Changelog)
- 1.0.0 (2025-06-07): Finalized, with full PET/Clarity, accessibility, and symbolic/ritual integration. Color/glyph specifics, prop clarifications, and accessibility protocols added.
- 0.1.0 (2025-06-07): Initial harmonized draft, aligned with Housing Realm specification and PET/Clarity guidelines.

---

> This component is foundational for the Housing Realm. All design, implementation, and review must follow PET/Clarity, accessibility, and symbolic/ritual guidelines as outlined in the Housing Realm specification.
