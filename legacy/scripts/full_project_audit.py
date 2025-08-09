import argparse
import os
import sys
from pathlib import Path
from typing import List, Tuple

# Configurable: file extensions and keywords to flag
# Expanded list to catch more nuanced or project-specific terms.
FLAG_EXTENSIONS = {
    ".md",
    ".py",
    ".ts",
    ".tsx",
    ".js",
    ".json",
    ".yaml",
    ".yml",
    ".sh",
    ".bat",
    ".ps1",
    ".cfg",
    ".ini",
}
FLAG_KEYWORDS = {
    "archive",
    "legacy",
    "deprecated",
    "old",
    "backup",
    "stub",
    "draft",
    "harmonize",
    "in progress",
    "not canonical",
    "superseded",
    "duplicate",
    "fragmented",
    "orphan",
    "todo",
    "fixme",
    "hack",
    "xxx",
    "to be created",
    "unreferenced",
    "unlinked",
    "obsolete",
    "temp",
    "temporary",
}

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
}


def scan_files(root: Path) -> Tuple[List[str], List[Tuple[str, str, str]]]:
    """
    Scans all files in the project root for flagged keywords and extensions.

    Args:
        root: The root directory of the project.

    Returns:
        A tuple containing a list of all scanned file paths and a list of
        flagged items (path, type, keyword).
    """
    flagged_items = []
    all_files = []
    for dirpath, dirnames, filenames in os.walk(root, topdown=True):
        # Modify dirnames in-place to prune traversal
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]

        for fname in filenames:
            fpath = Path(dirpath) / fname
            try:
                rel_path = str(fpath.relative_to(root))
            except ValueError:
                rel_path = str(fpath)

            all_files.append(rel_path)

            # Flag based on filename
            for kw in FLAG_KEYWORDS:
                if kw in fname.lower():
                    flagged_items.append((rel_path, "filename", kw))

            # Flag based on content
            if fpath.suffix.lower() in FLAG_EXTENSIONS:
                try:
                    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                        # Read in chunks to handle large
                        # files
                        for i, line in enumerate(f, 1):
                            line_lower = line.lower()
                            for kw in FLAG_KEYWORDS:
                                if kw in line_lower:
                                    flagged_items.append(
                                        (
                                            rel_path,
                                            f"content (line {i})",
                                            kw,
                                        )
                                    )
                except Exception as e:
                    print(
                        f"Warning: Could not read file {rel_path}: {e}",
                        file=sys.stderr,
                    )
    return all_files, flagged_items


def generate_report(
    report_file: Path,
    all_files: List[str],
    flagged: List[Tuple[str, str, str]],
):
    """Generates a text report of the audit findings."""
    unique_flagged_files = sorted({item[0] for item in flagged})
    with open(report_file, "w", encoding="utf-8") as out:
        out.write("--- FULL PROJECT AUDIT REPORT ---\n\n")
        out.write(f"Total files scanned: {len(all_files)}\n")
        out.write(f"Flagged files (potential issues): {len(unique_flagged_files)}\n")
        out.write("\n--- FLAGGED ITEMS ---\n")

        if not flagged:
            out.write("No issues found.\n")
        else:
            # Group flags by file
            flags_by_file = {}
            for rel_path, flag_type, kw in flagged:
                if rel_path not in flags_by_file:
                    flags_by_file[rel_path] = []
                flags_by_file[rel_path].append(f"- {flag_type}: '{kw}'")

            for rel_path in unique_flagged_files:
                out.write(f"\n[FILE] {rel_path}\n")
                for flag in flags_by_file[rel_path]:
                    out.write(f"  {flag}\n")

        out.write("\n--- END OF REPORT ---\n")


def main():
    """Main function to run the audit and generate the report."""
    parser = argparse.ArgumentParser(
        description="Perform a full audit of the project for potentially "
        "problematic files and content."
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
        default="full_project_audit_report.txt",
        help="The path to save the audit report.",
    )
    args = parser.parse_args()

    print(f"Starting audit in directory: {args.root.resolve()}")
    all_files, flagged = scan_files(args.root)
    generate_report(args.report_file, all_files, flagged)
    print(f"✅ Audit complete. See {args.report_file.resolve()}")


if __name__ == "__main__":
    main()
