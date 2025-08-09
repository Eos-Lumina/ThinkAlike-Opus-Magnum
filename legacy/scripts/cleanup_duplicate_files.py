#!/usr/bin/env python3
"""
Cleanup Duplicate Files Script
Removes hyphenated duplicates and consolidates content to underscore versions
"""

import difflib
import os
import shutil
from pathlib import Path


def find_duplicate_pairs(root_dir):
    """Find pairs of files that differ only by underscore vs hyphen"""
    pairs = []

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if "-" in file and file.endswith(".py"):
                # Check if there's an underscore version
                underscore_version = file.replace("-", "_")
                underscore_path = os.path.join(root, underscore_version)
                hyphen_path = os.path.join(root, file)

                if os.path.exists(underscore_path):
                    pairs.append((hyphen_path, underscore_path))

    return pairs


def compare_and_merge_files(hyphen_file, underscore_file):
    """Compare files and merge content if needed"""

    # Read both files
    try:
        with open(hyphen_file, "r", encoding="utf-8") as f:
            hyphen_content = f.read()
    except:
        hyphen_content = ""

    try:
        with open(underscore_file, "r", encoding="utf-8") as f:
            underscore_content = f.read()
    except:
        underscore_content = ""

    # If underscore file is empty but hyphen has content, copy content
    if not underscore_content.strip() and hyphen_content.strip():
        print(f"Copying content from {hyphen_file} to {underscore_file}")
        with open(underscore_file, "w", encoding="utf-8") as f:
            f.write(hyphen_content)
        return True

    # If both have content, show differences
    elif hyphen_content.strip() and underscore_content.strip():
        if hyphen_content != underscore_content:
            print(f"WARNING: Both files have different content:")
            print(f"  Hyphen: {hyphen_file}")
            print(f"  Underscore: {underscore_file}")

            # Show diff
            diff = list(
                difflib.unified_diff(
                    underscore_content.splitlines(keepends=True),
                    hyphen_content.splitlines(keepends=True),
                    fromfile=underscore_file,
                    tofile=hyphen_file,
                )
            )

            if diff:
                print("Differences:")
                for line in diff[:20]:  # Show first 20 lines of diff
                    print(f"  {line.rstrip()}")
                if len(diff) > 20:
                    print(f"  ... and {len(diff) - 20} more lines")
        return False

    return True


def cleanup_duplicates():
    """Main cleanup function"""
    root_dir = Path(__file__).parent.parent
    print(f"Cleaning up duplicates in: {root_dir}")

    pairs = find_duplicate_pairs(root_dir)

    if not pairs:
        print("No duplicate pairs found!")
        return

    print(f"Found {len(pairs)} duplicate pairs:")

    removed_count = 0
    merged_count = 0

    for hyphen_file, underscore_file in pairs:
        print(f"\nProcessing pair:")
        print(f"  Hyphen: {hyphen_file}")
        print(f"  Underscore: {underscore_file}")

        # Try to merge content
        if compare_and_merge_files(hyphen_file, underscore_file):
            try:
                os.remove(hyphen_file)
                print(f"  ✅ Removed: {hyphen_file}")
                removed_count += 1
                if os.path.getsize(underscore_file) > 0:
                    merged_count += 1
            except Exception as e:
                print(f"  ❌ Error removing {hyphen_file}: {e}")
        else:
            print(f"  ⚠️  Manual review needed for: {hyphen_file}")

    print(f"\n📊 Summary:")
    print(f"  Files removed: {removed_count}")
    print(f"  Content merged: {merged_count}")
    print(f"  Manual review needed: {len(pairs) - removed_count}")


if __name__ == "__main__":
    cleanup_duplicates()
