@echo off
REM -- Ensure you’re in the repo root --
cd /d %~dp0

REM -- Install dependencies if needed --
pip install fastapi uvicorn[standard] >nul

REM -- Pick one of the two lines below: --

REM 1) No auto-reload:
REM uvicorn src.backend.app.main:app

REM 2) Auto-reload, but only on agent&API changes:
uvicorn src.backend.app.main:app --reload --reload-dir src/backend/app/agents --reload-dir src/backend/app/api --reload-exclude src/backend/app/schemas
