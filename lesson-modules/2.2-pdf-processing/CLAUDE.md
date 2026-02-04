# Lesson 2.2 - PDF Invoice Processing Automation

**Module:** Building Real Automations
**Project Type:** Production-Ready Python Script
**Estimated Time:** 3-4 hours
**Complexity:** Intermediate

---

## What You'll Build

A Python script that processes PDF invoices from a local folder and automatically extracts structured data into Airtable.

**The Script:**
- Reads invoice PDFs from `/invoices` folder
- Extracts: invoice #, vendor, date, due date, amount
- Validates extracted data
- Inserts records into Airtable
- Handles errors gracefully
- Logs all operations
- Flags uncertain extractions for review

**Why This Matters:**
This is your first real automation. Not a tutorial example. Not a demo. This is the script Marcus will actually use at Precision Manufacturing to save Elena 2-3 hours of manual data entry every single day.

If you build this right, you'll have proven you can deliver real value as an AI operator.

---

## The Story So Far

You met with Marcus Rodriguez from Finance last week. His team is drowning in manual invoice processing:

**Current Process:**
1. Elena downloads 15-25 invoice PDFs daily
2. Opens each PDF manually
3. Types data into Airtable (5-8 minutes per invoice)
4. 2-3 hours of pure data entry every morning
5. Error-prone (typos, wrong decimals)
6. Doesn't scale as company grows

**What They Need:**
A system that can extract invoice data automatically with 95%+ accuracy, flag uncertain extractions for review, and let Elena focus on validation instead of typing.

**Your Mission:**
Build the proof of concept. Start with local PDF processing. Show Marcus it works. Then expand to full automation.

---

## Learning Objectives

By the end of this lesson, you will:

1. Parse PDF files using Python libraries
2. Extract structured data from unstructured documents
3. Integrate with Airtable API
4. Implement error handling and logging
5. Build confidence scoring for AI extractions
6. Create production-ready automation code

**Meta Skill:**
This lesson teaches you how to bridge the gap between messy real-world data (PDFs) and structured systems (Airtable). This pattern applies to any document processing task.

**Where Else This Applies:**
- Processing receipts for expense reports
- Extracting data from contracts
- Parsing resumes for HR systems
- Reading shipping labels for inventory
- Processing medical forms
- Any scenario where humans currently type from documents

---

## Prerequisites

**Required:**
- Completed Lesson 2.1 (Automation Design & Planning)
- Airtable account set up (from Module 1)
- Python 3.8+ installed
- Basic understanding of APIs

**Materials Provided:**
- 5 sample invoice PDFs (in `/precision-manufacturing/current-data-samples/invoices/`)
- Expected output structure (`expected-output.json`)
- Airtable structure template
- Testing progression guide

---

## Part A: Local PDF Processing

This is the core project. We'll build it step by step.

---

### STOP

Before proceeding:
- [ ] Read the finance department interview at `/precision-manufacturing/department-interviews/finance-invoice-nightmare.md`
- [ ] Review the invoice samples README at `/precision-manufacturing/current-data-samples/invoices/README.md`
- [ ] Check the expected output format at `/precision-manufacturing/current-data-samples/expected-output.json`

This context matters. You're building for Marcus and Elena. Understanding their pain makes you a better builder.

---

### USER: Ready to start building

---

### Step 1: Set Up Your Project Environment

**ACTION:** Create the project structure.

Tell me you're ready, and I'll guide you through setting up the project directory, installing dependencies, and organizing files properly.

**What We'll Create:**
```
invoice-processor/
├── invoice_processor.py       # Main script
├── requirements.txt           # Python dependencies
├── .env.example              # Template for API keys
├── logs/                     # Processing logs
└── processed/                # Processed PDFs (move here after)
```

---

### USER: I'm ready to set up the environment

---

### ACTION: Set up project structure

Run these commands to create your project:

```bash
# Navigate to course directory
cd "/Users/tomcrawshaw/AI OPERATOR OS/Claude-Code-AI-Operator-Course"

# Create project folder
mkdir -p invoice-processor/logs
mkdir -p invoice-processor/processed

# Create main script file
touch invoice-processor/invoice_processor.py

# Create requirements file
cat > invoice-processor/requirements.txt << 'EOF'
pdfplumber==0.10.3
python-dotenv==1.0.0
requests==2.31.0
EOF

# Create environment template
cat > invoice-processor/.env.example << 'EOF'
# Airtable Configuration
AIRTABLE_TOKEN=your_token_here
AIRTABLE_BASE_ID=your_base_id_here
AIRTABLE_TABLE_NAME=Invoices

# OpenRouter Configuration (for AI extraction - optional)
OPENROUTER_API_KEY=your_key_here
EOF
```

**Next:** Install dependencies.

```bash
cd invoice-processor
pip3 install -r requirements.txt
```

**Expected Output:**
```
Successfully installed pdfplumber-0.10.3 python-dotenv-1.0.0 requests-2.31.0
```

If you see errors, troubleshoot:
- Python version too old? (`python3 --version` should be 3.8+)
- Pip not installed? (`pip3 --version`)
- Permission issues? Try `pip3 install --user -r requirements.txt`

---

### STOP

Checkpoint:
- [ ] Project folder created
- [ ] Dependencies installed successfully
- [ ] No errors in terminal

---

### USER: Environment setup complete

---

### Step 2: Choose Your PDF Parsing Library

You have two main options for parsing PDFs in Python:

**Option 1: pdfplumber (Recommended)**
- Easier to use
- Better table extraction
- Good for digital PDFs
- What we'll use in this lesson

**Option 2: PyPDF2**
- Lower-level control
- Faster for simple text extraction
- Can be harder to position text accurately

