# How to Install Claude Code

Get set up in 10 minutes

---

# What You'll Need

- ✓ Mac, Windows, or Linux computer
- ✓ Internet connection
- ✓ Anthropic API key (I'll show you how)
- ✓ 10 minutes

**That's it!**

No technical prerequisites. If you can browse the web, you can do this.

---

# Step 1: Get Your API Key

**Create Anthropic Account:**

1. Go to **console.anthropic.com**
2. Sign up (free)
3. Add payment method (pay-as-you-go)
4. Navigate to API Keys
5. Create new key
6. **Copy and save it** (you'll need this!)

This is like a password that lets Claude Code access the AI.

It's pay-as-you-go - you only pay for what you use.

For this course, expect **$10-15 total.**

---

# Pricing Reality Check

**Typical course usage:**
- Module 1 (7 lessons): ~$2-3
- Module 2 (7 lessons): ~$3-5
- Building automations: ~$5-10
- **Total: $10-15 for entire course**

**What you get:**
- AI that writes code for you
- Access to Claude Sonnet 4.5
- Unlimited learning
- Real automations built

A few bucks for an AI coding assistant? That's a steal.

---

# Step 2: Install Node.js

**Check if you have Node.js:**

**Mac/Linux:** Open Terminal, type:
```
node --version
```

**Windows:** Open Command Prompt, type:
```
node --version
```

**If you see a version number:** You're good!

**If not:** Download from **nodejs.org** (LTS version)

Claude Code needs Node.js to run. It's a simple installer.

---

# Step 3: Install Claude Code

**One command:**

```bash
npm install -g @anthropics/claude-code
```

**That's it.**

**On Mac/Linux, you might need:**
```bash
sudo npm install -g @anthropics/claude-code
```

Copy this command exactly as shown.

If you get a permission error on Mac/Linux, add 'sudo' at the beginning.

---

# Step 4: Set Up Your API Key

**Tell Claude Code your API key:**

```bash
claude auth login
```

Paste your API key when prompted.

**It will save it securely.**

This connects Claude Code to your Anthropic account.

---

# Step 5: Test It!

**Verify installation:**

```bash
claude
```

**You should see:**
- Claude Code welcome message
- Cursor blinking, ready for input

**Try:** "Hello, Claude!"

If Claude responds - congratulations, you're ready!

---

# Optional: Install OpCode

**Better visual experience**

**OpCode** = Beautiful GUI for Claude Code

- Session management
- File viewer
- Usage tracking
- **Free!**

**Download:** opcode.sh

Not required, but recommended for a nicer experience with file viewing and conversation tracking.

---

# Troubleshooting

**Common Issues:**

**"Command not found"**
→ Restart terminal after installing Node.js

**"Permission denied"**
→ Use `sudo` on Mac/Linux

**"API key invalid"**
→ Double-check you copied the entire key

**"npm not found"**
→ Node.js didn't install correctly, try again

99% of issues are solved by restarting your terminal or reinstalling Node.js.

---

# You're Ready!

**Installation Complete ✓**

**What you now have:**
- ✓ Claude Code installed
- ✓ API key configured
- ✓ Ready to build automations

**Next up:** Getting started with the course!

---

# Quick Reference

**Commands to remember:**

| Command | What it does |
|---------|--------------|
| `claude` | Start Claude Code |
| `claude auth login` | Set up API key |
| `claude --version` | Check version |
| `/help` | Get help in Claude |
| `Ctrl+C` | Exit Claude Code |

Don't worry about memorizing - Claude can remind you of these anytime.

---

# Next Video: Course Overview

📺 **Next:** How to Get Started with the Course

🎓 **After That:** Module 1, Lesson 1

🚀 **End Goal:** 4 working automations

You're installed. You're ready.

Next video shows you exactly how to start the course and what you're going to build.

**Ready? Let's go.**
