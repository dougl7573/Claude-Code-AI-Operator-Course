# Inventory Management Interview - Lisa Park

**Date:** Week 4 of your new role
**Department:** Inventory & Warehouse
**Team Lead:** Lisa Park
**Team Size:** 5 people (Lisa + 4 warehouse coordinators)

---

## The Conversation

You met Lisa in the warehouse office - a small glass-walled room overlooking rows of shelving. The hum of forklifts in the background.

**You:** "Lisa! Thanks for taking the time. I heard you're dealing with some spreadsheet challenges?"

**Lisa:** (looks up from THREE monitors, all showing Excel) "Spreadsheet challenges? That's like calling a hurricane 'some weather.' Come see this disaster."

*She gestures to her center monitor. An Excel file with 50+ tabs at the bottom. File name: "MASTER_INVENTORY_2025_FINAL_v7_ACTUAL_FINAL.xlsx"*

**Lisa:** "This... THIS... is our inventory management system.

50,000+ SKUs. All tracked in this Excel file.

**You:** "Wait. Fifty THOUSAND SKUs in one Excel file?"

**Lisa:** "I KNOW. Trust me, I know. It's insane.

Here's how we got here:
- Started 15 years ago with 500 SKUs in Excel (fine)
- Grew to 5,000 (still manageable)
- Now we're at 50,000+ (absolutely not fine)

Every time I suggest moving to a real inventory system - like NetSuite or something - Finance says 'too expensive' and IT says 'too complex to migrate.'

So here we are. Excel. Held together with prayers and VLOOKUP formulas."

*She scrolls through the file. Tabs include: Raw_Materials, Finished_Goods, WIP, Vendors, Reorder_Triggers, Locations, Historical_Data, etc.*

**Lisa:** "And this file? It breaks. Constantly.

Like, literally every week something goes wrong:
- Formulas get accidentally deleted
- Circular references appear out of nowhere
- File gets corrupted and won't open
- Someone sorts one column but not the others (data mismatches)
- Excel crashes when we try to filter 50,000 rows

Last month, we lost 3 hours of work because the file crashed and autosave failed. THREE HOURS of inventory updates. Gone."

**You:** "What happens when it breaks?"

**Lisa:** "I fix it. Or one of my team fixes it. We've become Excel forensics experts.

I'd estimate we spend 5-8 hours per WEEK just troubleshooting Excel issues. Not doing inventory management. Just fixing the tool."

---

## The Pain Points

**You:** "Walk me through the biggest problems."

**Lisa:** "Where do I even start?

**1. Performance is TERRIBLE**
Opening this file takes 2-3 minutes. Saving takes 45 seconds. Filtering data? Crashes half the time.

My team wastes 15-20 minutes per day just waiting for Excel to respond.

**2. No Real-Time Updates**
We have 4 warehouse coordinators. They all work in the same file (saved on network drive).