**Why This Matters:**
PDF extraction is harder than it looks. PDFs store text as positioned characters, not structured data. You need a library that can reconstruct meaning from positions.

For Marcus's use case (mixed invoice formats), pdfplumber gives us the best balance of ease and power.

---

### Step 3: Test PDF Parsing on Simplest Invoice

Let's start with the easiest invoice to build confidence.

**ACTION:** Open your `invoice_processor.py` and let's write code to extract text from invoice-004 (Global Shipping - simplest format).

```python
#!/usr/bin/env python3
"""
Invoice PDF Processor
Extracts invoice data from PDFs and uploads to Airtable
"""

import pdfplumber
import os
import sys
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/processing.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


def extract_text_from_pdf(pdf_path):
    """
    Extract all text from a PDF file

    Args:
        pdf_path: Path to PDF file

    Returns:
        str: Extracted text
    """
    try:
        logger.info(f"Opening PDF: {pdf_path}")
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page_num, page in enumerate(pdf.pages, 1):
                logger.info(f"Extracting text from page {page_num}")
                text += page.extract_text() + "\n"

        logger.info(f"Successfully extracted {len(text)} characters")
        return text

    except Exception as e:
        logger.error(f"Error extracting text from {pdf_path}: {e}")
        return None


def main():
    """Main execution function"""
    logger.info("=== Invoice Processor Starting ===")

    # Test with invoice-004
    test_invoice = "../precision-manufacturing/current-data-samples/invoices/invoice-004-global-shipping.pdf"

    if not os.path.exists(test_invoice):
        logger.error(f"Test invoice not found: {test_invoice}")
        return

    # Extract text
    text = extract_text_from_pdf(test_invoice)

    if text:
        print("\n" + "="*60)
        print("EXTRACTED TEXT:")
        print("="*60)
        print(text)
        print("="*60)
    else:
        logger.error("Failed to extract text")

    logger.info("=== Processing Complete ===")


if __name__ == "__main__":
    main()
```

**ACTION:** Run the script.

```bash
python3 invoice_processor.py
```

**What You Should See:**
- Log messages showing PDF opening
- Extracted text from the invoice
- Invoice number, vendor name, amounts visible in the text

**Troubleshooting:**
- "No module named pdfplumber"? Run `pip3 install pdfplumber`
- "File not found"? Check the path to your invoice PDFs
- "Permission denied"? Check file permissions

---

### STOP

This is a critical moment. You should see the raw text extracted from the PDF.

**Check:**
- [ ] Script runs without errors
- [ ] You can see invoice text in terminal
- [ ] Log file created in `logs/processing.log`

If this works, you've proven PDF extraction is possible. That's huge.

---

### USER: I can see the extracted text!

---

### ACTION: Analyze the output

Look at the extracted text. Notice:
- Text is there, but unstructured
- Invoice number is somewhere in there
- Vendor name is visible
- Dates and amounts are mixed with labels
- No clean key-value pairs

**The Challenge:**
We need to parse this unstructured text into structured data.

**Two Approaches:**

1. **Pattern Matching (Traditional)**
   - Use regex to find "Invoice #:", "Total:", etc.
   - Works for consistent formats
   - Brittle when formats change
   - Fast and free

2. **AI Extraction (Modern)**
   - Send text to Claude/GPT
   - Ask for structured JSON
   - Handles format variations
   - Costs money per call (~$0.01-0.05/invoice)

**For This Lesson:**
We'll start with pattern matching (free, fast, teaches fundamentals). Part B will add AI extraction for edge cases.

---

### Step 4: Build Data Extraction Functions

Now we write functions to extract specific fields from the text.

**ACTION:** Add these extraction functions to your script (above the `main()` function):

