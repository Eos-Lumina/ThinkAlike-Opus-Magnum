import os
import yaml
glob = os.path.glob if hasattr(os.path, 'glob') else __import__('glob').glob

# This script searches for missing files by filename anywhere under _legacy.
MISSING_SOURCES_REPORT = 'missing_sources_report.yaml'
LEGACY_ROOT = '_legacy'
FOUND_REPORT = 'found_missing_sources.yaml'
NOT_FOUND_REPORT = 'still_missing_sources.yaml'

with open(MISSING_SOURCES_REPORT, 'r', encoding='utf-8') as f:
    missing = yaml.safe_load(f)['missing_sources']

found = []
still_missing = []

for rel_path in missing:
    filename = os.path.basename(rel_path)
    matches = []
    for root, dirs, files in os.walk(LEGACY_ROOT):
        for f in files:
            if f == filename:
                matches.append(os.path.join(root, f))
    if matches:
        found.append({'original': rel_path, 'matches': matches})
    else:
        still_missing.append(rel_path)

with open(FOUND_REPORT, 'w', encoding='utf-8') as out:
    yaml.safe_dump({'found': found}, out, sort_keys=False, allow_unicode=True)

with open(NOT_FOUND_REPORT, 'w', encoding='utf-8') as out:
    yaml.safe_dump({'still_missing': still_missing}, out, sort_keys=False, allow_unicode=True)

print(f"Found {len(found)} missing files by filename. Still missing: {len(still_missing)}. See reports for details.")
