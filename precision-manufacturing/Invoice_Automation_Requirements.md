# Invoice Automation – Requirements & Design

**Project:** Finance invoice processing automation (Precision Manufacturing)  
**Source:** Finance department interview (Marcus Rodriguez, Elena), Lesson 2.1  
**Purpose:** Turn manual PDF → Airtable data entry into an automated pipeline with human review where needed.

---

## 1. Current State (What exists now?)

- **Manual process:** Elena checks invoices@precisionmfg.com daily; 15–25 emails with PDF attachments. She downloads each PDF, opens it, and manually types into Airtable: invoice number, vendor, invoice date, due date, total amount, line items (sometimes 20+). Then she saves the PDF to Google Drive (by vendor) and replies to the sender.
- **Who / when / how often:** Elena (and similarly Priya for 1099s, James for expenses). Every morning; 2–3 hours for invoice data entry alone.
- **Time per invoice:** 5–8 minutes straightforward; up to 15 minutes if messy or many line items.
- **Systems/tools:** Google Workspace (inbox), Airtable (Finance & Accounting base, Invoices table), Google Drive (Invoices folder by vendor). Volume: 15–25 invoices/day (~350–500/month).
- **What breaks / delays:** Typos and misreads (e.g. $18,500 vs $1,850). If Elena is out, data entry backs up; approvals and payments are delayed.

---

## 2. Desired State (What should exist?)

- **Success vision (Marcus):** System checks inbox, downloads PDFs, extracts data with high accuracy (95%+), creates Airtable records, files PDFs in Drive, flags uncertain items for human review. Elena shifts from 2–3 hours of typing to ~20–30 minutes of review.
- **What stays manual:** Review of flagged invoices; approval workflows; exception handling; replying to senders (can be phased later).
- **Who uses the automation:** Initially Elena (and Marcus for oversight); design so Finance can troubleshoot with minimal IT.
- **Happy path:** PDF available (e.g. in a folder or inbox) → automation extracts core fields → record created in Airtable with status “Received” or “Under Review” → PDF filed in Drive (later phase) → uncertain extractions flagged for Elena.

---

## 3. Success Criteria (How we measure success?)

- **Time:** Reduce Elena’s invoice data-entry time from 2–3 hours to under 30 minutes (review only).
- **Accuracy:** 95%+ of extracted records correct without manual correction; remaining flagged for review.
- **Volume:** Handle 15–25 invoices per run; full batch in under ~5 minutes.
- **ROI:** Prefer low/no incremental cost (previous Zapier attempt was ~$200/month and failed).
- **Maintainability:** Elena or Marcus can follow runbook to rerun or troubleshoot; no “only the consultant knows how” situation.

---

## 4. Edge Cases & Failure Modes (What could go wrong?)

- **Scanned/blurry PDFs:** Extraction may fail or be wrong → flag for human review; create Airtable record with status “Needs Review” and preserve original PDF.
- **Wrong format (e.g. Word, image-only):** Detect non-PDF or unreadable file → skip or flag; log and optionally notify.
- **Missing required fields (no date, no amount):** Partial extraction → create record with “Needs Review”; log missing fields.
- **Vendor not in approved list:** Validation step → do not create record (or create with “Needs Review”); log and list for Marcus.
- **Airtable API down / rate limit / 4xx:** Retry with backoff; log failure; do not lose the PDF (keep in queue or “failed” folder).
- **Duplicate invoice (same invoice number already in Airtable):** Check before insert → skip and log, or flag for review.
- **Math doesn’t add up (subtotal + tax ≠ total):** Validation → flag for review; still create record with status “Needs Review”.
- **Previous Zapier failure:** Avoid opaque, undocumented integrations; prefer simple, documented pipeline (e.g. local script or clear n8n workflow) so Finance can understand and maintain.

---

## 5. Technical Constraints

- **Budget:** Prefer free or low-cost (no recurring Zapier-style cost if possible).
- **Integrations:** Must work with Airtable (Invoices table). Email and Google Drive are Phase 2+.
- **Access/security:** Credentials in .env or secure config; never commit tokens. Marcus can provide test base and token.
- **Maintenance:** Must be maintainable by Elena/Marcus with runbook; minimal dependency on IT.
- **Scale:** 15–25 invoices/day; no need for thousands per hour.
- **Existing Airtable structure:** Invoice Number, Vendor (link), Invoice Date, Due Date, Amount, Status (Received / Under Review / Approved / Paid), PDF File (attachment), Notes (long text).

---

## 6. Acceptance Criteria

**AC1 – Happy path (standard digital PDF)**  
- **Given:** A standard digital PDF invoice in the input folder (e.g. `invoices/` or `test_data/`).  
- **When:** The automation runs.  
- **Then:** Invoice number, vendor name, invoice date, due date, and total amount are extracted with 95%+ accuracy; a record is created in Airtable with Status “Received”; run is logged.

**AC2 – Error case (bad / unreadable PDF)**  
- **Given:** A scanned/blurry or corrupted PDF.  
- **When:** The automation runs.  
- **Then:** The system flags the invoice for human review; a record is created in Airtable with Status “Needs Review”; original PDF is preserved; failure or warning is logged.

**AC3 – Volume (multiple invoices)**  
- **Given:** 25 invoices in the input folder.  
- **When:** The automation runs.  
- **Then:** All 25 are processed within 5 minutes; success and failure counts are logged; failed or flagged items are listed (e.g. in log or report).

