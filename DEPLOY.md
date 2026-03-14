# 🚀 GitHub Deployment Guide

## Quick Deploy (5 Minutes)

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `business-lead-generator`
3. Description: "Automated lead generation for web design services"
4. **Public** or **Private** (your choice)
5. **DO NOT** initialize with README (we already have one)
6. Click "Create repository"

### Step 2: Configure Git Remote

```bash
cd ~/.openclaw/workspace

# Replace YOUR_USERNAME with your GitHub username
git remote add origin https://github.com/YOUR_USERNAME/business-lead-generator.git

# Verify
git remote -v
```

### Step 3: Push to GitHub

```bash
# Push main branch
git push -u origin main

# Optional: Create release tag
git tag -a v1.0.0 -m "Initial release - Complete automation system"
git push origin v1.0.0
```

### Step 4: Verify

Visit: `https://github.com/YOUR_USERNAME/business-lead-generator`

---

## Alternative: Using Script

```bash
cd ~/.openclaw/workspace

# Edit the script with your username
nano push-to-github.sh
# Change YOUR_USERNAME to your GitHub username

# Run it
./push-to-github.sh
```

---

## Troubleshooting

### "Remote already exists"
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/business-lead-generator.git
```

### "Authentication failed"
```bash
# Use personal access token instead of password
# Create token at: https://github.com/settings/tokens
# Then use: https://YOUR_TOKEN@github.com/YOUR_USERNAME/repo.git
```

### "Repository not found"
- Make sure you created the repo on GitHub first
- Check the URL is correct
- Verify username spelling

---

## What Gets Pushed

✅ **Included:**
- All scripts (find, generate, send, setup)
- Website templates (restaurant, retail, services)
- Email templates
- Documentation (README, guides, business plan)
- Sample data

❌ **Excluded (.gitignore):**
- `sender_info.json` (your personal info)
- `smtp.json` (your email credentials)
- `leads-*.csv` (your lead data)
- `proposals-*.csv` (your campaigns)
- `*.skill` packages
- API keys

---

## After Pushing

### 1. Add Repository Details

On GitHub:
- Add description
- Add topics: `lead-generation`, `email-automation`, `web-design`, `openclaw`, `business-automation`
- Pin the repository

### 2. Create Release

```bash
git tag -a v1.0.0 -m "v1.0.0 - Initial Release"
git push origin v1.0.0
```

Then on GitHub:
- Go to Releases
- Create release from tag v1.0.0
- Add release notes

### 3. Share Your Repo

- Add to your portfolio
- Share on social media
- Submit to OpenClaw community
- Post on Reddit (r/sideproject, r/entrepreneur)

---

## Deploy to Production Server (Optional)

### Option 1: VPS (DigitalOcean, Linode, etc.)

```bash
# SSH to your server
ssh user@your-server.com

# Clone repo
git clone https://github.com/YOUR_USERNAME/business-lead-generator.git
cd business-lead-generator

# Install dependencies
pip install selenium googlemaps

# Configure
# Edit ~/.openclaw/smtp.json and sender_info.json

# Run your first campaign
python scripts/send_emails.py --input proposals-100.csv --delay 60
```

### Option 2: GitHub Actions (Automated)

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: echo "Add your tests here"
```

---

## Security Best Practices

### Never Commit:
- ❌ SMTP passwords
- ❌ API keys
- ❌ Personal addresses
- ❌ Lead lists with real emails
- ❌ Customer data

### Use Environment Variables:
```bash
# .env file (add to .gitignore)
SMTP_HOST=smtp.gmail.com
SMTP_USER=your@email.com
SMTP_PASS=your-password
SENDER_ADDRESS="Your Address"
```

### Rotate Credentials:
- Change passwords regularly
- Use app-specific passwords
- Revoke access if compromised

---

## Next Steps After Deployment

1. **Test the installation** on a fresh machine
2. **Write unit tests** for scripts
3. **Add CI/CD** pipeline
4. **Create demo video**
5. **Write blog post** about your project
6. **Share on Product Hunt**
7. **Submit to directories**

---

## Questions?

- GitHub Docs: https://docs.github.com
- Git Basics: https://git-scm.com/book
- OpenClaw: https://docs.openclaw.ai

---

**Good luck with your deployment! 🚀**
