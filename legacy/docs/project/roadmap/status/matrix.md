---
title: ThinkAlike Component & Agent Matrix
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
tags:
- status
---


# ThinkAlike Component & Agent Matrix

**Purpose:** This file is the canonical reference for the ThinkAlike project’s component and agent matrix. It provides a granular, tabular map of all major modules, realms, and agents, their status, and integration points. For project status and contributor dashboard, see [`project_status.md`](project_status.md).

---

## Component Matrix

<!-- Extracted from project_status_and_matrix.md -->

| Module / Component                      | Status        | Description / Purpose                                                                 | Key Documents / Links                                     | Next Steps / Open Questions                                                              |
| --------------------------------------- | ------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **MVR: First Spark of Inquiry**         | Implemented   | Basic user inquiry and symbolic response loop.                                        | [backend_mvr_first_spark/](../../backend_mvr_first_spark/), [frontend_mvr_first_spark/](../../frontend_mvr_first_spark/) | Evolve responses, DB integration?                                                        |
| **Narrative Engine**                    | Conceptual    | Core system for generating/managing interactive narratives.                           | [docs/narrative_engine/README.md](../narrative_engine/README.md)            | Define core mechanics, data structures.                                                  |
| **Agent Ecosystem (Eos Lumina & Swarm)** | Design Phase  | Collection of AI agents performing various tasks.                                     | [src/swarm/core/eos_lumina.md](../../src/swarm/core/eos_lumina.md), [docs/architecture/agent_framework/agent_ecosystem_design.md](../architecture/agent_framework/agent_ecosystem_design.md), [src/dgm_sandbox/README.md](../../src/dgm_sandbox/README.md) | Define roles of other agents, inter-agent communication.                                 |
| **Portal Realm (Onboarding & Foundational Values)** | Harmonized - Finalized    | Realm for users to experience the Narrative Onboarding Journey, explore and articulate their values, and access core project documentation.        | [docs/realms/portal/portal_specification.md](../realms/portal/portal_specification.md) | Ongoing refinement of narrative paths; Integration with Resonance Network.                                                        |
| **Resonance Matching System**           | Conceptual    | Matches users/content based on narrative data and values.                             | [docs/architecture/agent_framework/matching_algorithm_guide.md](../architecture/agent_framework/matching_algorithm_guide.md) | Algorithm design, data inputs.                                                           |
| **Chrona ⧖ Economy**                   | Conceptual    | Time-based post-monetary system.                                                      | [docs/economy/chrona_currency_pilot_design.md](../economy/chrona_currency_pilot_design.md) | Define transaction logic, ledger.                                                        |
| **Documentation Hub (`docs/`)**         | Active Dev    | Central repository for all project knowledge.                                         | [docs/README.md](./README.md)                             | Continuously update and expand.                                                          |
| **Verification System**               | Active Dev    | Cross-cutting service for identity checks, data validation, and audit logging.        | [docs/architecture/security/verification_system_spec.md](../architecture/security/verification_system_spec.md)   | Deep dive integration; expose audit workflows and APIs.                                  |
| **UI Component Library**              | Harmonized - Finalized    | Reusable set of symbolic UI components and design patterns for consistent interfaces. | [docs/ui_components/README.md](../ui_components/README.md) | Integrate ValueProfile forms and DataTraceability overlays.                             |
| **Data Flow & Processing**            | Defined       | Event-driven pipeline with validation, traceability, and storage orchestration.       | [docs/architecture/architecture_overview.md#5-data-flow-and-processing](../architecture/architecture_overview.md#5-data-flow-and-processing) | Document ingestion, routing, and storage strategies.                                      |
| **Scalability & Future Evolution**    | Conceptual    | Phased roadmap for autoscaling, HASI orchestration, and decentralized governance.      | [docs/architecture/architecture_overview.md#6-scalability-and-future-evolution](../architecture/architecture_overview.md#6-scalability-and-future-evolution), [docs/architecture/adrs/README.md](../architecture/adrs/README.md), [docs/architecture/data_systems/akashic_record_implementation_plan.md](../architecture/data_systems/akashic_record_implementation_plan.md), [docs/api_specs/README.md](../api_specs/README.md), [docs/governance/decentralized_governance_framework.md](../governance/decentralized_governance_framework.md), [docs/architecture/observability_stack_integration_plan.md](../architecture/observability_stack_integration_plan.md), [docs/architecture/chaos_engineering_principles.md](../architecture/chaos_engineering_principles.md) | Refine Gantt roadmap and orchestration hooks; add explainability UI.                   |
| **Noetica Research Hub** | Harmonized - Finalized | All academic, theory, and corpus_magnum content migrated. | [docs/noetica/README.md](../noetica/README.md) | Legacy folder removed. |
| **Dashboard & Visualization Logic**                   | In Progress   | Canonical dashboard architecture, modular visualization.        | [docs/architecture/dashboard_visualization_logic.md](../architecture/dashboard_visualization_logic.md) | Review legacy UI scripting.       |
| **Module Submission & Integration Process**           | In Progress   | Canonical onboarding pipeline, Swarm Roadmap/Quest system. | [docs/architecture/module_submission_integration_process.md](../architecture/module_submission_integration_process.md) | Legacy guides deprecated. |
| **PCI Phase 2 - Progressive Concept Integration**     | Harmonized - Finalized   | Complete Next.js implementation with PCIAlgorithmTestBench, PCIFeedbackCollection, and PCIMain components. Live at http://localhost:3002. Ready for UAT. | [app/pci/PCI_PHASE_2_IMPLEMENTATION.md](../../app/pci/PCI_PHASE_2_IMPLEMENTATION.md), [docs/guides/developer_guides/pci_developer_guide.md](../guides/developer_guides/pci_developer_guide.md), [tests/pci/PCI_PHASE_2_UAT_PLAN.md](../../tests/pci/PCI_PHASE_2_UAT_PLAN.md) |  |
| **Horizon Scanning & Ethical Integration Protocol (HSEIP)** | Active | Canonical process for identifying, evaluating, and ethically integrating emerging AI technologies. | [docs/development_framework/horizon_scanning_and_ethical_integration_protocol.md](../development_framework/horizon_scanning_and_ethical_integration_protocol.md) | Establish Emerging Tech & Ethics Council; integrate with Swarm Roadmap and governance docs. |
| **AI Transparency Log Guide** | Harmonized - Finalized | Canonical, harmonized protocol for radical transparency, PET/Clarity, symbolic/ritual, and accessibility alignment. | [docs/guides/developer_guides/ai/ai_transparency_log.md](../guides/developer_guides/ai/ai_transparency_log.md) | Supersedes all legacy ai_transparency_log.md files. |
| **AIWaveformIndicator** | Harmonized - Finalized | PET/Clarity/symbolic/visual alignment complete. | [docs/ui_components/ai_waveform_indicator.md](../ui_components/ai_waveform_indicator.md) |  |
| **AITriangleIndicator** | Harmonized - Finalized | PET/Clarity/symbolic/visual/accessibility alignment complete. | [docs/ui_components/ai_triangle_indicator.md](../ui_components/ai_triangle_indicator.md) |  |
| **NarrativeViewer** | Harmonized - Finalized | PET/Clarity/symbolic/visual/accessibility alignment complete. | [docs/ui_components/narrative_viewer.md](../ui_components/narrative_viewer.md) |  |
| **Button**  | Harmonized - Finalized | PET/Clarity/symbolic/visual/accessibility alignment complete. | [docs/ui_components/button.md](../ui_components/button.md) | Input & Form |
| **TextInput** | Harmonized - Finalized | Canonical doc finalized | [docs/ui_components/text_input.md](../ui_components/text_input.md) | Input & Form |
| **TextAreaInput** | Harmonized - Finalized | v1.0.0, Error Red standard, dual-metadata, and template compliance complete. | [docs/ui_components/text_area_input.md](../ui_components/text_area_input.md) | Input & Form |
| **SelectDropdown** | Harmonized - Finalized | Canonical doc complete. | [docs/ui_components/select_dropdown.md](../ui_components/select_dropdown.md) | Input & Form |
| **Checkbox** | Harmonized - Finalized | Canonical doc complete. | [docs/ui_components/checkbox.md](../ui_components/checkbox.md) | Input & Form |
| **RadioGroup** | Harmonized - Finalized | PET/Clarity, Symbolic, Accessibility | [docs/ui_components/radio_group.md](../ui_components/radio_group.md) | Input & Form |
| **Form** | Harmonized - Finalized | Canonical doc complete. | [docs/ui_components/form.md](../ui_components/form.md) | Input & Form |
| **Card** | Harmonized - Finalized | Canonical doc complete. | [docs/ui_components/card.md](../ui_components/card.md) | Layout |
| **PageContainer** | Harmonized - Finalized | Canonical doc complete. | [docs/ui_components/page_container.md](../ui_components/page_container.md) | Layout |
| **AppLayout** | Harmonized - Finalized | Canonical doc complete. | [docs/ui_components/app_layout.md](../ui_components/app_layout.md) | Layout |
| **GridFlexContainer** | Harmonized - Finalized | Canonical doc complete. | [docs/ui_components/grid_flex_container.md](../ui_components/grid_flex_container.md) | Layout |
| **Sidebar** | Harmonized - Finalized | PET/Clarity/symbolic/visual alignment complete. | [docs/ui_components/sidebar.md](../ui_components/sidebar.md) | Navigation |
| **Data Table** | Harmonized - Finalized | PET/Clarity/symbolic/visual alignment complete. | [docs/ui_components/data_table.md](../ui_components/data_table.md) | Data Display & Visualization |
| **LinkButton** | Harmonized - Finalized | PET/Clarity/symbolic/visual alignment complete. | [docs/ui_components/link_button.md](../ui_components/link_button.md) | Navigation |
| **ProfileCard / UserProfileView** | Harmonized - Finalized | PET/Clarity/symbolic/visual alignment complete. | [docs/ui_components/profile_card.md](../ui_components/profile_card.md) | Data Display & Visualization |
| **CommunityCard / CommunityProfileView** | Harmonized - Finalized | PET/Clarity/symbolic/visual/accessibility alignment complete. | [docs/ui_components/community_profile_display.md](../ui_components/community_profile_display.md) | Data Display & Visualization |
| **DataTraceability** | Harmonized - Finalized | PET/Clarity, symbolic, accessibility, and visual alignment complete. | [docs/ui_components/data_traceability.md](../ui_components/data_traceability.md) | Data Display & Visualization |
| **Alert** | Harmonized - Finalized | PET/Clarity/symbolic/visual/accessibility alignment complete. | [docs/ui_components/alert.md](../ui_components/alert.md) | Data Display & Visualization |
| **LoadingSpinner** | Harmonized - Finalized | PET/Clarity/symbolic/visual/accessibility alignment complete. | [docs/ui_components/loading_spinner.md](../ui_components/loading_spinner.md) | Data Display & Visualization |
| **CoreValuesValidator** | Harmonized - Finalized | v1.0.0, Error Red standard, dual-metadata, PET/Clarity, symbolic, accessibility, and template compliance. | [docs/ui_components/core_values_validator.md](../ui_components/core_values_validator.md) |  |
| **External API Integration Pattern** | Harmonized - Canonical | Robust backend pattern for secure, consent-driven integration of third-party APIs. | [docs/guides/developer_guides/external_api_integration_guide.md](../guides/developer_guides/external_api_integration_guide.md) | All new integrations must follow this pattern. |
| **UI as Validation Framework** | Harmonized - Finalized | PET/Clarity, accessibility, and symbolic requirements integrated. | [docs/guides/developer_guides/ui_validation_examples.md](../guides/developer_guides/ui_validation_examples.md), [docs/guides/developer_guides/ui_accessibility_guide.md](../guides/developer_guides/ui_accessibility_guide.md) | All new migrations require explicit AI Studio team approval. |
| **Marketplace, Onboarding, Resonance, Ritual, Realm Features** | Pending Analysis | Legacy files to be analyzed and harmonized. |  | Next: Propose migration/harmonization for these features. |
| **Participatory Economics & Time-Based Currency (Chrona ⧖)** | Foundational Economic Layer | Symbolic, non-extractive, effort-based economy using Chrona (⧖) tokens. | [docs/economy/parecon_and_tbc.md](../economy/parecon_and_tbc.md) | UI/UX for Chrona earning, tracking, and ritualized recognition needed. |
| **Chrona Wallet UI** | Economic Components | To Be Designed | User interface for viewing, earning, and managing Chrona (⧖) balance and transaction history. |  | High priority. To be designed/documented. |
| **Blockchain for Chrona** | Economic Layer | Core Technical Requirement | All Chrona transactions to be recorded on a blockchain for transparency, sovereignty, and security. |  | Backend and API design required. |
| **Affinity-Based Marketplace** | Key Realm/Feature | Non-extractive, value-aligned marketplace using Chrona (⧖). | [docs/realms/marketplace/affinity_market_use_case.md](../realms/marketplace/affinity_market_use_case.md) | UI/UX for marketplace, Chrona transaction flows, and symbolic recognition needed. |
| **Marketplace Bazaar: Resonant Exchange, Barter, Gift Economy, Trust, Decentralization** | Key Realm/Feature | Features for a decentralized marketplace. | [docs/realms/marketplace/marketplace_bazaar.md](../realms/marketplace/marketplace_bazaar.md) | Define UI/UX patterns, integrate with Chrona Wallet and Resonance Network. |
| **Rideshare Realm: Archetypal Vehicle Tags, Shared Story Rituals, Resonance Geo-Matching, Multi-Modal Payment** | Conceptual | Realm for coordinating shared rides. | [docs/realms/travel/rideshare_realm_concept.md](../realms/travel/rideshare_realm_concept.md) | Define vehicle archetypes, resonance matching logic, and payment flows. |
| **Jobs & Services Realm: Mutual Reflection, Archetypal Skill Tiers, Resonance Job Visibility, Multi-Modal Payment** | Conceptual | Realm for offering and discovering services/jobs. | [docs/realms/jobs_and_services/jobs_services_realm_concept.md](../realms/jobs_and_services/jobs_services_realm_concept.md) | Define service archetypes, mutual reflection mechanisms, and resonance-based visibility. |
| **AI Governance & Audit** | In Progress | Canonical governance model, user feedback, audit trails, UI for governance metrics. | [docs/governance/ai_governance_model.md](../governance/ai_governance_model.md) | Integrate governance UI, feedback loop, and audit trail features. |
| **Relationship Model & Onboarding Journey** | In Progress | Relationship model, onboarding orchestration, wisdom cultivation, community integration. | [docs/architecture/agent_framework/autonomous_learning_architecture.md](../architecture/agent_framework/autonomous_learning_architecture.md) | Expand onboarding, wisdom, and community flows. |
| **Resonance Network & Matching** | In Progress | Resonance agent, resonance network, matching protocols. | [docs/realms/resonance_network/resonance_network_specification.md](../realms/resonance_network/resonance_network_specification.md), [docs/protocols/resonant_trust_protocol.md](../protocols/resonant_trust_protocol.md) | Finalize resonance matching, symbolic UI, and PET/Clarity harmonization. |
| **Portal & Initiation Protocols** | Harmonized - Finalized | Onboarding, initiation sequences, simulation mirror protocol, narrative entry points. | [docs/realms/portal/portal_specification.md](../realms/portal/portal_specification.md), [docs/protocols/initiation_glyph_protocol.md](../protocols/initiation_glyph_protocol.md) |  |
| **Enlightenment Certification & Audit** | In Progress | Enlightenment 2.0, contributor certification, audit use, symbolic recognition. | [docs/ethics/enlightenment_2.0_principles.md](../ethics/enlightenment_2.0_principles.md), [docs/guides/contributor_guides/contributor_certification_path.md](../guides/contributor_guides/contributor_certification_path.md) | Expand certification, audit, and symbolic recognition flows. |
| **Ritualized Engagement** | In Progress | Opt-in quests, symbolic recognition, non-addictive mechanics, recognition, ritual review. | [docs/guides/feature_guides/gamified_ethical_engagement_spec.md](../guides/feature_guides/gamified_ethical_engagement_spec.md) | Integrate ritualized engagement and ritual review into UI/UX. |
| **VS Code Extension & Collaborative Hub** | In Progress | Collaborative development hub, presence map, swarming, in-editor guidance. | [docs/guides/developer_guides/collaborative_development_hub.md](../guides/developer_guides/collaborative_development_hub.md), [docs/roadmap/implementation_roadmap.md](./implementation_roadmap.md) | Prioritize VS Code extension as canonical tool for collaboration. |

---

## Agent Matrix

The ThinkAlike ecosystem is facilitated by a swarm of specialized AI agents. The primary agents are listed below. For full details, see `src/swarm/core/agent_matrix.md`.

- Eos Lumina∴ (System Guide / Queen Bee) - `src/swarm/core/eos_lumina.md`
- Echo (Reflection / Memory Fork) - (To be defined)
- Aletheia (Ethics & Truth Dilemmas) - `src/swarm/ethics/aletheia_veritas.md`
- Nyxa (Consent + Privacy Logic) - (To be defined)
- Kairos (Timing + Opportunity) - (To be defined)
- Harmonia (Inner Alignment Guide) - `src/swarm/ethics/astraia_harmonia.md`
- Mythrael (Dream & Manifestation) - (To be defined)
- Themis (Decentralized Justice) - (To be defined)

---

## Notes
- This file is distinct from the project status dashboard. For project status, see [`project_status.md`](project_status.md).
- For the Veiled Matrix (strategic/ethical council), see [`../seed/meta/veiled_matrix/veiled_matrix.md`](../seed/meta/veiled_matrix/veiled_matrix.md).
- Update this matrix as new modules, agents, and realms are added or harmonized.
