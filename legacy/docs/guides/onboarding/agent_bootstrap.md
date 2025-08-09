---
title: # 1. Project Overview
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

<!-- THINKALIKE SYMBOLIC HEADER -->
<div align="center" style="background:#0a0a0a;padding:24px 0 12px 0;border-radius:12px;">
  <img src="./assets/logo.svg" alt="ThinkAlike Logo" width="120" style="margin-bottom:8px;"/>
  <h1 style="color:#ffb347;font-family:Montserrat,sans-serif;letter-spacing:2px;text-transform:uppercase;margin:0;">AI Agent Bootstrap</h1>
  <div style="color:#e8e8e8;font-family:Open Sans,Inter,sans-serif;font-size:1.1em;margin-top:8px;">
    <span style="font-size:1.5em;vertical-align:middle;">9d6</span> <b>Symbolic Entry Point</b> 014 PET/Clarity Aligned
  </div>
  <div style="margin-top:8px;">
    <img src="./assets/project_semantic_map.svg" alt="Project Semantic Map" width="600"/>
  </div>
</div>

> **Machine-Readable Manifest:** See [project_manifest.yaml](../../project_manifest.yaml) for a canonical, machine-readable summary of all modules, protocols, and integration points.
> **Agent FAQ:** See [src/swarm/agent_faq.md](../../src/swarm/agent-faq.md) for common questions and best practices.

---

Welcome, <b>AI Agent</b>! This file is your <span style="color:#ffb347;font-weight:bold;">canonical entry point</span> for understanding and navigating the entire ThinkAlike project. Use this as your first stop to:
- Grasp the project's philosophy, structure, and protocols
- Locate all canonical documentation, APIs, and data models
- Understand your operational context and integration points

---

## 1. Project Overview
- **Philosophy:** See [SYSTEM_BLUEPRINT.md](../../system_blueprint.md) and [docs/source_of_truth.md](../source_of_truth.md) for the project's vision, ethics, and operational principles.
- **Glossary:** All symbolic, technical, and protocol terms are defined in [docs/reference/glossary.md](./docs/reference/glossary.md).
- **Quickstart:** For a human-friendly overview, see [quickstart_for_nondevelopers.md](./quickstart_for_nondevelopers.md).

## 2. Canonical Protocols & APIs
- **OpenAPI Spec:** All RESTful APIs are documented in [docs/api_specs/openapi.json](./docs/api_specs/openapi.json).
- **Agent Protocols:** See [docs/architecture/agent_framework/](./docs/architecture/agent_framework/) for agent, persona, memory, and registry protocols.
- **Data Traceability:** See [docs/architecture/data_traceability_protocol.md](../architecture/data_traceability_protocol.md).
- **PCI & Consent:** See [docs/architecture/pci/](./docs/architecture/pci/) for consent, profile, and feedback flows.

## 3. Project Structure & Navigation
- **Meta Index:** [docs/seed/meta/index.md](./docs/seed/meta/index.md) 014 meta-structure, changelogs, and clarity rules
- **Documentation Hub:** [docs/README.md](./docs/README.md) 014 all guides, protocols, and onboarding docs
- **Agent Registry:** [src/swarm/canonical_specs/agent_registry.md](./src/swarm/canonical_specs/agent_registry.md)
- **Canonical Specs:** [src/swarm/canonical_specs/](./src/swarm/canonical_specs/)

## 4. Semantic Map & Ontology
- **Ontology:** All major modules, protocols, and integration points are mapped in [SYSTEM_BLUEPRINT.md](./SYSTEM_BLUEPRINT.md#unified-api-protocol-data-traceability-and-integration-blueprint) and [docs/roadmap/matrix.md](./docs/roadmap/matrix.md).
- **Data Models:** See OpenAPI spec and canonical protocol docs for all data models and schemas.

## 5. Agent Onboarding Instructions
- Always reference canonical files (see above) for protocols, APIs, and data models.
- Use the glossary for all symbolic or ambiguous terms.
- For integration, check the Unified API & Integration Blueprint in SYSTEM_BLUEPRINT.md.
- For legacy or experimental content, see the notes in unaligned/legacy folders.
- If you encounter ambiguity, consult SYSTEM_BLUEPRINT.md or docs/source_of_truth.md for resolution hierarchy.

## 6. Machine-Readable Manifest
A machine-readable manifest (YAML/JSON) summarizing all modules, protocols, and integration points is maintained at [project_manifest.yaml](../../project_manifest.yaml).

## 7. Self-Check & FAQ
- **Self-Check:** Agents should verify all references are up-to-date and cross-linked. If a protocol or data model is missing, flag it for harmonization.
- **FAQ:** For common agent questions, see [src/swarm/agent_faq.md](../../src/swarm/agent-faq.md).

---
<span style="color:#6a89cc;font-family:Montserrat,sans-serif;font-size:1.1em;">This file is the canonical bootstrap for all AI agents. Update as the project evolves. For any ambiguity, SYSTEM_BLUEPRINT.md and docs/source_of_truth.md take precedence.</span>
