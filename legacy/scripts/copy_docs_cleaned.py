#!/usr/bin/env python3
import os, csv, shutil

SRC_ROOT   = "docs/branches"
INDEX_CSV  = "docs_index.csv"
DST_ROOT   = "docs_cleaned/branches"

with open(INDEX_CSV, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rel_path = row["path"]
        parts    = rel_path.split("/")
        if len(parts) < 3:
            print(f"⚠️  SKIPPING (too shallow): {rel_path}")
            continue

        pillar, category, *rest = parts
        basename = rest[-1]
        subpath  = rest[:-1]

        # src should be relative to docs, not docs/branches
        src = os.path.join("docs", rel_path)
        dst_dir = os.path.join(DST_ROOT, pillar, category, *subpath)
        dst = os.path.join(dst_dir, basename)

        os.makedirs(dst_dir, exist_ok=True)
        print(f"→ {rel_path} → branches/{pillar}/{category}/{'/'.join(subpath + [basename])}")
        shutil.copy2(src, dst)

print("Done. Review `docs_cleaned/` and when you’re happy, delete old `docs/branches` and rename dc.")
