import os
import shutil
import json
from pathlib import Path
import re

# --- Configuration ---
PROJECT_ROOT_ARCHIVE = Path(r"f:\\ThinkAlike_Project\\archive_legacy\\project_root_archive")
LEGACY_TXT_DIR = Path(r"f:\\ThinkAlike_Project\\archive_legacy\\legacy_txt")
LEGACY_DEVS_DIR = Path(r"f:\\ThinkAlike_Project\\archive_legacy\\legacy_devs")
SCRIPTS_DIR = Path(r"f:\\ThinkAlike_Project\\scripts")

PROCESSED_LOG_FILE = SCRIPTS_DIR / "non_md_processed_files.log"
REPORT_FILE = SCRIPTS_DIR / "non_md_migration_report.txt"

DEV_EXTENSIONS = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".java", ".c", ".cpp", ".h", ".hpp", ".cs", ".go", ".rb", ".php", ".swift",
    ".kt", ".kts", ".gradle", ".html", ".css", ".scss", ".less", ".sql", ".config", ".ini", ".toml", ".yaml", ".yml",
    ".json", ".xml", ".sh", ".bat", ".ps1", ".ipynb", ".dockerfile", "Dockerfile", ".tf", ".tfvars", ".hcl",
    ".puml", ".plantuml", ".mermaid", ".mmd", ".cfg", ".conf", ".settings", ".csproj", ".sln", ".vb", ".fs"
}
# Markdown files are handled separately and should be skipped by this script.
# .md is intentionally omitted from DEV_EXTENSIONS for this script.

ARCHIVE_EXTENSIONS = {".zip", ".tar", ".gz", ".rar", ".7z", ".bz2", ".xz"}
OFFICE_EXTENSIONS = {
    ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".ods", ".odp", ".rtf", ".csv"
}
IMAGE_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".tif", ".svg", ".webp", ".ico", ".psd", ".ai"
}

# Files/folders to explicitly ignore
IRRELEVANT_FILENAMES = {"Thumbs.db", ".DS_Store", "desktop.ini"}
IRRELEVANT_EXTENSIONS = {
    ".tmp", ".bak", ".log", ".exe", ".dll", ".o", ".so", ".class", ".pyc", ".cache", ".swp", ".swo",
    ".lock", ".obj", ".pdb", ".ilk", ".ncb", ".suo", ".user"
} | IMAGE_EXTENSIONS # Add image extensions to irrelevant ones

IRRELEVANT_FOLDERS = {"node_modules", ".git", ".svn", "__pycache__", ".vscode", ".idea", "target", "build", "dist"}

# Specific chatlog files mentioned by user (relative to PROJECT_ROOT_ARCHIVE)
SPECIFIC_CHATLOG_FILES = {
    "chat.txt",
    "chat.html",
    "conversations.json",
    "message_feedback.json",
    "shared_conversations.json",
    "user.json" # Technically user data, but requested to be handled as chatlog
}
CHATLOG_KEYWORDS = [
    "idea", "resource", "link", "algorithm", "feature", "bug", "suggestion", "important", "todo",
    "remember", "concept", "plan", "strategy", "insight", "valuable", "key"
]
CHATLOG_KEYWORD_REGEX = re.compile(r"\\b(" + "|".join(CHATLOG_KEYWORDS) + r")\\b", re.IGNORECASE)


# --- Helper Functions ---
def load_processed_files():
    """Loads the set of already processed file paths from the log file."""
    if not PROCESSED_LOG_FILE.exists():
        return set()
    with open(PROCESSED_LOG_FILE, "r", encoding="utf-8") as f:
        return {Path(line.strip()) for line in f if line.strip()}

def add_to_processed_log(filepath_str, report_lines_list, main_report_list):
    """Adds a file to the processed log and its status to the main report."""
    with open(PROCESSED_LOG_FILE, "a", encoding="utf-8") as f:
        f.write(str(filepath_str) + "\\n")
    main_report_list.extend(report_lines_list)

