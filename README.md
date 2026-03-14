# 🦞 Business Lead Generator

> **Automated system for finding local businesses without websites and sending professional website proposals**

A complete OpenClaw skill that automates lead generation, proposal creation, and email outreach for web design services.

---

## 🎯 What It Does

1. **Find Businesses** - Search Google Maps for businesses without websites
2. **Extract Details** - Collect name, address, phone, email, industry
3. **Generate Proposals** - Create personalized email proposals
4. **Send Campaigns** - Deliver emails with rate limiting
5. **Build Websites** - Ready-to-deploy templates for fulfillment

---

## 💰 Business Model

| One-Time | Monthly |
|----------|---------|
| **£397** | **£39/month** |
| 5-page website | Everything above |
| Mobile responsive | Unlimited edits |
| Contact forms | 24/7 support |
| Google Maps | Hosting included |
| SEO optimized | Analytics reports |
| 1-year hosting | Cancel anytime |

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install selenium googlemaps
```

### 2. Configure

```bash
# Run interactive setup
cd skills/business-lead-gen
python scripts/setup_wizard.py
```

Or manually create:

**`~/.openclaw/smtp.json`:**
```json
{
  "host": "smtp.gmail.com",
  "port": 587,
  "username": "your@email.com",
  "password": "your-app-password",
  "from_name": "Your Name"
}
```

**`~/.openclaw/sender_info.json`:**
```json
{
  "name": "Your Name",
  "email": "your@email.com",
  "phone": "+1-555-0123",
  "address": "123 Your Street, City, State 12345, USA"
}
```

### 3. Find Leads

```bash
# Manual method (recommended)
python scripts/find_businesses.py \
  --location "Your City" \
  --industry "restaurants" \
  --limit 50 \
  --method manual
```

### 4. Generate Proposals

```bash
python scripts/generate_proposals.py \
  --input leads.csv \
  --output proposals.csv
```

### 5. Send Emails

```bash
# Test first
python scripts/send_emails.py --input proposals.csv --dry-run

# Send for real
python scripts/send_emails.py --input proposals.csv --delay 60
```

---

## 📁 What's Included

### Scripts
- `setup_wizard.py` - Interactive configuration
- `find_businesses.py` - Lead discovery (manual/Selenium/API)
- `generate_proposals.py` - Personalized email generation
- `send_emails.py` - Campaign delivery with rate limiting

### Templates
- `restaurant/` - Restaurant/cafe website template
- `retail/` - Retail store template
- `services/` - Service provider template

### Documentation
- `README.md` - This file
- `COMPLETE.md` - Complete overview
- `BUSINESS_PLAN.md` - Full business strategy
- `QUICKSTART.md` - Quick start guide
- `READY-TO-SEND.md` - Email sending instructions

---

## 📊 Expected Results

**Per 1,000 Emails:**
- 700 delivered (70%)
- 210 opened (30%)
- 21 replies (10%)
- **2-3 customers**

**Revenue:** £794-£1,191 per 1,000 emails

---

## ⚠️ Legal Compliance

**CAN-SPAM Act Requirements:**
- ✅ Include physical address in every email
- ✅ Provide unsubscribe mechanism
- ✅ No deceptive subject lines
- ✅ Honor opt-outs within 10 days

See `references/compliance.md` for full details.

---

## 🎯 Sample Campaign

This repo includes a ready-to-send campaign:

- `leads-100.csv` - 100 sample business leads
- `proposals-100.csv` - 100 personalized proposals

**To send:**
```bash
python scripts/send_emails.py --input proposals-100.csv --delay 60
```

---

## 🛠️ Technology Stack

- **Python 3** - Core automation
- **OpenClaw** - Agent framework
- **Selenium** - Browser automation (optional)
- **Google Maps API** - Lead discovery (optional)
- **SMTP** - Email delivery

---

## 📈 Scaling Strategy

1. **Month 1:** Manual research, 500 emails → 1-2 customers
2. **Month 2-3:** Semi-automated, 2,000 emails → 4-8 customers
3. **Month 4-6:** Full automation, 5,000+ emails → 10-15 customers
4. **Year 1+:** Agency model, team, multiple niches

See `BUSINESS_PLAN.md` for complete strategy.

---

## 📞 Support

- **Documentation:** Check `skills/business-lead-gen/` folder
- **OpenClaw:** https://discord.com/invite/clawd
- **Issues:** GitHub Issues

---

## 📄 License

MIT License - See LICENSE file

**Disclaimer:** This is not legal advice. Consult with a qualified attorney regarding CAN-SPAM, GDPR, and other regulations.

---

## 🎉 Ready to Start?

1. Configure your SMTP settings
2. Update sender info with your address
3. Research businesses in your area
4. Send your first 20 emails
5. Learn, iterate, scale!

**Good luck! 🚀**

---

**Version:** 1.0.0
**Created:** 2026-03-15
**Author:** Abdelhaq
