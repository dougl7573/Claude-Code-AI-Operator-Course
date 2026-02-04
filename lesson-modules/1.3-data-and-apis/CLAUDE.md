# Lesson 1.3: Working with Data & APIs

**Welcome back to Precision Manufacturing Co.**

---

## Where We Left Off

In Lesson 1.2, you investigated Marcus's invoice processing nightmare. You identified that Finance is:
- Processing 20+ PDF invoices manually every day
- Copying data into Excel spreadsheets
- Spending 2-3 hours daily on pure data entry
- Making errors that cause payment delays

You mapped out the automation opportunity. Now it's time to build the technical foundation you'll need.

**But here's the thing:** Before you can automate invoice processing, you need to understand how to work with data and connect to external systems (APIs).

This lesson is about those fundamentals:
- Reading and writing CSV files
- Parsing JSON data
- Connecting to Airtable (your database)
- Making API calls
- Transforming data between formats

**By the end of this lesson, you'll:**
- Parse vendor data from CSV files
- Connect to a real Airtable base
- Read and write data via API
- Transform invoice data structures
- Understand how to read API documentation with Claude's help

Let's get started.

---

## The Data Problem

Marcus just forwarded you an email with three attachments:

1. **vendor-list.csv** - Spreadsheet of approved vendors
2. **sample-invoice-data.json** - Example of how they want invoice data structured
3. **airtable-access.txt** - Login info for their Airtable workspace

The email says:

> "Hey, got you access to our Airtable. Also attached our vendor list (we use this to check if invoices are from approved vendors) and a JSON file that shows how we want invoice data structured. Not sure if this helps but thought you'd want to see it. Let me know if you need anything else!"

**Translation:** Marcus doesn't know what you need, but he's trying to be helpful. This is common when working with business teams. They give you data in whatever format they have, and your job is to make sense of it.

Let's start with the vendor list.

---

## Part 1: Working with CSV Files

CSV (Comma-Separated Values) files are everywhere in business. Excel exports to CSV. Accounting systems export to CSV. People email you CSVs constantly.

**Your first task:** Parse the vendor-list.csv file.

---

STOP: Let's create a sample vendor CSV file first.

