import os
from pathlib import Path

GROUPS_DIR = r"f:\\ThinkAlike_Project\\scripts\\md_groups_by_folder"
LEGACY_DOCS_DIR = r"f:\\ThinkAlike_Project\\archive_legacy\\legacy_docs"
PROJECT_ROOT_ARCHIVE = r"f:\\ThinkAlike_Project\\archive_legacy\\project_root_archive"
MIGRATION_MARKER_PREFIX = "<!-- MIGRATED: "

report_missing = []
report_unmarked = []

for root, dirs, files in os.walk(PROJECT_ROOT_ARCHIVE):
    for file in files:
        if file.lower().endswith('.md'):
            src_path = os.path.join(root, file)
            # Compute expected legacy_docs path
            rel_path = os.path.relpath(src_path, PROJECT_ROOT_ARCHIVE)
            group_name = rel_path.split(os.sep)[0] if os.sep in rel_path else "_"
            dest_dir = os.path.join(LEGACY_DOCS_DIR, group_name)
            dest_path = os.path.join(dest_dir, file)
            # Check if migrated
            if not os.path.exists(dest_path):
                report_missing.append(src_path)
            else:
                # Check for migration marker
                with open(src_path, encoding="utf-8", errors="ignore") as f:
                    first_line = f.readline()
                if not first_line.startswith(MIGRATION_MARKER_PREFIX):
                    report_unmarked.append(src_path)

with open(r"f:\\ThinkAlike_Project\\scripts\\migration_missing_report.txt", "w", encoding="utf-8") as f:
    f.write("Missing in legacy_docs:\n" + "\n".join(report_missing) + "\n\n")
    f.write("Not marked as migrated:\n" + "\n".join(report_unmarked) + "\n")
print(f"Report written: f:/ThinkAlike_Project/scripts/migration_missing_report.txt")
