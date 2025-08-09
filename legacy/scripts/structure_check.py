import argparse
import os
import re
import sys
from collections import defaultdict
from typing import Dict, List, Optional, Set

import yaml

# Canonical domains as per harmonization plan
CANONICAL_DOMAINS = {
    "ui_components": "docs/ui_components/",
    "onboarding": "docs/onboarding/",
    "contributors": "docs/contributors/",
    "protocols": "docs/protocols/",
    "style": "docs/style/",
    "templates": "docs/templates/",
    "data": "data/",
    "assets": "assets/",
    "scripts": "scripts/",
}

CANONICAL_FOLDERS = set(CANONICAL_DOMAINS.values())

# File index to scan
PROJECT_FILE_INDEX = "PROJECT_FILE_INDEX.md"

# Domains to check for duplicates/ambiguity
AMBIGUOUS_KEYWORDS = [
    "onboarding",
    "contributor",
    "ui_component",
    "protocol",
    "style",
    "template",
]

# List of deprecated folders/files that must NOT exist
DEPRECATED_PATHS = [
    "docs/guides/contributor_guides/",
    "docs/project/archive/testing_and_validation_plan.md",
    "docs/project/archive/testing_and_validation_plan_tests.md",
]

# Canonical sources of truth - there can be only ONE of each
CANONICAL_SOURCES = {
    "source_of_truth": "docs/source_of_truth.md",
    "system_blueprint": "SYSTEM_BLUEPRINT.md",
    "project_manifest": "project_manifest.yaml",
    "archive": "docs/archive/",  # The ONE archive location
}

# Additional anti-fragmentation rules
FORBIDDEN_PATTERNS = [
    r".*_archive.*",  # No custom archive folders
    r".*source.*of.*truth.*",  # No additional source of truth files
    r".*blueprint.*copy.*",  # No blueprint copies
    r".*_backup.*",  # No backup folders
    r".*/archive/.*archive/.*",  # No nested archives
    r".*_duplicate.*",  # No duplicate indicators
    r".*_old.*",  # No old version markers
    r".*_new.*",  # No new version markers
    r".*_v\d+.*",  # No version numbers in filenames
    r".*_draft.*",  # No draft files (use git branches instead)
]


def is_canonical(path: str) -> bool:
    """Check if a path is in a canonical location."""
    normalized_path = path.replace("\\", "/")
    for folder in CANONICAL_FOLDERS:
        if normalized_path.startswith(folder):
            return True
    return False


def find_duplicate_sources(root_dir: str) -> List[str]:
    """Find any duplicate sources of truth."""
    issues = []
    found_sources = defaultdict(list)

    for root, _, files in os.walk(root_dir):
        for file in files:
            filepath = os.path.join(root, file).replace("\\", "/")
            # Check for duplicates of canonical sources
            for source_type, canonical_path in CANONICAL_SOURCES.items():
                if canonical_path != filepath and (
                    source_type.lower() in filepath.lower()
                    or source_type.replace("_", "").lower() in filepath.lower()
                ):
                    issues.append(
                        f"Potential duplicate source of truth found: {filepath} (should be in {canonical_path})"
                    )
    return issues


def check_structure(manifest_path: str, root_dir: str) -> List[str]:
    """Checks the project structure against a manifest."""
    issues = []
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)

    expected_dirs = manifest.get("directories", [])
    expected_files = manifest.get("files", [])

    for d in expected_dirs:
        if not os.path.isdir(os.path.join(root_dir, d)):
            issues.append(f"Missing directory: {d}")

    for f in expected_files:
        if not os.path.isfile(os.path.join(root_dir, f)):
            issues.append(f"Missing file: {f}")

    return issues


