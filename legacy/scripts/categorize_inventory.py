"""
Script to categorize project inventory based on PROJECT_FILE_INDEX.md and
output categorized_inventory.yaml.
"""

import os

import yaml

# This script categorizes the project file inventory.
# It reads a list of files and categorizes them based on their path.


def load_file_index(path):
    with open(path, encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines


def categorize(paths):
    # Define category patterns
    category_defs = [
        ("src", lambda p: p.startswith("src/")),
        ("docs/architecture", lambda p: p.startswith("docs/architecture/")),
        ("docs/protocols", lambda p: p.startswith("docs/protocols/")),
        ("docs/ui_components", lambda p: p.startswith("docs/ui_components/")),
        ("tests", lambda p: p.startswith("tests/")),
        ("scripts", lambda p: p.startswith("scripts/")),
        ("assets", lambda p: p.startswith("assets/")),
        ("public", lambda p: p.startswith("public/")),
    ]
    categorized = {name: [] for name, _ in category_defs}
    categorized["legacy"] = []
    for p in paths:
        normalized = p.replace("\\", "/")
        matched = False
        for name, match_fn in category_defs:
            if match_fn(normalized):
                categorized[name].append(p)
                matched = True
                break
        if not matched:
            categorized["legacy"].append(p)
    return categorized


def categorize_inventory(file_list_path, categories_path, output_path):
    """Categorizes the file inventory."""
    with open(file_list_path, "r", encoding="utf-8") as f:
        files = [line.strip() for line in f]

    with open(categories_path, "r", encoding="utf-8") as f:
        categories = yaml.safe_load(f)

    categorized_files = {category: [] for category in categories}

    for file in files:
        for category, keywords in categories.items():
            if any(keyword in file for keyword in keywords):
                categorized_files[category].append(file)
                break

    with open(output_path, "w", encoding="utf-8") as f:
        yaml.dump(categorized_files, f, default_flow_style=False)


def main():
    # Determine project root
    script_dir = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(script_dir, os.pardir))
    index_path = os.path.join(project_root, "PROJECT_FILE_INDEX.md")
    if not os.path.exists(index_path):
        print(f"ERROR: {index_path} not found.")
        return

    paths = load_file_index(index_path)
    categories = categorize(paths)

    output_path = os.path.join(script_dir, "categorized_inventory.yaml")
    with open(output_path, "w", encoding="utf-8") as out_f:
        yaml.safe_dump(categories, out_f, sort_keys=False)

    print(f"Categorized inventory written to: {output_path}")


if __name__ == "__main__":
    main()
    # categorize_inventory(
    #     "project_file_list.txt",
    #     "categories.yaml",
    #     "categorized_inventory.yaml",
    # )
