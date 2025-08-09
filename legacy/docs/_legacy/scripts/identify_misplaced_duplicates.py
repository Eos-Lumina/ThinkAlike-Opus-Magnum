"""
Script to identify misplaced, duplicated, or unmanifested files and folders.

This script performs several checks:
1.  **Content-based Duplicates**: Finds files with identical content,
    regardless of their name or location, by comparing file hashes.
2.  **Name-based Duplicates**: Finds files that have the same name but exist in
    different locations.
3.  **Unmanifested Files**: If a project manifest is provided, it identifies
    files that exist in the project but are not listed in the manifest.

The results are saved to a markdown report.
"""

import argparse
import hashlib
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

import yaml

# Directories to exclude from the scan
EXCLUDE_DIRS = {
    ".git",
    ".vscode",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
    "venv",
    ".venv",
    ".next",
    "vaults",
    "archive_legacy",
}


def get_all_files(root: Path) -> List[Path]:
    """Get a list of all files in the directory, excluding specified folders."""
    all_files = []
    for p in root.rglob("*"):
        if any(part in EXCLUDE_DIRS for part in p.parts):
            continue
        if p.is_file():
            all_files.append(p)
    return all_files


def find_content_duplicates(files: List[Path], root: Path) -> Dict[str, List[str]]:
    """Finds files with duplicate content by hashing them."""
    hashes = defaultdict(list)
    for file_path in files:
        try:
            with open(file_path, "rb") as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
                hashes[file_hash].append(str(file_path.relative_to(root)))
        except IOError as e:
            print(
                f"Warning: Could not read file {file_path}: {e}",
                file=sys.stderr,
            )
    return {hash_val: paths for hash_val, paths in hashes.items() if len(paths) > 1}


def find_name_duplicates(files: List[Path], root: Path) -> Dict[str, List[str]]:
    """Finds files with the same name in different locations."""
    names = defaultdict(list)
    for file_path in files:
        names[file_path.name].append(str(file_path.relative_to(root)))

    return {name: paths for name, paths in names.items() if len(paths) > 1}


def find_unmanifested_files(
    files: List[Path], manifest_path: Path, root: Path
) -> List[str]:
    """Finds files not listed in the project manifest."""
    if not manifest_path or not manifest_path.exists():
        return []

    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = yaml.safe_load(f)
            if "canonical_paths" not in manifest:
                print(
                    "Warning: 'canonical_paths' key not found in " f"{manifest_path}",
                    file=sys.stderr,
                )
                return []
            canonical_paths = set(manifest["canonical_paths"])
    except yaml.YAMLError as e:
        print(
            f"Warning: Could not parse manifest {manifest_path}: {e}",
            file=sys.stderr,
        )
        return []
    except IOError as e:
        print(
            f"Warning: Could not read manifest {manifest_path}: {e}",
            file=sys.stderr,
        )
        return []

    project_files = {str(p.relative_to(root).as_posix()) for p in files}
    unmanifested = project_files - canonical_paths
    return sorted(list(unmanifested))


def generate_report(
    report_path: Path,
    content_duplicates: Dict[str, List[str]],
    name_duplicates: Dict[str, List[str]],
    unmanifested_files: List[str],
):
    """Generates a markdown report of the findings."""
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# Misplaced and Duplicate File Report\n\n")

        if content_duplicates:
            f.write("## 1. Files with Duplicate Content\n\n")
            f.write(
                "Files with the same content hash, "
                "indicating they are identical.\n\n"
            )
            for file_hash, paths in sorted(content_duplicates.items()):
                f.write(f"**Hash:** `{file_hash}`\n")
                for path in sorted(paths):
                    f.write(f"- `{path}`\n")
                f.write("\n")
        else:
            f.write(
                "## 1. Files with Duplicate Content\n\n"
                "No content duplicates found.\n\n"
            )

        if name_duplicates:
            f.write("## 2. Files with Duplicate Names\n\n")
            f.write("Files with the same name found in multiple locations.\n\n")
            for name, paths in sorted(name_duplicates.items()):
                f.write(f"**Filename:** `{name}`\n")
                for path in sorted(paths):
                    f.write(f"- `{path}`\n")
                f.write("\n")
        else:
            f.write(
                "## 2. Files with Duplicate Names\n\n"
                "No files with duplicate names found.\n\n"
            )

        if unmanifested_files:
            f.write("## 3. Unmanifested Files\n\n")
            f.write(
                "Files found in the project that are not listed in the "
                "canonical manifest.\n\n"
            )
            for path in unmanifested_files:
                f.write(f"- `{path}`\n")
            f.write("\n")
        else:
            f.write("## 3. Unmanifested Files\n\nNo unmanifested files found.\n\n")

        f.write(
            "---\n*Report generated by " "`scripts/identify_misplaced_duplicates.py`*\n"
        )


def main():
    """Main function to run the script."""
    parser = argparse.ArgumentParser(
        description="Identify misplaced, duplicated, or unmanifested files "
        "and folders."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).parent.parent,
        help="The root directory of the project to scan.",
    )
    parser.add_argument(
        "--report-file",
        type=Path,
        default=Path(__file__).parent / "misplaced_duplicates.md",
        help="The path to save the audit report.",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        help="Optional path to a project manifest YAML file with a "
        "'canonical_paths' key.",
    )
    args = parser.parse_args()

    print(f"Starting scan in: {args.root.resolve()}")
    all_files = get_all_files(args.root)

    print("Finding files with duplicate content...")
    content_dupes = find_content_duplicates(all_files, args.root)

    print("Finding files with duplicate names...")
    name_dupes = find_name_duplicates(all_files, args.root)

    unmanifested = []
    if args.manifest:
        print(f"Comparing against manifest: {args.manifest.resolve()}")
        unmanifested = find_unmanifested_files(all_files, args.manifest, args.root)

    print(f"Generating report at: {args.report_file.resolve()}")
    generate_report(args.report_file, content_dupes, name_dupes, unmanifested)

    print("✅ Scan complete.")


if __name__ == "__main__":
    main()
