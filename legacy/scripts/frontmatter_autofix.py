import os
import re
import shutil
import frontmatter

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PROTOCOL_DIRS = [
    'protocols',
    'docs/protocols',
    'bridges',
    'realms',
    'seed',
]

def fix_yaml_frontmatter(yaml_text):
    # Add quotes around values with colons or special characters
    fixed_lines = []
    for line in yaml_text.splitlines():
        if ':' in line:
            key, value = line.split(':', 1)
            value = value.strip()
            # Add quotes if value contains colon, backslash, or starts with special char
            if (':' in value or '\\' in value or value.startswith('>') or value.startswith('|')) and not (value.startswith('"') or value.startswith("'")):
                value = '"' + value.replace('"', '\"') + '"'
            # Escape backslashes in quoted strings
            if value.startswith('"') or value.startswith("'"):
                value = value.replace('\\', '\\\\')
            fixed_lines.append(f'{key}: {value}')
        else:
            fixed_lines.append(line)
    return '\n'.join(fixed_lines)

def process_file(path):
    with open(path, encoding='utf-8') as f:
        content = f.read()
    if not content.strip().startswith('---'):
        return False, 'No frontmatter found'
    # Extract frontmatter
    match = re.match(r'---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if not match:
        return False, 'Frontmatter block not found or malformed'
    yaml_text, body = match.groups()
    # Try to fix YAML
    fixed_yaml = fix_yaml_frontmatter(yaml_text)
    fixed_content = f'---\n{fixed_yaml}\n---\n{body}'
    # Try to parse again
    try:
        frontmatter.loads(fixed_content)
    except Exception as e:
        return False, f'Autofix failed: {e}'
    # Backup original
    shutil.copy2(path, path + '.bak')
    # Write fixed content
    with open(path, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    return True, 'Fixed'

def main():
    fixed = []
    failed = []
    for base in PROTOCOL_DIRS:
        dir_path = os.path.join(ROOT_DIR, base)
        for root, _, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.md'):
                    path = os.path.join(root, file)
                    try:
                        with open(path, encoding='utf-8') as f:
                            content = f.read()
                        frontmatter.loads(content)
                    except Exception:
                        ok, msg = process_file(path)
                        rel = os.path.relpath(path, ROOT_DIR)
                        if ok:
                            fixed.append(rel)
                        else:
                            failed.append((rel, msg))
    print('\n=== Autofix Report ===')
    if fixed:
        print('Fixed:')
        for f in fixed:
            print('  ', f)
    if failed:
        print('\nStill Broken:')
        for f, msg in failed:
            print(f'  {f}: {msg}')
    if not fixed and not failed:
        print('No issues found!')
    print('\nBackups of fixed files are saved as .bak')

if __name__ == '__main__':
    main()
    input('\nPress Enter to exit...')
