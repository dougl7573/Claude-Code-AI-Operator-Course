#!/usr/bin/env python3
"""Validate invoice math: line items sum to subtotal, subtotal + tax = total_amount."""

import json

def load_invoice(json_file_path):
    """Load invoice data from JSON file."""
    with open(json_file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def validate_invoice_math(invoice):
    """Check if invoice math is correct. Returns list of error strings (empty if OK)."""
    errors = []

    # Check each line item: quantity * unit_price = total (allow rounding)
    calculated_subtotal = 0.0
    for i, item in enumerate(invoice.get("line_items", [])):
        expected_total = item["quantity"] * item["unit_price"]
        if abs(expected_total - item["total"]) > 0.10:
            errors.append(
                f"Line item {i + 1} ({item['description']}): "
                f"expected {item['quantity']} × {item['unit_price']} = ${expected_total:.2f}, got ${item['total']:.2f}"
            )
        calculated_subtotal += item["total"]

    # Check subtotal matches sum of line items
    if abs(calculated_subtotal - invoice["subtotal"]) > 0.01:
        errors.append(
            f"Subtotal mismatch: line items sum to ${calculated_subtotal:.2f}, "
            f"invoice says ${invoice['subtotal']:.2f}"
        )

    # Check total = subtotal + tax
    expected_total = invoice["subtotal"] + invoice["tax"]
    if abs(expected_total - invoice["total_amount"]) > 0.01:
        errors.append(
            f"Total mismatch: expected ${expected_total:.2f}, invoice says ${invoice['total_amount']:.2f}"
        )

    return errors


def main():
    invoice = load_invoice("sample-invoice-data.json")

    print(f"Validating invoice: {invoice['invoice_number']}")
    print(f"Vendor: {invoice['vendor_name']}")
    print(f"Total: ${invoice['total_amount']:.2f}\n")

    errors = validate_invoice_math(invoice)

    if errors:
        print("ERRORS FOUND:")
        for err in errors:
            print(f"  - {err}")
    else:
        print("Invoice math is correct!")


if __name__ == "__main__":
    main()
