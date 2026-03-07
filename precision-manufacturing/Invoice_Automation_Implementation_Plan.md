# Invoice Automation – Implementation Plan (MVP)

**Purpose:** Step-by-step build plan for the invoice automation MVP (Lesson 2.2).  
**Reference:** `Invoice_Automation_Requirements.md`  
**Conventions:** Use paths and patterns from repo CLAUDE.md; credentials in .env or untracked config; log all runs.

---

## Step 1: Set up development environment

- [ ] Ensure Python 3.8+ is installed (`python3 --version`).
- [ ] Create project folder structure (or use existing `current-data-samples/`):
  - Input folder for PDFs (e.g. `invoices/`).
  - Optional: `processed/`, `logs/` if moving files or writing log files.
- [ ] Create `.env` (or equivalent) for Airtable token and base ID; add `.env` to `.gitignore`.
- [ ] Install dependencies: `pip install -r requirements.txt` (e.g. pdfplumber, requests, python-dotenv if used).

**Test:** Run `python3 -c "import pdfplumber; print('ok')"`.  
**Time estimate:** 15–30 min.

---

## Step 2: Verify Airtable connection

- [ ] Get Airtable API token (create at airtable.com/create/tokens) with scope for target base.
- [ ] Get base ID from Airtable API docs for your base.
- [ ] Write a small script (or use existing `airtable_test.py`) that creates one test record in the Invoices table.
- [ ] Run it and confirm the record appears in Airtable.

**Test:** One record created with dummy data; no 401/403.  
**Time estimate:** 15–30 min.

---

## Step 3: Implement or wire PDF read

- [ ] Implement (or reuse) a function that opens a PDF from a given path and returns raw text/tables (e.g. using pdfplumber).
- [ ] Handle file-not-found and corrupted-PDF errors; log and return None or raise clearly.
- [ ] Test with one sample PDF from `invoices/` (e.g. `invoice-001-acme-corp.pdf`).

**Test:** Function returns text/tables for a valid PDF; logs or raises for missing/corrupt file.  
**Time estimate:** 30–60 min.

---

## Step 4: Implement data extraction from PDF

- [ ] Implement (or reuse) extraction logic: invoice number, vendor, invoice date, due date, subtotal, tax, total, line items.
- [ ] Return a single dict matching the shape expected by the rest of the pipeline (e.g. `sample-invoice-data.json`).
- [ ] Test with 2–3 sample PDFs; compare key fields to known values.
- [ ] For course sample PDFs, optionally derive vendor from filename when label is present.

**Test:** Extracted dict has required keys; numbers and dates are parseable and reasonable.  
**Time estimate:** 1–2 hours.

---

## Step 5: Implement (or reuse) invoice math validation

- [ ] Implement (or reuse) validation: line items sum to subtotal; subtotal + tax = total.
- [ ] Return a list of error strings; empty list if valid.
- [ ] Test with valid and invalid payloads (e.g. from `validate_invoice.py`).

**Test:** Valid invoice passes; invalid totals or line items produce clear error messages.  
**Time estimate:** 30 min.

---

## Step 6: Implement (or reuse) vendor lookup

- [ ] Load approved vendor list (e.g. `vendor-list.csv`).
- [ ] Implement (or reuse) search by vendor name (exact and/or fuzzy).
- [ ] Return whether vendor is found and active; use for “create or flag” decision.
- [ ] Test with known vendors and unknown names.

**Test:** Known vendor returns found; unknown vendor returns not found; behavior matches requirements.  
**Time estimate:** 30 min.

---

## Step 7: Implement transform to Airtable shape

- [ ] Implement (or reuse) mapping from internal invoice dict to Airtable fields (Invoice Number, Vendor, Invoice Date, Due Date, Amount, Status, Notes if used).
- [ ] Handle line items (e.g. in Notes or separate field) per Airtable schema.
- [ ] Ensure field types and lengths match Airtable (e.g. Notes as long text).

**Test:** Transform of `sample-invoice-data.json` produces a dict that succeeds when sent to Airtable create.  
**Time estimate:** 30 min.

---

## Step 8: Wire pipeline: load → validate → vendor → transform → create

- [ ] Implement (or reuse) main pipeline: load from JSON or PDF path → validate math → vendor check → transform → create record via Airtable API.
- [ ] Use credentials from .env or config (no hardcoded tokens in committed code).
- [ ] On Airtable 4xx (e.g. 422 on Notes): retry without Notes or skip Notes per requirements.
- [ ] Log each step (e.g. [1/5] … [5/5]) and final success/failure.

**Test:** Run pipeline on one PDF and one JSON; confirm record in Airtable and logs.  
**Time estimate:** 30–60 min.

---

## Step 9: Add error handling and logging

- [ ] Ensure all failure modes from Error Handling Plan are covered: file not found, PDF read failure, extraction failure, validation failure, vendor not found, Airtable errors.
- [ ] Log at least: filename, step, success/failure, and error message or status code.
- [ ] Optionally write to a `logs/` file with date or run id.

**Test:** Run with one bad PDF and one good PDF; verify failures are logged and good one still creates record.  
**Time estimate:** 30 min.

---

## Step 10: Support batch run (multiple PDFs)

- [ ] Accept multiple paths or a folder path; loop over PDFs and run pipeline for each.
- [ ] Collect success/failure counts; log summary at end.
- [ ] Optionally list failed or “Needs Review” items in log or stdout.

**Test:** Run on all sample invoices in `invoices/`; verify count and that each record appears in Airtable (or is correctly skipped/flagged).  
**Time estimate:** 30 min.

---

## Step 11: Integration test against acceptance criteria

- [ ] Run through AC1–AC5 from `Invoice_Automation_Requirements.md`:
  - AC1: One standard PDF → record created, correct fields.
  - AC2: One bad PDF → flagged/“Needs Review” and logged.
  - AC3: Batch of ~5–10 PDFs → all processed, counts and failures logged.
  - AC4: Known PDF → extracted data matches expected; math validated.
  - AC5: Airtable create succeeds; on API error, log and do not drop invoice.
- [ ] Fix any gaps (e.g. status “Needs Review”, logging, retries).

**Test:** All acceptance criteria pass or are explicitly deferred with a note.  
**Time estimate:** 30–60 min.

---

## Step 12: Document run instructions and update CLAUDE.md

- [ ] Document in README or CLAUDE.md: how to install deps, set credentials, run pipeline (JSON vs PDF, single vs batch).
- [ ] Add any new conventions (paths, env vars, log location) to CLAUDE.md.
- [ ] Note known limitations and Phase 2/3 ideas.

**Test:** Another person (or you in a fresh shell) can run the pipeline using only the docs.  
**Time estimate:** 15–30 min.

---

**Total estimated time:** ~4–7 hours for first full pass.

**Note for this repo:** Steps 3–8 and 10 are largely implemented in `current-data-samples/` (e.g. `extract_invoice_pdf.py`, `validate_invoice.py`, `parse_vendors.py`, `transform_invoice.py`, `invoice_pipeline.py`). Use this plan to validate, extend (e.g. batch, logging, “Needs Review”), and document rather than rebuild from zero.
