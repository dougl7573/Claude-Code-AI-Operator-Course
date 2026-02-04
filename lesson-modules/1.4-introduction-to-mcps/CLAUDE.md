# Lesson 1.4: Introduction to MCPs (Model Context Protocol)

**Extending Claude Code's Superpowers**

---

## The Missing Tool Problem

It's Wednesday at Precision Manufacturing. You're in another meeting with Marcus from Finance.

> "So I get it - you can build this invoice automation. But here's the thing... our data is in Airtable. Like, ALL our data. Customers, invoices, products, everything. Can Claude Code even talk to Airtable? Or are we going to need to export CSVs every time we want data?"

Good question, Marcus.

You could write API calls manually. Import the `requests` library, handle authentication, parse JSON responses, deal with rate limits, debug error codes...

Or you could install an MCP.

**Two hours later**, you show Marcus the automation pulling data directly from Airtable, updating records in real-time, handling pagination automatically.

> "Wait. You just... installed something and now it works? Why didn't the last consultant do this?"

Because they didn't know about MCPs.

You do.

---

## What Are MCPs?

**MCP stands for Model Context Protocol.**

Think of MCPs as **plugins or extensions for Claude Code** - they give Claude new abilities to interact with tools, services, and platforms.

**Without MCPs:**
- Claude can read/write files on your computer
- Claude can run bash commands
- Claude can search the web
- That's it

**With MCPs:**
- Claude can interact with Airtable databases directly
- Claude can read/write Google Sheets
- Claude can browse GitHub repositories with specialized tools
- Claude can control Stripe accounts
- Claude can work with dozens of other services

**The key insight:** Instead of writing custom API integration code for every service, MCPs provide pre-built, optimized connections that Claude knows how to use.

---

## Why MCPs Matter for AI Operators

**Scenario 1: Without MCPs**

You need to sync data from Airtable to Google Sheets.

Your process:
1. Read Airtable API documentation (30 minutes)
2. Set up authentication tokens (15 minutes)
3. Write Python script to fetch data (45 minutes)
4. Handle pagination and rate limits (30 minutes)
5. Parse responses and format data (20 minutes)
6. Read Google Sheets API docs (30 minutes)
7. Set up OAuth authentication (45 minutes - ugh)
8. Write code to update sheets (30 minutes)
9. Debug authentication errors (60 minutes - why is OAuth like this?)
10. Test and verify (20 minutes)

**Total time:** 4-5 hours of work. Most of it is authentication and API boilerplate.

**Scenario 2: With MCPs**

You need to sync data from Airtable to Google Sheets.

Your process:
1. Install Airtable MCP (2 minutes)
2. Configure authentication (3 minutes)
3. Ask Claude to fetch data from Airtable (instant)
4. Ask Claude to write to Google Sheets (instant)
5. Test and verify (5 minutes)

**Total time:** 10 minutes of work. Claude handles all the API complexity.

**That's why MCPs matter.** They eliminate the grunt work and let you focus on the automation logic, not the plumbing.

---

## How MCPs Work (The Simple Explanation)

**Traditional approach:**
```
You → Write API code → Service API → Get data → Parse response → Use data
```

**MCP approach:**
```
You → Ask Claude → MCP handles everything → Get data
```

**What happens under the hood:**

1. You install an MCP (a pre-built integration package)
2. You configure it with credentials (API keys, tokens, etc.)
3. Claude Code automatically detects the MCP is available
4. You ask Claude to do something (e.g., "Get all records from Airtable table Customers")
5. Claude uses the MCP's functions to make the request
6. The MCP handles authentication, API calls, error handling, pagination
7. Claude receives clean data and works with it
8. You get results without writing API code

**You don't write API integration code. You just use the service through Claude.**

---

STOP: Let's make sure this concept is clear.

**Explain in your own words:**
1. What is an MCP?
2. Why would you use an MCP instead of writing API code yourself?
3. Can you think of a tool or service you use at work that you wish Claude could connect to directly?

---

USER: [Student explains MCPs in their own words]

---

ACTION: When student responds:

1. **Validate their understanding:**
   - If correct: "Exactly right. MCPs are like giving Claude new abilities to work with specific tools."
   - If partially correct: "You've got the idea. Let me clarify [specific point]..."
   - If confused: "Let me explain it differently. Think of MCPs like apps on your phone. Your phone can do basic stuff, but apps give it new capabilities..."

