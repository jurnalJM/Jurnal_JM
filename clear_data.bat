@echo off
REM Clear Database Script for Windows
REM Run this to delete database.db and reinitialize

echo.
echo ========================================
echo     JayaMotor - Clear Database
echo ========================================
echo.
echo This will DELETE all data in the database
echo Master data will be reseeded
echo.

set /p CONFIRM="Continue? (type 'yes' to confirm): "
if /i not "%CONFIRM%"=="yes" (
    echo Cancelled.
    pause
    exit /b 0
)

echo.
echo Stopping server (if running)...
taskkill /F /IM python.exe >nul 2>&1

echo Clearing database...
python clear_data.py

if %ERRORLEVEL% equ 0 (
    echo.
    echo ========================================
    echo     Database cleared successfully!
    echo ========================================
    echo.
    echo To start the server again:
    echo   python app.py
    echo.
) else (
    echo.
    echo ERROR: Failed to clear database
    echo.
)

pause
