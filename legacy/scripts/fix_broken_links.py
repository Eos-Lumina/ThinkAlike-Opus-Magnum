import os
import re
from pathlib import Path


def find_markdown_links(content):
    """Find all markdown links in content"""
    return re.findall(r"\[([^\]]+)\]\(([^\)]+)\)", content)


def resolve_path(file_path, link_path):
    """Resolve a relative link path to its absolute path"""
    if link_path.startswith("http"):
        return None  # External link

    # Convert Windows paths to forward slashes
    link_path = link_path.replace("\\", "/")

    # Handle absolute paths
    if link_path.startswith("/"):
        return link_path[1:]

    # Resolve relative path
    current_dir = os.path.dirname(file_path)
    absolute_path = os.path.normpath(os.path.join(current_dir, link_path))
    return os.path.relpath(absolute_path, os.path.dirname(file_path)).replace("\\", "/")


def update_broken_links(file_path):
    """Update broken links in a file"""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    links = find_markdown_links(content)
    updated = False

    for link_text, link_path in links:
        if link_path.startswith("http"):
            continue

        resolved_path = resolve_path(file_path, link_path)
        if not os.path.exists(resolved_path):
            # Try to find the file elsewhere
            possible_locations = [
                f"docs/{link_path}",
                f"docs/guides/{link_path}",
                f"docs/architecture/{link_path}",
                link_path.replace("_", "-").lower(),
            ]

            for new_path in possible_locations:
                if os.path.exists(new_path):
                    relative_path = os.path.relpath(
                        new_path, os.path.dirname(file_path)
                    ).replace("\\", "/")
                    content = content.replace(
                        f"[{link_text}]({link_path})", f"[{link_text}]({relative_path})"
                    )
                    updated = True
                    print(
                        f"Updated link in {file_path}: {link_path} -> {relative_path}"
                    )
                    break

    if updated:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)


def main():
    print("Checking and fixing broken links...")

    # Walk through all directories
    for root, dirs, files in os.walk("."):
        if any(
            exclude in root
            for exclude in [".git", "node_modules", "__pycache__", ".next"]
        ):
            continue

        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                update_broken_links(file_path)

    print("Link check and fix complete!")


if __name__ == "__main__":
    main()