2. **Address the tool they mentioned:**
   - "That's a great example! Let's actually check if an MCP exists for [tool]."
   - If it exists: "Actually, there IS an MCP for that. You could install it and start using it immediately."
   - If not: "Good news - you could build a custom MCP for that, but that's advanced. For now, we'll focus on the common ones."

3. **Transition:** "Alright, let's look at some real MCPs you can actually use..."

---

## Popular MCPs for AI Operators

Here are the MCPs you'll encounter most often in automation work:

**Data & Databases:**
- **Airtable MCP** - Read/write Airtable bases and tables
- **Google Sheets MCP** - Manage spreadsheets programmatically
- **PostgreSQL/MySQL MCPs** - Connect to databases directly

**Project Management:**
- **GitHub MCP** - Browse repos, create PRs, manage issues
- **Linear MCP** - Manage tickets and projects
- **Notion MCP** - Read/write Notion pages and databases

**Payments & Billing:**
- **Stripe MCP** - Manage customers, subscriptions, invoices
- **QuickBooks MCP** - Accounting data access

**Communication:**
- **Slack MCP** - Send messages, read channels
- **Email MCPs** - Various email service integrations

**File Storage:**
- **Google Drive MCP** - Manage files in Drive
- **Dropbox MCP** - Access Dropbox files

**Specialized:**
- **Synta MCP** - Visual workflow builder (n8n integration) - OPTIONAL
- **Custom MCPs** - Build your own for niche services

**Where to find MCPs:**
- MCP documentation site (specific URLs vary)
- GitHub repositories
- Tool-specific documentation
- Community forums

---

## When to Use MCPs vs. Direct API Calls

**Use an MCP when:**
- An MCP exists for the service you need
- You need to interact with the service frequently
- Authentication is complex (OAuth, tokens, etc.)
- The API has pagination, rate limits, or other complexity
- You want Claude to handle the integration automatically

**Write direct API code when:**
- No MCP exists for your service
- You need extremely custom behavior
- The API is very simple (single endpoint, no auth)
- You're building a one-off script that won't be reused
- The MCP doesn't support the specific feature you need

**Real talk:** 90% of the time, use the MCP if one exists. Your time is valuable. Don't reinvent the wheel.

---

STOP: Decision time.

For the Precision Manufacturing invoice automation, you need to interact with Airtable (where all the company data lives).

**What would you do?**
A) Write custom Python code using the Airtable API
B) Install the Airtable MCP and let Claude handle it
C) Export Airtable to CSV manually every time

Explain your reasoning in 1-2 sentences.

---

USER: [Student chooses an approach]

---

ACTION: When student responds:

**If they chose B (MCP):**
- "Exactly right. The Airtable MCP will save you hours of API wrangling. Let's install it."

**If they chose A (API code):**
- "I get it - you want control and want to understand what's happening. That's admirable. But here's the thing: the MCP doesn't hide what's happening, it just handles the boilerplate. You can always look at the MCP's code if you want to understand it."
- "We're going to use the MCP because you're an AI Operator, not a Python developer. Your job is to build automations quickly, not to become an API expert."

**If they chose C (CSV):**
- "That's what the previous consultant did. It works... until someone forgets to export, or exports the wrong data, or exports but doesn't update it. Manual steps break automations."
- "We're going to use the MCP so the automation is truly automated."

**Then:** "Alright, let's install your first MCP. We'll start with Airtable since that's what Precision Manufacturing uses."

---

## Hands-On: Installing Your First MCP

**You're going to install the Airtable MCP.**

Why Airtable?
- Precision Manufacturing uses it for all their data
- It's free for small bases (you can test with your own)
- It teaches you the MCP installation pattern
- You'll use it in Module 2 for the invoice automation

**Before you start:**
- Make sure you have Claude Code installed and working
- You should have OpCode or your editor open
- Have your terminal ready

---

### Step 1: Check Available MCPs

First, let's see what MCPs are available in your Claude Code installation.

**Ask me:** "What MCPs are currently installed?"

I'll check your system and tell you what's already available.

---

USER: [Student asks about installed MCPs]

---

ACTION: When student asks:

