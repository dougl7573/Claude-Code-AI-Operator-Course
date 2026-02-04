# Lesson 2.6 - Advanced: Multi-Step Automation (Optional)

**Module 2: Building Real Automations**
**Lesson Type:** Optional Advanced Project
**Prerequisites:** Lessons 2.1-2.5 completed
**Estimated Time:** 4-6 hours (spread across multiple sessions)

---

## Welcome to Advanced Automation

Congratulations on making it this far. You've built three solid automations:
1. Local PDF invoice processing
2. Google Drive folder monitoring
3. Deployed web application

Now it's time to level up.

In this **optional lesson**, you'll design and build a **complex multi-step automation** of YOUR choice. This is your opportunity to:
- Apply everything you've learned
- Build something for YOUR actual work
- Create a portfolio-worthy project
- Push your skills to the next level

This isn't a tutorial with step-by-step instructions. This is a **guided project** where Claude helps you design, build, and deploy a production-ready automation based on real needs.

---

## What Makes This "Advanced"?

Advanced automations have these characteristics:

**1. Multiple API Integrations**
- Chain 2+ APIs together
- Example: Gmail → Extract data → Airtable → Send Slack notification

**2. Complex Logic**
- Conditional workflows (if X, then Y, else Z)
- State management (remember what happened last time)
- Error recovery (retry on failure, fallback options)

**3. Production-Ready Features**
- Monitoring and alerts
- Logging for debugging
- Graceful error handling
- Configuration management
- Documentation for handoff

**4. Real Business Impact**
- Solves a genuine pain point
- Saves measurable time
- Improves accuracy or consistency
- Scales with growth

You're not just building a "demo." You're building something people will actually use.

---

## STOP: Choose Your Project

Before we proceed, you need to decide what automation you'll build.

**Option A: Choose a Precision Manufacturing Department**

Review these department interviews (in `/precision-manufacturing/department-interviews/`):
1. **Sales Operations** - Airtable → Google Sheets sync (multi-destination)
2. **Customer Service** - Email automation with AI classification
3. **Inventory Management** - Excel monitoring with Slack alerts
4. **HR Onboarding** - Document generation + scheduled email automation

Pick the one that interests you most or best matches skills you want to develop.

**Option B: Build for YOUR Real Work**

Do you have a manual process at your actual job that needs automation?
- Weekly report generation?
- Data sync between systems?
- Document processing workflow?
- Notification system?

Building something you'll actually use is the best learning experience.

**Option C: Build a Variation**

Take one of the Precision Manufacturing scenarios but adapt it:
- Sales sync but with different tools (Notion → Excel?)
- Customer service but for your industry
- Inventory but for a different type of data

---

## USER ACTION REQUIRED

**Stop and decide:**
1. Which project will you build?
2. Why did you choose this one?
3. What specific problem does it solve?

Write down your answers. This clarity will guide your entire project.

When you're ready, tell Claude: "I'm building [PROJECT NAME] because [REASON]."

---

## Part 1: Design Your Automation

Let's design your automation properly before writing code.

### Step 1.1: Define the Manual Process

**USER ACTION:** Answer these questions about the current manual process:

