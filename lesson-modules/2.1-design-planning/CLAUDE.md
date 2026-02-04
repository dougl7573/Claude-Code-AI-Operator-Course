# Lesson 2.1: Automation Design & Planning

**From Understanding to Building**

---

## The Shift

You walk into Marcus's office the Monday after completing your first week at Precision Manufacturing.

He looks up from his laptop. "Hey! How's it going? Learned anything useful yet?"

**You:** "Actually, yes. I've spent the week investigating processes across departments. I think I know where to start."

**Marcus:** (leans back, interested) "Yeah? Where?"

**You:** "Finance. The invoice processing nightmare you showed me. I think I can automate most of it."

**Marcus:** (sits up straight) "Wait, seriously? You're not just... researching? You're actually going to build something?"

**You:** "That's the plan. But I need to do this right. I need to understand exactly what you need before I start building."

**Marcus:** (excited now) "Okay. Okay yes. What do you need from me?"

**You:** "Time. Let's design this automation properly. I want to make sure we're solving the right problem."

---

## Welcome to Module 2

Stop for a second and recognize the shift that just happened.

**Module 1:** You learned concepts. You explored tools. You investigated processes. You understood the role.

**Module 2:** You BUILD.

This is where theory becomes reality. Where investigation becomes automation. Where ideas become working systems.

**Starting today, you will:**
- Design a real automation from scratch
- Build working code that processes actual data
- Deploy tools that save actual time
- Create a portfolio you can show employers or clients

**But before you write a single line of code, you need to PLAN.**

This lesson is about the design phase - turning Marcus's pain points into a specification you can build from.

**The most expensive mistakes in automation happen here - when you build the wrong thing or skip the planning phase entirely.**

Let's make sure you don't make those mistakes.

---

## The Problem with "Just Start Coding"

Here's what most people do when they hear about the invoice problem:

