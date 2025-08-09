import argparse
import os
from pathlib import Path

# NOTE: Only reference canonical documentation in docs/contributors/ and
# test plan in tests/testing_and_validation_plan.md.
# Deprecated folders/files (e.g., docs/guides/contributor_guides/,
# docs/project/archive/testing_and_validation_plan.md) must not be recreated.

# Common folders to exclude from the scan
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


def generate_file_list(root: Path, output_file: Path):
    """
    Walks the project root and writes all non-excluded file paths to the
    output file.
    """
    with open(output_file, "w", encoding="utf-8") as out:
        for dirpath, dirnames, files in os.walk(root, topdown=True):
            # Modify dirnames in-place to prune traversal
            dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]

            for file in sorted(files):
                try:
                    full_path = Path(dirpath) / file
                    rel_path = full_path.relative_to(root)
                    out.write(f"{rel_path.as_posix()}\n")
                except Exception as e:
                    print(f"Error processing file {full_path}: {e}")


def main():
    """Main function to generate the file index."""
    parser = argparse.ArgumentParser(
        description="Generate a list of all files in the project, excluding "
        "specified directories."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="The root directory of the project.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default="PROJECT_FILE_INDEX.md",
        help="The name of the output file.",
    )
    args = parser.parse_args()

    print(
        f"Generating file index for '{args.root.resolve()}' into "
        f"'{args.output.resolve()}'"
    )
    generate_file_list(args.root, args.output)
    print("✅ File index generation complete.")


if __name__ == "__main__":
    main()
