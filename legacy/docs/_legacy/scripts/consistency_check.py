"""
Script: consistency_check.py
Purpose: Run basic consistency checks for TODOs, stubs, drafts, and broken
         links in the ThinkAlike project.
"""

import os
import re

import yaml

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATTERNS = [
    r"TODO",
    r"Draft",
    r"to be created",
    r"missing",
    r"stub",
    r"placeholder",
    r"broken link",
]

# List of deprecated folders/files that must NOT exist
DEPRECATED_PATHS = [
    "docs/guides/contributor_guides/",
    "docs/project/archive/testing_and_validation_plan.md",
    "docs/project/archive/testing_and_validation_plan_tests.md",
]


def scan_files():
    results = []
    for dirpath, _, filenames in os.walk(ROOT_DIR):
        for fname in filenames:
            if fname.endswith((".md", ".py", ".js", ".ts", ".tsx", ".jsx")):
                fpath = os.path.join(dirpath, fname)
                try:
                    with open(fpath, encoding="utf-8") as f:
                        for i, line in enumerate(f, 1):
                            for pat in PATTERNS:
                                if re.search(pat, line, re.IGNORECASE):
                                    results.append(f"{fpath}:{i}: {line.strip()}")
                except Exception:
                    # Ignore files that can't be opened
                    pass
    return results


def check_consistency(manifest_path):
    """Checks the consistency of the project structure."""
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)

    required_dirs = manifest.get("required_directories", [])
    required_files = manifest.get("required_files", [])

    missing_dirs = [d for d in required_dirs if not os.path.isdir(d)]
    missing_files = [f for f in required_files if not os.path.isfile(f)]

    if missing_dirs:
        print("Missing required directories:")
        for d in missing_dirs:
            print(f"  - {d}")

    if missing_files:
        print("Missing required files:")
        for f in missing_files:
            print(f"  - {f}")

    if not missing_dirs and not missing_files:
        print("Project structure is consistent with the manifest.")
    else:
        exit(1)


def check_deprecated_paths():
    # Check for deprecated folders/files
    deprecated_found = []
    for path in DEPRECATED_PATHS:
        if os.path.exists(path):
            deprecated_found.append(path)
    if deprecated_found:
        print(
            "WARNING: Deprecated folders/files detected! "
            "Please remove the following:"
        )
        for p in deprecated_found:
            print(f"  {p}")
    else:
        print("No deprecated folders/files found.")


def main():
    check_deprecated_paths()

    results = scan_files()
    if results:
        print("Potential TODOs, stubs, or broken links found:")
        for r in results:
            print(r)
    else:
        print("No outstanding TODOs, stubs, or broken links found.")

    check_consistency("project_manifest.yaml")


if __name__ == "__main__":
    main()
