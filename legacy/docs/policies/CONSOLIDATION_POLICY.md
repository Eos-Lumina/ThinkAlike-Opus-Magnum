# CONSOLIDATION_POLICY.md

## ThinkAlike Project: Canonical Structure & Anti-Fragmentation Policy

### Purpose
This document defines the canonical directory structure, file placement rules, and anti-fragmentation policy for the ThinkAlike project. All automation, scripts, and contributors must strictly adhere to these rules to prevent file loss, duplication, or misplacement.

---

## 1. Canonical Project Root
- The only valid project root is:
  - `C:\Users\w_eed\OneDrive\Desktop\ThinkAlike\ThinkAlike`
- All scripts and automation must abort if run from any other location.

## 2. Manifest-Driven Operations
- The file `manifest.yaml` at the canonical root is the single source of truth for all canonical files and directories.
- Only files and folders listed in the manifest (especially under `canonical_files:`) are protected from deletion or modification.

## 3. Path Discipline
- No files or folders may be created, moved, or deleted outside the canonical structure.
- All destructive operations must:
  - Check the manifest for canonical status.
  - Abort or warn if a file is not listed or is ambiguous.

## 4. Duplicate & Misplaced Files
- No duplicate files with the same name may exist in different locations.
- Any detected duplicates or misplaced files must be moved or deleted, with actions logged.

## 5. Logging & Dry Runs
- All scripts must support a dry-run mode and log all actions.
- Destructive actions require explicit confirmation or dry-run by default.

## 6. User Confirmation
- If ambiguity or risk is detected (e.g., multiple possible targets, missing canonical files), prompt the user for confirmation before proceeding.

## 7. Policy Enforcement
- All scripts must reference this policy and abort if the policy cannot be enforced.
- Violations must be logged and reported.

---

**Reference this file in all scripts and automation.**

---

_Last updated: 2025-06-29_
