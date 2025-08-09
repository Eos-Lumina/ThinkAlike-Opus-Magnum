import os

# This script generates a file list for the project.
# It excludes certain directories and files.

EXCLUDED_DIRS = ["__pycache__", ".git", ".vscode", "node_modules"]
EXCLUDED_FILES = [".DS_Store", "package_lock.json"]


def generate_file_list(root_dir):
    """Generates a list of files in a directory.

    Args:
        root_dir: The root directory to start from.

    Returns:
        A list of file paths.
    """
    file_list = []
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        for file in files:
            if file not in EXCLUDED_FILES:
                file_list.append(os.path.join(root, file))
    return file_list


if __name__ == "__main__":
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    files = generate_file_list(project_dir)
    with open("project_file_list.txt", "w", encoding="utf-8") as f:
        for file_path in files:
            f.write(f"{file_path}\n")
