---
title: CommunityCard / CommunityProfileView
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
tags:
- cards
---


<!-- ∴ THINKALIKE COMPONENT MANIFEST ∴ -->
<!-- UID: /docs/ui_components/community_profile_display.md -->

<br/>

<p align="center">
  <!-- Placeholder for a prominent Community/Hive Glyph or Sigil -->
  <span style="font-size: 3em; color: #FFD700;"> 🐝 </span> <!-- Example Hive Glyph -->
</p>

<h1 align="center" style="font-family: 'Montserrat', Arial, sans-serif; font-weight: 700; color: #FFD700; letter-spacing: 0.05em; border-bottom: 1px solid #666666; padding-bottom: 0.2em;">
  COMMUNITYCARD / COMMUNITYPROFILEVIEW
</h1>

<p align="center" style="font-family: 'Open Sans', Arial, sans-serif; font-size: 1.1em; color: #CCCCCC; margin-bottom: 2em;">
  Visualizing the identity, values, and living activity of a ThinkAlike Hive.
</p>

---
<!-- METADATA LAYER -->
<div style="font-family: 'Courier New', monospace; font-size: 0.9em; color: #666666; margin-bottom: 2em; padding: 1em; border: 1px dashed #333333; background-color: #1a1a1a;">
  <p><strong>STATUS</strong> ::: Harmonized - Finalized</p>
  <p><strong>VERSION</strong> ::: 0.9.0</p>
  <p><strong>LAST PULSE</strong> ::: 2025-06-07</p>
  <p><strong>STEWARD(S)</strong> ::: UI Systems Guild | CommunityWeaver∴</p>
  <p><strong>ALIGNMENT SIGNALS</strong> ::: <code>[data_display]</code> <code>[community]</code> <code>[hive]</code> <code>[clarity_protocol]</code> <code>[pet_compliant]</code></p>
  <p><strong>RESONATES WITH</strong> ::: <code>[../style/canonical_visual_style_guide.md]</code> <code>[ProfileCard / UserProfileView.md]</code> <code>[ValueProfile.md]</code> <code>[DataTraceability.md]</code></p>
</div>

---

# CommunityCard / CommunityProfileView

> **Purpose:**
> The CommunityCard and CommunityProfileView components present the identity, values, and living activity of a ThinkAlike Hive (community). They embody the symbolic and functional essence of collective intelligence, transparency, and shared purpose.

## Visual & Symbolic Guidelines
- **Style:** Dark theme, glowing gold/amber accents (a symbolic extension for Hive/Community components; base palette follows canonical blue/orange on dark theme). Hive glyphs, hexagonal backgrounds, and animated constellation overlays (e.g., node-link overlays or animated lines connecting members). Animated member avatars or sigils.
- **Structure:**
  - **CommunityCard (compact):**
    - Hive glyph, name, tagline/mission, member count, key values, and recent activity indicator.
  - **CommunityProfileView (detailed):**
    - All of the above, plus: full description, value constellation, governance summary, recent proposals/decisions, member roster, and links to governance/data policies.
- **Symbolic Role:** The "living hive"—a constellation of values, members, and shared purpose. Each element is a ritual marker of community identity.

## Usage
```jsx
<CommunityCard
  community={communityData}
  variant="compact"
  onClick={handleSelect}
/>

<CommunityProfileView
  community={communityData}
  onMemberClick={handleMemberClick}
  onProposalClick={handleProposalClick}
/>
```

## Props
| Name              | Type                | Required | Description                                                        |
|-------------------|---------------------|----------|--------------------------------------------------------------------|
| `community`       | `CommunityProfile`  | Yes      | Community data structure (see below).                              |
| `variant`         | `"compact" | "detailed"` | No | Card or profile view.                                              |
| `onClick`         | `() => void`        | No       | Card click handler (for compact view).                             |
| `onMemberClick`   | `(memberId: string) => void` | No | Handler for member avatar/sigil click.                             |
| `onProposalClick` | `(proposalId: string) => void` | No | Handler for proposal/recent activity click.                        |
| `className`       | `string`            | No       | Additional CSS class names.                                        |
| `id`              | `string`            | No       | HTML id attribute.                                                 |
| `privacyLevel`    | `"open" | "invite-only" | "private"` | No | Community privacy setting.                                         |
| `memberVisibility`| `"public" | "members-only" | "hidden"` | No | Controls visibility of member list.                                |
| `joinRitualUrl`   | `string`            | No       | URL for ritualized onboarding/joining.                             |
| `onJoinRitual`    | `() => void`        | No       | Handler for ritualized join action.                                |

