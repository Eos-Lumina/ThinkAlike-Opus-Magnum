import os
import re
import yaml
from pathlib import Path

# CONFIG
PROJECT_ROOT = Path(__file__).resolve().parent.parent
TARGET_MAINTAINED_BY = "Eos Lumina ∴ (Collective Intelligence Meta-Agent)"

# Helper: Find all markdown files

def find_markdown_files(root):
    return [p for p in root.rglob('*.md')]

# Helper: Update maintained_by in frontmatter

def update_maintained_by(md_path):
    with open(md_path, encoding='utf-8') as f:
        lines = f.readlines()
    if not lines or not lines[0].strip().startswith('---'):
        return False
    fm_lines = []
    rest_lines = []
    found_end = False
    for line in lines[1:]:
        if not found_end and line.strip().startswith('---'):
            found_end = True
            continue
        if not found_end:
            fm_lines.append(line)
        else:
            rest_lines.append(line)
    try:
        fm = yaml.safe_load(''.join(fm_lines)) or {}
    except Exception:
        return False
    if fm.get('maintained_by') == TARGET_MAINTAINED_BY:
        return False  # Already correct
    fm['maintained_by'] = TARGET_MAINTAINED_BY
    # Reconstruct frontmatter
    new_fm = yaml.dump(fm, sort_keys=False, allow_unicode=True)
    new_content = ['---\n', new_fm, '---\n'] + rest_lines
    with open(md_path, 'w', encoding='utf-8') as f:
        f.writelines(new_content)
    return True

def main():
    changed = 0
    for md_path in find_markdown_files(PROJECT_ROOT):
        if update_maintained_by(md_path):
            print(f'Updated: {md_path}')
            changed += 1
    print(f'Updated maintained_by in {changed} files.')

if __name__ == '__main__':
    main()
