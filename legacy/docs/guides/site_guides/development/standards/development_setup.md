---
title: Development Setup
version: 1.0.1
status: Canonical
last_updated: 2025-06-23
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
tags:
- standards
---


# Development Setup

This guide provides the authoritative, up-to-date instructions for setting up a ThinkAlike development environment. All steps are verified against the live project structure and scripts.

## Prerequisites
- **Python 3.10+** (for backend and scripts)
- **Node.js (v18+) & npm** (for frontend)
- **Git** (for version control)
- **PostgreSQL** (for production; SQLite is used for local development)
- **PowerShell** (Windows users; for setup script)

## 1. Clone the Repository
```powershell
git clone https://github.com/your-org/thinkalike.git
cd thinkalike
```

## 2. Install Python Dependencies
Run the setup script (Windows/PowerShell):
```powershell
./scripts/setup-dev-env.ps1
```
This will:
- Upgrade pip
- Install all Python dependencies from `requirements.txt`
- Attempt to install pre-commit hooks (if configured)

*If you encounter issues, you can manually run:*
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 3. Install Node.js Dependencies
```powershell
npm install
```

## 4. Environment Configuration
- Copy the example environment file and edit as needed:
```powershell
cp .env.example .env
```
- Edit `.env` with your local settings (database, API keys, etc.)

## 5. Running the Project
- **Frontend (Next.js):**
  ```powershell
  npm run dev
  ```
- **Backend (FastAPI):**
  ```powershell
  uvicorn src.backend.app.main:app --reload
  ```

## 6. Database
- **Development:** Uses SQLite by default (no setup needed)
- **Production:** Set up PostgreSQL and update `.env` accordingly

## 7. Additional Resources & Troubleshooting
- [Onboarding Manual](../../../onboarding/onboarding_manual.md) – Full contributor journey
- [System Blueprint](../../../architecture/system_blueprint.md) – Architecture, modules, and roadmap
- [Technical Stack](../../../architecture/technical_stack.md) – Technologies in use
- [Troubleshooting Guide](../../../architecture/observability_stack_integration_plan.md)

## 8. Contribution Workflow
- Read [CONTRIBUTING.md](../../../../CONTRIBUTING.md) for standards and commit conventions
- Use the [Onboarding Hub](../../../onboarding/readme.md) for orientation and links

---

*This is the single source of truth for development setup. Remove all other setup stubs or duplicates. For updates, always verify instructions against the live project structure and scripts.*
