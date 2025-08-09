#!/usr/bin/env python3
"""
Global Naming Convention Enforcer
Renames files containing hyphens to underscores and updates references.
"""
import os
import re
from pathlib import Path

# File extensions to process
EXTENSIONS = [".py", ".md", ".ts", ".tsx", ".json", ".yaml", ".yml"]


def rename_file(src_path: Path):
    new_name = src_path.name.replace("-", "_")
    dest_path = src_path.with_name(new_name)
    if dest_path.exists():
        # If destination exists, skip or merge
        print(f"Skipping {src_path}: target exists {dest_path}")
    else:
        print(f"Renaming {src_path} -> {dest_path}")
        src_path.rename(dest_path)
    return dest_path


def update_references(root: Path, old_name: str, new_name: str):
    pattern = re.compile(re.escape(old_name))
    for file in root.rglob("*"):
        if file.suffix in EXTENSIONS:
            text = file.read_text(encoding="utf-8")
            if old_name in text:
                new_text = pattern.sub(new_name, text)
                print(f"Updating references in {file}")
                file.write_text(new_text, encoding="utf-8")


if __name__ == "__main__":
    root = Path(__file__).parent.parent
    # First pass: collect files with hyphens
    for file in root.rglob("*"):
        if file.is_file() and "-" in file.name:
            dest = rename_file(file)
            old = file.name
            new = dest.name
            # Update references project-wide
            update_references(root, old, new)
    print("Naming convention enforcement complete.")
