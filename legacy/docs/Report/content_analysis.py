
import os
import re
import yaml
from collections import defaultdict

def analyze_content_for_integrity(file_list_path, output_dir):
    all_filepaths = []
    with open(file_list_path, "r") as f:
        all_filepaths = [line.strip() for line in f]

    file_contents = {}
    for filepath in all_filepaths:
        with open(filepath, "r") as f:
            file_contents[filepath] = f.read()

    # --- Analysis for Consolidation, Repetition, Divergence, and Cross-linking ---

    # 1. Identify potential repetitions/similarities (simple approach: look for identical paragraphs/sections)
    #    This is a simplified approach. For true repetition, more advanced NLP (e.g., semantic similarity) is needed.
    #    For now, we will look for exact duplicate lines or paragraphs (defined as blocks of text between two newlines).
    
    duplicate_paragraphs = defaultdict(list)
    for filepath, content in file_contents.items():
        paragraphs = [p.strip() for p in content.split("\n\n") if p.strip()]
        for p in paragraphs:
            if len(p) > 50: # Only consider paragraphs longer than 50 characters to avoid trivial matches
                duplicate_paragraphs[p].append(filepath)

    with open(os.path.join(output_dir, "potential_duplicate_paragraphs.txt"), "w") as f:
        for paragraph, filepaths in duplicate_paragraphs.items():
            if len(filepaths) > 1:
                f.write(f"Paragraph:\n---\n{paragraph}\n---\nFound in files:\n")
                for fp in filepaths:
                    f.write(f"- {fp}\n")
                f.write("\n")

    # 2. Identify divergence between specs and plain language docs (based on naming convention)
    #    This is a heuristic based on file names containing \'spec\' and \'plain_language\' or similar.
    divergence_candidates = defaultdict(list)
    spec_files = [f for f in all_filepaths if "_spec.md" in f]
    for spec_file in spec_files:
        base_name = os.path.basename(spec_file).replace("_spec.md", "")
        for other_file in all_filepaths:
            if other_file != spec_file and base_name in other_file and ("plain_language" in other_file or "guide" in other_file or "manual" in other_file):
                divergence_candidates[base_name].append(spec_file)
                divergence_candidates[base_name].append(other_file)
    
    with open(os.path.join(output_dir, "potential_divergence_candidates.txt"), "w") as f:
        for concept, files in divergence_candidates.items():
            f.write("Concept: " + concept + "\nFiles: " + ", ".join(sorted(list(set(files)))) + "\n\n")

    # 3. Identify opportunities for cross-linking (simple: mention of a file name or key concept in another file)
    #    This is very basic and would ideally involve a knowledge graph or more advanced entity recognition.
    cross_link_opportunities = defaultdict(list)
    for filepath1, content1 in file_contents.items():
        for filepath2 in all_filepaths:
            if filepath1 == filepath2: continue
            # Look for mentions of other file base names (without .md) in the content
            filename2 = os.path.basename(filepath2).replace(".md", "")
            if filename2 in content1:
                cross_link_opportunities[filepath1].append(filepath2)
    
    with open(os.path.join(output_dir, "potential_cross_link_opportunities.txt"), "w") as f:
        for source_file, target_files in cross_link_opportunities.items():
            f.write(f"File {source_file} could link to:\n")
            for tf in target_files:
                f.write(f"- {tf}\n")
            f.write("\n")

    print(f"Content analysis complete. Results saved to {output_dir}")

if __name__ == "__main__":
    file_list_path = "/home/ubuntu/thinkalike_docs/markdown_files.txt"
    output_dir = "/home/ubuntu/thinkalike_docs/analysis_results"
    os.makedirs(output_dir, exist_ok=True)
    analyze_content_for_integrity(file_list_path, output_dir)


