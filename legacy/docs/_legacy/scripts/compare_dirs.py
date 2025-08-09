import os
import hashlib
import argparse
from pathlib import Path


def compute_sha256(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def build_file_map(root_dir):
    file_map = {}
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            abs_path = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(abs_path, root_dir)
            file_map[rel_path] = abs_path
    return file_map

def main(legacy_root, current_root, output_dir):
    legacy_files = build_file_map(legacy_root)
    current_files = build_file_map(current_root)

    identical = []
    different = []
    legacy_only = []
    current_only = []

    for rel_path, legacy_abs in legacy_files.items():
        if rel_path in current_files:
            current_abs = current_files[rel_path]
            legacy_hash = compute_sha256(legacy_abs)
            current_hash = compute_sha256(current_abs)
            if legacy_hash and current_hash:
                if legacy_hash == current_hash:
                    identical.append(rel_path)
                else:
                    different.append(rel_path)
        else:
            legacy_only.append(rel_path)

    for rel_path in current_files:
        if rel_path not in legacy_files:
            current_only.append(rel_path)

    os.makedirs(output_dir, exist_ok=True)
    print(f"Writing output files to: {os.path.abspath(output_dir)}")
    with open(os.path.join(output_dir, 'identical_files.txt'), 'w', encoding='utf-8') as f:
        for path in identical:
            f.write(path + '\n')
    with open(os.path.join(output_dir, 'different_files.txt'), 'w', encoding='utf-8') as f:
        for path in different:
            f.write(path + '\n')
    with open(os.path.join(output_dir, 'legacy_only_files.txt'), 'w', encoding='utf-8') as f:
        for path in legacy_only:
            f.write(path + '\n')
    with open(os.path.join(output_dir, 'current_only_files.txt'), 'w', encoding='utf-8') as f:
        for path in current_only:
            f.write(path + '\n')

    print(f"Identical files: {len(identical)}")
    print(f"Different files: {len(different)}")
    print(f"Legacy only files: {len(legacy_only)}")
    print(f"Current only files: {len(current_only)}")
    print(f"Results written to {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare two directories for identical files using SHA256.")
    parser.add_argument("legacy_root", help="Path to legacy archive root directory")
    parser.add_argument("current_root", help="Path to current project root directory")
    parser.add_argument("--output_dir", default="compare_results", help="Directory to write output lists")
    args = parser.parse_args()
    main(args.legacy_root, args.current_root, args.output_dir)
