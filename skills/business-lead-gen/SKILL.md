---
name: business-lead-gen
description: Find local businesses without websites, generate website proposals, and send outreach emails. Use when: (1) Finding businesses without online presence via Google Maps/search, (2) Creating website proposals for small businesses, (3) Sending cold outreach emails with pricing packages, (4) Building lead lists for web design services.
---

# Business Lead Generation Skill

Automated workflow for finding local businesses without websites and sending them professional website proposals.

## Quick Start

```bash
# Find businesses in a specific niche/location
python scripts/find_businesses.py --location "New York" --industry "restaurants" --limit 50

# Generate proposal emails
python scripts/generate_proposals.py --input leads.csv --template assets/email-templates/proposal.md

# Send emails (requires SMTP config)
python scripts/send_emails.py --input proposals.csv --smtp-config ~/.openclaw/smtp.json
```

## Workflow Overview

1. **Find Businesses** - Search for businesses without websites using Google Maps API or web scraping
2. **Extract Details** - Collect business name, location, contact info, industry
3. **Generate Proposals** - Create personalized emails with pricing packages
4. **Send Outreach** - Deliver emails via SMTP or email service

## Core Components

### Finding Businesses

Use `scripts/find_businesses.py` to search for businesses:

```bash
python scripts/find_businesses.py \
  --location "Los Angeles, CA" \
  --industry "retail" \
  --limit 100 \
  --output leads.csv
```

**Parameters:**
- `--location`: City/region to search
- `--industry`: Business category (restaurants, retail, services, etc.)
- `--limit`: Max results (start with 20-50 for testing)
- `--output`: CSV file for leads

**Output CSV format:**
```csv
business_name,address,phone,email,industry,google_maps_url,has_website
```

### Generating Proposals

Use `scripts/generate_proposals.py` to create personalized emails:

```bash
python scripts/generate_proposals.py \
  --input leads.csv \
  --template assets/email-templates/proposal.md \
  --output proposals.csv
```

**Email Template Variables:**
- `{{business_name}}` - Business name
- `{{owner_name}}` - Owner/contact name (if available)
- `{{location}}` - Business location
- `{{industry}}` - Industry type

### Sending Emails

Use `scripts/send_emails.py` for email delivery:

```bash
python scripts/send_emails.py \
  --input proposals.csv \
  --smtp-config ~/.openclaw/smtp.json \
  --rate-limit 50 \
  --delay 60
```

**SMTP Config Format** (`~/.openclaw/smtp.json`):
```json
{
  "host": "smtp.gmail.com",
  "port": 587,
  "username": "your@email.com",
  "password": "app-password",
  "from_name": "Your Name"
}
```

## Pricing Packages

### One-Time Package (£397)
- Professional 5-page website
- Mobile responsive design
- Contact forms & booking system
- Google Maps integration
- SEO optimization
- Stripe payment integration
- 1-year hosting included

### Monthly Package (£39/month)
- Unlimited website edits
- 24/7 priority support (24h response)
- Hosting always included
- Stripe maintenance
- Monthly analytics reports
- Cancel anytime

## Legal Compliance

**CAN-SPAM Act (US) Requirements:**
- Include physical mailing address in emails
- Provide clear opt-out/unsubscribe mechanism
- Don't use deceptive subject lines
- Honor opt-out requests within 10 days

**GDPR Considerations:**
- Only contact businesses with legitimate interest
- Respect opt-out requests immediately
- Don't store personal data longer than needed

**Best Practices:**
- Start with small batches (20-50 emails)
- Personalize each email genuinely
- Track opt-outs and honor them
- Use proper email authentication (SPF, DKIM)

## Scripts Reference

| Script | Purpose | Input | Output |
|--------|---------|-------|--------|
| `find_businesses.py` | Search for businesses | Location, industry | CSV with leads |
| `generate_proposals.py` | Create email drafts | Leads CSV | Proposals CSV |
| `send_emails.py` | Send outreach emails | Proposals CSV | Delivery log |
| `track_responses.py` | Monitor replies | Email inbox | Response report |

## Website Templates

Pre-built templates in `assets/website-templates/`:

- `restaurant/` - Restaurant/cafe template
- `retail/` - Retail store template
- `services/` - Service provider template
- `professional/` - Professional services template

Each template includes:
- 5 pages (Home, About, Services, Contact, Booking)
- Mobile responsive CSS
- Contact form with validation
- Google Maps embed
- Stripe integration ready
- SEO meta tags

## Email Templates

Pre-built templates in `assets/email-templates/`:

- `proposal.md` - Main proposal email
- `follow-up-1.md` - First follow-up (3 days)
- `follow-up-2.md` - Second follow-up (7 days)
- `thank-you.md` - After conversion

## Rate Limiting & Best Practices

**Email Sending:**
- Max 50 emails/hour for new accounts
- 60-second delay between emails
- Warm up new email accounts gradually
- Monitor bounce rates (<5% ideal)

**Google Maps Scraping:**
- Add 2-5 second delays between requests
- Rotate user agents
- Use proxies for large-scale operations
- Respect ToS - consider official API

**Tracking:**
- Log all sent emails
- Track open rates (use pixel tracking)
- Monitor reply rates
- A/B test subject lines

## Error Handling

**Common Issues:**

1. **Email bounces** - Remove invalid addresses, verify before sending
2. **Low reply rate** - Improve personalization, test different subject lines
3. **Spam complaints** - Reduce volume, improve targeting, add unsubscribe
4. **API rate limits** - Add delays, use official APIs, rotate keys

## Security Notes

- Never commit SMTP credentials to version control
- Use app-specific passwords for email accounts
- Encrypt stored lead data
- Regularly purge old leads (90-day retention)

## Related Files

### Core Scripts
- `scripts/setup_wizard.py` - Interactive setup wizard
- `scripts/find_businesses.py` - Business discovery (manual/Selenium/API)
- `scripts/generate_proposals.py` - Personalized email generation
- `scripts/send_emails.py` - Campaign delivery with rate limiting

### Templates
- `assets/email-templates/proposal.md` - Main proposal email
- `assets/email-templates/follow-up-1.md` - First follow-up
- `assets/website-templates/restaurant/index.html` - Restaurant template
- `assets/website-templates/retail/index.html` - Retail store template
- `assets/website-templates/services/index.html` - Service provider template

### Documentation
- `README.md` - Complete overview
- `QUICKSTART.md` - Quick start guide
- `BUSINESS_PLAN.md` - Full business strategy
- `references/compliance.md` - CAN-SPAM, GDPR guidelines
- `references/manual-research.md` - Manual research guide

### Configuration Examples
- `assets/sender-info.example.json` - Sender info template
- `assets/sample-leads.csv` - Sample lead data
