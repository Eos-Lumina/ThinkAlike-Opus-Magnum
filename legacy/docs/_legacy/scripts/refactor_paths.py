"""
Script to refactor imports and links across the project based on canonical path mappings.
Reads `canonical_paths.yaml` and updates all .ts, .py, and .md files under project root,
excluding `legacy/`.
"""

import os
import re

import yaml

# Extensions to process
EXTENSIONS = (".ts", ".tsx", ".js", ".jsx", ".py", ".md")


def load_mappings(path="canonical_paths.yaml"):
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    # Normalize keys and values to use forward slashes
    mappings = {k.rstrip("/") + "/": v.rstrip("/") + "/" for k, v in data.items()}
    return mappings


def should_process_file(filepath):
    # Skip legacy folder
    if os.path.normpath("legacy") in filepath.replace("\\", os.sep):
        return False
    return filepath.endswith(EXTENSIONS)


def refactor_file(filepath, mappings):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    original = text
    for old_pref, new_pref in mappings.items():
        # Escape for regex, replace any occurrence of old path
        pattern = re.escape(old_pref)
        text = re.sub(pattern, new_pref, text)

    if text != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)
        return True
    return False


def main():
    mappings = load_mappings()
    moved = []
    for root, dirs, files in os.walk(os.getcwd()):
        # skip legacy folder
        if "legacy" in root.split(os.sep):
            continue
        for name in files:
            path = os.path.join(root, name)
            if should_process_file(path):
                changed = refactor_file(path, mappings)
                if changed:
                    moved.append(path)
    # Report
    print(f"Refactored {len(moved)} files based on canonical_paths.yaml")
    for p in moved:
        print(f"Updated: {p}")


if __name__ == "__main__":
    main()