```python
import re
from typing import Dict, Optional


def extract_invoice_number(text: str) -> Optional[str]:
    """
    Extract invoice number from text

    Patterns to look for:
    - Invoice #: INV-2024-0342
    - Invoice: GS-2024-1556
    - Invoice No: TP-2024-0891
    """
    patterns = [
        r'Invoice\s*#?\s*:?\s*([A-Z0-9-]+)',
        r'Invoice\s+Number\s*:?\s*([A-Z0-9-]+)',
        r'INV[-\s]?([0-9-]+)',
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            invoice_num = match.group(1).strip()
            logger.info(f"Found invoice number: {invoice_num}")
            return invoice_num

    logger.warning("Could not find invoice number")
    return None


def extract_vendor_name(text: str) -> Optional[str]:
    """
    Extract vendor name from text

    Usually at the top of the invoice
    """
    # Split into lines
    lines = text.split('\n')

    # Vendor name is typically in the first few lines
    # Look for lines with "Corp", "Inc", "LLC", "Ltd", etc.
    company_suffixes = ['Corp', 'Inc', 'LLC', 'Ltd', 'Limited', 'Corporation', 'Company', 'Co\.']

    for i, line in enumerate(lines[:10]):  # Check first 10 lines
        line = line.strip()
        if not line:
            continue

        # Check if line contains company suffix
        for suffix in company_suffixes:
            if re.search(r'\b' + suffix + r'\b', line, re.IGNORECASE):
                vendor = line.strip()
                logger.info(f"Found vendor name: {vendor}")
                return vendor

    # Fallback: Look for "From:" or "Vendor:"
    patterns = [
        r'From\s*:?\s*(.+?)(?:\n|$)',
        r'Vendor\s*:?\s*(.+?)(?:\n|$)',
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            vendor = match.group(1).strip()
            logger.info(f"Found vendor name (fallback): {vendor}")
            return vendor

    logger.warning("Could not find vendor name")
    return None


def extract_date(text: str, date_label: str = "Invoice Date") -> Optional[str]:
    """
    Extract date from text

    Args:
        text: Full invoice text
        date_label: Label to look for (e.g., "Invoice Date", "Due Date")

    Returns:
        Date in YYYY-MM-DD format or None
    """
    # Look for date after label
    pattern = rf'{date_label}\s*:?\s*(\d{{1,2}}[-/]\d{{1,2}}[-/]\d{{4}}|\d{{4}}[-/]\d{{1,2}}[-/]\d{{1,2}})'
    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        date_str = match.group(1)
        # Normalize to YYYY-MM-DD
        date_normalized = normalize_date(date_str)
        logger.info(f"Found {date_label}: {date_normalized}")
        return date_normalized

    logger.warning(f"Could not find {date_label}")
    return None


def normalize_date(date_str: str) -> str:
    """
    Convert various date formats to YYYY-MM-DD

    Handles:
    - 01/15/2024 -> 2024-01-15
    - 2024-01-15 -> 2024-01-15
    - 01-15-2024 -> 2024-01-15
    """
    # Remove extra whitespace
    date_str = date_str.strip()

    # Try different formats
    formats = [
        '%m/%d/%Y',  # 01/15/2024
        '%m-%d-%Y',  # 01-15-2024
        '%Y-%m-%d',  # 2024-01-15 (already normalized)
        '%Y/%m/%d',  # 2024/01/15
    ]

    for fmt in formats:
        try:
            dt = datetime.strptime(date_str, fmt)
            return dt.strftime('%Y-%m-%d')
        except ValueError:
            continue

    # If we get here, couldn't parse
    logger.warning(f"Could not normalize date: {date_str}")
    return date_str


def extract_amount(text: str, amount_label: str = "Total") -> Optional[float]:
    """
    Extract monetary amount from text

    Args:
        text: Full invoice text
        amount_label: Label to look for (e.g., "Total", "Amount Due")

    Returns:
        Float amount or None
    """
    # Look for amount after label
    # Match patterns like: Total: $1,242.00 or Total Amount: 1242.00
    pattern = rf'{amount_label}\s*:?\s*\$?\s*([\d,]+\.\d{{2}})'
    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        amount_str = match.group(1).replace(',', '')  # Remove commas
        try:
            amount = float(amount_str)
            logger.info(f"Found {amount_label}: ${amount:.2f}")
            return amount
        except ValueError:
            logger.warning(f"Could not convert amount to float: {amount_str}")
            return None

    logger.warning(f"Could not find {amount_label}")
    return None


def extract_invoice_data(text: str) -> Dict:
    """
    Extract all invoice fields from text

    Returns:
        Dictionary with invoice data
    """
    logger.info("Extracting invoice data from text")

    data = {
        'invoice_number': extract_invoice_number(text),
        'vendor_name': extract_vendor_name(text),
        'invoice_date': extract_date(text, 'Invoice Date'),
        'due_date': extract_date(text, 'Due Date'),
        'total_amount': extract_amount(text, 'Total'),
        'extracted_at': datetime.now().isoformat(),
    }

    # Calculate confidence score
    data['confidence_score'] = calculate_confidence(data)

    return data


def calculate_confidence(data: Dict) -> float:
    """
    Calculate confidence score based on extracted fields

    Required fields: invoice_number, vendor_name, invoice_date, due_date, total_amount
    Each required field found = 0.20 points

    Returns:
        Float between 0 and 1
    """
    required_fields = ['invoice_number', 'vendor_name', 'invoice_date', 'due_date', 'total_amount']
    fields_found = sum(1 for field in required_fields if data.get(field) is not None)

    confidence = fields_found / len(required_fields)
    logger.info(f"Confidence score: {confidence:.2f} ({fields_found}/{len(required_fields)} fields)")

    return confidence
```

**ACTION:** Update your `main()` function to use these extractors:

```python
def main():
    """Main execution function"""
    logger.info("=== Invoice Processor Starting ===")

    # Test with invoice-004
    test_invoice = "../precision-manufacturing/current-data-samples/invoices/invoice-004-global-shipping.pdf"

    if not os.path.exists(test_invoice):
        logger.error(f"Test invoice not found: {test_invoice}")
        return

    # Extract text
    text = extract_text_from_pdf(test_invoice)

    if not text:
        logger.error("Failed to extract text")
        return

    # Extract structured data
    invoice_data = extract_invoice_data(text)

    # Display results
    print("\n" + "="*60)
    print("EXTRACTED INVOICE DATA:")
    print("="*60)
    for key, value in invoice_data.items():
        print(f"{key:20s}: {value}")
    print("="*60)

    # Check if confidence is high enough
    if invoice_data['confidence_score'] < 0.90:
        logger.warning(f"⚠️  Low confidence score: {invoice_data['confidence_score']:.2f}")
        logger.warning("This invoice should be flagged for manual review")
    else:
        logger.info(f"✓ High confidence score: {invoice_data['confidence_score']:.2f}")

    logger.info("=== Processing Complete ===")
```

**ACTION:** Run the updated script.

```bash
python3 invoice_processor.py
```

**What You Should See:**
- Extracted invoice number
- Vendor name
- Invoice date (normalized to YYYY-MM-DD)
- Due date
- Total amount
- Confidence score (should be 1.0 if all fields found)

---

### STOP

This is a major milestone. You've gone from raw PDF text to structured data.

**Check:**
- [ ] All 5 required fields extracted
- [ ] Dates in YYYY-MM-DD format
- [ ] Amount as float
- [ ] Confidence score calculated

If this works, you're 60% done with the core functionality.

---

### USER: Data extraction is working!

---

### Step 5: Add Data Validation

Before sending data to Airtable, we need to validate it.

**Why Validation Matters:**
- Garbage in = garbage out
- Airtable will reject invalid data types
- Better to catch errors early
- Helps identify extraction issues

