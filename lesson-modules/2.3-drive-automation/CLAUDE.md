# Lesson 2.3: Project 2 - Google Drive Automation

**From Local Script to Cloud Integration**

---

## The Finance Team's Next Request

It's been two weeks since you deployed the PDF invoice processor from Lesson 2.2. Marcus Rodriguez (Finance Lead) catches you in the hallway.

> "Hey! That invoice script is working great. But... there's one problem. Sarah and I are constantly emailing each other: 'Did you run the script?' 'I forgot to run the script.' 'Can you process these new invoices?'"
>
> "We need something that just... watches for new invoices and processes them automatically. Like, we drop the PDF in a folder and it just happens. Can you do that?"

You nod. "Yeah, we can do that. We'll set up a Google Drive folder that automatically processes anything you drop into it."

Marcus lights up. "That's EXACTLY what we need. When can you have it?"

**This is Lesson 2.3: Taking your local automation to the cloud.**

---

## What You'll Build

**The Automation:**
- A Google Drive folder called "Invoices - To Process"
- Drop a PDF invoice in that folder
- Script automatically detects new files
- Processes them with your invoice_processor.py from Lesson 2.2
- Moves processed files to "Invoices - Processed" subfolder
- Logs everything so you know what happened
- Runs continuously in the background OR on a schedule

**By the end of this lesson:**
- Finance team drops invoices in Drive, never thinks about it again
- Invoices appear in Airtable automatically
- You've learned Google Drive API and OAuth authentication
- You understand cloud automation vs. local automation
- You have a pattern you can apply to other file-watching scenarios

**Time to build:** 2-3 hours (OAuth setup takes the longest)

---

## What You'll Learn

**Technical Skills:**
- Google Cloud Console setup (detailed walkthrough)
- OAuth 2.0 authentication (step-by-step, beginner-friendly)
- Google Drive API basics
- File watching patterns
- Scheduling automations (cron vs. continuous running)

**AI Operator Skills:**
- Recognizing when to move from local to cloud
- User experience thinking (drop file → magic happens)
- Building maintainable scheduled automations
- Documentation for cloud services

**Meta Skill:**
Cloud automation is different from local scripts. You're learning to build automations that run WITHOUT you being there - that's when automation gets powerful.

---

STOP: Before we dive into Google APIs, let's make sure you're ready.

