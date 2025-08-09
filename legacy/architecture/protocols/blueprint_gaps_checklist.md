---
title: Blueprint Gaps & Next Actions: Prioritized Checklist (June 2025)
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Blueprint Gaps & Next Actions: Prioritized Checklist (June 2025)

This document summarizes the most important gaps and next steps surfaced by recent simulations and blueprint validation. Use this as your master to-do list for blueprint completion and project readiness.

---

## 1. Data Models & Schemas
- [ ] Finalize all core entities and relationships in `data_models.md` (especially for agent, trust, audit, and narrative modules)
- [ ] Add/clarify ERD diagrams for new modules as needed

## 2. Unified API & Protocols
- [ ] Ensure all endpoints in OpenAPI spec match the expanded data model (add missing PCI, agent, trust, audit, and narrative endpoints)
- [ ] Cross-link all protocol docs and update `protocols_overview.md` as new details are added

## 3. Chrona Wallet & Economic Protocol
- [ ] Specify UBI distribution logic, demurrage, and auditability
- [ ] Complete Chrona Wallet UI/UX spec (ritualized flows, accessibility, audit)
- [ ] Ensure all Chrona transaction types and metadata are modeled

## 4. Governance & Trust
- [ ] Finalize Hive, HiveMember, HiveGovernance, and Trust models (roles, proposals, voting, trust indicators)
- [ ] Complete governance dashboard and trust UI specs
- [ ] Specify trust protocol, privacy controls, and audit endpoints

## 5. Agent & Narrative Engine
- [ ] Fully specify AgentSession, AgentPersona, AgentRegistry, AgentMemory, and AgentAction protocols
- [ ] Complete UI specs for agent chat/guidance and narrative interfaces
- [ ] Specify NarrativeDuet branching, scoring, and audit logic

## 6. Consent & Data Traceability
- [ ] Ensure all consent and traceability flows are modeled, auditable, and user-facing
- [ ] Add/clarify audit and traceability endpoints for all major actions

## 7. Documentation & Cross-Linking
- [ ] Update all indices, onboarding guides, and FAQ to reflect new flows and modules
- [ ] Cross-link all protocol, API, and UI docs for easy navigation

## 8. Internationalization (i18n) & Multilingual Support
- [ ] Ensure all UI components, onboarding flows, and documentation are designed for easy translation and language selection
- [ ] Specify i18n framework and translation management tools (e.g., i18next, Lokalise)
- [ ] Plan for translation of agent responses, narrative content, and onboarding scripts
- [ ] Prioritize translation of key documents and guides
- [ ] Add language selection and fallback logic to user experience

---

## Recommendations
- Prioritize completion of the most user-facing and foundational flows (onboarding, Chrona wallet, agent/narrative, governance/trust)
- Use simulation documents as checklists for blueprint and protocol doc updates
- Validate each flow with plain-language user journeys before implementation
- Keep all documentation modular, up-to-date, and cross-referenced

---

*Update this checklist as gaps are closed and new priorities emerge. This is your living roadmap to a complete, actionable blueprint.*