**ACTION:** Add validation functions (above `main()`):

```python
def validate_invoice_data(data: Dict) -> tuple[bool, list]:
    """
    Validate extracted invoice data

    Returns:
        (is_valid, errors) tuple
    """
    errors = []

    # Check required fields exist
    required_fields = ['invoice_number', 'vendor_name', 'invoice_date', 'due_date', 'total_amount']
    for field in required_fields:
        if not data.get(field):
            errors.append(f"Missing required field: {field}")

    # Validate dates
    if data.get('invoice_date'):
        if not is_valid_date(data['invoice_date']):
            errors.append(f"Invalid invoice_date format: {data['invoice_date']}")

    if data.get('due_date'):
        if not is_valid_date(data['due_date']):
            errors.append(f"Invalid due_date format: {data['due_date']}")

    # Validate due_date >= invoice_date
    if data.get('invoice_date') and data.get('due_date'):
        try:
            inv_date = datetime.strptime(data['invoice_date'], '%Y-%m-%d')
            due_date = datetime.strptime(data['due_date'], '%Y-%m-%d')
            if due_date < inv_date:
                errors.append(f"Due date ({data['due_date']}) is before invoice date ({data['invoice_date']})")
        except ValueError as e:
            errors.append(f"Date validation error: {e}")

    # Validate amount
    if data.get('total_amount'):
        if not isinstance(data['total_amount'], (int, float)) or data['total_amount'] <= 0:
            errors.append(f"Invalid total_amount: {data['total_amount']}")

    is_valid = len(errors) == 0

    if is_valid:
        logger.info("✓ Data validation passed")
    else:
        logger.error(f"✗ Data validation failed: {len(errors)} errors")
        for error in errors:
            logger.error(f"  - {error}")

    return is_valid, errors


def is_valid_date(date_str: str) -> bool:
    """Check if date string is valid YYYY-MM-DD format"""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False
```

**ACTION:** Update `main()` to validate before proceeding:

```python
def main():
    """Main execution function"""
    logger.info("=== Invoice Processor Starting ===")

    # Test with invoice-004
    test_invoice = "../precision-manufacturing/current-data-samples/invoices/invoice-004-global-shipping.pdf"

    if not os.path.exists(test_invoice):
        logger.error(f"Test invoice not found: {test_invoice}")
        return

    # Extract text
    text = extract_text_from_pdf(test_invoice)
    if not text:
        logger.error("Failed to extract text")
        return

    # Extract structured data
    invoice_data = extract_invoice_data(text)

    # Display results
    print("\n" + "="*60)
    print("EXTRACTED INVOICE DATA:")
    print("="*60)
    for key, value in invoice_data.items():
        print(f"{key:20s}: {value}")
    print("="*60)

    # Validate data
    is_valid, errors = validate_invoice_data(invoice_data)

    if not is_valid:
        print("\n⚠️  VALIDATION ERRORS:")
        for error in errors:
            print(f"  - {error}")
        print("\nThis invoice requires manual review.")
        return

    # Check confidence
    if invoice_data['confidence_score'] < 0.90:
        logger.warning(f"⚠️  Low confidence score: {invoice_data['confidence_score']:.2f}")
        print("\n⚠️  Low confidence - flagged for manual review")
    else:
        logger.info(f"✓ High confidence score: {invoice_data['confidence_score']:.2f}")
        print("\n✓ Ready to send to Airtable")

    logger.info("=== Processing Complete ===")
```

**ACTION:** Run the script again.

```bash
python3 invoice_processor.py
```

**Expected Output:**
- All validation checks should pass
- "Ready to send to Airtable" message

---

### Step 6: Connect to Airtable API

Now we integrate with Airtable to store the extracted data.

**ACTION:** First, set up your Airtable credentials.

Copy the example file:
```bash
cp .env.example .env
```

**ACTION:** Open `.env` and add your credentials:
```
AIRTABLE_TOKEN=your_personal_access_token
AIRTABLE_BASE_ID=your_base_id
AIRTABLE_TABLE_NAME=Invoices
```

**Getting Your Credentials:**

1. **Airtable Token:**
   - Go to https://airtable.com/create/tokens
   - Create new token with `data.records:write` scope
   - Copy the token

2. **Base ID:**
   - Open your Airtable base
   - Go to Help > API documentation
   - Base ID is in the URL: `app...`

3. **Table Name:**
   - The table where invoices will be stored
   - Default: "Invoices"

**ACTION:** Add Airtable integration code to your script:

```python
import os
from dotenv import load_dotenv
import requests
import json

# Load environment variables
load_dotenv()

# Airtable configuration
AIRTABLE_TOKEN = os.getenv('AIRTABLE_TOKEN')
AIRTABLE_BASE_ID = os.getenv('AIRTABLE_BASE_ID')
AIRTABLE_TABLE_NAME = os.getenv('AIRTABLE_TABLE_NAME', 'Invoices')


def create_airtable_record(invoice_data: Dict) -> bool:
    """
    Create a record in Airtable with invoice data

    Args:
        invoice_data: Dictionary with invoice fields

    Returns:
        True if successful, False otherwise
    """
    if not AIRTABLE_TOKEN or not AIRTABLE_BASE_ID:
        logger.error("Airtable credentials not configured")
        return False

    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"

    headers = {
        "Authorization": f"Bearer {AIRTABLE_TOKEN}",
        "Content-Type": "application/json"
    }

    # Map our data to Airtable fields
    fields = {
        "Invoice Number": invoice_data.get('invoice_number'),
        "Vendor": invoice_data.get('vendor_name'),
        "Invoice Date": invoice_data.get('invoice_date'),
        "Due Date": invoice_data.get('due_date'),
        "Amount": invoice_data.get('total_amount'),
        "Status": "Received",
        "Notes": f"Extracted automatically with confidence score: {invoice_data.get('confidence_score', 0):.2f}"
    }

    # Remove None values
    fields = {k: v for k, v in fields.items() if v is not None}

    payload = {"fields": fields}

    try:
        logger.info(f"Sending data to Airtable: {AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}")
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            record_id = response.json().get('id')
            logger.info(f"✓ Record created successfully: {record_id}")
            return True
        else:
            logger.error(f"✗ Airtable API error: {response.status_code}")
            logger.error(f"Response: {response.text}")
            return False

    except Exception as e:
        logger.error(f"Exception creating Airtable record: {e}")
        return False
```

