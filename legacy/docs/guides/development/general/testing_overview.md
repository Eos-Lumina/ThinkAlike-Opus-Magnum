---
title: TESTING.md
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# TESTING.md

This guide explains how to run, write, and contribute tests for ThinkAlike.

## How to Run Tests

### Frontend (Next.js)
```
cd app
npm test
```

### Backend/Agents
```
cd tests
pytest  # or your preferred Python test runner
```

### CI/CD
All tests are run automatically on push/PR via GitHub Actions (see `.github/workflows/ci.yml`).

## Test Types
- Unit: `tests/unit/`
- Integration: `tests/integration/`
- UI: `tests/ui/`
- Ethical: `tests/ethical/`
- Forks: `tests/forks/`
- Mock Data: `tests/mock_data/`

## Writing Tests
- Follow the code style and PET/Clarity guidelines.
- Add new tests for every new feature or bugfix.
- See `tests/README.md` for philosophy and structure.

## More Info
- [Testing Framework Overview](tests/README.md)
- [PET/Clarity Guidelines](docs/pet_clarity.md)
