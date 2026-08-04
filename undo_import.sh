#!/bin/bash
# Undo Import Script for Linux/Mac
# Restore database from most recent backup

echo ""
echo "========================================"
echo "     JayaMotor - Undo Import"
echo "========================================"
echo ""

echo "Listing available backups..."
python undo_import.py
