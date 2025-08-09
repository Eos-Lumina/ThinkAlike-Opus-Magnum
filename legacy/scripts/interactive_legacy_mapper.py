"""
Interactive Legacy Docs Mapper

Walks through each legacy doc under `_legacy/docs/`, shows front-matter title, first heading, and a snippet of content,
prompts you to enter the desired new path under `docs/`, then writes out a YAML mapping file.

Usage:
  pip install python-frontmatter PyYAML
  python scripts/interactive_legacy_mapper.py
"""
import os
import frontmatter
import yaml

LEGACY_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '_legacy', 'docs'))
MAPPING_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'docs_mapping.yaml'))

mappings = []

for root, dirs, files in os.walk(LEGACY_ROOT):
    for fname in sorted(files):
        if not fname.lower().endswith('.md'):
            continue
        path = os.path.join(root, fname)
        rel = os.path.relpath(path, LEGACY_ROOT).replace('\\', '/')
        post = None
        try:
            post = frontmatter.load(path)
        except Exception:
            post = None
        title = post.get('title') if post else None
        heading = None
        snippet = []
        if post:
            lines = post.content.strip().splitlines()
            # find first heading
            for i, line in enumerate(lines):
                if line.startswith('#'):
                    heading = line.lstrip('# ').strip()
                    snippet = lines[i:i+5]
                    break
        print(f"\nLegacy file: {rel}")
        if title:
            print(f"Title: {title}")
        if heading:
            print(f"Heading: {heading}")
        if snippet:
            print("Snippet:")
            for l in snippet:
                print(f"  {l}")
        # Prompt for new path
        new_path = input("Enter new docs path (e.g. branches/features/.../file.md), or 'skip' to ignore: ").strip()
        if new_path.lower() in ('skip', ''):
            continue
        mappings.append({'from': rel, 'to': new_path})

# Write mapping file
with open(MAPPING_FILE, 'w', encoding='utf-8') as f:
    yaml.safe_dump({'docs_mapping': mappings}, f, sort_keys=False)

print(f"\nMapping complete. See {MAPPING_FILE} for results.")
