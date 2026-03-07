#!/usr/bin/env python3
"""
One-off script: find Airtable invoice records with wrong Invoice Number (e.g. OICE)
and update them to the correct number by matching Vendor + Amount to known sample invoices.
"""

from airtable_test import get_invoices, update_invoice

# Known correct invoice numbers by (vendor substring, amount) from sample PDFs
VENDOR_AMOUNT_TO_INVOICE = [
    ("Acme Corp", 1242.0, "INV-2024-0342"),
    ("Widget Supplies", 3499.74, "WS-789456"),
    ("Tech Parts", 945.0, "TP-2024-0891"),
    ("Global Shipping", 2824.2, "GS-2024-1556"),
    ("Office Depot", 3918.79, "OD-2024-8823"),
]


def _amount_match(a, b, tolerance=0.02):
    if a is None or b is None:
        return False
    return abs(float(a) - float(b)) <= tolerance


def find_correct_invoice_number(vendor, amount):
    """Return correct invoice number for this vendor/amount, or None."""
    if not vendor or amount is None:
        return None
    vendor_str = (vendor or "").strip()
    amt = float(amount) if amount is not None else None
    for vendor_sub, expected_amt, inv_num in VENDOR_AMOUNT_TO_INVOICE:
        if vendor_sub.lower() in vendor_str.lower() and _amount_match(amt, expected_amt):
            return inv_num
    return None


def main():
    data = get_invoices()
    if not data:
        print("Could not fetch Airtable data.")
        return

    records = data.get("records", [])
    bad_values = ("oice", "OICE", "number", "inv")  # wrong extractions to fix

    updated = 0
    for rec in records:
        rid = rec["id"]
        fields = rec.get("fields", {})
        inv_num = fields.get("Invoice Number") or ""
        vendor = fields.get("Vendor")
        amount = fields.get("Amount")

        if inv_num and len(inv_num) >= 8 and inv_num.lower() not in bad_values:
            if "-" in inv_num or inv_num.replace("-", "").replace(" ", "").isalnum():
                continue

        is_bad = not inv_num or inv_num.strip().lower() in bad_values or len(inv_num.strip()) <= 4
        if not is_bad:
            continue

        correct = find_correct_invoice_number(vendor, amount)
        if not correct:
            print(f"  Skip {rid}: Vendor={vendor}, Amount={amount} (no match)")
            continue

        print(f"  Updating {rid}: '{inv_num}' -> '{correct}' (Vendor={vendor}, Amount={amount})")
        result = update_invoice(rid, {"Invoice Number": correct})
        if result:
            updated += 1
        else:
            print(f"    Failed to update {rid}")

    print(f"\nDone. Updated {updated} record(s).")


if __name__ == "__main__":
    print("Fetching invoices and fixing records with wrong Invoice Number...\n")
    main()
