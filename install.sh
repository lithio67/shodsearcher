#!/bin/bash

# Define the location where the script will be installed
INSTALL_DIR="$HOME/.local/bin"
SCRIPT_URL="https://raw.githubusercontent.com/lithio67/shodsearcher/main/shodsearcher.py"
# Create the installation directory if it doesn't exist
mkdir -p "$INSTALL_DIR"

# Download the shodsearcher.py script
curl -o "$INSTALL_DIR/shodsearcher" "$SCRIPT_URL"

# Make the script executable
chmod +x "$INSTALL_DIR/shodsearcher"

# Create a symlink to make the command globally accessible
ln -sf "$INSTALL_DIR/shodsearcher" "/usr/local/bin/shodsearcher"

# Print a success message
echo "shodsearcher has been successfully installed!"

