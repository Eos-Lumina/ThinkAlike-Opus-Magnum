import subprocess
import sys
import os

def run_command(command_list):
    """
    Runs a system command using subprocess and prints the output.
    :param command_list: A list of command arguments to be executed.
    """
    try:
        result = subprocess.run(command_list, capture_output=True, text=True, check=True)
        print(result.stdout)
        print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error running command {command_list}: {e.stdout}\n{e.stderr}")

def fix_code_style(file_path):
    """
    Applies code style and formatting fixes to the specified file or directory.
    :param file_path: Path to the file or directory that needs style fixing.
    """
    # 1. Format code with black for consistent indentation, line length, etc.
    run_command(["black", "--line-length", "88", file_path])

    # 2. Optionally sort imports (pep8 compliant)
    run_command(["isort", file_path])

    # 3. Format docstrings/comments for better documentation
    run_command([
        "docformatter",
        "--in-place",
        "--wrap-summaries", "88",
        "--wrap-descriptions", "88",
        file_path,
    ])

    # 4. (Optional) Check with Flake8 and pep8-naming plugin to identify naming convention issues
    #    Note: This step does not fix naming automatically—it only reports issues.
    run_command(["flake8", "--select", "N", file_path])  # 'N' indicates pep8-naming detection

def main():
    """
    Main function that checks command-line arguments and then runs the style fixer.
    """
    if len(sys.argv) < 2:
        print("Usage: python style_fixer.py path/to/your/code.py")
        sys.exit(1)

    target_path = sys.argv[1]

    # Ensure the file or directory exists
    if not os.path.exists(target_path):
        print(f"Error: The path '{target_path}' does not exist.")
        sys.exit(1)

    fix_code_style(target_path)
    print("Code style fix process completed.")

if __name__ == "__main__":
    main()