**ACTION:** Update `main()` to send to Airtable:

```python
def main():
    """Main execution function"""
    logger.info("=== Invoice Processor Starting ===")

    # Test with invoice-004
    test_invoice = "../precision-manufacturing/current-data-samples/invoices/invoice-004-global-shipping.pdf"

    if not os.path.exists(test_invoice):
        logger.error(f"Test invoice not found: {test_invoice}")
        return

    # Extract text
    text = extract_text_from_pdf(test_invoice)
    if not text:
        logger.error("Failed to extract text")
        return

    # Extract structured data
    invoice_data = extract_invoice_data(text)

    # Display results
    print("\n" + "="*60)
    print("EXTRACTED INVOICE DATA:")
    print("="*60)
    for key, value in invoice_data.items():
        print(f"{key:20s}: {value}")
    print("="*60)

    # Validate data
    is_valid, errors = validate_invoice_data(invoice_data)

    if not is_valid:
        print("\n⚠️  VALIDATION ERRORS:")
        for error in errors:
            print(f"  - {error}")
        print("\nThis invoice requires manual review.")
        return

    # Check confidence
    if invoice_data['confidence_score'] < 0.90:
        logger.warning(f"⚠️  Low confidence score: {invoice_data['confidence_score']:.2f}")
        print("\n⚠️  Low confidence - flagged for manual review")
        # Still send to Airtable but with flag
    else:
        logger.info(f"✓ High confidence score: {invoice_data['confidence_score']:.2f}")

    # Send to Airtable
    print("\nSending to Airtable...")
    success = create_airtable_record(invoice_data)

    if success:
        print("✓ Invoice successfully processed and saved to Airtable!")
    else:
        print("✗ Failed to save to Airtable. Check logs for details.")

    logger.info("=== Processing Complete ===")
```

**ACTION:** Run the script.

```bash
python3 invoice_processor.py
```

**Expected Output:**
- Data extraction
- Validation pass
- "Sending to Airtable..."
- "Invoice successfully processed and saved to Airtable!"

**ACTION:** Check your Airtable base. You should see a new record with the invoice data.

---

### STOP

Huge milestone. You just built a working end-to-end automation:
PDF → Extract → Validate → Airtable

**Check:**
- [ ] Script completes successfully
- [ ] New record appears in Airtable
- [ ] All fields populated correctly
- [ ] Logs show success

This is real. This works. You're an automation builder now.

---

### USER: It worked! I see the record in Airtable!

---

### Step 7: Process All Invoices

Now we expand from one test invoice to all five.

**ACTION:** Update `main()` to process multiple invoices:

```python
def process_invoice_file(pdf_path: str) -> Dict:
    """
    Process a single invoice PDF file

    Args:
        pdf_path: Path to PDF file

    Returns:
        Dictionary with processing results
    """
    logger.info(f"\n{'='*60}")
    logger.info(f"Processing: {os.path.basename(pdf_path)}")
    logger.info(f"{'='*60}")

    result = {
        'filename': os.path.basename(pdf_path),
        'success': False,
        'data': None,
        'errors': []
    }

    # Extract text
    text = extract_text_from_pdf(pdf_path)
    if not text:
        result['errors'].append("Failed to extract text from PDF")
        return result

    # Extract data
    invoice_data = extract_invoice_data(text)
    result['data'] = invoice_data

    # Validate
    is_valid, validation_errors = validate_invoice_data(invoice_data)
    if not is_valid:
        result['errors'].extend(validation_errors)
        return result

    # Check confidence
    if invoice_data['confidence_score'] < 0.90:
        result['errors'].append(f"Low confidence score: {invoice_data['confidence_score']:.2f}")
        logger.warning("Low confidence - flagging for manual review")

    # Send to Airtable
    airtable_success = create_airtable_record(invoice_data)
    if not airtable_success:
        result['errors'].append("Failed to create Airtable record")
        return result

    result['success'] = True
    return result


def main():
    """Main execution function"""
    logger.info("=== Invoice Processor Starting ===")

    # Path to invoice directory
    invoice_dir = "../precision-manufacturing/current-data-samples/invoices"

    if not os.path.exists(invoice_dir):
        logger.error(f"Invoice directory not found: {invoice_dir}")
        return

    # Get all PDF files
    pdf_files = [
        os.path.join(invoice_dir, f)
        for f in os.listdir(invoice_dir)
        if f.endswith('.pdf')
    ]

    if not pdf_files:
        logger.error(f"No PDF files found in {invoice_dir}")
        return

    logger.info(f"Found {len(pdf_files)} invoice PDFs to process")

    # Process each invoice
    results = []
    for pdf_path in sorted(pdf_files):
        result = process_invoice_file(pdf_path)
        results.append(result)

    # Summary report
    print("\n" + "="*60)
    print("PROCESSING SUMMARY")
    print("="*60)

    successful = sum(1 for r in results if r['success'])
    failed = len(results) - successful

    print(f"Total Invoices: {len(results)}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print()

    # Show details
    for result in results:
        status = "✓" if result['success'] else "✗"
        print(f"{status} {result['filename']}")
        if result['errors']:
            for error in result['errors']:
                print(f"    - {error}")

    print("="*60)
    logger.info("=== Processing Complete ===")


if __name__ == "__main__":
    main()
```

