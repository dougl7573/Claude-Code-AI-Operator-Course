# Lesson 2.5: GitHub Setup & Deployment

**Get your app live on the internet - from zero to shareable URL**

---

## The Text Message You Want to Send

It's Friday morning. Your invoice upload web app is working perfectly on your laptop. You can upload invoices, see the extracted data, save to Airtable. It's great.

But it only works on YOUR computer.

Marcus from Finance walks over.

> "Hey, is that invoice tool ready? I wanted to show Janet in Accounts Payable. She's been asking about it."

> "It works! But... it's only running on my machine right now. You'd have to come over here to use it."

Marcus looks disappointed.

> "Oh. I was hoping you could just send me a link. Like a website."

Sarah (the CEO) overhears.

> "Wait, it's not a website yet? Can we make it one? I want to text the link to the whole Finance team."

**That's what this lesson is about.** Taking your working app and putting it on the internet so anyone can use it with a URL.

By the end of this lesson, you'll text Marcus a link. He'll open it on his phone, upload an invoice, and watch it work.

---

## What We're Doing Today

**Two things:**

1. **Set up GitHub** - This is where your code lives on the internet. Think of it like cloud storage for code.
2. **Deploy to Vercel** - This takes your code from GitHub and turns it into a live website.

**The flow:**
```
Your Computer → GitHub (stores code) → Vercel (runs it as a website) → Live URL
```

If you've never used GitHub before, that's completely fine. We're setting it up from scratch.

If you already have a GitHub account, you can skip the parts you've already done.

---

STOP: Let's check your starting point.

**Answer these:**
1. Do you have a GitHub account? (Yes/No)
2. Have you ever pushed code to GitHub before? (Yes/No)
3. Is your invoice web app from Lesson 2.4 working locally? (Yes/No/Having issues)

---

USER: [Student responds]

---

ACTION: When student responds:

**If they have a GitHub account AND have pushed code before:**
- "Great! You can skip to Part 3 (Authenticate with GitHub CLI) to make sure everything is connected properly, then we'll push your app and deploy it."

**If they have a GitHub account but never pushed code:**
- "Good, you have an account. We'll skip account creation but walk through everything else step by step."

**If they don't have a GitHub account:**
- "Perfect. We'll set everything up from scratch. It takes about 10 minutes."

**If their web app isn't working:**
- "Let's fix that first. Go back to Lesson 2.4 and make sure the app runs locally before we deploy it. No point deploying something that doesn't work yet."
- "Tell me what's happening and I can help troubleshoot."

**Then:** "Alright, let's get started..."

---

## Part 1: Create a GitHub Account

**If you already have a GitHub account, skip to Part 2.**

GitHub is free. Your account is permanent. You'll use it for everything you build going forward.

---

STOP: Create your GitHub account.

