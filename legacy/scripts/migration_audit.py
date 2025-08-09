"""
ThinkAlike Migration Audit Script

- Loads migration_manifest.md
- Scans all markdown files in project and _legacy folders
- Flags files as keep/merge, archive, or purge based on manifest
- Checks for normalized frontmatter/tags (optional, can be extended)
- Outputs a report for review
"""
import os
import re
import yaml
from pathlib import Path
from datetime import datetime

# CONFIG
PROJECT_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = PROJECT_ROOT / 'docs' / 'migration_manifest.md'
LEGACY_DIR = PROJECT_ROOT / '_legacy'
REPORT_PATH = PROJECT_ROOT / 'docs' / 'migration_audit_report.txt'

# Helper: Parse migration manifest table

def parse_manifest_table(md_path):
    keep_files = set()
    archive_files = set()
    with open(md_path, encoding='utf-8') as f:
        lines = f.readlines()
    in_table = False
    for line in lines:
        if line.strip().startswith('|') and not in_table:
            in_table = True
            continue
        if in_table:
            if not line.strip().startswith('|'):
                break
            cols = [c.strip() for c in line.strip().split('|')[1:-1]]
            if len(cols) < 5:
                continue
            file_path, _, action, _, notes = cols
            if action.lower().startswith('merge') or action.lower().startswith('keep'):
                keep_files.add(file_path)
            elif action.lower().startswith('archive'):
                archive_files.add(file_path)
    return keep_files, archive_files

# Helper: Find all markdown files

def find_markdown_files(root):
    return [str(p.relative_to(PROJECT_ROOT)) for p in root.rglob('*.md')]

# Helper: Extract YAML frontmatter from a markdown file
def extract_frontmatter(md_path):
    with open(md_path, encoding='utf-8') as f:
        lines = f.readlines()
    if not lines or not lines[0].strip().startswith('---'):
        return None
    fm_lines = []
    for line in lines[1:]:
        if line.strip().startswith('---'):
            break
        fm_lines.append(line)
    try:
        return yaml.safe_load(''.join(fm_lines))
    except Exception:
        return None

# Helper: Validate tags
REQUIRED_FIELDS = ['title', 'status', 'last_updated', 'maintained_by', 'tags']
STATUS_VOCAB = {'Draft', 'Review', 'Approved', 'Harmonized', 'Deprecated', 'Archived'}
TAG_PREFIXES = {'type/', 'domain/', 'aspect/', 'project/'}
def validate_tags(tags):
    if not isinstance(tags, list) or not tags:
        return False, 'tags must be a non-empty YAML list'
    for tag in tags:
        if not isinstance(tag, str):
            return False, f'tag {tag} is not a string'
        if ' ' in tag:
            return False, f'tag {tag} contains spaces'
        if tag.lower() != tag:
            return False, f'tag {tag} is not lowercase'
        if not any(tag.startswith(prefix) for prefix in TAG_PREFIXES):
            return False, f'tag {tag} missing required prefix'
    return True, ''

def check_frontmatter(md_path):
    fm = extract_frontmatter(md_path)
    if not fm:
        return 'Missing or invalid YAML frontmatter'
    for field in REQUIRED_FIELDS:
        if field not in fm or fm[field] in (None, '', []):
            return f'Missing required field: {field}'
    status = fm.get('status')
    if status and status not in STATUS_VOCAB:
        return f'Invalid status: {status}'
    last_updated = fm.get('last_updated')
    if last_updated:
        try:
            datetime.strptime(str(last_updated), '%Y-%m-%d')
        except Exception:
            return 'last_updated not in YYYY-MM-DD format'
    tags = fm.get('tags')
    ok, msg = validate_tags(tags) if tags else (False, 'tags missing')
    if not ok:
        return msg
    return 'OK'

# Main audit logic

def main():
    keep_files, archive_files = parse_manifest_table(MANIFEST_PATH)
    all_md = set(find_markdown_files(PROJECT_ROOT))
    legacy_md = set(find_markdown_files(LEGACY_DIR))
    report = []
    for f in sorted(legacy_md):
        abs_path = PROJECT_ROOT / f
        if f in keep_files:
            status = 'KEEP/MERGE (in manifest)'
            fm_status = check_frontmatter(abs_path)
            report.append(f'{f}: {status} | Frontmatter: {fm_status}')
        elif f in archive_files:
            status = 'ARCHIVE (in manifest)'
            report.append(f'{f}: {status}')
        else:
            status = 'PURGE (not in manifest)'
            report.append(f'{f}: {status}')
    with open(REPORT_PATH, 'w', encoding='utf-8') as out:
        out.write('\n'.join(report))
    print(f'Audit complete. See report: {REPORT_PATH}')

if __name__ == '__main__':
    main()
