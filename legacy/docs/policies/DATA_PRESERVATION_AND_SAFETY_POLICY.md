# Data Preservation & Safety Policy for Consolidation

To ensure zero data loss and full provenance during consolidation, all agents and automation must strictly follow these rules:

## 1. No Deletion of Important Files
- No protocol, documentation, or code file may be deleted outright.
- All legacy, alternate, or duplicate files must be archived to `_legacy/archived_protocols/` or a designated archive folder.
- Add a redirect notice in the original location, pointing to the canonical or harmonized version.

## 2. Provenance & Migration Logging
- Every move, merge, or archival action must be logged in the migration log (e.g., `migration_log.yaml` and dated migration log entries).
- Migration log entries must include:
  - Original file path
  - New file path (if moved/archived)
  - Reason for action (e.g., harmonization, deduplication)
  - Reference to related canonical file

## 3. Dry-Run and Review for Automation
- All automation scripts must:
  - Run in dry-run mode first, logging all proposed actions
  - Require explicit confirmation before making changes
  - Log all actions for review

## 4. Human Review
- After automation or bulk actions, a human agent must review the archive and migration logs to confirm:
  - No important content was lost
  - All provenance is preserved
  - All redirects are in place

## 5. Recovery
- If any file is found to be missing or lost, restore it from the archive or version control immediately.
- Document the recovery in the migration log.

---

By following this policy, you guarantee that all valuable content is preserved, all provenance is clear, and the project remains fully auditable and trustworthy throughout consolidation.
