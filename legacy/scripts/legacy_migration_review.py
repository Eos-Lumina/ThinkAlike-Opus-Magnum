import os
import frontmatter
import yaml

# Path to the list of not-yet-migrated legacy files
to_review_path = 'not_migrated_from_legacy.txt'
legacy_root = os.path.join(os.getcwd(), '_legacy')

review = []

with open(to_review_path, 'r', encoding='utf-8') as f:
    files = [line.strip() for line in f if line.strip()]

for rel_path in files:
    abs_path = os.path.join(legacy_root, rel_path)
    if not os.path.exists(abs_path):
        continue
    try:
        post = frontmatter.load(abs_path)
        title = post.get('title', post.get('Title', ''))
        tags = post.get('tags', [])
        content_lines = post.content.strip().splitlines()
        heading = ''
        for line in content_lines:
            if line.startswith('#'):
                heading = line.lstrip('# ').strip()
                break
        preview = ' '.join(content_lines[:2]) if content_lines else ''
        snippet_lines = []
        if content_lines:
            idx = next((i for i, ln in enumerate(content_lines) if ln.startswith('#')), 0)
            snippet_lines = content_lines[idx:idx+5]
        snippet = snippet_lines
    except Exception:
        title = ''
        tags = []
        heading = ''
        preview = ''
        snippet = []
    review.append({
        'file': rel_path.replace('\\', '/'),
        'title': title,
        'tags': tags,
        'heading': heading,
        'preview': preview,
        'snippet': snippet
    })

with open('legacy_migration_review.yaml', 'w', encoding='utf-8') as out:
    yaml.safe_dump({'legacy_migration_review': review}, out, sort_keys=False, allow_unicode=True)

print(f"Review file created: legacy_migration_review.yaml ({len(review)} files)")
