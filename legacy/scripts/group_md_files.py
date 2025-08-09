import os
import hashlib
import difflib
from collections import defaultdict

ARCHIVE_DIR = r"F:\ThinkAlike_Project\archive_legacy"
OUTPUT_FILE = r"F:\ThinkAlike_Project\scripts\md_file_groups.txt"

# Keywords for grouping by topic
TOPIC_KEYWORDS = {
    'architecture': ['architecture', 'design', 'structure'],
    'planning': ['plan', 'roadmap', 'milestone', 'timeline'],
    'ethics': ['ethic', 'value', 'principle'],
    'testing': ['test', 'validation', 'qa'],
    'documentation': ['doc', 'readme', 'manual', 'guide'],
    'uiux': ['ui', 'ux', 'interface', 'style'],
    'security': ['security', 'privacy', 'compliance'],
    'agent': ['agent', 'ai', 'bot'],
    'other': []
}


def get_md_files(base_dir):
    md_files = []
    for root, _, files in os.walk(base_dir):
        for f in files:
            if f.lower().endswith('.md'):
                md_files.append(os.path.join(root, f))
    return md_files


def sha256sum(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


def get_first_line(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    return line.strip()
    except Exception:
        return ''
    return ''


def group_by_topic(files):
    groups = defaultdict(list)
    for f in files:
        fname = os.path.basename(f).lower()
        assigned = False
        for topic, keywords in TOPIC_KEYWORDS.items():
            if any(kw in fname for kw in keywords):
                groups[topic].append(f)
                assigned = True
                break
        if not assigned:
            groups['other'].append(f)
    return groups


def find_duplicates(files):
    hash_map = defaultdict(list)
    for f in files:
        try:
            h = sha256sum(f)
            hash_map[h].append(f)
        except Exception:
            continue
    return hash_map


def find_similar_names(files):
    name_map = defaultdict(list)
    for f in files:
        name = os.path.splitext(os.path.basename(f))[0].lower()
        name_map[name].append(f)
    return name_map


def find_near_duplicates(files):
    # Use first 2KB for quick similarity check
    content_map = defaultdict(list)
    for f in files:
        try:
            with open(f, 'r', encoding='utf-8') as file:
                snippet = file.read(2048)
            content_map[snippet].append(f)
        except Exception:
            continue
    # Now, compare snippets for high similarity
    near_dups = defaultdict(list)
    checked = set()
    for snippet1, files1 in content_map.items():
        for f1 in files1:
            if f1 in checked:
                continue
            group = [f1]
            for snippet2, files2 in content_map.items():
                if snippet1 == snippet2:
                    continue
                for f2 in files2:
                    if f2 in checked or f2 == f1:
                        continue
                    ratio = difflib.SequenceMatcher(None, snippet1, snippet2).ratio()
                    if ratio > 0.85:
                        group.append(f2)
                        checked.add(f2)
            if len(group) > 1:
                for f in group:
                    checked.add(f)
                near_dups[f1] = group
    return near_dups


def main():
    md_files = get_md_files(ARCHIVE_DIR)
    topic_groups = group_by_topic(md_files)
    hash_map = find_duplicates(md_files)
    name_map = find_similar_names(md_files)
    near_dups = find_near_duplicates(md_files)

    try:
        print(f"Found {len(md_files)} markdown files. Writing to {OUTPUT_FILE}")
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
            out.write("# Markdown File Grouping and Duplicate Report\n\n")
            for topic, files in topic_groups.items():
                out.write(f"## {topic.capitalize()} Files ({len(files)})\n\n")
                for f in files:
                    fname = os.path.basename(f)
                    first_line = get_first_line(f)
                    # Check for exact duplicate
                    is_dup = any(len(v) > 1 and f in v for v in hash_map.values())
                    # Check for near-duplicate
                    is_near_dup = any(f in v for v in near_dups.values())
                    # Check for name duplicates
                    name = os.path.splitext(fname)[0].lower()
                    is_name_dup = len(name_map[name]) > 1
                    status = []
                    if is_dup:
                        status.append("DUPLICATE")
                    if is_near_dup:
                        status.append("NEAR-DUPLICATE")
                    if is_name_dup:
                        status.append("NAME-DUPLICATE")
                    status_str = f" [{'|'.join(status)}]" if status else ''
                    out.write(f"- {f}{status_str}\n    - First line: {first_line[:80]}\n    - Suggest: [KEEP] [REVIEW] [DISCARD]\n")
                out.write("\n")
            out.write("# End of Report\n")
        print(f"Output written to: {os.path.abspath(OUTPUT_FILE)}")
    except Exception as e:
        print(f"Error writing output: {e}")

if __name__ == "__main__":
    main()
