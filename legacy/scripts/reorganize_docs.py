import os
import shutil
from pathlib import Path

# Get the root directory (one level up from scripts)
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def ensure_dir(path):
    """Create directory if it doesn't exist"""
    if not os.path.exists(path):
        os.makedirs(path)


# Define the canonical structure using absolute paths
CANONICAL_STRUCTURE = {
    # Documentation Structure
    os.path.join(ROOT_DIR, "docs/guides/development/general"): [
        "performance_scalability_guidelines.md",
        "testing_and_validation_plan.md",
        "data_handling_policy_guide.md",
        "code_review_guidelines.md",
        "coding_standards.md",
        "development_setup.md",
        "testing_strategy.md",
    ],
    os.path.join(ROOT_DIR, "docs/guides/development/ai"): [
        "ai_ethical_implementation_guide.md",
    ],
    os.path.join(ROOT_DIR, "docs/ui_components"): [
        "ui_developer_guide.md",
    ],
    os.path.join(ROOT_DIR, "docs/guides/development/frontend"): [
        "component_development_guide.md",
        "state_management_guide.md",
    ],
    os.path.join(ROOT_DIR, "docs/guides/development/backend"): [
        "api_design_guide.md",
        "database_schema.md",
    ],
    os.path.join(ROOT_DIR, "docs/guides/development/narrative"): [
        "gamified_narrative_guide.md",
        "chapters",
    ],
    os.path.join(ROOT_DIR, "docs/guides/development/operations"): [
        "deployment_guide.md",
        "monitoring_guide.md",
        "scaling_guide.md",
    ],
    os.path.join(ROOT_DIR, "docs/architecture"): [
        "system_blueprint.md",
        "data_flow.md",
        "security_model.md",
    ],
    # Source Code Structure
    os.path.join(ROOT_DIR, "src/core"): [  # Core application logic
        "agent_registry",  # Agent management
        "alchemy",  # Core transformation logic
        "narrative_engine",  # Narrative processing
        "resonance_graph",  # Graph database interactions
        "ritual_engine",  # Ritual processing
    ],
    os.path.join(ROOT_DIR, "src/frontend"): [  # Frontend application
        "components",  # Reusable UI components
        "pages",  # Page definitions
        "hooks",  # Custom React hooks
        "styles",  # CSS/styling
        "utils",  # Frontend utilities
    ],
    os.path.join(ROOT_DIR, "src/backend"): [  # Backend services
        "api",  # API endpoints
        "services",  # Business logic
        "models",  # Data models
        "database",  # Database interactions
        "middleware",  # Express/HTTP middleware
    ],
    os.path.join(ROOT_DIR, "src/shared"): [  # Shared code
        "types",  # TypeScript types/interfaces
        "constants",  # Shared constants
        "utils",  # Shared utilities
    ],
    # Configuration
    os.path.join(ROOT_DIR, "config"): [  # Configuration files
        "default.json",  # Default configuration
        "development.json",  # Development settings
        "production.json",  # Production settings
        "test.json",  # Test settings
    ],
    # Testing
    os.path.join(ROOT_DIR, "tests/unit"): [
        "frontend",  # Frontend unit tests
        "backend",  # Backend unit tests
        "shared",  # Shared code tests
    ],
    os.path.join(ROOT_DIR, "tests/integration"): [
        "api",  # API integration tests
        "e2e",  # End-to-end tests
    ],
    # Development Tools
    os.path.join(ROOT_DIR, "tools"): [  # Development tools
        "scripts",  # Build/deployment scripts
        "generators",  # Code generators
        "debug",  # Debugging utilities
    ],
}

PROTECTED_CONTENT_MARKERS = [
    "Human-Centered",
    "Our Mission",
    "For Everyone",
    "Community",
    "Ethics",
    "Wellbeing",
    "User Stories",
    "Accessibility",
]


def preserve_human_content(original_content, new_content):
    """Ensure human-centered content is preserved during updates"""
    if not original_content or not new_content:
        return new_content

    # Check if original content contains protected markers
    has_protected_content = any(
        marker in original_content for marker in PROTECTED_CONTENT_MARKERS
    )

    if has_protected_content:
        print("⚠️  Protected human-centered content detected - preserving original")
        return original_content

    return new_content


