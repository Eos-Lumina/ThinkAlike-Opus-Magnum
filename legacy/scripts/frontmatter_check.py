
import os
import frontmatter

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PROTOCOL_DIRS = [
    'protocols',
    'docs/protocols',
    'bridges',
    'realms',
    'seed',
]

errors = []
for base in PROTOCOL_DIRS:
    dir_path = os.path.join(ROOT_DIR, base)
    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                try:
                    with open(path, encoding='utf-8') as f:
                        content = f.read()
                    # Try to parse frontmatter using python-frontmatter
                    post = frontmatter.loads(content)
                except Exception as e:
                    errors.append((os.path.relpath(path, ROOT_DIR), str(e)))

if errors:
    print("\n=== Frontmatter/YAML Errors Detected ===")
    for file, err in errors:
        print(f"{file}: {err}")
else:
    print("No frontmatter/YAML errors detected!")
