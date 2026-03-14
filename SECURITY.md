# 🔒 Security & Privacy Protection

## ✅ What's Protected (NOT pushed to GitHub)

### Your Personal Credentials
- ❌ `~/.openclaw/sender_info.json` - Your name, address, phone, email
- ❌ `~/.openclaw/smtp.json` - Your email passwords
- ❌ `~/.openclaw/pricing.json` - Your pricing configuration
- ❌ `~/.openclaw/google_maps_api_key.txt` - API keys

### Your Business Data
- ❌ `leads-*.csv` - Your lead lists (business contacts you collect)
- ❌ `proposals-*.csv` - Your generated email campaigns
- ❌ `followups-*.csv` - Your follow-up campaigns
- ❌ `*.skill` - Compiled skill packages

### System Files
- ❌ `__pycache__/` - Python cache
- ❌ `*.log` - Log files
- ❌ `.env`, `.env.local` - Environment variables

---

## ✅ What IS Pushed to GitHub (Safe to Share)

### Code & Scripts
- ✅ `scripts/*.py` - Automation scripts (no credentials)
- ✅ `assets/website-templates/` - Website HTML templates
- ✅ `assets/email-templates/` - Email template files

### Documentation
- ✅ `README.md` - Project documentation
- ✅ `DEPLOY.md` - Deployment guide
- ✅ `BUSINESS_PLAN.md` - Business strategy
- ✅ `SKILL.md` - Technical documentation

### Sample Data (Public)
- ✅ `assets/sample-leads.csv` - Example format only (fake data)

---

## 🔐 Security Measures in Place

### 1. .gitignore Configuration
```
# Protects credentials
~/.openclaw/sender_info.json
~/.openclaw/smtp.json

# Protects your business data
leads-*.csv
proposals-*.csv
```

### 2. Git Tracking Removed
```bash
# Already removed from git history:
git rm --cached skills/business-lead-gen/proposals-100.csv
git rm --cached skills/business-lead-gen/leads-100.csv
```

### 3. Template Files Use Variables
Email templates use placeholders like:
- `{{sender_name}}` - Filled from your local config
- `{{sender_address}}` - Filled from your local config
- Never hardcoded in templates

---

## 📋 Pre-Push Security Checklist

Before pushing to GitHub, verify:

- [ ] `sender_info.json` is NOT in the commit
- [ ] `smtp.json` is NOT in the commit
- [ ] Your lead CSVs are NOT in the commit
- [ ] No API keys in code
- [ ] No hardcoded passwords
- [ ] No personal address in templates

**Run this check:**
```bash
cd ~/.openclaw/workspace
git status
git diff --cached
```

Look for any `.json` or `.csv` files - they should NOT appear!

---

## 🔍 Verify Before Pushing

```bash
# See what will be pushed
git status

# Check for sensitive files
git ls-files | grep -E '\.(json|csv)$'

# Should only show:
# - assets/sample-leads.csv (fake sample data)
# - assets/sender-info.example.json (example template)
# - package.json (if exists)
```

---

## 🚨 If You Accidentally Commit Sensitive Data

### 1. If NOT pushed yet:
```bash
git reset HEAD~1
# Remove the file
git add .
git commit -m "Fixed: removed sensitive data"
```

### 2. If already pushed:
```bash
# Remove from history
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch PATH_TO_FILE' \
  --prune-empty --tag-name-filter cat -- --all

# Force push (careful!)
git push origin --force --all
```

### 3. Rotate compromised credentials:
- Change passwords immediately
- Revoke API keys
- Create new SMTP passwords

---

## 📊 Current Repository Status

**Protected files (NOT pushed):**
- ✅ `~/.openclaw/sender_info.json` - Your personal info
- ✅ `~/.openclaw/smtp.json` - Email credentials
- ✅ `leads-100.csv` - Your lead list (stays local)
- ✅ `proposals-100.csv` - Your campaigns (stays local)

**Safe to push:**
- ✅ All Python scripts
- ✅ Website templates
- ✅ Email templates
- ✅ Documentation
- ✅ Sample/example files only

---

## 🛡️ Best Practices

### When Adding New Files:
```bash
# Always check before committing
git status

# If adding CSV or JSON, double-check:
git add filename
git diff --cached
```

### When Creating Config Files:
```bash
# Always put in ~/.openclaw/ folder (gitignored)
# Never in workspace root
```

### When Generating Leads:
```bash
# Save to: ~/.openclaw/workspace/skills/business-lead-gen/
# But DON'T commit: git add leads.csv (skip this)
# Or explicitly ignore: git update-index --assume-unchanged leads.csv
```

---

## ✅ Final Security Confirmation

**Before you push, confirm:**

1. Run: `git status`
   - Should NOT show any `.json` files (except examples)
   - Should NOT show your lead/proposal CSVs

2. Run: `git ls-files | grep -E '\.(json|csv)$'`
   - Should only show sample/template files

3. Check: No passwords, API keys, or personal addresses in code

**If all clear → Safe to push! 🚀**

---

## 📞 Questions?

- Review: `cat .gitignore`
- Check: `git status`
- Verify: `git diff --cached`

**When in doubt, ask before pushing!**
