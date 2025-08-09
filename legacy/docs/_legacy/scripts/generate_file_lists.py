import os

# 1. List all files under archive_legacy
with open('archive_legacy_file_list.txt', 'w', encoding='utf-8') as out:
    for root, dirs, files in os.walk(r'F:\ThinkAlike_Project\archive_legacy'):
        for file in files:
            out.write(os.path.join(root, file) + '\n')

# 2. List all files under F:\ThinkAlike_Project, excluding certain folders
def is_excluded(path):
    exclude = [
        os.path.normpath(r'F:\ThinkAlike_Project\.github'),
        os.path.normpath(r'F:\ThinkAlike_Project\_git_disabled'),
        os.path.normpath(r'F:\ThinkAlike_Project\archive_legacy'),
        os.path.normpath(r'F:\ThinkAlike_Project\.vscode'),
        os.path.normpath(r'F:\ThinkAlike_Project\vaults'),
    ]
    for ex in exclude:
        if os.path.commonpath([ex, path]) == ex:
            return True
    return False

with open('project_file_list.txt', 'w', encoding='utf-8') as out:
    for root, dirs, files in os.walk(r'F:\ThinkAlike_Project'):
        if is_excluded(root):
            dirs[:] = []  # Don't recurse into excluded dirs
            continue
        for file in files:
            out.write(os.path.join(root, file) + '\n')
