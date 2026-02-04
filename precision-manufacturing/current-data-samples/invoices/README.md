# Sample Invoice PDFs for Course Testing

This directory contains 5 realistic invoice PDFs that students will use to test their PDF processing automation.

## Invoice Files

### 1. invoice-001-acme-corp.pdf
**Vendor:** Acme Corp
**Invoice #:** INV-2024-0342
**Date:** 01/15/2024
**Due Date:** 02/14/2024
**Total:** $1,242.00
**Format:** Clean, modern digital invoice with colored header and professional table layout
**Line Items:** 2 items (Steel rods, Shipping)
**Complexity:** Medium

### 2. invoice-002-widget-supplies.pdf
**Vendor:** Widget Supplies Inc.
**Invoice #:** WS-789456
**Date:** 01/18/2024
**Due Date:** 02/17/2024
**Total:** $3,499.74
**Format:** Standard business format with centered header and grid layout
**Line Items:** 2 items (Precision bearings, Industrial fasteners)
**Special Notes:** Bulk discount applied - 10%
**Complexity:** Medium

### 3. invoice-003-tech-parts-inc.pdf
**Vendor:** Tech Parts Direct
**Invoice #:** TP-2024-0891
**Date:** 01/20/2024
**Due Date:** 02/04/2024
**Total:** $945.00
**Format:** Different template style with colored sections and notice boxes
**Line Items:** 1 item (Circuit boards - custom order)
**Special Notes:** Express shipping - Due date is strict
**Complexity:** Medium

### 4. invoice-004-global-shipping.pdf
**Vendor:** Global Shipping Solutions
**Invoice #:** GS-2024-1556
**Date:** 01/22/2024
**Due Date:** 02/21/2024
**Total:** $2,824.20
**Format:** Simpler, minimalist format with basic table layout
**Line Items:** 3 items (International freight, Customs clearance, Documentation)
**Complexity:** Low (good for initial testing)

### 5. invoice-005-office-depot.pdf
**Vendor:** Office Depot Industrial Supplies
**Invoice #:** OD-2024-8823
**Date:** 01/25/2024
**Due Date:** 02/24/2024
**Total:** $3,918.79
**Format:** Multi-page invoice with detailed header and many line items
**Line Items:** 20 items (office supplies)
**Additional Fields:** Customer #, P.O. Number, Sales Rep, Ship Via, separate Bill To/Ship To
**Complexity:** High (tests pagination and complex data extraction)

## Expected Output Structure

All invoices should be processed to extract the following data (see `expected-output.json`):

**Required Fields:**
- invoice_number
- vendor_name
- invoice_date (YYYY-MM-DD format)
- due_date (YYYY-MM-DD format)
- total_amount

**Optional Fields:**
- subtotal
- tax
- line_items (array of objects with description, quantity, unit_price, total)
- notes
- confidence_score (AI extraction confidence, 0-1)

## Testing Progression

Students should test their automation in this order:

1. **Start Simple:** invoice-004-global-shipping.pdf (simplest format)
2. **Standard Formats:** invoice-001-acme-corp.pdf and invoice-002-widget-supplies.pdf
3. **Different Template:** invoice-003-tech-parts-inc.pdf (tests template variation handling)
4. **Complex Multi-page:** invoice-005-office-depot.pdf (tests pagination and many line items)

## Validation Rules

Students' automation should validate:
- Invoice dates are valid (YYYY-MM-DD)
- Due date >= Invoice date
- Total amount > 0
- Subtotal + Tax = Total (within $0.10 tolerance)
- Confidence score >= 0.90 (flag for manual review if lower)

## Generation

These PDFs were generated using ReportLab with the script:
`generate_invoices.py`

To regenerate:
```bash
cd current-data-samples
source venv/bin/activate
python3 generate_invoices.py
```
