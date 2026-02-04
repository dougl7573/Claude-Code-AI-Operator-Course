# Video 2: How to Install Claude Code

**Duration:** 5-7 minutes
**Tone:** Clear, step-by-step, reassuring

---

## Slide 1: Title
**How to Install Claude Code**
*Get set up in 10 minutes*

**Speaker Notes:**
"Let's get Claude Code installed on your computer. This is simpler than you think - I'll walk you through every step."

**Visual:** Claude Code logo + installation icon

---

## Slide 2: What You'll Need
**Before We Start:**

- ✓ Mac, Windows, or Linux computer
- ✓ Internet connection
- ✓ Anthropic API key (I'll show you how)
- ✓ 10 minutes

**That's it!**

**Speaker Notes:**
"No technical prerequisites. If you can browse the web, you can do this."

**Visual:** Checklist with icons

---

## Slide 3: Step 1 - Get Your API Key
**Create Anthropic Account**

1. Go to **console.anthropic.com**
2. Sign up (free)
3. Add payment method (pay-as-you-go)
4. Navigate to API Keys
5. Create new key
6. **Copy and save it** (you'll need this!)

**Speaker Notes:**
"First, you need an API key from Anthropic. This is like a password that lets Claude Code access the AI. It's pay-as-you-go - you only pay for what you use. For this course, expect $5-10 total."

**Visual:** Screenshots of each step in Anthropic console

---

## Slide 4: Pricing Reality Check
**How Much Does This Cost?**

**Typical course usage:**
- Module 1 (7 lessons): ~$2-3
- Module 2 (7 lessons): ~$3-5
- Building automations: ~$5-10
**Total: $10-15 for entire course**

**What you get:**
- AI that writes code for you
- Access to Claude Sonnet 4.5
- Unlimited learning
- Real automations built

**Speaker Notes:**
"Let's be real about cost. It's not free, but it's insanely cheap for what you're getting. A few bucks for an AI coding assistant? That's a steal."

**Visual:** Cost breakdown with comparison (coffee, Netflix, etc.)

---

## Slide 5: Step 2 - Install Node.js (if needed)
**Check if You Have Node.js**

**Mac/Linux:**
Open Terminal, type: `node --version`

**Windows:**
Open Command Prompt, type: `node --version`

**If you see a version number:** You're good!
**If not:** Download from **nodejs.org** (LTS version)

**Speaker Notes:**
"Claude Code needs Node.js to run. Check if you have it first. If not, download the LTS version from nodejs.org - it's a simple installer."

**Visual:** Terminal screenshot showing version check + nodejs.org website

---

## Slide 6: Step 3 - Install Claude Code
**One Command:**

```bash
npm install -g @anthropics/claude-code
```

**That's it.**

**On Mac/Linux, you might need:**
```bash
sudo npm install -g @anthropics/claude-code
```

**Speaker Notes:**
"Now install Claude Code with this one command. Copy it exactly as shown. If you're on Mac or Linux and get a permission error, add 'sudo' at the beginning."

**Visual:** Terminal showing the installation command and progress

---

## Slide 7: Step 4 - Set Up Your API Key
**Tell Claude Code Your API Key**

```bash
claude auth login
```

Paste your API key when prompted.

**It will save it securely.**

**Speaker Notes:**
"Now connect Claude Code to your Anthropic account. Run this command and paste the API key you copied earlier."

**Visual:** Terminal showing auth login process

---

## Slide 8: Step 5 - Test It!
**Verify Installation**

```bash
claude
```

**You should see:**
- Claude Code welcome message
- Cursor blinking, ready for input

**Try:** "Hello, Claude!"

**Speaker Notes:**
"Test that everything works. Type 'claude' and hit enter. You should see Claude respond. If you do - congratulations, you're ready!"

**Visual:** Terminal showing successful Claude Code launch

---

## Slide 9: Optional - Install OpCode
**Better Visual Experience**

**OpCode** = Beautiful GUI for Claude Code
- Session management
- File viewer
- Usage tracking
- Free!

**Download:** opcode.sh

**Not required, but recommended.**

**Speaker Notes:**
"For a better experience, install OpCode. It's a visual interface for Claude Code. Makes it easier to see your files and track conversations. Totally optional but nice to have."

**Visual:** OpCode interface screenshot

---

## Slide 10: Troubleshooting
**Common Issues:**

**"Command not found"**
→ Restart terminal after installing Node.js

**"Permission denied"**
→ Use `sudo` on Mac/Linux

**"API key invalid"**
→ Double-check you copied the entire key

**"npm not found"**
→ Node.js didn't install correctly, try again

**Speaker Notes:**
"If something goes wrong, these are the usual culprits. 99% of issues are solved by restarting your terminal or reinstalling Node.js."

**Visual:** Error messages with solutions

---

## Slide 11: You're Ready!
**Installation Complete ✓**

**What you now have:**
- ✓ Claude Code installed
- ✓ API key configured
- ✓ Ready to build automations

**Next up:**
Getting started with the course!

**Speaker Notes:**
"That's it - you're ready to start building. In the next video, I'll show you how to get started with the full AI Operator course."

**Visual:** Checkmarks + celebration

---

## Slide 12: Quick Reference Card
**Commands to Remember:**

| Command | What it does |
|---------|--------------|
| `claude` | Start Claude Code |
| `claude auth login` | Set up API key |
| `claude --version` | Check version |
| `/help` | Get help in Claude |
| Ctrl+C | Exit Claude Code |

**Speaker Notes:**
"Here are the basic commands you'll use. Don't worry about memorizing - Claude can remind you of these anytime."

**Visual:** Command reference table

---

## Slide 13: Call to Action
**Next Video: Course Overview**

📺 **Next:** How to Get Started with the Course
🎓 **After That:** Module 1, Lesson 1
🚀 **End Goal:** 4 working automations

**Ready? Let's go.**

**Speaker Notes:**
"You're installed. You're ready. Next video shows you exactly how to start the course and what you're going to build. See you there!"

**Visual:** Next steps roadmap

---

## Production Notes:
- Show actual installation process (screen recording)
- Pause at each step to let viewers follow along
- Show both Mac and Windows where different
- Reassure about technical aspects
- Mention you can restart video anytime
- Include timestamps in description for each step
- Link to written installation guide in description
