"""
ThinkAlike Frontmatter/Tag Validation Script

- Scans all .md files in the project
- Validates YAML frontmatter for required fields, controlled vocabulary, and tag formatting
- Reports violations for remediation
"""
import os
import re
import yaml
from pathlib import Path
from datetime import datetime

# CONFIG
PROJECT_ROOT = Path(__file__).resolve().parent.parent
REPORT_PATH = PROJECT_ROOT / 'docs' / 'frontmatter_validation_report.txt'
REQUIRED_FIELDS = ['title', 'status', 'last_updated', 'maintained_by', 'tags']
STATUS_VOCAB = {'Draft', 'Review', 'Approved', 'Harmonized', 'Deprecated', 'Archived'}
TAG_PREFIXES = {'type/', 'domain/', 'aspect/', 'project/'}

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
        if '-' in tag and ' ' in tag:
            return False, f'tag {tag} must use hyphens, not spaces'
        if not any(tag.startswith(prefix) for prefix in TAG_PREFIXES):
            return False, f'tag {tag} missing required prefix'
    return True, ''

# Main validation logic
def main():
    violations = []
    for md_path in PROJECT_ROOT.rglob('*.md'):
        rel_path = str(md_path.relative_to(PROJECT_ROOT))
        fm = extract_frontmatter(md_path)
        if not fm:
            violations.append(f'{rel_path}: Missing or invalid YAML frontmatter')
            continue
        for field in REQUIRED_FIELDS:
            if field not in fm or fm[field] in (None, '', []):
                violations.append(f'{rel_path}: Missing required field: {field}')
        # Status field check
        status = fm.get('status')
        if status and status not in STATUS_VOCAB:
            violations.append(f'{rel_path}: Invalid status: {status}')
        # last_updated format check
        last_updated = fm.get('last_updated')
        if last_updated:
            try:
                datetime.strptime(str(last_updated), '%Y-%m-%d')
            except Exception:
                violations.append(f'{rel_path}: last_updated not in YYYY-MM-DD format')
        # Tags check
        tags = fm.get('tags')
        ok, msg = validate_tags(tags) if tags else (False, 'tags missing')
        if not ok:
            violations.append(f'{rel_path}: {msg}')
    with open(REPORT_PATH, 'w', encoding='utf-8') as out:
        if violations:
            out.write('\n'.join(violations))
            print(f'Frontmatter validation complete. Violations found. See report: {REPORT_PATH}')
        else:
            out.write('All markdown files passed frontmatter validation.')
            print('All markdown files passed frontmatter validation.')

if __name__ == '__main__':
    main()
