#!/usr/bin/env python3
"""Transform invoice JSON into the format Airtable expects (field names + line items in Notes)."""

import json


def transform_invoice_for_airtable(invoice):
    """Convert invoice JSON to Airtable record format."""
    line_items_text = "Line Items:\n"
    for item in invoice.get("line_items", []):
        line_items_text += (
            f"- {item['description']}: {item['quantity']} × ${item['unit_price']} = ${item['total']}\n"
        )
    notes = line_items_text.rstrip()
    if invoice.get("notes"):
        notes += f"\n\n{invoice['notes']}"

    return {
        "Invoice Number": invoice["invoice_number"],
        "Vendor": invoice["vendor_name"],
        "Invoice Date": invoice["invoice_date"],
        "Due Date": invoice["due_date"],
        "Amount": invoice["total_amount"],
        "Status": "Received",
        "Notes": notes,
    }


def main():
    with open("sample-invoice-data.json", "r", encoding="utf-8") as f:
        invoice = json.load(f)

    print("Original invoice data:")
    print(json.dumps(invoice, indent=2))
    print("\n" + "=" * 50 + "\n")

    airtable_data = transform_invoice_for_airtable(invoice)
    print("Transformed for Airtable:")
    print(json.dumps(airtable_data, indent=2))
    print("\n" + "=" * 50)
    print("\nThis is ready to send to the Airtable API.")


if __name__ == "__main__":
    main()
