
import os
import re
import yaml

def analyze_markdown_files(file_list_path, output_dir):
    missing_frontmatter = []
    inconsistent_tags = {}
    all_tags = set()
    file_contents = {}

    with open(file_list_path, 'r') as f:
        filepaths = [line.strip() for line in f]

    for filepath in filepaths:
        with open(filepath, 'r') as f:
            content = f.read()
            file_contents[filepath] = content

        # Check for frontmatter
        frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if not frontmatter_match:
            missing_frontmatter.append(filepath)
            continue

        frontmatter_str = frontmatter_match.group(1)
        try:
            frontmatter = yaml.safe_load(frontmatter_str)
        except yaml.YAMLError:
            # If frontmatter is malformed, treat as missing for now
            missing_frontmatter.append(filepath)
            continue

        # Check for title and tags
        if 'title' not in frontmatter:
            missing_frontmatter.append(filepath) # Or categorize as missing title
        if 'tags' in frontmatter:
            tags = frontmatter['tags']
            if isinstance(tags, str):
                tags = [t.strip() for t in tags.split(',')]
            elif not isinstance(tags, list):
                inconsistent_tags[filepath] = tags # Log inconsistent format
                continue
            
            for tag in tags:
                all_tags.add(tag)

    # Save findings
    with open(os.path.join(output_dir, 'missing_frontmatter.txt'), 'w') as f:
        for item in missing_frontmatter:
            f.write(f'{item}\n')

    with open(os.path.join(output_dir, 'inconsistent_tags.txt'), 'w') as f:
        for filepath, tags in inconsistent_tags.items():
            f.write(f'{filepath}: {tags}\n')

    with open(os.path.join(output_dir, 'all_tags.txt'), 'w') as f:
        for tag in sorted(list(all_tags)):
            f.write(f'{tag}\n')

    # For now, just return the file contents for further analysis
    return file_contents

if __name__ == '__main__':
    file_list_path = '/home/ubuntu/thinkalike_docs/markdown_files.txt'
    output_dir = '/home/ubuntu/thinkalike_docs/analysis_results'
    os.makedirs(output_dir, exist_ok=True)
    file_contents = analyze_markdown_files(file_list_path, output_dir)
    # Further analysis will be done in subsequent steps
    print(f"Analysis complete. Results saved to {output_dir}")


