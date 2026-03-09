# Lesson 2.6: GitHub Portfolio & Version Control

**Your Automations Deserve a Home**

---

## The Missing Piece

It's Thursday afternoon. You're sitting at your desk at Precision Manufacturing with a sense of satisfaction. Over the past few weeks, you've built:

- A PDF invoice processor that extracts data and sends it to Airtable
- A Google Drive automation that watches for new invoices
- A web app that the Finance team can use to upload invoices manually

Three working automations. Real code. Real business value.

Then Marcus from Finance stops by your desk.

> "Hey, quick question. My laptop died yesterday and IT gave me a new one. Can you send me that invoice processor script again? And also... where's the instructions for setting it up? I want to show Janet in Accounts Payable how to run it if I'm out sick."

You realize something important: **Your automations only exist on your laptop.**

No backup. No documentation in one place. No way for others to access it. If your laptop died tomorrow, weeks of work would vanish.

There's a name for this in software: **a single point of failure.**

You need version control. You need GitHub.

---

## What This Lesson Is Really About

Here's what we're doing today: **Creating a professional portfolio that backs up your work and makes it shareable.**

By the end of this lesson, you'll have:
- A repository with ALL your automation code organized professionally
- Professional documentation that explains what you built
- A shareable link you can send to employers, clients, or colleagues
- A portfolio that shows real, working automations

**Important:** You already set up GitHub and deployed your web app in Lesson 2.5. This lesson is about organizing ALL your automations into a professional portfolio.

**What you'll learn:**
- Organizing multiple projects in one repository
- Writing professional READMEs
- Committing your automation files
- Making your work shareable and portfolio-ready

---

**Quick check:** You should already have GitHub set up and authenticated from Lesson 2.5. If not, go back and complete that lesson first.

Let's verify you're good to go:

```bash
gh auth status
```

You should see checkmarks showing you're logged in. If not, run `gh auth login` and follow the prompts (covered in Lesson 2.5).

---

## Creating Your Portfolio Repository

In Lesson 2.5, you pushed your web app to GitHub as a single project. Now we're creating a **portfolio repository** that organizes ALL your automations in one place.

**Why a portfolio repo?**
- Shows the full scope of what you built (not just one project)
- Professional presentation for employers or clients
- Central documentation hub
- Easy to share one link that shows everything

A repository (or "repo") is basically a project folder on GitHub. We'll create one specifically for your Precision Manufacturing portfolio.

---

STOP: Create the portfolio repository.

**We're going to create a new folder, initialize it as a portfolio project, and then we'll push it to GitHub after we've added everything.**

**In your terminal:**

1. **Navigate to where you keep your projects:**
   ```bash
   cd ~/Documents
   ```
   (Or wherever you prefer)

2. **Create the portfolio folder:**
   ```bash
   mkdir precision-manufacturing-automations
   cd precision-manufacturing-automations
   ```

3. **Initialize git:**
   ```bash
   git init
   ```

4. **Create a placeholder README:**
   ```bash
   echo "# Precision Manufacturing Automations" > README.md
   ```

**Tell me when you've done this.**

---

USER: [Student creates the folder]

---

ACTION: When student responds:

- "Perfect! You now have a local project folder ready for your automations."
- "We'll add files, write documentation, and push it all to GitHub at the end."
- "Let's start by organizing your automation files."

---

## Adding Your Automation Files

Time to move your automations into this repository. We'll organize them logically.

---

STOP: Create the folder structure.

