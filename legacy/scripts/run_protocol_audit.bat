@echo off
REM Run the protocol audit automation script with one double-click
cd /d %~dp0
python scripts\protocol_audit_automation.py
pause
