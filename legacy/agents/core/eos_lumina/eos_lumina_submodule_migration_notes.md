# Eos Lumina Agent Submodule Migration Notes

This document provides migration notes and recommendations for each agent submodule. Use this as a living record during the audit and migration process.

## Migration Notes by Submodule

### core/eos_lumina/
- Contains several markdown files with conceptual documentation.
- Audit for actual code implementations; flag missing logic for manual recreation.

### narrative/
- Multiple agent markdown files present in main repo, but no legacy folder found. Flag for manual recreation or deeper archive search.
- Check for narrative logic, story generation, and routing code. Document gaps.

### resonance/
- Only one file (harmonia_concordis.md) in main repo, no legacy folder found. Flag for manual recreation or deeper archive search.
- Likely conceptual; flag for logic migration and implementation.

### ritual/
- Several ritual agent docs present.
- Audit for ritual logic, event triggers, and integration points.

### ethics/
- Multiple ethics agent docs present.
- Check for ethical reasoning logic and decision boundaries.

### governance/
- Governance agent docs present.
- Audit for governance logic, voting, and protocol enforcement.

### knowledge/
- Knowledge agent docs present.
- Check for knowledge retrieval, synthesis, and integration logic.

### memory/
- Memory agent docs present in main repo, but no legacy folder found. Flag for manual recreation or deeper archive search.
- Audit for memory store logic, retrieval, and traceability features.

### relationships/
- Only one file (eleusis_synesis.md) in main repo, no legacy folder found. Flag for manual recreation or deeper archive search.
- Flag for relationship modeling logic and migration.

### utility/
- Utility agent docs present.
- Audit for utility functions, orchestration helpers, and missing code.

## Recommendations
- For each submodule, create a migration task in the project TODO if logic is missing.
- Prioritize submodules that impact agent orchestration and user experience.
- Use this document to track audit progress and update as migration proceeds.