**In your terminal (make sure you're in the `precision-manufacturing-automations` folder):**

```bash
mkdir -p automations/invoice-processor
mkdir -p automations/drive-automation
mkdir -p automations/invoice-webapp
mkdir -p sample-data
```

**This creates a clean structure:**
```
precision-manufacturing-automations/
├── README.md
├── automations/
│   ├── invoice-processor/
│   ├── drive-automation/
│   └── invoice-webapp/
└── sample-data/
```

**Verify it worked:**
```bash
ls -R
```

**Tell me when you've created the folders.**

---

USER: [Student creates folders]

---

ACTION: When student responds:

1. **Confirm success:**
   - "Great! Your repository now has a logical structure."
   - "This makes it easy for others (and future you) to navigate."

2. **Next step:**
   - "Now let's copy your actual automation files into these folders."

---

STOP: Copy your automation files.

**Find your existing automation files** (the ones you built in previous lessons).

**Copy them into the appropriate folders:**

**For the invoice processor:**
```bash
cp /path/to/your/invoice_processor.py automations/invoice-processor/
```

**For the Google Drive automation:**
```bash
cp /path/to/your/drive_invoice_watcher.py automations/drive-automation/
```

**For the web app:**
```bash
cp -r /path/to/your/webapp-folder/* automations/invoice-webapp/
```

**Sample data (if you have test invoices):**
```bash
cp /path/to/sample-invoices/*.pdf sample-data/
```

**Note:** Adjust the paths to match where YOUR files actually are.

**Important:** Do NOT copy files with API keys or sensitive credentials. If your code has hardcoded keys, we'll address that next.

**Tell me when you've copied your files.**

---

USER: [Student copies files]

---

ACTION: When student responds:

**If they copied files successfully:**
- "Perfect! Let's verify everything's there."
- "Run: `ls -R` to see all files"
- "You should see your Python scripts, web app files, etc."

**If they have API keys in files:**
- "STOP. Before we commit these files, we need to handle API keys."
- "You should NEVER put API keys in public GitHub repositories."
- "Let's create a .env file approach and update your scripts."
- Walk them through:
  1. Creating a `.env.example` file (without real keys)
  2. Adding `.env` to `.gitignore`
  3. Updating scripts to read from environment variables
  4. "I can help you update the scripts if you share which files have hardcoded keys"

**Once files are safely added:**
- "Great! Now let's check what git sees."

---

## Understanding Git Status

Before we save (commit) anything, let's see what git is tracking.

---

STOP: Check git status.

**Run this command:**
```bash
git status
```

**What you'll see:**
- Files in red under "Untracked files" - these are new files git doesn't know about yet
- This should include your automation files, folders, etc.

**This is normal!** Git sees the files but hasn't started tracking them.

**Tell me what you see in the output.**

---

USER: [Student runs git status]

---

ACTION: When student responds:

1. **Explain what they're seeing:**
   - "The red files are 'untracked' - git sees them but isn't saving their history yet."
   - "We need to 'add' them to the staging area, then 'commit' them."

2. **Explain the git workflow:**
   - **Working Directory:** Where you edit files (what you just did)
   - **Staging Area:** Where you prepare files for saving (`git add`)
   - **Repository:** Where files are permanently saved (`git commit`)
   - "Think of it like: Edit → Prepare → Save"

3. **Visual explanation:**
   ```
   Working Directory  →  Staging Area  →  Repository  →  GitHub
   (your files)          (git add)        (git commit)   (git push)
   ```

4. **Next step:**
   - "Now let's add these files to the staging area."

---

## Creating a .gitignore File

Before we commit, let's tell git to ignore certain files (like API keys, temporary files, etc.).

---

STOP: Create a .gitignore file.

**In your terminal, create a .gitignore file:**

```bash
nano .gitignore
```

**Add these lines:**
```
# Environment variables (API keys, secrets)
.env
*.env
credentials.json

# Python
__pycache__/
*.pyc
*.pyo
venv/
env/

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Logs
*.log
```

**Save and exit:**
- Press `Ctrl+O` (save)
- Press `Enter` (confirm filename)
- Press `Ctrl+X` (exit)

**Verify it was created:**
```bash
cat .gitignore
```

**This tells git to never track these files.** API keys, temporary files, etc. won't accidentally get committed.

**Tell me when you've created the .gitignore file.**

---

USER: [Student creates .gitignore]

---

ACTION: When student responds:

1. **Confirm success:**
   - "Perfect! Now git will ignore sensitive files."
   - "This is a critical safety step."

2. **Explain why this matters:**
   - "If you accidentally committed API keys to GitHub, anyone could see them."
   - "The `.gitignore` file prevents this from happening."
   - "It's like a blacklist for git."

3. **Next step:**
   - "Now let's stage all your files for commit."

---

## Staging Your Files (git add)

Time to tell git which files to save.

---

STOP: Add files to staging area.

**Run this command:**
```bash
git add .
```

**What this does:**
- The `.` means "add everything in the current folder"
- Git will stage all files except those in .gitignore
- Files are now ready to be committed

**Check the status:**
```bash
git status
```

**Now you should see:**
- Files in green under "Changes to be committed"
- These are staged and ready to save

**Tell me what you see.**

---

USER: [Student runs git add]

---

ACTION: When student responds:

**If files are green:**
- "Perfect! Your files are staged."
- "Green means 'ready to commit'."
- "These are the files that will be saved in the next step."

**If they still see red files:**
- "That's fine. Red files are either:
  - In .gitignore (like .env) - intentionally ignored
  - Or not in the current directory
- Run `git status` again and tell me which files are red"

**If everything looks good:**
- "Now for the important part: creating your first commit."

---

## Creating Your First Commit

A commit is a save point. Think of it like a snapshot of your project at this moment.

---

STOP: Create your first commit.

**Run this command:**
```bash
git commit -m "Initial commit: Add invoice processing automations

- PDF invoice processor (local script)
- Google Drive automation
- Invoice upload web app
- Sample data for testing
- Documentation in README"
```

**About commit messages:**
- The `-m` flag means "message"
- First line is the summary (keep it short)
- Blank line, then details (optional)
- Good commit messages explain WHAT you changed and WHY

**What you'll see:**
- A summary of files changed
- Number of insertions
- Commit hash (a unique ID for this save point)

**Tell me when the commit completes.**

---

USER: [Student creates first commit]

---

ACTION: When student responds:

**If successful:**
- "Congratulations! You just created your first commit."
- "Your automations are now saved in git's history."
- "But they're still only on your computer. Next, we push to GitHub."

**If they got an error:**
- Common error: "Please tell me who you are"
  - "You need to configure git first. Run:"
  - `git config --global user.name "Your Name"`
  - `git config --global user.email "your@email.com"`
  - "Then try the commit again"

**Once successful:**
- "Now let's push this commit to GitHub so it's backed up and shareable."

---

## Pushing to GitHub

Time to upload everything to GitHub. Since you already set up the `gh` CLI in Lesson 2.5, this is one command.

---

STOP: Push to GitHub.

**Run this command:**
```bash
gh repo create precision-manufacturing-automations --public --source=. --remote=origin --push
```

**What this single command does:**
- Creates a new repository on your GitHub account
- Sets it as public (good for portfolio)
- Connects your local folder to GitHub
- Pushes all your code up

**You should see:**
```
✓ Created repository your-username/precision-manufacturing-automations on GitHub
✓ Added remote origin
✓ Pushed commits to origin/main
```

**Now open it in your browser:**
```
https://github.com/your-username/precision-manufacturing-automations
```

**Tell me what you see on GitHub.**

---

USER: [Student pushes to GitHub and views repository]

---

ACTION: When student responds:

**If successful:**
- "YES! Look at that. Your automations are now on GitHub!"
- "You should see:
  - All your folders (automations/, sample-data/)
  - All your files
  - Your commit message
  - When it was last updated"
- "Your work is backed up. If your laptop dies, this is all safe."

**If they got "repository already exists":**
- "You already have a repo with that name. Either use a different name:"
- `gh repo create pm-automations-portfolio --public --source=. --remote=origin --push`
- "Or delete the old one on GitHub.com (Settings → Danger Zone → Delete)"

**If authentication error:**
- "Run `gh auth status` to check if you're still logged in."
- "If not, run `gh auth login` again (same process from Lesson 2.5)."

**Once successful:**
- "Now comes the most important part: documentation. We need to write a README that explains what this project is."

---

## Writing a Professional README

Your README.md is the first thing people see. It's your project's homepage. Let's make it professional.

---

STOP: Write your README.

**In your terminal:**
```bash
nano README.md
```

**Replace the contents with this template** (customize for your project):

```markdown
# Precision Manufacturing Invoice Automations

**Automated invoice processing system built with Python and Claude Code**

This repository contains three invoice processing automations built for Precision Manufacturing Co.'s Finance department, eliminating 2+ hours of manual data entry per day.

## 🎯 Project Overview

These automations extract invoice data (invoice number, vendor, date, amount) from PDF files and automatically sync to Airtable, replacing a manual process that was taking 10-15 hours per week.

**Built with:** Python, Airtable API, Google Drive API, Vercel

**Impact:**
- ⏱️ Saves 2+ hours/day for Finance team
- ✅ 95%+ accuracy in data extraction
- 🚀 Fully automated workflow from upload to database

## 📁 What's Included

### 1. Invoice Processor (Local)
**Location:** `automations/invoice-processor/`

A Python script that processes PDF invoices from a local folder and sends extracted data to Airtable.

**Usage:**
```bash
python invoice_processor.py
```

**Features:**
- Extracts invoice number, vendor, date, amount
- Handles multiple invoice formats
- Logs all processing activity
- Error handling for malformed PDFs

### 2. Google Drive Automation
**Location:** `automations/drive-automation/`

A scheduled script that watches a Google Drive folder for new invoices and automatically processes them.

**Usage:**
```bash
python drive_invoice_watcher.py
```

**Features:**
- Monitors Drive folder in real-time
- Auto-processes new uploads
- Moves processed files to archive
- Email notifications on errors

### 3. Invoice Upload Web App
**Location:** `automations/invoice-webapp/`

A web application where Finance team members can manually upload invoices for processing.

**Live Demo:** [Your Vercel URL]

**Features:**
- Drag-and-drop PDF upload
- Real-time data extraction preview
- Manual review/edit before saving
- One-click save to Airtable

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8+
- Airtable account (free tier works)
- Google Cloud account (for Drive automation)

### Installation

1. **Clone this repository:**
```bash
git clone https://github.com/your-username/precision-manufacturing-automations.git
cd precision-manufacturing-automations
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables:**

Create a `.env` file in the project root:
```
AIRTABLE_API_KEY=your_api_key_here
AIRTABLE_BASE_ID=your_base_id_here
AIRTABLE_TABLE_NAME=Invoices
GOOGLE_DRIVE_CREDENTIALS=path/to/credentials.json
```

4. **Run the local processor:**
```bash
python automations/invoice-processor/invoice_processor.py
```

## 📊 Technical Details

**Invoice Data Extraction:**
- Uses PDF parsing library to extract text
- Pattern matching for invoice fields
- Fallback extraction methods for edge cases

**Airtable Integration:**
- REST API for data insertion
- Duplicate detection by invoice number
- Automatic timestamp tracking

**Google Drive Integration:**
- OAuth 2.0 authentication
- Webhook-based file monitoring
- Automatic file organization

## 📝 Process Documentation

**See the full process documentation:** `CLAUDE.md`

This file contains the automation playbook - all the context, decisions, and lessons learned while building these automations.

## 🛠️ Built With

- **Python** - Core automation logic
- **Airtable API** - Database storage
- **Google Drive API** - File monitoring
- **Claude Code** - AI-assisted development
- **Vercel** - Web app deployment

## 📈 Results

**Before Automation:**
- 20+ invoices processed manually each day
- 10-15 hours per week spent on data entry
- Frequent data entry errors
- Invoices lost in email threads

**After Automation:**
- 100% of invoices processed automatically
- ~2 minutes of review time per day
- <1% error rate
- All invoices tracked in Airtable

## 🤝 Contributing

This is a portfolio project demonstrating AI Operator skills. While not actively maintained, feel free to fork and adapt for your own use cases.

## 📫 Contact

**Your Name** - [Your LinkedIn] - [Your Email]

Project Link: [https://github.com/your-username/precision-manufacturing-automations](https://github.com/your-username/precision-manufacturing-automations)

---

*Built as part of the Claude Code for AI Operators course*
```

**Customize this template:**
- Replace "Your Name" with your actual name
- Add your LinkedIn/email
- Add your actual Vercel URL (if deployed)
- Adjust the impact numbers if different

**Save and exit:**
- `Ctrl+O`, `Enter`, `Ctrl+X`

**Tell me when you've customized and saved the README.**

---

USER: [Student writes README]

---

ACTION: When student responds:

1. **Review their README:**
   - "Great! Let's look at what you wrote."
   - `cat README.md` to display it
   - "This is the first thing people see when they visit your GitHub repo."

2. **Feedback on README:**
   - "A good README has:
     - Clear project title
     - What problem it solves
     - What's included
     - How to use it
     - Setup instructions
     - Results/impact"
   - "Yours should cover all of these now."

3. **Next step:**
   - "Now we commit and push this updated README to GitHub."

---

## Committing Your README

One more commit cycle to save your documentation.

---

STOP: Commit and push your README.

**Run these commands:**

```bash
git add README.md
git commit -m "Add comprehensive project documentation

- Overview of all three automations
- Setup instructions
- Technical details
- Impact metrics
- Contact information"
git push origin main
```

**Then refresh your GitHub repository page in your browser.**

**Tell me what you see now.**

---

USER: [Student commits and pushes README]

---

ACTION: When student responds:

**If successful:**
- "Look at that! Your README is now beautifully displayed on your GitHub homepage."
- "Anyone who visits your repo can now understand:
  - What you built
  - Why it matters
  - How to use it
  - How to contact you"
- "This is a professional portfolio piece."

**Celebrate this moment:**
- "You now have:
  - ✅ Working automations backed up to GitHub
  - ✅ Professional documentation
  - ✅ A shareable link
  - ✅ Portfolio evidence of your skills
  - ✅ Protection against laptop failure"

**Then say:**
- "Let's add one more important file: your CLAUDE.md automation playbook."

---

## Adding Your CLAUDE.md Playbook

You've been building automations for weeks. You've learned patterns, made decisions, hit roadblocks. That knowledge should be documented.

The CLAUDE.md file is your automation playbook - it captures:
- Why you built what you built
- Decisions you made along the way
- Lessons learned
- Common issues and solutions
- How to extend the automations

This isn't for end users. This is for you (future you), other AI operators, or anyone maintaining these automations.

---

STOP: Create your CLAUDE.md file.

**In your terminal:**
```bash
nano CLAUDE.md
```

**Here's a template to get started:**

```markdown
# Automation Playbook - Precision Manufacturing Invoices

**AI Operator Guide for maintaining and extending these automations**

---

## 🎯 Project Context

### The Problem
Precision Manufacturing's Finance department was manually processing 20+ invoice PDFs daily:
- Opening each PDF
- Copying data to Excel
- Transferring to Airtable
- 10-15 hours per week of manual work
- Frequent data entry errors

### The Solution
Three integrated automations that handle the entire invoice workflow:
1. Local processor (for batch processing)
2. Google Drive automation (for ongoing daily processing)
3. Web app (for ad-hoc uploads)

### Why This Approach
- Started simple (local script) to prove value quickly
- Added cloud automation once Finance trusted the system
- Built web app for edge cases and training
- Progressive complexity = progressive buy-in

---

## 🔧 Technical Decisions

### Why Python?
- Finance team had some Python knowledge
- Rich library ecosystem (PDF parsing, API clients)
- Easy to schedule and automate
- Claude Code handles Python well

### Why Airtable?
- Finance was already using it
- Free tier sufficient for invoice volume
- REST API is straightforward
- Better than Excel for this use case

### Why Google Drive (not Gmail)?
- Simpler OAuth setup
- Finance already used Drive
- Easier to organize/archive files
- Gmail API was overkill for this need

### Why Not Other Tools?
- **Not Zapier/Make:** Finance wanted control over the code
- **Not RPA tools:** Expensive, harder to maintain
- **Not OCR services:** Built-in PDF parsing was sufficient
- **Not email automation:** Drive provided better visibility

---

## 📝 Invoice Processing Logic

### Extraction Pattern
1. Convert PDF to text
2. Search for invoice number (pattern: `INV-\d+` or `Invoice #\d+`)
3. Search for date (multiple formats handled)
4. Search for total/amount (handles various formats: $1,234.56 or 1,234.56)
5. Extract vendor name (usually top of invoice)

### Edge Cases Handled
- Multi-page invoices (searches all pages)
- Scanned/image PDFs (OCR fallback - if implemented)
- Missing fields (logs warning, doesn't fail entire process)
- Duplicate invoices (checks Airtable before inserting)

### Known Limitations
- Struggles with handwritten invoices
- Requires somewhat consistent PDF structure
- Doesn't handle invoice line items (only header data)
- No currency conversion (assumes USD)

---

## 🚨 Common Issues & Solutions

### Issue: API Rate Limits
**Symptom:** Script fails after processing many invoices
**Solution:** Add delays between API calls (100ms is sufficient)
**Code:** `time.sleep(0.1)` between Airtable inserts

### Issue: PDF Parsing Fails
**Symptom:** Can't extract text from certain PDFs
**Solution:** These are likely scanned images, need OCR
**Temporary Fix:** Process manually, mark for investigation
**Long-term:** Implement OCR library (pytesseract)

### Issue: Drive Authentication Expires
**Symptom:** "Invalid credentials" error in Drive automation
**Solution:** Re-authenticate using OAuth flow
**Prevention:** Set up service account for non-expiring access

### Issue: Duplicate Invoices
**Symptom:** Same invoice processed multiple times
**Solution:** Check Airtable for existing invoice # before inserting
**Code:** Query Airtable by invoice number field first

---

## 🔑 API Keys & Credentials

### What You Need
- Airtable Personal Access Token (or API key)
- Airtable Base ID
- Airtable Table Name
- Google Drive credentials.json (for Drive automation)

### Where to Store Them
- NEVER hardcode in scripts
- Use .env file (in .gitignore)
- Load with `python-dotenv` library
- Example: `AIRTABLE_API_KEY=os.getenv('AIRTABLE_API_KEY')`

### How to Rotate Keys
1. Generate new key in Airtable/Google Cloud
2. Update .env file
3. Restart any scheduled processes
4. Test thoroughly before deleting old key

---

## 📅 Automation Schedule

### Local Processor
- Run manually as needed
- Typically used for backlog processing
- Not scheduled

### Drive Automation
- Runs every 15 minutes (cron: `*/15 * * * *`)
- Checks Drive folder for new files
- Processes and archives

### Web App
- Always available (deployed on Vercel)
- No scheduling needed
- Used for ad-hoc uploads

---

## 🔄 Extension Ideas

### Phase 2 Enhancements
- [ ] Add OCR for scanned invoices
- [ ] Extract line items (not just header data)
- [ ] Multi-currency support
- [ ] Email notifications on processing errors
- [ ] Weekly summary reports

### Other Departments
- **Accounts Payable:** Adapt for purchase orders
- **Sales:** Process customer orders
- **Operations:** Equipment inspection reports
- [ ] HR: Resume/application processing

---

## 🧪 Testing Strategy

### Before Deploying Changes
1. Test with sample PDFs in `sample-data/`
2. Verify extraction accuracy
3. Check Airtable data matches expected output
4. Test error handling (malformed PDF)
5. Run on full batch of invoices

### Regression Testing
- Keep sample PDFs representing edge cases
- Run processor on samples before deploying updates
- Compare output to expected-output.json

---

## 🎓 Lessons Learned

### What Worked Well
- Starting with local script (fast to build, easy to test)
- Progressive complexity (don't over-engineer upfront)
- Regular check-ins with Finance (caught issues early)
- Comprehensive logging (made debugging easy)

### What I'd Do Differently
- Should have set up .env earlier (hardcoded keys initially)
- Should have documented invoice formats sooner
- Could have used Airtable webhooks instead of polling
- Should have added unit tests from the start

### Skills Developed
- PDF text extraction and pattern matching
- RESTful API integration (Airtable)
- OAuth 2.0 flows (Google Drive)
- Web deployment (Vercel)
- Git/GitHub workflows
- Technical documentation

---

## 🤝 Handoff Guide

### For the Next AI Operator
If you're maintaining this system:

1. **Read this entire file first**
2. **Run the local processor manually to understand the flow**
3. **Review the logs** (see how errors are handled)
4. **Check the Airtable schema** (understand the data structure)
5. **Test the Drive automation** (watch it process a file)
6. **Use the web app** (understand the user experience)

### For Finance Team
- Upload invoices to the "Invoices - To Process" Drive folder
- Or use the web app for one-off uploads
- Check Airtable daily to ensure processing is working
- Email [your email] if invoices aren't appearing

### For IT/Security
- API keys are in .env (not in code)
- Drive automation runs as service account
- Web app hosted on Vercel (free tier)
- No PII/sensitive data stored outside company systems

---

## 📞 Support

**Questions about the code?** Read the inline comments in scripts
**Questions about the process?** Check the README.md
**Need to make changes?** Test locally first, then push to GitHub
**Something broken?** Check logs first, then contact [your email]

---

**Last Updated:** [Today's Date]
**Status:** ✅ Production (all three automations active)
**Maintained By:** [Your Name]
```

**Customize this:**
- Add your actual insights from building the automations
- Include specific issues YOU encountered
- Add your contact info
- Update status/dates

**Save:** `Ctrl+O`, `Enter`, `Ctrl+X`

**Tell me when you've written your CLAUDE.md file.**

---

USER: [Student creates CLAUDE.md]

---

ACTION: When student responds:

1. **Review the purpose:**
   - "This file is powerful. It captures WHY you made decisions, not just WHAT you built."
   - "Future you (in 6 months) will thank you for this."
   - "Other AI operators can learn from your approach."

2. **Emphasize the value:**
   - "The difference between code and a system is documentation."
   - "You just created a system that can be maintained, extended, and understood."

3. **Commit it:**
   - "Let's commit this to GitHub."

---

STOP: Commit your CLAUDE.md file.

**Run these commands:**

```bash
git add CLAUDE.md
git commit -m "Add automation playbook (CLAUDE.md)

- Technical decisions and rationale
- Common issues and solutions
- Extension ideas
- Lessons learned
- Handoff guide for future maintainers"
git push origin main
```

**Refresh your GitHub page.**

**Tell me when you see CLAUDE.md on GitHub.**

---

USER: [Student commits CLAUDE.md]

---

ACTION: When student responds:

**Celebrate this achievement:**
- "There it is. Your complete automation portfolio."
- "You now have:
  - ✅ Three working automations
  - ✅ Professional README documentation
  - ✅ Technical playbook (CLAUDE.md)
  - ✅ Organized file structure
  - ✅ Everything backed up to GitHub
  - ✅ A shareable URL for your portfolio"

**The portfolio URL:**
- "Your portfolio URL is: `https://github.com/[your-username]/precision-manufacturing-automations`"
- "You can share this with:
  - Employers (shows you build real things)
  - Clients (proves your skills)
  - Colleagues (lets them use your automations)
  - Other AI operators (open source contribution)"

**Next step:**
- "There's one more thing we should add: a requirements.txt file for Python dependencies."

---

## Adding Requirements.txt

Anyone who wants to run your automations needs to install the same Python libraries you used. A `requirements.txt` file lists these dependencies.

---

STOP: Create requirements.txt.

**In your terminal:**
```bash
nano requirements.txt
```

**Add your Python dependencies** (adjust based on what you actually used):

```
requests==2.31.0
python-dotenv==1.0.0
PyPDF2==3.0.1
google-auth==2.23.0
google-auth-oauthlib==1.1.0
google-api-python-client==2.100.0
flask==3.0.0
```

**Note:** These are common libraries for your automations. If you used different libraries, list those instead.

**Save:** `Ctrl+O`, `Enter`, `Ctrl+X`

**To verify what's installed in your environment, run:**
```bash
pip freeze
```

**This shows all installed packages. You can copy relevant ones to requirements.txt.**

**Tell me when you've created requirements.txt.**

---

USER: [Student creates requirements.txt]

---

ACTION: When student responds:

1. **Explain the purpose:**
   - "This file lets anyone recreate your Python environment."
   - "They just run: `pip install -r requirements.txt`"
   - "It's the standard way to share Python project dependencies."

2. **Commit it:**
   - "Let's add this to GitHub too."

---

STOP: Commit requirements.txt.

**Run:**
```bash
git add requirements.txt
git commit -m "Add Python dependencies (requirements.txt)"
git push origin main
```

**Tell me when it's pushed.**

---

USER: [Student commits requirements.txt]

---

ACTION: When student responds:

**Final confirmation:**
- "Perfect! Your repository is now complete and professional."
- "Let's review everything you've accomplished."

---

## What You've Accomplished

Let's take a step back and appreciate what you just built.

**Your GitHub Repository Now Contains:**

1. **Three Working Automations**
   - Invoice processor (local script)
   - Google Drive automation (cloud integration)
   - Invoice upload web app (deployed tool)

2. **Professional Documentation**
   - README.md (project homepage)
   - CLAUDE.md (technical playbook)
   - requirements.txt (dependency list)

3. **Organized Structure**
   - Clean folder organization
   - Sample data included
   - .gitignore for security

4. **Portfolio Piece**
   - Shareable URL
   - Demonstrates real skills
   - Shows business impact
   - Professional presentation

**What This Means:**

**For Job Hunting:**
- You can add this GitHub URL to your resume
- Shows you build real things, not just tutorials
- Demonstrates automation thinking
- Proves you understand documentation

**For Freelancing:**
- Portfolio piece you can show clients
- Demonstrates your process
- Shows you think about maintenance
- Proves ROI (hours saved)

**For Current Role:**
- Your work is backed up
- Others can use your automations
- You can reference your own documentation
- Protected against laptop failure

**For Learning:**
- You now understand git/GitHub
- You can version control future projects
- You know how to collaborate using repos
- You understand professional code documentation

---

## The Complete Git Workflow (Recap)

Now that you've done the full cycle, here's the workflow you'll use going forward:

**When you make changes to your code:**

```bash
# 1. Check what changed
git status

# 2. Stage the files you want to commit
git add filename.py
# or add everything:
git add .

# 3. Commit with a descriptive message
git commit -m "Description of what you changed"

# 4. Push to GitHub
git push origin main

# 5. Verify on GitHub
# Refresh your repo page in browser
```

**That's it. That's the core workflow.**

You'll do this cycle every time you:
- Fix a bug
- Add a feature
- Update documentation
- Refactor code

Each commit is a save point you can return to if needed.

---

## Git Commands You Know Now

**Basic Git Commands:**

- `git status` - See what changed
- `git add <file>` - Stage a file for commit
- `git add .` - Stage all changes
- `git commit -m "message"` - Save a snapshot
- `git push origin main` - Upload to GitHub
- `git log` - See commit history
- `git clone <url>` - Download a repository

**This is enough for 90% of your needs as an AI Operator.**

**Advanced commands exist** (branching, merging, rebasing, etc.) but you don't need them yet. Learn them when you need them.

---

## Making Your Repository Public or Private

One more decision: do you want your repo to be public or private?

**Public Repositories:**
- ✅ Good for portfolio (anyone can see your work)
- ✅ Shows up on your GitHub profile
- ✅ Contributes to your "green squares" (activity graph)
- ❌ Anyone can see your code

**Private Repositories:**
- ✅ Only you can see it
- ✅ Good if code has sensitive business logic
- ✅ Can selectively share with collaborators
- ❌ Doesn't show on public profile

**My recommendation:** Public, UNLESS your code contains:
- Proprietary business logic
- Company-specific information they don't want shared
- Anything confidential

**For a portfolio piece, public is better.**

---

STOP: Decide on repository visibility.

**If you want to change your repo visibility:**

1. Go to your repository on GitHub
2. Click "Settings" (top right)
3. Scroll down to "Danger Zone"
4. Click "Change visibility"
5. Choose Public or Private

**Current status:** Your repo is [public/private based on what they selected earlier]

**Do you want to change it? Or keep it as is?**

---

USER: [Student decides on visibility]

---

ACTION: When student responds:

**If they chose public:**
- "Great choice for a portfolio piece."
- "Make sure there are NO API keys or sensitive data in the code."
- "Anyone can now see and learn from your work."

**If they chose private:**
- "Understandable. You can always make it public later."
- "You can still share it with specific people by adding them as collaborators."

**Then say:**
- "Alright, your repository is complete. Let's talk about how to share it."

---

## Sharing Your Work

You've built something valuable. Here's how to share it.

**Your Portfolio URL:**
```
https://github.com/[your-username]/precision-manufacturing-automations
```

**Where to share it:**

**On LinkedIn:**
- Post about building automations
- Link to the GitHub repo
- Highlight the business impact (hours saved)
- Tag it with: #automation #AI #operations

**On Your Resume:**
```
GitHub: github.com/[your-username]
Portfolio: github.com/[your-username]/precision-manufacturing-automations
```

**In Job Interviews:**
- "I built invoice processing automations that saved 10+ hours/week"
- "Here's the code and documentation: [GitHub URL]"
- "It demonstrates API integration, error handling, and deployment"

**To Colleagues:**
- "I automated invoice processing. Check it out: [URL]"
- "Feel free to adapt it for your own processes"

**To Clients (if freelancing):**
- "Here's an example of my automation work: [URL]"
- "Shows my process from problem → solution → deployment"

**GitHub Profile:**
- Pin this repository to your profile (makes it featured)
- Add a bio that mentions you're an AI Operator
- Keep building - add more automation projects over time

---

STOP: Update your GitHub profile.

**Let's make your GitHub profile professional:**

1. Go to https://github.com/[your-username]
2. Click "Edit profile"
3. Add a bio, for example:
   - "AI Operator | Building automations that save time | Python, APIs, Claude Code"
4. Add your location (optional)
5. Add your website/LinkedIn (optional)
6. Click "Save"

7. **Pin your repository:**
   - On your profile, click "Customize your pins"
   - Select your `precision-manufacturing-automations` repo
   - Click "Save pins"
   - This features it at the top of your profile

**Tell me when you've updated your profile.**

---

USER: [Student updates profile]

---

ACTION: When student responds:

**Celebrate:**
- "Your GitHub profile now looks professional."
- "Anyone who visits can immediately see your automation work."
- "This is how you build credibility as an AI Operator."

**Next:**
- "Let me show you what to do next time you update your code."

---

## Future Workflow: Updating Your Code

You'll continue improving these automations. Here's how to update your GitHub repo.

**Example: You fix a bug in invoice_processor.py**

**Workflow:**

1. **Make the change locally** (edit the file in your code editor)

2. **Test it** (make sure it works)

3. **Check what changed:**
   ```bash
   git status
   git diff invoice_processor.py
   ```
   (Shows exact lines that changed)

4. **Stage the change:**
   ```bash
   git add automations/invoice-processor/invoice_processor.py
   ```

5. **Commit with a clear message:**
   ```bash
   git commit -m "Fix: Handle invoices with missing date field

   - Added fallback date extraction logic
   - Logs warning if date not found
   - Uses file creation date as fallback"
   ```

6. **Push to GitHub:**
   ```bash
   git push origin main
   ```

7. **Verify on GitHub** (refresh your repo page)

**That's the cycle.** Edit → Test → Stage → Commit → Push.

You'll repeat this every time you update code.

---

## Meta Skill: Version Control Thinking

**What you're really learning in this lesson:**

Version control isn't just about backing up code. It's a way of thinking about work.

**Version control thinking means:**
- **Incremental progress:** Small, frequent saves (not one huge change)
- **Documentation:** Every commit message explains WHY you changed something
- **Reversibility:** You can undo any change by going back to a previous commit
- **Collaboration:** Others can see your thought process through commit history
- **Accountability:** Clear trail of who changed what and when

**This applies beyond code:**
- Writing (drafts, edits, revisions)
- Design (iterations, versions)
- Process improvement (changes, experiments, rollbacks)
- Any creative/technical work

**The meta skill:** Thinking in save points, not just final products.

You're learning to:
- Work iteratively (build, commit, build more)
- Document decisions (commit messages tell a story)
- Feel safe experimenting (can always revert)
- Share work in progress (GitHub as collaboration tool)

This mindset makes you more effective in any technical or creative role.

---

## Where Else This Applies

**Beyond automation projects, these skills apply to:**

**In Operations Roles:**
- Version control for process documentation
- Track changes to SOPs (standard operating procedures)
- Maintain wiki/knowledge bases
- Collaborate on operational improvements

**In Consulting:**
- Share work-in-progress with clients
- Show your methodology through commit history
- Deliver code that clients can maintain
- Create open-source tools that build your reputation

**In Freelancing:**
- Portfolio of real projects
- Demonstrate your working style
- Share code with clients professionally
- Build library of reusable components

**In Startups:**
- Document early processes and automations
- Enable anyone to contribute/improve
- Create institutional knowledge from day one
- Make onboarding easier (new team members can see history)

**In Education/Training:**
- Share course materials
- Collaborate with other instructors
- Let students fork and adapt your resources
- Track curriculum evolution over time

**The core skill - version control and professional documentation - is valuable in any field that produces digital work.**

---

## Success Criteria for Lesson 2.6

Before moving on, make sure you can honestly check these off:

- [ ] I have a GitHub account
- [ ] I understand git vs GitHub (the difference)
- [ ] I have git installed and configured on my computer
- [ ] I created a repository on GitHub
- [ ] I cloned it to my local machine
- [ ] I added all my automation files to the repository
- [ ] I created a .gitignore file to protect sensitive data
- [ ] I committed my code with clear commit messages
- [ ] I pushed my commits to GitHub
- [ ] I wrote a professional README.md
- [ ] I created a CLAUDE.md automation playbook
- [ ] I added a requirements.txt file
- [ ] I can see all my files on GitHub
- [ ] I updated my GitHub profile
- [ ] I understand the basic git workflow (add → commit → push)
- [ ] I have a shareable portfolio URL

**If you can check all those boxes, you've mastered the essentials of version control for AI Operators.**

---

STOP: Final reflection.

**Tell me:**
1. What was the most challenging part of this lesson?
2. What surprised you about GitHub?
3. How does it feel to have your work backed up and shareable?
4. On a scale of 1-10, how confident do you feel using git/GitHub now?
5. What's one thing you'll do differently next time based on what you learned?

Take a moment and reflect honestly.

---

USER: [Student reflects on the lesson]

---

ACTION: When student responds:

1. **Address their challenges:**
   - If git commands were confusing: "Totally normal. It takes time to build muscle memory. The more you use it, the more natural it becomes."
   - If commit messages were hard: "Writing good commit messages is an art. You'll get better with practice."
   - If authentication was frustrating: "GitHub authentication can be annoying. You only have to set it up once though."

2. **Address surprises:**
   - If they're surprised it's not just for developers: "Right? GitHub is useful for anyone doing technical work."
   - If they didn't realize the value of documentation: "That's the real power. Code without docs is hard to maintain."

3. **Celebrate their confidence:**
   - If confidence is low (1-5): "That's okay. You'll use git more and it'll become second nature. Reference these notes when you need to."
   - If confidence is medium (6-8): "Perfect. Realistic confidence. You know enough to be productive."
   - If confidence is high (9-10): "Great! Now you just need to build the habit of committing regularly."

4. **Reinforce key takeaways:**
   - "You now have:
     - Backup of all your work
     - Professional portfolio
     - Documentation that lasts
     - Shareable proof of your skills"

5. **What they'll do differently:**
   - Acknowledge their insight
   - Connect it to being a better AI operator

6. **Transition to next steps:**
   - "You've now completed the core automation projects."
   - "You have:
     - Three working automations
     - Documentation
     - GitHub portfolio
     - Real skills you can apply"
   - "In the optional lessons ahead, you can learn more advanced techniques."
   - "But you already have everything you need to call yourself an AI Operator."

---

## What's Next

**You've completed the essential lessons of Module 2.**

You've built:
- PDF invoice processor (local automation)
- Google Drive automation (cloud integration)
- Invoice upload web app (deployed tool)
- GitHub portfolio (professional documentation)

**You now have:**
- Working code that solves real business problems
- Portfolio you can share with employers/clients
- Documentation others can understand and maintain
- Skills to identify and build automations in any company

**Optional Next Steps:**

**Lesson 2.7 - Advanced: Multi-Step Automation (Optional)**
- Chain multiple APIs together
- Build more complex workflows
- Handle edge cases and errors
- Create your own custom automation project

**Lesson 2.8 - Documentation & Handoff (Optional)**
- Create comprehensive runbooks
- Train non-technical users
- Build maintainable automation libraries
- Prepare for team handoff

**Or Apply These Skills Immediately:**
- Identify manual processes in your actual job
- Build automations that solve real problems
- Add new projects to your GitHub portfolio
- Continue practicing and improving

**You're ready to be an AI Operator.**

The best way to solidify these skills is to build something for a real use case. Find a manual process in your work or life and automate it.

Then add it to your GitHub portfolio.

That's how you become truly proficient.

---

## Additional Resources

**GitHub Basics:**
- GitHub Docs: https://docs.github.com/en/get-started
- GitHub Learning Lab: https://lab.github.com
- Pro Git Book (free): https://git-scm.com/book/en/v2

**Git Cheat Sheet:**
- `git status` - Check what's changed
- `git add <file>` - Stage a file
- `git commit -m "message"` - Save changes
- `git push` - Upload to GitHub
- `git log` - See history
- `git diff` - See exact changes

**README Writing:**
- Make a README: https://www.makeareadme.com
- Awesome README examples: https://github.com/matiassingers/awesome-readme

**Portfolio Building:**
- Pin your best repositories to your profile
- Write clear commit messages
- Add screenshots/demos to READMEs
- Keep building and documenting

**Remember:** The best portfolio is one with real projects that solved real problems. Keep building.

---

**End of Lesson 2.6**

**Next (Optional):** Lesson 2.7 - Advanced: Multi-Step Automation

---

*Your code is now backed up, documented, and shareable. You have a portfolio. You're an AI Operator.*
