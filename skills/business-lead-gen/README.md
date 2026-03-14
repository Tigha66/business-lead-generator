# 🦞 Business Lead Generator

> **Find local businesses without websites → Send professional proposals → Close deals**

A complete OpenClaw skill for automated lead generation and outreach to businesses without web presence.

---

## 🎯 What It Does

This skill automates the entire workflow of:

1. **Finding Businesses** - Search Google Maps for businesses without websites
2. **Extracting Details** - Collect name, address, phone, email, industry
3. **Generating Proposals** - Create personalized email proposals
4. **Sending Campaigns** - Deliver emails with rate limiting and tracking
5. **Building Websites** - Ready-to-deploy templates for quick fulfillment

---

## 💰 Business Model

**Offer Two Packages:**

| One-Time | Monthly |
|----------|---------|
| £397 | £39/month |
| 5-page website | Everything above |
| Mobile responsive | Unlimited edits |
| Contact forms | 24/7 support |
| Google Maps | Hosting included |
| SEO optimized | Analytics reports |
| 1-year hosting | Cancel anytime |
| Stripe payments | |

---

## 🚀 Quick Start

### 1. Install the Skill

```bash
# Skill is already packaged at:
~/.openclaw/workspace/skills/business-lead-gen.skill
```

### 2. Run Setup Wizard

```bash
cd ~/.openclaw/workspace/skills/business-lead-gen
python scripts/setup_wizard.py
```

This guides you through:
- Your contact information
- SMTP email configuration
- Pricing customization

### 3. Find Leads

```bash
# Manual method (recommended for start)
python scripts/find_businesses.py \
  --location "New York" \
  --industry "restaurants" \
  --limit 50 \
  --method manual \
  --output leads.csv
```

### 4. Generate Proposals

```bash
python scripts/generate_proposals.py \
  --input leads.csv \
  --output proposals.csv \
  --preview  # Remove after testing
```

### 5. Send Emails

```bash
# Always dry-run first!
python scripts/send_emails.py \
  --input proposals.csv \
  --dry-run  # Remove to actually send

# Send for real
python scripts/send_emails.py \
  --input proposals.csv \
  --delay 60  # Seconds between emails
```

---

## 📁 What's Included

### Scripts

| Script | Purpose |
|--------|---------|
| `setup_wizard.py` | Interactive configuration |
| `find_businesses.py` | Lead discovery (manual/Selenium/API) |
| `generate_proposals.py` | Personalized email generation |
| `send_emails.py` | Campaign delivery with rate limiting |

### Templates

**Email Templates:**
- `proposal.md` - Main proposal email
- `follow-up-1.md` - First follow-up (Day 4)

**Website Templates:**
- `restaurant/` - For restaurants/cafes
- `retail/` - For retail stores
- `services/` - For service providers (plumbers, electricians, etc.)

### Documentation

- `SKILL.md` - Full technical documentation
- `QUICKSTART.md` - Quick start guide
- `BUSINESS_PLAN.md` - Complete business strategy
- `references/compliance.md` - CAN-SPAM, GDPR compliance
- `references/manual-research.md` - Manual lead research guide

---

## 🎨 Website Templates

Each template includes:

- ✅ 5 pages (Home, About, Services, Contact, Booking)
- ✅ Mobile responsive design
- ✅ Contact/quote forms
- ✅ Google Maps integration
- ✅ SEO meta tags
- ✅ Stripe payment ready
- ✅ Social media links
- ✅ Professional styling

**Industries Covered:**
1. 🍽️ Restaurant/Cafe
2. 🛍️ Retail Store
3. 🔧 Service Provider (plumber, electrician, cleaner)

---

## 📧 Email Campaign Best Practices

### Subject Lines That Work

```
✓ "Quick question about {{business_name}}"
✓ "Your online presence, {{owner_name}}"
✓ "Website idea for {{business_name}}"
✓ "Missed opportunity for {{business_name}}"
```

### Email Schedule

| Day | Email | Purpose |
|-----|-------|---------|
| 1 | Proposal | Initial offer |
| 4 | Follow-up 1 | Gentle reminder |
| 10 | Follow-up 2 | Final attempt |

### Legal Requirements (CAN-SPAM)

- ✅ Include your physical address
- ✅ Provide unsubscribe mechanism
- ✅ No deceptive subject lines
- ✅ Honor opt-outs within 10 days

See `references/compliance.md` for full details.

---

## 📊 Expected Metrics

**Conservative Estimates:**

```
1,000 emails sent
├── 700 delivered (70%)
├── 210 opened (30% open rate)
├── 21 replies (10% reply rate)
├── 7 qualified (33% qualification)
└── 2-3 customers (30% close rate)
```

