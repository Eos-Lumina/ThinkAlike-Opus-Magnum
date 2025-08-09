# Project Health Automation

## Linting
- Run `npm run lint` to check TypeScript/React files for errors.
- Run `npm run lint:json` to validate JSON files.

## Testing
- Run `npm run test` to execute Python tests (backend).

## Pre-commit Hook
- Husky will block commits if lint or test fails.
- To set up Husky, run:
  ```sh
  npx husky install
  npx husky add .husky/pre-commit "npm run lint && npm run lint:json && npm run test"
  ```

## Maintenance
- Regularly run lint and test scripts.
- Clean up any files with errors before committing.

## Contributor Guide
- All new code must pass lint and tests before merging.
- Document any major fixes in the migration log or README.