**Beginner approach:**
1. "I'll build a PDF parser!"
2. (Opens Claude Code, starts writing code)
3. (Builds something that works on one invoice)
4. (Doesn't work on other invoices)
5. (Adds special cases and hacks)
6. (Creates unmaintainable spaghetti code)
7. (Gives up or delivers something brittle)

**Why this fails:**
- No clear requirements
- No definition of success
- No error handling plan
- No consideration of edge cases
- No thought about maintenance

**The result:** Weeks of work, nothing production-ready.

**The better approach:**
1. Understand the problem deeply
2. Define success criteria clearly
3. Break down the automation into steps
4. Choose the right technical approach
5. Plan error handling upfront
6. Build incrementally
7. Test thoroughly
8. Deploy confidently

**The result:** Working automation in days, not weeks.

**Today, you're learning the better approach.**

---

## STOP: Think about your past experience.

Have you ever started a project without planning, and regretted it?

Maybe you:
- Built something nobody wanted
- Spent hours on the wrong approach
- Had to throw away code and restart
- Delivered something that broke immediately
- Couldn't explain what you built or why

**If you've experienced any of those: that's what planning prevents.**

Answer honestly:
1. Have you ever jumped into building something without planning first? What happened?
2. What would you want to know BEFORE starting the invoice automation?
3. What could go wrong if you just start coding?

---

USER: [Student reflects on planning experiences]

---

ACTION: When student responds:

1. **Acknowledge their experience:**
   - If they've had planning failures: "Exactly. Every automation builder learns this lesson at least once. Usually the hard way."
   - If they've never built anything: "Good. You get to learn planning BEFORE the painful lessons."
   - If they're disciplined about planning: "Perfect. You already have the right mindset. Now we'll formalize it."

2. **Emphasize the stakes:**
   - "Marcus's team is depending on this. If you build the wrong thing, you waste their time AND yours."
   - "Elena is burned out. If this fails, she might quit. The pressure is real."
   - "But if you PLAN this right, you'll build something that actually works."

3. **Set up the framework:**
   - "I'm going to walk you through a requirements gathering framework."
   - "It's the same process professional automation consultants use."
   - "Master this once, use it forever."

4. **Transition:** "Let's start by going back to Marcus's interview and extracting the REAL requirements..."

---

## Requirements Gathering: The Right Questions

You have Marcus's interview transcript. Now you need to turn his pain points into clear, testable requirements.

**The requirements gathering framework has 5 parts:**

### 1. Current State (What exists now?)
- What is the manual process today?
- Who does it, when, and how often?
- What systems/tools are involved?
- What data flows where?
- What breaks? What causes delays?

### 2. Desired State (What should exist?)
- What does success look like?
- What stays manual? What gets automated?
- Who uses the automation?
- What's the workflow?
- What's the happy path?

### 3. Success Criteria (How do we measure success?)
- What metrics improve?
- How much time saved?
- How do we know it's working?
- What's acceptable accuracy?
- What ROI do we expect?

### 4. Edge Cases & Failure Modes (What could go wrong?)
- What are the messy scenarios?
- What happens when it fails?
- How do users recover?
- What needs human review?
- What's the fallback plan?

### 5. Technical Constraints (What are the limits?)
- What's the budget?
- What systems must we integrate with?
- What are the access/security requirements?
- Who will maintain this?
- What's the scale (volume)?

**Let's apply this framework to the Finance invoice automation.**

---

## STOP: Extract the requirements from Marcus's interview.

**Your task:**

Go back to the Finance department interview. Read it carefully.

Then document the requirements using the 5-part framework:

1. **Current State** - Describe the manual process
2. **Desired State** - What Marcus wants automated
3. **Success Criteria** - How we measure success
4. **Edge Cases & Failure Modes** - What could go wrong
5. **Technical Constraints** - System limitations

**Be specific. Use quotes from the interview. Include numbers.**

Example:
- ❌ "They want to process invoices faster"
- ✅ "Elena spends 2-3 hours every morning (5-8 min per invoice × 15-25 invoices/day) manually entering invoice data into Airtable"

**Create a document called:** `Invoice_Automation_Requirements.md`

**Take your time. This is the foundation everything else builds on.**

---

USER: [Student creates requirements document]

---

ACTION: When student says they're done:

1. **Ask to see it:**
   - "Great. Show me what you extracted. Share key sections."

2. **Review their work:**
   - Check if they captured the MEASURABLE details:
     * Volume: 15-25 invoices/day
     * Time: 2-3 hours/day currently
     * Accuracy requirement: 95%+
     * Team size: 4 people
     * Current cost of failed attempt: $200/month Zapier

   - Check if they identified KEY requirements:
     * Must integrate: Email inbox, Airtable, Google Drive
     * Must handle: Different PDF formats, scanned images
     * Must provide: Human review for uncertain extractions
     * Must maintain: Elena should be able to troubleshoot

   - Check if they caught the CONSTRAINTS:
     * Prefer free/low-cost
     * Minimal IT support
     * Needs to be maintainable by non-technical people

3. **Point out what they might have missed:**
   - "Did you capture the failed Zapier attempt? That tells us what NOT to do."
   - "Notice Marcus said '95%+ accuracy is acceptable' - that's crucial. We don't need perfection."
   - "See how Elena's burnout is mentioned? This isn't just about efficiency, it's about retention."

4. **Ask the critical question:**
   - "Based on these requirements, what's the CORE problem we're solving?"
   - Help them articulate: "We're eliminating manual data entry for invoice processing while maintaining accuracy and enabling scale."

5. **Transition:** "Perfect. Now let's define what 'done' looks like..."

---

## Defining "Done": Acceptance Criteria

Requirements tell you WHAT to build. Acceptance criteria tell you when you're FINISHED.

**Acceptance criteria are testable conditions that must be true for the automation to be considered complete.**

**Format:**
```
Given [precondition]
When [action happens]
Then [expected result]
```

**Examples for Invoice Automation:**

**Acceptance Criterion 1: PDF Processing**
```
Given: A standard digital PDF invoice in /invoices/ folder
When: The automation runs
Then:
- Invoice number is extracted with 95%+ accuracy
- Vendor name is extracted correctly
- Invoice date is extracted correctly
- Amount is extracted correctly
- Record is created in Airtable
```

**Acceptance Criterion 2: Error Handling**
```
Given: A scanned/blurry invoice PDF
When: The automation runs
Then:
- System flags the invoice for human review
- Record is created in Airtable with "Needs Review" status
- Elena receives a notification
- Original PDF is preserved
```

**Acceptance Criterion 3: Volume Handling**
```
Given: 25 invoices in the folder
When: The automation runs
Then:
- All 25 are processed within 5 minutes
- Success/failure count is logged
- Failed invoices are listed for review
```

**Why this matters:**

These criteria become your testing checklist. When you build the automation, you test against these EXACT conditions.

If it meets all criteria → DONE
If it doesn't → Keep building

**No ambiguity. No "I think it's done". Clear, testable conditions.**

---

## STOP: Write acceptance criteria for the invoice automation.

**Your task:**

Add a section to your `Invoice_Automation_Requirements.md` called "Acceptance Criteria"

Write at least 5 acceptance criteria using the Given/When/Then format.

Cover:
1. Happy path (perfect invoice)
2. Error case (bad PDF)
3. Volume (multiple invoices)
4. Data accuracy (correct extraction)
5. Integration (Airtable update)

**Be specific. Make them testable.**

---

USER: [Student writes acceptance criteria]

---

ACTION: When student completes this:

1. **Review their criteria:**
   - "Good. Let me see what you wrote."
   - Check if they're actually testable
   - Check if they cover success AND failure cases
   - Check if they're specific enough

2. **Improve if needed:**
   - "Make this more specific: 'System works correctly' is too vague. What does 'correctly' mean exactly?"
   - "Add a failure case: What happens if Airtable API is down?"
   - "Add an edge case: What if invoice has no date field?"

3. **Connect to testing:**
   - "These criteria are now your test plan."
   - "When you build the automation, you'll test each of these scenarios."
   - "If it passes all criteria, it's done. If not, you keep building."

4. **Transition:** "Great. Now we need to decide: what's the MVP vs. the full solution?"

---

## MVP vs. Full Solution: The Build Strategy

Here's a critical concept: **Don't try to build everything at once.**

**The mistake:**
"I'm going to build an automation that:
- Monitors the email inbox 24/7
- Downloads PDF attachments automatically
- Extracts all invoice data with AI
- Validates against vendor database
- Sends to Airtable
- Files in Google Drive
- Sends confirmation emails
- Generates weekly reports
- ...all in the first version"

**Why this fails:**
- Takes weeks to build
- Too many integration points
- Hard to debug
- If one piece breaks, everything breaks
- No early wins

**The better approach: MVP First**

**MVP = Minimum Viable Product**

The simplest version that delivers real value.

**For Invoice Automation, the MVP is:**

**MVP (Week 1):**
- Process PDFs from LOCAL folder (not email yet)
- Extract: invoice #, vendor, date, amount (core data only)
- Insert into Airtable
- Log successes and failures
- **Value:** Proves the PDF extraction works

**Phase 2 (Week 2):**
- Add Google Drive monitoring
- Automatically process new PDFs dropped in Drive
- Move processed files to "done" folder
- **Value:** Automation runs without manual trigger

**Phase 3 (Week 3):**
- Build web upload interface
- Let Elena upload PDFs directly
- Display extracted data for review
- **Value:** User-friendly interface, no file system access needed

**Full Solution (Week 4):**
- Connect to email inbox
- Auto-download attachments
- Send confirmation replies
- Generate reports
- **Value:** Fully automated end-to-end

**Why this progression works:**
1. **Fast feedback:** Show Marcus a working demo after Week 1
2. **Early value:** Elena can use MVP immediately (upload PDFs to folder)
3. **Incremental risk:** Each phase builds on proven foundation
4. **Flexible:** Can stop after Phase 2 if that's good enough
5. **Maintainable:** Each phase is a complete, working system

**The lesson: Build the smallest thing that delivers value, then expand.**

---

## STOP: Define your MVP.

**Your task:**

Add a section to your `Invoice_Automation_Requirements.md` called "Build Phases"

Define:

**MVP (Week 1):**
- What it does
- What it doesn't do yet
- Why this is valuable
- What you'll test

**Phase 2:**
- What you add
- Why this matters
- When you build this

**Phase 3 (Optional):**
- Future enhancements
- Nice-to-haves
- Might build later

**Be realistic. You're building the MVP in Lesson 2.2, so keep it SIMPLE.**

---

USER: [Student defines MVP and phases]

---

ACTION: When student completes this:

1. **Review their MVP scope:**
   - "Show me your MVP definition."
   - Check if it's actually minimal
   - Make sure it's achievable in one lesson
   - Verify it delivers real value

2. **Challenge if too ambitious:**
   - "This MVP is too big. Let's cut it down."
   - "Email integration is Phase 2, not MVP."
   - "Focus on: local folder → PDF extraction → Airtable. That's it."

3. **Challenge if too small:**
   - "If your MVP doesn't create Airtable records, Elena can't use it yet."
   - "Make sure the MVP delivers actual value, not just a proof of concept."

4. **Reinforce the principle:**
   - "MVP thinking is crucial. Most failed automations try to do too much."
   - "Build small, test fast, iterate based on real feedback."
   - "Marcus will be MORE impressed by a working MVP than by promises of a complex future system."

5. **Transition:** "Perfect. Now let's choose the technical approach..."

---

## Choosing Your Technical Approach

You have requirements. You have acceptance criteria. You have an MVP scope.

**Now: how do you actually build this?**

**Three main options:**

### Option 1: Python Script (Local Automation)
**What it is:** A Python script that processes files on your local machine

**Pros:**
- Fast to build
- Easy to debug
- Full control
- No external dependencies (besides libraries)
- Can run on-demand or scheduled

**Cons:**
- Requires Python installed
- Runs on one machine only
- Manual triggering (unless you set up cron)
- Not user-friendly for non-technical people

**Best for:** MVP, proof of concept, personal automation, batch processing

**Invoice automation fit:** ✅ Perfect for MVP

---

### Option 2: n8n Workflow (Visual Automation)
**What it is:** A visual workflow builder that connects services without code

**Pros:**
- Visual interface (easier for non-coders to understand)
- Built-in integrations with common services
- Can run in cloud or self-hosted
- Team members can modify workflows

**Cons:**
- Requires n8n account or server
- Limited flexibility vs. code
- Learning curve for workflow logic
- Can be expensive at scale (if using hosted version)

**Best for:** Multi-step automations, team collaboration, connecting APIs visually

**Invoice automation fit:** ✅ Good for Phase 2-3 (Google Drive monitoring)

---

### Option 3: Web Application (Hosted Tool)
**What it is:** A web app with user interface, deployed to a server

**Pros:**
- User-friendly interface
- Accessible from anywhere
- Can serve entire team
- Professional-looking tool
- No local software required

**Cons:**
- More complex to build
- Requires hosting (Vercel, Heroku, etc.)
- More to maintain
- Takes longer to develop

**Best for:** Tools used by multiple people, client-facing automation, polished deliverables

**Invoice automation fit:** ✅ Perfect for Phase 3 (web upload interface)

---

## The Decision Framework

**Ask these questions:**

1. **Who will use this?**
   - Just you? → Python script
   - Your team? → Web app
   - Non-technical people? → Web app or n8n

2. **How often does it run?**
   - On-demand? → Python script
   - Scheduled? → Python + cron or n8n
   - Real-time? → n8n or web app

3. **What systems does it integrate?**
   - Simple file processing? → Python script
   - Multiple APIs? → n8n or Python
   - User interaction needed? → Web app

4. **What's your timeline?**
   - Need it this week? → Python script
   - Need it polished? → Web app
   - Need it flexible? → n8n

5. **Who will maintain it?**
   - Just you? → Python script
   - Team? → Web app or n8n (more maintainable)
   - Non-technical team? → Web app

**For the invoice automation MVP:**

| Question | Answer | Implication |
|----------|--------|-------------|
| Who will use this? | Elena (initially), then you'll hand off | Start with script, build web app later |
| How often? | Daily, morning batch | Script with scheduling |
| What systems? | Files → Airtable (simple) | Python script handles this well |
| Timeline? | This week | Script is fastest |
| Who maintains? | You initially, then Elena | Web app for Phase 3 |

**Decision: Start with Python script for MVP, build web app in Phase 3.**

---

## STOP: Choose your technical approach.

**Your task:**

Add a section to your `Invoice_Automation_Requirements.md` called "Technical Approach"

Answer these questions:
1. What will you use for MVP? (Python script / n8n / web app)
2. Why did you choose that approach?
3. What will you use for Phase 2 and 3?
4. What tools/libraries will you need?

**Be specific about your reasoning. Show your thought process.**

---

USER: [Student chooses technical approach]

---

ACTION: When student completes this:

1. **Review their choice:**
   - "Show me what you chose and why."

2. **Validate if they chose Python script for MVP:**
   - "Perfect. Python script is the right call for MVP."
   - "Fast to build, easy to test, proves the concept."
   - "You can build this in Lesson 2.2."

3. **Challenge if they chose something complex:**
   - "Web app for MVP is too ambitious. That's Phase 3."
   - "n8n might work, but Python gives you more control for PDF parsing."
   - "Let's start simple, add complexity later."

4. **Discuss libraries they'll need:**
   - "For PDF parsing, you'll likely use PyPDF2 or pdfplumber"
   - "For Airtable, you'll use the requests library or pyairtable"
   - "Don't worry about installing these yet - Lesson 2.2 will guide you"

5. **Transition:** "Great. Now let's plan error handling..."

---

## Planning Error Handling (The Part Everyone Skips)

Here's the truth: **The difference between a toy automation and a production automation is error handling.**

**Toy automation:**
```python
pdf = read_pdf(file)
data = extract_data(pdf)
airtable.create(data)
print("Done!")
```

**Production automation:**
```python
try:
    pdf = read_pdf(file)
    if pdf is None:
        log.error(f"Could not read {file}")
        return

    data = extract_data(pdf)
    if data['amount'] is None:
        log.warning(f"Amount missing in {file}, flagging for review")
        data['status'] = 'Needs Review'

    result = airtable.create(data)
    if result.status_code == 200:
        log.info(f"Successfully processed {file}")
        move_to_processed_folder(file)
    else:
        log.error(f"Airtable API failed: {result.error}")

except Exception as e:
    log.critical(f"Unexpected error processing {file}: {str(e)}")
    notify_admin(file, error=e)
```

**The difference:**
- Handles file read failures
- Handles missing data
- Handles API failures
- Logs everything
- Notifies on critical errors
- Organizes processed files

**This is what Marcus needs.** Not code that works once on perfect data, but code that gracefully handles reality.

**Common errors in invoice automation:**

| Error Type | Cause | How to Handle |
|------------|-------|---------------|
| File not found | Wrong path, file moved | Check path exists, log error |
| PDF won't open | Corrupted file, wrong format | Try/except, flag for review |
| Data extraction fails | Scanned image, weird format | Return partial data, flag for review |
| Airtable API error | Rate limit, network issue, bad credentials | Retry with exponential backoff, log failure |
| Duplicate invoice | Already processed | Check before inserting, skip if exists |
| Missing required field | Invoice doesn't have date | Flag for manual review, log warning |

**Your error handling plan should address:**

1. **What can go wrong?** (List all failure modes)
2. **How do we detect it?** (Validation, try/except, status codes)
3. **How do we handle it?** (Retry? Skip? Flag? Notify?)
4. **How do we log it?** (What information do we capture?)
5. **How do we recover?** (Can we continue? Do we stop?)

---

## STOP: Plan your error handling.

**Your task:**

Add a section to your `Invoice_Automation_Requirements.md` called "Error Handling Plan"

Create a table with these columns:
- Error Type
- Cause
- Detection Method
- Handling Strategy
- Logging Approach

Include at least 5 common errors for the invoice automation.

**Think about reality. Think about what Marcus described. What WILL go wrong?**

---

USER: [Student creates error handling plan]

---

ACTION: When student completes this:

1. **Review their error plan:**
   - "Show me your error handling table."
   - Check if they covered the obvious failures
   - Check if their handling strategies are realistic

2. **Add what they missed:**
   - "What if Airtable API key is expired? Add that."
   - "What if a vendor sends a Word doc instead of PDF? Add that."
   - "What if Elena is processing the same file manually while your script runs? Add duplicate handling."

3. **Challenge vague strategies:**
   - "You said 'handle gracefully' - what does that mean specifically?"
   - "Define 'retry' - how many times? With what delay?"
   - "Be specific: 'Flag for review' means what exactly? Create record with 'Needs Review' status?"

4. **Emphasize the value:**
   - "This error handling plan is what makes your automation TRUSTWORTHY."
   - "Marcus tried automation before and it broke randomly. Yours won't, because you planned for failure."
   - "When (not if) something goes wrong, you'll have a plan."

5. **Transition:** "Perfect. Now let's talk about testing strategy..."

---

## Testing Strategy: How You Know It Works

**You can't just build it and hope it works.**

You need a testing strategy BEFORE you write code.

**The three testing stages:**

### Stage 1: Unit Testing (Does each piece work?)
**What:** Test individual functions in isolation

**For invoice automation:**
- Test PDF reading with sample PDFs
- Test data extraction with known invoices
- Test Airtable connection with dummy data
- Test each function independently

**How:**
- Use 3-5 sample invoices
- Include one perfect invoice, one messy one, one scanned image
- Verify extraction accuracy for each

**Success:** Each function works correctly with test data

---

### Stage 2: Integration Testing (Do the pieces work together?)
**What:** Test the full workflow end-to-end

**For invoice automation:**
- Put 5 invoices in /test_invoices/ folder
- Run the automation
- Verify all 5 are processed
- Check Airtable has 5 new records
- Verify data matches source PDFs

**How:**
- Use a test Airtable base (not production!)
- Process small batches (5-10 invoices)
- Verify success AND failure handling

**Success:** Entire workflow works, errors are handled gracefully

---

### Stage 3: Production Testing (Does it work with real data?)
**What:** Test with actual invoices in production environment

**For invoice automation:**
- Process today's invoices (15-25 real PDFs)
- Elena reviews output in Airtable
- Compare automated extraction vs. manual review
- Measure accuracy rate
- Identify edge cases you missed

**How:**
- Run alongside manual process first (don't replace immediately)
- Elena reviews every automated record
- Track accuracy metrics
- Fix issues found
- Gradually increase automation confidence

**Success:** 95%+ accuracy, Elena trusts the system, ready to go full automation

---

## The Testing Data You Need

**Before you build, gather test data:**

**Required:**
1. **5 sample invoices** representing different scenarios:
   - Perfect digital PDF (baseline)
   - Multi-page invoice (complexity)
   - Scanned/image-based PDF (challenging)
   - Unusual format (edge case)
   - Borderline unreadable (failure case)

2. **Expected output** for each invoice:
   - What SHOULD be extracted
   - Use this as your "answer key"

3. **Test Airtable base:**
   - Same structure as production
   - Use for testing without affecting real data

**In the course, these sample invoices are provided for you.** In real work, you'd get them from Marcus.

---

## STOP: Define your testing plan.

**Your task:**

Add a section to your `Invoice_Automation_Requirements.md` called "Testing Strategy"

For each testing stage, document:

**Unit Testing:**
- What you'll test
- What sample data you'll use
- What success looks like

**Integration Testing:**
- How you'll test the full workflow
- How many test invoices you'll use
- What you'll verify

**Production Testing:**
- How you'll roll out safely
- Who reviews the output
- How you measure success

**Be specific. This becomes your actual test plan when you build in Lesson 2.2.**

---

USER: [Student creates testing plan]

---

ACTION: When student completes this:

1. **Review their test plan:**
   - "Show me what you wrote."
   - Check if it's actually executable
   - Make sure they have clear success criteria

2. **Improve if needed:**
   - "Add a specific number: 'Test with 5 invoices' not 'test with multiple'"
   - "Define how you'll verify accuracy: manual comparison? percentage match?"
   - "Include Elena in production testing - she's your domain expert"

3. **Connect to MVP:**
   - "You'll execute this test plan in Lesson 2.2."
   - "Having this plan NOW means you'll know EXACTLY how to validate your work."
   - "No guessing 'is it done?' - you'll have clear pass/fail criteria."

4. **Transition:** "Excellent. Now let's create the implementation plan..."

---

## Creating the Implementation Plan

You have:
- ✅ Requirements
- ✅ Acceptance criteria
- ✅ MVP defined
- ✅ Technical approach chosen
- ✅ Error handling planned
- ✅ Testing strategy

**Now: break down the build into specific, actionable steps.**

**Implementation plan format:**

```markdown
## Step 1: Set Up Development Environment
- [ ] Install Python 3.8+
- [ ] Install required libraries (PyPDF2, requests)
- [ ] Set up project folder structure
- [ ] Create .env file for credentials
Time estimate: 30 minutes

## Step 2: Test Airtable Connection
- [ ] Get Airtable API token
- [ ] Create test base with Invoices table
- [ ] Write script to create test record
- [ ] Verify record appears in Airtable
Time estimate: 30 minutes

## Step 3: Build PDF Reader Function
- [ ] Write function to read PDF file
- [ ] Test with sample invoice
- [ ] Handle errors (file not found, corrupted PDF)
- [ ] Log successes and failures
Time estimate: 1 hour

## Step 4: Build Data Extraction Function
- [ ] Extract invoice number from PDF
- [ ] Extract vendor name
- [ ] Extract date and amount
- [ ] Return structured dictionary
Time estimate: 2 hours

[... continue for all major steps ...]
```

**Why this matters:**

Each step is:
- **Specific:** You know exactly what to do
- **Testable:** You know when it's done
- **Estimable:** You know how long it should take
- **Incremental:** Each step builds on the previous

**This plan becomes your roadmap in Lesson 2.2.**

---

## STOP: Create your implementation plan.

**Your task:**

Create a NEW document: `Invoice_Automation_Implementation_Plan.md`

Break down the MVP build into 8-12 specific steps.

For each step, include:
- **What to build**
- **How to test it**
- **Time estimate**
- **Success criteria**

**Start with environment setup, end with full integration test.**

**Use the CLAUDE.md patterns you defined in Lesson 1.7:**
- Absolute file paths
- .env for credentials
- Logging approach
- Error handling standards

**Take your time. This plan is what you'll follow in Lesson 2.2.**

---

USER: [Student creates implementation plan]

---

ACTION: When student completes this:

1. **Review their plan:**
   - "Show me your step breakdown."
   - Check if steps are specific enough
   - Make sure they're in logical order
   - Verify time estimates are realistic

2. **Improve if needed:**
   - "Break 'Build PDF Parser' into smaller steps - that's too vague"
   - "Add 'Test with sample invoice' after each component"
   - "Include logging from the start, not as an afterthought"
   - "Time estimates: first-time builds take longer than you think. Double them."

3. **Check against CLAUDE.md standards:**
   - "Does your plan include creating logs/ directory?"
   - "Are you using .env for the Airtable token?"
   - "Did you include error handling in each step?"

4. **Validate order:**
   - "You're testing Airtable connection in Step 2 - good. Get that working early."
   - "You're building PDF reader before extraction - perfect. One piece at a time."

5. **Set expectations:**
   - "This plan will take 4-6 hours to execute in Lesson 2.2."
   - "You might get stuck. That's normal. Refer back to this plan."
   - "Each step should work before you move to the next."

6. **Celebrate:**
   - "This is a real implementation plan. Professional quality."
   - "You could hand this to another developer and they'd know what to build."
   - "This is exactly how consulting firms plan automation projects."

7. **Transition:** "Excellent work. Now let's talk about setting up your development environment..."

---

## Setting Up Your Development Environment

**Before you can build in Lesson 2.2, you need your development environment ready.**

Let's set that up NOW, so Lesson 2.2 is pure building.

**What you need:**

### 1. Python 3.8 or higher
Check if you have it:
```bash
python3 --version
```

If not installed, download from python.org

---

### 2. Code editor
You're using OpCode or Claude Code, so you're covered.

---

### 3. Project folder structure
Create this structure:

```
/invoice-automation/
├── .env                    # API credentials (DO NOT COMMIT TO GIT)
├── invoices/              # Input folder (PDFs go here)
├── processed/             # Processed PDFs move here
├── logs/                  # Log files
├── scripts/               # Your Python scripts
│   └── process_invoices.py
├── test_data/             # Sample invoices for testing
└── README.md              # Documentation
```

---

### 4. Python libraries
You'll install these in Lesson 2.2, but know what you need:

```bash
pip3 install PyPDF2        # PDF parsing
pip3 install pdfplumber    # Alternative PDF parser
pip3 install requests      # API calls
pip3 install python-dotenv # Environment variables
```

---

### 5. Airtable account & test base
- Create free Airtable account (if you don't have one)
- Create a workspace called "Test Automations"
- Create a base called "Invoice Testing"
- Create a table called "Invoices" with these fields:
  - Invoice Number (single line text)
  - Vendor (single line text)
  - Invoice Date (date)
  - Amount (currency)
  - Status (single select: Received / Needs Review / Processed)

---

### 6. Sample invoices
In the course materials, you have 5 sample invoices in:
`/precision-manufacturing/current-data-samples/invoices/`

Copy these to your `/invoice-automation/test_data/` folder

---

## STOP: Set up your development environment NOW.

**Your task:**

Set up your development environment:

1. **Verify Python is installed** (python3 --version)
2. **Create project folder structure** (exactly as shown above)
3. **Create Airtable test base** (with Invoices table)
4. **Get Airtable API token:**
   - Go to https://airtable.com/create/tokens
   - Create new token
   - Give it access to your test base
   - Copy the token (starts with "pat...")
5. **Create .env file** with:
   ```
   AIRTABLE_TOKEN=pat...your_token_here...
   AIRTABLE_BASE_ID=app...your_base_id...
   ```
6. **Copy sample invoices** to test_data/ folder

**When done, reply with: "Environment ready"**

**Don't skip this. Lesson 2.2 assumes this is done.**

---

USER: [Student sets up development environment]

---

ACTION: When student says environment is ready:

1. **Verify they completed setup:**
   - "Great! Let me verify. Can you show me:"
   - "1. Output of `python3 --version`"
   - "2. Output of `ls -la` in your project folder (to see the structure)"
   - "3. Confirmation you have Airtable token (just say yes, don't share the token)"

2. **Troubleshoot if needed:**
   - If Python not installed: "Let's install Python. Are you on Mac, Windows, or Linux?"
   - If folder structure wrong: "Let me help you create the right structure..."
   - If Airtable issues: "Let's walk through creating the base step-by-step..."

3. **Verify .env file is NOT committed to git:**
   - "Important: Never commit your .env file with API tokens to git."
   - "Add .env to .gitignore if you haven't already."

4. **Celebrate:**
   - "Perfect. Your development environment is ready."
   - "In Lesson 2.2, you'll hit the ground running."
   - "Everything you need is set up."

5. **Transition:** "Now let's review what you've accomplished today..."

---

## What You Accomplished Today

Stop and look at what you created:

**You built:**
1. ✅ **Requirements document** - Clear understanding of the problem
2. ✅ **Acceptance criteria** - Testable definition of success
3. ✅ **MVP definition** - Scoped down to achievable first version
4. ✅ **Technical approach decision** - Clear plan for how to build
5. ✅ **Error handling plan** - Strategies for when things go wrong
6. ✅ **Testing strategy** - How you'll validate your work
7. ✅ **Implementation plan** - Step-by-step build roadmap
8. ✅ **Development environment** - Ready to start building

**This is automation design.**

Not coding. Not building. PLANNING.

**And it's the most valuable work you'll do on this project.**

Why? Because:
- You won't waste time building the wrong thing
- You won't get stuck wondering what to do next
- You won't discover major issues after building
- You won't deliver something Marcus can't use

**You planned like a professional.**

When consultants charge $10,000 for an automation project, THIS is where half the value comes from. Not the code - the DESIGN.

**You now have a complete specification for an automation you'll build in Lesson 2.2.**

---

## STOP: Final reflection.

**Answer these questions:**

1. How does having this detailed plan make you feel about building the automation?

2. What surprised you about the planning process?

3. If you'd just started coding without this planning, what problems would you have hit?

4. What's the most valuable part of the plan you created?

**Take a moment. This is a significant skill you just learned.**

---

USER: [Student reflects on planning process]

---

ACTION: When student responds:

1. **Acknowledge their feelings:**
   - If confident: "Good. That confidence comes from preparation. You know exactly what you're building."
   - If overwhelmed: "That's normal. Planning reveals complexity. But now you can tackle it piece by piece."
   - If excited: "Harness that excitement. You're about to build something real."

2. **Reinforce key insights:**
   - "The surprise many people have: planning takes time, but SAVES more time."
   - "Without this plan, you'd have built something, gotten stuck, restarted, and wasted days."
   - "WITH this plan, you'll build systematically and finish in one session."

3. **Highlight what they learned:**
   - "You learned requirements gathering"
   - "You learned acceptance criteria"
   - "You learned MVP thinking"
   - "You learned technical decision-making"
   - "You learned error handling planning"
   - "You learned testing strategy"
   - "These skills transfer to EVERY automation project."

4. **Set up next lesson:**
   - "In Lesson 2.2, you execute this plan."
   - "You'll write code, test with sample invoices, and build a working automation."
   - "It won't all work perfectly the first time. That's expected."
   - "But you'll have a plan to follow. You'll know what to build next."

5. **Give them the transition:**
   - "When you're ready to BUILD, open Lesson 2.2: Project 1 - PDF Invoice Processing"
   - "Bring your implementation plan. Bring your sample invoices. Bring your energy."
   - "You're going to turn Marcus's invoice nightmare into a working solution."
   - "See you there."

---

## Meta Skill: Systems Thinking & Design

**What you really learned today:**

How to design systems before building them.

This lesson wasn't about invoice processing. It was about:
- Breaking complex problems into requirements
- Defining success clearly
- Scoping work realistically
- Planning for failure
- Testing systematically
- Building incrementally

**The broader skill:** Design thinking for automation.

**This applies to:**
- Any automation project (not just invoices)
- Software development
- Process improvement
- Product design
- Consulting projects
- Business strategy

**The pattern is universal:**
1. Understand the problem deeply
2. Define success criteria
3. Choose the right approach
4. Plan for edge cases
5. Build incrementally
6. Test thoroughly

**You can use this framework for any automation opportunity.**

Whether you're:
- Automating sales data sync
- Building email response automation
- Creating report generation tools
- Designing data pipelines
- Building internal tools

**The planning process is the same.**

---

## Where Else This Applies

**Beyond automation:**

### In Consulting
- Client wants "automation" but doesn't know what
- You use this framework to define the project
- Requirements gathering = billable discovery phase
- Clear acceptance criteria = project success metrics
- MVP approach = fast time-to-value

### In Product Management
- Feature requests from users
- This framework defines the spec
- Acceptance criteria become user stories
- MVP thinking prevents over-building
- Testing strategy ensures quality

### In Operations
- Process improvement requests
- This framework scopes the work
- Requirements clarify the pain points
- MVP delivers quick wins
- Error handling ensures reliability

### In Freelancing
- Client has vague "can you build this?" request
- This framework creates a professional proposal
- Requirements = scope of work
- Acceptance criteria = deliverables
- Implementation plan = timeline & milestones

**The skill: turning ambiguity into actionable plans.**

---

## Success Criteria for Lesson 2.1

Before moving to Lesson 2.2, make sure you have:

- [ ] Completed requirements document with all 5 sections
- [ ] Written clear, testable acceptance criteria
- [ ] Defined MVP scope (and resisted scope creep)
- [ ] Chosen technical approach with justification
- [ ] Created error handling plan
- [ ] Documented testing strategy
- [ ] Built detailed implementation plan
- [ ] Set up development environment completely
- [ ] Understand why planning matters
- [ ] Feel ready to start building

**If you can check all those boxes, you're ready for Lesson 2.2.**

---

## What's Next: Lesson 2.2 Preview

**Lesson 2.2: Project 1 - PDF Invoice Processing**

You're going to BUILD the MVP automation.

**What you'll create:**
- Python script that processes invoice PDFs
- Extracts invoice #, vendor, date, amount
- Creates Airtable records
- Handles errors gracefully
- Logs all operations
- Processes batch of invoices

**You'll follow your implementation plan step-by-step.**

**You'll test with the sample invoices.**

**By the end, you'll have a WORKING automation.**

Not a tutorial. Not a demo. A real tool that processes real invoices.

**This is where you become a builder.**

---

## Before You Go

**Three things to remember:**

1. **Planning is not wasted time.** It's the most valuable time. It prevents waste.

2. **MVP thinking is crucial.** Don't try to build everything. Build the smallest valuable thing first.

3. **The plan guides the build.** When you get stuck in Lesson 2.2, refer back to your implementation plan.

**You're ready.**

You designed an automation from scratch. You planned professionally. You set up your environment.

**Now you build.**

---

**When you're ready to write code and create a working automation, open Lesson 2.2.**

**Welcome to the building phase.**

---

**End of Lesson 2.1 - Automation Design & Planning**

**Next:** Lesson 2.2 - Project 1: PDF Invoice Processing (Part A)

---

*The best code is the code you don't have to rewrite because you planned it right the first time.*
