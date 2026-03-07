#!/usr/bin/env python3
"""Read and create invoices in Airtable. Set AIRTABLE_TOKEN and AIRTABLE_BASE_ID in .env or environment."""

import os
import requests

# Load from environment (use .env via python-dotenv if available; never commit real tokens)
AIRTABLE_TOKEN = os.environ.get("AIRTABLE_TOKEN", "YOUR_AIRTABLE_TOKEN")
BASE_ID = os.environ.get("AIRTABLE_BASE_ID", "YOUR_BASE_ID")
TABLE_NAME = "Invoices"


def get_invoices():
    """Fetch all invoices from Airtable."""
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    print(f"Error: {response.status_code}")
    print(response.text)
    return None


def create_invoice(invoice_data):
    """Create a new invoice record in Airtable."""
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {"fields": invoice_data}
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("Invoice created successfully!")
        return response.json()
    print(f"Error creating invoice: {response.status_code}")
    print(response.text)
    return None


def update_invoice(record_id, fields):
    """Update an existing Airtable record by ID. fields is a dict of field names to new values."""
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}/{record_id}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {"fields": fields}
    response = requests.patch(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    print(f"Error updating {record_id}: {response.status_code}")
    print(response.text)
    return None


def main():
    if AIRTABLE_TOKEN == "YOUR_AIRTABLE_TOKEN" or BASE_ID == "YOUR_BASE_ID":
        print("Please edit this script and replace YOUR_AIRTABLE_TOKEN and YOUR_BASE_ID with your real credentials.")
        return

    print("Fetching invoices from Airtable...\n")
    data = get_invoices()

    if data:
        records = data.get("records", [])
        print(f"Found {len(records)} invoice(s):\n")
        for rec in records:
            fields = rec.get("fields", {})
            print(f"Invoice: {fields.get('Invoice Number', 'N/A')}")
            print(f"Vendor: {fields.get('Vendor', 'N/A')}")
            print(f"Amount: ${fields.get('Amount', 0):.2f}")
            print(f"Status: {fields.get('Status', '—')}")
            print("-" * 40)

    # Create a test invoice via API
    print("\nCreating test invoice...")
    new_invoice = {
        "Invoice Number": "INV-2024-9999",
        "Vendor": "Widget Supplies Inc",
        "Invoice Date": "2024-02-04",
        "Due Date": "2024-03-05",
        "Amount": 2500.00,
        "Status": "Received",
        # "Notes": "Created via API - Lesson 1.3",  # Omit if your Notes field has restrictions
    }
    result = create_invoice(new_invoice)
    if result:
        print(f"Created record ID: {result['id']}")


if __name__ == "__main__":
    main()
