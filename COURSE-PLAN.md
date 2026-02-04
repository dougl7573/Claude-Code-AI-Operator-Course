# Claude Code for AI Operators - Course Plan

**Version:** 1.0
**Created:** February 4, 2026
**Target Audience:** AI Operators, Automation Builders, Process Improvement Specialists

---

## 🎯 Course Overview

**Mission:** Train AI Operators to investigate manual processes in companies and build practical automations using Claude Code.

**Core Philosophy:**
- AI Operators identify automation opportunities and build solutions
- Focus on real, working automations (not just demos)
- Progressive complexity: local scripts → cloud integrations → deployable tools
- Students build a portfolio of automations they can actually use

**Deliverables:**
- Portfolio of 3-4 working automations
- GitHub repo with documented code
- CLAUDE.md automation playbook
- Custom AI operator agents

---

## 🏭 Company Scenario: Precision Manufacturing Co.

**Setup:**
You're the newly hired **AI Operations Lead** at **Precision Manufacturing Co.**, a mid-sized manufacturing company (200 employees, $50M revenue). The CEO hired you after hearing about "AI automating everything" - they know operations are drowning in manual processes but don't know where to start.

**What You Inherited:**
- Finance team manually processing 20+ invoice PDFs daily
- Sales team copying data between systems
- Customer service spending hours on repetitive emails
- Inventory team with Excel spreadsheets that break constantly
- HR doing manual onboarding paperwork
- No documentation, failed automation attempts everywhere

**Your Mission:**
1. Investigate each department's pain points
2. Identify quick-win automation opportunities
3. Build working automations that save real time
4. Document everything for maintenance
5. Train the team on new workflows

**Departments:**
- Finance (invoice processing nightmare)
- Sales Operations (data sync chaos)
- Customer Service (repetitive emails)
- Inventory Management (spreadsheet hell)
- HR (manual onboarding)

---

## 📚 Course Structure

### **Module 1: AI Operator Fundamentals** (7 lessons)

Master Claude Code for automation and process improvement work.

**1.1 - Introduction & The AI Operator Role**
- What is an AI operator?
- Your mission at Precision Manufacturing
- The automation mindset
- Setting up OpCode workspace

**1.2 - Investigating Manual Processes**
- Navigate messy documentation
- Read process descriptions, spreadsheets, email chains
- Extract automation opportunities
- Create automation opportunity map

**1.3 - Working with Data & APIs**
- Parse CSV files, JSON data
- Connect to Airtable API (free tier)
- Google Sheets API basics
- Transform data between systems

**1.4 - Introduction to MCPs**
- What are MCPs and why they matter
- Installing your first MCP (Airtable or Google)
- Optional: Synta MCP for n8n visual workflows
- Extending Claude Code's capabilities

**1.5 - Agents & Parallel Processing**
- Use agents to research APIs simultaneously
- Parallel file processing
- Create investigation reports faster
- When to use agents vs. direct work

**1.6 - Custom Sub-Agents for Operations**
- Build a "Process Analyzer" agent
- Build an "API Integration Expert" agent
- Persistent helpers for daily work
- Agent best practices

**1.7 - CLAUDE.md: Your Automation Playbook**
- Document automation patterns
- Create team standards
- Context that persists across sessions
- Build institutional knowledge

---

### **Module 2: Building Real Automations** (6-7 lessons)

Build production-ready automations from scratch.

**2.1 - Automation Design & Planning**
- From manual process to automation spec
- Planning your first automation
- Choosing the right tool (script vs. n8n vs. web app)
- Requirements gathering

**2.2 - Project 1: PDF Invoice Processing**
- **Part A:** Local PDF folder → Airtable
  - Process sample invoices (provided in course)
  - Extract invoice #, amount, vendor, date
  - Insert into Airtable automatically
  - Error handling and logging
  - **Deliverable:** Working Python script

- **Part B:** Advanced (Optional)
  - Schedule with cron
  - Email notifications on errors
  - Handle edge cases

**2.3 - Project 2: Google Drive Automation**
- Set up Google Drive API (step-by-step walkthrough)
- Watch Drive folder for new PDFs
- Auto-process and organize files
- Move to "processed" folder
- **Deliverable:** Scheduled automation that runs continuously
- **Real Use Case:** Finance team drops invoices in Drive, automation handles rest

