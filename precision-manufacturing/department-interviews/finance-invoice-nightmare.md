precision-manufacturing/department-interviews/sales-process-notes.md# Finance Department Interview - Marcus Rodriguez

**Date:** Your first week
**Department:** Finance & Accounts Payable
**Team Lead:** Marcus Rodriguez
**Team Size:** 4 people (Marcus, Elena, Priya, James)

---

## The Conversation

You met Marcus in the cramped finance office. He looked tired.

**You:** "Thanks for meeting with me. Sarah said you're dealing with some manual process issues?"

**Marcus:** (laughs) "Issues? That's diplomatic. We're drowning. Come, let me show you."

*He walks you to Elena's desk. She's got 3 monitors, all showing different things.*

**Marcus:** "Elena, show them the morning routine."

**Elena:** "Sure. Every morning I do this:

1. Check the invoices@precisionmfg.com inbox - we get 15-25 emails per day
2. Each email has a PDF invoice attachment from vendors
3. I download each PDF to my desktop
4. Open the PDF, read the invoice
5. Manually type the data into our Airtable 'Invoices' base:
   - Invoice number
   - Vendor name
   - Invoice date
   - Due date
   - Total amount
   - Line items (sometimes 20+ lines)
6. Save the PDF to Google Drive in the right vendor folder
7. Reply to the sender confirming receipt
8. Move on to the next one

**You:** "How long does this take?"

**Elena:** "Per invoice? 5-8 minutes if it's straightforward. 15 minutes if the invoice is messy or has lots of line items. So... 2-3 hours every single morning. Just. Data. Entry."

**Marcus:** "And that's ONE person. Priya does the same thing for 1099s. James does expense reports. It's absurd."

---

## The Pain Points

**You:** "What makes this so painful?"

**Marcus:** "Where do I start?

**1. It's Mind-Numbing**
I have a finance degree and an MBA. Elena has her CPA. We're typing numbers from PDFs like it's 1995.

**2. It's Error-Prone**
Typos happen. Wrong decimal places. Misread numbers. We catch most of them, but not all. Last month we paid $18,500 instead of $1,850 because Elena missed a comma.

**3. It Delays Everything**
We can't approve payments until invoices are in the system. If Elena's out sick? Vendors wait. Relationships suffer.

**4. It Doesn't Scale**
We're growing. More vendors = more invoices. I can't just hire another person to do data entry. The budget doesn't allow it.

**5. The PDFs Are Inconsistent**
Every vendor uses a different template. Some are clean, some are scanned images (terrible quality), some have weird formatting. Humans can figure it out. Software... I don't know, can it?"

---

## What They've Tried

**You:** "Has anyone tried to automate this?"

**Marcus:** (sighs) "Oh yeah. The previous consultant - what was their name? - they tried.

They set up some Zapier thing that was supposed to:
- Monitor the inbox
- Extract invoice data automatically
- Send to Airtable

It... sort of worked? For like 3 days?

**Problems:**
1. The OCR accuracy was terrible - maybe 60%? We had to fix everything anyway
2. It couldn't handle scanned PDFs at all
3. Cost like $200/month for the Zapier premium plan
4. Broke randomly and nobody knew how to fix it
5. They left before documenting how it worked

We turned it off after 2 weeks. Went back to manual."

---

## What Success Would Look Like

**You:** "If you could wave a magic wand, what would the perfect solution look like?"

**Marcus:** "Honestly? I just want this:

**Morning Routine (Automated):**
1. System checks the invoices inbox
2. Downloads PDFs automatically
3. Extracts the data (accurately - like 95%+ accuracy)
4. Creates Airtable records with the data
5. Files PDFs in the right Google Drive folder
6. Maybe flags anything weird for human review
7. Elena reviews instead of typing

