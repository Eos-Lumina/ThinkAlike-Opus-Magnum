#!/usr/bin/env python3
"""
ThinkAlike Documentation Scaffolder
-----------------------------------
Creates a new Markdown documentation file from a template, populating it with a
title, author, and date.

Usage:
    python scripts/new_doc.py <output_path> [--title "Doc Title"] \
        [--author "Your Name"] [--template <template_name>]

Example:
    python scripts/new_doc.py docs/new_feature.md --title "My New Feature" \
        --author "Jane Doe"
"""

# NOTE: Only reference canonical documentation in docs/contributors/ and test plan
# in tests/testing_and_validation_plan.md. Deprecated folders/files (e.g.,
# docs/guides/contributor_guides/,
# docs/project/archive/testing_and_validation_plan.md) must not be recreated
# or referenced.

import argparse
import sys
from datetime import datetime
from pathlib import Path

# --- Templates ---
# Templates are stored as multiline strings to keep the script self-contained.
TEMPLATES = {
    "default": """
# {{TITLE}}

**Author:** {{AUTHOR}}
**Date:** {{DATE}}

---

## Overview

(A brief summary of the document's purpose.)

## Section 1

(Content goes here.)

""",
    "technical_spec": """
# Technical Specification: {{TITLE}}

**Author:** {{AUTHOR}}
**Date:** {{DATE}}
**Status:** Draft

---

## 1. Introduction

### 1.1. Purpose

### 1.2. Scope

### 1.3. Definitions, Acronyms, and Abbreviations

## 2. System Architecture

## 3. Design

### 3.1. Component A

### 3.2. Component B

## 4. Requirements

## 5. Open Questions

""",
}


def create_new_doc(
    template_name: str,
    output_path: Path,
    title: str,
    author: str | None,
) -> None:
    """Creates a new documentation file from a template."""
    if template_name not in TEMPLATES:
        print(
            f"Error: Template '{template_name}' not found.",
            file=sys.stderr,
        )
        sys.exit(1)

    template_content = TEMPLATES[template_name]

    # Ensure the output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Replace placeholders
    content = template_content.replace("{{TITLE}}", title)
    content = content.replace("{{AUTHOR}}", author or "ThinkAlike Team")
    content = content.replace("{{DATE}}", datetime.now().strftime("%Y-%m-%d"))

    if output_path.exists():
        overwrite = input(
            f"Warning: '{output_path}' already exists. Overwrite? (y/n): "
        )
        if overwrite.lower() != "y":
            print("Operation cancelled.")
            return

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Successfully created new document: {output_path}")
    except IOError as e:
        print(
            f"Error: Could not write to file {output_path}: {e}",
            file=sys.stderr,
        )
        sys.exit(1)


def main():
    """Main function for the new documentation script."""
    parser = argparse.ArgumentParser(
        description="Create a new documentation file from a template."
    )
    parser.add_argument(
        "output_path",
        type=Path,
        help=("Path to the new documentation file (e.g., " '"docs/new_feature.md").'),
    )
    parser.add_argument(
        "--title",
        type=str,
        help=(
            "The title of the document. If not provided, it will be derived "
            "from the filename."
        ),
    )
    parser.add_argument("--author", type=str, help="The author of the document.")
    parser.add_argument(
        "--template",
        type=str,
        default="default",
        choices=TEMPLATES.keys(),
        help="The template to use.",
    )

    args = parser.parse_args()

    # If title is not provided, generate it from the filename
    doc_title = (
        args.title
        if args.title
        else args.output_path.stem.replace("_", " ").replace("-", " ").title()
    )

    create_new_doc(args.template, args.output_path, doc_title, args.author)


if __name__ == "__main__":
    main()
