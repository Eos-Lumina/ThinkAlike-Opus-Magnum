#!/usr/bin/env python3
import os, yaml, csv

ROOT = "docs"
OUT_INDEX    = "docs_index.csv"
OUT_MISMATCH = "mismatches_refined_v4.csv"
SKIP = ["_templates", "core_specs", "FOLDER_INDEX.md", "readme.md"]

def skip(path):
    return any(p in path for p in SKIP)

def load_frontmatter(path):
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---"): return {}
    parts = text.split("---", 2)
    try:
        return yaml.safe_load(parts[1]) or {}
    except Exception as e:
        with open("yaml_frontmatter_errors.log", "a", encoding="utf-8") as log:
            log.write(f"{path}: {e}\n")
        return {}

all_rows, mismatches = [], []

for dp, _, files in os.walk(ROOT):
    for fn in sorted(files):
        if not fn.endswith(".md"):
            continue
        full = os.path.join(dp, fn)
        rel  = os.path.relpath(full, ROOT).replace("\\","/")
        if skip(rel):
            continue

        meta = load_frontmatter(full)
        title_val = meta.get("title", "")
        if isinstance(title_val, list):
            title = ", ".join(str(t) for t in title_val)
        else:
            title = str(title_val)
        title = title.strip().replace("\n", " ")
        raw_tags = meta.get("tags", [])
        # normalize to lowercase list
        if isinstance(raw_tags, str):
            tags = [t.strip().lower() for t in raw_tags.replace("|",",").split(",") if t.strip()]
        elif isinstance(raw_tags, list):
            tags = [str(t).strip().lower() for t in raw_tags if str(t).strip()]
        else:
            tags = []

        # direct parent folder name
        parent = os.path.basename(os.path.dirname(full)).lower()

        all_rows.append({"path":rel, "title":title, "tags":"|".join(tags)})

        # skip files with no tags at all (treat as no‐mismatch)
        if not tags:
            continue

        # if the parent folder isn't in the tags, it's a genuine mismatch
        if parent not in tags:
            mismatches.append({"path":rel, "title":title, "tags":"|".join(tags)})

# write outputs
with open(OUT_INDEX, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, ["path","title","tags"])
    w.writeheader(); w.writerows(all_rows)

with open(OUT_MISMATCH, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, ["path","title","tags"])
    w.writeheader(); w.writerows(mismatches)

print(f"Wrote {OUT_INDEX} ({len(all_rows)} rows)")
print(f"Wrote {OUT_MISMATCH} ({len(mismatches)} mismatches)")