def check_fragmentation(root_dir: str) -> List[str]:
    """Check for project fragmentation issues."""
    issues = []

    # Check for forbidden patterns
    for pattern in FORBIDDEN_PATTERNS:
        for root, dirs, files in os.walk(root_dir):
            for item in dirs + files:
                if re.match(pattern, item.lower()):
                    if root.replace("\\", "/") != CANONICAL_SOURCES["archive"]:
                        issues.append(
                            f"Fragmentation detected: {os.path.join(root, item)} matches forbidden pattern {pattern}"
                        )

    # Check for deprecated paths
    for path in DEPRECATED_PATHS:
        full_path = os.path.join(root_dir, path)
        if os.path.exists(full_path):
            issues.append(f"Deprecated path still exists: {path}")

    # Check for duplicate sources of truth
    issues.extend(find_duplicate_sources(root_dir))

    # Check for non-canonical locations of domain-specific content
    for root, _, files in os.walk(root_dir):
        for file in files:
            filepath = os.path.join(root, file)
            for keyword in AMBIGUOUS_KEYWORDS:
                if keyword in filepath.lower() and not is_canonical(filepath):
                    issues.append(
                        f"Content found in non-canonical location: {filepath} contains '{keyword}'"
                    )

    return issues


def load_manifest(manifest_path: str) -> dict:
    """Load and validate the project manifest."""
    with open(manifest_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_allowed_root_files(manifest: dict) -> Set[str]:
    """Get the set of files allowed in the root directory."""
    return set(manifest.get("root_files", []))


def check_root_files(root_dir: str, manifest: dict) -> List[str]:
    """Check that only allowed files are in the root directory."""
    issues = []
    allowed_files = get_allowed_root_files(manifest)

    # Add some common development files that are always allowed
    allowed_files.update(
        {
            ".git",
            ".gitignore",
            ".pre_commit_config.yaml",
            "package_lock.json",
            "yarn.lock",
        }
    )

    root_contents = os.listdir(root_dir)
    for item in root_contents:
        if os.path.isfile(os.path.join(root_dir, item)):
            if item not in allowed_files:
                issues.append(f"File '{item}' is not allowed in root directory")

    return issues


def check_file_naming(filepath: str, manifest: dict) -> List[str]:
    """Check if file follows naming conventions from manifest."""
    issues = []
    filename = os.path.basename(filepath)

    # Get naming conventions from manifest
    conventions = manifest.get("naming_conventions", {})

    # Check each convention
    for conv_name, conv in conventions.items():
        pattern = conv.get("pattern")
        if pattern and re.match(pattern, filename):
            return []  # File matches a valid convention

    # If we get here, file doesn't match any convention
    issues.append(f"File '{filename}' doesn't follow naming conventions")
    return issues


def check_file_location(filepath: str, manifest: dict) -> List[str]:
    """Check if a file is in its canonical location."""
    issues = []
    for domain, path in CANONICAL_DOMAINS.items():
        if domain.lower() in filepath.lower():
            relpath = os.path.relpath(filepath, start=path)
            if not filepath.startswith(path):
                issues.append(
                    f"File {filepath} contains '{domain}' but is not in canonical location {path}"
                )
    return issues


def validate_file_structure(root_dir: str) -> bool:
    """Run all structure validations and return True if all pass."""
    manifest_path = os.path.join(root_dir, "project_manifest.yaml")

    all_issues = []

    # Check basic structure against manifest
    if os.path.exists(manifest_path):
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = yaml.safe_load(f)
        all_issues.extend(check_structure(manifest_path, root_dir))

        # Check each file's location
        for root, _, files in os.walk(root_dir):
            for file in files:
                filepath = os.path.join(root, file)
                all_issues.extend(check_file_location(filepath, manifest))

    # Check for fragmentation issues
    all_issues.extend(check_fragmentation(root_dir))

    # Report all issues
    if all_issues:
        print("Structure validation failed!")
        for issue in all_issues:
            print(f"- {issue}")
        return False

    print("Structure validation passed.")
    return True


def main():
    parser = argparse.ArgumentParser(description="Validate project structure")
    parser.add_argument("--root", default=".", help="Root directory to check")
    args = parser.parse_args()

    success = validate_file_structure(args.root)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