**ACTION:** Run the script to process all invoices.

```bash
python3 invoice_processor.py
```

**What You Should See:**
- Processing each PDF in sequence
- Success/failure for each invoice
- Summary report at the end

**Expected Results:**
- invoice-004: ✓ Success (simplest)
- invoice-001: ✓ Success (clean format)
- invoice-002: ✓ Success (standard format)
- invoice-003: ? (might need regex adjustments)
- invoice-005: ? (complex, multi-page)

If some fail, that's expected. Different invoice formats need different regex patterns.

---

### STOP

Review your results:
- [ ] How many invoices processed successfully?
- [ ] Which ones failed?
- [ ] What were the errors?

This is where automation gets real. One test case is easy. Five different formats? Now you're handling real-world variety.

---

### USER: Some invoices worked, others failed

---

### ACTION: Debug and improve extraction patterns

Look at your logs and the invoices that failed. Common issues:

**Issue 1: Vendor name not found**
- Some invoices put company name in different locations
- Solution: Add more patterns to `extract_vendor_name()`

**Issue 2: Invoice number format varies**
- Different prefixes (INV-, GS-, TP-, etc.)
- Solution: Make regex more flexible

**Issue 3: Date formats vary**
- MM/DD/YYYY vs DD/MM/YYYY vs YYYY-MM-DD
- Solution: Add more date format handlers

**How to Fix:**

1. Open the failing PDF manually
2. Look at where the data appears
3. Update your regex patterns to match
4. Re-run the script

**Example Fix for Vendor Names:**

```python
def extract_vendor_name(text: str) -> Optional[str]:
    """Extract vendor name - improved version"""
    lines = text.split('\n')

    # Strategy 1: Look for company suffixes
    company_suffixes = [
        'Corp', 'Corporation', 'Inc', 'Incorporated',
        'LLC', 'Ltd', 'Limited', 'Company', 'Co\.',
        'Solutions', 'Services', 'Supplies', 'Direct',
        'Industries', 'Group', 'Partners'
    ]

    for i, line in enumerate(lines[:15]):  # Check first 15 lines
        line = line.strip()
        if len(line) < 3 or len(line) > 60:  # Skip too short/long
            continue

        for suffix in company_suffixes:
            if re.search(r'\b' + suffix + r'\b', line, re.IGNORECASE):
                # Check if it's not a label/header
                if ':' not in line and line.upper() != line:
                    vendor = line.strip()
                    logger.info(f"Found vendor name: {vendor}")
                    return vendor

    # Strategy 2: First non-empty line that's not "INVOICE"
    for line in lines[:10]:
        line = line.strip()
        if line and line.upper() != 'INVOICE' and len(line) > 5:
            logger.info(f"Found vendor name (first line): {line}")
            return line

    logger.warning("Could not find vendor name")
    return None
```

Work through each failing invoice systematically. This is the messy part of automation, but it's where you learn the most.

---

### Step 8: Add Error Handling and Logging

Make the script more robust.

**ACTION:** Add try-catch blocks and better error reporting:

```python
def process_invoice_file(pdf_path: str) -> Dict:
    """
    Process a single invoice PDF file with comprehensive error handling
    """
    logger.info(f"\n{'='*60}")
    logger.info(f"Processing: {os.path.basename(pdf_path)}")
    logger.info(f"{'='*60}")

    result = {
        'filename': os.path.basename(pdf_path),
        'filepath': pdf_path,
        'success': False,
        'data': None,
        'errors': [],
        'warnings': [],
        'processed_at': datetime.now().isoformat()
    }

    try:
        # Extract text
        text = extract_text_from_pdf(pdf_path)
        if not text:
            result['errors'].append("Failed to extract text from PDF")
            return result

        # Extract data
        invoice_data = extract_invoice_data(text)
        invoice_data['source_file'] = os.path.basename(pdf_path)
        result['data'] = invoice_data

        # Validate
        is_valid, validation_errors = validate_invoice_data(invoice_data)
        if not is_valid:
            result['errors'].extend(validation_errors)
            logger.error("Validation failed - invoice flagged for manual review")
            return result

        # Check confidence
        if invoice_data['confidence_score'] < 0.90:
            warning = f"Low confidence score: {invoice_data['confidence_score']:.2f}"
            result['warnings'].append(warning)
            logger.warning(warning)

        # Send to Airtable
        airtable_success = create_airtable_record(invoice_data)
        if not airtable_success:
            result['errors'].append("Failed to create Airtable record")
            return result

        result['success'] = True
        logger.info("✓ Invoice processed successfully")

    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        result['errors'].append(error_msg)
        logger.exception(error_msg)

    return result
```

**ACTION:** Add a function to save results to JSON:

```python
def save_results_to_json(results: list, output_path: str = "logs/processing_results.json"):
    """Save processing results to JSON file"""
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        output_data = {
            'processed_at': datetime.now().isoformat(),
            'total_invoices': len(results),
            'successful': sum(1 for r in results if r['success']),
            'failed': sum(1 for r in results if not r['success']),
            'results': results
        }

        with open(output_path, 'w') as f:
            json.dump(output_data, f, indent=2)

        logger.info(f"Results saved to {output_path}")
        return True

    except Exception as e:
        logger.error(f"Failed to save results: {e}")
        return False
```

**ACTION:** Update `main()` to save results:

