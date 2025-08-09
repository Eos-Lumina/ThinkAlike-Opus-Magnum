import yaml

# This script will filter the legacy_migration_review.yaml file to help you prioritize migration.
# It will flag files with missing titles, tags, or headings, and group by heading/title for deduplication review.

REVIEW_FILE = 'legacy_migration_review.yaml'
OUTPUT_FILE = 'legacy_migration_candidates.yaml'

with open(REVIEW_FILE, 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

candidates = []
duplicates = {}


for entry in data['legacy_migration_review']:
    # Normalize None or list to string for title/heading
    def normalize_field(val):
        if val is None:
            return ''
        if isinstance(val, list):
            return ' '.join(str(v) for v in val)
        return str(val)
    title = normalize_field(entry['title'])
    heading = normalize_field(entry['heading'])
    tags = entry['tags'] if entry['tags'] is not None else []
    # Flag files with missing or empty title, tags, or heading
    missing = []
    if not title.strip():
        missing.append('title')
    if not tags:
        missing.append('tags')
    if not heading.strip():
        missing.append('heading')
    entry['missing'] = missing
    # Group by normalized title+heading for deduplication
    key = (title.strip().lower(), heading.strip().lower())
    if key not in duplicates:
        duplicates[key] = []
    duplicates[key].append(entry['file'])
    # Prioritize for migration if it has a title, tags, and heading
    if not missing:
        # Store normalized title/heading for deduplication info
        entry['normalized_title'] = title
        entry['normalized_heading'] = heading
        candidates.append(entry)

# Add deduplication info
for entry in candidates:
    key = (entry['normalized_title'].strip().lower(), entry['normalized_heading'].strip().lower())
    entry['possible_duplicates'] = [f for f in duplicates[key] if f != entry['file']]

with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
    yaml.safe_dump({'migration_candidates': candidates}, out, sort_keys=False, allow_unicode=True)

print(f"Filtered migration candidates written to {OUTPUT_FILE} ({len(candidates)} files with title, tags, and heading)")