**What This Gives Us:**
- Elena's 2-3 hours → 20-30 minutes of review time
- Fewer errors (computer doesn't typo)
- We can scale (more vendors = no problem)
- Data is searchable immediately
- I can actually analyze spending patterns instead of just entering data

**You:** "What about accuracy? You mentioned the Zapier thing was only 60%"

**Marcus:** "Here's the thing - I don't need 100%. I need 95%+. If the system gets it right most of the time, and flags uncertain ones for review? That's still way faster than typing everything manually.

Like, if it processes 20 invoices and gets 18 perfect and flags 2 for Elena to check? I'll take that deal all day."

---

## The Data

**You:** "Can I see some sample invoices?"

**Marcus:** "Sure, let me grab a few..."

*He pulls up some PDFs on his screen*

**Invoice Types You'll See:**
1. **Clean Digital PDFs** - Modern vendors, easy to read
2. **Scanned Images** - Older vendors, sometimes blurry
3. **Multi-Page** - Big orders with 20+ line items
4. **Different Formats** - Every vendor's template is different

**Data We Need:**
- **Invoice Number** (required)
- **Vendor Name** (required)
- **Invoice Date** (required)
- **Due Date** (required)
- **Total Amount** (required)
- **Subtotal** (nice to have)
- **Tax** (nice to have)
- **Line Items** (nice to have, but a lot of work)

**You:** "What's your Airtable structure look like?"

**Marcus:** "Pretty simple:

**Table: Invoices**
- Invoice Number (single line text)
- Vendor (linked to Vendors table)
- Invoice Date (date)
- Due Date (date)
- Amount (currency)
- Status (single select: Received / Under Review / Approved / Paid)
- PDF File (attachment)
- Notes (long text)

We can share access if you need to test."

---

## Priority Level

**You:** "Where does this rank in terms of urgency?"

**Marcus:** "Top 3 for sure. Maybe #1.

Sarah's pushing us to close books faster. We can't do that if we're 2 days behind on data entry.

Plus - and I hate to say this - Elena's getting burned out. She's mentioned looking for other jobs. If she leaves, we're screwed. Nobody else wants to do this work.

If you can automate even 70% of this? You're a hero. The whole finance team will love you."

---

## Technical Details

**Current Setup:**
- Email: invoices@precisionmfg.com (Google Workspace)
- Database: Airtable (Finance & Accounting base)
- Storage: Google Drive (Invoices folder, organized by vendor)
- Volume: 15-25 invoices per day (350-500/month)

**Access:**
- Marcus can give you view access to everything
- Test credentials available
- He can create a "Test Invoices" folder for development

**Constraints:**
- Budget: Prefer free/low-cost solutions
- IT Support: Minimal (they're swamped)
- Maintenance: Needs to be something Elena can troubleshoot if it breaks

---

## The Ask

**Marcus:** "Look, I'm not a technical person. I don't know if this is hard or easy. But if there's a way to make this happen... please. This is killing us.

And if you can do this one? The word will spread. Every department has something like this. You'll be the most popular person in the company."

**You:** "Let me see what I can do."

**Marcus:** "Thank you. Seriously. Just... thank you for even trying."

---

## Your Notes

After the meeting, you jot down thoughts:

**Opportunity Assessment:**
- ✅ High impact (saves 2-3 hours/day)
- ✅ Clear requirements
- ✅ Measurable ROI
- ✅ Cooperative stakeholder
- ✅ Access to test data
- ⚠️ Technical challenge (PDF parsing varies)
- ⚠️ Integration complexity (Email + Airtable + Drive)

**Approach Ideas:**
1. Start with local PDF processing (prove it works)
2. Add Google Drive monitoring (automate the folder check)
3. Build web upload tool as backup (if email too complex)
4. Focus on accuracy - flag uncertain extractions

**Next Steps:**
- Get sample invoices from Marcus
- Set up test Airtable base
- Build proof of concept with local PDFs
- Show Marcus working demo
- Iterate based on feedback

**Risk:**
If this fails, you lose credibility fast. But if it works? Golden.

---

*This is your first project. Let's make it count.*
