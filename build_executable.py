"""
PyInstaller Build Script
Creates standalone executable for JayaMotor application
"""

import subprocess
import sys
import os
from pathlib import Path

def build_executable():
    """Build PyInstaller executable"""

    # Project root
    project_root = Path(__file__).parent

    # Ensure PyInstaller is installed
    print("📦 Checking PyInstaller...")
    try:
        import PyInstaller
        print(f"✅ PyInstaller {PyInstaller.__version__} found")
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

    # Build command
    cmd = [
        "pyinstaller",
        "--name=JayaMotor",
        "--onefile",
        "--windowed",
        "--icon=data/jaya_motor.ico" if Path("data/jaya_motor.ico").exists() else "",
        "--add-data=database:database",
        "--add-data=business:business",
        "--add-data=ui:ui",
        "--hidden-import=PyQt6",
        "--hidden-import=sqlalchemy",
        "--hidden-import=openpyxl",
        "--hidden-import=reportlab",
        "--distpath=dist",
        "--buildpath=build",
        "--specpath=.",
        "main.py"
    ]

    # Remove empty strings
    cmd = [c for c in cmd if c]

    print("\n🔨 Building executable...")
    print(f"Command: {' '.join(cmd)}")

    try:
        result = subprocess.run(cmd, cwd=project_root, check=True)
        print("\n✅ Build completed successfully!")
        print(f"📁 Executable location: {project_root / 'dist' / 'JayaMotor.exe'}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Build failed: {e}")
        return False

if __name__ == "__main__":
    success = build_executable()
    sys.exit(0 if success else 1)