def get_file_category(filepath: Path):
    """Categorizes a file based on its extension and name."""
    filename = filepath.name
    extension = filepath.suffix.lower()
    parent_dir_name = filepath.parent.name

    if filename in IRRELEVANT_FILENAMES or extension in IRRELEVANT_EXTENSIONS:
        return "irrelevant_file_type"
    if extension == ".md":
        return "markdown" # Should be skipped
    if extension == ".txt":
        return "txt"
    if extension in ARCHIVE_EXTENSIONS:
        return "archive"
    if extension in OFFICE_EXTENSIONS:
        return "office"
    if extension in DEV_EXTENSIONS: # Covers .json, .html etc.
        return "dev"
    # If it's a known chatlog file, ensure it's categorized as such for keyword scanning
    if filename in SPECIFIC_CHATLOG_FILES:
        if extension == ".txt": return "chatlog_txt"
        return "chatlog_dev" # for .json, .html

    # Fallback for unknown files
    return "unknown"

def scan_chatlog_content(filepath: Path, report_lines_list):
    """Scans text-based chatlog content for keywords."""
    try:
        content = filepath.read_text(encoding="utf-8", errors="ignore")
        found_keywords = CHATLOG_KEYWORD_REGEX.findall(content)
        if found_keywords:
            report_lines_list.append(f"    INFO: Found keywords in {filepath.name}: {', '.join(set(k.lower() for k in found_keywords[:5]))}{'...' if len(found_keywords) > 5 else ''}")
            return True
    except Exception as e:
        report_lines_list.append(f"    WARNING: Could not read/scan chatlog {filepath}: {e}")
    return False

def migrate_file(src_path: Path, category: str, original_rel_path: Path, report_lines_list):
    """Moves a file to its new categorized location."""
    dest_base_dir = None
    special_subdir = ""

    if category == "txt" or category == "chatlog_txt":
        dest_base_dir = LEGACY_TXT_DIR
    elif category == "dev" or category == "chatlog_dev":
        dest_base_dir = LEGACY_DEVS_DIR
    elif category == "archive":
        dest_base_dir = LEGACY_DEVS_DIR
        special_subdir = "archives_to_inspect"
    elif category == "office":
        dest_base_dir = LEGACY_DEVS_DIR
        special_subdir = "office_documents_to_review"
    else:
        report_lines_list.append(f"  SKIPPED (Unhandled Category): {src_path} (Category: {category})")
        return

    # Construct destination path
    # original_rel_path is relative to PROJECT_ROOT_ARCHIVE, e.g., "subdir/file.txt" or "file.txt"
    # We want to place it into dest_base_dir / special_subdir / original_rel_path.parent / original_rel_path.name

    if original_rel_path.name == str(original_rel_path): # File is in PROJECT_ROOT_ARCHIVE root
        dest_dir = dest_base_dir / special_subdir
    else:
        dest_dir = dest_base_dir / special_subdir / original_rel_path.parent

    dest_path = dest_dir / src_path.name

    try:
        dest_dir.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src_path), str(dest_path))
        report_lines_list.append(f"  MOVED: {src_path} -> {dest_path}")

        # If it's a chatlog, scan its content (now that it's moved)
        is_chatlog_category = category.startswith("chatlog")
        # Check if the original path indicated it was in a temp inspect folder and is a txt file
        # This part might need adjustment if _TEMP_INSPECT is not part of the src_path directly
        # For now, assuming it could be part of the path if files were manually placed there before script run.
        is_in_temp_inspect = False # Simplified, as _TEMP_INSPECT is not a standard source for this script.

        if is_chatlog_category:
            scan_chatlog_content(dest_path, report_lines_list)

    except Exception as e:
        report_lines_list.append(f"  ERROR migrating {src_path} to {dest_path}: {e}")

