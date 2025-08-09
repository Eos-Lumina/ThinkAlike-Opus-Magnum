"""
Script to consolidate project structure according to canonical path mappings.
Reads `canonical_paths.yaml` for prefix mappings, moves files accordingly,
preserves content, and logs operations.
"""

import os
import shutil

import yaml

REPORT_FILE = "scripts/consolidate_report.md"
MAPPINGS_FILE = "canonical_paths.yaml"
INDEX_FILE = "PROJECT_FILE_INDEX.md"


def load_mappings(path):
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    # Normalize keys and values
    mappings = {f"{k.rstrip('/')}/": f"{v.rstrip('/')}/" for k, v in data.items()}
    return mappings


def main():
    # Load canonical mappings
    if not os.path.exists(MAPPINGS_FILE):
        print(f"ERROR: {MAPPINGS_FILE} not found. " "Please populate it with mappings.")
        return
    mappings = load_mappings(MAPPINGS_FILE)

    # Generate file index
    if not os.path.exists(INDEX_FILE):
        print(f"ERROR: {INDEX_FILE} not found. " "Run generate_file_lists.py first.")
        return
    with open(INDEX_FILE, encoding="utf-8") as f:
        paths = [line.strip() for line in f if line.strip()]

    operations = []
    for path in paths:
        normalized = path.replace("\\", "/")
        for old_pref, new_pref in mappings.items():
            if normalized.startswith(old_pref):
                rel_path = normalized[len(old_pref) :]  # noqa: E203
                src = os.path.join(os.getcwd(), normalized)
                dst = os.path.join(os.getcwd(), new_pref, rel_path)
                operations.append((src, dst))
                break

    # Perform moves
    with open(REPORT_FILE, "w", encoding="utf-8") as report:
        report.write("# Consolidation Report\n\n")
        for src, dst in operations:
            report.write(f"- Move `{src}` → `{dst}`\n")
            dst_dir = os.path.dirname(dst)
            os.makedirs(dst_dir, exist_ok=True)
            shutil.move(src, dst)
        report.write(f"\nTotal files moved: {len(operations)}\n")

    print(f"Consolidation complete. See {REPORT_FILE} for details.")


if __name__ == "__main__":
    main()
