"""
Script: audit_legacy_docs.py
Purpose: Scan `_legacy/docs/` folder, parse Markdown front-matter and headers,
produce a YAML mapping of each file with metadata for manual review.
Usage: python scripts/audit_legacy_docs.py > legacy_docs_audit.yaml
"""
import os
import frontmatter
import yaml

LEGACY_DOCS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '_legacy', 'docs'))
audit = []

for root, dirs, files in os.walk(LEGACY_DOCS_DIR):
    for file in files:
        if file.lower().endswith('.md'):
            path = os.path.join(root, file)
            rel_path = os.path.relpath(path, LEGACY_DOCS_DIR)
            try:
                post = frontmatter.load(path)
                title = post.get('title', post.get('Title', ''))
                tags = post.get('tags', [])
                # Extract first markdown heading and preview content
                content_lines = post.content.strip().splitlines()
                heading = ''
                for line in content_lines:
                    if line.startswith('#'):
                        heading = line.lstrip('# ').strip()
                        break
                preview = ' '.join(content_lines[:2]) if content_lines else ''
                # Capture a snippet of content around the first heading for context (5 lines)
                snippet_lines = []
                if content_lines:
                    # find index of heading
                    idx = next((i for i, ln in enumerate(content_lines) if ln.startswith('#')), 0)
                    snippet_lines = content_lines[idx:idx+5]
                snippet = snippet_lines
            except Exception:
                title = ''
                tags = []
                heading = ''
                preview = ''
                snippet = []
            audit.append({
                'file': rel_path.replace('\\', '/'),
                'title': title,
                'tags': tags,
                'current_folder': os.path.basename(root)
                ,'heading': heading
                ,'preview': preview
                ,'snippet': snippet
            })

print(yaml.safe_dump({'legacy_docs_audit': audit}, sort_keys=False))
