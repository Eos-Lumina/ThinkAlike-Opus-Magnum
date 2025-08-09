# NOTE: Only reference canonical documentation in docs/contributors/ and test plan
# in tests/testing_and_validation_plan.md.
# Deprecated folders/files (e.g., docs/guides/contributor_guides/,
# docs/project/archive/testing_and_validation_plan.md) must not be recreated
# or referenced.

import subprocess
import sys


def run_command(command_list):
    """
    Runs a system command using subprocess and prints the output.
    :param command_list: A list of command arguments to be executed.
    """
    try:
        result = subprocess.run(
            command_list, capture_output=True, text=True, check=True
        )
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
    run_command(
        [
            "docformatter",
            "--in-place",
            "--wrap-summaries",
            "88",
            "--wrap-descriptions",
            "88",
            file_path,
        ]
    )

    # 4. (Optional) Check with Flake8 and pep8-naming plugin to identify naming
    #    convention issues
    #    Note: This step does not fix naming automatically—it only reports issues.
    run_command(
        ["flake8", "--select", "N", file_path]
    )  # 'N' indicates pep8-naming detection


def fix_style(fixers: list[str], files: list[str] | None = None):
    """Automatically fixes style issues."""
    for fixer in fixers:
        command = [fixer]
        if files:
            command.extend(files)
        else:
            command.append(".")

        try:
            subprocess.run(command, check=True)
            print(f"Successfully ran {fixer}.")
        except subprocess.CalledProcessError as e:
            print(f"Error running {fixer}: {e}")


def main():
    """
    Main function that checks command-line arguments and then runs the style fixer.
    """
    if len(sys.argv) < 2:
        print("Usage: python style_fixer.py <file_or_directory>")
        sys.exit(1)
    file_to_fix = sys.argv[1]
    fix_code_style(file_to_fix)


if __name__ == "__main__":
    main()
