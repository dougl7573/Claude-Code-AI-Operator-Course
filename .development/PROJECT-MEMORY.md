# Project Memory - Claude Code for AI Operators Course

**Created:** February 4, 2026
**Project:** Building a comprehensive Claude Code course for AI Operators
**Lead:** Tom Crawshaw

---

## 🎯 Project Vision

Create a hands-on, interactive course that teaches students to become AI Operators - professionals who investigate manual processes in companies and build real, working automations using Claude Code.

**Key Differentiator:** Unlike other courses that teach general Claude Code usage or basic programming, this course focuses specifically on automation thinking and building production-ready integrations.

---

## 📝 Design Decisions & Context

### **Course Name & Positioning**
- **Name:** "Claude Code for AI Operators"
- **Not:** "Claude Code for Automation Builders" (too narrow)
- **Target Audience:** People deployed in companies to identify and automate manual processes

### **Company Scenario**
- **Company:** Precision Manufacturing Co. (mid-sized manufacturer, 200 employees, $50M revenue)
- **Role:** AI Operations Lead
- **Mission:** Save 100+ hours/month by automating manual processes across 5 departments
- **Why Manufacturing?** Realistic, relatable, lots of manual process pain points
- **NOT a digital agency:** Original idea was digital agency, pivoted to manufacturing for broader appeal

### **Key Projects Students Build**

**Project 1: PDF Invoice Processing (Local → Airtable)**
- Start with local folder processing (we provide sample invoices)
- Extract: invoice #, vendor, date, amount
- Insert into Airtable automatically
- **Why this project:** High impact (Finance saves 2-3 hours/day), realistic, teaches PDF parsing + API integration
- **Critical decision:** NO Gmail API initially (too complex). Start local, add Google Drive later.

**Project 2: Google Drive Automation**
- Watch Drive folder for new PDFs
- Auto-process and organize
- **Why Google Drive not Gmail:** Simpler OAuth, easier for beginners

**Project 3: Invoice Upload Web App**
- Build web interface for PDF upload
- Process on backend, deploy to Vercel
- **Why this:** Deployable tool, shareable URL, shows web app as automation

**Project 4: Student's Choice**
- Apply skills to their real use case

### **API Choices**
- ✅ **Airtable** - Free tier, easy to set up, good for databases
- ✅ **Google Sheets/Drive** - Free, familiar, simpler than Gmail
- ❌ **NO Stripe** - Too complex, requires payment setup
- ❌ **NO Gmail API initially** - OAuth complexity, can add as advanced optional

### **Editor Recommendation**
- **Primary:** OpCode (purpose-built for Claude Code, handles all file types)
- **Alternative:** Obsidian mentioned but limited to markdown
- **NOT Cursor:** Too code-focused, overwhelming for beginners

### **MCP Approach**
- **Introduce MCPs** in Module 1, Lesson 4
- **Synta MCP (not Sinter!)** for n8n - OPTIONAL, not required
- **Focus:** Building automations in code primarily, n8n is just one option
- **Don't over-emphasize** any single MCP

### **GitHub Integration**
- Students probably DON'T use GitHub currently
- Need detailed walkthrough in Module 2, Lesson 5
- Position as "backup & collaboration tool"
- Not assumed knowledge

---

## 🏗️ Course Structure

### **Module 1: AI Operator Fundamentals** (7 lessons, ~4 hours)
1. Introduction & AI Operator Role
2. Investigating Manual Processes
3. Working with Data & APIs
4. Introduction to MCPs
5. Agents & Parallel Processing
6. Custom Sub-Agents for Operations
7. CLAUDE.md: Your Automation Playbook

### **Module 2: Building Real Automations** (7 lessons, ~8 hours)
1. Automation Design & Planning
2. Project 1: PDF Invoice Processing
3. Project 2: Google Drive Automation
4. Project 3: Invoice Upload Web App
5. Version Control with GitHub
6. Advanced: Multi-Step Automation (optional)
7. Documentation & Handoff

**Total:** 12-15 hours of hands-on learning

---

## 🎓 Teaching Methodology

**Format:** Interactive CLAUDE.md files
- Each lesson is a CLAUDE.md file that guides Claude's behavior
- Uses STOP/USER/ACTION format for pacing
- Students DO everything themselves (no passive videos)
- Claude guides step-by-step conversationally

**Lesson Structure Template:**
```markdown
# Lesson X.X: Title

[Hook/Introduction]

STOP: Question or instruction to student

USER: Expected response

ACTION: What Claude should do

[Next section...]

## Meta Skill
What broader skill this lesson teaches

## Where Else This Applies
Real-world examples beyond the scenario

## Success Criteria
- [ ] Checklist of learning objectives
```

**Inspiration:** Based on Carl Vellotti's "Claude Code for Everyone" course structure, but adapted for automation focus

---

## 📊 Key Metrics & Goals