def ensure_canonical_structure():
    """Create the canonical directory structure and ensure files are in place"""
    print("Starting documentation reorganization...")

    for dir_path, files in CANONICAL_STRUCTURE.items():
        ensure_dir(dir_path)
        print(f"Ensured directory exists: {dir_path}")


def move_file(src, dest):
    """Move a file and print the operation."""
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        print(f"Moving {src} -> {dest}")
        shutil.move(src, dest)


def reorganize_docs():
    """Reorganize documentation files according to canonical structure."""
    ensure_canonical_structure()

    # Move files to their canonical locations
    for target_dir, files in CANONICAL_STRUCTURE.items():
        for filename in files:
            # Check various possible source locations
            possible_locations = [
                filename,  # Root
                f"docs/{filename}",
                f"docs/guides/{filename}",
                f"docs/devops/{filename}",
                f"docs/development_framework/{filename}",
            ]

            for src in possible_locations:
                if os.path.exists(src):
                    dest = os.path.join(target_dir, filename)
                    move_file(src, dest)
                    break


def move_development_framework_files():
    """Move files from development_framework to their canonical locations"""
    dev_framework_dir = os.path.join(ROOT_DIR, "docs/development_framework")
    if not os.path.exists(dev_framework_dir):
        print(f"Directory not found: {dev_framework_dir}")
        return

    moves = {
        "coding_standards.md": os.path.join(
            ROOT_DIR, "docs/guides/development/general"
        ),
        "development_setup.md": os.path.join(
            ROOT_DIR, "docs/guides/development/general"
        ),
        "testing_strategy.md": os.path.join(
            ROOT_DIR, "docs/guides/development/general"
        ),
        "gamified_narrative_guide.md": os.path.join(
            ROOT_DIR, "docs/guides/development/narrative"
        ),
        "narrative_dev_chapters": os.path.join(
            ROOT_DIR, "docs/guides/development/narrative/chapters"
        ),
    }

    for src, dest_dir in moves.items():
        src_path = os.path.join(dev_framework_dir, src)
        if os.path.exists(src_path):
            dest_path = os.path.join(dest_dir, src)
            ensure_dir(os.path.dirname(dest_path))
            shutil.move(src_path, dest_path)
            print(f"Moved {src} to {dest_dir}")

    # Move remaining files to general
    general_dir = os.path.join(ROOT_DIR, "docs/guides/development/general")
    for item in os.listdir(dev_framework_dir):
        if item not in moves:
            src_path = os.path.join(dev_framework_dir, item)
            if os.path.isfile(src_path):
                dest_path = os.path.join(general_dir, item)
                ensure_dir(os.path.dirname(dest_path))
                shutil.move(src_path, dest_path)
                print(f"Moved {item} to {general_dir}")

    # Try to remove the now-empty directory
    try:
        os.rmdir(dev_framework_dir)
        print(f"Removed empty directory: {dev_framework_dir}")
    except OSError as e:
        print(f"Could not remove directory {dev_framework_dir}: {e}")


def cleanup_empty_dirs():
    """Remove empty directories after reorganization."""
    for root, dirs, files in os.walk(".", topdown=False):
        for name in dirs:
            try:
                dir_path = os.path.join(root, name)
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)
                    print(f"Removed empty directory: {dir_path}")
            except:
                pass


def move_directory_contents(src_dir, dest_dir):
    """Move contents of a directory to another location."""
    if not os.path.exists(src_dir):
        return

    ensure_dir(dest_dir)
    print(f"Moving contents from {src_dir} to {dest_dir}")

    # Move all contents
    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)

        if os.path.isfile(src_path):
            shutil.move(src_path, dest_path)
        elif os.path.isdir(src_path):
            if os.path.exists(dest_path):
                move_directory_contents(src_path, dest_path)
            else:
                shutil.move(src_path, dest_path)