**2.4 - Project 3: Invoice Upload Web App**
- Build web interface for PDF upload
- Process files on backend
- Display extracted data for review
- Save to Airtable
- Deploy to Vercel
- **Deliverable:** Live URL anyone can use
- **Real Use Case:** Shareable tool for entire finance team

**2.5 - Version Control with GitHub**
- GitHub basics for non-developers
- Why version control matters for automations
- Setting up your first repo (detailed walkthrough)
- Committing automation code
- Creating README documentation
- **Deliverable:** GitHub repo with all automations

**2.6 - Advanced: Multi-Step Automation** (Optional)
- Chain multiple APIs together
- Error handling in complex workflows
- Monitoring and alerts
- **Deliverable:** Complex automation of student's choice

**2.7 - Documentation & Handoff**
- Create runbooks for automations
- Train non-technical users
- Build maintainable automation library
- Prepare for team handoff

---

## 🎓 Learning Methodology

**Interactive, Conversational Learning:**
- No videos, no passive watching
- Students DO everything themselves
- Claude guides step-by-step via CLAUDE.md files
- STOP/USER/ACTION format for pacing

**Each Lesson Includes:**
- Clear learning objectives
- Hands-on exercises
- Success criteria
- "Meta skill" explanation
- "Where else this applies" examples
- Troubleshooting tips

**Student Experience:**
1. Open lesson CLAUDE.md in OpCode
2. Claude guides them through exercises
3. Build real files, run real code
4. Test with actual outputs
5. Move to next lesson when ready

---

## 💻 Technical Requirements

**Required:**
- Claude Code installed
- OpCode (recommended) or text editor
- Free Airtable account
- Google account (for Drive/Sheets API)
- Python 3.8+ installed

**Set Up During Course:**
- GitHub account (guided setup in Module 2)
- Vercel account for deployment (free tier)

**Optional:**
- Synta account for n8n MCP (visual workflow builder)
- Node.js (if students prefer JavaScript)

**No Complex/Paid APIs:**
- No Stripe ✅
- No paid services required ✅
- Everything works on free tiers ✅

---

## 📁 Course Materials Structure

```
Claude-Code-AI-Operator-Course/
├── README.md
├── COURSE-PLAN.md (this file)
├── course-structure.json
│
├── lesson-modules/
│   ├── 1.1-introduction/CLAUDE.md
│   ├── 1.2-investigating-processes/CLAUDE.md
│   ├── 1.3-data-and-apis/CLAUDE.md
│   ├── 1.4-introduction-to-mcps/CLAUDE.md
│   ├── 1.5-agents/CLAUDE.md
│   ├── 1.6-custom-sub-agents/CLAUDE.md
│   ├── 1.7-claude-md/CLAUDE.md
│   └── [Module 2 lessons...]
│
├── precision-manufacturing/
│   ├── company-context/
│   │   ├── SCENARIO.md
│   │   ├── DEPARTMENTS.md
│   │   └── TECH-STACK.md
│   │
│   ├── department-interviews/
│   │   ├── finance-invoice-nightmare.md
│   │   ├── sales-process-notes.md
│   │   ├── customer-service-pain-points.md
│   │   ├── inventory-management-issues.md
│   │   └── hr-onboarding-workflow.md
│   │
│   ├── current-data-samples/
│   │   ├── invoices/
│   │   │   ├── invoice-001-acme-corp.pdf
│   │   │   ├── invoice-002-widget-supplies.pdf
│   │   │   ├── invoice-003-tech-parts-inc.pdf
│   │   │   ├── invoice-004-global-shipping.pdf
│   │   │   └── invoice-005-office-depot.pdf
│   │   ├── expected-output.json
│   │   ├── vendor-list.csv
│   │   └── airtable-structure.json
│   │
│   ├── failed-automation-attempts/
│   │   ├── johns-email-script.py
│   │   ├── invoice-parser-attempt.js
│   │   └── previous-consultant-notes.md
│   │
│   └── api-credentials-and-docs/
│       ├── airtable-setup-guide.md
│       ├── google-drive-api-setup.md
│       └── credentials-template.env
│
├── templates/
│   ├── automation-spec-template.md
│   ├── process-investigation-template.md
│   └── runbook-template.md
│
└── reference-materials/
    ├── api-cheatsheets/
    ├── troubleshooting-guides/
    └── additional-resources.md
```

