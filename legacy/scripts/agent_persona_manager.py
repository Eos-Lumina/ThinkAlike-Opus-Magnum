"""
Agent Persona Manager Script for ThinkAlike Project

Purpose:
- Prevents fragmentation of agent persona files and registry.
- Validates that all agent persona .md files in agents/ follow the
  ThinkAlike template.
- Updates agent_registry.md with new/removed/renamed personas.
- Archives superseded personas and logs changes.
- Optionally checks for broken or legacy references in documentation.

Usage:
    python scripts/agent_persona_manager.py [--validate] [--sync-registry]
           [--archive-old] [--check-references]

Recommended to run as a pre_commit hook or CI step.

NOTE: Only reference canonical documentation in docs/contributors/ and
      test plan in tests/testing_and_validation_plan.md.
Deprecated folders/files (e.g., docs/guides/contributor_guides/,
      docs/project/archive/testing_and_validation_plan.md) must not be
      recreated or referenced.
"""

import argparse
import glob
import logging
import os
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

AGENTS_ROOT = Path(__file__).parent.parent / "agents"
LEGACY_AGENTS = Path(__file__).parent.parent / "legacy_archive" / "agents"
ARCHIVE_ROOT = LEGACY_AGENTS
REGISTRY_PATH = AGENTS_ROOT / "agent_registry.md"
DOCS_ROOT = Path(__file__).parent.parent / "docs"

TEMPLATE_HEADER = (
    "<!-- ThinkAlike: State-of-the-Art Branded Markdown Template v3.0 -->"  # noqa: E501
)


# Utility functions
def find_agent_persona_files():
    # Only include .md files that are not agent_registry.md
    files = AGENTS_ROOT.rglob("*.md")
    return [f for f in files if f.name != "agent_registry.md"]


def validate_template(file_path):
    with open(file_path, encoding="utf-8") as f:
        content = f.read()
    return TEMPLATE_HEADER in content


def archive_persona(file_path):
    ARCHIVE_ROOT.mkdir(parents=True, exist_ok=True)
    target_path = ARCHIVE_ROOT / file_path.name
    shutil.move(str(file_path), str(target_path))


