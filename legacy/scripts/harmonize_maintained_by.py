import os
import re
from pathlib import Path

MAINTAINED_BY_VALUE = "Eos Lumina ∴ (Collective Intelligence Meta-Agent)"
FRONTMATTER_PATTERN = re.compile(r"^---[\r\n]+(.*?)[\r\n]+---", re.DOTALL)
MAINTAINED_BY_PATTERN = re.compile(r"^maintained_by:.*$", re.MULTILINE)

def update_maintained_by_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find YAML frontmatter
    match = FRONTMATTER_PATTERN.match(content)
    if match:
        frontmatter = match.group(1)
        if 'maintained_by:' in frontmatter:
            # Replace existing maintained_by
            new_frontmatter = MAINTAINED_BY_PATTERN.sub(f"maintained_by: {MAINTAINED_BY_VALUE}", frontmatter)
        else:
            # Add maintained_by after title or at the top
            lines = frontmatter.splitlines()
            inserted = False
            for i, line in enumerate(lines):
                if line.startswith('title:'):
                    lines.insert(i+1, f"maintained_by: {MAINTAINED_BY_VALUE}")
                    inserted = True
                    break
            if not inserted:
                lines.insert(0, f"maintained_by: {MAINTAINED_BY_VALUE}")
            new_frontmatter = '\n'.join(lines)
        new_content = f"---\n{new_frontmatter}\n---" + content[match.end():]
    else:
        # No frontmatter, add it
        new_content = f"---\nmaintained_by: {MAINTAINED_BY_VALUE}\n---\n" + content

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    docs_dir = Path('c:/Users/w_eed/OneDrive/Desktop/ThinkAlike/docs')
    updated_files = []
    for md_file in docs_dir.rglob('*.md'):
        if update_maintained_by_in_file(md_file):
            updated_files.append(str(md_file))
    print("Updated files:")
    for f in updated_files:
        print(f)

if __name__ == "__main__":
    main()