1. **Check their MCP status:**
   - Use the ListMcpResourcesTool to see what MCPs are currently installed
   - List them clearly: "You currently have these MCPs installed: [list]"
   - If Airtable is already installed: "Great! Airtable MCP is already set up. Let's test it."
   - If not: "You don't have the Airtable MCP yet. Let's install it."

2. **Explain what you found:**
   - "MCPs are configured in your Claude Code settings. Each one needs credentials to connect to the service."

3. **Next step:** "Now let's [install/test] the Airtable MCP..."

---

### Step 2: Install the Airtable MCP

**Installation process:**

The exact installation steps depend on your operating system and Claude Code version, but the general pattern is:

1. **Open Claude Code settings**
   - Location varies by OS (check Claude Code docs)
   - Look for "MCP Configuration" or "Model Context Protocol"

2. **Add Airtable MCP configuration**
   - You'll need to specify the MCP package
   - Provide authentication credentials

3. **Get your Airtable credentials**
   - Go to Airtable.com
   - Create a free account if you don't have one
   - Generate a Personal Access Token
   - Find your Base ID (from the URL when you open a base)

4. **Configure the MCP**
   - Add your token and base ID to the configuration
   - Save the settings
   - Restart Claude Code if needed

**Detailed walkthrough:**

I'll guide you through this step-by-step based on your OS.

**Tell me:** What operating system are you using? (Mac, Windows, Linux)

---

USER: [Student shares OS and follows installation steps]

---

ACTION: When student responds:

1. **Provide OS-specific installation instructions**
   - Mac: "Open ~/Library/Application Support/Claude/..."
   - Windows: "Open %APPDATA%/Claude/..."
   - Linux: "Open ~/.config/claude/..."

2. **Walk through Airtable setup:**
   - "Go to airtable.com and sign in"
   - "Click your profile picture → Developer Hub → Personal Access Tokens"
   - "Create a new token with these permissions: [list required permissions]"
   - "Copy the token (you'll only see it once)"
   - "Open a base and grab the base ID from the URL: airtable.com/appXXXXXXXXXX/..."

3. **Guide MCP configuration:**
   - Show them where to add the configuration JSON
   - Explain each field clearly
   - Have them save and restart if needed

4. **Verify installation:**
   - "Now ask me: 'Can you access Airtable?'"
   - Test by trying to list available tables
   - Confirm it's working: "Perfect! The Airtable MCP is installed and working."

**If they get stuck:**
- Troubleshoot common issues (wrong path, malformed JSON, invalid token)
- Be patient and methodical
- Once working, celebrate: "Great! You just installed your first MCP. This is a skill you'll use constantly."

**Then:** "Now that it's installed, let me show you how powerful this is..."

---

### Step 3: Test the Airtable MCP

Now that the MCP is installed, let's actually use it.

**Test 1: List tables in your base**

Ask me: "What tables are in my Airtable base?"

I'll use the MCP to query your Airtable and tell you what tables exist.

**Test 2: Read data**

Pick a table (or create a simple one if your base is empty) and ask me: "Show me the first 5 records from [table name]"

I'll fetch the data and display it.

**Test 3: Write data**

Ask me: "Add a test record to [table name] with [some field values]"

I'll create a record using the MCP.

**What you're learning:**
- You're not writing API code
- You're just asking Claude to do things
- The MCP handles all the complexity
- This is how you'll work with Airtable in the invoice automation

---

USER: [Student tests the MCP functions]

---

ACTION: When student tests:

1. **Execute their requests using the MCP:**
   - Use mcp__airtable__list_tables to show tables
   - Use mcp__airtable__list_records to show data
   - Use mcp__airtable__create_record to add test data

2. **Show them the results:**
   - Display the data clearly
   - Point out how easy that was
   - "Notice: you didn't write a single line of API code. You just asked, and the MCP made it happen."

3. **Explain what happened behind the scenes:**
   - "When you asked me to [action], I used the Airtable MCP function [function name]"
   - "The MCP handled authentication, made the API call, parsed the response, and gave me clean data"
   - "You could have written 50+ lines of code to do the same thing"

4. **Transition:** "This is the power of MCPs. Now imagine doing this with Google Sheets, Stripe, GitHub, and dozens of other services..."

---

## Comparing MCP Usage to Manual API Calls

**Let's make this concrete.**