```python
def main():
    """Main execution function"""
    logger.info("=== Invoice Processor Starting ===")

    # ... (previous code for finding PDFs)

    # Process each invoice
    results = []
    for pdf_path in sorted(pdf_files):
        result = process_invoice_file(pdf_path)
        results.append(result)

    # Save results to JSON
    save_results_to_json(results)

    # Summary report (previous code)
    # ...
```

---

### Step 9: Test with All Invoices

Run the complete script on all five invoices.

**ACTION:** Execute the script:

```bash
python3 invoice_processor.py
```

**Review:**
1. Check the terminal output
2. Review `logs/processing.log`
3. Open `logs/processing_results.json`
4. Verify records in Airtable

**Success Criteria:**
- At least 3/5 invoices process successfully
- Failed invoices have clear error messages
- All successful records appear in Airtable
- Logs are comprehensive

---

### STOP

Take a moment. You've built something real:
- Extracts data from PDFs
- Validates the data
- Saves to Airtable
- Handles errors gracefully
- Logs everything
- Processes multiple files

This is production-ready code. With some regex tuning, Marcus could use this today.

---

### USER: The script is working! What's next?

---

## Part B: Advanced Features (Optional)

These features take your automation from good to great.

---

### Advanced Feature 1: Confidence Scoring Improvements

Right now, confidence is a simple count. Let's make it smarter.

**ACTION:** Enhance confidence calculation:

```python
def calculate_confidence(data: Dict, text: str = None) -> float:
    """
    Enhanced confidence scoring

    Factors:
    - Required fields present (base score)
    - Data format quality (bonus points)
    - Text extraction quality (penalty for issues)
    """
    score = 0.0

    # Base score: required fields (60% of total)
    required_fields = ['invoice_number', 'vendor_name', 'invoice_date', 'due_date', 'total_amount']
    fields_found = sum(1 for field in required_fields if data.get(field) is not None)
    score += (fields_found / len(required_fields)) * 0.6

    # Format quality bonuses (40% of total)

    # Invoice number format looks valid?
    if data.get('invoice_number'):
        inv_num = data['invoice_number']
        if re.match(r'^[A-Z]{2,4}[-\s]?\d{4,}', inv_num):
            score += 0.10  # Good format

    # Dates are valid format?
    if data.get('invoice_date') and is_valid_date(data['invoice_date']):
        score += 0.10

    # Due date after invoice date?
    if data.get('invoice_date') and data.get('due_date'):
        try:
            inv = datetime.strptime(data['invoice_date'], '%Y-%m-%d')
            due = datetime.strptime(data['due_date'], '%Y-%m-%d')
            if due >= inv:
                score += 0.10
        except:
            pass

    # Amount seems reasonable? (not 0, not absurdly high)
    if data.get('total_amount'):
        amt = data['total_amount']
        if 10 <= amt <= 100000:
            score += 0.10

    # Cap at 1.0
    score = min(score, 1.0)

    logger.info(f"Enhanced confidence score: {score:.2f}")
    return score
```

---

### Advanced Feature 2: Handle Edge Cases

Add special handling for common problems.

**ACTION:** Add edge case handlers:

```python
def handle_scanned_pdf(pdf_path: str) -> Optional[str]:
    """
    Detect and handle scanned (image-based) PDFs

    These need OCR, which is beyond this lesson,
    but we can at least detect them and flag for manual processing
    """
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()

        # If very little text extracted, likely scanned
        if not text or len(text.strip()) < 50:
            logger.warning("PDF appears to be scanned image - OCR required")
            return None

    return text


def handle_multipage_invoice(pdf_path: str) -> str:
    """
    Handle invoices that span multiple pages

    Extract text from all pages, but be smart about what to use
    """
    with pdfplumber.open(pdf_path) as pdf:
        if len(pdf.pages) == 1:
            # Simple case
            return pdf.pages[0].extract_text()

        logger.info(f"Multi-page PDF: {len(pdf.pages)} pages")

        # First page usually has header info
        first_page_text = pdf.pages[0].extract_text()

        # Subsequent pages might have line items
        # For now, just extract from first page for header data
        # (line items are optional in our schema)

        return first_page_text
```

---

### Advanced Feature 3: Schedule with Cron (macOS/Linux)

Automate the script to run daily.

**ACTION:** Create a wrapper script `run_invoice_processor.sh`:

```bash
#!/bin/bash

# Invoice Processor - Automated Runner
# This script runs the invoice processor and sends notifications

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "=== Invoice Processor Automated Run ==="
echo "Started at: $(date)"

# Run the processor
python3 invoice_processor.py

# Check exit code
if [ $? -eq 0 ]; then
    echo "✓ Processing completed successfully"
else
    echo "✗ Processing failed"
fi

echo "Finished at: $(date)"
```

**ACTION:** Make it executable:

```bash
chmod +x run_invoice_processor.sh
```

**ACTION:** Test the wrapper:

```bash
./run_invoice_processor.sh
```

**ACTION:** Set up cron job (runs daily at 9 AM):

```bash
# Open crontab editor
crontab -e

# Add this line:
0 9 * * * /Users/tomcrawshaw/AI\ OPERATOR\ OS/Claude-Code-AI-Operator-Course/invoice-processor/run_invoice_processor.sh >> /Users/tomcrawshaw/AI\ OPERATOR\ OS/Claude-Code-AI-Operator-Course/invoice-processor/logs/cron.log 2>&1
```

**Save and exit.** The script now runs automatically every morning at 9 AM.

---

### Advanced Feature 4: Email Notifications on Errors

Alert the team when processing fails.

