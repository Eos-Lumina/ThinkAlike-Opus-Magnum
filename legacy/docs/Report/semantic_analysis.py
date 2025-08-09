
import os
import re
from collections import Counter

def analyze_semantics(file_path, output_dir):
    with open(file_path, "r") as f:
        content = f.read()

    # Simple word frequency analysis (excluding common stop words)
    words = re.findall(r'\b\w+\b', content.lower())
    stop_words = set(["the", "a", "an", "in", "of", "to", "and", "is", "for", "it", "with", "as", "on", "that", "this", "be", "are", "by", "or", "at"])
    filtered_words = [word for word in words if word not in stop_words and not word.isdigit()]
    word_freq = Counter(filtered_words)

    with open(os.path.join(output_dir, "word_frequency.txt"), "w") as f:
        for word, freq in word_freq.most_common(100):
            f.write(f"{word}: {freq}\n")

    # Simple n-gram analysis (bigrams and trigrams)
    bigrams = list(zip(filtered_words, filtered_words[1:]))
    trigrams = list(zip(filtered_words, filtered_words[1:], filtered_words[2:]))
    bigram_freq = Counter(bigrams)
    trigram_freq = Counter(trigrams)

    with open(os.path.join(output_dir, "bigram_frequency.txt"), "w") as f:
        for bigram, freq in bigram_freq.most_common(50):
            f.write(f"{' '.join(bigram)}: {freq}\n")

    with open(os.path.join(output_dir, "trigram_frequency.txt"), "w") as f:
        for trigram, freq in trigram_freq.most_common(50):
            f.write(f"{' '.join(trigram)}: {freq}\n")

    print(f"Semantic analysis complete. Results saved to {output_dir}")

if __name__ == "__main__":
    file_path = "/home/ubuntu/thinkalike_docs/analysis_results/all_markdown_content.txt"
    output_dir = "/home/ubuntu/thinkalike_docs/analysis_results"
    os.makedirs(output_dir, exist_ok=True)
    analyze_semantics(file_path, output_dir)


