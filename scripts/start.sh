#!/bin/bash

# Get today's date in YYYY-MM-DD format
DATE=$(date +%F)

# Set paths
SRC_DIR="/home/blackteam/DWAYNE-INATOR-5000"
BACKUP_DIR="/home/blackteam/backups"

# Ensure the backup directory exists
mkdir -p "$BACKUP_DIR"

# Move and rename database
mv "$SRC_DIR/dwayne.db" "$BACKUP_DIR/dwayne-$DATE.db"

# Move and rename submissions directory
mv "$SRC_DIR/submissions" "$BACKUP_DIR/submissions-$DATE"

# Recreate submissions directory
mkdir "$SRC_DIR/submissions"

# Start the service
sudo systemctl start dwayne.service