**Overall conversion: 0.2-0.3%**

**Revenue per 1,000 emails:**
- One-time: 2-3 × £397 = £794-£1,191
- Monthly: 1-2 × £39 = £39-£78 recurring

---

## 🛠️ Configuration Files

### Sender Info (`~/.openclaw/sender_info.json`)

```json
{
  "name": "Your Name",
  "email": "your@email.com",
  "phone": "+1-555-0123",
  "address": "123 Business St, City, State 12345, USA",
  "company": "Your Web Services"
}
```

### SMTP Config (`~/.openclaw/smtp.json`)

```json
{
  "host": "smtp.gmail.com",
  "port": 587,
  "username": "your@email.com",
  "password": "your-app-password",
  "from_name": "Your Name"
}
```

### Pricing (`~/.openclaw/pricing.json`)

```json
{
  "one_time_amount": "397",
  "one_time_currency": "£",
  "monthly_amount": "39",
  "monthly_currency": "£"
}
```

---

## 🔍 Finding Leads

### Method 1: Manual (Recommended)

**Pros:** High quality, verified, free
**Cons:** Time-intensive (50-100/hour)

**Process:**
1. Open Google Maps
2. Search "[industry] in [city]"
3. Click each listing
4. Check for website button
5. Record businesses without websites

### Method 2: Google Maps API

**Pros:** Automated, scalable
**Cons:** Costs $5/1,000 requests

Requires API key from Google Cloud Console.

### Method 3: Selenium Automation

**Pros:** Free, scalable
**Cons:** Technical setup, ToS concerns

Use rotating proxies and rate limiting.

---

## 📈 Scaling Strategy

### Month 1: Test & Learn
- 500 emails total
- Manual lead research
- Refine email templates
- Close 1-3 customers

### Month 2-3: Optimize
- 2,000 emails/month
- Semi-automated research
- A/B test subject lines
- Close 5-10 customers

### Month 4-6: Scale
- 5,000+ emails/month
- Multiple email accounts
- Hire VA for follow-ups
- Close 15-30 customers

### Year 1+: Agency
- Team of 2-5
- Multiple niches
- Upsell services
- £50K-£100K/year

---

## ⚠️ Important Notes

### Email Deliverability

- Warm up new email accounts (start with 10/day)
- Use proper authentication (SPF, DKIM, DMARC)
- Monitor bounce rates (keep under 5%)
- Use multiple accounts for scale

### Legal Compliance

- **CAN-SPAM (US):** Address, unsubscribe, no deception
- **GDPR (EU):** Legitimate interest, honor opt-outs
- **UK PECR:** Similar to GDPR for B2B

Always consult a lawyer for your specific situation.

### Best Practices

- Start small (20-50 emails test batch)
- Personalize each email genuinely
- Track everything (opens, replies, conversions)
- Follow up 2-3 times (most sales happen after touch #3)
- Deliver quality websites (builds reputation)

---

## 📞 Support & Resources

### Documentation
- `SKILL.md` - Technical docs
- `QUICKSTART.md` - Getting started
- `BUSINESS_PLAN.md` - Full strategy
- `references/` - Compliance & research guides

### Tools Recommended
- **Hunter.io** - Find email addresses
- **Mailtrack** - Track email opens
- **Netlify** - Host websites (free tier)
- **Stripe** - Payment processing
- **Notion** - CRM & tracking

### Community
- OpenClaw Discord: https://discord.com/invite/clawd
- Skill updates: Check `business-lead-gen.skill`

---

## 🎯 Success Checklist

**Before Launch:**
- [ ] SMTP configured and tested
- [ ] Sender info includes physical address
- [ ] Email templates customized
- [ ] Website templates reviewed
- [ ] Stripe account set up
- [ ] Tracking spreadsheet created

**First Campaign:**
- [ ] 20-50 leads researched
- [ ] Proposals generated
- [ ] Dry run completed
- [ ] First 20 emails sent
- [ ] Tracking opens/replies

**After First Week:**
- [ ] Analyze open rates
- [ ] Analyze reply rates
- [ ] Refine subject lines
- [ ] Follow up on replies
- [ ] Close first customers

---

## 📄 License

This skill is provided as-is for educational and business purposes.

**Disclaimer:** This is not legal advice. Consult with a qualified attorney regarding CAN-SPAM, GDPR, and other regulations applicable to your business.

---

## 🦞 Built with OpenClaw

Part of the OpenClaw ecosystem. Share your success stories and improvements!

**Version:** 1.0.0
**Author:** Your Name
**Updated:** 2026-03-15
