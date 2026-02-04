# Google Drive Setup Instructions

## How to Upload and Share the Course

### Step 1: Create the ZIP File

From the course directory, create a clean ZIP file:

```bash
cd "/Users/tomcrawshaw/AI OPERATOR OS"
zip -r ai-operator-course.zip "Claude-Code-AI-Operator-Course" \
  -x "*.git*" \
  -x "*/.DS_Store" \
  -x "*/node_modules/*" \
  -x "*/__pycache__/*"
```

This creates `ai-operator-course.zip` with all course materials, excluding git files and system files.

### Step 2: Upload to Google Drive

1. Go to https://drive.google.com
2. Click **"New"** → **"File upload"**
3. Select `ai-operator-course.zip`
4. Wait for upload to complete

### Step 3: Get Shareable Link

1. Right-click the uploaded file in Google Drive
2. Click **"Get link"**
3. Change access to **"Anyone with the link"**
4. Set to **"Viewer"** (read-only)
5. Click **"Copy link"**

**Your link will look like:**
```
https://drive.google.com/file/d/1a2b3c4d5e6f7g8h9i0j/view?usp=sharing
```

### Step 4: Convert to Direct Download Link

Google Drive links need to be converted for direct downloads in curl commands.

**Change this format:**
```
https://drive.google.com/file/d/FILE_ID/view?usp=sharing
```

**To this format:**
```
https://drive.google.com/uc?export=download&id=FILE_ID
```

**Example:**
- Original: `https://drive.google.com/file/d/1a2b3c4d5e6f7g8h9i0j/view?usp=sharing`
- Direct: `https://drive.google.com/uc?export=download&id=1a2b3c4d5e6f7g8h9i0j`

### Step 5: Update Course Materials

Replace `YOUR_GOOGLE_DRIVE_LINK` in these files:

1. **README.md**
   - Line ~87: Option 1 curl command
   - Line ~99: Option 2 instructions
   - Line ~110: Option 3 download button

2. **Video-Scripts/04-Download-And-Start.md**
   - Slide 3: Option 1 curl command
   - Slide 4: Option 2 instructions

**Find and replace:**
```bash
# From the course directory
sed -i '' 's|YOUR_GOOGLE_DRIVE_LINK|https://drive.google.com/uc?export=download\&id=YOUR_FILE_ID|g' README.md
sed -i '' 's|YOUR_GOOGLE_DRIVE_LINK|https://drive.google.com/uc?export=download\&id=YOUR_FILE_ID|g' Video-Scripts/04-Download-And-Start.md
```

Replace `YOUR_FILE_ID` with the actual ID from your Google Drive link.

### Step 6: Test the Download

Test that the download works:

```bash
cd ~/Desktop
curl -L "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID" -o test-download.zip
unzip test-download.zip
```

If it works, you're done!

### Step 7: Commit and Push Changes

```bash
git add README.md Video-Scripts/04-Download-And-Start.md
git commit -m "Update download links with Google Drive"
git push
```

---

## Alternative: Use a Link Shortener (Optional)

To make the link cleaner in videos/materials:

1. Go to https://bit.ly or https://tinyurl.com
2. Paste your Google Drive direct download link
3. Create short link (e.g., `bit.ly/ai-operator-course`)
4. Use this shortened link in your materials

---

## Troubleshooting

**"The download is very slow"**
- Google Drive has rate limits for large downloads
- Consider using Dropbox instead (faster for direct downloads)

**"Students get a virus warning"**
- Google scans files >25MB differently
- Add a note: "Google may show a warning for large files - click 'Download anyway'"

**"Download fails with curl"**
- Make sure you're using the `uc?export=download&id=` format
- Check that the file is set to "Anyone with the link"

**"File too large for Google Drive direct download"**
- Files >100MB may require confirmation page
- Consider splitting into smaller modules
- Or use Dropbox/your own server instead
