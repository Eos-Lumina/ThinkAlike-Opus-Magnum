import os
import re
from pathlib import Path


def check_markdown_links(file_path):
    """Check if markdown links in a file are valid"""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find all markdown links
    links = re.findall(r"\[([^\]]+)\]\(([^\)]+)\)", content)

    issues = []
    for link_text, link_path in links:
        if link_path.startswith("http"):
            continue

        # Convert relative path to absolute
        if link_path.startswith("./"):
            link_path = link_path[2:]
        elif link_path.startswith("../"):
            current_dir = os.path.dirname(file_path)
            link_path = os.path.normpath(os.path.join(current_dir, link_path))
        else:
            link_path = os.path.normpath(
                os.path.join(os.path.dirname(file_path), link_path)
            )

        if not os.path.exists(link_path):
            issues.append(f"Broken link in {file_path}: [{link_text}]({link_path})")

    return issues


def check_file_content(file_path):
    """Check if a file has content"""
    if os.path.getsize(file_path) == 0:
        return [f"Empty file: {file_path}"]
    return []


def main():
    print("Starting file integrity check...")

    issues = []

    # Walk through all directories
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith((".md", ".mdx")):
                file_path = os.path.join(root, file)

                # Check file content
                issues.extend(check_file_content(file_path))

                # Check markdown links
                issues.extend(check_markdown_links(file_path))

    if issues:
        print("\nFound issues:")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("\nNo issues found. All files have content and links are valid.")


if __name__ == "__main__":
    main()
