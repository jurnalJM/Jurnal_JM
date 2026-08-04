#!/bin/bash
# Clear Database Script for Linux/Mac
# Run this to delete database.db and reinitialize

echo ""
echo "========================================"
echo "     JayaMotor - Clear Database"
echo "========================================"
echo ""
echo "This will DELETE all data in the database"
echo "Master data will be reseeded"
echo ""

read -p "Continue? (type 'yes' to confirm): " CONFIRM

if [ "$CONFIRM" != "yes" ]; then
    echo "Cancelled."
    exit 0
fi

echo ""
echo "Stopping server (if running)..."
pkill -f "python.*app" 2>/dev/null

echo "Clearing database..."
python clear_data.py

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================"
    echo "     Database cleared successfully!"
    echo "========================================"
    echo ""
    echo "To start the server again:"
    echo "  python app.py"
    echo ""
else
    echo ""
    echo "ERROR: Failed to clear database"
    echo ""
fi
