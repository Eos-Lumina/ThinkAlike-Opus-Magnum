"""
Agent Persona Manager Script for ThinkAlike Project

Purpose:
- Prevents fragmentation of agent persona files and registry.
- Validates that all agent persona .md files in agents/ follow the ThinkAlike template.
- Updates agent_registry.md with new/removed/renamed personas.
- Archives superseded personas and logs changes.
- Optionally checks for broken or legacy references in documentation.

Usage:
    python scripts/agent_persona_manager.py [--validate] [--sync-registry] [--archive-old] [--check-references]

Recommended to run as a pre-commit hook or CI step.
"""

import os
import re
import shutil
from pathlib import Path

AGENTS_ROOT = Path(__file__).parent.parent / "agents"
ARCHIVE_ROOT = Path(__file__).parent.parent / "legacy_archive" / "agents"
REGISTRY_PATH = AGENTS_ROOT / "agent_registry.md"
DOCS_ROOT = Path(__file__).parent.parent / "docs"

TEMPLATE_HEADER = "<!-- ThinkAlike: State-of-the-Art Branded Markdown Template v3.0 -->"

# Utility functions
def find_agent_persona_files():
    # Only include .md files that are not agent_registry.md
    return [f for f in AGENTS_ROOT.rglob("*.md") if f.name != "agent_registry.md"]

def validate_template(file_path):
    with open(file_path, encoding="utf-8") as f:
        content = f.read()
    return TEMPLATE_HEADER in content

def archive_persona(file_path):
    ARCHIVE_ROOT.mkdir(parents=True, exist_ok=True)
    shutil.move(str(file_path), str(ARCHIVE_ROOT / file_path.name))

def update_registry(persona_files):
    """
    Auto-update agents/agent_registry.md to reflect the current set of persona files.
    This function should parse the persona files for key metadata (e.g., name, role, status) and rewrite the registry table.
    """
    # Example: Extract agent name and file path from each persona file
    registry_lines = [
        "| Agent Name | Role | Symbolic Lineage | File Path | Status | Description |",
        "|------------|------|------------------|-----------|--------|-------------|"
    ]
    for f in sorted(persona_files):
        with open(f, encoding="utf-8") as fh:
            content = fh.read()
        # Extract agent name (from first H1 or fallback)
        name_match = re.search(r"# ([^\n]+)", content)
        name = name_match.group(1).strip() if name_match else f.stem
        # Extract role (from subtitle or fallback)
        role_match = re.search(r"— ([^\n]+)", content)
        role = role_match.group(1).strip() if role_match else ""
        # Extract status (from Status line)
        status_match = re.search(r"\*\*Status:\*\* ([^\n]+)", content)
        status = status_match.group(1).strip() if status_match else ""
        # Extract symbolic lineage (from Symbolic Lineage line)
        lineage_match = re.search(r"\*\*Symbolic Lineage:\*\* ([^\n]+)", content)
        lineage = lineage_match.group(1).strip() if lineage_match else ""
        # Extract description (from first paragraph after abstract)
        desc_match = re.search(r"## Scholarly Mandate \(Abstract\)\n+([^\n]+)", content)
        desc = desc_match.group(1).strip() if desc_match else ""
        rel_path = f.relative_to(AGENTS_ROOT.parent).as_posix()
        registry_lines.append(f"| {name} | {role} | {lineage} | `{rel_path}` | {status} | {desc} |")
    with open(REGISTRY_PATH, "w", encoding="utf-8") as reg:
        reg.write("# ThinkAlike Agent Registry\n\n")
        reg.write("\n".join(registry_lines))
        reg.write("\n")

def check_legacy_references():
    legacy_patterns = ["src/agents/personas", "agents_harmonized"]
    broken = []
    for md_file in DOCS_ROOT.rglob("*.md"):
        with open(md_file, encoding="utf-8") as f:
            content = f.read()
        for pat in legacy_patterns:
            if pat in content:
                broken.append((md_file, pat))
    return broken

def main():
    persona_files = find_agent_persona_files()
    # Validate templates
    invalid = [f for f in persona_files if not validate_template(f)]
    if invalid:
        print("[ERROR] The following agent persona files do not follow the ThinkAlike template:")
        for f in invalid:
            print(f" - {f}")
        exit(1)
    # Auto-update registry
    update_registry(persona_files)
    print("[OK] All agent persona files validated and registry updated.")

if __name__ == "__main__":
    main()