---

## 📦 Student Deliverables

### **By End of Module 1:**
- [ ] Process investigation report for Precision Manufacturing
- [ ] Automation opportunity map
- [ ] Custom AI operator sub-agents
- [ ] CLAUDE.md automation playbook

### **By End of Module 2:**
- [ ] **Automation 1:** PDF invoice processor (local)
- [ ] **Automation 2:** Google Drive automation (cloud)
- [ ] **Automation 3:** Invoice upload web app (deployed)
- [ ] **Automation 4:** Student's choice (their real use case)
- [ ] GitHub repo with all code documented
- [ ] Runbook for each automation
- [ ] Portfolio they can show employers/clients

---

## 🎯 Key Skills Taught

**Technical Skills:**
- ✅ API integration (Airtable, Google Drive, Sheets)
- ✅ PDF data extraction
- ✅ File processing automation
- ✅ Web app development basics
- ✅ Deployment (Vercel)
- ✅ Version control (GitHub)
- ✅ Error handling and logging
- ✅ MCPs (Model Context Protocol)

**AI Operator Skills:**
- ✅ Process investigation
- ✅ Opportunity identification
- ✅ Automation design
- ✅ Tool selection (when to use what)
- ✅ Documentation practices
- ✅ Team training
- ✅ Using Claude Code agents effectively
- ✅ Building CLAUDE.md playbooks

**Soft Skills:**
- ✅ Requirements gathering
- ✅ Stakeholder communication
- ✅ Prioritization
- ✅ Handoff preparation

---

## 🧪 Testing & Quality Assurance

**Before Launch:**
- [ ] Test with zero-coding-experience user
- [ ] Verify all API setups work on free tiers
- [ ] Ensure sample PDFs process correctly
- [ ] Check GitHub walkthrough is detailed enough
- [ ] Confirm OpCode setup is smooth
- [ ] Test all automations actually work

**Success Criteria:**
- Can non-technical person complete Module 1?
- Can they build working PDF automation?
- Can they deploy to Vercel successfully?
- Would they feel confident as an "AI Operator"?
- Do they have portfolio pieces to show?

---

## 🚀 Differentiation from Other Courses

**vs. Claude Code for Everyone (Carl Vellotti):**
- Different scenario (manufacturing vs. coffee shop)
- Automation focus vs. general business
- Real API integrations vs. simple web app
- AI operator role vs. manager role
- Process investigation emphasis
- Production-ready code vs. prototypes

**vs. Generic Automation Courses:**
- Uses Claude Code as primary tool
- AI-first approach to automation
- No-code AND code options
- Emphasis on CLAUDE.md documentation
- Agent-driven workflows

**vs. Python/JavaScript Courses:**
- Not teaching programming fundamentals
- Teaching automation thinking
- Claude Code does the heavy lifting
- Focus on results, not syntax

---

## 📈 Future Enhancements (Post-Launch)

**Module 3: Advanced Integrations**
- Multi-system workflows
- Custom MCPs development
- Advanced error handling
- Scalability patterns

**Module 4: AI-Powered Automations**
- LLM API integrations
- AI-powered data extraction
- Intelligent routing
- Conversational interfaces

**Module 5: Enterprise Deployment**
- Security best practices
- Team collaboration
- Production monitoring
- Cost optimization

---

## 📞 Support & Community

**Student Support:**
- Reference materials for each lesson
- Troubleshooting guides
- API setup walkthroughs
- Common error solutions

**Community Building:**
- Student showcase gallery
- Automation templates library
- Best practices wiki
- Office hours (optional)

---

## ✅ Next Steps

1. **Complete course materials creation**
   - Write all CLAUDE.md lesson files
   - Create scenario documents
   - Generate sample invoices
   - Build starter code templates

2. **Beta testing**
   - Recruit 3-5 students
   - Gather feedback
   - Iterate on clarity

3. **Launch preparation**
   - Create marketing materials
   - Set up course delivery platform
   - Prepare instructor guide

4. **Post-launch**
   - Monitor student progress
   - Collect completion data
   - Gather testimonials
   - Plan future modules

---

**Last Updated:** February 4, 2026
**Status:** In Development
**Estimated Launch:** TBD