**Scenario:** Get all customers from an Airtable table and count how many are in California.

**Without MCP (manual API code):**

```python
import requests
import json

# Set up authentication
AIRTABLE_TOKEN = "your-token-here"
BASE_ID = "your-base-id"
TABLE_NAME = "Customers"

headers = {
    "Authorization": f"Bearer {AIRTABLE_TOKEN}",
    "Content-Type": "application/json"
}

# Fetch all records (handle pagination)
all_records = []
offset = None

while True:
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
    params = {"offset": offset} if offset else {}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        break

    data = response.json()
    all_records.extend(data.get("records", []))

    offset = data.get("offset")
    if not offset:
        break

# Count California customers
ca_count = 0
for record in all_records:
    fields = record.get("fields", {})
    if fields.get("State") == "California":
        ca_count += 1

print(f"California customers: {ca_count}")
```

**Time to write:** 20-30 minutes (if you know the API well)
**Lines of code:** ~35 lines
**Maintenance:** You own all error handling, rate limit management, etc.

---

**With MCP (Claude Code approach):**

**You ask me:** "How many customers in the Customers table are in California?"

**I respond:** "I'll check that for you."

[Uses MCP to fetch records, filters by state, counts results]

"There are 47 customers in California."

**Time to write:** 10 seconds (the time it took to ask)
**Lines of code:** 0 lines (you wrote nothing)
**Maintenance:** The MCP handles updates, errors, rate limits automatically

---

**That's a 100x productivity improvement.**

This is why AI Operators who know MCPs are so valuable. You build automations in minutes that would take developers hours.

---

STOP: Reflection point.

**Think about your current work:**

1. What's one repetitive task you do that involves data in a tool (Airtable, Sheets, database, etc.)?
2. If an MCP existed for that tool, how much time would it save you per week?
3. On a scale of 1-10, how excited are you about MCPs after seeing this?

---

USER: [Student reflects on MCP value for their work]

---

ACTION: When student responds:

1. **Engage with their specific task:**
   - "That's a perfect use case for MCPs!"
   - If MCP exists: "Actually, there IS an MCP for [tool]. You could automate that right now."
   - If not: "No MCP yet, but you could either: a) build one later, or b) use API calls for now"

2. **Quantify the time savings:**
   - If they say "5 hours/week": "That's 260 hours per year. That's six full work weeks. Imagine what you could do with that time."
   - Connect it to business value: "If your hourly rate is $50, that's $13,000 in saved time annually."

3. **Address excitement level:**
   - High (8-10): "I love it. This is what makes automation work feel like magic."
   - Medium (5-7): "Good. MCPs are powerful but they're just tools. What matters is WHAT you build with them."
   - Low (1-4): "Fair enough. MCPs might not seem exciting until you're building something real. Check back after Module 2."

4. **Transition:** "Alright, there's one more MCP I want to mention - but it's totally optional..."

---

## Optional: Synta MCP for Visual Workflows (n8n)

**Note:** This section is OPTIONAL. You do NOT need this for the course.

There's another MCP worth knowing about: **Synta MCP**.

**What is Synta MCP?**
- Connects Claude Code to n8n (a visual workflow automation tool)
- Lets you build automations with a drag-and-drop interface
- Alternative to writing code for complex workflows
- Good for non-developers or visual thinkers

**When you might use it:**
- You prefer visual workflow builders over code
- You're building complex multi-step automations
- You want to hand off workflows to non-technical team members
- You need to quickly prototype automation logic

**When you DON'T need it:**
- You're comfortable with code-based automations (the default in this course)
- You're building simple scripts
- You want full control over every detail
- You prefer working in code

**The truth:** Most AI Operators use a mix. Code for simple automations, visual tools like n8n for complex workflows with many steps and conditions.

**For this course:** We're focusing on code-based automations primarily. That's what you'll use in Module 2. But if you want to explore Synta/n8n later, the skills you learn here transfer directly.

**Resources:**
- Synta MCP docs: https://mcp-docs.synta.io/installation
- n8n documentation: n8n.io
- OpCode: https://opcode.sh/

**Should you install it now?** No. Focus on Airtable MCP first. You can explore Synta later if you want.

---

## MCP Discovery and Installation Pattern

**You just learned the pattern for working with MCPs. Here it is explicitly:**

