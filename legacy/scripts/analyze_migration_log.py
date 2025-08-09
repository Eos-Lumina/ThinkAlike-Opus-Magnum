import os
import yaml
from collections import defaultdict

# This script analyzes migration_log.yaml and helps with skipped files.
# It generates two reports:
# 1. missing_sources_report.yaml: files that could not be found in _legacy
# 2. existing_destinations_report.yaml: files that were skipped because they already exist in docs

MIGRATION_LOG = 'migration_log.yaml'
MISSING_SOURCES_REPORT = 'missing_sources_report.yaml'
EXISTING_DESTINATIONS_REPORT = 'existing_destinations_report.yaml'

with open(MIGRATION_LOG, 'r', encoding='utf-8') as f:
    log = yaml.safe_load(f)

missing_sources = []
existing_destinations = []
other_skipped = []

for entry in log.get('skipped', []):
    reason = entry.get('reason', '')
    if 'Source file does not exist' in reason:
        missing_sources.append(entry['file'])
    elif 'Destination exists' in reason:
        existing_destinations.append({'source': entry['file'], 'destination': reason.split(': ', 1)[-1]})
    else:
        other_skipped.append(entry)

with open(MISSING_SOURCES_REPORT, 'w', encoding='utf-8') as out:
    yaml.safe_dump({'missing_sources': missing_sources}, out, sort_keys=False, allow_unicode=True)

with open(EXISTING_DESTINATIONS_REPORT, 'w', encoding='utf-8') as out:
    yaml.safe_dump({'existing_destinations': existing_destinations}, out, sort_keys=False, allow_unicode=True)

print(f"Missing sources: {len(missing_sources)}. Existing destinations: {len(existing_destinations)}. See reports for details.")
