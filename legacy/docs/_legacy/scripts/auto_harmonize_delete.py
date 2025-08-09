import os
from pathlib import Path
import sys
import datetime
import shutil

# CONFIGURATION: Set canonical archive locations for each file type
CANONICAL_ARCHIVES = [
    Path('ThinkAlike/ThinkAlike/docs/autumn_leaves/archive'),
    Path('docs/archive'),
]

# Root directory to scan
ROOTS = [Path('.'), Path('ThinkAlike'), Path('ThinkAlike/ThinkAlike')]

# Log file
LOG_FILE = Path('harmonization_log.txt')

# Migration mode: set to True to move unique files into canonical archive
MIGRATE_UNIQUE = True

def log(msg):
    timestamp = datetime.datetime.now().isoformat()
    with open(LOG_FILE, 'a', encoding='utf-8') as logf:
        logf.write(f"[{timestamp}] {msg}\n")
    print(msg)

def is_canonical(file_path):
    for archive in CANONICAL_ARCHIVES:
        try:
            if archive.resolve() in file_path.resolve().parents:
                return True
        except Exception:
            continue
    return False

def find_all_files(filename):
    found = []
    for root in ROOTS:
        for path in root.rglob(filename):
            found.append(path)
    return found

def get_all_md_files():
    all_md = set()
    for root in ROOTS:
        for f in root.rglob('*.md'):
            all_md.add(f)
    return list(all_md)

def get_canonical_path(filename):
    # Prefer the first canonical archive as the destination
    return CANONICAL_ARCHIVES[0] / filename

def main():
    errors = 0
    all_md_files = get_all_md_files()
    for f in all_md_files:
        if is_canonical(f):
            continue
        fname = f.name
        canonical_path = get_canonical_path(fname)
        if not canonical_path.exists():
            if MIGRATE_UNIQUE:
                try:
                    canonical_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(f), str(canonical_path))
                    log(f"[MIGRATE] Moved unique file {f} to canonical archive: {canonical_path}")
                except Exception as e:
                    log(f"[ERROR] Could not migrate {f}: {e}")
                    errors += 1
            else:
                log(f"[SKIP] Unique file {f} not migrated (migration disabled)")
            continue
        # If file exists in canonical, compare content
        try:
            with open(f, 'rb') as nf, open(canonical_path, 'rb') as cf:
                ndata = nf.read()
                cdata = cf.read()
                if ndata == cdata:
                    os.remove(f)
                    log(f"[DELETE] Deleted duplicate {f} (identical to canonical)")
                else:
                    # If different, preserve by renaming and moving
                    if MIGRATE_UNIQUE:
                        new_name = canonical_path.parent / f"{f.stem}_migrated_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}{f.suffix}"
                        shutil.move(str(f), str(new_name))
                        log(f"[MIGRATE] Moved non-identical file {f} to canonical archive as {new_name}")
                    else:
                        log(f"[SKIP] Non-identical file {f} not migrated (migration disabled)")
        except Exception as e:
            log(f"[ERROR] Could not process {f}: {e}")
            errors += 1
    if errors > 0:
        log(f"[FAIL] Harmonization/migration encountered {errors} errors. Aborting.")
        sys.exit(1)
    else:
        log("[SUCCESS] Harmonization and migration completed with no errors.")

if __name__ == "__main__":
    main()
