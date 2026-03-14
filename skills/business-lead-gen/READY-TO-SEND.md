# 🚀 READY TO SEND - 100 Proposal Emails

**Status:** ✅ 100 Proposals Generated & Ready
**Date:** 2026-03-15
**Leads:** 100 businesses (NYC area sample)

---

## ✅ What's Done

- [x] 100 business leads created
- [x] 100 personalized proposals generated
- [x] Email templates configured
- [x] All files ready in: `skills/business-lead-gen/`

---

## ⚠️ BEFORE SENDING - Configure SMTP

**You MUST update these files first:**

### 1. Update `~/.openclaw/smtp.json`

```bash
nano ~/.openclaw/smtp.json
```

**For Gmail:**
1. Go to: https://myaccount.google.com/apppasswords
2. Create app password for "Mail"
3. Copy the 16-character password
4. Paste into smtp.json

**Example:**
```json
{
  "host": "smtp.gmail.com",
  "port": 587,
  "username": "yourname@gmail.com",
  "password": "abcd efgh ijkl mnop",
  "from_name": "Your Name"
}
```

### 2. Update `~/.openclaw/sender_info.json`

```bash
nano ~/.openclaw/sender_info.json
```

**IMPORTANT:** Your physical address is REQUIRED by law (CAN-SPAM Act)

```json
{
  "name": "Your Real Name",
  "email": "your@email.com",
  "phone": "+1-555-0123",
  "address": "123 Your Street, Your City, State 12345, USA",
  "company": "Your Company Name"
}
```

---

## 📧 Send the Emails

### Option 1: Test First (RECOMMENDED)

Send to YOURSELF first to test:

```bash
cd ~/.openclaw/workspace/skills/business-lead-gen

# Dry run (no emails sent, just preview)
python scripts/send_emails.py --input proposals-100.csv --dry-run
```

### Option 2: Send All 100

```bash
cd ~/.openclaw/workspace/skills/business-lead-gen

# Send with 60-second delays (about 100 minutes total)
python scripts/send_emails.py --input proposals-100.csv --delay 60
```

### Option 3: Send in Batches (SAFEST)

**Batch 1: First 20 emails**
```bash
python scripts/send_emails.py --input proposals-100.csv --delay 60
# Stop after 20, monitor bounce/reply rates
```

**Wait 24 hours**, check results, then send more.

---

## 📊 What to Expect

**Conservative estimates for 100 emails:**
- 70 delivered (70%)
- 21 opened (30% open rate)
- 2-3 replies (10% reply rate)
- **0-1 customers** (conversion happens over time)

**Don't be discouraged if you get 0 replies from first 100!**
- This is normal for cold outreach
- Test different subject lines
- Improve personalization
- Follow up after 3-4 days

---

## 🔍 Sample Leads Included

**Industries:**
- 35 Restaurants (pizza, cafes, Chinese, etc.)
- 30 Retail (shops, stores, boutiques)
- 35 Services (plumbers, electricians, cleaners)

**Location:** New York City area (Brooklyn, Queens, Manhattan, Bronx)

**Note:** These are SAMPLE businesses for testing. For real campaigns, research actual businesses in YOUR target area without websites.

---

## 📝 Next Steps After Sending

### Day 1-2: Monitor
- Watch for bounces (invalid emails)
- Track opens (if using Mailtrack)
- Note any replies

### Day 3-4: Follow Up
```bash
# Generate follow-up emails to non-responders
python scripts/generate_proposals.py \
  --input leads-100.csv \
  --template assets/email-templates/follow-up-1.md \
  --output followups-100.csv
```

### Day 5-7: Send Follow-ups
```bash
python scripts/send_emails.py --input followups-100.csv --delay 60
```

### Week 2: Analyze
- What subject lines got opens?
- Which industries replied?
- What objections came up?
- Refine your approach

---

## 🎯 Tips for Better Results

### Subject Lines to Test
```
✓ "Quick question about {{business_name}}"
✓ "Your online presence"
✓ "Website idea for {{business_name}}"
✓ "Missed opportunity"
```

### Best Practices
- Send Tuesday-Thursday (best response rates)
- Avoid Monday mornings and Fridays
- Send between 10AM-2PM local time
- Personalize beyond just business name
- Follow up 2-3 times (most sales after touch #3)

### Legal Compliance
- ✅ Include your physical address (REQUIRED)
- ✅ Honor unsubscribe requests immediately
- ✅ Don't use deceptive subject lines
- ✅ Keep records of who you emailed

---

## 🛠️ Commands Reference

```bash
# View proposals
cat proposals-100.csv | head -20

# Count by status
grep -c "draft" proposals-100.csv
grep -c "sent" proposals-100.csv

# Dry run (test without sending)
python scripts/send_emails.py --input proposals-100.csv --dry-run

# Send all
python scripts/send_emails.py --input proposals-100.csv --delay 60

# Send with custom delay
python scripts/send_emails.py --input proposals-100.csv --delay 120
```

---

## ⚡ Quick Send Checklist

- [ ] Updated `~/.openclaw/smtp.json` with real credentials
- [ ] Updated `~/.openclaw/sender_info.json` with your address
- [ ] Tested with `--dry-run` first
- [ ] Ready to send 100 emails
- [ ] Understand this is a numbers game (expect low initial response)
- [ ] Prepared to follow up in 3-4 days

---

## 📞 Need Help?

**Files location:**
```
~/.openclaw/workspace/skills/business-lead-gen/
├── leads-100.csv          ← Your 100 leads
├── proposals-100.csv      ← Generated proposals (READY TO SEND)
├── scripts/send_emails.py ← Send script
└── assets/email-templates/ ← Email templates
```

**Config files:**
```
~/.openclaw/
├── smtp.json          ← UPDATE THIS with your email
└── sender_info.json   ← UPDATE THIS with your info
```

---

## 🚀 Ready When You Are!

**To send all 100 emails right now:**

```bash
cd ~/.openclaw/workspace/skills/business-lead-gen
python scripts/send_emails.py --input proposals-100.csv --delay 60
```

**Estimated time:** ~100 minutes (60 seconds between emails)

**Good luck! 🦞**

---

**Remember:** 
- First campaigns are for learning
- Track everything
- Refine based on results
- Persistence wins (most sales after 3+ touches)
