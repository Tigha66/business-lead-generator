# 🦞 Business Lead Generator - Quick Start

## What You Got

A complete OpenClaw skill for finding businesses without websites and sending them website proposals.

**Location:** `~/.openclaw/workspace/skills/business-lead-gen/`

**Packaged:** `~/.openclaw/workspace/skills/business-lead-gen.skill`

---

## 🚀 Quick Start (3 Steps)

### Step 1: Install Dependencies

```bash
pip install selenium googlemaps
```

### Step 2: Configure Your Info

Create `~/.openclaw/sender_info.json`:

```json
{
  "name": "Your Name",
  "email": "your@email.com",
  "phone": "+1-555-0123",
  "address": "123 Business St, City, State 12345, USA"
}
```

Create `~/.openclaw/smtp.json` for sending emails:

```json
{
  "host": "smtp.gmail.com",
  "port": 587,
  "username": "your@email.com",
  "password": "your-app-password",
  "from_name": "Your Name"
}
```

### Step 3: Run the Workflow

```bash
# 1. Find businesses (manual mode to start)
cd ~/.openclaw/workspace/skills/business-lead-gen
python scripts/find_businesses.py \
  --location "New York" \
  --industry "restaurants" \
  --limit 20 \
  --output leads.csv \
  --method manual

# 2. Generate proposal emails
python scripts/generate_proposals.py \
  --input leads.csv \
  --output proposals.csv \
  --preview  # Preview first, remove to save

# 3. Send emails (dry run first!)
python scripts/send_emails.py \
  --input proposals.csv \
  --dry-run  # Remove to actually send
```

---

## 📋 What's Included

### Scripts
- `find_businesses.py` - Search for businesses (manual/Selenium/API)
- `generate_proposals.py` - Create personalized emails
- `send_emails.py` - Send campaigns with rate limiting

### Templates
- `assets/email-templates/proposal.md` - Main proposal
- `assets/email-templates/follow-up-1.md` - First follow-up
- `assets/website-templates/restaurant/index.html` - Sample website

### References
- `references/compliance.md` - CAN-SPAM, GDPR guidelines
- `references/manual-research.md` - How to find businesses manually

### Samples
- `assets/sample-leads.csv` - Example lead format
- `assets/sender-info.example.json` - Config template

---

## 💰 Your Offer

### One-Time Package: £397
- 5-page professional website
- Mobile responsive
- Contact forms & booking
- Google Maps integration
- SEO optimization
- Stripe payments
- 1-year hosting

### Monthly Package: £39/month
- Everything above
- Unlimited edits
- 24/7 support
- Hosting included
- Analytics reports
- Cancel anytime

---

## ⚠️ Important Legal Notes

**CAN-SPAM Act (US):**
- ✅ Include your physical address in every email
- ✅ Provide clear unsubscribe mechanism
- ✅ Don't use deceptive subject lines
- ✅ Honor opt-outs within 10 days

**Best Practices:**
- Start with 20-50 emails (test batch)
- Personalize each email
- Rate limit: max 50/hour
- Monitor bounce rates (<5%)

See `references/compliance.md` for full details.

---

## 🎯 Next Steps

1. **Test the workflow** with the sample leads first
2. **Research 20-50 businesses** manually using the guide
3. **Send a small test batch** (10-20 emails)
4. **Track responses** and refine your approach
5. **Scale up** once you have a working process

---

## 📞 Need Help?

- Check `SKILL.md` for detailed documentation
- Read `references/manual-research.md` for finding leads
- Review `references/compliance.md` for legal requirements

**Good luck! 🚀**