**Student Success:**
- Can complete Module 1 with zero coding experience
- Build 3+ working automations in Module 2
- Deploy at least one tool to production (Vercel)
- Have GitHub portfolio to show employers/clients

**Business Value:**
- Students save actual time in their real jobs
- Automations are production-ready, not demos
- Documentation enables maintenance by others

---

## 🚧 Current Status

### **Completed:**
- ✅ Complete course plan (COURSE-PLAN.md)
- ✅ Course structure (course-structure.json)
- ✅ README.md
- ✅ Company scenario (SCENARIO.md)
- ✅ Departments overview (DEPARTMENTS.md)
- ✅ Finance department interview (finance-invoice-nightmare.md)
- ✅ Expected invoice data structure (expected-output.json)
- ✅ Folder structure created
- ✅ Committed to git

### **In Progress:**
- 🔄 Lesson 1.1 (Introduction & AI Operator Role)
- 🔄 Sample invoice PDFs (need 5 realistic examples)

### **TODO:**
- ⏳ Remaining Module 1 lessons (1.2 - 1.7)
- ⏳ Module 2 lessons (2.1 - 2.7)
- ⏳ Other department interview files
- ⏳ Starter code templates
- ⏳ Reference materials (API cheatsheets, troubleshooting)
- ⏳ Sample Airtable base structure
- ⏳ Beta testing protocol

---

## 💡 Important Context & Decisions

### **Why This Scenario Works**
The Precision Manufacturing scenario was chosen because:
1. **Relatable:** Most companies have manual processes
2. **Multiple automation types:** PDFs, data sync, emails, documents
3. **Clear ROI:** Hours saved is measurable
4. **Progressive complexity:** Start simple, build up
5. **Real pain points:** Based on actual business problems

### **Design Philosophy**
- **Practical over theoretical:** Build real things
- **Progressive complexity:** Local → Cloud → Deployed
- **Documentation-first:** Every automation needs runbooks
- **Portfolio-building:** Students create showable work
- **No coding prerequisites:** Claude Code does heavy lifting

### **What Makes This Different**
vs. Carl Vellotti's course:
- Different scenario (manufacturing vs. coffee shop)
- Automation focus vs. general business
- API integrations vs. simple web app
- AI operator role vs. manager role

vs. Generic automation courses:
- Claude Code as primary tool
- AI-first approach
- CLAUDE.md documentation emphasis
- Agent-driven workflows

vs. Programming courses:
- Not teaching syntax
- Teaching automation thinking
- Focus on results, not code quality
- Claude does the coding

---

## 🔧 Technical Stack

**Required:**
- Claude Code
- Python 3.8+
- OpCode (or text editor)
- Airtable account (free)
- Google account

**Learned During Course:**
- GitHub
- Vercel deployment
- API authentication
- PDF parsing libraries
- Cron/scheduling

**Optional:**
- Synta MCP for n8n
- Node.js (if prefer JavaScript)

---

## 📚 Reference Materials

**Inspiration Sources:**
- Carl Vellotti's "Claude Code for Everyone" course
- Real automation consulting experience
- Common business pain points

**Links:**
- Original course: https://github.com/carlvellotti/claude-code-everyone-course
- Synta MCP docs: https://mcp-docs.synta.io/installation

---

## 🎯 Next Steps (Priority Order)

1. **Write Lesson 1.1** - Sets the tone, critical first impression
2. **Create sample invoice PDFs** - Needed for testing in Module 2
3. **Write remaining Module 1 lessons** - Complete fundamentals
4. **Create starter code templates** - Help students get unstuck
5. **Write Module 2 lessons** - Build the automations
6. **Beta testing** - 3-5 students, iterate on feedback

---

## 💭 Open Questions & Considerations

**Not Yet Decided:**
- Should we create video walkthroughs or keep it purely text-based?
- Do we need a companion Discord/community?
- Pricing model (free? paid? freemium?)
- Platform for delivery (GitHub? Course platform? Both?)

**Potential Challenges:**
- Students might have different OS (Mac/Windows/Linux) - need to test all
- API rate limits on free tiers - document clearly
- Students getting stuck on authentication - troubleshooting guides critical
- Maintaining course as Claude Code updates - versioning strategy

**Future Enhancements:**
- Module 3: Advanced integrations
- Module 4: AI-powered automations (LLM APIs)
- Module 5: Enterprise deployment
- Library of automation templates
- Student showcase gallery

---

## 📝 Development Notes

**Working Directory:** `/Users/tomcrawshaw/AI OPERATOR OS/Claude-Code-AI-Operator-Course/`

**Git Repo:** Local repository, can push to GitHub when ready

**File Naming Conventions:**
- Lessons: `X.X-descriptive-name/CLAUDE.md`
- Scenarios: `kebab-case.md`
- Data: `snake_case.json` or `.csv`

---

*This file captures the context and decisions made during course development. Update as the project evolves.*
