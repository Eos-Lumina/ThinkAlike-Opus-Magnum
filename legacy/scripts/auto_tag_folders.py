import os, yaml

ROOT = "docs"

def update_tags(md_path):
    with open(md_path, encoding="utf-8") as f:
        lines = f.readlines()

    if not lines[0].startswith("---"):
        return  # no frontmatter

    fm_end = next(i for i, l in enumerate(lines[1:], 1) if l.strip() == "---")
    fm = "".join(lines[1:fm_end])
    body = "".join(lines[fm_end+1:])
    meta = yaml.safe_load(fm)

    folder = os.path.normpath(md_path).split(os.sep)[-2]
    tags = meta.get("tags", [])

    if isinstance(tags, str):
        tags = [t.strip() for t in tags.replace("|",",").split(",")]

    if folder not in tags:
        tags.append(folder)
        meta["tags"] = sorted(set(tags))

        with open(md_path, "w", encoding="utf-8") as f:
            f.write("---\n")
            yaml.dump(meta, f, sort_keys=False)
            f.write("---\n\n")
            f.write(body)

count = 0
for dirpath, _, files in os.walk(ROOT):
    for f in files:
        if not f.endswith(".md"): continue
        path = os.path.join(dirpath, f)
        try:
            update_tags(path)
            count += 1
        except:
            pass

print(f"✅ Auto-tagged {count} Markdown files with folder context.")
