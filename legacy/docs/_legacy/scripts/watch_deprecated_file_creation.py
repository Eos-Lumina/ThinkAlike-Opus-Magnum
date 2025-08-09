import os
import time
import traceback
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# This script watches for the creation of deprecated files.

DEPRECATED_FILES = ["old_config.yaml", "temp_data.csv"]

# Paths to monitor
WATCH_PATHS = [
    Path("docs/project/archive/testing_and_validation_plan.md"),
    Path("docs/project/archive/testing_and_validation_plan_tests.md"),
    Path("docs/guides/contributor_guides/"),
]
# Always watch the root docs folder so missing subpaths don’t break the observer
WATCH_ROOT = Path("docs")

LOG_FILE = "deprecated_file_creation.log"
# Ensure the log file exists before starting
_log_path = Path(LOG_FILE)
try:
    _log_path.touch(exist_ok=True)
    print(f"Using log file: {_log_path.resolve()}")
except Exception as _e:
    print(f"Failed to create log file '{LOG_FILE}': {_e}")


class DeprecatedFileHandler(FileSystemEventHandler):
    """Handles the creation of deprecated files."""

    def on_created(self, event):
        for watch_path in WATCH_PATHS:
            # Check for file or directory creation
            if watch_path.is_dir():
                if event.src_path.startswith(str(watch_path)):
                    self.log_event(event.src_path, is_dir=True)
            else:
                if os.path.abspath(event.src_path) == str(watch_path.resolve()):
                    self.log_event(event.src_path, is_dir=False)
        if (
            not event.is_directory
            and os.path.basename(event.src_path) in DEPRECATED_FILES
        ):
            print(f"Warning: Deprecated file created: {event.src_path}")

    def log_event(self, path, is_dir):
        msg = f"[DETECTED] {'Directory' if is_dir else 'File'} created: {path}\n"
        msg += f"Timestamp: {time.ctime()}\n"
        msg += f"Current process: {os.getpid()}\n"
        msg += (
            "Stack trace (if available):\n'''"
            f"{''''''.join(traceback.format_stack())}\n"
        )
        print(msg)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(msg + "\n")


def main():
    """Main function to start the watchdog observer."""
    event_handler = DeprecatedFileHandler()
    observer = Observer()
    observer.schedule(event_handler, str(WATCH_ROOT), recursive=True)
    print("Monitoring for deprecated file/folder creation. " "Press Ctrl+C to stop.")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
