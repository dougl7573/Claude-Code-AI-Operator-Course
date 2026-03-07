"""
Configuration for Drive Invoice Watcher (Lesson 2.3).
Edit these values for your setup.
"""

import os

# Google Drive folder IDs (from the folder URL: .../folders/FOLDER_ID)
# Create two folders in Drive: "Invoices - To Process" and "Invoices - Processed"
# Open each folder and copy the ID from the URL.
TO_PROCESS_FOLDER_ID = os.environ.get("DRIVE_TO_PROCESS_FOLDER_ID", "1ADzLuwJ9EAjYuDwDuXoLB-keFQUKdkM5")
PROCESSED_FOLDER_ID = os.environ.get("DRIVE_PROCESSED_FOLDER_ID", "13OzOdM4xQ0vNLMueaOYklIY-9nxtMIhf")

# How often to check for new files (seconds). Default: 5 minutes.
CHECK_INTERVAL_SECONDS = int(os.environ.get("DRIVE_CHECK_INTERVAL", "300"))

# Log file path (relative to this script's directory)
LOG_FILE = os.environ.get("DRIVE_LOG_FILE", "automation.log")

# Path to the invoice pipeline (Lesson 2.2) - sibling folder current-data-samples
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PIPELINE_DIR = os.path.join(SCRIPT_DIR, "..", "current-data-samples")
VENDOR_LIST_PATH = os.path.join(PIPELINE_DIR, "vendor-list.csv")
