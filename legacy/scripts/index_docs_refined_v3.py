#!/usr/bin/env python3
import os, yaml, csv

# —— CONFIG —— 
ROOT = "docs"
OUT_INDEX    = "docs_index.csv"
OUT_MISMATCH = "mismatches_refined_v3.csv"

# patterns to skip entirely
EXCLUDE = ["_templates", "core_specs", "FOLDER_INDEX.md", "readme.md"]

def should_skip(path):
    return any(p in path for p in EXCLUDE)

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

def get_folder_category(path):
    # e.g. docs/branches/protocols/economic/foo.md → "economic"
    rel = os.path.relpath(path, ROOT).replace("\\","/")
    parts = rel.split("/")
    if parts[0] == "branches":
        parts = parts[1:]
    # if there is at least a pillar and a category, return parts[1]
    return parts[1] if len(parts) >= 2 else parts[0]

# ——— 1) Build the set of all folder names (first & second level) ———
categories = set()
for dp, dirs, files in os.walk(os.path.join(ROOT, "branches")):
    rel = os.path.relpath(dp, ROOT).replace("\\","/")
    parts = rel.split("/")
    # look for branches/<pillar>/<category>
    if len(parts) >= 3 and parts[0] == "branches":
        categories.add(parts[1])       # pillar
        categories.add(parts[2])       # category
# fallback if you also have docs/<category> directly
for dp, dirs, files in os.walk(ROOT):
    rel = os.path.relpath(dp, ROOT).replace("\\","/")
    parts = rel.split("/")
    if len(parts) == 1 and parts[0] not in ("branches","_templates"):
        categories.add(parts[0])

# Make a dict where each category maps to itself (as its only synonym)
FOLDER_TAGS = {cat: [cat] for cat in categories}

# ——— 2) Walk and index ———
all_rows, mismatches = [], []

for dp, _, files in os.walk(ROOT):
    for fn in sorted(files):
        if not fn.lower().endswith(".md"):
            continue
        full = os.path.join(dp, fn)
        rel  = os.path.relpath(full, ROOT).replace("\\","/")
        if should_skip(rel):
            continue

        meta = load_frontmatter(full)
        
        # Robustly handle title as string, list, or other types
        title_val = meta.get("title", "")
        if isinstance(title_val, list):
            title = ", ".join(str(t) for t in title_val)
        else:
            title = str(title_val)
        title = title.strip().replace("\n", " ")
        raw_tags = meta.get("tags", [])
        # normalize tags list
        if isinstance(raw_tags, str):
            tags = [t.strip().lower() for t in raw_tags.replace("|",",").split(",") if t.strip()]
        elif isinstance(raw_tags, list):
            tags = [str(t).strip().lower() for t in raw_tags if str(t).strip()]
        else:
            tags = []

        cat = get_folder_category(full).lower()
        valid = FOLDER_TAGS.get(cat, [cat])

        all_rows.append({"path":rel, "title":title, "tags":"|".join(tags)})

        # Skip mismatches if there are NO tags at all
        if not tags:
            continue

        # If none of the valid synonyms appear in tags, flag it
        if not any(v in tags for v in valid):
            mismatches.append({"path":rel, "title":title, "tags":"|".join(tags)})

# ——— 3) Write outputs ———
with open(OUT_INDEX, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["path","title","tags"])
    w.writeheader(); w.writerows(all_rows)

with open(OUT_MISMATCH, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["path","title","tags"])
    w.writeheader(); w.writerows(mismatches)

print(f"→ Wrote {OUT_INDEX} ({len(all_rows)} entries)")
print(f"→ Wrote {OUT_MISMATCH} ({len(mismatches)} potential mismatches)")