**AC4 – Data accuracy (correct extraction)**  
- **Given:** A PDF with known invoice number, vendor, date, amount.  
- **When:** The automation runs.  
- **Then:** Extracted values match the known values (or are within acceptable tolerance); line-item math (subtotal + tax = total) is validated; mismatches result in “Needs Review” and are logged.

**AC5 – Integration (Airtable update)**  
- **Given:** Valid extracted data and a working Airtable token/base.  
- **When:** The automation runs.  
- **Then:** A record is created in the Invoices table with correct field mapping; if Airtable returns 4xx/5xx, the run logs the error and does not silently drop the invoice (e.g. keep in queue or “failed” list).

---

## 7. Build Phases

**MVP (Week 1 – Lesson 2.2)**  
- **What it does:** Process PDFs from a local folder (e.g. `current-data-samples/invoices/`). Extract core fields (invoice #, vendor, date, amount). Validate math and vendor against `vendor-list.csv`. Create record in Airtable. Log successes and failures.  
- **What it doesn’t do yet:** No email monitoring, no Google Drive filing, no web UI.  
- **Why it’s valuable:** Proves PDF extraction and Airtable integration; Elena can drop PDFs into the folder and run the script (or run it on demand).  
- **What we’ll test:** Sample invoices (clean, multi-page, messy); vendor validation; Airtable create; logging.

**Phase 2 (later)**  
- **What we add:** Google Drive monitoring (or watched folder); automatically process new PDFs; move processed files to “done” (or equivalent).  
- **Why it matters:** Reduces manual “drop in folder and run”; more automated trigger.  
- **When:** After MVP is stable and accepted by Finance.

**Phase 3 (optional)**  
- **What we add:** Web upload interface so Elena can upload PDFs in a browser; display extracted data for review before/after create.  
- **Nice-to-haves:** Email notifications, weekly summary report.  
- **When:** If Marcus/Elena want a user-friendly interface and we have capacity.

---

## 8. Technical Approach

- **MVP:** Python script (local). Reasons: fast to build, easy to debug, full control over PDF parsing and Airtable API; matches existing course materials (`invoice_pipeline.py`, `extract_invoice_pdf.py`).  
- **Phase 2:** Same Python script plus folder watcher or scheduled run; or n8n workflow that calls the script or replicates logic (if team prefers visual workflows).  
- **Phase 3:** Web app (e.g. Flask/FastAPI + simple UI) or n8n + form; deploy to Vercel or similar if needed.  
- **Tools/libraries:** Python 3.8+; pdfplumber (or PyPDF2) for PDF text/tables; requests for Airtable API; python-dotenv for .env; standard library for logging and file handling.  
- **Credentials:** Airtable token and base ID in `.env` (or in a config file that is not committed).  
- **Conventions:** Follow CLAUDE.md patterns—paths, logging, error handling, no hardcoded secrets.

---

## 9. Error Handling Plan

| Error Type        | Cause                    | Detection Method              | Handling Strategy                    | Logging Approach                          |
|-------------------|--------------------------|-------------------------------|-------------------------------------|------------------------------------------|
| File not found    | Wrong path, file moved   | Check path before read        | Log error; skip file; continue      | Log file path, error message              |
| PDF won’t open    | Corrupted, wrong format  | try/except on PDF open        | Flag for review; skip or partial    | Log filename, exception                   |
| Extraction fails  | Scanned image, odd layout| Missing/invalid key fields    | Partial data + “Needs Review”        | Log missing fields, filename             |
| Airtable API error| Rate limit, 4xx/5xx, bad token | Response status code     | Retry with backoff (e.g. 2 retries); then log and keep in “failed” list | Log status, body, filename   |
| Duplicate invoice | Same invoice # in base  | Check before create (optional)| Skip and log; or flag for review     | Log invoice number, “duplicate”           |
| Vendor not in list| Vendor not in vendor-list.csv | Vendor lookup returns none | Do not create (or create “Needs Review”); log | Log vendor name, filename        |
| Math validation   | Subtotal + tax ≠ total   | validate_invoice_math         | Flag “Needs Review”; still create   | Log expected vs actual                    |

---

## 10. Testing Strategy

**Unit testing**  
- **What:** Test PDF read and extraction with 3–5 sample invoices (one clean, one multi-page, one messy/scanned). Test vendor lookup and math validation with known data. Test Airtable create with dummy record (test base).  
- **Sample data:** Use `current-data-samples/invoices/*.pdf` and known expected output (e.g. from `sample-invoice-data.json` shape).  
- **Success:** Each function behaves as expected; extraction matches known values for sample PDFs.

**Integration testing**  
- **What:** Run full pipeline on 5–10 invoices in a test folder; verify Airtable records created; verify logs and any “Needs Review” or failed items.  
- **How:** Use test Airtable base; compare created records to source PDFs.  
- **Success:** End-to-end flow works; errors are logged and handled per Error Handling Plan.

**Production testing**  
- **What:** Run on real invoices alongside manual process; Elena reviews every automated record; measure accuracy and edge cases.  
- **How:** Run in parallel first; track corrections and failures; iterate; then switch to automation-first with review.  
- **Success:** 95%+ accuracy; Elena trusts the system; ready to rely on automation for daily runs.

---

*This document is the design for the invoice automation MVP and later phases. Implementation plan is in `Invoice_Automation_Implementation_Plan.md`.*
