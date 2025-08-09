import os

# Set the paths for your current project and legacy folder
PROJECT_ROOT = os.path.abspath(os.getcwd())
LEGACY_DIR = os.path.join(PROJECT_ROOT, '_legacy')

# Helper: Get all markdown files in a directory tree
def get_all_md_files(root):
    md_files = set()
    for subdir, _, files in os.walk(root):
        for file in files:
            if file.endswith('.md'):
                md_files.add(os.path.relpath(os.path.join(subdir, file), root))
    return md_files

if __name__ == '__main__':
    # 1. Get all markdown files in the main project (excluding _legacy)
    main_md_files = get_all_md_files(PROJECT_ROOT)
    # Remove _legacy files from the main set
    main_md_files = {f for f in main_md_files if not f.startswith('_legacy')}

    # 2. Get all markdown files in the _legacy folder
    legacy_md_files = get_all_md_files(LEGACY_DIR)

    # 3. Find legacy files not present in the main project
    not_migrated = sorted([f for f in legacy_md_files if f not in main_md_files])

    # 4. Output the list
    with open('not_migrated_from_legacy.txt', 'w', encoding='utf-8') as out:
        for f in not_migrated:
            out.write(f + '\n')
    print(f"Found {len(not_migrated)} legacy markdown files not yet migrated. See not_migrated_from_legacy.txt.")
