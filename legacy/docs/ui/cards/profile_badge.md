---
title: ProfileBadge UI Component
document_status: Harmonized - Finalized
version: 1.0.0
last_updated: 2025-06-09
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
alignment_tags:
- profile
- badge
- trust
- reputation
- PET/Clarity
- accessibility
- symbolic
- resonance
related_components:
- HousingOfferCard
- HousingNeedCard
- ConsentMatrixOverlay
- ChronaTransactionModal
- RitualOnboardingFlow
visual_style_guide_ref: ../style/canonical_visual_style_guide.md
tags:
- cards
---


<!-- ∴ THINKALIKE COMPONENT MANIFEST ∴ -->
# 🛡️ PROFILE BADGE
<small>"Trust, earned and seen."</small>

## ⚭ OVERVIEW & PURPOSE
The ProfileBadge is a symbolic, PET/Clarity-aligned UI element for displaying user trust, reputation, and key profile attributes. It is used throughout ThinkAlike to visually communicate DID-bound reputation, feedback, and symbolic status in a compact, accessible format. The badge is foundational for building trust and conveying key attributes at a glance in ProfileCard, CommunityProfileDisplay, HousingOfferCard, and HousingNeedCard.

---

## 👁️‍🗨️ VISUAL & SYMBOLIC GUIDELINES
- **Shape & Structure:** Circular or shield-shaped badge, with layered glyphs for trust, feedback, and symbolic status. Only one primary badge/glyph is shown at a time; if multiple, consider a ProfileBadgeGroup or cycle/aggregate visually.
- **Color Harmonics:**
  - Gold (#FFD700) for verified/trusted
  - Blue (#1E90FF) for feedback
  - Orange (#FF9500) for new/ritual status
  - **Error Red (#FF4136)** for warnings or revoked trust
- **Symbolic Overlays/Glyphs:**
  - **Trust:** Checkmark (✔️), star (⭐), handshake (🤝), flame (🔥 for ritual)
  - **Feedback:** Numeric score or count as a sub-badge, ring, or small overlay (e.g., 4.5★, or a blue ring with the number inside)
  - **PET/Clarity:** Optional overlays for privacy/consent (lock 🔒, eye 👁️, shield 🛡️) if badge represents profile visibility status
- **States:**
  - **Default:** All glyphs and overlays visible, high contrast
  - **Hover/Focus:** Badge slightly enlarges, border glows in accent color
  - **Error/Revoked:** Badge dims, Error Red border/accent, tooltip explains status
- **Accessibility:** ARIA role `img` with comprehensive `aria-label` (e.g., "Profile Trust Status: Verified. Community Feedback: 4.5 average. Active Ritual Participant."). Color is never the sole indicator; glyphs and text reinforce meaning.

---

## ⚙️ FUNCTIONAL CORE & INTERACTION DYNAMICS (PROPS)
| Name           | Type                | Required | Description |
|----------------|---------------------|----------|-------------|
| did / userId   | string              | Yes      | Decentralized identifier for the user. |
| trustLevel     | 'verified' | 'trusted' | 'new' | 'revoked' | 'pending_verification' | Yes | Trust status, affects glyph and color. |
| feedbackScore  | number              | No       | Aggregate feedback or rating (e.g., 4.5). |
| feedbackCount  | number              | No       | Number of feedback entries. |
| badge          | BadgeDetail         | No       | Primary symbolic badge (e.g., host, mentor, ritual participant). |
| petStatus      | 'private' | 'public' | 'consent-required' | No | PET/Clarity overlay status. |
| onClick        | function            | No       | Handler for badge click (e.g., show profile details or tooltip). |

**BadgeDetail interface:**
```ts
interface BadgeDetail {
  label: string;
  glyph: string; // Unicode or SVG glyph
  description?: string;
}
```

---

## 🧭 USAGE PROTOCOLS & ACCESSIBILITY
- Used in profile cards, community member lists, onboarding flows, and housing cards.
- ARIA role: `img` with `aria-label` describing trust level, feedback, and badge.
- Tooltip or modal with full badge details on click or focus.
- Color is never the sole means of conveying trust or status; glyphs and text are always present.
- Error/warning states are announced to screen readers.
- WCAG AAA compliance targeted.

---

## ⚖️ PET/CLARITY & SYMBOLIC PROTOCOLS
- **Transparency:** All trust/status indicators are clear, with tooltips explaining their meaning. Trust is earned, not bought.
- **Non-Extractive:** Badges and trust levels are earned through community participation, not payment or extraction.
- **Symbolic:** Each glyph and color is meaningful and explained in a legend or tooltip.

---

## ✨ IMPLEMENTATION ECHOES (EXAMPLES)
```jsx
// Example 1: Verified user with feedback
<ProfileBadge
  userId="did:example:123"
  trustLevel="verified"
  feedbackScore={4.8}
  feedbackCount={32}
  badge={{ label: "Host", glyph: "⭐", description: "Recognized community host." }}
  petStatus="public"
  onClick={() => showBadgeDetails()}
/>

// Example 2: New user, ritual participant
<ProfileBadge
  userId="did:example:456"
  trustLevel="new"
  badge={{ label: "Ritual Participant", glyph: "🔥", description: "Completed onboarding ritual." }}
  petStatus="consent-required"
/>

// Example 3: Revoked trust
<ProfileBadge
  userId="did:example:789"
  trustLevel="revoked"
  badge={{ label: "Revoked", glyph: "❌", description: "Trust revoked due to policy violation." }}
  feedbackScore={2.1}
  feedbackCount={5}
  petStatus="private"
/>
```

---

## ⏳ CHRONICLE OF EVOLUTION (CHANGELOG)
- 2025-06-09 :: v1.0.0 :: HARMONIZED – Clarified symbolic glyphs, color harmonics, trustLevel enum, BadgeDetail usage, PET/Clarity, accessibility, and richer examples. Error Red and transparency reaffirmed.
- 2025-06-07 :: v1.0.0 :: FINALIZED – Harmonized with PET/Clarity, symbolic, and accessibility guidelines.

> This component is foundational for trust and reputation in ThinkAlike. All design, implementation, and review must follow PET/Clarity, accessibility, and symbolic/ritual guidelines as outlined in the project specification.

<div align="center">
<img src="../assets/thinkalike_logo.svg" alt="ThinkAlike Logo Placeholder" width="40" height="40" />
<br/>
<em>ThinkAlike — Harmonizing Human & Machine</em>
</div>
