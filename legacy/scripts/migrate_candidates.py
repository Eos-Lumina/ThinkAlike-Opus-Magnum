import os
import shutil
import yaml

# This script migrates canonical files from legacy_migration_candidates.yaml to the new docs structure.
# It assumes the working directory is the project root (C:/ThinkAlike).

CANDIDATES_FILE = 'legacy_migration_candidates.yaml'
LEGACY_ROOT = '_legacy'
DEST_ROOT = os.path.join('docs')

with open(CANDIDATES_FILE, 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

migrated = []
skipped = []

for entry in data['migration_candidates']:
    legacy_rel_path = entry['file']
    # Remove any leading 'Legacy_main/1/' or similar, to get the relative path under _legacy
    if legacy_rel_path.startswith('Legacy_main/1/'):
        rel_path = legacy_rel_path[len('Legacy_main/1/'):]
    elif legacy_rel_path.startswith('Legacy_main/'):
        rel_path = legacy_rel_path[len('Legacy_main/'):]
    else:
        # If not under Legacy_main, just use the path as-is (may need further adjustment)
        rel_path = legacy_rel_path
    src = os.path.join(LEGACY_ROOT, rel_path)
    dest = os.path.join(DEST_ROOT, rel_path)
    dest_dir = os.path.dirname(dest)
    os.makedirs(dest_dir, exist_ok=True)
    if not os.path.exists(src):
        skipped.append({'file': src, 'reason': 'Source file does not exist'})
        continue
    if os.path.exists(dest):
        skipped.append({'file': src, 'reason': f'Destination exists: {dest}'})
        continue
    try:
        shutil.copy2(src, dest)
        migrated.append({'from': src, 'to': dest})
    except Exception as e:
        skipped.append({'file': src, 'reason': str(e)})

with open('migration_log.yaml', 'w', encoding='utf-8') as out:
    yaml.safe_dump({'migrated': migrated, 'skipped': skipped}, out, sort_keys=False, allow_unicode=True)

print(f"Migrated {len(migrated)} files. Skipped {len(skipped)}. See migration_log.yaml for details.")
