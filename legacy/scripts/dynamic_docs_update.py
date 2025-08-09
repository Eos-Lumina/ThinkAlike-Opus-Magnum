"""
Dynamic Documentation Updater for ThinkAlike

This script updates README.md, whitepaper_blueprint.md, and foundational docs by extracting up-to-date information from project files (modules, roadmap, matrix, etc.) and injecting it into markdown templates.

- Define dynamic regions in markdown files using special comments, e.g.:
  <!-- DYNAMIC:MODULE_LIST_START --> ... <!-- DYNAMIC:MODULE_LIST_END -->
- The script will replace only these regions with generated content.
- Add new dynamic regions as needed (features, roadmap, agent list, etc.).

Usage:
  python scripts/dynamic_docs_update.py

Requirements:
  - Python 3.8+
"""
import os
import re
import json
from pathlib import Path

# --- Configurable paths and regions ---
PROJECT_ROOT = Path(__file__).parent.parent
DOCS = PROJECT_ROOT / "docs"
README = PROJECT_ROOT / "README.md"
WHITEPAPER = DOCS / "seed" / "core" / "whitepaper_blueprint.md"
MATRIX = DOCS / "project_status_and_matrix.md"

DYNAMIC_REGIONS = {
    "module_list": ("<!-- DYNAMIC:MODULE_LIST_START -->", "<!-- DYNAMIC:MODULE_LIST_END -->"),
    "roadmap": ("<!-- DYNAMIC:ROADMAP_START -->", "<!-- DYNAMIC:ROADMAP_END -->"),
    "agent_list": ("<!-- DYNAMIC:AGENT_LIST_START -->", "<!-- DYNAMIC:AGENT_LIST_END -->"),
    "research_foundations": ("<!-- DYNAMIC:RESEARCH_FOUNDATIONS_START -->", "<!-- DYNAMIC:RESEARCH_FOUNDATIONS_END -->"),
    "innovations_table": ("<!-- DYNAMIC:INNOVATIONS_TABLE_START -->", "<!-- DYNAMIC:INNOVATIONS_TABLE_END -->"),
    "metrics": ("<!-- DYNAMIC:METRICS_START -->", "<!-- DYNAMIC:METRICS_END -->"),
    "document_index": ("<!-- DYNAMIC:DOCUMENT_INDEX_START -->", "<!-- DYNAMIC:DOCUMENT_INDEX_END -->"),
    "noetica_index": ("<!-- DYNAMIC:NOETICA_INDEX_START -->", "<!-- DYNAMIC:NOETICA_INDEX_END -->"),
    # Add more as needed
}

SOURCE_OF_TRUTH = DOCS / "seed" / "core" / "dynamic_source_of_truth.json"

