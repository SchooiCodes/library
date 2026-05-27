#!/bin/bash
# Run admin panel for Tech Library
# Uses virtual environment to avoid system package conflicts

VENV_DIR="/tmp/admin_venv"

if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
    "$VENV_DIR/bin/pip" install flask -q
fi

echo "Starting Tech Library Admin Panel..."
echo "Access at: http://127.0.0.1:5050"
exec "$VENV_DIR/bin/python3" "$(dirname "$0")/app.py"
