---
title: Obsidian Dashboard Logic
version: 1.0
maintained_by: Lumina∴ System Meta-Agent
status: Active — Agent Tooling Guide
last_updated: 2025-05-11
tags: [obsidian, navigation, ui_logic, agents, dashboard]
---

# 🗂️ Obsidian Dashboard Logic

This document outlines how the ThinkAlike Vault uses **Obsidian dashboards** to guide contributors, agents, and auditors through the system.

---

## 🧭 Purpose

- Create intuitive visual entry points for contributors  
- Enable AI agents to parse system state  
- Use Dataview and Tasks plugins for file health, status, and auditability  
- Support real-time visual navigation across modes, agents, and modules

---

## 🔍 Core Components

- `📍Start Here.md` → Primary gateway file  
- `feature_document_matrix.md` → Living file tracker  
- `active_task_board.md` → Contributor + AI assignment control  
- `documentation_history.md` → All file lineage + edits

---

## 🧠 AI Agent Behavior

Agents must:
- Begin with `📍Start Here.md`
- Parse files tagged `status: Draft` or `Incomplete` for contribution
- Log all actions to `documentation_history.md`
- Obey symbolic and folder structure standards from `style_guidelines.md`

---

## 🔧 Recommended Plugins

- **Homepage**: set `📍Start Here.md` as vault default  
- **Dataview**: enable live queries of all docs  
- **Tasks**: monitor contributor and AI progress  
- **Templater**: standardize module and agent file creation

---

## 📌 Dashboard Query Example

```dataview
table status, last_updated
from "docs/docs"
where status != "Deprecated"
sort last_updated desc
