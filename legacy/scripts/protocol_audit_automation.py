import os
import frontmatter
from collections import defaultdict

# Directory to scan
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PROTOCOL_DIRS = [
    'protocols',
    'docs/protocols',
    'bridges',
    'realms',
    'seed',
]

# Collect protocol metadata
protocols = []
for base in PROTOCOL_DIRS:
    dir_path = os.path.join(ROOT_DIR, base)
    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                try:
                    post = frontmatter.load(path)
                    meta = post.metadata
                    meta['file'] = os.path.relpath(path, ROOT_DIR)
                    protocols.append(meta)
                except Exception as e:
                    print(f"Error reading {path}: {e}")

# Build interdependency matrix
matrix = defaultdict(list)
for proto in protocols:
    refs = proto.get('related_docs', [])
    for ref in refs:
        matrix[proto['file']].append(ref)

# Find orphans (not referenced by any other doc)
all_files = set(p['file'] for p in protocols)
referenced = set(ref for refs in matrix.values() for ref in refs)
orphans = all_files - referenced

# Output results
print("\n=== Protocol Interdependency Matrix ===")
for k, v in matrix.items():
    print(f"{k}: {v}")

print("\n=== Orphan Protocols (not referenced) ===")
for o in orphans:
    print(o)

print("\n=== Protocols Missing Harmonization Note or Bridge ===")
for p in protocols:
    if 'harmonization_note' not in p or not any('bridge' in str(v).lower() for v in p.values()):
        print(p['file'])
