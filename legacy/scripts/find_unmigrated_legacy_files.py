import os
import yaml
from pathlib import Path

LEGACY_DIR = Path('_legacy')
ARCHIVE_DIR = LEGACY_DIR / '_archived_migrated'
MIGRATION_LOG = Path('migration_log.yaml')

# Load migrated legacy paths from migration_log.yaml
def load_migrated_legacy_paths():
    if not MIGRATION_LOG.exists():
        return set()
    with open(MIGRATION_LOG, 'r', encoding='utf-8') as f:
        log = yaml.safe_load(f)
    migrated = set()
    if isinstance(log, dict) and 'migrated' in log:
        for entry in log['migrated']:
            if isinstance(entry, dict) and 'from' in entry:
                migrated.add(os.path.normpath(entry['from']))
    return migrated

def find_unmigrated_legacy_files():
    migrated = load_migrated_legacy_paths()
    unmigrated = []
    for root, _, files in os.walk(LEGACY_DIR):
        # Skip archived files
        if ARCHIVE_DIR in Path(root).parents or Path(root) == ARCHIVE_DIR:
            continue
        for file in files:
            if file.endswith('.md'):
                rel_path = os.path.normpath(os.path.join(root, file))
                rel_path_short = os.path.relpath(rel_path, '.')
                if rel_path_short not in migrated:
                    unmigrated.append(rel_path_short)
    with open('docs/unmigrated_legacy_report.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(unmigrated, f, allow_unicode=True)
    print(f"Found {len(unmigrated)} unmigrated legacy markdown files. See docs/unmigrated_legacy_report.yaml for details.")

if __name__ == '__main__':
    find_unmigrated_legacy_files()