def reorganize_source_code():
    """Reorganize source code according to canonical structure."""
    print("Starting source code reorganization...")

    # Create core directory and move core modules
    core_dir = os.path.join(ROOT_DIR, "src/core")
    ensure_dir(core_dir)

    core_modules = [
        "agent_registry",
        "alchemy",
        "narrative_engine",
        "resonance_graph",
        "ritual_engine",
    ]

    for module in core_modules:
        src_path = os.path.join(ROOT_DIR, "src", module)
        dest_path = os.path.join(core_dir, module)
        if os.path.exists(src_path):
            move_directory_contents(src_path, dest_path)
            try:
                os.rmdir(src_path)
            except:
                pass

    # Move frontend-related code
    frontend_dir = os.path.join(ROOT_DIR, "src/frontend")
    ensure_dir(frontend_dir)

    # Move pet_clarity_ui contents to frontend/components
    pet_ui_dir = os.path.join(ROOT_DIR, "src/pet_clarity_ui")
    if os.path.exists(pet_ui_dir):
        components_dir = os.path.join(frontend_dir, "components")
        move_directory_contents(pet_ui_dir, components_dir)
        try:
            os.rmdir(pet_ui_dir)
        except:
            pass

    # Organize shared utilities
    shared_dir = os.path.join(ROOT_DIR, "src/shared")
    ensure_dir(shared_dir)
    utils_dir = os.path.join(ROOT_DIR, "src/utils")
    shared_utils_dir = os.path.join(ROOT_DIR, "src/shared_utils")

    if os.path.exists(utils_dir):
        move_directory_contents(utils_dir, os.path.join(shared_dir, "utils"))
        try:
            os.rmdir(utils_dir)
        except:
            pass

    if os.path.exists(shared_utils_dir):
        move_directory_contents(shared_utils_dir, os.path.join(shared_dir, "utils"))
        try:
            os.rmdir(shared_utils_dir)
        except:
            pass

    print("Source code reorganization complete!")


def handle_special_directories():
    """Handle special directories that need custom processing."""
    print("Handling special directories...")

    src_dir = os.path.join(ROOT_DIR, "src")

    # Move realtime features to backend
    realtime_dir = os.path.join(src_dir, "realtime")
    if os.path.exists(realtime_dir):
        dest_dir = os.path.join(src_dir, "backend/services/realtime")
        move_directory_contents(realtime_dir, dest_dir)
        try:
            os.rmdir(realtime_dir)
        except:
            pass

    # Move swarm logic to core
    swarm_dir = os.path.join(src_dir, "swarm")
    if os.path.exists(swarm_dir):
        dest_dir = os.path.join(src_dir, "core/swarm")
        move_directory_contents(swarm_dir, dest_dir)
        try:
            os.rmdir(swarm_dir)
        except:
            pass

    # Move sybil resilience to core security
    sybil_dir = os.path.join(src_dir, "sybil_resilience")
    if os.path.exists(sybil_dir):
        dest_dir = os.path.join(src_dir, "core/security/sybil_resilience")
        ensure_dir(os.path.dirname(dest_dir))
        move_directory_contents(sybil_dir, dest_dir)
        try:
            os.rmdir(sybil_dir)
        except:
            pass

    # Move framework to shared
    framework_dir = os.path.join(src_dir, "framework")
    if os.path.exists(framework_dir):
        dest_dir = os.path.join(src_dir, "shared/framework")
        move_directory_contents(framework_dir, dest_dir)
        try:
            os.rmdir(framework_dir)
        except:
            pass

    # Move sandbox to tools
    sandbox_dir = os.path.join(src_dir, "dgm_sandbox")
    if os.path.exists(sandbox_dir):
        dest_dir = os.path.join(ROOT_DIR, "tools/sandbox")
        ensure_dir(dest_dir)
        move_directory_contents(sandbox_dir, dest_dir)
        try:
            os.rmdir(sandbox_dir)
        except:
            pass


if __name__ == "__main__":
    print("Starting project reorganization...")
    reorganize_docs()
    move_development_framework_files()
    reorganize_source_code()
    handle_special_directories()
    cleanup_empty_dirs()
    print("Project reorganization complete!")
