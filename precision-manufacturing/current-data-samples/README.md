# Invoice pipeline and PDF extraction

This folder contains the **invoice pipeline** (Lesson 1.3) plus **PDF extraction** (Module 2 / Lesson 2.2 style): load from JSON or PDF → validate → vendor check → transform → Airtable.

## Setup

```bash
pip install -r requirements.txt
```

(`requirements.txt` includes `pdfplumber` for PDF extraction.)

## Run the pipeline

**From JSON (default):**
```bash
python3 invoice_pipeline.py
# or
python3 invoice_pipeline.py sample-invoice-data.json
```

**From a PDF:**
```bash
python3 invoice_pipeline.py invoices/invoice-001-acme-corp.pdf
```

**Batch (all PDFs in a folder):**
```bash
python3 invoice_pipeline.py invoices/
```
Processes every PDF in `invoices/` and prints a summary (Total / Successful / Failed).

For course sample PDFs (`invoices/invoice-XXX-*.pdf`), the **vendor name** is taken from the filename (e.g. `invoice-001-acme-corp.pdf` → Acme Corp) so the vendor list lookup succeeds. For other PDFs, vendor is parsed from the PDF text.

## Extract only (no Airtable)

To see the extracted data from a PDF without running the full pipeline:

```bash
python3 extract_invoice_pdf.py invoices/invoice-001-acme-corp.pdf
```

## Files

| File | Purpose |
|------|--------|
| `extract_invoice_pdf.py` | Extract invoice fields + line items from a PDF (pdfplumber). |
| `invoice_pipeline.py` | Full pipeline: load (JSON/PDF) → validate → vendor → transform → Airtable. |
| `validate_invoice.py` | Load JSON invoice and validate line-item and total math. |
| `parse_vendors.py` | Load and search `vendor-list.csv`. |
| `transform_invoice.py` | Convert invoice dict to Airtable shape. |
| `airtable_test.py` | Airtable API: create/list records (token and base ID configured there). |
| `vendor-list.csv` | Approved vendors. |
| `sample-invoice-data.json` | Sample invoice for JSON path. |
| `invoices/*.pdf` | Sample invoice PDFs for testing. |

## Airtable

Credentials (token, base ID) are in `airtable_test.py`. If the **Notes** field causes a 422, the pipeline retries without Notes and still creates the record.