# --- Main Logic ---
def main():
    main_report = [f"Non-Markdown Migration Report - {Path(__file__).name}\\n"]
    processed_files = load_processed_files()
    files_processed_this_run = 0
    files_skipped_this_run = 0
    files_moved_this_run = 0
    errors_this_run = 0

    main_report.append(f"Starting scan of: {PROJECT_ROOT_ARCHIVE}\\n")

    # Ensure target base directories exist
    LEGACY_TXT_DIR.mkdir(parents=True, exist_ok=True)
    LEGACY_DEVS_DIR.mkdir(parents=True, exist_ok=True)
    (LEGACY_DEVS_DIR / "archives_to_inspect").mkdir(parents=True, exist_ok=True)
    (LEGACY_DEVS_DIR / "office_documents_to_review").mkdir(parents=True, exist_ok=True)


    for dirpath, dirnames, filenames in os.walk(PROJECT_ROOT_ARCHIVE, topdown=True):
        current_dir = Path(dirpath)
        current_report_lines = []
        
        # Prevent processing of target migration directories if they are nested within source
        # This check is crucial if PROJECT_ROOT_ARCHIVE might contain LEGACY_TXT_DIR or LEGACY_DEVS_DIR
        # (e.g. if script is run multiple times with slightly different target paths that might overlap with source)
        if LEGACY_TXT_DIR.is_relative_to(current_dir) and current_dir != LEGACY_TXT_DIR:
             # current_dir is a parent of LEGACY_TXT_DIR, or LEGACY_TXT_DIR itself
            if str(LEGACY_TXT_DIR.name) in dirnames:
                dirnames.remove(LEGACY_TXT_DIR.name)
        if LEGACY_DEVS_DIR.is_relative_to(current_dir) and current_dir != LEGACY_DEVS_DIR:
            if str(LEGACY_DEVS_DIR.name) in dirnames:
                dirnames.remove(LEGACY_DEVS_DIR.name)

        # Skip irrelevant folders
        dirnames[:] = [d for d in dirnames if d not in IRRELEVANT_FOLDERS]

        if current_dir.name in IRRELEVANT_FOLDERS:
            current_report_lines.append(f"Skipping irrelevant directory: {current_dir}")
            main_report.extend(current_report_lines)
            continue
        
        # Skip the actual target directories themselves if encountered during the walk
        if current_dir == LEGACY_TXT_DIR or current_dir == LEGACY_DEVS_DIR:
            main_report.append(f"Skipping processing of target migration directory: {current_dir}")
            dirnames[:] = [] # Don't recurse further into these
            continue

        for filename in filenames:
            src_filepath = current_dir / filename
            file_report_lines = []

            if src_filepath in processed_files:
                files_skipped_this_run +=1
                continue
            
            if src_filepath == PROCESSED_LOG_FILE or src_filepath == REPORT_FILE:
                file_report_lines.append(f"  SKIPPED (Self log/report file): {src_filepath}")
                add_to_processed_log(src_filepath, file_report_lines, main_report)
                files_skipped_this_run +=1
                continue

            files_processed_this_run += 1
            category = get_file_category(src_filepath)
            original_relative_path = src_filepath.relative_to(PROJECT_ROOT_ARCHIVE)

            if category == "markdown":
                file_report_lines.append(f"  SKIPPED (Markdown, handled by other script): {src_filepath}")
                files_skipped_this_run +=1
            elif category == "irrelevant_file_type":
                file_report_lines.append(f"  SKIPPED (Irrelevant type/name): {src_filepath}")
                files_skipped_this_run +=1
            elif category == "unknown":
                file_report_lines.append(f"  SKIPPED (Unknown type, needs review): {src_filepath}")
                files_skipped_this_run +=1
            else: # txt, dev, archive, office, chatlog_txt, chatlog_dev
                migrate_file(src_filepath, category, original_relative_path, file_report_lines)
                if any("ERROR" in line for line in file_report_lines):
                    errors_this_run +=1
                elif any("MOVED" in line for line in file_report_lines):
                    files_moved_this_run +=1
                else: # Skipped due to unhandled category inside migrate_file or other logic
                    files_skipped_this_run +=1
            
            add_to_processed_log(src_filepath, file_report_lines, main_report)

    main_report.append(f"\\n--- Summary ---")
    main_report.append(f"Total files encountered for potential processing (excluding already logged before this run): {files_processed_this_run}")
    main_report.append(f"Files moved this run: {files_moved_this_run}")
    main_report.append(f"Files skipped this run (irrelevant, markdown, unknown, etc.): {files_skipped_this_run}")
    main_report.append(f"Total files in processed log (includes all runs): {len(load_processed_files())}")
    main_report.append(f"Errors this run: {errors_this_run}")
    main_report.append(f"Processed log: {PROCESSED_LOG_FILE}")
    main_report.append(f"Full report: {REPORT_FILE}")

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("\\n".join(main_report))

    print("\\n".join(main_report)) # Print summary to console
    # print(f"\\nDetailed report written to {REPORT_FILE}")
    # print(f"Processed files log updated: {PROCESSED_LOG_FILE}")

if __name__ == "__main__":
    main()