But Excel doesn't do real-time collaboration well. So we have a RULE:
- 'Check out' the file before editing (Slack message: 'I'm using inventory file')
- Make your changes
- Save and 'check in'

If two people edit at the same time? Conflicts. Data gets overwritten. Chaos.

Last week, Tony and Maria both updated inventory simultaneously. Tony's changes got lost. We thought we had 500 units of Part #XK-2847. Actually had 200. Almost missed a customer order.

**3. Formula Hell**
This file has THOUSANDS of formulas:
- VLOOKUP to match SKU to description
- SUMIF to calculate total inventory by location
- Conditional formatting for reorder alerts
- INDIRECT references across tabs

Every time we add a new row, formulas break. Every time we add a new tab, references break.

I have a 4-page Word doc titled 'How to Fix Common Excel Errors in Inventory File.' My team has it printed and laminated.

**4. No Audit Trail**
If someone changes a number, there's no log of who did it or why.

Example: Last month, inventory for Part #MZ-4521 showed 0 units. Customer called asking for it. I checked - we actually had 1,200 units.

Someone had accidentally typed '0' instead of '1200.' But who? When? Why? No idea. No way to track it.

**5. Can't Scale**
We're growing. We'll be at 75,000 SKUs by next year.

Excel has a 1,048,576 row limit. We're not there yet, but we're using 50,000+ rows now. Add historical data, and we're in trouble.

Also, the file is 67 MB. It takes forever to email. Network drive is slow. Everything sucks.

**6. Integration Nightmares**
Sales team uses Airtable for orders. Finance uses different spreadsheets for cost accounting. Purchasing uses ANOTHER system for vendor management.

Nothing talks to each other.

So when Sales closes an order, they Slack me: 'Lisa, do we have 300 units of Part X?'

I check Excel. Slack back: 'Yes' or 'No.'

Then I manually update the Excel file to reserve those units.

Then I manually update ANOTHER sheet to trigger a reorder if we're low.

It's manual. All of it."

---

## What They've Tried

**You:** "Have you tried to fix this?"

**Lisa:** (laughs darkly) "Oh, we've tried.

**Attempt 1: Upgrade to Excel 365 Online**
Thought maybe Excel Online would handle large files better + allow real-time collaboration.

Results:
- Still slow
- Lost some formula functionality
- Offline access was unreliable (warehouse WiFi is spotty)
- Gave up after 2 weeks

**Attempt 2: Split into Multiple Files**
Tried breaking the master file into smaller files: Raw_Materials.xlsx, Finished_Goods.xlsx, etc.

Problems:
- Formulas that referenced across tabs broke
- Now we had 8 files to keep in sync
- Version control nightmare (which file is current?)
- Worse than the original problem

Merged back into one file.

**Attempt 3: Proposal for NetSuite**
I spent 3 weeks building a business case for NetSuite (real inventory management system).

Cost: $10,000/year + $25,000 implementation.

CFO's response: 'Excel is free. Make it work.'

Died on the vine.

**Attempt 4: Access Database (Tony's idea)**
Tony used to be a database guy. He suggested Microsoft Access.

We tried it for 1 month:
- Migrated data to Access
- Built some queries
- It was actually... better?

But then:
- Tony left the company
- Nobody else knew Access
- Couldn't troubleshoot when things broke
- Migrated back to Excel

**Current State:** Excel. Forever. Apparently."

---

## What Success Would Look Like

**You:** "If you could wave a magic wand - and let's assume a full ERP migration is off the table - what would make your life better?"

**Lisa:** "Okay, realistic improvements:

**Phase 1: Stop the Bleeding (Alerts & Monitoring)**
I don't need to replace Excel immediately. But I need to know when things go wrong.

Ideal alerts:
- 'SKU #12345 is below reorder threshold' → Slack notification
- 'Inventory file hasn't been updated in 24 hours' → Alert (means something's broken)
- 'Negative inventory detected for SKU #67890' → Immediate alert (data error)
- 'Formula error in column G' → Alert (someone broke something)

If I could catch errors EARLY, I could fix them before they cascade.

**Phase 2: Automate Reorder Process**
Right now, reordering is manual:
1. Check inventory levels (filter for 'below threshold')
2. Check vendor lead times (different spreadsheet)
3. Create purchase order (email to vendor)
4. Update 'On Order' column in Excel
5. Hope I didn't forget anything

Ideal:
- System detects low inventory
- Auto-generates PO draft
- Sends me a Slack message: 'Review PO for SKU #12345 - 500 units from Vendor ABC'
- I approve or edit
- PO gets sent automatically
- Excel gets updated automatically

**Phase 3: Real-Time Sync with Sales**
When Sales closes an order in Airtable, it should automatically:
- Deduct inventory from Excel
- Alert me if inventory is insufficient
- Trigger reorder if below threshold

No more Slack messages asking 'Do we have X units?'

**You:** "What about a full migration away from Excel?"

**Lisa:** "Look, I've given up on that dream.

Everyone hates Excel, but everyone KNOWS Excel. If I move to some new system, I need to:
- Train 5 people
- Migrate 50,000+ SKUs without errors
- Get IT support (good luck)
- Get budget approval (not happening)

So for now? I'll settle for making Excel LESS PAINFUL.

Alerts, automation around the edges, reducing manual work - that's realistic.

Full replacement? That's a 2027 problem."

---

## The Data

**You:** "Can you show me what the Excel file looks like?"

**Lisa:** "Sure, buckle up..."

*She opens the main tab: 'Finished_Goods'*

**Columns:**
- SKU (text, e.g., 'XK-2847-B')
- Description (text)
- Category (dropdown)
- Location (warehouse zone, e.g., 'A3-12')
- Qty_On_Hand (number)
- Qty_Reserved (number - for active orders)
- Qty_Available (formula: On_Hand - Reserved)
- Reorder_Threshold (number)
- Reorder_Qty (number)
- Vendor (VLOOKUP to Vendors tab)
- Unit_Cost (currency)
- Last_Updated (date - manually entered)
- Notes (text)

**Formulas (examples):**
```excel
// Qty_Available
=[@[Qty_On_Hand]]-[@[Qty_Reserved]]

// Conditional Formatting (turns red if below threshold)
=[@[Qty_Available]]<[@[Reorder_Threshold]]

// Vendor Lookup
=VLOOKUP([@SKU],Vendors!A:D,2,FALSE)
```

**Other Tabs:**
- Raw_Materials (similar structure, 15,000 rows)
- WIP (Work in Progress, 8,000 rows)
- Vendors (vendor info, 200 rows)
- Locations (warehouse zones, 150 rows)
- Historical_Data (3 years of inventory snapshots - huge tab, rarely used)

**File Details:**
- Size: 67 MB
- Rows (total): ~50,000 across all tabs
- Last Modified: Changes daily
- Saved Location: Network drive (slow access)

**You:** "What's the biggest pain point with this structure?"

**Lisa:** "Three things:

1. **Formulas are fragile** - One wrong sort breaks everything
2. **No audit trail** - Can't see who changed what
3. **Manual updates** - Every inventory transaction requires someone to type in a number

If I could fix those three things? Life gets 70% better."

---

## Technical Details

**Current Setup:**
- File: Excel 2019 (desktop version)
- Storage: Windows network drive (warehouse server)
- Access: 5 people have edit access
- Backup: Daily backup to external drive (manual)
- Update Frequency: 20-50 changes per day

**Integration Points:**
- Sales: Airtable (Sales Orders table has SKU + Qty fields)
- Purchasing: Email-based (no system)
- Finance: Separate cost accounting spreadsheets

**Constraints:**
- Budget: Minimal (no big software purchases)
- Migration: Can't fully replace Excel (political + training reasons)
- IT Support: Limited (they're swamped)
- Training: Keep it simple (warehouse team is not technical)

**Access:**
- Lisa can share read-only copy for development
- Can create test data subset for POC
- Airtable access available (for Sales integration)

---

## Priority Level

**You:** "How urgent is this?"

**Lisa:** "Honest answer? Medium urgency, HIGH frustration.

It's not BREAKING the business like Finance's invoice thing. We're limping along.

But it's death by a thousand cuts:
- 5-8 hours/week fixing Excel issues
- Frequent close calls on inventory accuracy
- Team morale is low (everyone hates the Excel file)
- It's going to get WORSE as we scale

I think this is a good 'Phase 2' project. Not urgent, but strategically important.

Plus, if you can show a successful 'Excel automation' project, every department will want one. This could be your template for dealing with spreadsheet chaos."

---

## The Ask

**Lisa:** "Here's what I need, in order of priority:

**Phase 1: Alerts (Minimum Viable)**
- Monitor the Excel file for errors (formulas, negative values, etc.)
- Alert me via Slack when things break
- Alert me when inventory drops below reorder threshold
- Saves 2-3 hours/week of manual checking

**Phase 2: Reorder Automation (Big Win)**
- Detect low inventory
- Auto-generate PO drafts
- Send for approval
- Update Excel when approved
- Saves 3-5 hours/week

**Phase 3: Sales Integration (Dream)**
- Sync Airtable orders → Excel inventory
- Auto-deduct reserved inventory
- Alert if order exceeds available inventory
- Saves 5+ hours/week + reduces errors

But honestly? If you can just do Phase 1? You'll save my sanity.

I'm tired of playing Excel firefighter."

**You:** "This is definitely doable. The alerts are pretty straightforward. Reorder automation is more complex but achievable."

**Lisa:** "I don't need it tomorrow. I know you've got other priorities.

But when you're ready? I'll give you full access, sample data, whatever you need.

Just... please. Help me escape Excel hell."

---

## Your Notes

After the meeting, you write down thoughts:

**Opportunity Assessment:**
- ✅ Clear pain points (5-8 hours/week wasted)
- ✅ Realistic expectations (not asking for full replacement)
- ✅ Good data access
- ✅ Cooperative stakeholder
- ⚠️ Complex data structure (50K+ rows, many formulas)
- ⚠️ Integration challenges (multiple systems)
- ⚠️ Excel is fragile (any automation needs error handling)

**Approach Ideas:**
1. **Phase 1: Monitoring Script**
   - Python script reads Excel file (openpyxl library)
   - Checks for errors: formula errors, negative values, missing data
   - Checks inventory levels vs thresholds
   - Sends Slack alerts
   - Runs on schedule (every hour?)

2. **Phase 2: Reorder Automation**
   - Detect SKUs below threshold
   - Generate PO (template-based)
   - Email/Slack for approval
   - Update Excel on approval

3. **Phase 3: Airtable Sync**
   - Read new orders from Airtable
   - Update Excel 'Reserved' column
   - Alert if insufficient inventory
   - Trigger reorder if needed

**Technical Considerations:**
- Excel file locking (need read-only access while warehouse uses it)
- Formula preservation (don't break existing formulas)
- Error handling (what if file is corrupted?)
- Performance (50K rows is slow to process)
- Backup before any automation writes to file

**Next Steps:**
- Get sample copy of Excel file
- Build read-only monitoring script (Phase 1 POC)
- Test Slack integration
- Demo to Lisa
- Iterate

**Risk:**
Medium. Excel automation can be brittle. Need robust error handling.

**Opportunity:**
Great showcase for "modernizing legacy processes without full replacement." Many companies have Excel problems like this.

---

*This is a Phase 3 project. Solid opportunity, but lower urgency than Finance/Sales.*
