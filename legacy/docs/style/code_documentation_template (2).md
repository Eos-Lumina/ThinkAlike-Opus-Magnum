---
title: ThinkAlike Code Documentation Template – Harmonized
version: 2.0.0
status: Harmonized
last_updated: 2025-06-10
harmonization_note: Fully updated to provide explicit templates for code comments, docstrings, and symbolic/ritual intent documentation. Includes language-specific conventions and references to harmonized guides. Supersedes all previous versions.
tags: [documentation, code_quality, symbolic_ux, ritual_logic, maintainability, developer_guide]
---

# ThinkAlike Code Documentation Template (Canonical)

## Purpose
This template provides a harmonized standard for documenting code in ThinkAlike, ensuring clarity, maintainability, and the explicit communication of symbolic/ritual intent. All code should be documented using these conventions, referencing relevant design documents and harmonized guides.

## 1. File/Module-Level Docstring Template

```python
"""
Module Name: [module_name.py]
Purpose: [Brief description of the module's function and its role in the system.]
Symbolic/Ritual Intent: [Describe the symbolic meaning or ritual step this module implements.]
Author: [Name(s)]
Date: [YYYY-MM-DD]
Related Specs/Docs: [e.g., architectural_overview.md, ritual_protocol.md]
"""
```

```js
/**
 * Module Name: [moduleName.js]
 * Purpose: [Brief description of the module's function and its role in the system.]
 * Symbolic/Ritual Intent: [Describe the symbolic meaning or ritual step this module implements.]
 * Author: [Name(s)]
 * Date: [YYYY-MM-DD]
 * Related Specs/Docs: [e.g., architectural_overview.md, ritual_protocol.md]
 */
```

## 2. Class/Interface Docstring Template

```python
class MyClass:
    """
    Purpose: [What does this class represent?]
    Symbolic/Ritual Intent: [Symbolic meaning or ritual role.]
    Related Specs/Docs: [List]
    """
```

```js
/**
 * Purpose: [What does this class represent?]
 * Symbolic/Ritual Intent: [Symbolic meaning or ritual role.]
 * Related Specs/Docs: [List]
 */
class MyClass {}
```

## 3. Function/Method Docstring Template

```python
def my_function(param1: str) -> int:
    """
    Purpose: [What does this function do?]
    Parameters:
        param1 (str): [Description]
    Returns:
        int: [Description]
    Raises:
        [ExceptionType]: [Condition]
    Symbolic/Ritual Step: [Describe the ritual step or symbolic logic implemented.]
    Related Specs/Docs: [List]
    """
```

```js
/**
 * Purpose: [What does this function do?]
 * @param {string} param1 - [Description]
 * @returns {number} [Description]
 * @throws [ExceptionType] [Condition]
 * Symbolic/Ritual Step: [Describe the ritual step or symbolic logic implemented.]
 * Related Specs/Docs: [List]
 */
function myFunction(param1) {}
```

## 4. Inline Comments (All Languages)
- Use inline comments to clarify complex logic, especially where symbolic/ritual meaning is present.
- Example:
  ```python
  # This loop represents the "Resonance Alignment" ritual phase
  for node in resonance_network:
      ...
  ```
  ```js
  // This block implements the "Glyph Forging" symbolic step
  for (const glyph of glyphs) {
      ...
  }
  ```

## 5. Referencing Design Documents
- Always reference relevant design documents, specs, or harmonized guides in docstrings/comments.
- Use relative paths or canonical doc names (e.g., `architectural_overview.md`, `ritual_protocol.md`).

## 6. Language-Specific Conventions
- **Python:** Use reStructuredText, Google, or NumPy docstring formats. Prefer triple double-quoted strings for docstrings.
- **JavaScript/TypeScript:** Use JSDoc/TSDoc conventions. Place block comments above functions/classes.
- **Other Languages:** Follow community best practices and adapt the symbolic/ritual intent fields as appropriate.

## 7. Documenting Symbolic/Ritual Logic
- Explicitly describe the symbolic or ritual purpose of code blocks, classes, and functions.
- If a function implements a ritual step, state which step and its meaning.
- If a class models a symbolic entity, describe its role in the narrative or ritual.

## 8. Example: Complete Python Function Docstring
```python
def forge_glyph(user_input: str) -> Glyph:
    """
    Purpose: Forges a new glyph based on user input and system resonance.
    Parameters:
        user_input (str): The user's symbolic input.
    Returns:
        Glyph: The newly forged glyph object.
    Raises:
        ValueError: If input is invalid or fails ritual validation.
    Symbolic/Ritual Step: Implements the "Glyph Forging" phase of the Initiation Journey.
    Related Specs/Docs: ritual_protocol.md, architectural_overview.md
    """
    ...
```

## 9. References & Crosslinks
- `code_style_guide.md`
- `architectural_overview.md`
- `ritual_protocol.md`
- `testing_and_validation_plan.md`
- `api_design_guidelines.md`
- `canonical_visual_style_guide.md`

---

# This file is canonical. Supersedes all previous versions. All contributors must reference this document for code documentation standards.