def load_source_of_truth():
    if not SOURCE_OF_TRUTH.exists():
        return {"modules": [], "roadmap": [], "agents": [], "research_foundations": []}
    with open(SOURCE_OF_TRUTH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_source_of_truth(data):
    with open(SOURCE_OF_TRUTH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def update_source_of_truth():
    """If any section is empty, auto-populate from project structure."""
    data = load_source_of_truth()
    changed = False
    # Modules
    if not data["modules"]:
        realms_dir = DOCS / "realms"
        if realms_dir.exists():
            modules = [f.name.replace('_', ' ').title() for f in realms_dir.iterdir() if f.is_dir()]
            modules.sort()
            data["modules"] = modules
            changed = True
    # Roadmap
    if not data["roadmap"]:
        roadmap_file = DOCS / "seed" / "planning" / "emergent_roadmap.md"
        if roadmap_file.exists():
            lines = roadmap_file.read_text(encoding="utf-8").splitlines()
            roadmap = [l.strip('- ').strip() for l in lines if l.strip().startswith('- ')]
            data["roadmap"] = roadmap
            changed = True
    # Agents
    if not data["agents"]:
        agents_dir = DOCS / "agents"
        if agents_dir.exists():
            agents = [f.stem.replace('_', ' ').title() for f in agents_dir.glob("*.md")]
            agents.sort()
            data["agents"] = agents
            changed = True
    # Research Foundations
    if not data["research_foundations"]:
        whitepaper_lines = WHITEPAPER.read_text(encoding="utf-8").splitlines()
        rf_start = None
        rf_end = None
        for i, line in enumerate(whitepaper_lines):
            if line.strip().startswith("### 10. Research Foundations"):
                rf_start = i + 1
            elif rf_start and (line.strip().startswith("### ") or line.strip() == "---"):
                rf_end = i
                break
        if rf_start is not None:
            rf_lines = whitepaper_lines[rf_start:rf_end] if rf_end else whitepaper_lines[rf_start:]
            rf_lines = [l for l in rf_lines if l.strip() and not l.strip().startswith("<!--")]  # skip comments
            data["research_foundations"] = [l.strip('- ').strip() for l in rf_lines]
            changed = True
    # Innovations Table
    if "innovations_table" not in data:
        data["innovations_table"] = [
            {"Innovation": "Resonance Algorithm", "Description": "Matches users based on deep value alignment rather than superficial traits", "Technical Implementation": "Neural resonance network with symbolic vector embedding"},
            {"Innovation": "Fork-Based Narrative", "Description": "User choices create a unique path that reveals authentic values", "Technical Implementation": "Decision tree with ethical weighting and resonance scoring"},
            {"Innovation": "DataTraceability", "Description": "Users maintain sovereignty over their data and its usage", "Technical Implementation": "Blockchain-inspired verification system with user control panel"},
            {"Innovation": "Model Context Protocol (MCP)", "Description": "Ensures all context flows are transparent, auditable, and user-controlled", "Technical Implementation": "Canonical context objects, audit trails, agent roles, and sovereignty controls; MCP Context Manager UI for user empowerment"},
            {"Innovation": "Swarm Intelligence", "Description": "Distributed agent system that ensures ethical alignment", "Technical Implementation": "Multi-agent architecture with mutual supervision protocols"},
            {"Innovation": "Chrona Currency", "Description": "Time-based value exchange that resists exploitation", "Technical Implementation": "Non-fungible token system with decay mechanisms and regenerative properties"}
        ]
        changed = True
    # Metrics
    if "metrics" not in data:
        data["metrics"] = [
            "User resonance satisfaction: Target 85%+ (vs. 32% on conventional platforms)",
            "Data sovereignty index: Target 100% user control",
            "Ethical alignment score: Minimum 90% for all system operations",
            "Governance participation: Target 40% of active users",
            "Value distribution: 70% to users, 20% to development, 10% to governance"
        ]
        changed = True
    if changed:
        save_source_of_truth(data)
    return data

def extract_modules():
    data = update_source_of_truth()
    return '\n'.join(f"- {m}" for m in data["modules"])

def extract_roadmap():
    data = update_source_of_truth()
    return '\n'.join(f"- {r}" for r in data["roadmap"])

def extract_agents():
    data = update_source_of_truth()
    return '\n'.join(f"- {a}" for a in data["agents"])

def extract_research_foundations():
    data = update_source_of_truth()
    return '\n'.join(f"- {rf}" for rf in data["research_foundations"])

def extract_innovations_table():
    data = update_source_of_truth()
    rows = data["innovations_table"]
    header = "| Innovation | Description | Technical Implementation |"
    sep = "|------------|-------------|--------------------------|"
    table = [header, sep]
    for row in rows:
        table.append(f"| {row['Innovation']} | {row['Description']} | {row['Technical Implementation']} |")
    return '\n'.join(table)

def extract_metrics():
    data = update_source_of_truth()
    return '\n'.join(f"- {m}" for m in data["metrics"])

def extract_folder_index(folder_path, rel_to=None, skip_files=None):
    """Generate a markdown index of all .md files and subfolders in a folder."""
    if skip_files is None:
        skip_files = set()
    lines = []
    for item in sorted(folder_path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower())):
        if item.name.startswith('.') or item.name in skip_files:
            continue
        if item.is_dir():
            lines.append(f"- **{item.name}/**")
            # Optionally, list .md files in subfolder (one level deep)
            submds = [f for f in item.glob("*.md") if not f.name.startswith('.')]
            for f in sorted(submds, key=lambda x: x.name.lower()):
                rel = f.relative_to(rel_to) if rel_to else f
                lines.append(f"  - [{f.name}]({rel.as_posix()})")
        elif item.suffix == ".md":
            rel = item.relative_to(rel_to) if rel_to else item
            lines.append(f"- [{item.name}]({rel.as_posix()})")
    return '\n'.join(lines)

def extract_document_index():
    return extract_folder_index(DOCS, rel_to=DOCS, skip_files={"README.md"})

def extract_noetica_index():
    noetica_dir = DOCS / "noetica"
    return extract_folder_index(noetica_dir, rel_to=DOCS / "noetica", skip_files={"README.md"})

def update_dynamic_region(md_path, region_key, new_content):
    """Replace the content between region markers in a markdown file."""
    start, end = DYNAMIC_REGIONS[region_key]
    text = md_path.read_text(encoding="utf-8")
    pattern = re.compile(f"{re.escape(start)}.*?{re.escape(end)}", re.DOTALL)
    replacement = f"{start}\n{new_content}\n{end}"
    if pattern.search(text):
        text = pattern.sub(replacement, text)
    else:
        # Insert at end if not found
        text += f"\n\n{replacement}\n"
    md_path.write_text(text, encoding="utf-8")
    print(f"Updated {region_key} in {md_path}")

def main():
    # Update module list in README and whitepaper
    modules_md = extract_modules()
    update_dynamic_region(README, "module_list", modules_md)
    update_dynamic_region(WHITEPAPER, "module_list", modules_md)
    # Update roadmap in README and whitepaper
    roadmap_md = extract_roadmap()
    update_dynamic_region(README, "roadmap", roadmap_md)
    update_dynamic_region(WHITEPAPER, "roadmap", roadmap_md)
    # Update agent list in whitepaper
    agents_md = extract_agents()
    update_dynamic_region(WHITEPAPER, "agent_list", agents_md)
    # Update research foundations in whitepaper
    rf_md = extract_research_foundations()
    update_dynamic_region(WHITEPAPER, "research_foundations", rf_md)
    # Update innovations table in whitepaper
    innovations_md = extract_innovations_table()
    update_dynamic_region(WHITEPAPER, "innovations_table", innovations_md)
    # Update metrics in whitepaper
    metrics_md = extract_metrics()
    update_dynamic_region(WHITEPAPER, "metrics", metrics_md)
    # Update document index in docs/README.md
    doc_index_md = extract_document_index()
    update_dynamic_region(DOCS / "README.md", "document_index", doc_index_md)
    # Update noetica index in docs/noetica/README.md
    noetica_index_md = extract_noetica_index()
    update_dynamic_region(DOCS / "noetica" / "README.md", "noetica_index", noetica_index_md)
    # Add more dynamic updates as needed

if __name__ == "__main__":
    main()
