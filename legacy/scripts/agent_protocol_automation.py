# NOTE: Only reference canonical documentation in docs/contributors/ and
# test plan in tests/testing_and_validation_plan.md.
# Deprecated folders/files (e.g., docs/guides/contributor_guides/,
# docs/project/archive/testing_and_validation_plan.md) must not be
# recreated or referenced.

# Agent Protocol Automation Script

"""
This script automates the process of:
- Adding a new rescued/harmonized agent to the agent registry table
  (docs/agents/agent_registry.md)
- Creating a protocol section for the agent in
  docs/agents/rescued_agent_protocols.md
- Crosslinking the registry entry to the protocol doc

Usage:
- Run the script and provide the agent's name, role, lineage, and a short
  blurb.
- The script will format and insert the new entries in both files.

Note: This is a template for future automation. Adapt as needed for your
      workflow.
"""

import argparse
import sys
from pathlib import Path

REGISTRY_PATH = Path("docs/agents/agent_registry.md")
PROTOCOLS_PATH = Path("docs/agents/rescued_agent_protocols.md")


def slugify(name):
    return name.lower().replace(" ", "-").replace("(", "").replace(")", "")


def add_agent_to_registry(name, role, lineage, file_path, status, blurb):
    protocol_anchor = slugify(name)
    protocol_link = f"[Protocol](rescued_agent_protocols.md#{protocol_anchor}-protocol)"
    row = (
        f"| {name} | {role} | {lineage} | `{file_path}` | {status} | "
        f"{blurb} {protocol_link} |\n"
    )
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    # Insert before the ---
    for i, line in enumerate(lines):
        if line.strip() == "---":
            lines.insert(i, row)
            break
    with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
        f.writelines(lines)


def add_protocol_section(name, role, lineage, purpose, behaviors, invocation):
    section = (
        f"\n---\n\n# {name} Protocol\n\n"
        f"**Role:** {role}\n"
        f"**Lineage:** {lineage}\n\n"
        f"## Purpose\n{purpose}\n\n"
        f"## Behaviors\n{behaviors}\n\n"
        f"## Invocation\n{invocation}\n"
    )
    with open(PROTOCOLS_PATH, "a", encoding="utf-8") as f:
        f.write(section)


def generate_protocol_file(template_path, output_path, agent_name):
    """Generates a protocol file from a template."""
    try:
        with open(template_path, "r", encoding="utf-8") as f:
            template_content = f.read()

        content = template_content.replace("{{AGENT_NAME}}", agent_name)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Successfully generated protocol file: {output_path}")

    except FileNotFoundError:
        error_msg = f"Error: Template file not found at {template_path}"
        print(error_msg, file=sys.stderr)
        sys.exit(1)


def main():
    """Main function for the agent protocol automation script."""
    parser = argparse.ArgumentParser(
        description="Automate the creation of agent protocol files."
    )
    parser.add_argument(
        "--template",
        type=str,
        required=True,
        help="Path to the protocol template file.",
    )
    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="Path to the output protocol file.",
    )
    parser.add_argument(
        "--agent-name",
        type=str,
        required=True,
        help="The name of the agent.",
    )

    args = parser.parse_args()

    generate_protocol_file(args.template, args.output, args.agent_name)


if __name__ == "__main__":
    main()

print("Agent protocol automation template ready. Adapt and run as needed.")
