# 🚀 ReviewPilot - Quick Start Guide

**Get ReviewPilot running in 5 minutes**

---

## ⚡ Step-by-Step Setup

### 1️⃣ Install Dependencies (1 min)

```bash
cd ~/.openclaw/workspace/skills/automation-products/reviewpilot
pip install -r requirements.txt
```

### 2️⃣ Create Config (1 min)

```bash
cp config.example.json config.json
nano config.json
```

**Edit these fields:**
```json
{
  "business_name": "Your Business Name",
  "smtp_user": "your-email@gmail.com",
  "smtp_password": "your-gmail-app-password",
  "owner_email": "owner@business.com"
}
```

**Get Gmail App Password:**
1. Go to https://myaccount.google.com/apppasswords
2. Select "Mail" and your device
3. Copy the 16-character password
4. Paste into `smtp_password` field

### 3️⃣ Test Run (1 min)

```bash
# Run in test mode (simulates a review)
python review_pilot.py --config config.json --test --once
```

**Expected output:**
```
✅ ReviewPilot initialized for: Your Business Name
🔄 ReviewPilot Polling Cycle - 2026-03-15 14:30
📍 Polling for new reviews...
📊 Found new review: 5 stars from John Smith
✍️  Generating AI response...
📧 Sending approval email to owner@business.com...
✅ Approval email sent successfully
📋 Logged to reviews.csv
✅ Cycle complete. Processed 1 review(s)
```

### 4️⃣ Check Results (1 min)

**Check email:**
- You should receive an email with a draft response
- Subject: "New Google Review - 5 Stars from John Smith"

**Check files created:**
```bash
ls -la
# Should see:
# - reviewpilot.log (activity log)
# - reviews.csv (spreadsheet of reviews)
```

**View the CSV:**
```bash
cat reviews.csv
```

### 5️⃣ Run in Production (1 min)

**Option A: Run continuously (foreground)**
```bash
python review_pilot.py --config config.json
```

**Option B: Run in background**
```bash
nohup python review_pilot.py --config config.json &
```

**Option C: Run as cron job (every 6 hours)**
```bash
crontab -e
# Add this line:
0 */6 * * * cd /home/admin/.openclaw/workspace/skills/automation-products/reviewpilot && python review_pilot.py --config config.json --once
```

---

## 🔧 Google API Setup (For Production)

**To connect real Google Business Profile:**

1. **Create Google Cloud Project**
   ```
   https://console.cloud.google.com/
   → New Project → Name it "ReviewPilot"
   ```

2. **Enable Google Business Profile API**
   ```
   APIs & Services → Library → Search "Google Business Profile"
   → Enable
   ```

3. **Create OAuth Credentials**
   ```
   APIs & Services → Credentials → Create Credentials → OAuth 2.0
   → Application type: Web application
   → Download JSON
   ```

4. **Get Account ID**
   ```
   Copy your Google Business Profile account ID
   Add to config.json: "google_account_id": "YOUR_ACCOUNT_ID"
   ```

5. **Test with Real API**
   ```bash
   python review_pilot.py --config config.json --once
   ```

---

## 📊 What You Get

### Files Created

| File | Purpose |
|------|---------|
| `reviewpilot.log` | All activity logged here |
| `reviews.csv` | Spreadsheet of all reviews & responses |

### Email You Receive

```
Subject: New Google Review - 5 Stars from John Smith

📬 New Google Review Received

Reviewer: John Smith
Rating: ⭐⭐⭐⭐⭐
Review: "Great service! Very professional and friendly."

✍️ Drafted Response:

Hi John,

Thank you so much for the wonderful 5-star review! We're thrilled 
you had a great experience with Your Business Name.

We appreciate you mentioning our professional and friendly service!

We look forward to serving you again soon!

Best regards,
The Your Business Name Team

✅ Next Steps:
1. Review the drafted response above
2. Edit if needed (optional)
3. [Post Response on Google] ← Click to post
```

---

## ✅ Success Checklist

- [ ] Dependencies installed
- [ ] Config.json created and edited
- [ ] Test run completed successfully
- [ ] Email received with draft response
- [ ] reviews.csv file created
- [ ] Production mode running (or cron job set)

---

## 🐛 Troubleshooting

### "Module not found"
```bash
pip install -r requirements.txt --upgrade
```

### "Config file not found"
```bash
ls -la config.json
# If missing:
cp config.example.json config.json
```

### "Email not sending"
- Use Gmail app password (not regular password)
- Check SMTP settings in config.json
- Verify 2FA is enabled on Gmail account

### "No reviews found"
- Normal if no new reviews since last poll
- Test mode simulates a review for testing
- Production: wait for real reviews

---

## 🎯 Next Steps

1. **Monitor for 1 week** - Let it run, check emails daily
2. **Track metrics** - Response rate, time to respond
3. **Adjust tone** - Edit response templates in config if needed
4. **Scale** - Add more locations (Professional plan)

---

## 📞 Need Help?

1. Check `reviewpilot.log` for errors
2. Review config.json settings
3. Run with `--test --once` to verify setup
4. Check email spam folder for drafts

---

**You're all set!** 🎉

ReviewPilot is now monitoring your Google Business Profile 24/7.

---

**Time to complete:** 5 minutes  
**Next poll:** In 6 hours (or when new review arrives)
