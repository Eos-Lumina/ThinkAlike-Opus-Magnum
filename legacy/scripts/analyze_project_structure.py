import os
import re
from pathlib import Path

import yaml


def load_manifest():
    """Load the project manifest to understand canonical structure"""
    manifest_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "project_manifest.yaml"
    )
    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except:
        return {}


def is_binary(file_path):
    """Check if a file is binary"""
    try:
        with open(file_path, "tr") as f:
            f.read()
            return False
    except:
        return True


def analyze_file(file_path):
    """Analyze a single file for issues"""
    issues = []

    # Skip binary files
    if is_binary(file_path):
        return issues

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Check for empty files
        if not content.strip():
            issues.append(f"Empty file: {file_path}")
            return issues

        # Check markdown files for frontmatter
        if file_path.endswith(".md"):
            if not re.match(r"^---\n.*?\n---", content, re.DOTALL):
                issues.append(f"Missing frontmatter: {file_path}")

        # Check for TODO comments
        if "TODO" in content or "FIXME" in content:
            issues.append(f"Contains TODO/FIXME: {file_path}")

        # Check for potentially outdated dates
        date_pattern = r"\b202[0-4]\b"
        if re.search(date_pattern, content):
            issues.append(f"Contains potentially outdated dates: {file_path}")

    except Exception as e:
        issues.append(f"Error analyzing {file_path}: {str(e)}")

    return issues


def find_orphaned_files():
    """Find files that don't match the canonical structure"""
    manifest = load_manifest()
    issues = []

    # Standard directories that should have README files
    standard_dirs = {
        "src",
        "docs",
        "tests",
        "scripts",
        "assets",
    }

    # Walk through all directories
    for root, dirs, files in os.walk("."):
        # Skip node_modules and other standard excludes
        if any(
            exclude in root
            for exclude in [".git", "node_modules", "__pycache__", ".next"]
        ):
            continue

        # Check for missing README
        if any(root.endswith(d) for d in standard_dirs) and "README.md" not in files:
            issues.append(f"Missing README: {root}")

        # Check each file
        for file in files:
            file_path = os.path.join(root, file)

            # Analyze file content
            issues.extend(analyze_file(file_path))

            # Check naming conventions
            if not re.match(r"^[a-z0-9_.-]+$", file.lower()):
                issues.append(f"Non-standard file name: {file_path}")

    return issues


def main():
    print("Analyzing project structure...")
    issues = find_orphaned_files()

    if issues:
        print("\nFound issues:")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("\nNo issues found.")

    # Create report
    with open("structure_analysis_report.md", "w", encoding="utf-8") as f:
        f.write("# Project Structure Analysis Report\n\n")
        f.write(f"Generated: {os.path.basename(__file__)}\n\n")

        if issues:
            f.write("## Issues Found\n\n")
            for issue in issues:
                f.write(f"- {issue}\n")
        else:
            f.write("No issues found.\n")


if __name__ == "__main__":
    main()
