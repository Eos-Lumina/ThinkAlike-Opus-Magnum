"""
Analyze the project structure by domain and list all files under each domain.
Generate a JSON map of domains and their files.
"""

import json
import os


def analyze_project_structure(root_dir):
    structure = {}
    for dirpath, dirs, files in os.walk(root_dir):
        # skip hidden folders
        parts = os.path.relpath(dirpath, root_dir).split(os.sep)
        domain = parts[0] if parts[0] not in (".", "") else "root"
        for f in files:
            structure.setdefault(domain, []).append(os.path.join(dirpath, f))
    return structure


if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    project_map = analyze_project_structure(root)
    # pretty print to console
    print(json.dumps(project_map, indent=2))
    # also save to file
    out_file = os.path.join(root, "structure_map.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(project_map, f, indent=2)
    print(f"Structure map written to {out_file}")
