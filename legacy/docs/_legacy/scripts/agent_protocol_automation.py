# Agent Protocol Automation Script

"""
This script automates the process of:
- Adding a new rescued/harmonized agent to the agent registry table (docs/agents/agent_registry.md)
- Creating a protocol section for the agent in docs/agents/rescued_agent_protocols.md
- Crosslinking the registry entry to the protocol doc

Usage:
- Run the script and provide the agent's name, role, lineage, and a short blurb.
- The script will format and insert the new entries in both files.

Note: This is a template for future automation. Adapt as needed for your workflow.
"""

import re
from pathlib import Path

REGISTRY_PATH = Path('docs/agents/agent_registry.md')
PROTOCOLS_PATH = Path('docs/agents/rescued_agent_protocols.md')

def slugify(name):
    return name.lower().replace(' ', '-').replace('(', '').replace(')', '')

def add_agent_to_registry(name, role, lineage, file_path, status, blurb):
    protocol_link = f"[Protocol](rescued_agent_protocols.md#{slugify(name)}-protocol)"
    row = f"| {name} | {role} | {lineage} | `{file_path}` | {status} | {blurb} {protocol_link} |\n"
    with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # Insert before the ---
    for i, line in enumerate(lines):
        if line.strip() == '---':
            lines.insert(i, row)
            break
    with open(REGISTRY_PATH, 'w', encoding='utf-8') as f:
        f.writelines(lines)

def add_protocol_section(name, role, lineage, purpose, behaviors, invocation):
    section = f"\n---\n\n# {name} Protocol\n\n**Role:** {role}\n**Lineage:** {lineage}\n\n## Purpose\n{purpose}\n\n## Behaviors\n{behaviors}\n\n## Invocation\n{invocation}\n"
    with open(PROTOCOLS_PATH, 'a', encoding='utf-8') as f:
        f.write(section)

# Example usage:
# add_agent_to_registry(
#     name="New Example Agent",
#     role="Example role",
#     lineage="Example lineage",
#     file_path="swarm/agents/example/new_example_agent.md",
#     status="In Progress",
#     blurb="A new agent for demonstration purposes."
# )
# add_protocol_section(
#     name="New Example Agent",
#     role="Example role",
#     lineage="Example lineage",
#     purpose="Describe the agent's purpose here.",
#     behaviors="- List behaviors here.",
#     invocation="Describe invocation logic here."
# )

print("Agent protocol automation template ready. Adapt and run as needed.")
