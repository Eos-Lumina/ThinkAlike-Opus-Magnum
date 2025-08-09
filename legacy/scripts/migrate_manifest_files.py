import os
import shutil
import yaml
from pathlib import Path

MANIFEST_PATH = Path('docs/migration_manifest.md')
LOG_PATH = Path('docs/migrated_manifest_files.yaml')

# Parse the migration manifest for Merge/Keep actions
def parse_manifest():
    files = []
    with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip().startswith('|') and 'Merge/Keep' in line:
                parts = [p.strip() for p in line.strip().split('|') if p.strip()]
                if len(parts) >= 4:
                    legacy = parts[0]
                    canonical = parts[3]
                    files.append((legacy, canonical))
    return files

def migrate_files():
    files = parse_manifest()
    log = []
    for legacy, canonical in files:
        legacy_path = Path(legacy)
        canonical_path = Path(canonical)
        if legacy_path.exists():
            canonical_path.parent.mkdir(parents=True, exist_ok=True)
            if not canonical_path.exists():
                shutil.move(str(legacy_path), str(canonical_path))
                log.append({'from': str(legacy_path), 'to': str(canonical_path)})
            else:
                log.append({'from': str(legacy_path), 'to': str(canonical_path), 'status': 'skipped (destination exists)'})
        else:
            log.append({'from': str(legacy_path), 'to': str(canonical_path), 'status': 'skipped (source missing)'})
    with open(LOG_PATH, 'w', encoding='utf-8') as f:
        yaml.dump(log, f, allow_unicode=True)
    print(f"Migrated {len([l for l in log if 'status' not in l])} files. See {LOG_PATH} for details.")

if __name__ == '__main__':
    migrate_files()
