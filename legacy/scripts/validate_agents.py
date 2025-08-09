import os
import re

def main():
    agent_registry_path = "agents/agent_registry.md"
    if not os.path.exists(agent_registry_path):
        print(f"Error: {agent_registry_path} not found.")
        return

    with open(agent_registry_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    core_agents = []
    # Start processing after the header and separator lines
    for line in lines[4:]:
        if "| Core" in line:
            parts = [p.strip() for p in line.split('|')]
            if len(parts) > 4:
                agent_name = parts[1]
                md_path = parts[4]
                # Clean up the path if it's a markdown link
                if "[" in md_path and "](" in md_path:
                    md_path = md_path.split('](')[1][:-1]
                
                if md_path.startswith("agents/core/"):
                    core_agents.append((agent_name, md_path))

    print(f"Found {len(core_agents)} core agents in the registry. Validating file presence...")
    print("-" * 30)

    all_good = True
    for agent_name, md_path in core_agents:
        print(f"Checking: {agent_name}")
        
        agent_id = os.path.basename(md_path).replace('.md', '')
        agent_doc_dir = os.path.dirname(md_path)

        # 1. Check for .md file
        if os.path.exists(md_path):
            print(f"  [+] Found Doc:      {md_path}")
        else:
            print(f"  [!] MISSING Doc:    {md_path}")
            all_good = False

        # 2. Check for .yaml persona file
        yaml_path = os.path.join(agent_doc_dir, f"{agent_id}_persona.yaml")
        if os.path.exists(yaml_path):
            print(f"  [+] Found Persona:  {yaml_path}")
        else:
            print(f"  [!] MISSING Persona:  {yaml_path}")
            all_good = False

        # 3. Check for .py implementation file
        py_path = os.path.join("src", "backend", "app", "agents", f"{agent_id}_agent.py")
        if os.path.exists(py_path):
            print(f"  [+] Found Code:     {py_path}")
        else:
            print(f"  [!] MISSING Code:   {py_path}")
            all_good = False
        
        print("-" * 30)

    if all_good:
        print("\nValidation successful! All core agents have required files.")
    else:
        print("\nValidation failed. Some core agent files are missing.")

if __name__ == "__main__":
    main()