**Tell me:**
1. Do you know what a CSV file is? (Just answer yes/no - if no, I'll explain)
2. Have you ever opened a CSV in Excel or Google Sheets?

---

USER: [Student responds about CSV knowledge]

---

ACTION: When student responds:

**IF they know CSV:**
- "Great. You know the format - rows and columns, comma-separated. Let's create a sample file and parse it."

**IF they don't know CSV:**
- "No problem. CSV is just a simple text file where each line is a row, and columns are separated by commas. It looks like this:"
```
Name,Email,Department
John,john@company.com,Sales
Sarah,sarah@company.com,Finance
```
- "Open it in Excel and it becomes a nice table. Open it in a text editor and it's just commas."
- "CSVs are the universal data exchange format. Every system can export/import them."

**Then:** "Let's create the vendor-list.csv file that Marcus sent you. I'll guide you through it."

---

### Exercise 1.3.1: Create Sample Vendor CSV

Let's create the vendor-list.csv file that Precision Manufacturing uses to track approved vendors.

**Task:** Create a file called `vendor-list.csv` in your course folder with this content:

```csv
vendor_id,vendor_name,contact_email,payment_terms,category,active
V001,Acme Corp,billing@acmecorp.com,Net 30,Raw Materials,TRUE
V002,Widget Supplies Inc,accounts@widgetsupplies.com,Net 30,Components,TRUE
V003,Tech Parts Direct,invoices@techpartsdirect.com,Net 15,Electronics,TRUE
V004,Global Shipping Co,payments@globalship.com,Due on Receipt,Logistics,TRUE
V005,Office Depot Business,business@officedepot.com,Net 30,Office Supplies,TRUE
V006,Industrial Tools LLC,billing@indtools.com,Net 45,Equipment,TRUE
V007,Quality Metals Inc,ar@qualitymetals.com,Net 30,Raw Materials,FALSE
V008,Precision Bearings Co,invoices@precisionbearings.com,Net 30,Components,TRUE
```

**How to do this:**
1. Create a new file in your course folder
2. Name it exactly: `vendor-list.csv`
3. Copy the content above (including the header row)
4. Save it

**What this data represents:**
- `vendor_id`: Unique identifier for each vendor
- `vendor_name`: Company name (needs to match invoice exactly)
- `contact_email`: Where to send payment questions
- `payment_terms`: When payment is due
- `category`: Type of supplies they provide
- `active`: Whether they're still an approved vendor (V007 is deactivated)

---

STOP: Create the file, then tell me when you're done.

If you need help creating the file, ask me and I'll walk you through it step by step.

---

USER: [Student creates vendor-list.csv]

---

ACTION: When student confirms file creation:

1. **Verify they created it:**
   - "Great! Let me ask you - if you open that CSV in a text editor, do you see commas separating the values?"
   - "If you open it in Excel/Google Sheets, does it look like a nice table?"

2. **Explain significance:**
   - "This file represents Precision Manufacturing's approved vendor list. In the real world, this might come from their accounting system, or it might just be a spreadsheet Marcus maintains."
   - "Your automation will need to check incoming invoices against this list to make sure they're from approved vendors."

3. **Transition:** "Now let's write code to read this CSV file. Don't worry - Claude Code will do the heavy lifting. Your job is to understand what's happening."

---

### Exercise 1.3.2: Parse the CSV File

Now let's read this CSV file programmatically. You'll use Python (Claude Code will write it for you).

**Task:** Create a Python script that reads the vendor CSV and prints out all active vendors.

---

STOP: Before I show you the code, try this:

**Tell me in plain English:**
- What should the script do, step by step?
- What would be the output you'd want to see?

Think about it like giving instructions to a junior employee. What are the steps?

---

USER: [Student describes the logic]

---

ACTION: When student responds:

1. **Validate their thinking:**
   - Good steps to look for: "Open the file, read each row, check if active is TRUE, print the vendor name"
   - If they miss the header row: "Don't forget - the first row is column names, not data!"
   - If they got it right: "Exactly! Now let's turn that into code."

2. **Show the code:**

"Here's the Python script. Create a file called `parse_vendors.py`:"

```python
import csv

def read_vendor_list(csv_file_path):
    """Read vendor CSV and return list of active vendors."""
    active_vendors = []

    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Check if vendor is active
            if row['active'] == 'TRUE':
                vendor_info = {
                    'id': row['vendor_id'],
                    'name': row['vendor_name'],
                    'email': row['contact_email'],
                    'terms': row['payment_terms'],
                    'category': row['category']
                }
                active_vendors.append(vendor_info)

    return active_vendors

def main():
    # Read the vendor list
    vendors = read_vendor_list('vendor-list.csv')

    # Print results
    print(f"Found {len(vendors)} active vendors:\n")

    for vendor in vendors:
        print(f"ID: {vendor['id']}")
        print(f"Name: {vendor['name']}")
        print(f"Category: {vendor['category']}")
        print(f"Payment Terms: {vendor['terms']}")
        print("-" * 40)

if __name__ == "__main__":
    main()
```

**What this code does:**
- `csv.DictReader` reads the CSV and treats each row as a dictionary (key = column name)
- We loop through each row and check if `active == 'TRUE'`
- We build a cleaner dictionary with just the info we need
- We print it in a readable format

3. **Have them run it:**
   - "Save this as `parse_vendors.py` in the same folder as your CSV."
   - "Run it with: `python3 parse_vendors.py`"
   - "You should see 7 active vendors listed (V007 Quality Metals is inactive)."

---

### Exercise 1.3.3: Search for a Specific Vendor

Now let's make it interactive. Add a function that searches for a vendor by name.

**Task:** Modify the script to let you search for a vendor.

---

STOP: Here's a challenge for you.

**Tell me:** If you wanted to search for "Acme Corp" in the vendor list, how would you modify the code above? Don't write the full code - just describe the logic.

Think about:
- Where would you add the search functionality?
- How would you compare the search term to vendor names?
- What if someone types "acme corp" in lowercase?

---

USER: [Student describes search logic]

---

ACTION: When student responds:

1. **Validate approach:**
   - Good answers mention: looping through vendors, comparing names (case-insensitive), returning match
   - If they mention `.lower()` for case-insensitive search - great!
   - If not: "Good thinking, but what if someone searches for 'acme' instead of 'Acme Corp'? How do we handle case?"

2. **Provide solution:**

"Here's the updated code with a search function. Add this to your `parse_vendors.py`:"

```python
def search_vendor(vendor_name, csv_file_path):
    """Search for a vendor by name (case-insensitive)."""
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if vendor_name.lower() in row['vendor_name'].lower():
                return {
                    'id': row['vendor_id'],
                    'name': row['vendor_name'],
                    'email': row['contact_email'],
                    'terms': row['payment_terms'],
                    'category': row['category'],
                    'active': row['active']
                }

    return None

# Update main() to test search
def main():
    # Test search functionality
    search_term = "Acme"
    result = search_vendor(search_term, 'vendor-list.csv')

    if result:
        print(f"Found vendor matching '{search_term}':\n")
        print(f"Name: {result['name']}")
        print(f"ID: {result['id']}")
        print(f"Active: {result['active']}")
    else:
        print(f"No vendor found matching '{search_term}'")
```

3. **Have them test:**
   - "Run it again. Try changing `search_term` to different values: 'Widget', 'xyz', 'Quality Metals'"
   - "Notice: 'Quality Metals' shows up even though it's inactive. This is important - you might want to flag invoices from inactive vendors!"

---

**Key Skill Unlocked: CSV Parsing**

You now know how to:
- Read CSV files in Python
- Convert rows to dictionaries for easier handling
- Filter data based on conditions
- Search through records

**This applies to:**
- Vendor lists (you just did this)
- Transaction exports from banks
- Customer lists from CRM systems
- Inventory data from warehouse systems
- Any spreadsheet someone emails you

CSV is the universal business data format. Master it.

---

## Part 2: Working with JSON Data

JSON (JavaScript Object Notation) is how APIs talk to each other. It's also how modern systems store structured data.

Marcus sent you `sample-invoice-data.json` - this shows the structure Finance wants for invoice data.

Let's look at it.

---

### Exercise 1.3.4: Understanding JSON Structure

**Task:** Create the sample invoice JSON file.

Create a file called `sample-invoice-data.json` with this content:

```json
{
  "invoice_number": "INV-2024-0342",
  "vendor_name": "Acme Corp",
  "invoice_date": "2024-01-15",
  "due_date": "2024-02-14",
  "subtotal": 1150.00,
  "tax": 92.00,
  "total_amount": 1242.00,
  "line_items": [
    {
      "description": "Steel rods - Grade 304",
      "quantity": 50,
      "unit_price": 18.00,
      "total": 900.00
    },
    {
      "description": "Shipping & Handling",
      "quantity": 1,
      "unit_price": 250.00,
      "total": 250.00
    }
  ],
  "notes": "Payment terms: Net 30"
}
```

**What you're looking at:**
- `{}` = An object (like a dictionary in Python)
- `[]` = An array (like a list in Python)
- `"key": "value"` = Key-value pairs
- Numbers don't have quotes, strings do
- `line_items` is an array of objects (nested structure)

This is more complex than CSV. JSON can represent nested, hierarchical data.

---

STOP: Create the JSON file, then answer:

1. How many line items does this invoice have?
2. What's the difference between `subtotal` and `total_amount`?
3. Why do you think `line_items` is an array instead of just a single value?

---

USER: [Student creates file and answers questions]

---

ACTION: When student responds:

1. **Validate answers:**
   - 2 line items (steel rods + shipping)
   - Difference is tax ($1150 + $92 = $1242)
   - Array because invoices usually have multiple line items

2. **Explain significance:**
   - "This JSON structure is what you'll create when you parse invoice PDFs."
   - "You'll extract data from PDFs and convert it into this format."
   - "Then you'll send this JSON to Airtable via their API."

3. **Transition:** "Let's write code to read and manipulate this JSON."

---

### Exercise 1.3.5: Parse and Transform JSON

**Task:** Create a script that reads the invoice JSON and calculates if the math is correct.

Why? Because sometimes invoice totals don't add up correctly. Your automation should flag those.

---

STOP: Before I show you code, think about this:

**What would you need to check to verify the invoice math is correct?**

Hint: Think about line items, subtotal, tax, and total.

---

USER: [Student describes validation logic]

---

ACTION: When student responds:

1. **Validate thinking:**
   - Good answer: "Sum all line item totals, check if it equals subtotal, then add tax and check if it equals total_amount"
   - If they got it: "Exactly right!"
   - If partial: "Close! Don't forget to also check that line_item total = quantity × unit_price"

2. **Provide code:**

"Create a file called `validate_invoice.py`:"

```python
import json

def load_invoice(json_file_path):
    """Load invoice data from JSON file."""
    with open(json_file_path, 'r') as file:
        return json.load(file)

def validate_invoice_math(invoice):
    """Check if invoice math is correct."""
    errors = []

    # Check line items
    calculated_subtotal = 0
    for i, item in enumerate(invoice['line_items']):
        expected_total = item['quantity'] * item['unit_price']
        if abs(expected_total - item['total']) > 0.01:  # Allow for rounding
            errors.append(f"Line item {i+1}: {item['description']} - Math error!")
        calculated_subtotal += item['total']

    # Check subtotal
    if abs(calculated_subtotal - invoice['subtotal']) > 0.01:
        errors.append(f"Subtotal mismatch: Items sum to ${calculated_subtotal:.2f}, invoice says ${invoice['subtotal']:.2f}")

    # Check total
    expected_total = invoice['subtotal'] + invoice['tax']
    if abs(expected_total - invoice['total_amount']) > 0.01:
        errors.append(f"Total mismatch: Expected ${expected_total:.2f}, invoice says ${invoice['total_amount']:.2f}")

    return errors

def main():
    # Load the invoice
    invoice = load_invoice('sample-invoice-data.json')

    print(f"Validating invoice: {invoice['invoice_number']}")
    print(f"Vendor: {invoice['vendor_name']}")
    print(f"Total: ${invoice['total_amount']:.2f}\n")

    # Validate math
    errors = validate_invoice_math(invoice)

    if errors:
        print("ERRORS FOUND:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("Invoice math is correct!")

if __name__ == "__main__":
    main()
```

3. **Have them test:**
   - "Run this with `python3 validate_invoice.py`"
   - "It should say the math is correct."
   - "Now try changing the `total_amount` to 1300.00 and run it again. See the error?"

4. **Challenge:**
   - "This is real validation logic you'll use in your invoice automation."
   - "Finance will love that you flag bad invoices automatically."

---

**Key Skill Unlocked: JSON Handling**

You now know how to:
- Read JSON files
- Navigate nested structures (objects in arrays)
- Perform calculations on JSON data
- Validate data integrity

**This applies to:**
- API responses (everything is JSON)
- Configuration files
- Data exchange between systems
- Storing complex, structured data

---

## Part 3: Connecting to Airtable API

Now for the real power move: connecting to an external API.

**Airtable** is your database. It's like Excel on steroids, with an API that lets you read/write data programmatically.

**What you'll do:**
1. Set up a free Airtable account
2. Create a test "base" (database)
3. Get your API credentials
4. Write code to read/write data

This is where automation gets real.

---

### Exercise 1.3.6: Set Up Airtable (Step by Step)

**Task:** Create a free Airtable account and set up a test base for invoice tracking.

**Step-by-step walkthrough:**

1. **Create account:**
   - Go to https://airtable.com
   - Sign up for free (you won't need a credit card)
   - Confirm your email

2. **Create a workspace:**
   - After login, you'll see "Create a workspace"
   - Name it: "Precision Manufacturing Test"
   - This is your container for databases

3. **Create a base:**
   - Click "Create" → "Start from scratch"
   - Name it: "Invoice Tracker"
   - This is your actual database

4. **Set up the Invoices table:**
   - Airtable creates a default table - rename it to "Invoices"
   - Create these fields (columns):
     - `Invoice Number` (Single line text)
     - `Vendor` (Single line text)
     - `Invoice Date` (Date)
     - `Due Date` (Date)
     - `Amount` (Currency)
     - `Status` (Single select: Received, Approved, Paid)
     - `Notes` (Long text)

5. **Add sample data:**
   - Add 2-3 test invoices manually (use data from your JSON file)
   - This helps you verify the API is working later

---

STOP: Follow those steps now. This will take 10-15 minutes if it's your first time.

**When done, tell me:**
1. Did you successfully create the base?
2. How many test invoices did you add?
3. Do you see the Invoices table with all the fields?

If you get stuck at any step, describe where you're stuck and I'll help.

---

USER: [Student sets up Airtable]

---

ACTION: When student confirms setup:

1. **Celebrate:**
   - "Excellent! You now have a cloud database. This is where your automation will store invoice data."
   - "Right now you're adding records manually. Soon you'll do it via code."

2. **Get API credentials:**
   - "Now we need your API key so code can access this base. Follow these steps carefully..."

**Get API Token:**
```
1. Click your profile icon (top right)
2. Go to "Developer hub"
3. Click "Create token"
4. Name it: "Invoice Automation"
5. Add scopes:
   - data.records:read
   - data.records:write
   - schema.bases:read
6. Add access to your "Invoice Tracker" base
7. Click "Create token"
8. COPY THE TOKEN - you won't see it again!
```

**Get Base ID:**
```
1. Go to https://airtable.com/api
2. Click on "Invoice Tracker"
3. Look for "The ID of this base is appXXXXXXXXXXXXXX"
4. Copy that ID
```

3. **Store credentials safely:**
   - "Create a file called `airtable-credentials.txt` (do NOT commit this to git later!)"
   - "Save your token and base ID there for reference"
   - "You'll use these in code in a moment"

4. **Security note:**
   - "NEVER share your API token publicly or commit it to GitHub"
   - "Treat it like a password - it gives full access to your Airtable data"

---

### Exercise 1.3.7: Make Your First API Call

Now let's read data from Airtable via the API.

**Task:** Write a script that connects to your Airtable base and prints all invoices.

---

STOP: Before I give you code, let me explain how APIs work.

**API Basics:**

An API (Application Programming Interface) is like a waiter at a restaurant:
- You (your code) make a request: "I'd like the invoice data, please"
- The API goes to the kitchen (Airtable's servers)
- It brings back your data

**HTTP Requests:**
- GET = Read data
- POST = Create data
- PATCH = Update data
- DELETE = Delete data

**Authentication:**
- Your API token proves you're allowed to access the data
- It goes in the request header (like showing your ID)

**Make sense?**

Just respond "yes" or "kind of" or "wait what?" and I'll adjust the explanation.

---

USER: [Student responds to API explanation]

---

ACTION: Based on understanding:

**IF they get it:**
- "Great! Let's write code to make a GET request to Airtable."

**IF confused:**
- Give restaurant analogy with more detail:
  - "Think of it like calling a restaurant to place a takeout order"
  - "GET = asking what's on the menu"
  - "POST = placing an order"
  - "Your API token = your phone number so they know it's you"
- Then: "Don't worry if it's still fuzzy. It'll click when you see it work."

**Then provide code:**

"Create a file called `airtable_test.py`:"

```python
import requests
import json

# YOUR CREDENTIALS (replace with your actual values)
AIRTABLE_TOKEN = "patXXXXXXXXXXXXXX"  # Your token from earlier
BASE_ID = "appXXXXXXXXXXXXXX"  # Your base ID
TABLE_NAME = "Invoices"

def get_invoices():
    """Fetch all invoices from Airtable."""
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"

    headers = {
        "Authorization": f"Bearer {AIRTABLE_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

def main():
    print("Fetching invoices from Airtable...\n")

    data = get_invoices()

    if data:
        invoices = data.get('records', [])
        print(f"Found {len(invoices)} invoices:\n")

        for record in invoices:
            fields = record['fields']
            print(f"Invoice: {fields.get('Invoice Number', 'N/A')}")
            print(f"Vendor: {fields.get('Vendor', 'N/A')}")
            print(f"Amount: ${fields.get('Amount', 0):.2f}")
            print(f"Status: {fields.get('Status', 'Unknown')}")
            print("-" * 40)

if __name__ == "__main__":
    main()
```

**What this does:**
- Builds the API URL (base ID + table name)
- Adds authentication header (your token)
- Makes GET request
- Parses JSON response
- Prints invoice data

**Before running:**
1. Install requests library: `pip3 install requests`
2. Replace `AIRTABLE_TOKEN` with your actual token
3. Replace `BASE_ID` with your actual base ID
4. Make sure `TABLE_NAME` matches exactly ("Invoices")

**Run it:**
```bash
python3 airtable_test.py
```

You should see the test invoices you created earlier!

---

STOP: Run the script now.

**Tell me:**
1. Did it work? Did you see your test invoices?
2. If not, what error did you get? (Copy the exact error message)
3. If it worked - how does it feel to pull data from a cloud database via API?

---

USER: [Student runs script and reports results]

---

ACTION: Based on results:

**IF it worked:**
- "Boom! You just made your first API call. That data is coming from Airtable's servers, through the internet, into your script."
- "This is the foundation of all automation. You can now read data from anywhere with an API."
- "Let's add one more invoice via API..."

**IF error (common issues):**

*Error: "Invalid token"*
- "Your token might be wrong. Go back to Airtable Developer Hub and verify you copied it correctly."
- "Make sure there are no extra spaces or quotes around the token in your code."

*Error: "Table not found"*
- "Check the table name. It's case-sensitive. Is it exactly 'Invoices'?"

*Error: "Module not found: requests"*
- "You need to install the requests library. Run: `pip3 install requests`"

*Error: 401 Unauthorized*
- "Your token doesn't have permission to access this base. Go back and make sure you added the base to your token's access list."

Help them debug, then have them try again.

---

### Exercise 1.3.8: Create a Record via API

Reading data is cool. Writing data is power.

**Task:** Add a new invoice to Airtable via API.

**The code:**

Add this function to your `airtable_test.py`:

```python
def create_invoice(invoice_data):
    """Create a new invoice in Airtable."""
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"

    headers = {
        "Authorization": f"Bearer {AIRTABLE_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "fields": invoice_data
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("Invoice created successfully!")
        return response.json()
    else:
        print(f"Error creating invoice: {response.status_code}")
        print(response.text)
        return None

# Update main() to test creation
def main():
    # Create a new invoice
    new_invoice = {
        "Invoice Number": "INV-2024-9999",
        "Vendor": "Widget Supplies Inc",
        "Invoice Date": "2024-02-04",
        "Due Date": "2024-03-05",
        "Amount": 2500.00,
        "Status": "Received",
        "Notes": "Created via API - test automation"
    }

    print("Creating new invoice...\n")
    result = create_invoice(new_invoice)

    if result:
        print(f"Created record ID: {result['id']}")
        print("\nNow fetching all invoices...\n")

        # Fetch all to verify
        data = get_invoices()
        if data:
            print(f"Total invoices: {len(data['records'])}")
```

**Run it:**
```bash
python3 airtable_test.py
```

Then go to Airtable in your browser and refresh. You should see the new invoice!

---

STOP: Run the script and check Airtable.

**Tell me:**
1. Did the new invoice appear in Airtable?
2. Look at the invoice - does all the data look correct?
3. What's the record ID that was returned?

This is a huge milestone. You just created a database record programmatically.

---

USER: [Student reports creation results]

---

ACTION: When confirmed working:

**Celebrate the achievement:**
- "You just automated data entry. Think about what you did:"
- "Your code sent data over the internet to Airtable's API"
- "Airtable created a new record in your database"
- "You can now do this with ANY data - including parsed invoices from PDFs"
- "This is exactly what your invoice automation will do in Module 2"

**Key insight:**
- "Right now you're creating invoices with hardcoded data."
- "Soon, you'll parse PDFs to get invoice data, then create Airtable records automatically."
- "The API part? You just learned it. The PDF parsing? We'll cover that next module."

---

## Part 4: Data Transformation

The final skill: transforming data from one format to another.

You have:
- Invoice data from PDFs (eventually)
- CSV vendor lists
- JSON data structures
- Airtable API format

They're all slightly different. You need to transform between them.

---

### Exercise 1.3.9: Transform Invoice JSON to Airtable Format

**Task:** Take your `sample-invoice-data.json` and convert it to the format Airtable expects.

**The challenge:**

Your JSON has:
```json
{
  "invoice_number": "INV-2024-0342",
  "vendor_name": "Acme Corp",
  "total_amount": 1242.00,
  "line_items": [ ... ]
}
```

Airtable wants:
```python
{
  "Invoice Number": "INV-2024-0342",
  "Vendor": "Acme Corp",
  "Amount": 1242.00
}
```

Notice:
- Different key names (snake_case vs Title Case)
- Airtable doesn't have a field for line_items (you'll store that in Notes)
- You need to map fields correctly

---

STOP: Before I give you code, think about this transformation.

**Describe in your own words:**
- What fields from the JSON should map to Airtable?
- What should you do with the line_items data?
- How would you handle the date format?

---

USER: [Student describes transformation logic]

---

ACTION: Validate their thinking, then provide solution:

**Create a file called `transform_invoice.py`:**

```python
import json
from datetime import datetime

def transform_invoice_for_airtable(invoice):
    """Transform invoice JSON to Airtable format."""

    # Build line items summary for notes
    line_items_text = "Line Items:\n"
    for item in invoice.get('line_items', []):
        line_items_text += f"- {item['description']}: {item['quantity']} × ${item['unit_price']} = ${item['total']}\n"

    # Add other notes
    notes = line_items_text
    if 'notes' in invoice:
        notes += f"\n{invoice['notes']}"

    # Transform to Airtable format
    airtable_record = {
        "Invoice Number": invoice['invoice_number'],
        "Vendor": invoice['vendor_name'],
        "Invoice Date": invoice['invoice_date'],
        "Due Date": invoice['due_date'],
        "Amount": invoice['total_amount'],
        "Status": "Received",  # Default status
        "Notes": notes
    }

    return airtable_record

def main():
    # Load sample invoice
    with open('sample-invoice-data.json', 'r') as f:
        invoice = json.load(f)

    print("Original invoice data:")
    print(json.dumps(invoice, indent=2))
    print("\n" + "="*50 + "\n")

    # Transform
    airtable_data = transform_invoice_for_airtable(invoice)

    print("Transformed for Airtable:")
    print(json.dumps(airtable_data, indent=2))

    print("\n" + "="*50)
    print("\nThis is ready to send to Airtable API!")

if __name__ == "__main__":
    main()
```

**Run it:**
```bash
python3 transform_invoice.py
```

You'll see both formats side-by-side.

---

### Exercise 1.3.10: Combine Everything - Full Pipeline

Now let's combine all the skills you've learned:

1. Load invoice from JSON
2. Validate the math
3. Look up vendor in CSV
4. Transform for Airtable
5. Create record via API

**The complete automation pipeline.**

---

STOP: This is the big one.

**Before I show you the code, describe what this script should do, step by step.**

Think about error handling too:
- What if the vendor isn't in the CSV?
- What if the invoice math is wrong?
- What if the API call fails?

Write out the logic in plain English.

---

USER: [Student describes complete pipeline logic]

---

ACTION: Validate their thinking, then provide complete solution:

**Create `invoice_pipeline.py`:**

```python
import json
import csv
import requests

# Airtable credentials
AIRTABLE_TOKEN = "patXXXXXXXXXXXXXX"  # Your token
BASE_ID = "appXXXXXXXXXXXXXX"  # Your base ID
TABLE_NAME = "Invoices"

def load_invoice(json_file):
    """Load invoice from JSON file."""
    with open(json_file, 'r') as f:
        return json.load(f)

def validate_invoice(invoice):
    """Validate invoice math."""
    errors = []

    # Check line items sum to subtotal
    calculated_subtotal = sum(item['total'] for item in invoice['line_items'])
    if abs(calculated_subtotal - invoice['subtotal']) > 0.01:
        errors.append(f"Subtotal mismatch")

    # Check subtotal + tax = total
    expected_total = invoice['subtotal'] + invoice['tax']
    if abs(expected_total - invoice['total_amount']) > 0.01:
        errors.append(f"Total amount mismatch")

    return errors

def lookup_vendor(vendor_name, csv_file):
    """Check if vendor is in approved list."""
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if vendor_name.lower() in row['vendor_name'].lower():
                return {
                    'found': True,
                    'active': row['active'] == 'TRUE',
                    'id': row['vendor_id'],
                    'terms': row['payment_terms']
                }
    return {'found': False}

def transform_for_airtable(invoice):
    """Transform invoice to Airtable format."""
    line_items_text = "Line Items:\n"
    for item in invoice['line_items']:
        line_items_text += f"- {item['description']}: ${item['total']}\n"

    return {
        "Invoice Number": invoice['invoice_number'],
        "Vendor": invoice['vendor_name'],
        "Invoice Date": invoice['invoice_date'],
        "Due Date": invoice['due_date'],
        "Amount": invoice['total_amount'],
        "Status": "Received",
        "Notes": line_items_text + f"\n{invoice.get('notes', '')}"
    }

def create_airtable_record(data):
    """Create record in Airtable."""
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {"fields": data}

    response = requests.post(url, headers=headers, json=payload)
    return response.status_code == 200

def process_invoice(invoice_file, vendor_file):
    """Complete invoice processing pipeline."""
    print("="*50)
    print("INVOICE PROCESSING PIPELINE")
    print("="*50)

    # Step 1: Load invoice
    print("\n[1/5] Loading invoice...")
    invoice = load_invoice(invoice_file)
    print(f"  ✓ Loaded: {invoice['invoice_number']} from {invoice['vendor_name']}")

    # Step 2: Validate math
    print("\n[2/5] Validating invoice math...")
    errors = validate_invoice(invoice)
    if errors:
        print(f"  ✗ VALIDATION FAILED:")
        for error in errors:
            print(f"    - {error}")
        return False
    print(f"  ✓ Math is correct (Total: ${invoice['total_amount']})")

    # Step 3: Check vendor
    print("\n[3/5] Checking vendor...")
    vendor_check = lookup_vendor(invoice['vendor_name'], vendor_file)
    if not vendor_check['found']:
        print(f"  ✗ Vendor not found in approved list!")
        return False
    if not vendor_check['active']:
        print(f"  ⚠ Warning: Vendor is INACTIVE!")
    print(f"  ✓ Vendor found: {vendor_check['id']} ({vendor_check['terms']})")

    # Step 4: Transform data
    print("\n[4/5] Transforming for Airtable...")
    airtable_data = transform_for_airtable(invoice)
    print(f"  ✓ Data transformed")

    # Step 5: Create record
    print("\n[5/5] Creating Airtable record...")
    success = create_airtable_record(airtable_data)
    if success:
        print(f"  ✓ Record created successfully!")
        print("\n" + "="*50)
        print("INVOICE PROCESSED SUCCESSFULLY")
        print("="*50)
        return True
    else:
        print(f"  ✗ Failed to create record")
        return False

if __name__ == "__main__":
    result = process_invoice('sample-invoice-data.json', 'vendor-list.csv')
    if result:
        print("\n✓ Check Airtable to see your new invoice!")
    else:
        print("\n✗ Processing failed - check errors above")
```

**This is the foundation of your invoice automation.**

Run it:
```bash
python3 invoice_pipeline.py
```

Watch it process the invoice step by step!

---

STOP: Run the complete pipeline script.

**Then answer:**
1. Did it successfully process the invoice?
2. Check Airtable - do you see the new record?
3. Look at the console output - which step do you think is most important for catching errors?
4. How would you modify this to process 100 invoices instead of just one?

This is the critical thinking part.

---

USER: [Student runs pipeline and reflects]

---

ACTION: Final debrief and wrap-up:

1. **Celebrate completion:**
   - "You just built a complete data processing pipeline."
   - "This script does what Finance currently does manually in 5-10 minutes per invoice."
   - "And it validates the data, checks vendors, and catches errors automatically."

2. **Address their reflection:**
   - Validation step is crucial - it prevents bad data from entering the system
   - To process 100 invoices: loop through a folder of JSON files
   - Error handling becomes even more important at scale

3. **Bridge to next lesson:**
   - "Right now you're processing pre-made JSON files."
   - "In Module 2, you'll add PDF parsing to extract this data from actual invoice PDFs."
   - "But the API connection, validation, transformation? You already know how to do that."

---

## Meta Skill: Reading API Documentation

**What you really learned in this lesson:**

How to work with external systems via APIs.

Every SaaS tool has an API:
- Airtable (you just used it)
- Google Sheets
- Stripe
- Slack
- Gmail
- QuickBooks

The pattern is always the same:
1. Get API credentials (token/key)
2. Read the API docs
3. Make HTTP requests (GET/POST/PATCH/DELETE)
4. Handle responses
5. Transform data as needed

**The meta skill:** You don't need to memorize every API. You need to know how to:
- Find API documentation
- Understand authentication requirements
- Read example code
- Test API calls
- Debug when things break

**And here's the secret:** Claude Code can read API docs for you and generate the code. Your job is to understand:
- What you're trying to accomplish
- What data goes in
- What data comes out
- How to handle errors

---

## Where Else This Applies

**Skills from this lesson apply to:**

**CSV Parsing:**
- Bank transaction exports
- Customer lists from CRM
- Inventory data from warehouse systems
- Sales reports from e-commerce platforms
- Any spreadsheet anyone ever emails you

**JSON Handling:**
- Every API response (they all use JSON)
- Configuration files for applications
- Data exchange between internal systems
- Webhook payloads

**API Integration:**
- Syncing data between systems (Airtable ↔ Google Sheets)
- Automating social media posts
- Creating invoices in QuickBooks automatically
- Sending Slack notifications
- Updating CRM records
- Literally any SaaS tool integration

**Data Transformation:**
- Every automation that connects two systems
- Migrating data from old system to new system
- Preparing data for analysis
- Cleaning messy data before use

**These are universal automation skills.**

---

## Troubleshooting Guide

**Common issues and solutions:**

**CSV File Not Found:**
- Make sure file is in same folder as script
- Check filename (case-sensitive)
- Use absolute path if needed: `/full/path/to/file.csv`

**JSON Parsing Error:**
- Check for syntax errors (missing comma, extra bracket)
- Use a JSON validator: jsonlint.com
- Make sure it's actually JSON (not CSV with .json extension)

**Airtable API Errors:**

*401 Unauthorized:*
- Token is wrong or expired
- Token doesn't have access to the base
- Token doesn't have correct scopes

*404 Not Found:*
- Base ID is wrong
- Table name is wrong (case-sensitive!)
- Record ID doesn't exist (if updating)

*422 Unprocessable Entity:*
- Field name is wrong
- Data type doesn't match field type
- Required field is missing

**Requests Module Not Found:**
- Install with: `pip3 install requests`
- Or: `python3 -m pip install requests`

**General Debugging Tips:**
- Print variables to see what they contain
- Use `print(json.dumps(data, indent=2))` for pretty JSON
- Check API responses: `print(response.text)`
- Read error messages carefully - they usually tell you what's wrong

---

## Success Criteria for Lesson 1.3

Before moving to Lesson 1.4, make sure you can check these off:

- [ ] I can read and parse CSV files in Python
- [ ] I can search and filter data from CSVs
- [ ] I understand JSON structure (objects, arrays, nested data)
- [ ] I can read and validate JSON files
- [ ] I have a working Airtable account with a test base
- [ ] I successfully connected to Airtable API
- [ ] I can read records from Airtable via API
- [ ] I can create records in Airtable via API
- [ ] I understand data transformation (mapping between formats)
- [ ] I built a complete data processing pipeline
- [ ] I know how to debug API issues
- [ ] I understand how APIs work at a high level

**If you can check all those boxes, you're ready for Lesson 1.4: Introduction to MCPs.**

---

STOP: Final reflection before moving on.

**Answer these questions:**

1. What was the hardest part of this lesson?
2. What clicked for you that didn't make sense before?
3. On a scale of 1-10, how confident do you feel working with APIs now?
4. What's one thing you want to automate with these skills?

Be honest. If something still doesn't make sense, ask me now.

---

USER: [Student reflects on lesson]

---

ACTION: Final wrap-up based on reflection:

**Address what was hard:**
- If API concepts: "That's normal. You'll get more comfortable with practice. Every API works the same way - you've got the pattern now."
- If JSON: "JSON gets easier the more you see it. Just remember: {} = object, [] = array."
- If transformation: "Data transformation is hard because every system is different. You'll build a library of patterns over time."

**Celebrate what clicked:**
- Reinforce their insight
- Connect it to what they'll do next

**Address confidence level:**
- If low (1-5): "Don't worry. You'll practice more in Module 2 when we build the real automation. This was just foundation."
- If medium (6-8): "Perfect. You have healthy respect for the complexity but understand the basics. That's ideal."
- If high (9-10): "Great! Put that confidence to work in the next lessons."

**Address their automation idea:**
- If it's related to course material: "Perfect! Keep that in mind for Module 2's custom project."
- If it's unrelated: "Love it. The skills you're learning will apply there too. Finish the course, then build it!"

**Final send-off:**

"Alright, you just leveled up. You can now:
- Parse business data (CSV/JSON)
- Connect to external systems (APIs)
- Transform data between formats
- Build complete automation pipelines

Next up: **Lesson 1.4 - Introduction to MCPs**.

MCPs (Model Context Protocol) let you extend Claude Code's capabilities with plugins. You'll install MCPs for Airtable, Google Sheets, and other tools - so you can work with them conversationally instead of writing API code.

It's like giving Claude Code superpowers.

When you're ready, open Lesson 1.4.

Great work on this one. Seriously."

---

## Additional Resources

**Want to go deeper?**

**Airtable API Documentation:**
- https://airtable.com/developers/web/api/introduction
- Read this when building your real automations
- Has examples for every operation

**CSV in Python:**
- Official docs: https://docs.python.org/3/library/csv.html
- Lots of options beyond what we covered (delimiters, quote handling, etc.)

**JSON in Python:**
- Official docs: https://docs.python.org/3/library/json.html
- Learn about json.dump vs json.dumps, json.load vs json.loads

**Requests Library:**
- https://requests.readthedocs.io/
- The standard Python library for HTTP requests
- Essential for API work

**Practice Ideas:**
- Build a script that reads your bank CSV exports and categorizes transactions
- Connect to Google Sheets API (similar to Airtable)
- Parse JSON from a public API (weather, stocks, etc.)
- Build a vendor lookup tool with Flask web interface

**But don't get lost in tutorials. Your goal is to build real automations, not become a Python expert.**

---

**End of Lesson 1.3**

**Next:** Lesson 1.4 - Introduction to MCPs

---

*You don't need to memorize every API. You need to know the pattern. Get credentials, make requests, handle data. That's it.*
