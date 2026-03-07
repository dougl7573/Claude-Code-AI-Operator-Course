# Drive Invoice Automation (Lesson 2.3)

This folder contains a **watcher** that monitors a Google Drive folder for new invoice PDFs, runs them through the [Lesson 2.2 pipeline](../current-data-samples/) (extract → validate → vendor check → Airtable), and moves processed files to a "Processed" folder.

## Setup

### 1. Google Cloud & OAuth

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create or select a project and enable **Google Drive API**.
3. Create **OAuth 2.0 credentials** (Desktop application).
4. Download the JSON and save it as **`credentials.json`** in this folder (`drive-invoice-automation/`).

### 2. Drive folders

1. In Google Drive, create two folders, e.g.:
   - **Invoices - To Process** (drop new PDFs here)
   - **Invoices - Processed** (watcher moves files here after success)
2. Open each folder and copy its **Folder ID** from the URL:  
   `https://drive.google.com/drive/folders/FOLDER_ID`
3. Set the IDs in **`config.py`**:
   - `TO_PROCESS_FOLDER_ID` = ID of "To Process"
   - `PROCESSED_FOLDER_ID` = ID of "Processed"  
   Or set env vars: `DRIVE_TO_PROCESS_FOLDER_ID`, `DRIVE_PROCESSED_FOLDER_ID`.

### 3. Dependencies

From this folder:

```bash
pip install -r requirements.txt
pip install -r ../current-data-samples/requirements.txt
```

The pipeline (Airtable token, vendor list) is in `../current-data-samples/`. Ensure that folder is set up and working (e.g. run `python3 invoice_pipeline.py` from there once).

## Run

- **One-time run** (check folder once and exit):
  ```bash
  python3 drive_invoice_watcher.py --once
  ```

- **Continuous** (check every 5 minutes by default):
  ```bash
  python3 drive_invoice_watcher.py
  ```

On first run you'll get a browser login to authorize Drive; a `token.json` will be created for future runs.

Logs go to **`automation.log`** in this folder and to the console. To change the check interval, edit `CHECK_INTERVAL_SECONDS` in `config.py` or set `DRIVE_CHECK_INTERVAL` (seconds).

## Flow

1. List PDFs in the "To Process" folder.
2. For each PDF: download to a temp file → run `invoice_pipeline.process_invoice(pdf_path, vendor_file=...)` → if success, move file in Drive to "Processed".
3. Failures are logged; the file stays in "To Process" for retry or manual handling.

## Files

| File | Purpose |
|------|---------|
| `config.py` | Folder IDs, interval, log path, paths to pipeline |
| `drive_invoice_watcher.py` | Drive auth, list/download/move, calls pipeline |
| `credentials.json` | You add: OAuth client JSON from Google Cloud |
| `token.json` | Created after first login; do not commit |
| `automation.log` | Created when watcher runs |
