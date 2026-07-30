"""
Setup configuration for JayaMotor application
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="jayamotor",
    version="2.0.0",
    description="Modern Motor Sales Management System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Development Team",
    author_email="dev@jayamotor.com",
    url="https://github.com/jayamotor/jayamotor-python",
    license="Proprietary",
    packages=find_packages(),
    python_requires=">=3.11",
    install_requires=[
        "PyQt6>=6.6.0",
        "SQLAlchemy>=2.0.0",
        "openpyxl>=3.1.0",
        "reportlab>=4.0.0",
        "python-dotenv>=1.0.0",
        "pandas>=2.0.0",
        "Pillow>=10.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "pytest-qt>=4.2.0",
            "black>=23.11.0",
            "pylint>=3.0.0",
            "flake8>=6.1.0",
        ],
        "build": [
            "PyInstaller>=6.1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "jayamotor=main:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Business",
        "License :: Other/Proprietary License",
        "Natural Language :: Indonesian",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business",
    ],
    keywords=[
        "motor",
        "sales",
        "management",
        "inventory",
        "leasing",
    ],
)
