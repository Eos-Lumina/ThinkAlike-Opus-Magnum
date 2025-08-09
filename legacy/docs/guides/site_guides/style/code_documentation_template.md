---
title: 'Code Documentation Template: Recording the Ritual'
version: 2.0.0
status: Canonical
last_updated: 2025-06-17
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
harmonization_note: This file is the canonical template for all code documentation
  (docstrings, etc.) and is cross-referenced in the main code style guide.
tags:
- code_quality
- developer_guide
- documentation
- maintainability
- ritual_logic
- style
- symbolic_ux
---


# Code Documentation Template: Recording the Ritual

**Code is ritual. Documentation is the record of intent.** This template provides a harmonized standard for documenting code in ThinkAlike, ensuring clarity, maintainability, and the explicit communication of symbolic/ritual intent.

All code should be documented using these conventions, referencing relevant design documents and harmonized guides as defined in `docs/source_of_truth.md`.

## 1. File/Module-Level Docstring Template

```python
"""
Module Name: [module_name.py]
Purpose: [Brief, one-sentence description of the module's function and its role in the system.]
Symbolic Intent: [Describe the symbolic meaning or ritual step this module implements. E.g., 'This module serves as the Alchemical Vessel for processing user reflections.']
Author(s): [Name(s)]
Date: [YYYY-MM-DD]
Related Specs: [Link to the primary spec file, e.g., `realms/portal/portal_specification.md`]
"""
```

```javascript
/**
 * @module [moduleName.js]
 * @purpose [Brief, one-sentence description of the module's function.]
 * @symbolicIntent [Describe the symbolic meaning or ritual role.]
 * @author [Name(s)]
 * @date [YYYY-MM-DD]
 * @relatedSpecs [Link to the primary spec file]
 */
```

## 2. Class/Interface & Function/Method Docstrings
Follow the standard docstring conventions for your language (e.g., Python's reStructuredText, JSDoc for JS/TS), but you must include a @symbolicIntent or Symbolic Intent: field to explain the narrative or ritual purpose of the code.

### Example (Python)
```python
def forge_glyph(user_input: str, context_seed: dict) -> Glyph:
    """Forges a new Initiation Glyph based on user input and system resonance.

    This function implements the "Glyph Forging" phase of the Portal Initiation
    Journey, transforming user reflections into a unique symbolic anchor.

    Args:
        user_input: The user's symbolic input.
        context_seed: Ephemeral data for ensuring uniqueness.

    Returns:
        The newly forged Glyph object.

    Symbolic Intent:
        Implements the "Vow & The Sealing" ritual step.

    Related Specs:
        - `docs/protocols/initiation_glyph_protocol.md`
    """
    # ... implementation ...
```

## 3. Inline Comments for Ritual Logic
Use inline comments to mark specific, non-obvious ritual steps or symbolic logic.

```python
# This loop represents the "Resonance Alignment" ritual phase
for node in resonance_network:
    # ...
```

## 4. Cross-References
- [Code Style Guide](code_style_guide.md)
- [Canonical Visual Style Guide](./visual_style_guide.md)
- [API Design Guidelines](../architecture/api_design_guidelines.md)

---
