# RAZ Worksheet Automation — One-Time Setup

Run these 4 commands in Terminal **once** to connect everything.

---

## Step 1 — Clone your RAZ repo to your Mac

```bash
cd ~/Claude/Projects
git clone https://github.com/lexilink-ideation/RAZ--Junior-IELTS-Workbook.git
```

This creates the folder Claude will write worksheets into.

---

## Step 2 — Store your GitHub credentials (so Claude can push)

```bash
git config --global credential.helper osxkeychain
```

Then do a manual push once to save your password:

```bash
cd ~/Claude/Projects/RAZ--Junior-IELTS-Workbook
git pull  # enter your GitHub username + a Personal Access Token when prompted
```

> **Personal Access Token:** Go to github.com → Settings → Developer Settings →
> Personal Access Tokens → Tokens (classic) → Generate new token.
> Give it `repo` scope. Use this token as your "password" when prompted.
> macOS Keychain saves it — you won't be asked again.

---

## Step 3 — Verify git is ready

```bash
cd ~/Claude/Projects/RAZ--Junior-IELTS-Workbook
git push
```

You should see "Everything up to date." — if so, auto-push is ready.

---

## Daily Workflow (after setup)

1. **Drop a RAZ PDF** into:
   `~/Claude/Projects/IELTS Vocabulary workbook/raz-watch/input/`

2. **Wait** — Claude checks every hour, or you can click **Run now** on the
   `raz-worksheet-generator` task in the Cowork sidebar.

3. **Done** — the worksheet HTML is pushed to your GitHub Pages automatically.
   Your students can access it at:
   `https://lexilink-ideation.github.io/RAZ--Junior-IELTS-Workbook/level-X/book-name.html`

Processed PDFs are moved to: `raz-watch/done/` so they won't be re-processed.

---

## Folder Structure

```
~/Claude/Projects/
├── IELTS Vocabulary workbook/
│   └── raz-watch/
│       ├── input/          ← DROP PDFs HERE
│       ├── done/           ← processed PDFs land here
│       ├── extract_pdf.py  ← PDF text extractor
│       └── WORKSHEET_TEMPLATE.html
│
└── RAZ--Junior-IELTS-Workbook/   ← git repo (cloned in Step 1)
    ├── index.html
    ├── level-a/
    ├── level-b/
    └── ...
```