**CommunityProfile Type Definition:**
```typescript
interface CommunityProfile {
  id: string;
  name: string;
  tagline?: string;
  description?: string;
  memberCount: number;
  members: Array<{
    id: string;
    name: string;
    avatarUrl?: string;
    sigil?: React.ReactNode;
    role?: string;
  }>;
  keyValues: string[];
  recentActivity: Array<{
    id: string;
    type: 'proposal' | 'decision' | 'event';
    summary: string;
    timestamp: string;
  }>;
  governanceSummary?: string;
  dataPolicyUrl?: string;
  valueConstellation?: string[];
  privacyLevel?: 'open' | 'invite-only' | 'private';
  memberVisibility?: 'public' | 'members-only' | 'hidden';
  joinRitualUrl?: string;
}
```

## PET/Clarity & Symbolic Protocols
- **Transparency:**
  - Governance, membership criteria, and data sharing policies are visible and accessible.
  - Recent proposals/decisions are surfaced for radical transparency.
  - Member lists respect privacy settings; users can control visibility of their profile within the community.
- **Ritual over Interface:**
  - Joining or interacting with a community can trigger a ritualized onboarding or welcome overlay, reinforcing symbolic entry.
  - Onboarding rituals may include guided tours, introductory messages from stewards, or interactive tutorials on community values and practices.
- **Symbolic Representation:**
  - Hive glyphs, hexagonal/constellation motifs, and animated sigils reinforce the living, collective nature of the community.
  - Value constellation visually encodes the community’s core values.

## Accessibility
- All interactive elements are keyboard navigable and focusable.
- Member avatars/sigils and activity items have accessible labels.
- Color contrast meets or exceeds WCAG AAA.
- Community structure and activity are announced to screen readers (e.g., "Community Hive: 42 members, 3 new proposals").
- All overlays, modals, and links are accessible and clearly labeled.
- Community cards/profiles use appropriate ARIA roles (e.g., `role="region"` or `role="group"`).
- Dynamic information (member count, recent activity) is announced using ARIA live regions.
- Member and proposal lists are keyboard navigable and support focus management.
- Empty states (e.g., no recent activity, hidden members) are handled gracefully and announced to users.

## Example
```jsx
<CommunityProfileView
  community={{
    id: 'hive1',
    name: 'Clarity Hive',
    tagline: 'Transparency, Trust, Transformation',
    description: 'A community dedicated to radical transparency and ethical collaboration.',
    memberCount: 42,
    members: [
      { id: 'm1', name: 'Aletheia', sigil: <span>🦉</span>, role: 'Steward' },
      { id: 'm2', name: 'Mythos', sigil: <span>🐉</span> },
      { id: 'm3', name: 'Echo', sigil: <span>🦋</span> }
    ],
    keyValues: ['Transparency', 'Trust', 'Collaboration'],
    recentActivity: [
      { id: 'p1', type: 'proposal', summary: 'Adopt PET/Clarity Protocols', timestamp: '2025-06-06' },
      { id: 'd1', type: 'decision', summary: 'Approved new member onboarding ritual', timestamp: '2025-06-05' }
    ],
    governanceSummary: 'Consensus-based, with rotating stewards.',
    dataPolicyUrl: '/docs/policies/community_data_policy.md',
    valueConstellation: ['Transparency', 'Trust', 'Transformation']
  }}
  onMemberClick={id => showMemberProfile(id)}
  onProposalClick={id => showProposalDetails(id)}
/>
```

## Migration Notes
- Replace legacy community/hive display components with CommunityCard / CommunityProfileView for PET/Clarity and symbolic alignment.
- Integrate with ValueProfile, DataTraceability, and ProfileCard/UserProfileView components.
- Ensure all visual motifs and overlays are harmonized with the canonical style guide.

## Changelog
2025-06-07 :: v0.9.0 :: DRAFT – Initial harmonized documentation. Defines CommunityCard / CommunityProfileView as the canonical community/hive display, aligned with PET/Clarity, symbolic, and accessibility protocols.

<div align="center">
<img src="../assets/thinkalike_logo.svg" alt="ThinkAlike Logo Placeholder" width="40" height="40" />
<br/>
<em>ThinkAlike — Harmonizing Human & Machine</em>
</div>
