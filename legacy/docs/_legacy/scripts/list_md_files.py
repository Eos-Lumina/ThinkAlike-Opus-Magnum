import os

ARCHIVE_DIR = r"F:\ThinkAlike_Project\archive_legacy"
OUTPUT_FILE = r"F:\ThinkAlike_Project\scripts\found_md_files.txt"

md_files = []
for root, _, files in os.walk(ARCHIVE_DIR):
    for f in files:
        if f.lower().endswith('.md'):
            md_files.append(os.path.join(root, f))

with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
    out.write(f"Found {len(md_files)} markdown files:\n")
    for path in md_files:
        out.write(path + '\n')
print(f"Wrote list of markdown files to {OUTPUT_FILE}")
