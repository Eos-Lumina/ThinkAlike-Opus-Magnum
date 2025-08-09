import os
import re
import yaml
from pathlib import Path

# Directory containing canonical docs
DOCS_DIR = Path('docs')
# Optionally, add more legacy path patterns here
LEGACY_PATTERNS = [
    re.compile(r'\]\((\.\./_legacy/[^)]+)\)'),
    re.compile(r'\]\((\.\./legacy/[^)]+)\)'),
    re.compile(r'\]\((\.\./old_thinkalike/[^)]+)\)'),
    re.compile(r'\]\((\.\./docs/[^)]+)\)'),
    re.compile(r'\]\((\.\./[^)]+)\)'),
]

# Find all markdown files in docs/
def find_markdown_files():
    for root, _, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith('.md'):
                yield Path(root) / file

def update_links_in_file(filepath, canonical_paths):
    changed = False
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original_content = content
    # Find all markdown links
    for match in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', content):
        text, link = match.groups()
        # Only update relative links
        if not link.startswith('http') and not link.startswith('#'):
            # Normalize path
            link_path = (filepath.parent / link).resolve()
            # If the link points to a known canonical file, rewrite it as relative to docs/
            for canon in canonical_paths:
                try:
                    if link_path.samefile(canon):
                        rel = os.path.relpath(canon, filepath.parent)
                        content = content.replace(f']({link})', f']({rel.replace(os.sep, "/")})')
                        changed = True
                except FileNotFoundError:
                    # Skip if the file does not exist
                    continue
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    return changed, original_content, content

def main():
    # Build a set of all canonical markdown file paths
    canonical_paths = set(find_markdown_files())
    report = []
    for md_file in canonical_paths:
        changed, before, after = update_links_in_file(md_file, canonical_paths)
        if changed:
            report.append({'file': str(md_file), 'updated': True})
    # Write a YAML report
    with open('docs/reference_update_report.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(report, f, allow_unicode=True)
    print(f"Updated {len(report)} files. See docs/reference_update_report.yaml for details.")

if __name__ == '__main__':
    main()