**Step 1: Identify the need**
- "I need to interact with [service]"
- Example: "I need to read data from Google Sheets"

**Step 2: Check if an MCP exists**
- Search for "[service] MCP"
- Check MCP documentation sites
- Ask me: "Is there an MCP for [service]?"

**Step 3: Install and configure**
- Follow installation instructions for your OS
- Get credentials from the service (API keys, tokens, OAuth)
- Add configuration to Claude Code settings
- Restart if needed

**Step 4: Test the MCP**
- Ask me to perform a simple action
- Verify it works
- Troubleshoot if needed

**Step 5: Use it in automation**
- Build your automation using the MCP
- No API code needed - just ask me to interact with the service

**You'll use this pattern constantly as an AI Operator.**

Every new service you need to integrate? Follow this pattern. In 5-10 minutes, you'll have it working.

---

## MCP Best Practices for AI Operators

**1. Always use MCPs when available**
Don't write custom API code if an MCP exists. Your time is valuable.

**2. Configure MCPs once, use them forever**
Set up your MCPs properly and they'll work across all your automations.

**3. Secure your credentials**
Store API tokens securely. Don't hardcode them in scripts. Use environment variables.

**4. Test MCPs before building automations**
Make sure the MCP works before you build a complex automation that depends on it.

**5. Know when to skip MCPs**
If you need very custom behavior or the MCP doesn't support your use case, write API code.

**6. Document which MCPs your automation uses**
When you hand off an automation, document the required MCPs so others can set them up.

**7. Keep MCP configurations backed up**
If you configure 10 MCPs, back up that configuration file. Don't lose hours of setup work.

---

STOP: Let's test your understanding of the full MCP workflow.

**Scenario:** You need to build an automation that:
1. Reads new customer data from a Google Sheet
2. Creates customer records in Airtable
3. Sends a welcome email via an email service

**Questions:**
1. What MCPs would you need for this automation?
2. How would you approach setting this up? (Describe the steps)
3. What would you do first to verify the automation could work?

---

USER: [Student outlines their approach]

---

ACTION: When student responds:

1. **Evaluate their MCP selection:**
   - Correct: "Google Sheets MCP, Airtable MCP, and an Email MCP (like Gmail or SendGrid)"
   - If they missed one: "Don't forget [MCP]. You need it for [step]."
   - If they suggested API code: "You COULD write API code, but why? The MCP does it in seconds."

2. **Evaluate their setup approach:**
   - Good approach: "Exactly. Install each MCP, configure credentials, test individually, then chain them together."
   - Missing steps: "Good start. I'd also [add missing step]."
   - Unclear: "Let me show you how I'd approach it: [outline clear steps]"

3. **Evaluate their verification plan:**
   - Good answer: "Perfect. Test each MCP independently before building the full workflow."
   - Missing testing: "Remember: test early, test often. Don't build the whole automation and THEN discover one MCP doesn't work."

4. **Reinforce the pattern:**
   - "This is exactly how you'll approach automation projects: identify services needed → find/install MCPs → test → build."
   - "You just demonstrated the AI Operator mindset."

5. **Transition:** "Alright, you understand MCPs. Let's wrap this up with the key takeaways..."

---

## Meta Skill: Leveraging Existing Tools vs. Building from Scratch

**What you're really learning in this lesson:**

The difference between "I'll build it" and "I'll use what exists."

Junior developers want to build everything from scratch. They want to prove they can code the solution.

Senior developers know that using existing, well-maintained tools is smarter. They've been burned by maintaining custom code.

**AI Operators think like senior developers:** Use what exists. Build only what's unique to your use case.

**MCPs are the perfect example:**
- Someone already built the Airtable integration
- It's maintained, tested, optimized
- You don't need to build it again
- You just need to use it

**This mindset applies beyond MCPs:**
- Use existing Python libraries instead of writing functions from scratch
- Use SaaS tools instead of building custom software
- Use templates instead of starting from blank pages
- Use frameworks instead of building architecture

**The meta skill:** Knowing when to build vs. when to use existing solutions.

**For AI Operators:** Almost always use existing solutions. Your value is in identifying opportunities and assembling solutions quickly, not in building infrastructure from scratch.

---

## Where Else This Applies

**Beyond this course, the MCP concept applies to:**

