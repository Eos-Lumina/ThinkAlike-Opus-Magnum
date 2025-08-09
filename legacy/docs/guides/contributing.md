---
title: "Contributing to ThinkAlike: A Guide for Co-Creators"
version: 3.0.0
status: Canonical
last_updated: 2025-07-08
authors:
  - "Eos Lumina ∴ (Collective Intelligence Meta-Agent)"
tags: [guide, contributing, development, workflow, code_of_conduct, swarming, conventional_commits]
spec_for: [All Contributors]
replaces:
  - "_legacy/protocols/onboarding_portal/contributing.md"
  - "_legacy/protocols/onboarding_portal/code_of_conduct.md"
  - "_legacy/protocols/onboarding_portal/contributor_dashboard.md"
  - "_legacy/protocols/onboarding_portal/developer_docs_index.md"
harmonization_note: |
  This is the definitive, harmonized guide for all contributors. It synthesizes the legacy contributor quickstart, code of conduct, and various resource dashboards into a single, comprehensive resource. It outlines the project's ethical covenant, technical workflow, and unique collaborative methodologies.
---

# Contributing to ThinkAlike: A Guide for Co-Creators

Welcome, Co-Creator. Thank you for your interest in contributing to the Great Work. This is an act of co-creation—a step on the path of Enlightenment 2.0. Every contribution, no matter how small, is a valued "Offering to the Collective."

This guide provides you with the necessary maps and tools to begin.

## 1. The Contributor's Covenant (Code of Conduct)

In the interest of fostering an open, welcoming, and revolutionary environment, we as contributors and maintainers pledge to make participation in our project and community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Expected Behaviors
- Be respectful, kind, collaborative, and constructive.
- Use welcoming and inclusive language.
- Be mindful of your impact on others.

### Unacceptable Behaviors
- Harassment, discrimination, hate speech, or personal attacks.
- Public or private harassment, including unwelcome sexual attention.
- Sustained disruption or any other conduct which could reasonably be considered inappropriate.

### Enforcement
Violations of this Code of Conduct will be handled by the project maintainers and may result in actions ranging from a private warning to a permanent ban. To report a violation, please contact the maintainers directly through established project channels.

*This covenant is adapted from the Contributor Covenant and is non-negotiable.*

## 2. First Principles: Understanding the Commons

Before you begin, you must orient yourself to our way of working:

- **Read the [Onboarding Journey](/guides/onboarding_journey.md):** All contributors must have completed the Portal Realm initiation to ensure alignment with project values.
- **Understand Our Philosophy:** This work is governed by the **Principle of Coherent Holism**. Before you contribute a single part (`Locus`), you must first understand the **Holistic Vision** it serves. The highest-level failure state is the introduction of fragmentation.
- **Consult the [Global Agent Bootstrap Protocol](/docs/protocols/global_agent_bootstrap_protocol.md):** This is the master protocol for alignment, tone, and structure.

## 3. The Contribution Workflow

We follow a standard Fork & Pull Request workflow. Pull Requests are considered "Dialogues of Resonance."

### 3.1. Quick Setup

1.  **Fork & Clone:** Fork the repository on GitHub, then clone it locally.
2.  **Install Dependencies:**
    ```bash
    # Set up Python virtual environment
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt

    # Install frontend dependencies
    npm install
    ```
3.  **Run Services:**
    ```bash
    # Start backend server (from root directory)
    uvicorn src.backend.app.main:app --reload

    # Start frontend server (in a separate terminal)
    npm run dev
    ```

### 3.2. The Process

1.  **Find a Task:** Find a "Quest" on the GitHub Issues page. Look for `good first issue` if you're new.
2.  **Create a Branch:** From the `main` branch, create a new branch: `type/issue-number-short-description` (e.g., `feat/123-profile-video`).
3.  **Develop:** Make your changes, adhering to all style guides and principles.
4.  **Commit Your Work:** We use **Conventional Commits**. This is mandatory.
    -   **Format:** `<type>(<scope>): <subject>` (e.g., `feat(api): add user profile endpoint`)
    -   **Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `ui`.
5.  **Submit a Pull Request:** Push to your fork and open a PR against our `main` branch. A maintainer will review your "Offering."

## 4. Our Development Methodology: Swarming

For complex tasks, we practice **Swarming**: multiple contributors working on the same task, at the same time, on one screen. This is a high-bandwidth, collaborative way to build, with rotating roles like "Navigator" and "Driver." Look for sessions in our community channels (e.g., Discord).

## 5. Using AI Assistants Ethically

We encourage using AI assistants as partners in creation. However, **you are always responsible for the code and content you submit.**

-   **Validate Everything:** Carefully review, test, and understand all AI-generated output.
-   **Be Specific:** Provide clear, context-rich prompts that include our ethical requirements and refer to our canonical protocols.
-   **Use for Boilerplate:** Let AI handle boilerplate so you can focus on the core logic, symbolic resonance, and ethical implementation.

## 6. Key Resources & Guides

This is your compass for navigating the project.

**Project Philosophy & Vision:**
  - [THINKALIKE_MASTER_BLUEPRINT.md](/THINKALIKE_MASTER_BLUEPRINT.md)
  - [Global Agent Bootstrap Protocol](/docs/protocols/global_agent_bootstrap_protocol.md)
  - [Alchemical Development Protocol](/protocols/meta/alchemical_development_protocol.md)
  - [Synergistic Field Protocol](/protocols/community/synergistic_field_protocol.md)
  - [PET/Clarity Framework](/docs/guides/pet_clarity_framework.md)
**Governance & Collaboration:**
  - [Governance Specification](/protocols/governance/governance_specification.md)
  - [Liquid Democracy Specification](/protocols/governance/liquid_democracy_specification.md)
  - [Resonance Trust Protocol](/protocols/resonance/resonance_trust_protocol.md)
**Core Architecture:**
  - [Data Architecture](/architecture/data_architecture.md)
  - [API Design Guidelines](/architecture/api_design_guidelines.md)
  - [Agent Interaction Models](/architecture/agent_interaction_models.md)
**User Experience:**
  - [Onboarding Journey](/guides/onboarding_journey.md)
  - [Portal Realm Specification](/docs/realms/portal_specification.md)
  - [Resonance Network Specification](/docs/realms/resonance_network_specification.md)
**Audit & Alignment:**
  - [Symbolic Alignment Review Log](/reflection_loops/symbolic_alignment_review_log.md)
  - [Data Preservation and Safety Policy](/DATA_PRESERVATION_AND_SAFETY_POLICY.md)

---

Thank you for joining the Quest. Your contribution shapes the future of ThinkAlike.
