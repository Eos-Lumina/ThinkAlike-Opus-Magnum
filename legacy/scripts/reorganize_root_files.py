import os
import shutil
from pathlib import Path

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define moves for root MD files
ROOT_MD_MOVES = {
    "AGENT_ACTION_PLAN.md": "docs/project/agent_action_plan.md",
    "SYSTEM_BLUEPRINT.md": "docs/architecture/system_blueprint.md",
    "TESTING.md": "docs/guides/development/general/testing_overview.md",
    "ROADMAP.md": "docs/project/roadmap.md",
    "RELEASE_NOTES.md": "docs/project/release_notes.md",
    "PROJECT_INDEX.md": "docs/project/project_index.md",
}

# Files that should stay in root
ROOT_KEEP = {
    "README.md",  # Project entry point
    "LICENSE",  # Standard location
    "package.json",  # NPM configuration
    "next.config.js",  # Next.js configuration
    "tsconfig.json",  # TypeScript configuration
    "requirements.txt",  # Python dependencies
}


def ensure_dir(path):
    """Create directory if it doesn't exist"""
    if not os.path.exists(path):
        os.makedirs(path)


def move_file(src, dest):
    """Move a file and create destination directory if needed"""
    if os.path.exists(src):
        dest_dir = os.path.dirname(dest)
        ensure_dir(dest_dir)
        shutil.move(src, dest)
        print(f"Moved {src} to {dest}")
    else:
        print(f"Source file not found: {src}")


def reorganize_root_files():
    """Move documentation files from root to appropriate locations"""
    for src, dest in ROOT_MD_MOVES.items():
        src_path = os.path.join(ROOT_DIR, src)
        dest_path = os.path.join(ROOT_DIR, dest)
        move_file(src_path, dest_path)


def update_readme_links():
    """Update links in README.md to point to new locations"""
    readme_path = os.path.join(ROOT_DIR, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Update links to moved files
        for old_file, new_file in ROOT_MD_MOVES.items():
            content = content.replace(f"]({old_file})", f"]({new_file})")

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated links in README.md")


def main():
    print("Starting root file reorganization...")
    reorganize_root_files()
    update_readme_links()
    print("Reorganization complete!")


if __name__ == "__main__":
    main()
