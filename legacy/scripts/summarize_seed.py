"""
Summarize all markdown files under docs/seed/
Extract frontmatter and top-level headings for each file and output to
seed_summary.json
"""

import json
import os


def extract_headings(text):
    headings = []
    for line in text.splitlines():
        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            title = line.lstrip("#").strip()
            headings.append({"level": level, "title": title})
    return headings


def summarize_seed(root_dir):
    summary = {}
    seed_dir = os.path.join(root_dir, "docs", "seed")
    for dirpath, dirs, files in os.walk(seed_dir):
        for fname in files:
            if fname.endswith(".md"):
                fpath = os.path.join(dirpath, fname)
                text = open(fpath, "r", encoding="utf-8").read()
                rel = os.path.relpath(fpath, root_dir)
                headings = extract_headings(text)
                summary[rel] = {"headings": headings}
    return summary


if __name__ == "__main__":
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    data = summarize_seed(root)
    out_path = os.path.join(root, "seed_summary.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"Seed summary written to {out_path}")
