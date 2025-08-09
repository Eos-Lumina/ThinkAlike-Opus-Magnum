import os
from collections import defaultdict

ARCHIVE_DIR = r"F:\ThinkAlike_Project\archive_legacy"
OUTPUT_DIR = r"F:\ThinkAlike_Project\scripts\md_groups_by_folder"

os.makedirs(OUTPUT_DIR, exist_ok=True)

folder_groups = defaultdict(list)
for root, _, files in os.walk(ARCHIVE_DIR):
    for f in files:
        if f.lower().endswith('.md'):
            rel_folder = os.path.relpath(root, ARCHIVE_DIR)
            folder_groups[rel_folder].append(os.path.join(root, f))

for folder, files in folder_groups.items():
    safe_folder = folder.replace(os.sep, '_').replace('.', '_')
    if safe_folder in ('', '.'): safe_folder = 'root'
    out_path = os.path.join(OUTPUT_DIR, f"md_group_{safe_folder}.txt")
    with open(out_path, 'w', encoding='utf-8') as out:
        out.write(f"# Markdown files in {folder} ({len(files)})\n\n")
        for path in files:
            out.write(f"- {path}\n")
print(f"Wrote grouped lists to {OUTPUT_DIR}")
