#!/usr/bin/env python3
import os, yaml, csv

# ==== CONFIG ====
ROOT = "docs"
OUT_INDEX    = "docs_index.csv"
OUT_MISMATCH = "mismatches_refined.csv"

# Skip these patterns
EXCLUDE = ["_templates", "core_specs", "FOLDER_INDEX.md", "readme.md"]

# Folder→valid tag synonyms (all lowercase)
FOLDER_TAGS = {
    "wallet":            ["wallet","chrona"],
    "extensions":        ["extension","vscode","browser_plugin"],
    "local_exchange":    ["local_exchange","exchange"],
    "narrative_engine":  ["narrative_engine","narrative","symbolic"],
    "blueprints":        ["blueprint","plan"],
    "roadmap":           ["roadmap","quest","visualization"],
    "governance":        ["governance","trust","certification"],
    "deployment":        ["deployment","website","domain"],
    "economic":          ["economic","economy","chrona","valuation"],
    "identity":          ["identity","reputation","sybil","glyphic"],
    "resonance":         ["resonance","temporal","kairos"],
    "trust":             ["trust","matching","restorative"],
    # add more pillars here…
}

def should_skip(rel_path):
    return any(p in rel_path for p in EXCLUDE)

def load_frontmatter(path):
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    try:
        loaded = yaml.safe_load(parts[1])
        if loaded is None:
            return {}
        return loaded
    except Exception as e:
        with open("yaml_frontmatter_errors.log", "a", encoding="utf-8") as log:
            log.write(f"{path}: {e}\n")
        return {"__yaml_error__": str(e)}

def get_category(path):
    # e.g. docs/branches/protocols/economic/file.md → 'economic'
    parts = os.path.relpath(path, ROOT).replace("\\","/").split("/")
    if parts[0]=="branches": parts = parts[1:]
    return parts[1] if len(parts)>=2 else parts[0]

all_rows, mismatches = [], []

for dp, _, files in os.walk(ROOT):
    for fn in sorted(files):
        if not fn.endswith(".md"): continue
        full = os.path.join(dp, fn)
        rel  = os.path.relpath(full, ROOT).replace("\\","/")
        if should_skip(rel): continue

        meta = load_frontmatter(full)
        if meta is None:
            meta = {}
        if "__yaml_error__" in meta:
            continue  # skip files with YAML errors, already logged
        title = str(meta.get("title") or "").strip().replace("\n", " ")
        raw_tags = meta.get("tags", [])
        # Normalize tags to a lowercase list
        if isinstance(raw_tags, str):
            tags = [t.strip().lower() for t in raw_tags.replace("|",",").split(",") if t.strip()]
        elif isinstance(raw_tags, list):
            tags = [str(t).strip().lower() for t in raw_tags if str(t).strip()]
        else:
            tags = []

        cat = get_category(full).lower()
        valid = FOLDER_TAGS.get(cat, [cat])

        all_rows.append({"path":rel, "title":title, "tags":"|".join(tags)})

        # if none of the valid synonyms appear in tags, it's a mismatch
        if not any(v.lower() in tags for v in valid):
            mismatches.append({"path":rel, "title":title, "tags":"|".join(tags)})

# Write global index
with open(OUT_INDEX, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["path","title","tags"])
    w.writeheader(); w.writerows(all_rows)
print(f"→ Wrote {OUT_INDEX} ({len(all_rows)} entries)")

# Write refined mismatches
with open(OUT_MISMATCH, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["path","title","tags"])
    w.writeheader(); w.writerows(mismatches)
print(f"→ Wrote {OUT_MISMATCH} ({len(mismatches)} potential mismatches)")