**Check these:**
1. Did you complete Lesson 2.2 and have a working invoice_processor.py? (If not, go back - we'll be using that code)
2. Do you have a Google account? (Personal Gmail is fine)
3. Are you comfortable with the idea of OAuth authentication? (Don't worry if not - I'll explain everything)

**Also, quick question:**
Have you ever set up a Google API before? (Yes/No/Tried but got confused)

Be honest - if you've never done this, that's totally fine. I'll walk you through every single step.

---

USER: [Student confirms readiness and OAuth experience level]

---

ACTION: When student responds:

**IF they haven't done Lesson 2.2:**
- "Hold up - we need that invoice_processor.py working first. The whole point of this lesson is to automate THAT script with Drive. Go back to Lesson 2.2, get that working, then come back here."
- Don't let them proceed without the foundation

**IF they're ready but nervous about OAuth:**
- "OAuth sounds scary, but it's just 'letting your script access Drive on your behalf.' Think of it like giving someone a key to your house - they can come in, but only to do specific things you allow."
- "I'll walk you through EVERY click. You'll be fine."

**IF they've tried OAuth before and failed:**
- "Yeah, Google's documentation is awful. That's why this lesson exists. Follow my steps exactly and you'll get it working."

**IF they're confident:**
- "Great! Let's not waste time then. We'll move quickly through the setup."

**Then continue:** "Alright, let's start with the Google Cloud Console. This is where all Google API magic begins..."

---

## Phase 1: Google Cloud Console Setup

**What you're doing:** Creating a "project" in Google Cloud that will let your script talk to Drive.

**Think of it like this:**
- Google Cloud is the bouncer at a club
- Your script is someone who wants to get in
- You're creating a VIP pass that gives your script permission

**This section takes 15-20 minutes. Follow each step carefully.**

---

### Step 1: Create a Google Cloud Project

1. Go to: https://console.cloud.google.com/
2. Sign in with your Google account (personal Gmail is fine)
3. If this is your first time:
   - You'll see a welcome screen
   - Click "Select a project" at the top
   - Click "NEW PROJECT"

4. If you've been here before:
   - Click the project dropdown at the top (says "My Project" or whatever)
   - Click "NEW PROJECT"

5. Fill in the details:
   - **Project name:** "Invoice Drive Automation"
   - **Organization:** Leave it (probably says "No organization")
   - Click "CREATE"

6. Wait 30 seconds while Google creates the project
7. You'll see a notification "Project created"
8. Click "SELECT PROJECT" or make sure "Invoice Drive Automation" is selected in the top dropdown

**Checkpoint:** You should see "Invoice Drive Automation" in the top bar.

---

STOP: Did you create the project successfully?

Tell me:
- What's your project name showing at the top?
- Any errors or confusion?

---

USER: [Student confirms project creation]

---

ACTION: When student responds:

**IF they got it:**
- "Perfect. You now have a Google Cloud project. Next, we need to enable the Drive API."

**IF they're confused about organization:**
- "Don't worry about 'No organization' - that's normal for personal accounts. Just means it's not part of a company Google Workspace."

**IF they can't find the NEW PROJECT button:**
- "Top left, click the project dropdown (it's the project name next to the Google Cloud logo). Then NEW PROJECT is in that menu."

**IF they got it working:**
- "Great! On to the Drive API..."

---

### Step 2: Enable the Google Drive API

**What you're doing:** Turning on the "Drive" feature for your project.

1. In the Google Cloud Console, you should see a search bar at the top
2. Type: "Google Drive API"
3. Click on "Google Drive API" in the results (it'll have a Google Drive icon)
4. You'll see an API details page
5. Click the big blue "ENABLE" button
6. Wait 10-20 seconds
7. The page will refresh and say "API enabled"

**You should now see:**
- Metrics (probably empty)
- A message like "To use this API, you may need credentials"

**Checkpoint:** The top of the page says "Google Drive API" and there's no "ENABLE" button (because it's already enabled).

---

STOP: Did you enable the Drive API?

Confirm:
- You see "Google Drive API" at the top
- No "ENABLE" button (means it's on)
- You see "Credentials" in the left sidebar

---

USER: [Student confirms API enabled]

---

ACTION: When student responds:

**IF successful:**
- "Excellent. The API is now active. Next step: creating OAuth credentials. This is the trickiest part, so pay close attention."

**IF they see "Quotas" or "Metrics" tabs:**
- "Perfect, those tabs mean the API is enabled. Let's move to credentials."

**IF they're on the wrong page:**
- "Make sure you're on the Google Drive API page specifically. Search for 'Google Drive API' and enable that one."

**Then:** "Now comes OAuth. This is where most people get stuck, so I'm going to be VERY detailed..."

---

### Step 3: Create OAuth Credentials

**What you're doing:** Creating the "key" that lets your script access YOUR Drive files.

**Important concept:**
- OAuth = "Let this app access my stuff, but only what I allow"
- You're creating credentials that will ask YOU for permission
- Once you grant permission, your script can access Drive
- You can revoke access anytime

**This is different from an API key:**
- API key = "This app can access public stuff"
- OAuth = "This app can access MY stuff, with my permission"

**Follow these steps exactly:**

1. Click "Credentials" in the left sidebar
2. Click "+ CREATE CREDENTIALS" at the top
3. Select "OAuth client ID"

4. **IF you see "Configure consent screen":**
   - Click that blue button
   - Select "External" (unless you have a Google Workspace, then "Internal" is fine)
   - Click "CREATE"

5. **OAuth consent screen - App information:**
   - **App name:** "Invoice Drive Automation"
   - **User support email:** Your email (auto-filled)
   - **App logo:** Skip this
   - **Application home page:** Leave blank
   - **Authorized domains:** Leave blank
   - **Developer contact email:** Your email
   - Click "SAVE AND CONTINUE"

6. **Scopes page:**
   - Click "ADD OR REMOVE SCOPES"
   - In the filter, search for: "drive.file"
   - Check the box next to: ".../auth/drive.file" (it says "See, edit, create, and delete only the specific Google Drive files you use with this app")
   - Click "UPDATE"
   - Click "SAVE AND CONTINUE"

7. **Test users page:**
   - Click "+ ADD USERS"
   - Enter YOUR email address (the one you're logged in with)
   - Click "ADD"
   - Click "SAVE AND CONTINUE"

8. **Summary page:**
   - Review everything
   - Click "BACK TO DASHBOARD"

9. **Now create the actual OAuth client:**
   - Click "Credentials" in left sidebar again
   - Click "+ CREATE CREDENTIALS"
   - Select "OAuth client ID"
   - **Application type:** "Desktop app"
   - **Name:** "Drive Automation Script"
   - Click "CREATE"

10. **You'll see a popup: "OAuth client created"**
    - Click "DOWNLOAD JSON"
    - Save the file as `credentials.json`
    - Remember where you saved it (you'll need it in a minute)
    - Click "OK"

**Checkpoint:** You have a file called `credentials.json` on your computer.

---

STOP: This was a lot of steps. Let's make sure you made it through.

**Tell me:**
1. Do you have a credentials.json file? (Yes/No)
2. Where did you save it?
3. Did you get stuck anywhere? (Be specific if yes)

If you got lost, tell me exactly where and I'll help you backtrack.

---

USER: [Student confirms credentials creation and file location]

---

ACTION: When student responds:

**IF they have credentials.json:**
- "Perfect! That's the hard part done. OAuth setup is always the worst part of Google APIs, but you made it through."
- "That JSON file is your 'key' to accessing Drive. Keep it safe - don't commit it to GitHub or share it publicly."

**IF they got stuck on consent screen:**
- "The consent screen is confusing. Just think of it as 'what does my app do and who can use it?' You're the only user, so add your email and move on."

**IF they can't find the downloaded file:**
- "Check your Downloads folder. It's probably called something like 'client_secret_XXXXX.json'. Rename it to credentials.json for simplicity."

**IF they're confused about scopes:**
- "Scopes = permissions. 'drive.file' means 'only files this app creates or is given access to.' That's the safest scope - your script can't see ALL your Drive files, just the ones in folders you point it to."

**Then:** "Now let's set up your project folder and test the Drive connection..."

---

## Phase 2: Project Setup & Drive Connection Test

**What you're doing:** Creating a Python script that connects to Drive and proves it works.

**Folder structure we're building:**
```
drive-invoice-automation/
├── credentials.json          (the file you just downloaded)
├── token.json               (will be created automatically)
├── drive_invoice_watcher.py (the main script - we'll build this)
├── invoice_processor.py     (copy from Lesson 2.2)
└── requirements.txt         (Python dependencies)
```

---

### Step 4: Create the Project Folder

1. Open your terminal (or command prompt on Windows)
2. Navigate to where you keep your projects
3. Run these commands:

```bash
mkdir drive-invoice-automation
cd drive-invoice-automation
```

4. Copy your `invoice_processor.py` from Lesson 2.2 into this folder
   - If you don't have it, stop and go back to Lesson 2.2

5. Move your `credentials.json` file into this folder

**Your folder should now have:**
- credentials.json
- invoice_processor.py

---

STOP: Let's verify your folder setup.

**Run this command in your terminal:**
```bash
ls -la
```

**Tell me:**
- Do you see both credentials.json and invoice_processor.py?
- Are you in the drive-invoice-automation folder? (Check with `pwd`)

---

USER: [Student confirms folder setup]

---

ACTION: When student responds:

**IF files are there:**
- "Great! Now let's install the Google Drive API library and test the connection."

**IF invoice_processor.py is missing:**
- "You need that file from Lesson 2.2. Go grab it and copy it into this folder."

**IF credentials.json is elsewhere:**
- "Move it into this folder so everything is in one place."

**Then:** "Let's install dependencies and test Drive access..."

---

### Step 5: Install Required Libraries

**What you're doing:** Installing the Google API Python library.

1. Make sure you're in the `drive-invoice-automation` folder
2. Run this command:

```bash
pip3 install google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

**This installs:**
- `google-auth-oauthlib` - Handles OAuth authentication
- `google-auth-httplib2` - HTTP library for Google APIs
- `google-api-python-client` - The main Google API client

Wait for it to finish (30-60 seconds).

**Create a requirements.txt file so others can install dependencies:**

```bash
echo "google-auth-oauthlib==1.2.0
google-auth-httplib2==0.2.0
google-api-python-client==2.108.0" > requirements.txt
```

---

STOP: Did the installation work?

**Run this to test:**
```bash
python3 -c "import googleapiclient; print('Google API library installed!')"
```

**What do you see?**
- If you see "Google API library installed!" - you're good
- If you see an error - tell me what it says

---

USER: [Student confirms installation]

---

ACTION: When student responds:

**IF installed successfully:**
- "Perfect. Now let's test connecting to Drive."

**IF they get a ModuleNotFoundError:**
- "Try running the pip install command again, but with --user flag: `pip3 install --user [packages]`"
- "Or check if you're using the right Python version: `which python3`"

**IF they're on Windows and having issues:**
- "Windows sometimes needs: `python -m pip install [packages]` instead of pip3."

**Then:** "Time to test the Drive connection..."

---

### Step 6: Test Drive Connection

**What you're doing:** Writing a simple script that lists files in your Drive, just to prove authentication works.

**Use Claude Code to create this file:**

Tell me: "Create a file called `test_drive_connection.py` with code that:
1. Authenticates with Google Drive using credentials.json
2. Lists the first 10 files in my Drive
3. Uses the OAuth flow to get permission
4. Saves the token to token.json for future use"

Let Claude Code generate the script. It should handle the OAuth flow properly.

**Once the file is created, run it:**

```bash
python3 test_drive_connection.py
```

**What happens:**
1. Your web browser will open automatically
2. Google will ask you to sign in (if you're not already)
3. Google will show: "Invoice Drive Automation wants to access your Google Drive"
4. Click "Continue" or "Allow"
5. You might see "This app isn't verified" - click "Advanced" then "Go to Invoice Drive Automation (unsafe)"
   - This is normal! It's YOUR app, you just haven't verified it with Google (which costs money and takes weeks)
6. Google will ask "Allow Invoice Drive Automation to see, edit, create, and delete only the specific Google Drive files you use with this app?"
7. Click "Allow"
8. You'll see "The authentication flow has completed. You may close this window."
9. Go back to your terminal

**In your terminal, you should see:**
- A list of files from your Drive
- Something like: "File: Document.pdf (ID: 1234abcd...)"

**Also, a new file appears: `token.json`**
- This stores your access token
- Your script will use this from now on (won't ask for permission again)
- Keep this file safe too (don't commit to GitHub)

---

STOP: This is the critical test. Did the OAuth flow work?

**Tell me:**
1. Did your browser open and show the Google permission screen? (Yes/No)
2. Did you click "Allow"?
3. Does your terminal show a list of Drive files?
4. Do you see a token.json file in your folder?

If ANY of these didn't happen, tell me exactly what you saw so I can troubleshoot.

---

USER: [Student reports OAuth flow results]

---

ACTION: When student responds:

**IF everything worked:**
- "EXCELLENT! You just completed OAuth authentication. The hard part is over."
- "That token.json file is your golden ticket - your script can now access Drive without asking permission every time."
- "Now we build the actual automation."

**IF browser didn't open:**
- "The script should open your browser automatically. If it didn't, check if there's a URL printed in the terminal. Copy/paste that into your browser manually."

**IF they see 'app isn't verified':**
- "That's normal! Click 'Advanced' then 'Go to Invoice Drive Automation (unsafe)'. It's safe - it's YOUR app. Google just wants you to verify apps publicly, which we don't need for personal use."

**IF they get a 'redirect_uri_mismatch' error:**
- "That means the OAuth client type is wrong. Go back to Google Cloud Console > Credentials, delete the OAuth client, and recreate it as 'Desktop app' (not Web application)."

**IF token.json was created and files listed:**
- "You're ready! Delete test_drive_connection.py - we don't need it anymore. Now we build the real watcher script."

**Then:** "On to Phase 3 - building the actual Drive watcher..."

---

## Phase 3: Building the Drive Invoice Watcher

**What you're doing:** Creating a script that:
1. Watches a specific Google Drive folder
2. Detects new PDF files
3. Downloads them
4. Processes them with invoice_processor.py
5. Moves them to a "Processed" folder
6. Logs everything

---

### Step 7: Create Drive Folders

**First, let's set up the folder structure in Google Drive:**

1. Go to https://drive.google.com
2. Create a new folder: "Invoices - To Process"
3. Create another folder: "Invoices - Processed"
4. Open "Invoices - To Process"
5. Look at the URL in your browser

The URL will look like:
```
https://drive.google.com/drive/folders/1a2B3c4D5e6F7g8H9i0J
```

That long string at the end (`1a2B3c4D5e6F7g8H9i0J`) is the **folder ID**.

**Copy both folder IDs:**
- Folder ID for "Invoices - To Process": _______________
- Folder ID for "Invoices - Processed": _______________

You'll need these in a minute.

---

STOP: Do you have both folder IDs copied?

**Paste them here:**
- To Process folder ID: [paste yours]
- Processed folder ID: [paste yours]

---

USER: [Student provides folder IDs]

---

ACTION: When student responds:

**IF they have both IDs:**
- "Perfect! Those IDs are how we'll tell the script which folders to watch and move files to."

**IF they can't find the ID:**
- "Open the folder in Drive, then look at the URL in your browser's address bar. Everything after '/folders/' is the ID."

**IF they only have one:**
- "Create both folders. We need a source folder (new invoices) and a destination folder (processed invoices)."

**Then:** "Now let's build the watcher script using Claude Code..."

---

### Step 8: Build the Main Script

**Now use Claude Code to build the automation.**

**Tell me:**

"Create a file called `drive_invoice_watcher.py` that:

1. Connects to Google Drive using token.json (or creates it from credentials.json if first run)
2. Watches the folder ID: [STUDENT'S TO PROCESS FOLDER ID]
3. Lists all PDF files in that folder
4. For each PDF:
   - Download it to a temp folder
   - Call invoice_processor.py to extract data
   - Move the file in Drive to folder ID: [STUDENT'S PROCESSED FOLDER ID]
5. Log each step to a file called `automation.log`
6. Handle errors gracefully (if processing fails, don't move the file)
7. Add a `--once` flag to run once, or run continuously (check every 5 minutes by default)

Requirements:
- Use the Google Drive API v3
- Use invoice_processor.py from Lesson 2.2 (import it as a module)
- Create a temp folder for downloads
- Clean up temp files after processing
- Log timestamps and file names
- If a file fails to process, log the error but continue with other files"

Let Claude Code generate the script.

**Key functions you should see in the generated code:**
- `authenticate_drive()` - Handles OAuth
- `list_files_in_folder(folder_id)` - Gets files from folder
- `download_file(file_id, destination)` - Downloads PDF
- `move_file(file_id, new_folder_id)` - Moves file after processing
- `process_invoice(pdf_path)` - Calls your invoice_processor
- `watch_folder()` - Main loop

---

STOP: Let Claude Code generate the script, then review it.

**Once generated, tell me:**
1. Does the script have all the functions listed above?
2. Does it import invoice_processor?
3. Does it use the folder IDs you provided?
4. Does it create a log file?

Show me the first 50 lines of the generated script so I can verify it looks correct.

---

USER: [Student shares generated script]

---

ACTION: When student responds:

**Review the script they share:**

**IF it looks good (has all required functions, proper error handling, logging):**
- "Great! That looks solid. A few things to check:
  1. Make sure the folder IDs are in the code (either hardcoded or as config variables)
  2. Verify it imports invoice_processor correctly
  3. Check that it creates a 'temp' folder for downloads
  4. Confirm it has logging setup with timestamps"

**IF it's missing error handling:**
- "Add try/except blocks around the download and processing steps. If one file fails, we should continue with others."

**IF it doesn't have the --once flag:**
- "Add an argument parser so you can run `python3 drive_invoice_watcher.py --once` for testing vs. continuous mode."

**IF it looks complete:**
- "Perfect! Let's test it."

**Then:** "Before we run it on real invoices, let's test with a dummy PDF..."

---

### Step 9: Test the Watcher

**Testing approach:**
1. Test with a dummy PDF first
2. Verify it downloads, processes, and moves
3. Check the log file
4. Then test with real invoices

**Create a test PDF:**

1. Create a simple text file and save it as test-invoice.pdf (or use any PDF)
2. Upload it to your "Invoices - To Process" folder in Google Drive
3. Wait a few seconds for it to appear

**Run the watcher in --once mode:**

```bash
python3 drive_invoice_watcher.py --once
```

**What should happen:**
1. Script authenticates (uses token.json)
2. Checks the "To Process" folder
3. Finds test-invoice.pdf
4. Downloads it to temp folder
5. Tries to process it (might fail if it's not a real invoice - that's okay)
6. Moves it to "Processed" folder (or leaves it if processing failed)
7. Logs everything to automation.log
8. Exits

**Check the results:**
1. Look in Google Drive - did the file move to "Invoices - Processed"?
2. Look at automation.log - what does it say?
3. Check your terminal output - any errors?

---

STOP: Run the test and report back.

**Tell me:**
1. Did the script run without crashing? (Yes/No)
2. Did the file move to the Processed folder? (Yes/No)
3. What does automation.log say? (Share the last few lines)
4. Any errors in the terminal? (Copy/paste if yes)

---

USER: [Student reports test results]

---

ACTION: When student responds:

**IF everything worked:**
- "Excellent! Your watcher is working. Now let's test with a real invoice from Lesson 2.2."

**IF file didn't move:**
- "Check the log - did processing succeed? The script should only move files if processing worked."
- "If processing failed, that's actually correct behavior - we don't want to move files that failed."

**IF there's an authentication error:**
- "Delete token.json and run again - it'll re-authenticate."

**IF there's a folder permission error:**
- "The script can only access files it creates OR files in folders you explicitly give it access to. Make sure the folders are in your Drive, not a shared folder."

**IF it worked with the test file:**
- "Now try with a real invoice from Lesson 2.2. Upload one to the 'To Process' folder and run the script again."

**Then:** "Once you've verified it works with real invoices, let's set up automatic scheduling..."

---

## Phase 4: Scheduling the Automation

**What you're doing:** Making the script run automatically without you.

**Two approaches:**
1. **Continuous running** - Script runs forever, checking every 5 minutes
2. **Cron job** - System runs the script on a schedule

We'll set up continuous running (easier) with instructions for cron as optional.

---

### Step 10: Run in Continuous Mode

**Your script should have a continuous mode (if not, we'll add it).**

**Test continuous mode:**

```bash
python3 drive_invoice_watcher.py
```

(No --once flag)

**What should happen:**
1. Script starts
2. Checks the folder
3. Processes any files
4. Waits 5 minutes
5. Repeats forever (until you stop it)

**Let it run for a couple of checks to verify it works.**

**To stop it:**
Press `Ctrl+C`

**Check automation.log:**
You should see entries like:
```
[2026-02-04 13:45:00] Checking folder for new invoices...
[2026-02-04 13:45:02] Found 0 new files
[2026-02-04 13:45:02] Waiting 5 minutes before next check...
[2026-02-04 13:50:02] Checking folder for new invoices...
```

---

STOP: Does continuous mode work?

**Tell me:**
1. Did the script run continuously?
2. Does it check every 5 minutes?
3. Can you stop it with Ctrl+C?
4. Does the log show multiple check cycles?

---

USER: [Student confirms continuous mode works]

---

ACTION: When student responds:

**IF continuous mode works:**
- "Perfect! Now you have a choice: run this continuously on your computer (need to leave it running) OR set up a cron job (runs automatically on schedule, even if terminal closes)."

**Ask:** "Do you want to learn how to set up a cron job so this runs even when you're not logged in? (Yes/No/Later)"

**IF they want cron setup:**
- Continue to Step 11 (Cron Job Setup)

**IF they're happy with continuous mode:**
- "That's fine. Just keep the script running in a terminal window. You can minimize it and forget about it."
- Skip to Phase 5 (Testing & Documentation)

**IF the script isn't working:**
- Troubleshoot specific errors they're seeing

**Then based on their choice, continue...**

---

### Step 11: Optional - Cron Job Setup

**This is optional. Only do this if you want the script to run automatically on a schedule.**

**What's a cron job?**
- A scheduled task on Mac/Linux
- Runs at specific times without you doing anything
- Like a calendar reminder that runs code

**For this automation, we'll set it to run every hour** (not continuous checking, but close enough).

**Create a shell script wrapper:**

```bash
cat > run_drive_watcher.sh << 'EOF'
#!/bin/bash
cd /full/path/to/drive-invoice-automation
/usr/local/bin/python3 drive_invoice_watcher.py --once >> automation.log 2>&1
EOF
```

Replace `/full/path/to/drive-invoice-automation` with your actual folder path.

**Make it executable:**

```bash
chmod +x run_drive_watcher.sh
```

**Set up cron:**

1. Open cron editor:
```bash
crontab -e
```

2. Add this line (runs every hour at minute 0):
```
0 * * * * /full/path/to/drive-invoice-automation/run_drive_watcher.sh
```

3. Save and exit (in vi/vim: press Escape, type `:wq`, press Enter)

**Verify cron is set up:**
```bash
crontab -l
```

You should see your entry.

**The script will now run every hour automatically.**

---

STOP: If you set up cron, tell me.

**Did you:**
1. Create run_drive_watcher.sh?
2. Make it executable?
3. Add it to cron?
4. Verify with `crontab -l`?

If you skipped this (totally fine), just tell me and we'll move on.

---

USER: [Student reports cron setup status]

---

ACTION: When student responds:

**IF they set up cron:**
- "Great! Your automation will now run every hour. Test it by dropping a file in the 'To Process' folder and waiting for the next hour mark."
- "Check automation.log to see when it ran."

**IF they skipped cron:**
- "No problem. Continuous mode works fine. Just keep the script running."

**IF they're on Windows:**
- "Windows doesn't have cron. Use Task Scheduler instead (similar concept). Google 'Windows Task Scheduler Python script' if you want to set this up."

**Then:** "Let's move to final testing and documentation..."

---

## Phase 5: Final Testing & Documentation

**What you're doing:** Verifying the complete workflow and documenting for the Finance team.

---

### Step 12: End-to-End Test

**Complete workflow test:**

1. Take a real invoice PDF from Lesson 2.2
2. Upload it to "Invoices - To Process" in Google Drive
3. Let the watcher script detect and process it (or run manually with --once)
4. Verify:
   - File moves to "Invoices - Processed"
   - Data appears in Airtable
   - automation.log shows success
   - No errors in terminal

**Do this 3 times with different invoices to ensure it's reliable.**

---

STOP: Run the complete test.

**Report:**
1. How many invoices did you test?
2. Did they all process successfully?
3. Did data appear in Airtable correctly?
4. Any issues or edge cases you noticed?

---

USER: [Student reports test results]

---

ACTION: When student responds:

**IF all tests passed:**
- "Perfect! Your automation is production-ready."

**IF some failed:**
- "Let's troubleshoot what failed. Common issues:
  - File format not supported (only PDFs work)
  - Invoice format not recognized (your invoice_processor.py might need updates)
  - Airtable authentication expired (check API key)
  - Network issues (Drive download failed)"
- Diagnose specific failures and fix

**IF everything works consistently:**
- "Time to document this for Marcus and the Finance team..."

**Then:** "Let's create the documentation..."

---

### Step 13: Create Documentation

**Create a README.md file in your project folder:**

**Use Claude Code:**

Tell me: "Create a README.md file that explains:
1. What this automation does
2. How to set it up (Google Cloud, OAuth, folders)
3. How to run it (continuous mode vs. cron)
4. How to troubleshoot common issues
5. How to add more invoice folders if needed
6. Where to find logs
7. Who to contact if it breaks (your name/email)

Make it clear enough that Marcus (Finance Lead) could hand this to someone else and they could maintain it."

Let Claude Code generate the README.

**Also create a configuration file for easy updates:**

Tell Claude Code: "Create a config.py file that stores:
- Folder IDs (so users don't have to edit the main script)
- Check interval (5 minutes default)
- Log file location
- Airtable credentials (reference to invoice_processor)

Make it obvious what settings can be changed."

---

STOP: Once you have README.md and config.py created, review them.

**Check:**
1. Is the README clear enough for a non-technical person?
2. Does config.py make it easy to change folder IDs?
3. Did you document how to troubleshoot common errors?

Share the README with me so I can review it.

---

USER: [Student shares README]

---

ACTION: When student responds:

**Review the README:**

**IF it's clear and complete:**
- "Excellent documentation. This is professional-grade. Anyone could maintain this."

**IF it's missing key info:**
- "Add a section on:
  - What to do if authentication expires (delete token.json and re-run)
  - How to check if the script is running (look at automation.log)
  - What to do if invoices aren't processing (check Airtable connection from Lesson 2.2)"

**IF it's too technical:**
- "Simplify the language. Marcus is smart but not technical. Avoid jargon like 'OAuth flow' - just say 'Google permission screen.'"

**When README is good:**
- "Perfect! Now let's set this up for the Finance team's final handoff..."

**Then:** "One more thing - let's add email notifications for errors..."

---

### Step 14: Optional - Email Notifications

**This is optional but recommended for production automations.**

**If you want the script to email you when something goes wrong:**

Tell Claude Code: "Add email notification functionality to drive_invoice_watcher.py:
- Send email when processing fails
- Send email if no files have been processed in 7 days (might mean the script crashed)
- Use Python's smtplib with Gmail SMTP
- Make email settings configurable in config.py (recipient email, SMTP credentials)
- Don't spam - max 1 email per error per day"

**This requires:**
- Gmail account
- App-specific password (not your regular password)
- SMTP setup

**If you want to set this up:**
- I'll guide you through Gmail app password creation
- Otherwise, skip this - logs are enough for monitoring

---

STOP: Do you want to add email notifications?

**Options:**
1. Yes, I want to set up email alerts
2. No, logs are enough for now
3. Maybe later

---

USER: [Student chooses notification approach]

---

ACTION: When student responds:

**IF they want email notifications:**
- Walk them through Gmail app password setup
- Help them configure SMTP in config.py
- Test with a dummy error

**IF they skip it:**
- "No problem. You can always add this later. Logs are fine for monitoring."

**Then:** "Alright, let's wrap up and hand this off to Marcus..."

---

## Phase 6: Handoff to Finance Team

**What you're doing:** Making sure the Finance team can actually use this.

---

### Step 15: Demo & Training

**Schedule a quick meeting with Marcus (in the real world, this would be a real meeting - for this course, just imagine it).**

**Demo the workflow:**

1. Show Marcus the "Invoices - To Process" folder in Google Drive
2. Drop a test invoice in
3. Show how it automatically appears in Airtable
4. Show the "Invoices - Processed" folder
5. Show the automation.log file
6. Explain how to tell if it's running (check log timestamps)

**What Marcus needs to know:**
- "Drop invoices in this folder, they'll be processed within 5 minutes"
- "Check the 'Processed' folder if you need to find an old invoice"
- "If something seems broken, check automation.log - email me if you see errors"
- "Don't rename the folders - the script looks for specific folder IDs"

**Questions Marcus might ask:**

**"What if I need to reprocess an invoice?"**
- "Move it from 'Processed' back to 'To Process' - the script will pick it up again."

**"What if the script stops working?"**
- "Check if your computer is on and the terminal is still running (if continuous mode) or if you set up cron, check automation.log for errors and email me."

**"Can we add more people's invoices?"**
- "Yes! Just share the 'To Process' folder with them in Google Drive. They can drop files and it'll work."

**"What happens if a PDF isn't an invoice?"**
- "The processor will try and might fail. Failed files stay in 'To Process' and log an error. You'd need to manually remove bad files."

---

STOP: Imagine you're presenting this to Marcus.

**Write out:**
1. The 3 key points you'd tell him (simplest explanation of how it works)
2. The one thing you'd warn him about (common mistake to avoid)
3. How he'd know if something went wrong

Practice explaining technical work to non-technical people - this is a critical AI Operator skill.

---

USER: [Student writes their handoff explanation]

---

ACTION: When student responds:

**Review their explanation:**

**IF it's clear and simple:**
- "That's perfect. You explained technical concepts in business terms. This is a skill that makes or breaks AI Operators."

**IF it's too technical:**
- "Simplify. Marcus doesn't care about OAuth or APIs. He cares about: 'Drop PDF here, it shows up in Airtable.'"

**IF they forgot the warning:**
- "Always warn about common mistakes. For this: 'Don't rename the folders' is critical."

**Key points to emphasize:**
- Keep it simple
- Focus on what THEY do, not what the script does
- Always include "what to do if it breaks"
- Make it obvious how to tell if it's working

**Then:** "Great! Now let's measure the impact..."

---

## Phase 7: Measuring Impact

**What you're doing:** Proving the value of your automation.

---

### Step 16: Calculate Time Savings

**Before automation:**
- Marcus manually processed 20 invoices/day
- Each took 3 minutes (find PDF, open, read, type into Airtable)
- 20 invoices × 3 minutes = 60 minutes/day = 1 hour/day

**After automation:**
- Marcus drops PDFs in Drive folder
- Processing happens automatically
- Time spent: 30 seconds per invoice (just uploading)
- 20 invoices × 0.5 minutes = 10 minutes/day

**Time saved:**
- 60 - 10 = 50 minutes/day
- 50 minutes × 5 days = 250 minutes/week
- 250 minutes = 4.2 hours/week
- 4.2 hours × 4 weeks = ~17 hours/month

**Value:**
- If Marcus makes $30/hour
- $30 × 17 hours = $510/month in saved labor
- $510 × 12 months = $6,120/year

**Your time investment:**
- ~3 hours to build this automation
- ROI: Pays back in less than 1 week

**That's the impact you report to Sarah (CEO).**

---

STOP: Calculate the impact for YOUR use case (or use the numbers above).

**Write a 2-3 sentence impact summary:**
"This automation saves [X] hours per week by [what it does]. Over a year, that's [Y] hours saved, worth approximately $[Z] in labor costs. The automation took [A] hours to build, paying for itself in [B] days."

This is how you communicate value to executives.

---

USER: [Student writes impact summary]

---

ACTION: When student responds:

**Review their impact summary:**

**IF it's clear and quantified:**
- "Perfect! That's exactly how you communicate ROI to leadership. Numbers matter."

**IF they forgot time-to-payback:**
- "Always include how long it takes to pay for itself. Executives love '3 hours to build, pays back in 5 days.'"

**IF they focused on features instead of outcomes:**
- "Don't say 'uses Google Drive API and OAuth.' Say 'saves 17 hours per month.'"

**Key lesson:**
- "Always measure your automations. Time saved = your value as an AI Operator."

**Then:** "Alright, let's wrap up this lesson..."

---

## Lesson Wrap-Up

**What you built:**
- Google Drive automation that watches a folder
- Processes invoices automatically without manual intervention
- Moves files after processing
- Logs everything for monitoring
- Scheduled to run continuously or on cron
- Documented for team handoff

**What you learned:**

**Technical:**
- Google Cloud Console setup
- OAuth 2.0 authentication flow
- Google Drive API basics
- File watching patterns
- Scheduling automations (continuous vs. cron)
- Error handling in production automations

**AI Operator Skills:**
- Moving from local scripts to cloud integrations
- Designing user-friendly workflows (drop file → magic happens)
- Production-ready error handling and logging
- Documentation for non-technical users
- Measuring and communicating impact
- Team handoff and training

**Meta Skill:**
Cloud automation is about removing yourself from the process. Local scripts require you to run them. Cloud automations run WITHOUT you - that's when automation becomes truly valuable.

---

## Where Else This Applies

**This Google Drive pattern works for:**
- Contract review automation (legal team drops contracts, get summaries)
- Receipt processing (expense reports)
- Resume screening (HR drops resumes, get analysis)
- Report generation (drop data file, get formatted report)
- Image processing (drop photos, get resized/optimized versions)

**The file-watching pattern applies to:**
- Email attachments (process files from emails)
- Dropbox/OneDrive (same concept, different API)
- FTP servers (legacy systems)
- Webhooks (trigger automation on file upload)

**The skills you learned (OAuth, API setup, scheduling) transfer to:**
- Google Sheets automation
- Google Calendar automation
- Slack bot development
- Any OAuth-based API

**You now have a template for "watch folder → process file → move file" automations.**

---

## Troubleshooting Guide

**Common Issues:**

**"Browser won't open for OAuth"**
- Solution: Copy the URL from terminal and paste into browser manually

**"This app isn't verified" error**
- Solution: Click "Advanced" → "Go to [your app] (unsafe)" - it's YOUR app, it's safe

**"Insufficient permissions" error**
- Solution: Delete token.json, re-run script, grant permissions again

**"File not found in Drive"**
- Solution: Check folder IDs in config.py - make sure they're correct

**"Import error: invoice_processor not found"**
- Solution: Make sure invoice_processor.py is in the same folder as drive_invoice_watcher.py

**"Cron job not running"**
- Solution: Check paths in run_drive_watcher.sh are ABSOLUTE paths (not relative)
- Check cron logs: `grep CRON /var/log/syslog` (Linux) or `log show --predicate 'process == "cron"' --last 1h` (Mac)

**"Script crashes after a few hours"**
- Solution: Add error handling around Drive API calls (network can be flaky)
- Make sure your token doesn't expire (token.json should auto-refresh)

---

## Success Criteria for Lesson 2.3

Before moving to Lesson 2.4, make sure you can check these off:

- [ ] Set up Google Cloud project and enabled Drive API
- [ ] Created OAuth credentials and consent screen
- [ ] Successfully authenticated with Google Drive (token.json created)
- [ ] Created "To Process" and "Processed" folders in Drive
- [ ] Built drive_invoice_watcher.py that watches the folder
- [ ] Tested with real invoices - they process and move correctly
- [ ] Set up continuous running OR cron job for scheduling
- [ ] Created README.md documentation
- [ ] Created config.py for easy configuration
- [ ] Verified automation.log shows activity
- [ ] Calculated time savings and ROI
- [ ] Could explain the system to a non-technical person

**If you can check all those boxes, you're ready for Lesson 2.4.**

---

STOP: Final reflection.

**Answer these:**
1. What was the hardest part of this lesson? (Be honest)
2. On a scale of 1-10, how confident are you with Google OAuth now?
3. What's one other automation you could build with this Drive-watching pattern?
4. Are you ready to build a web interface in Lesson 2.4? (We'll take your invoice processor and make it a web app that anyone can use with a browser)

---

USER: [Student reflects on lesson]

---

ACTION: When student responds:

**Address what was hardest:**
- If OAuth: "Yeah, OAuth is always the worst part. Good news: you only have to do it once per API. Next time will be easier."
- If Drive API: "Google's documentation is confusing. You did great figuring it out."
- If debugging: "Debugging production automations is a key skill. You're building that muscle."

**Address confidence level:**
- If low (1-5): "That's okay. OAuth is confusing at first. As you use it more, it'll click."
- If medium (6-8): "Perfect. You don't need to be an expert - you just need to get it working."
- If high (9-10): "Great! You've mastered a skill most people find intimidating."

**Address their other automation idea:**
- "That's a great use case! You could totally build that with what you learned today."
- If it's a good idea, encourage them: "Actually, that might be your Lesson 2.6 project - a custom automation of YOUR choice."

**Transition to next lesson:**
- "You've now built two automations: local script (2.2) and cloud automation (2.3). Next up: web interface."
- "In Lesson 2.4, we'll turn your invoice processor into a web app that ANYONE can use with just a browser. No Python, no terminal, just upload and see results."
- "This is where automation becomes really shareable - you're building a tool others can use independently."
- "Ready? Take a break if you need one, then open Lesson 2.4 when you're ready."

**End with:**
- "Great work on this lesson. You built something production-ready. That's real AI Operator work."

---

## Additional Resources

**Google Drive API Documentation:**
- Official docs: https://developers.google.com/drive/api/v3/about-sdk
- Python quickstart: https://developers.google.com/drive/api/v3/quickstart/python
- OAuth explained: https://developers.google.com/identity/protocols/oauth2

**Troubleshooting OAuth:**
- Token expiration: https://developers.google.com/identity/protocols/oauth2#expiration
- Scopes explained: https://developers.google.com/drive/api/v3/about-auth

**Cron tutorials:**
- Mac/Linux: https://crontab.guru/ (cron schedule expressions)
- Cron syntax: https://en.wikipedia.org/wiki/Cron

**Alternative approaches:**
- Zapier/Make.com (no-code Drive watching, but limited)
- n8n workflows (visual automation builder)
- Google Apps Script (runs in Drive, no OAuth needed, but JavaScript)

**But you built it yourself. You own the code. That's the AI Operator way.**

---

**End of Lesson 2.3**

**Next:** Lesson 2.4 - Project 3: Invoice Upload Web App

---

*You just moved from local automation to cloud automation. Now you're ready to build user interfaces that make your automations accessible to everyone.*
