import os
import re
import shutil
from datetime import datetime
from pathlib import Path


def ensure_dir(path):
    """Create directory if it doesn't exist"""
    if not os.path.exists(path):
        os.makedirs(path)


def copy_template(template_path, dest_path, replacements=None):
    """Copy a template file and optionally replace placeholders"""
    with open(template_path, "r", encoding="utf-8") as f:
        content = f.read()

    if replacements:
        for key, value in replacements.items():
            content = content.replace(key, value)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(content)


def get_directories_needing_readme():
    """Find directories that should have README files"""
    important_dirs = []

    for root, dirs, files in os.walk("."):
        if any(
            exclude in root
            for exclude in [".git", "node_modules", "__pycache__", ".next"]
        ):
            continue

        if "README.md" not in files and (
            "/src/" in root
            or "/docs/" in root
            or "/tests/" in root
            or len([f for f in files if not f.startswith(".")]) > 0
        ):
            important_dirs.append(root)

    return important_dirs


def standardize_filenames(directory):
    """Standardize filenames to lowercase with hyphens"""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(
                exclude in root
                for exclude in [".git", "node_modules", "__pycache__", ".next"]
            ):
                continue

            # Convert spaces and underscores to hyphens, lowercase
            new_name = file.lower().replace(" ", "-").replace("_", "-")

            # Remove multiple hyphens
            new_name = re.sub(r"-+", "-", new_name)

            if new_name != file:
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, new_name)
                print(f"Renaming: {old_path} -> {new_path}")
                os.rename(old_path, new_path)


def add_frontmatter_to_docs():
    """Add frontmatter to markdown files that don't have it"""
    for root, _, files in os.walk("."):
        if any(
            exclude in root
            for exclude in [".git", "node_modules", "__pycache__", ".next"]
        ):
            continue

        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)

                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                if not content.startswith("---"):
                    # Extract title from first heading
                    title = file.replace(".md", "").replace("-", " ").title()
                    match = re.search(r"^#\s*(.+)$", content, re.MULTILINE)
                    if match:
                        title = match.group(1)

                    frontmatter = f"""---
title: {title}
version: 1.0.0
status: Draft
last_updated: {datetime.now().strftime('%Y-%m-%d')}
maintained_by: Project Team
tags: []
---

"""
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(frontmatter + content)
                        print(f"Added frontmatter to {file_path}")


def main():
    print("Starting project standardization...")

    # Copy templates to directories needing README
    readme_template = "docs/templates/readme_template.md"
    if os.path.exists(readme_template):
        for dir_path in get_directories_needing_readme():
            dest_path = os.path.join(dir_path, "README.md")
            if not os.path.exists(dest_path):
                print(f"Adding README to {dir_path}")
                copy_template(
                    readme_template,
                    dest_path,
                    {"[Directory Name]": os.path.basename(dir_path)},
                )

    # Standardize filenames
    print("\nStandardizing filenames...")
    standardize_filenames(".")

    # Add frontmatter to docs
    print("\nAdding frontmatter to documentation...")
    add_frontmatter_to_docs()

    print("\nStandardization complete!")


if __name__ == "__main__":
    main()
