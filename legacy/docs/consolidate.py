import os

# --- The Alchemist's Settings ---
prima_materia_directory = '.'  # The folder with your .md files
output_vessel_name = 'consolidated_materia.txt'
chunk_size = 500000  # characters per chunk
# --------------------------------

script_path = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(script_path, prima_materia_directory)
output_file_path = os.path.join(script_path, output_vessel_name)

file_paths = []
for root, dirs, files in os.walk(input_dir):
    for file in files:
        if file.endswith('.md'):
            file_paths.append(os.path.join(root, file))

all_text = ""
for path in sorted(file_paths):
    all_text += f"\n\n--- START OF FILE {os.path.relpath(path, input_dir)} ---\n"
    try:
        with open(path, 'r', encoding='utf-8') as infile:
            file_content = infile.read()
            if file_content.strip():
                all_text += file_content
            else:
                all_text += "(File is empty)"
    except Exception as e:
        all_text += f"ERROR READING FILE: {e}\n"
    all_text += f"\n--- END OF FILE ---\n\n"

chunks = [all_text[i:i+chunk_size] for i in range(0, len(all_text), chunk_size)]
for idx, chunk in enumerate(chunks):
    chunk_file = f"{output_vessel_name.replace('.txt', '')}_chunk{idx+1}.txt"
    with open(os.path.join(script_path, chunk_file), 'w', encoding='utf-8') as f:
        f.write(chunk)
    print(f"Created {chunk_file}")

print("Consolidation complete.")