**ACTION:** Add email notification function (requires SMTP setup):

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_error_notification(results: list):
    """
    Send email notification if processing had errors

    Note: Requires SMTP configuration in .env
    """
    failed_invoices = [r for r in results if not r['success']]

    if not failed_invoices:
        return  # No errors, no email

    # Email config from environment
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT', '587'))
    smtp_user = os.getenv('SMTP_USER')
    smtp_pass = os.getenv('SMTP_PASS')
    notify_email = os.getenv('NOTIFY_EMAIL')

    if not all([smtp_server, smtp_user, smtp_pass, notify_email]):
        logger.warning("Email notification not configured")
        return

    # Build email
    subject = f"Invoice Processing Errors - {len(failed_invoices)} Failed"
    body = f"""
    Invoice processing completed with errors.

    Failed Invoices: {len(failed_invoices)}
    Total Processed: {len(results)}

    Failed Files:
    """

    for invoice in failed_invoices:
        body += f"\n- {invoice['filename']}"
        for error in invoice['errors']:
            body += f"\n    {error}"

    body += "\n\nPlease review these invoices manually."

    # Send email
    try:
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = notify_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)

        logger.info(f"Error notification sent to {notify_email}")

    except Exception as e:
        logger.error(f"Failed to send email notification: {e}")
```

---

## What You've Accomplished

Let's take inventory. You've built:

**Core Functionality:**
- PDF text extraction
- Pattern-based data extraction
- Date normalization
- Amount parsing
- Data validation
- Airtable integration
- Batch processing
- Error handling
- Comprehensive logging

**Advanced Features (if completed):**
- Enhanced confidence scoring
- Edge case handling
- Scheduled automation (cron)
- Email notifications

**The Impact:**
Marcus's finance team can now:
- Process 20+ invoices in minutes (not hours)
- Reduce data entry errors
- Scale as the company grows
- Focus on approval/analysis instead of typing

**Your Value as an AI Operator:**
- Identified a high-impact opportunity
- Built a working solution
- Handled real-world complexity
- Delivered measurable ROI

This is the kind of work that makes AI operators invaluable.

---

## Testing & Iteration

**ACTION:** Run the final complete test:

```bash
# Delete test records from Airtable first
# Then run full processing

python3 invoice_processor.py
```

**Verify:**
1. All invoices process (or fail gracefully)
2. Successful records appear in Airtable
3. Failed invoices flagged with clear errors
4. Logs are detailed and useful
5. Results JSON is generated

---

## Handoff to Marcus

When you show this to Marcus, demonstrate:

1. **The Problem** (show Elena manually entering data)
2. **Your Solution** (run the script)
3. **The Results** (show Airtable records)
4. **The Accuracy** (confidence scores, validation)
5. **The Maintenance** (logs, error handling)

**What to Say:**

> "Marcus, I've built an automated invoice processor. It reads PDF invoices, extracts the data, validates it, and sends it directly to your Airtable.
>
> I tested it on 5 different invoice formats. It successfully processed [X] out of 5, with the others flagged for manual review due to [reasons].
>
> The system includes confidence scoring - if it's not sure about something, it flags it. You get accuracy without risk.
>
> Elena's morning routine goes from 2-3 hours of typing to 15 minutes of reviewing. The script can run automatically every morning.
>
> Want to see it in action?"

---

## Key Takeaways

**Technical Lessons:**
- PDF extraction is harder than it looks (unstructured data)
- Regex patterns need iteration for real-world variety
- Validation prevents downstream problems
- Logging is essential for production automation
- Confidence scoring manages uncertainty

**AI Operator Lessons:**
- Start with one test case, expand gradually
- Real data is messy - plan for edge cases
- Show working demos > perfect solutions
- Error handling is half the work
- Documentation makes handoff possible

**Meta Skills:**
- Document → Structured Data transformation
- API integration patterns
- Error handling strategies
- Production readiness thinking

---

## Where to Go Next

**Immediate Next Steps:**
- Lesson 2.3: Google Drive Automation (auto-process when invoices arrive)
- Lesson 2.4: Web App (give finance team an upload interface)

**Ways to Expand This Project:**
- Add OCR for scanned PDFs (using Google Vision API)
- Extract line items (more complex parsing)
- Vendor lookup/matching (link to existing vendor records)
- Approval workflow (route to managers)
- Payment scheduling (integrate with payment system)

---

## Troubleshooting Guide

**Problem: "No module named pdfplumber"**
- Solution: `pip3 install pdfplumber`

**Problem: "Airtable API error 401"**
- Solution: Check your token is correct and has write permissions

**Problem: "Airtable API error 422"**
- Solution: Field names don't match. Check Airtable table schema.

**Problem: "Cannot find invoice number"**
- Solution: Open the PDF, find where invoice # appears, update regex

**Problem: "Date parsing fails"**
- Solution: Add the date format to `normalize_date()` function

**Problem: "Script runs but no records in Airtable"**
- Solution: Check logs for API errors. Verify base ID and table name.

---

## Final ACTION

**Before you consider this lesson complete:**

1. Run the script successfully on at least 3 invoices
2. Verify records appear in Airtable
3. Review the logs
4. Read through your code and understand what each function does
5. Think about how you'd explain this to Marcus

**Then:**

Document your learnings. What was hardest? What surprised you? What would you do differently next time?

These reflections make you a better builder.

---

## Lesson Complete

You've built your first production automation. Not a tutorial. Not a demo. Real code that solves a real problem.

Marcus's finance team will save 10+ hours per week. Elena won't burn out. The company can scale.

And you proved you can deliver.

That's the AI operator advantage.

---

**Ready for Lesson 2.3?** We'll take this local script and make it cloud-native with Google Drive monitoring.

---

**Last Updated:** February 4, 2026
**Estimated Completion Time:** 3-4 hours
**Difficulty:** Intermediate
**Prerequisites:** Module 1 complete, Python basics, Airtable account
