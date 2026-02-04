# Sales Operations Interview - Jennifer Wu

**Date:** Week 2 of your new role
**Department:** Sales Operations
**Team Lead:** Jennifer Wu
**Team Size:** 3 people (Jennifer, Mike, Amy)

---

## The Conversation

You caught Jennifer right as she was finishing lunch at her desk.

**You:** "Hey Jennifer! Thanks for making time. Sarah mentioned you're dealing with some data sync issues?"

**Jennifer:** (looks up from her laptop, slightly frazzled) "Data sync? That's putting it mildly. Come look at this nightmare."

*She spins her monitor around. There are 6 Chrome tabs open - 3 Airtable tabs, 2 Google Sheets, 1 Gmail.*

**Jennifer:** "See this? This is my Tuesday morning ritual. Every. Single. Tuesday.

1. Open our Airtable Sales Pipeline base
2. Export last week's closed deals to CSV
3. Open the Revenue Tracking Google Sheet (Finance owns this)
4. Manually paste the data
5. Fix all the formatting (dates break, currency formats go crazy)
6. Add formulas back (they don't copy over)
7. Export another CSV from Airtable - this time for forecasting
8. Open the Sales Forecast Sheet (CEO wants this weekly)
9. Same copy-paste dance
10. Then Mike does the SAME thing for customer data going into the Marketing sheet
11. Amy does it for territory analysis

**You:** "How long does this take?"

**Jennifer:** "For me? 90 minutes on Tuesdays. Mike spends an hour on Thursdays. Amy does hers on Mondays. That's like... 3.5-4 hours per week across the team. Just copying data between systems."

**You:** "Why not just use Airtable for everything?"

**Jennifer:** (laughs bitterly) "Oh, I WISH. But:
- Finance team refuses to learn Airtable (they're Excel/Sheets people)
- CEO wants his forecast in Google Sheets because he has a whole dashboard there
- Marketing wants data in THEIR format, not ours
- Everyone wants different fields, different calculations, different views

So we maintain the golden source in Airtable, and then... manually distribute copies. Like it's 2010."

---

## The Pain Points

**You:** "Walk me through what makes this so frustrating."

**Jennifer:** "Okay, buckle up:

**1. The Data Gets Stale Immediately**
I export on Tuesday morning. By Tuesday afternoon, 3 deals have updated. But Finance is still looking at the morning snapshot. They make decisions on OLD DATA. Drives me insane.

**2. Version Control Nightmare**
Last month, Finance had a version from Week 1, CEO had Week 3, Marketing had Week 2. Nobody knew which was current. We made a $50K forecasting error because of it.

**3. It's Mind-Numbing Work**
I went to business school. I'm supposed to be analyzing sales trends, optimizing conversion rates, coaching reps. Instead, I'm doing copy-paste for 90 minutes every Tuesday.

**4. Errors Everywhere**
When you're manually copying 200+ rows of data, mistakes happen:
- Wrong columns get pasted
- Formulas break
- Data types change (dates become text, numbers become dates - it's chaos)
- I've sent wrong numbers to the CEO twice

**5. Can't Scale**
We're hiring 3 new sales reps next quarter. More reps = more data = more copying. At some point this becomes my full-time job."

---

## What They've Tried

**You:** "Have you looked for solutions?"

**Jennifer:** "Oh yeah. Multiple times.

**Attempt 1: Zapier**
Mike set up a Zapier automation that was supposed to sync Airtable to Google Sheets.

Problems:
- The free plan only gives you 100 tasks/month (we need 500+)
- The paid plan is $20/month per user ($60/month for our team)
- It kept breaking when we added new fields
- Google Sheets would hit row limits and everything crashed
- No control over formatting

We used it for 3 weeks, then gave up.

**Attempt 2: Airtable Sync to Google Sheets Extension**
There's an Airtable extension that's supposed to push data to Sheets.

Problems:
- Only syncs one table at a time (we need 3+ tables)
- Doesn't handle linked records well
- Updates are manual - you still have to click 'Sync' every time
- So we're back to manual anyway

**Attempt 3: Convinced Finance to Try Airtable**
I actually got the Finance director to log into Airtable once.

She took one look at the interface and said "This is too complicated. I need my pivot tables."

Lost that battle.

**Current State:** We're back to manual CSV exports. It's reliable, if soul-crushing."

---

## What Success Would Look Like

**You:** "If you could design the perfect solution, what would it do?"

**Jennifer:** "Honestly, I've dreamed about this:

**The Ideal Morning (Automated):**
1. I update a deal in Airtable (status, amount, close date)
2. Within minutes - maybe hourly? - the data automatically flows to:
   - Finance's Revenue Tracking Sheet
   - CEO's Sales Forecast Sheet
   - Marketing's Customer Data Sheet
3. Formatting is preserved (dates look like dates, currency has $)
4. Formulas in the destination sheets DON'T break
5. Maybe I get a Slack notification: "Sync complete - 47 records updated"
6. I can see a log of what changed

**What This Gives Us:**
- My 90 minutes → 5 minutes of reviewing the log
- Data is always current (no more stale snapshots)
- No more "which version is right?" confusion
- I can focus on actual sales ops work
- When we scale, the automation scales with us

**You:** "What about data going the other way? Sheets to Airtable?"

**Jennifer:** "Ooh, good question. Right now, no. But eventually? Yes.

Finance sometimes adjusts revenue numbers (accounting stuff I don't understand). It would be nice if those adjustments synced BACK to Airtable. But that's version 2.0.

For now, I just need Airtable → Sheets to work reliably."

---

## The Data

**You:** "Can you show me what this looks like?"

**Jennifer:** "Sure, let me pull up the systems..."

*She shares her screen*

**Airtable Structure:**

**Table 1: Deals Pipeline**
- Deal Name (text)
- Company (linked to Companies table)
- Amount (currency)
- Close Date (date)
- Stage (single select: Prospecting / Qualified / Proposal / Negotiation / Closed Won / Closed Lost)
- Owner (linked to Sales Reps table)
- Probability (percent)
- Product (linked to Products table)

**Table 2: Companies**
- Company Name
- Industry
- Size
- Territory

**Table 3: Sales Reps**
- Name
- Territory
- Quota

**Google Sheets They Need:**

**Sheet 1: Revenue Tracking (Finance)**
- Needs: Deal Name, Company Name, Amount, Close Date, Stage, Owner Name
- Format: Dates as MM/DD/YYYY, Currency as $X,XXX.XX
- Updates: Weekly (Tuesdays)
- Rows: 200-300 deals

**Sheet 2: Sales Forecast (CEO)**
- Needs: Deal Name, Amount, Close Date, Probability, Stage, Territory
- Format: Custom (has conditional formatting based on stage)
- Updates: Weekly (Tuesdays)
- Rows: Active pipeline only (~100 deals)

**Sheet 3: Customer Data (Marketing)**
- Needs: Company Name, Industry, Size, Deal Owner, Close Date, Amount
- Format: Different column order than the others (Marketing's preference)
- Updates: Weekly (Mondays)
- Rows: Closed Won only (~50/month)

**You:** "These all pull from the same Airtable data, just formatted differently?"

**Jennifer:** "EXACTLY. Same source, three different destinations with different formatting needs. That's why Zapier didn't work well - it's one-size-fits-all.

I need something that can:
- Pull from Airtable
- Map fields to different column names
- Format data appropriately
- Update the right sheet tabs
- Handle the fact that Sheets have formulas we don't want to overwrite"

---

## Priority Level

**You:** "Where does this rank for you urgency-wise?"

**Jennifer:** "High. Maybe not CRITICAL like Finance's invoice thing (I heard about that - Marcus is desperate). But definitely top 3.

Here's why:
- We're scaling sales team (3 new reps by April)
- CEO is getting impatient with "stale data" complaints
- Finance director and I have had... tense conversations about data accuracy
- My team's morale is low - nobody wants to do this manual work

If you can automate this? I will personally buy you lunch every week for a month."

---

## Technical Details

**Current Setup:**
- Source: Airtable (Sales Operations base)
- Destinations: 3 Google Sheets (in Shared Drives)
- Volume: ~200 active deals, 50-100 updates per week
- Update Frequency: Current = weekly, Ideal = daily or hourly

**Access:**
- Jennifer can share Airtable base (view + edit access)
- Google Sheets are in company Shared Drive
- She can create test copies for development

**Constraints:**
- Budget: Prefer under $50/month total (cheaper than Zapier team plan)
- Maintenance: Needs to be reliable (can't babysit it)
- Flexibility: New fields get added quarterly (needs to be adjustable)

**Systems Integration Points:**
- Airtable API (has good documentation)
- Google Sheets API (Jennifer has used this before)
- Slack (nice-to-have for notifications)

---

## The Ask

**Jennifer:** "Look, I know this might seem less urgent than the invoice processing thing. But here's the thing:

Sales is the lifeblood of this company. If we can't report revenue accurately and quickly, everything downstream breaks. Finance can't plan. CEO can't strategize. Marketing can't target the right customers.

This data flows through the ENTIRE company.

And right now, the bottleneck is me spending 90 minutes on Tuesdays doing copy-paste.

If you can make this automatic and reliable? You're not just saving my time. You're improving decision-making across the org."

**You:** "That's a compelling case. Let me think about the approach."

**Jennifer:** "I'm flexible on HOW it works. Python script? Google Apps Script? Magic beans? I don't care. I just need it to:
1. Work reliably
2. Run without me clicking buttons
3. Not break when we add fields
4. Be maintainable by someone who's not a programmer

That's it. Can you do it?"

---

## Your Notes

After the meeting, you write down your thoughts:

**Opportunity Assessment:**
- ✅ Clear impact (saves 3.5-4 hours/week team-wide)
- ✅ Well-defined requirements
- ✅ Measurable success criteria
- ✅ Motivated stakeholder (Jennifer gets it)
- ✅ Good data access
- ⚠️ Multi-destination complexity (3 different Sheets)
- ⚠️ Formatting requirements vary by destination
- ⚠️ Need to preserve existing formulas

**Approach Ideas:**
1. Python script with Airtable API + Google Sheets API
2. Run on schedule (cron job or cloud scheduler)
3. Map Airtable fields → Sheet columns (configurable)
4. Smart update (only change what's different)
5. Log all changes for auditing
6. Slack notifications optional

**Technical Considerations:**
- Airtable pagination (if >100 records)
- Google Sheets API quotas (should be fine for this volume)
- Error handling (what if API fails?)
- Dry-run mode (test before applying changes)
- Config file (so Jennifer can adjust mappings)

**Next Steps:**
- Get Airtable API key from Jennifer
- Get Google Sheets access
- Build POC with one Sheet first
- Show Jennifer it works
- Expand to all 3 Sheets
- Add scheduling

**Risk:**
Lower than Finance project (less mission-critical), but still high visibility. CEO sees these Sheets weekly.

**Opportunity:**
If this works, it's a template for ANY Airtable → Sheets sync. Other departments will want this.

---

*This could be your second win. Let's prove you can integrate systems.*
