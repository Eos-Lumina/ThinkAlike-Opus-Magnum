#!/usr/bin/env python3
import os, yaml, csv
import re

ROOT = "docs"                     # your docs root
OUT_INDEX = "docs_index.csv"
OUT_MISMATCH = "mismatches.csv"
FILTERED_MISMATCH = "mismatches_filtered.csv"

all_rows = []
# 1) Walk and collect
for dirpath, _, files in os.walk(ROOT):
    rel_dir = os.path.relpath(dirpath, ROOT).replace("\\","/")
    md = [f for f in files if f.endswith(".md")]
    for f in sorted(md):
        full = os.path.join(dirpath, f)
        text = open(full, encoding="utf-8").read()
        title, tags = "", ""
        if text.startswith("---"):
            try:
                fm = text.split("---",2)[1]
                data = yaml.safe_load(fm)
                title = data.get("title","")
                tags  = "|".join(data.get("tags",[]))
            except: pass
        path = f"{rel_dir}/{f}" if rel_dir!="." else f
        all_rows.append({"path":path, "title":title, "tags":tags})

# 2) Emit global CSV
with open(OUT_INDEX, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["path","title","tags"])
    w.writeheader(); w.writerows(all_rows)
print(f"→ Wrote {OUT_INDEX} ({len(all_rows)} rows)")

# 3) Find mismatches
mismatches = []
for row in all_rows:
    folder = row["path"].split("/")[0]
    # skip templates/system files
    if folder.startswith("_") or folder=="trunk": 
        continue
    tag_list = row["tags"].split("|")
    # if folder not in tags, maybe misplaced
    if folder and folder not in tag_list:
        mismatches.append(row)
with open(OUT_MISMATCH, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["path","title","tags"])
    w.writeheader(); w.writerows(mismatches)
print(f"→ Wrote {OUT_MISMATCH} ({len(mismatches)} potential mismatches)")

# 4) Per-folder index files
from collections import defaultdict
by_folder = defaultdict(list)
for r in all_rows: 
    fld = r["path"].split("/")[0]
    by_folder[fld].append(r)

for fld, rows in by_folder.items():
    folder_path = os.path.join(ROOT, fld)
    idx_file    = os.path.join(folder_path, "FOLDER_INDEX.md")
    with open(idx_file, "w", encoding="utf-8") as md:
        md.write(f"# {fld}  Index\n\n")
        md.write("| file | title | tags |\n")
        md.write("|---|---|---|\n")
        for r in rows:
            fn = r["path"].split("/",1)[1] if "/" in r["path"] else r["path"]
            md.write(f"| `{fn}` | {r['title']} | {r['tags']} |\n")
    print(f"→ {idx_file}")

# 5) Filter mismatches.csv to exclude false positives
with open(OUT_MISMATCH, newline='', encoding='utf-8') as src, open(FILTERED_MISMATCH, 'w', newline='', encoding='utf-8') as dst:
    reader = csv.DictReader(src)
    writer = csv.DictWriter(dst, fieldnames=reader.fieldnames)
    writer.writeheader()
    for row in reader:
        path = row['path']
        if (
            re.search(r'/readme\\.md$', path, re.IGNORECASE) or
            re.search(r'/FOLDER_INDEX\\.md$', path, re.IGNORECASE) or
            '/core_specs/' in path or
            path.endswith('FOLDER_INDEX.md')
        ):
            continue
        writer.writerow(row)
print(f"→ Wrote {FILTERED_MISMATCH} (filtered mismatches)")

# 6) Print actionable next steps for each remaining mismatch
with open(FILTERED_MISMATCH, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    actionable = [row for row in reader if row['path'] and not row['path'].endswith('FOLDER_INDEX.md')]
    print(f"\nActionable mismatches: {len(actionable)}\n")
    for row in actionable[:20]:  # print first 20 for scan
        print(f"- {row['path']} | {row['title']} | {row['tags']}")
    if len(actionable) > 20:
        print(f"...and {len(actionable)-20} more. See mismatches_filtered.csv for full list.")

print("\nFor each, open its FOLDER_INDEX.md to review context. Move or retag as needed.")
print("To bulk-annotate tags, use the provided PowerShell one-liner for the relevant folder.")
print("All done. Now open `mismatches.csv` and each `*/FOLDER_INDEX.md` in VS\u2009Code.")