def update_registry(persona_files):
    """
    Auto-update agents/agent_registry.md to reflect the current set of persona
    files.
    This function should parse the persona files for key metadata (e.g., name,
    role, status) and rewrite the registry table.
    """
    # Example: Extract agent name and file path from each persona file
    registry_lines = [
        (
            "| Agent Name | Role | Symbolic Lineage | File Path | Status | "
            "Description |"
        ),
        "|------------|------|------------------|-----------|--------|-------------|",
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
        status_pattern = r"\*\*Status:\*\* ([^\n]+)"
        status_match = re.search(status_pattern, content)
        status = status_match.group(1).strip() if status_match else ""
        # Extract symbolic lineage (from Symbolic Lineage line)
        lineage_pattern = r"\*\*Symbolic Lineage:\*\* ([^\n]+)"
        lineage_match = re.search(lineage_pattern, content)
        lineage = lineage_match.group(1).strip() if lineage_match else ""
        # Extract description (from first paragraph after abstract)
        desc_pattern = r"## Scholarly Mandate \(Abstract\)\n+([^\n]+)"
        desc_match = re.search(desc_pattern, content)
        desc = desc_match.group(1).strip() if desc_match else ""
        rel_path = f.relative_to(AGENTS_ROOT.parent).as_posix()
        line = f"| {name} | {role} | {lineage} | `{rel_path}` | " f"{status} | {desc} |"
        registry_lines.append(line)
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


logger = logging.getLogger(__name__)


@dataclass
class CommunicationStyle:
    """Defines the communication style of an agent persona."""

    tone: str
    vocabulary_level: str
    use_of_metaphor: bool = False
    preferred_phrasing: Optional[List[str]] = None
    verbosity: Optional[str] = None  # Extended from observations
    directness: Optional[str] = None  # Extended from observations
    humor_level: Optional[str] = None  # Extended from observations


@dataclass
class EthicalBoundaries:
    """Defines the ethical boundaries and directives for a persona."""

    directives: List[str] = field(default_factory=list)


@dataclass
class KnowledgeDomain:
    """Specifies the persona's areas of expertise or knowledge boundaries."""

    domains: List[str] = field(default_factory=list)


@dataclass
class CapabilitiesProfile:
    """Describes the persona's intended strengths or capabilities."""

    strengths: List[str] = field(default_factory=list)


@dataclass
class SystemPromptComponents:
    """Structured components for building the LLM system prompt."""

    role_definition: str
    task_orientation: str
    style_guidance: str
    constraint_reminders: Optional[List[str]] = None


@dataclass
class Persona:
    """Represents an agent persona, loaded from a YAML definition file."""

    persona_id: str
    display_name: str
    symbolic_lineage: str
    core_mission: str
    description: str
    communication_style: CommunicationStyle
    ethical_boundaries: EthicalBoundaries
    knowledge_domain: KnowledgeDomain
    capabilities_profile: CapabilitiesProfile
    system_prompt_components: SystemPromptComponents
    schema_version: str

    status: str = "active"
    visual_cue_references: Optional[Dict[str, Any]] = None
    author: Optional[str] = None
    last_updated: Optional[str] = None  # ISO 8601 date
    change_log: Optional[List[Dict[str, str]]] = None
    extended_attributes: Optional[Dict[str, Any]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Persona":
        """Creates a Persona object from a dictionary."""
        data_copy = data.copy()

        cs_data = data_copy.pop("communication_style", {})
        comm_style = CommunicationStyle(**cs_data)

        eb_data = data_copy.pop("ethical_boundaries", {})
        eth_boundaries = EthicalBoundaries(**eb_data)

        kd_data = data_copy.pop("knowledge_domain", {})
        know_domain = KnowledgeDomain(**kd_data)

        cp_data = data_copy.pop("capabilities_profile", {})
        cap_profile = CapabilitiesProfile(**cp_data)

        spc_data = data_copy.pop("system_prompt_components", {})
        sys_prompt_comp = SystemPromptComponents(**spc_data)

        visual_cues = data_copy.pop("visual_cue_references", None)
        extended_attrs = data_copy.pop("extended_attributes", None)

        return cls(
            communication_style=comm_style,
            ethical_boundaries=eth_boundaries,
            knowledge_domain=know_domain,
            capabilities_profile=cap_profile,
            system_prompt_components=sys_prompt_comp,
            visual_cue_references=visual_cues,
            extended_attributes=extended_attrs,
            **data_copy,
        )


class PersonaManager:
    """Manages the loading, validation, and retrieval of personas."""

    def __init__(self, persona_dir: str):
        self.persona_dir = persona_dir
        self.personas: Dict[str, Persona] = {}
        self._load_personas()

    def _load_personas(self):
        """Loads all persona YAML files from the specified directory."""
        path_pattern = os.path.join(self.persona_dir, "**/*.yaml")
        yaml_files = glob.glob(path_pattern, recursive=True)
        for file_path in yaml_files:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    persona_data = yaml.safe_load(f)
                    persona_id = persona_data.get("persona_id")
                    if persona_id:
                        self.personas[persona_id] = Persona.from_dict(persona_data)
            except (yaml.YAMLError, FileNotFoundError) as e:
                logger.error(f"Error loading persona from {file_path}: {e}")

    def get_persona(self, persona_id: str) -> Optional[Persona]:
        """Retrieves a persona by its ID."""
        return self.personas.get(persona_id)

    def list_personas(self) -> List[Persona]:
        """Returns a list of all loaded personas."""
        return list(self.personas.values())


def main():
    """Main function for the persona manager script."""
    parser = argparse.ArgumentParser(description="Manage agent personas.")
    parser.add_argument(
        "--persona-dir",
        type=str,
        default="./personas",
        help="The directory where persona YAML files are stored.",
    )
    parser.add_argument(
        "--list", action="store_true", help="List all available personas."
    )
    parser.add_argument(
        "--get",
        type=str,
        metavar="PERSONA_ID",
        help="Get a specific persona by ID.",
    )

    args = parser.parse_args()

    manager = PersonaManager(args.persona_dir)

    if args.list:
        for persona in manager.list_personas():
            print(f"- {persona.persona_id}: {persona.display_name}")

    if args.get:
        persona = manager.get_persona(args.get)
        if persona:
            print(yaml.dump(persona.__dict__, default_flow_style=False))
        else:
            print(f"Persona with ID '{args.get}' not found.", file=sys.stderr)
