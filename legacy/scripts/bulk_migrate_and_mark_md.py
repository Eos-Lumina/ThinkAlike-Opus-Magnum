import os
import shutil
from pathlib import Path

# Configuration
GROUPS_DIR = os.path.join(os.getcwd(), "scripts", "md_groups_by_folder")
LEGACY_DOCS_DIR = os.path.join(os.getcwd(), "archive_legacy", "legacy_docs")
PROJECT_ROOT_ARCHIVE = os.path.join(os.getcwd(), "archive_legacy", "project_root_archive")
MIGRATION_MARKER = "<!-- MIGRATED: This file has been migrated to {dest_rel} and is ready for deletion. -->\n"
MIGRATION_MARKER_PREFIX = "<!-- MIGRATED: "

report_missing = []
report_unmarked = []
report_migrated = []
report_errors = []


def migrate_file(src_path, dest_path):
    try:
        dest_dir = os.path.dirname(dest_path)
        os.makedirs(dest_dir, exist_ok=True)
        if not os.path.exists(dest_path):
            shutil.copy2(src_path, dest_path)
            report_migrated.append(f"Copied: {src_path} -> {dest_path}")
        # Add migration marker if not present
        with open(src_path, encoding="utf-8", errors="ignore") as f:
            content = f.read()
        marker = MIGRATION_MARKER.format(dest_rel=os.path.relpath(dest_path, os.path.dirname(src_path)).replace('\\', '/'))
        if not content.startswith(marker):
            with open(src_path, "w", encoding="utf-8") as f:
                f.write(marker + "\n" + content)
            report_migrated.append(f"Marked as migrated: {src_path}")
    except Exception as e:
        report_errors.append(f"Error migrating {src_path}: {e}")


def main():
    for root, dirs, files in os.walk(PROJECT_ROOT_ARCHIVE):
        for file in files:
            if file.lower().endswith('.md'):
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, PROJECT_ROOT_ARCHIVE)
                # Use group folder as subfolder in legacy_docs
                group_name = rel_path.split(os.sep)[0] if os.sep in rel_path else "_"
                dest_dir = os.path.join(LEGACY_DOCS_DIR, group_name)
                dest_path = os.path.join(dest_dir, file)
                # Check if migrated
                migrated = os.path.exists(dest_path)
                with open(src_path, encoding="utf-8", errors="ignore") as f:
                    first_line = f.readline()
                marked = first_line.startswith(MIGRATION_MARKER_PREFIX)
                if not migrated or not marked:
                    migrate_file(src_path, dest_path)
                # For reporting
                if not os.path.exists(dest_path):
                    report_missing.append(src_path)
                elif not marked:
                    report_unmarked.append(src_path)
    # Write report
    with open(os.path.join(os.getcwd(), "scripts", "migration_missing_report.txt"), "w", encoding="utf-8") as f:
        f.write("Migrated/Marked this run:\n" + "\n".join(report_migrated) + "\n\n")
        f.write("Missing in legacy_docs after run:\n" + "\n".join(report_missing) + "\n\n")
        f.write("Not marked as migrated after run:\n" + "\n".join(report_unmarked) + "\n\n")
        f.write("Errors:\n" + "\n".join(report_errors) + "\n")
    print(f"Migration complete. See migration_missing_report.txt for details.")


if __name__ == "__main__":
    main()
