@echo off
REM Undo Import Script for Windows
REM Restore database from most recent backup

echo.
echo ========================================
echo     JayaMotor - Undo Import
echo ========================================
echo.

echo Listing available backups...
python undo_import.py

pause