**In Software Development:**
- Using libraries and packages instead of writing utilities
- Leveraging APIs instead of building services
- Using frameworks instead of custom architecture

**In Business Operations:**
- Using Zapier/Make/n8n instead of custom automation scripts
- Using SaaS tools instead of building software
- Using templates instead of creating from scratch

**In Consulting:**
- Using proven methodologies instead of inventing new ones
- Using existing tools and integrations to deliver faster
- Building on platforms clients already use

**In AI/Automation Work:**
- Using Claude Code + MCPs instead of learning to code
- Using no-code tools where appropriate
- Using AI to augment, not replace, existing workflows

**The principle:** Stand on the shoulders of giants. Don't reinvent wheels.

MCPs embody this principle perfectly.

---

## Success Criteria for Lesson 1.4

Before moving to Lesson 1.5, make sure you can check these off:

- [ ] I understand what MCPs are (plugins for Claude Code)
- [ ] I know why MCPs matter for AI Operators (eliminate API boilerplate)
- [ ] I've installed at least one MCP (Airtable or another)
- [ ] I've tested the MCP by asking Claude to interact with the service
- [ ] I understand the MCP installation pattern (identify, install, configure, test, use)
- [ ] I know when to use MCPs vs. writing API code
- [ ] I can explain MCPs in my own words
- [ ] I know about Synta MCP (optional visual workflows) but understand it's not required
- [ ] I'm ready to use MCPs in the invoice automation project

**If you can check all those boxes, you're ready for Lesson 1.5.**

---

STOP: Final reflection.

**Tell me:**
1. Before this lesson, had you heard of MCPs? If yes, where?
2. What's one automation you could build NOW using the Airtable MCP you installed?
3. What's one question you still have about MCPs?

Be honest. If something's unclear, ask now.

---

USER: [Student reflects and asks final questions]

---

ACTION: When student responds:

1. **Address their prior knowledge:**
   - If they knew about MCPs: "Great! This lesson should have deepened your understanding of when and how to use them."
   - If they didn't: "Perfect. You just learned something that many developers don't even know about yet."

2. **Engage with their automation idea:**
   - "That's a perfect use case! [Specific feedback on their idea]"
   - If it's feasible: "You could literally build that in the next hour if you wanted to."
   - If it's complex: "That's ambitious. Break it down into smaller steps and start with the simplest version."
   - Encourage them: "Hold onto that idea. After you finish the course, build it."

3. **Answer their question thoroughly:**
   - Take time to address any confusion
   - Provide examples if needed
   - Make sure they understand before moving on

4. **Transition to next lesson:**
   - "Excellent. You now understand how to extend Claude Code's capabilities with MCPs."
   - "In Lesson 1.5, we're going to talk about another powerful feature: Agents."
   - "Agents let you run multiple Claude instances in parallel, researching different things simultaneously. Imagine investigating 5 API documentation sites at once instead of one at a time."
   - "It's like having a team of researchers working for you."
   - "Ready? Open Lesson 1.5 when you are."
   - "See you there."

---

## Additional Resources

**MCP Documentation:**
- Official MCP documentation: [check latest sources]
- Community MCP directory: [search for updated lists]
- GitHub repos for popular MCPs

**Tutorials:**
- Airtable API basics (if you want to understand what the MCP does under the hood)
- Google Sheets API documentation
- Authentication patterns for common services

**Practice Projects:**
- Build a simple "Airtable to Google Sheets" sync
- Create a customer directory from Airtable data
- Pull data from Airtable and generate a report

**But remember:** Don't get lost in reading. Your goal is to DO.

The best way to learn MCPs is to use them in a real project. You'll do that in Module 2.

---

## Looking Ahead: MCPs in the Invoice Automation

**In Module 2, you'll build the PDF invoice automation.**

The automation will:
1. Extract data from PDF invoices (invoice #, vendor, date, amount)
2. **Use the Airtable MCP to insert records automatically**
3. Handle errors and log results

Without the Airtable MCP, step 2 would require 50+ lines of API code.

With the MCP, it's one request to Claude.

You just saved hours of development time and made your automation easier to maintain.

**That's the power of MCPs.**

---

**End of Lesson 1.4**

**Next:** Lesson 1.5 - Agents & Parallel Processing

---

*Don't build what already exists. Use MCPs. Build what's unique to your problem.*