1. **What are the steps today?**
   - List out every action someone takes manually
   - Be specific (don't skip "obvious" steps)

2. **Who does this work?**
   - How much time does it take them?
   - How often (daily, weekly, monthly)?

3. **What goes wrong?**
   - Common errors?
   - Things that fall through cracks?
   - Bottlenecks?

4. **What data/systems are involved?**
   - Where does data come from?
   - Where does it go?
   - What format transformations happen?

Create a document: `automation-design.md` with this information.

---

### Step 1.2: Define Success Criteria

**USER ACTION:** Answer these questions:

1. **What does success look like?**
   - How much time saved?
   - What errors eliminated?
   - What new capabilities enabled?

2. **What are the must-have features?** (MVP)
   - What's the minimum that makes this useful?

3. **What are nice-to-have features?** (Future)
   - What can wait for version 2?

4. **What are the constraints?**
   - Budget limits?
   - Technical limitations?
   - Privacy/security requirements?

Add this to your `automation-design.md`.

---

### Step 1.3: Map the Automation Flow

**USER ACTION:** Create a flowchart (text-based is fine):

```
Example structure:

TRIGGER
  → Step 1: [Action]
     → If [Condition]: Step 2A
     → Else: Step 2B
  → Step 3: [Action]
     → On Success: Step 4
     → On Error: Alert + Retry
  → Step 4: [Action]
  → Step 5: Log completion
```

Include:
- Trigger (what starts the automation?)
- Each processing step
- Decision points
- Error handling
- Success confirmation

---

### Step 1.4: Identify Integration Points

**USER ACTION:** For each system/API you'll use, document:

1. **System Name** (e.g., Airtable, Gmail, Slack)
2. **What data** you need from it
3. **What actions** you'll perform
4. **Authentication method** (API key, OAuth, etc.)
5. **Rate limits** or restrictions
6. **Documentation link**

Create a section in `automation-design.md` called "Integration Requirements."

---

### STOP: Review Your Design

Before coding, make sure your design is solid.

**Quality Check:**
- Can you explain the automation to someone in 2 minutes?
- Is the value clear? (X hours saved, Y errors eliminated)
- Are the steps concrete and actionable?
- Do you know what APIs/tools you need?

If yes to all, proceed. If not, refine your design.

**Pro Tip:** The best automations are simple in concept but powerful in impact. If your design feels overly complicated, simplify.

---

## Part 2: Setup and Configuration

Before building, set up your development environment properly.

### Step 2.1: Project Structure

**USER ACTION:** Create a well-organized project folder:

```
my-automation/
├── README.md                 # Project overview
├── automation-design.md      # Your design doc
├── .env.template            # Template for credentials
├── .env                     # Actual credentials (gitignored)
├── .gitignore               # Ignore sensitive files
├── config.py                # Configuration management
├── main.py                  # Main automation script
├── utils/                   # Helper functions
│   ├── __init__.py
│   ├── api_clients.py      # API wrappers
│   ├── data_processing.py  # Data transformation
│   └── notifications.py    # Alerts/logging
├── tests/                   # Test scripts
│   └── test_api_access.py
├── logs/                    # Log files
└── docs/                    # Additional documentation
    └── runbook.md          # How to run/maintain
```

**Ask Claude:** "Help me create this project structure with starter files."

---

### Step 2.2: Credential Management

**CRITICAL:** Never hardcode API keys.

**USER ACTION:** Set up proper credential management:

1. Create `.env.template`:
```bash
# Template - copy to .env and fill in real values
API_KEY_SYSTEM1=your_key_here
API_KEY_SYSTEM2=your_key_here
SLACK_WEBHOOK_URL=your_url_here
```

2. Create `.env` with real credentials (copy from template)

3. Add to `.gitignore`:
```
.env
*.log
__pycache__/
*.pyc
```

4. Create `config.py`:
```python
import os
from dotenv import load_dotenv

load_dotenv()

# Load all credentials
SYSTEM1_API_KEY = os.getenv('API_KEY_SYSTEM1')
SYSTEM2_API_KEY = os.getenv('API_KEY_SYSTEM2')
SLACK_WEBHOOK = os.getenv('SLACK_WEBHOOK_URL')

# Validate
def validate_config():
    required = ['API_KEY_SYSTEM1', 'API_KEY_SYSTEM2']
    missing = [var for var in required if not os.getenv(var)]
    if missing:
        raise ValueError(f"Missing required env vars: {missing}")
```

**Ask Claude:** "Help me set up secure credential management for my specific APIs."

---

### Step 2.3: Test API Access

Before building the full automation, test each API individually.

**USER ACTION:** Create `tests/test_api_access.py`:

```python
# Test that you can connect to each API
# Example structure:

import config

def test_system1_connection():
    """Test connection to System 1 API"""
    # Your test code here
    print("✓ System 1 API: Connected")

def test_system2_connection():
    """Test connection to System 2 API"""
    # Your test code here
    print("✓ System 2 API: Connected")

if __name__ == "__main__":
    config.validate_config()
    test_system1_connection()
    test_system2_connection()
    print("\n✓ All API connections successful!")
```

**Ask Claude:** "Help me write API connection tests for [YOUR SPECIFIC APIS]."

Run your tests: `python tests/test_api_access.py`

Don't proceed until all APIs are accessible.

---

## Part 3: Build Core Functionality

Now we build the automation piece by piece.

### Step 3.1: Start with Data Extraction

**USER ACTION:** Build the first step - getting data from the source.

**Example Task:** "Pull records from Airtable" or "Read emails from Gmail"

1. Create a function that fetches the data
2. Log what you're retrieving
3. Return data in a clean structure
4. Handle errors (what if API fails?)

**Ask Claude:** "Help me build a function to [YOUR EXTRACTION TASK] with error handling."

**Test it:** Run your extraction function standalone. Print the results. Verify data looks correct.

---

### Step 3.2: Build Data Transformation

**USER ACTION:** Process the extracted data into the format you need.

**Common transformations:**
- Filter (only records that meet criteria)
- Map (rename fields, reformat dates)
- Enrich (lookup additional data)
- Validate (check for required fields)

**Ask Claude:** "Help me transform [SOURCE DATA] into [TARGET FORMAT]."

**Test it:** Feed sample data through your transformation. Verify output matches expectations.

---

### Step 3.3: Build the Action

**USER ACTION:** Take the transformed data and do something with it.

**Example actions:**
- Insert into Airtable
- Send email via Gmail
- Update Google Sheet
- Post to Slack

**Ask Claude:** "Help me build a function to [YOUR ACTION] with the transformed data."

**Test it:** Run the action with test data. Verify it works correctly. Check that the destination system shows the expected result.

---

### Step 3.4: Chain the Steps Together

**USER ACTION:** Create your main automation flow in `main.py`:

```python
# Example structure:

import logging
import config
from utils import api_clients, data_processing, notifications

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/automation.log'),
        logging.StreamHandler()
    ]
)

def run_automation():
    """Main automation workflow"""
    try:
        logging.info("Starting automation run")

        # Step 1: Extract data
        logging.info("Extracting data from source...")
        raw_data = api_clients.fetch_from_source()
        logging.info(f"Extracted {len(raw_data)} records")

        # Step 2: Transform data
        logging.info("Transforming data...")
        processed_data = data_processing.transform(raw_data)
        logging.info(f"Transformed into {len(processed_data)} items")

        # Step 3: Take action
        logging.info("Executing actions...")
        results = api_clients.send_to_destination(processed_data)
        logging.info(f"Successfully processed {results['success']} items")

        # Step 4: Notify success
        notifications.send_success_alert(results)
        logging.info("Automation completed successfully")

        return results

    except Exception as e:
        logging.error(f"Automation failed: {str(e)}")
        notifications.send_error_alert(str(e))
        raise

if __name__ == "__main__":
    config.validate_config()
    run_automation()
```

**Ask Claude:** "Help me structure my main automation flow for [YOUR SPECIFIC WORKFLOW]."

**Test the full flow:** Run `python main.py` and watch it execute end-to-end.

---

## Part 4: Add Production Features

Your automation works. Now make it production-ready.

### Step 4.1: Comprehensive Error Handling

**USER ACTION:** Add error handling for everything that can fail.

**Common failure points:**
- API rate limits (retry with backoff)
- Network timeouts (retry logic)
- Invalid data (validation + skip)
- Authentication failures (alert immediately)

**Ask Claude:** "Help me add robust error handling to [SPECIFIC FUNCTION]."

**Pattern to use:**
```python
import time

def api_call_with_retry(func, max_retries=3):
    """Retry failed API calls with exponential backoff"""
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            wait_time = 2 ** attempt  # 1s, 2s, 4s
            logging.warning(f"Attempt {attempt+1} failed: {e}. Retrying in {wait_time}s...")
            time.sleep(wait_time)
```

---

### Step 4.2: Add Monitoring and Alerts

**USER ACTION:** Set up notifications for important events.

**Events to monitor:**
1. **Success:** "Automation completed - processed X records"
2. **Errors:** "Automation failed - [ERROR MESSAGE]"
3. **Warnings:** "Automation ran but skipped Y records"
4. **Metrics:** "Processing time: X seconds"

**Implementation options:**
- Slack webhooks (easy)
- Email alerts (via Gmail API)
- Log files (always include)

**Ask Claude:** "Help me set up Slack notifications for my automation status."

Create `utils/notifications.py`:
```python
import requests
import logging
import config

def send_slack_message(message, level="info"):
    """Send message to Slack webhook"""
    if not config.SLACK_WEBHOOK:
        logging.warning("No Slack webhook configured, skipping notification")
        return

    color_map = {
        "success": "#36a64f",
        "error": "#ff0000",
        "warning": "#ffaa00",
        "info": "#0000ff"
    }

    payload = {
        "attachments": [{
            "color": color_map.get(level, "#0000ff"),
            "text": message,
            "footer": "Automation System",
            "ts": int(time.time())
        }]
    }

    try:
        response = requests.post(config.SLACK_WEBHOOK, json=payload)
        response.raise_for_status()
    except Exception as e:
        logging.error(f"Failed to send Slack notification: {e}")

def send_success_alert(results):
    """Send success notification"""
    message = f"✓ Automation completed successfully\n"
    message += f"Processed: {results['success']} items\n"
    message += f"Duration: {results.get('duration', 'N/A')} seconds"
    send_slack_message(message, level="success")

def send_error_alert(error_msg):
    """Send error notification"""
    message = f"✗ Automation failed\n"
    message += f"Error: {error_msg}\n"
    message += f"Check logs for details"
    send_slack_message(message, level="error")
```

---

### Step 4.3: Add Configuration Options

**USER ACTION:** Make your automation configurable without code changes.

**Things to make configurable:**
- Which records to process (filters)
- How many records per run (limits)
- Which notifications to send
- Dry-run mode (test without making changes)

Add to `config.py`:
```python
# Feature flags
DRY_RUN = os.getenv('DRY_RUN', 'false').lower() == 'true'
MAX_RECORDS_PER_RUN = int(os.getenv('MAX_RECORDS', '100'))
ENABLE_SLACK_NOTIFICATIONS = os.getenv('ENABLE_SLACK', 'true').lower() == 'true'

# Filters
PROCESS_ONLY_NEW = os.getenv('PROCESS_ONLY_NEW', 'true').lower() == 'true'
DATE_FILTER_DAYS = int(os.getenv('DATE_FILTER_DAYS', '7'))
```

Update `.env.template`:
```bash
# Feature Configuration
DRY_RUN=false
MAX_RECORDS=100
ENABLE_SLACK=true
PROCESS_ONLY_NEW=true
DATE_FILTER_DAYS=7
```

**Why this matters:** Non-technical users can adjust behavior by editing `.env` without touching code.

---

### Step 4.4: Implement Dry-Run Mode

**USER ACTION:** Add a "test mode" that shows what WOULD happen without actually doing it.

```python
def send_to_destination(data):
    """Send data to destination system"""
    if config.DRY_RUN:
        logging.info(f"[DRY RUN] Would send {len(data)} records to destination")
        for item in data[:3]:  # Show first 3
            logging.info(f"[DRY RUN] Would process: {item}")
        return {'success': len(data), 'dry_run': True}

    # Actual implementation
    results = actual_api_call(data)
    return results
```

**Why this matters:** Test the full flow safely before running for real.

**Test it:** Run `DRY_RUN=true python main.py`

---

### Step 4.5: Add Detailed Logging

**USER ACTION:** Log everything important for debugging.

**What to log:**
- Start/end times
- Record counts at each step
- Decisions made (why was a record skipped?)
- API response times
- Errors with full context

**Logging best practices:**
```python
# Good logging
logging.info(f"Processing record {i+1}/{total}: {record['id']}")
logging.debug(f"API response: {response.status_code} - {response.text[:100]}")
logging.warning(f"Skipping record {record['id']}: missing required field 'email'")
logging.error(f"API call failed for record {record['id']}: {str(e)}")

# Bad logging
logging.info("Processing")  # Too vague
logging.error(str(e))  # No context
```

**Ask Claude:** "Review my logging and suggest improvements for debugging."

---

## Part 5: Schedule and Deploy

Your automation works reliably. Now make it run automatically.

### Step 5.1: Create a Run Script

**USER ACTION:** Create `run.sh` (or `run.bat` for Windows):

```bash
#!/bin/bash
# Run script for automation

# Activate virtual environment (if using one)
# source venv/bin/activate

# Set working directory
cd "$(dirname "$0")"

# Run automation
python main.py

# Check exit code
if [ $? -eq 0 ]; then
    echo "Automation completed successfully"
else
    echo "Automation failed - check logs"
    exit 1
fi
```

Make it executable: `chmod +x run.sh`

**Why this matters:** Consistent way to run the automation, whether manual or scheduled.

---

### Step 5.2: Set Up Scheduling

**USER ACTION:** Schedule your automation to run automatically.

**Option A: Cron (Linux/Mac)**

Edit crontab: `crontab -e`

```bash
# Run every day at 9 AM
0 9 * * * /path/to/your/automation/run.sh >> /path/to/logs/cron.log 2>&1

# Run every hour
0 * * * * /path/to/your/automation/run.sh >> /path/to/logs/cron.log 2>&1

# Run every Monday at 8 AM
0 8 * * 1 /path/to/your/automation/run.sh >> /path/to/logs/cron.log 2>&1
```

**Option B: Task Scheduler (Windows)**

1. Open Task Scheduler
2. Create Basic Task
3. Set trigger (daily, weekly, etc.)
4. Set action: `python C:\path\to\main.py`

**Option C: Cloud Scheduler (Production)**

For production deployments:
- AWS CloudWatch Events
- Google Cloud Scheduler
- Heroku Scheduler

**Ask Claude:** "Help me set up a cron job to run my automation [SCHEDULE]."

---

### Step 5.3: Test the Scheduled Run

**USER ACTION:** Verify your automation runs correctly when scheduled.

1. **Test manually first:**
   ```bash
   ./run.sh
   ```

2. **Set a test schedule** (5 minutes from now):
   ```bash
   # Temporary cron for testing
   */5 * * * * /path/to/run.sh >> /path/to/logs/test.log 2>&1
   ```

3. **Wait and verify:**
   - Check logs: `tail -f logs/test.log`
   - Check destination system (did data arrive?)
   - Check notifications (did Slack message send?)

4. **Remove test schedule** once verified:
   ```bash
   crontab -e  # Remove the test line
   ```

5. **Set production schedule**

---

## Part 6: Documentation and Handoff

Your automation runs in production. Now make it maintainable.

### Step 6.1: Write a Comprehensive README

**USER ACTION:** Create an excellent `README.md`:

```markdown
# [Automation Name]

## Purpose
[One paragraph: What does this do and why?]

## Business Impact
- Saves: X hours per week
- Eliminates: Y manual errors
- Improves: Z metric

## How It Works
[Brief description of the workflow]

1. Step 1: [Extract data from...]
2. Step 2: [Transform...]
3. Step 3: [Send to...]

## Setup

### Prerequisites
- Python 3.8+
- API access to [System A] and [System B]
- Credentials: [List required keys]

### Installation
```bash
git clone [repo]
cd [automation-folder]
pip install -r requirements.txt
cp .env.template .env
# Edit .env with your credentials
```

### Configuration
Edit `.env` file:
- `API_KEY_SYSTEM1`: Get from [URL]
- `SLACK_WEBHOOK_URL`: Create at [URL]
- `MAX_RECORDS`: Adjust based on volume

## Usage

### Manual Run
```bash
python main.py
```

### Dry Run (Test Mode)
```bash
DRY_RUN=true python main.py
```

### Scheduled Run
Runs automatically via cron: [SCHEDULE]

## Monitoring

### Check Logs
```bash
tail -f logs/automation.log
```

### Slack Notifications
Success/failure alerts sent to #automation-alerts

### What to Watch For
- Error messages in logs
- Missing Slack notifications (means automation didn't run)
- Records not appearing in destination system

## Troubleshooting

### Automation didn't run
- Check cron is active: `crontab -l`
- Check logs: `tail logs/cron.log`
- Verify credentials in `.env`

### API errors
- Check API keys are valid
- Check rate limits
- Check network connectivity

### Data not syncing
- Run in dry-run mode: `DRY_RUN=true python main.py`
- Check transformation logic
- Verify destination API is working

## Maintenance

### Weekly
- Review logs for errors
- Check success notifications

### Monthly
- Rotate log files
- Review performance metrics
- Update dependencies if needed

### When Things Change
- Adding new fields: Update transformation in `utils/data_processing.py`
- New API credentials: Update `.env`
- Schedule change: Edit crontab

## Contact
- Owner: [Your Name]
- Created: [Date]
- Last Updated: [Date]
```

**Ask Claude:** "Help me write a comprehensive README for my automation."

---

### Step 6.2: Create a Runbook

**USER ACTION:** Create `docs/runbook.md` for operators:

```markdown
# Automation Runbook

## Quick Reference

**Purpose:** [One sentence]
**Schedule:** [When it runs]
**Duration:** [How long it takes]
**Owner:** [Your name/email]

## Daily Operations

### Morning Check (5 minutes)
1. Check Slack for success notification
2. If no notification, investigate:
   - Check logs: `tail -50 logs/automation.log`
   - Try manual run: `python main.py`
   - Contact owner if unresolved

### Verify Output
- Log into [Destination System]
- Check for new records from today
- Spot-check 2-3 records for accuracy

## Common Issues

### Issue: Automation didn't run
**Symptoms:** No Slack notification, no log entries

**Diagnosis:**
1. Check cron: `crontab -l`
2. Check server was up at scheduled time

**Resolution:**
1. Run manually: `python main.py`
2. If successful, cron issue (contact sysadmin)
3. If fails, check logs

### Issue: API authentication failed
**Symptoms:** Error in logs: "401 Unauthorized"

**Diagnosis:**
API credentials expired or invalid

**Resolution:**
1. Check `.env` file has credentials
2. Test credentials manually
3. Generate new API key if needed
4. Update `.env`
5. Restart automation

### Issue: Data format error
**Symptoms:** Error in logs: "Invalid field X"

**Diagnosis:**
Source system changed data structure

**Resolution:**
1. Contact owner immediately
2. Don't modify code yourself
3. Run in dry-run mode to test: `DRY_RUN=true python main.py`

## Emergency Contacts

**Primary Owner:** [Name] - [Email] - [Phone]
**Backup Contact:** [Name] - [Email]
**System Admin:** [Name] - [Email]

## Rollback Procedure

If automation causes issues:

1. **Stop scheduled runs:**
   ```bash
   crontab -e
   # Comment out the automation line with #
   ```

2. **Notify stakeholders** via Slack: #automation-alerts

3. **Manual workaround:**
   [Describe manual process to do the same work]

4. **Contact owner** for investigation

## Performance Metrics

**Normal Operation:**
- Run time: 2-5 minutes
- Records processed: 50-200 per run
- Success rate: >95%

**Alert Thresholds:**
- Run time >10 minutes (investigate)
- Success rate <90% (investigate)
- 3 consecutive failures (page owner)

## Monthly Maintenance

### First Monday of Month
1. Review error logs
2. Check disk space (logs can grow large)
3. Rotate old log files:
   ```bash
   cd logs
   mv automation.log automation.log.$(date +%Y%m)
   ```

### Quarterly
1. Update dependencies: `pip install --upgrade -r requirements.txt`
2. Test in staging environment
3. Review and update documentation

---

**Last Updated:** [Date]
**Version:** 1.0
```

**Ask Claude:** "Help me create a runbook for operators who aren't technical."

---

### Step 6.3: Document Technical Details

**USER ACTION:** Create `docs/technical-details.md`:

```markdown
# Technical Documentation

## Architecture

### High-Level Flow
[Diagram or description of data flow]

### Components
- **main.py**: Orchestration and workflow
- **config.py**: Configuration management
- **utils/api_clients.py**: API wrappers
- **utils/data_processing.py**: Data transformation
- **utils/notifications.py**: Alerts and logging

## API Integrations

### System 1 - [Name]
- **API Documentation:** [URL]
- **Authentication:** API Key
- **Rate Limits:** 100 requests/minute
- **Endpoints Used:**
  - `GET /endpoint1` - Fetch records
  - `POST /endpoint2` - Create records

### System 2 - [Name]
- **API Documentation:** [URL]
- **Authentication:** OAuth 2.0
- **Rate Limits:** 1000 requests/hour
- **Endpoints Used:**
  - `GET /endpoint1` - Read data
  - `PUT /endpoint2` - Update data

## Data Transformations

### Step 1: Extract
```python
# Pseudocode
raw_data = fetch_from_source()
# Returns: List of dicts with fields [a, b, c]
```

### Step 2: Transform
```python
# Pseudocode
for record in raw_data:
    transformed = {
        'field1': record['a'],
        'field2': format_date(record['b']),
        'field3': calculate(record['c'])
    }
```

### Step 3: Load
```python
# Pseudocode
send_to_destination(transformed_data)
```

## Error Handling

### Retry Logic
- API failures: 3 retries with exponential backoff
- Network timeouts: 5-second timeout, 2 retries
- Invalid data: Log and skip, continue processing

### Failure Modes
1. **API unavailable:** Alert + exit, retry next scheduled run
2. **Partial failure:** Process successful records, alert about failures
3. **Configuration error:** Fail fast with clear error message

## Logging

### Log Levels
- **DEBUG:** Detailed API responses, data samples
- **INFO:** Normal operation, record counts
- **WARNING:** Skipped records, retries
- **ERROR:** Failures requiring attention

### Log Rotation
- Logs stored in `logs/automation.log`
- Rotated monthly (manual process)
- Keep 6 months of history

## Security

### Credentials
- Stored in `.env` (not in git)
- Read-only access where possible
- Rotated quarterly

### Data Handling
- No PII logged
- API responses sanitized before logging
- Temporary data deleted after processing

## Performance

### Benchmarks
- Typical run: 2-5 minutes
- Records per second: 10-20
- Memory usage: <100 MB
- Network bandwidth: <1 MB per run

### Scalability
- Current: 100-200 records per run
- Max tested: 1000 records (8 minutes)
- Bottleneck: API rate limits

## Dependencies

```
requests==2.31.0
python-dotenv==1.0.0
[List all dependencies with versions]
```

## Testing

### Unit Tests
```bash
python -m pytest tests/
```

### Integration Tests
```bash
python tests/test_api_access.py
```

### Manual Test
```bash
DRY_RUN=true python main.py
```

## Future Enhancements

### Version 2.0 Ideas
- [ ] Add dashboard for monitoring
- [ ] Implement two-way sync
- [ ] Add data validation rules
- [ ] Support for additional data sources

---

**Author:** [Your name]
**Last Updated:** [Date]
```

---

## Part 7: Testing and Validation

Before declaring success, thoroughly test your automation.

### Step 7.1: Test Scenarios

**USER ACTION:** Test these scenarios:

**1. Happy Path**
- Run automation with normal data
- Verify all records process correctly
- Check destination system matches expectations
- Confirm notifications sent

**2. Empty Data**
- What if source has no new records?
- Should run successfully (no errors)
- Log: "No new records to process"

**3. Bad Data**
- What if a record has missing required field?
- Should skip that record, continue with others
- Log warning with details
- Alert if too many failures

**4. API Failures**
- Simulate API down (temporarily break credential)
- Should retry, then fail gracefully
- Should send error alert
- Should not corrupt existing data

**5. Partial Failure**
- What if 5/100 records fail?
- Should process the 95 successful ones
- Should log the 5 failures
- Should notify about partial success

**6. Already Processed**
- What if record already exists in destination?
- Should skip or update (depending on design)
- Should not create duplicates
- Should log skip reason

**Create a test checklist and verify each scenario.**

---

### Step 7.2: Load Testing

**USER ACTION:** Test with realistic data volumes.

**Questions to answer:**
- How long does it take with 10 records? 100? 1000?
- Does it handle rate limits gracefully?
- Does memory usage stay reasonable?
- Are there any bottlenecks?

**Ask Claude:** "Help me optimize my automation for [EXPECTED VOLUME]."

---

### Step 7.3: Monitor First Week

**USER ACTION:** After deploying, watch it closely.

**Daily checks (first week):**
- Review logs each day
- Verify data in destination
- Check notification accuracy
- Monitor performance metrics
- Ask users for feedback

**Keep a log:** What issues came up? How did you fix them?

---

## Part 8: Present Your Work

You've built something impressive. Now showcase it.

### Step 8.1: Create a Demo Video

**USER ACTION:** Record a 3-5 minute video showing:

1. **The Problem** (1 min)
   - What was manual before?
   - How long did it take?
   - What went wrong?

2. **The Solution** (2 min)
   - Show the automation running
   - Show the results in destination system
   - Show the monitoring/alerts

3. **The Impact** (1 min)
   - Time saved
   - Errors eliminated
   - What's now possible

**Tools:** Loom, OBS, or QuickTime screen recording

---

### Step 8.2: Write a Case Study

**USER ACTION:** Create `CASE-STUDY.md`:

```markdown
# [Automation Name] - Case Study

## Executive Summary
[2-3 sentences: Problem, solution, impact]

## The Challenge

### Before Automation
- [Description of manual process]
- Time required: [X hours per week]
- Common problems: [Errors, delays, etc.]

### Why This Mattered
- [Business impact of manual process]
- [Why now was the right time]

## The Solution

### Design Approach
- [How you designed the automation]
- [Key technical decisions]

### Implementation
- **Technologies used:** [APIs, languages, tools]
- **Development time:** [How long it took]
- **Key features:**
  - [Feature 1 and why it matters]
  - [Feature 2 and why it matters]

### Technical Highlights
- [Interesting challenge you solved]
- [Creative solution you implemented]

## The Results

### Quantitative Impact
- **Time saved:** X hours per week
- **Accuracy improvement:** From Y% to Z%
- **Processing speed:** Records per hour

### Qualitative Impact
- [User feedback]
- [Improved workflows]
- [New capabilities enabled]

### ROI Calculation
- **Cost to build:** X hours @ $Y/hour = $Z
- **Ongoing cost:** $A per month (API fees, hosting)
- **Time saved:** B hours/week @ $Y/hour = $C/week
- **Payback period:** [Weeks until break-even]

## Lessons Learned

### What Went Well
- [Things that worked great]

### What Was Challenging
- [Problems you encountered]
- [How you overcame them]

### What You'd Do Differently
- [Hindsight improvements]

## Future Enhancements
- [Version 2.0 ideas]
- [Related automations to build]

## Conclusion
[Wrap up with key takeaway]

---

**Project Date:** [When you built this]
**Tools:** [List of technologies]
**GitHub:** [Link to repo]
```

**Ask Claude:** "Help me write a compelling case study for my automation."

---

### Step 8.3: Add to Portfolio

**USER ACTION:** Package your work for your portfolio.

**Include:**
1. README.md (excellent documentation)
2. CASE-STUDY.md (the story)
3. Demo video or screenshots
4. Code (clean, well-commented)
5. Metrics (before/after numbers)

**Where to showcase:**
- GitHub repo (public or private)
- Personal website portfolio page
- LinkedIn post about the project
- Resume bullet point

**Example bullet point:**
> "Built multi-step automation integrating Airtable, Google Sheets, and Slack APIs, reducing manual data entry by 15 hours/week and eliminating 95% of transcription errors. Implemented with Python, scheduled execution, error monitoring, and comprehensive documentation."

---

## Part 9: Advanced Patterns (Optional)

Want to go even further? Here are advanced patterns.

### Pattern 1: State Management

Track what's been processed to avoid duplicates.

**Implementation:**
```python
import json
from pathlib import Path

STATE_FILE = Path('state.json')

def load_state():
    """Load last processed state"""
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {'last_processed_id': None, 'last_run': None}

def save_state(state):
    """Save current state"""
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

# Usage in main.py
state = load_state()
# Process only records newer than last_processed_id
# After success, save new state
```

**Why this matters:** Prevents reprocessing, enables incremental runs.

---

### Pattern 2: Parallel Processing

Speed up by processing multiple items simultaneously.

**Implementation:**
```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def process_single_record(record):
    """Process one record"""
    # Your processing logic
    return result

def process_records_parallel(records, max_workers=5):
    """Process multiple records in parallel"""
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_single_record, r): r for r in records}
        for future in as_completed(futures):
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                record = futures[future]
                logging.error(f"Failed to process {record['id']}: {e}")
    return results
```

**Why this matters:** Process 100 records in minutes instead of an hour.

**Caution:** Watch API rate limits.

---

### Pattern 3: Dead Letter Queue

Save failed records for later reprocessing.

**Implementation:**
```python
import json
from datetime import datetime

def save_to_dlq(record, error):
    """Save failed record to dead letter queue"""
    dlq_file = Path('logs/failed_records.jsonl')
    entry = {
        'timestamp': datetime.now().isoformat(),
        'record': record,
        'error': str(error)
    }
    with open(dlq_file, 'a') as f:
        f.write(json.dumps(entry) + '\n')
    logging.warning(f"Record saved to DLQ: {record.get('id')}")

# Usage
try:
    process_record(record)
except Exception as e:
    save_to_dlq(record, e)
    continue  # Keep processing other records
```

**Why this matters:** Don't lose data on temporary failures. Reprocess later.

---

### Pattern 4: Circuit Breaker

Stop trying if API is consistently failing.

**Implementation:**
```python
class CircuitBreaker:
    def __init__(self, failure_threshold=5):
        self.failure_count = 0
        self.failure_threshold = failure_threshold
        self.is_open = False

    def call(self, func):
        if self.is_open:
            raise Exception("Circuit breaker is OPEN - too many failures")

        try:
            result = func()
            self.failure_count = 0  # Reset on success
            return result
        except Exception as e:
            self.failure_count += 1
            if self.failure_count >= self.failure_threshold:
                self.is_open = True
                logging.error("Circuit breaker OPENED - too many failures")
            raise

# Usage
circuit = CircuitBreaker(failure_threshold=5)
for record in records:
    try:
        circuit.call(lambda: process_record(record))
    except Exception as e:
        logging.error(f"Processing failed: {e}")
        break  # Stop processing if circuit opens
```

**Why this matters:** Don't waste time retrying if API is down for maintenance.

---

### Pattern 5: Metrics and Analytics

Track automation performance over time.

**Implementation:**
```python
import json
from datetime import datetime

def log_metrics(run_stats):
    """Append run metrics to metrics log"""
    metrics_file = Path('logs/metrics.jsonl')
    entry = {
        'timestamp': datetime.now().isoformat(),
        'records_processed': run_stats['success'],
        'records_failed': run_stats['failed'],
        'duration_seconds': run_stats['duration'],
        'records_per_second': run_stats['success'] / run_stats['duration']
    }
    with open(metrics_file, 'a') as f:
        f.write(json.dumps(entry) + '\n')

# Generate weekly report
def generate_weekly_report():
    """Analyze last week of metrics"""
    metrics = []
    with open('logs/metrics.jsonl') as f:
        for line in f:
            metrics.append(json.loads(line))

    # Calculate statistics
    total_processed = sum(m['records_processed'] for m in metrics)
    avg_duration = sum(m['duration_seconds'] for m in metrics) / len(metrics)

    return {
        'total_processed': total_processed,
        'avg_duration': avg_duration,
        'runs': len(metrics)
    }
```

**Why this matters:** Data-driven optimization and reporting.

---

## Part 10: Reflection and Next Steps

You've built an advanced automation. Take a moment to reflect.

### Reflection Questions

**USER ACTION:** Answer these for yourself:

1. **What am I most proud of in this project?**

2. **What was the hardest part? How did I overcome it?**

3. **What would I do differently if I started over?**

4. **What new skills did I develop?**

5. **How can I apply these patterns to other projects?**

6. **What feedback have users given me?**

Write your reflections in a file called `REFLECTIONS.md`.

---

### Share Your Success

**USER ACTION:** Share what you built.

**Ideas:**
- Post on LinkedIn with demo video
- Write a blog post about the experience
- Share in developer communities
- Add to your portfolio site
- Tweet about it (developers love automation stories)

**Template post:**
> "Just built a multi-step automation that [DOES X], saving [Y HOURS] per week. Used Claude Code to integrate [APIS], handle errors gracefully, and deploy with monitoring. Check out the case study: [LINK]"

---

### What's Next?

**Option 1: Enhance This Automation**
- Add the advanced patterns above
- Build a web dashboard for monitoring
- Implement two-way sync
- Add ML for intelligent routing

**Option 2: Build Another Automation**
- Pick a different department from Precision Manufacturing
- Or tackle another problem at your actual job
- Apply lessons learned from this project

**Option 3: Teach Others**
- Document your process
- Mentor someone building their first automation
- Contribute to automation communities

**Option 4: Go Pro**
- Offer automation consulting
- Build a portfolio of 3-5 automations
- Market yourself as an "AI Operations Engineer"

---

## Course Completion

If you've made it this far, you've accomplished something significant.

**You've learned to:**
- Investigate manual processes
- Design complex automations
- Integrate multiple APIs
- Handle errors gracefully
- Deploy production systems
- Monitor and maintain automations
- Document for handoff
- Build portfolio-worthy projects

**You're no longer just learning. You're building real solutions.**

---

## Final Resources

### API Integration Resources
- Airtable API: https://airtable.com/developers/web/api/introduction
- Google Sheets API: https://developers.google.com/sheets/api
- Gmail API: https://developers.google.com/gmail/api
- Slack Webhooks: https://api.slack.com/messaging/webhooks

### Automation Patterns
- Error handling patterns: https://docs.python.org/3/tutorial/errors.html
- Retry strategies: https://github.com/jd/tenacity
- API best practices: https://restfulapi.net/

### Claude Code Resources
- Claude Code documentation: https://docs.anthropic.com/en/docs/agents-and-tools/claude-code
- Example automations: [Your course GitHub repo]
- Community forum: [Your community link]

### Monitoring Tools
- Slack webhooks for alerts
- Papertrail for log management
- UptimeRobot for monitoring
- Grafana for dashboards (advanced)

---

## Need Help?

**Stuck on something?**

**Ask Claude:**
- "Help me debug this error: [ERROR MESSAGE]"
- "How do I optimize [SPECIFIC FUNCTION]?"
- "What's the best way to handle [SCENARIO]?"
- "Review my code for best practices"

**Remember:** The skill isn't memorizing code. The skill is knowing how to break down problems, design solutions, and use AI tools (like Claude) to implement them efficiently.

---

## Congratulations!

You've completed the advanced automation module.

**What you've proven:**
- You can tackle complex, multi-step workflows
- You can build production-ready systems
- You can integrate multiple technologies
- You can think like an AI Operations Engineer

**This is portfolio-worthy work.** Show it proudly.

**Next:** Move to Lesson 2.7 (Documentation & Handoff) or start building your next automation.

---

**Last Updated:** February 4, 2026
**Lesson Version:** 1.0
**Difficulty:** Advanced

**Feedback:** If you complete this lesson, share your project! We'd love to feature successful student automations.
