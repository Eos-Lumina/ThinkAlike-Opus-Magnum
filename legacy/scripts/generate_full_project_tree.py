from __future__ import annotations

import argparse
from pathlib import Path

# NOTE: Only reference canonical documentation in docs/contributors/ and
# test plan in tests/testing_and_validation_plan.md.
# Deprecated folders/files (e.g., docs/guides/contributor_guides/,
# docs/project/archive/testing_and_validation_plan.md) must not be recreated
# or referenced.

# Directories to exclude from the tree view
EXCLUDE_DIRS = {
    ".git",
    "node_modules",
    ".next",
    ".vscode",
    "vaults",
    "archive_legacy",
    "venv",
    ".venv",
    "__pycache__",
    "dist",
    "build",
}


def create_tree(dir_path: Path, prefix: str = "", exclude: set = None) -> list[str]:
    """Recursively creates a string representation of the directory tree."""
    if exclude is None:
        exclude = set()
    lines = []
    contents = sorted(
        [p for p in dir_path.iterdir() if p.name not in exclude],
        key=lambda p: (p.is_file(), p.name.lower()),
    )
    for i, path in enumerate(contents):
        connector = "├── " if i < len(contents) - 1 else "└── "
        lines.append(f"{prefix}{connector}{path.name}")
        if path.is_dir():
            extension = "│   " if i < len(contents) - 1 else "    "
            lines.extend(create_tree(path, prefix=prefix + extension, exclude=exclude))
    return lines


def main():
    """Main function to generate and save the project tree."""
    parser = argparse.ArgumentParser(
        description="Generate a textual representation of the project "
        "directory tree."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).parent.parent,
        help="The root directory to generate the tree from.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default="full_project_tree.txt",
        help="The file to save the project tree to.",
    )
    args = parser.parse_args()

    print(f"Generating project tree for: {args.root.resolve()}")
    try:
        tree_lines = create_tree(args.root, exclude=EXCLUDE_DIRS)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(f"{args.root.name}/\n")
            f.write("\n".join(tree_lines))
        print(f"✅ Project tree saved to {args.output.resolve()}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    main()