1. **Go to** [https://github.com](https://github.com)
2. **Click "Sign up"**
3. **Enter your email address**
4. **Create a password**
5. **Choose a username** - This will be in your portfolio URL, so pick something professional
   - Good: `john-smith`, `jsmith-dev`, `sarahchen`, `your-actual-name`
   - Avoid: `coolcoder123`, `xxhackerxx`, random strings
6. **Complete the verification puzzle**
7. **Verify your email** (check your inbox and click the link)

**When you're done, tell me: "Account created"**

---

USER: [Student creates account or confirms they have one]

---

ACTION: When confirmed:

**If they just created an account:**
- "Welcome to GitHub! That username will be part of every project URL, so good choice."

**If they already had one:**
- "Perfect, we'll use your existing account."

**Then:** "Next, we need to install the GitHub CLI tool. This is what makes pushing code painless."

---

## Part 2: Install the GitHub CLI

The GitHub CLI (`gh`) is a tool that lets you interact with GitHub from your terminal. It handles all the tricky authentication stuff automatically.

**This is the key tool that makes everything smooth.** Without it, you'd have to create tokens, configure credentials, and deal with authentication errors. The `gh` tool handles all of that for you.

---

STOP: Install the GitHub CLI.

**For Mac:**

Option A (if you have Homebrew):
```bash
brew install gh
```

Option B (if you don't have Homebrew, or aren't sure):
```bash
# First, check if you have Homebrew
brew --version
```

If that shows a version number, use Option A above.

If it says "command not found", install Homebrew first:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Then run `brew install gh`.

Option C (if you don't want to use Homebrew):
- Go to https://cli.github.com/
- Download the macOS installer
- Open the downloaded file and follow the instructions

**For Windows:**

Option A (if you have winget):
```bash
winget install --id GitHub.cli
```

Option B:
- Go to https://cli.github.com/
- Download the Windows installer (.msi)
- Run the installer, click through the defaults

**For Linux:**

```bash
# Ubuntu/Debian
sudo apt install gh

# Fedora
sudo dnf install gh
```

---

**Verify it installed:**

```bash
gh --version
```

You should see something like: `gh version 2.x.x`

**Tell me what you see when you run `gh --version`.**

---

USER: [Student installs gh and confirms]

---

ACTION: When student responds:

**If they see a version number:**
- "Perfect! The GitHub CLI is installed. Now comes the important part: connecting it to your GitHub account."

**If they got an error:**
- "command not found" → "The installation didn't work. Let's try a different method."
  - Mac: Try the direct download from https://cli.github.com/
  - Windows: Try the .msi download from https://cli.github.com/
  - "After installing, close and reopen your terminal, then try `gh --version` again."

**Once installed:** "Now let's authenticate. This is the step that saves you from 2 hours of frustration with tokens and passwords."

---

## Part 3: Authenticate with GitHub

This is the step that trips most people up when they try to do it manually. The `gh` tool makes it simple.

**What's happening:** You're telling your computer "I'm allowed to push code to this GitHub account." Without this, GitHub will reject everything you try to send it.

---

STOP: Authenticate with GitHub.

**Run this command:**

```bash
gh auth login
```

**You'll see a series of prompts. Here's exactly what to choose:**

**Prompt 1:** "What account do you want to log into?"
→ Select: **GitHub.com** (use arrow keys, press Enter)

**Prompt 2:** "What is your preferred protocol for Git operations on this host?"
→ Select: **HTTPS**

**Prompt 3:** "Authenticate Git with your GitHub credentials?"
→ Select: **Yes**

**Prompt 4:** "How would you like to authenticate GitHub CLI?"
→ Select: **Login with a web browser**

**What happens next:**

1. Your terminal shows a **one-time code** (something like `ABCD-1234`)
2. It says "Press Enter to open github.com in your browser"
3. **Press Enter**
4. Your browser opens to GitHub
5. **Paste the code** from your terminal into the browser
6. Click **"Authorize"**
7. Your terminal shows: **"Authentication complete"**

**That's it. You're connected.**

---

**Verify it worked:**

```bash
gh auth status
```

You should see something like:
```
github.com
  ✓ Logged in to github.com account your-username
  ✓ Git operations protocol: https
  ✓ Token: gho_xxxx...
```

**Tell me what you see.**

---

USER: [Student authenticates]

---

ACTION: When student responds:

**If they see the checkmarks and "Logged in":**
- "You're connected. Every git and GitHub operation from your terminal will now work automatically."
- "No more password prompts. No more token errors. The `gh` tool handles it all."

**If they got an error during the browser step:**
- "Did the browser open? If not, copy the URL shown in the terminal and paste it into your browser manually."
- "If the code expired, run `gh auth login` again. The code is only valid for a few minutes."

**If they see "not logged in":**
- "Let's try again. Run `gh auth login` and follow the prompts. Make sure to select 'Login with a web browser'."

**Once authenticated:** "Now we're ready for the fun part. Let's push your web app to GitHub."

---

## Part 4: Push Your Web App to GitHub

Now we're going to take your invoice web app and upload it to GitHub. This does two things:
1. Backs up your code in the cloud
2. Gets it ready for Vercel to deploy

---

STOP: Let's push your code to GitHub.

**Step 1: Navigate to your web app folder**

```bash
cd /path/to/your/invoice-upload-webapp
```

Replace the path with wherever your web app files are. If you're not sure, check where you created it in Lesson 2.4.

**Step 2: Make sure git is set up**

First, check if git knows who you are:
```bash
git config user.name
git config user.email
```

If these are empty, set them:
```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```
Use the same email you used for your GitHub account.

**Step 3: Initialize git (if needed)**

Check if this folder is already a git repository:
```bash
git status
```

If you see "not a git repository", run:
```bash
git init
```

If you see a list of files (tracked/untracked), you're already set up.

**Step 4: Make sure your `.gitignore` is in place**

```bash
cat .gitignore
```

You should see entries for `.env`, `__pycache__/`, `node_modules/`, etc. (You created this in Lesson 2.4.)

If it doesn't exist, create it now:
```bash
cat > .gitignore << 'EOF'
.env
.env.local
__pycache__/
*.pyc
node_modules/
.DS_Store
venv/
EOF
```

**Step 5: Stage and commit your files**

```bash
git add .
git commit -m "Invoice upload web app - ready for deployment"
```

**Step 6: Create a GitHub repo and push (this is the magic command)**

```bash
gh repo create invoice-webapp --public --source=. --remote=origin --push
```

**What this single command does:**
- Creates a new repository called "invoice-webapp" on your GitHub account
- Sets it as public (anyone can see it)
- Connects your local folder to this GitHub repository
- Pushes all your code up to GitHub

**You should see output like:**
```
✓ Created repository your-username/invoice-webapp on GitHub
✓ Added remote origin
✓ Pushed commits to origin/main
```

**Step 7: Verify on GitHub**

Open your browser and go to:
```
https://github.com/your-username/invoice-webapp
```

You should see all your project files there.

**Tell me: "Code is on GitHub" and share the URL.**

---

USER: [Student pushes to GitHub]

---

ACTION: When student responds:

**If successful:**
- "Your code is on GitHub! That URL is your project's home on the internet."
- "Anyone can see it, download it, and learn from it."
- "But more importantly: Vercel can now access it and deploy it as a website."

**If they got "repository already exists":**
- "You already have a repo with that name. Either use a different name:"
- `gh repo create invoice-webapp-v2 --public --source=. --remote=origin --push`
- "Or delete the old one first on GitHub.com (Settings → Danger Zone → Delete)"

**If they got "not a git repository":**
- "Run `git init` first, then `git add .`, then `git commit -m "Initial commit"`, then try the `gh repo create` command again."

**If they got other errors:**
- "What error message do you see? Copy and paste it here and we'll figure it out."

**Once code is on GitHub:** "Now for the final step: deploying it as a live website."

---

## Part 5: Deploy to Vercel

Vercel takes your code from GitHub and turns it into a live website. Free tier, no credit card needed.

**Why Vercel?**
- Free for personal projects
- Connects directly to GitHub
- Automatic HTTPS (secure)
- Live URL in minutes
- Redeploys automatically when you update code

---

STOP: Create a Vercel account.

1. **Go to** [https://vercel.com](https://vercel.com)
2. **Click "Sign Up"**
3. **Choose "Continue with GitHub"** (this is important - it connects your accounts)
4. **Authorize Vercel** to access your GitHub repos
5. You'll land on the Vercel dashboard

**Tell me: "Vercel account created"**

---

USER: [Student creates Vercel account]

---

ACTION: When confirmed:

**"Perfect. Now let's import your project and deploy it."**

---

STOP: Deploy your app.

**Step 1: Import your GitHub repository**

1. On your Vercel dashboard, click **"Add New..."** → **"Project"**
2. You'll see a list of your GitHub repositories
3. Find **"invoice-webapp"** (or whatever you named it)
4. Click **"Import"**

**Step 2: Configure the project**

**If you built with Next.js:**
- Vercel auto-detects Next.js. You probably don't need to change anything.
- Skip to "Add Environment Variables" below.

**If you built with Flask (Python):**
- Vercel needs a little configuration to run Python apps.
- Before clicking Deploy, we need to create a config file.

**For Flask students, do this FIRST:**

Go back to your terminal and create a `vercel.json` file in your project root:

```bash
cat > vercel.json << 'EOF'
{
  "builds": [
    {
      "src": "backend/app.py",
      "use": "@vercel/python"
    },
    {
      "src": "frontend/**",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "backend/app.py"
    },
    {
      "src": "/(.*)",
      "dest": "frontend/$1"
    }
  ]
}
```

**Important for Flask:** Your Flask app needs to expose the app as a WSGI application. Make sure your `app.py` has the Flask app at the module level (not hidden inside `if __name__ == "__main__"`). Vercel imports your app, it doesn't "run" it.

Example - your `app.py` should look something like:
```python
from flask import Flask
app = Flask(__name__)

# ... your routes here ...

# This part is for local development only
if __name__ == "__main__":
    app.run(debug=True)
```

The `app = Flask(__name__)` line at the top level is what Vercel uses.

Now push the config file:
```bash
git add vercel.json
git commit -m "Add Vercel deployment config"
git push
```

Go back to the Vercel import page and refresh if needed.

**Step 3: Add Environment Variables**

Before clicking Deploy, scroll down to **"Environment Variables"**.

Add these:
- **Name:** `AIRTABLE_TOKEN` → **Value:** your Airtable token
- **Name:** `AIRTABLE_BASE_ID` → **Value:** your Airtable base ID

These are the same values from your `.env` file, but Vercel needs them set separately (it doesn't read your `.env` file).

**Step 4: Click "Deploy"**

Click the **"Deploy"** button and wait.

**What you'll see:**
- Vercel pulls your code from GitHub
- It builds your project (installs dependencies, etc.)
- Progress bars and build logs scroll by
- After 1-3 minutes, you'll see: **"Congratulations!"** with a preview of your site

**Step 5: Get your URL**

Vercel gives you a URL like: `invoice-webapp-abc123.vercel.app`

**Click "Visit"** to open your live app.

**Tell me: Share the URL Vercel gave you.**

---

USER: [Student deploys and shares URL]

---

ACTION: When student shares URL:

**If deployment succeeded:**
- "YES! Open that URL right now."
- "Now upload a sample invoice. Does it work?"

**Guide them through testing:**
1. "Upload one of your sample invoice PDFs"
2. "Click Process"
3. "Do you see the extracted data?"
4. "Click Save to Airtable"
5. "Check your Airtable base - did the record appear?"

**If everything works:**
- "THAT'S IT. You have a live web app."
- "Text that link to someone right now. Have them try it."
- "That URL works on any phone, tablet, or computer. Anywhere in the world."
- "Marcus can use it from his desk. Sarah can demo it to the board. You just shipped a product."

**If the app loads but something doesn't work:**
- Jump to Part 6 (Troubleshooting) below

**If deployment failed:**
- Jump to Part 6 (Troubleshooting) below

---

## Part 6: Troubleshooting

**Deployment rarely works perfectly the first time. That's normal.** Here are the most common issues and exactly how to fix them.

---

### "Build Failed" on Vercel

**What you see:** Red error on the Vercel dashboard saying the build failed.

**How to debug:**
1. Click on the failed deployment
2. Click **"Build Logs"** or **"Logs"** tab
3. Scroll to the red error message
4. Read the actual error (it usually tells you exactly what's wrong)

**Common causes:**

**"ModuleNotFoundError: No module named 'pdfplumber'"** (or any dependency)
- Your `requirements.txt` is missing a dependency
- Fix: Add the missing package to `requirements.txt`
- Make sure EVERY package you import is listed:
```
flask
flask-cors
pdfplumber
python-dotenv
requests
```
- Push the fix: `git add requirements.txt && git commit -m "Fix dependencies" && git push`
- Vercel auto-redeploys when you push

**"No module named 'backend.app'" or path errors**
- Your file structure doesn't match what `vercel.json` expects
- Check that your `vercel.json` paths match your actual folder structure
- If your Flask app is at `app.py` (not `backend/app.py`), update `vercel.json` accordingly

---

### "502 Bad Gateway" or "Function Crashed"

**What you see:** The page loads but API calls return 502 errors.

**Common causes:**

**Flask app not structured for serverless:**
- Vercel runs Python as serverless functions, not as a traditional server
- Make sure `app = Flask(__name__)` is at the top level of your file
- Don't put it inside a function or class

**File too large for serverless:**
- Vercel serverless functions have a 50MB limit
- If you're processing large PDFs, this might be an issue
- Fix: Add file size validation in your upload endpoint

---

### "CORS Error" on Deployed App

**What you see:** App loads but uploads fail with "Access-Control-Allow-Origin" errors in the browser console.

**Fix:** Update your Flask CORS configuration for production:

```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This allows all origins - fine for internal tools
```

Push the fix and Vercel will auto-redeploy.

---

### "Environment Variables Not Working"

**What you see:** App loads but Airtable saves fail, or you get "unauthorized" errors.

**Fix:**
1. Go to your Vercel project dashboard
2. Click **"Settings"** → **"Environment Variables"**
3. Make sure both `AIRTABLE_TOKEN` and `AIRTABLE_BASE_ID` are set
4. Make sure there are no extra spaces or quotes in the values
5. After changing env vars, click **"Redeploy"** from the Deployments tab (env vars only take effect on new deployments)

---

### "App Works Locally But Not on Vercel"

**Checklist:**
- [ ] All dependencies in `requirements.txt`?
- [ ] Environment variables set in Vercel dashboard?
- [ ] File paths use relative paths (not absolute like `/Users/tom/...`)?
- [ ] `vercel.json` routes match your project structure?
- [ ] Flask app object at module level (not inside `if __name__`)?

---

### Still Stuck?

If you've been debugging for more than 30 minutes and can't figure it out, try the Render fallback in Part 7 below. Sometimes a different platform is the easiest fix.

You can also ask Claude Code for help: paste the Vercel error log into Claude Code and ask it to diagnose the issue.

---

## Part 7: Fallback - Deploy to Render

**If Vercel isn't working for your Flask app, try Render.**

Render handles Python/Flask apps more naturally because it runs them as traditional web servers (not serverless functions). This means fewer configuration headaches.

---

STOP: Deploy to Render (only if Vercel didn't work).

**Step 1: Create a Render account**
1. Go to [https://render.com](https://render.com)
2. Click "Get Started for Free"
3. Sign up with GitHub (same as Vercel - this connects your repos)

**Step 2: Create a new Web Service**
1. Click "New" → "Web Service"
2. Connect your GitHub repository (invoice-webapp)
3. Render will ask for configuration:
   - **Name:** invoice-webapp
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app` (or `gunicorn backend.app:app` if your Flask file is in a backend folder)

**Note:** You'll need `gunicorn` in your `requirements.txt`:
```
flask
flask-cors
pdfplumber
python-dotenv
requests
gunicorn
```

Push this update: `git add requirements.txt && git commit -m "Add gunicorn" && git push`

**Step 3: Add Environment Variables**
- Click "Environment" in your Render service settings
- Add `AIRTABLE_TOKEN` and `AIRTABLE_BASE_ID`

**Step 4: Deploy**
- Click "Create Web Service"
- Render will build and deploy (takes 2-5 minutes)
- You'll get a URL like: `invoice-webapp-abc.onrender.com`

**Step 5: Test it**
- Open the URL
- Upload an invoice
- Verify it works end-to-end

**Note:** Render's free tier sleeps after 15 minutes of inactivity. The first load after sleeping takes ~30 seconds. This is fine for internal team tools.

**Tell me the URL when it's deployed.**

---

USER: [Student deploys to Render]

---

ACTION: When deployed:

- "Your app is live! The Render URL works the same way."
- "One thing to know: Render's free tier 'sleeps' after 15 minutes of no activity. The first visit after sleeping takes about 30 seconds to wake up. After that it's fast."
- "For a team tool, this is totally fine."

---

## Part 8: You Just Shipped a Product

**Take a breath. Look at what just happened.**

You went from "I have a script on my laptop" to "I have a live URL anyone can use."

**The journey:**
1. Lesson 2.2: Built a PDF processing script
2. Lesson 2.3: Connected it to Google Drive
3. Lesson 2.4: Wrapped it in a web app
4. **This lesson: Put it on the internet**

**That URL is real.** It works on phones, tablets, laptops. Marcus can use it. Sarah can demo it to the board. Janet in Accounts Payable can process invoices from her desk.

**You just went from "AI Operator learning the ropes" to "person who ships working tools."**

---

STOP: Let's test and celebrate.

**Your final task for this lesson:**

1. **Open your live URL** on your phone (or text it to yourself and open it there)
2. **Upload a sample invoice** from your phone
3. **Check Airtable** to see if the record appeared
4. **Update your User Guide** from Lesson 2.4 - replace the placeholder URL with your real one

**Then tell me:**
1. What's your live URL?
2. Did it work on your phone?
3. How does it feel to have a live app you can share?

---

USER: [Student tests and celebrates]

---

ACTION: When student responds:

1. **Celebrate genuinely:**
   - "That URL is yours. You built it. You deployed it. Anyone in the world can use it."
   - "This is what separates people who 'learn to code' from people who actually ship things."

2. **Address how they feel:**
   - If excited: "Channel that energy. You're going to build more things like this."
   - If relieved: "Deployment is the hardest part for most people. You got through it."
   - If surprised it was easier than expected: "The `gh` tool and Vercel make it way easier than it used to be."

3. **Practical next step:**
   - "Now that you know how to deploy, every future project can go live the same way."
   - "In the next lesson, we'll organize ALL your automations into a professional GitHub portfolio."

4. **Wrap up:**
   - "Great work. Seriously. Go share that link with someone."
   - "When you're ready, head to Lesson 2.6."

---

## Success Criteria for Lesson 2.5

**Before moving to the next lesson, make sure you can check these off:**

- [ ] I have a GitHub account
- [ ] I installed the GitHub CLI (`gh`)
- [ ] I authenticated with `gh auth login`
- [ ] I pushed my web app code to a GitHub repository
- [ ] I created a Vercel (or Render) account
- [ ] I deployed my app and have a live URL
- [ ] I tested the live app with a real invoice upload
- [ ] I updated my User Guide with the real URL
- [ ] I understand the flow: Code → GitHub → Vercel → Live URL

**If you can check all those boxes, you're ready for Lesson 2.6.**

---

## Quick Reference

**Commands you'll use again:**

```bash
# Check GitHub auth status
gh auth status

# Create a new repo from existing code
gh repo create REPO-NAME --public --source=. --remote=origin --push

# Push updates after changes
git add .
git commit -m "Your message"
git push

# Check what's happening with git
git status
git log --oneline
```

**Vercel tips:**
- Vercel auto-redeploys when you push to GitHub
- Environment variables: Settings → Environment Variables
- Build logs: Deployments → click deployment → Logs
- Custom domain: Settings → Domains (optional, free)

---

**End of Lesson 2.5**

**Next:** Lesson 2.6 - GitHub Portfolio & Version Control

---

*Your app is live. People can use it. You shipped something real.*

*That's what AI Operators do.*
