# 🚀 ReviewPilot - Automated Google Review Responses

**Auto-respond to every Google review in 30 seconds. Boost local SEO and win more customers — on autopilot.**

---

## 📋 What It Does

ReviewPilot monitors your Google Business Profile 24/7. When a new review arrives:

1. ✅ Detects the review instantly
2. ✍️ Generates a professional AI response
3. 📧 Emails you the draft for approval
4. 📊 Logs everything for tracking

**Result:** Every review gets answered, your local SEO improves, and more customers choose you.

---

## 🎯 Who It's For

- Dentists & medical clinics
- Restaurants & cafes
- Salons & spas
- HVAC & plumbing companies
- Real estate agents
- Any local business with 20+ Google reviews

---

## ⚡ Quick Start (5 Minutes)

### Step 1: Install Dependencies

```bash
cd reviewpilot
pip install -r requirements.txt
```

### Step 2: Create Config

```bash
cp config.example.json config.json
```

Edit `config.json` with your details:

```json
{
  "business_name": "Tony's Pizza",
  "google_account_id": "your-google-account-id",
  "smtp_host": "smtp.gmail.com",
  "smtp_port": 587,
  "smtp_user": "your-email@gmail.com",
  "smtp_password": "your-gmail-app-password",
  "owner_email": "owner@tonyspizza.com",
  "poll_interval_hours": 6
}
```

### Step 3: Get Google API Credentials

1. Go to https://console.cloud.google.com/
2. Create new project
3. Enable "Google Business Profile API"
4. Create credentials (OAuth 2.0)
5. Copy your account ID to config.json

### Step 4: Run ReviewPilot

**Test mode (simulated review):**
```bash
python review_pilot.py --config config.json --test --once
```

**Production mode (real API):**
```bash
python review_pilot.py --config config.json
```

---

## 📁 Files Created

| File | Purpose |
|------|---------|
| `reviewpilot.log` | Activity log (all actions) |
| `reviews.csv` | Spreadsheet of all reviews & responses |

---

## 🔄 How It Works

```
┌─────────────────────────────────────────────────────────────┐
│                    ReviewPilot Workflow                      │
└─────────────────────────────────────────────────────────────┘

1. POLL (Every 6 hours)
   └─→ Google Business Profile API
       └─→ Check for new reviews

2. DETECT
   └─→ New review found?
       ├─→ YES: Extract (reviewer, stars, text)
       └─→ NO: Wait for next poll

3. GENERATE RESPONSE
   └─→ AI drafts professional response
       └─→ Personalized to review content
       └─→ Matches your brand tone

4. NOTIFY OWNER
   └─→ Email with draft response
       └─→ Review details
       └─→ One-click link to post

5. LOG
   └─→ CSV row: date, reviewer, stars, response, status
```

---

## 📧 Sample Email

When a new review arrives, you get an email like this:

```
Subject: New Google Review - 5 Stars from John Smith

📬 New Google Review Received

Reviewer: John Smith
Rating: ⭐⭐⭐⭐⭐
Review: "Great service! Very professional and friendly."

✍️ Drafted Response:

Hi John,

Thank you so much for the wonderful 5-star review! We're thrilled 
you had a great experience with Tony's Pizza.

We appreciate you mentioning our professional and friendly service!

We look forward to serving you again soon!

Best regards,
The Tony's Pizza Team

✅ Next Steps:
1. Review the drafted response above
2. Edit if needed (optional)
3. [Post Response on Google] ← Click this button
```

---

## 🛠️ Configuration Options

| Setting | Description | Default |
|---------|-------------|---------|
| `business_name` | Your business name | Required |
| `google_account_id` | Google Business Profile ID | Required |
| `smtp_host` | Email server | smtp.gmail.com |
| `smtp_port` | Email port | 587 |
| `smtp_user` | Email address | Required |
| `smtp_password` | Email app password | Required |
| `owner_email` | Where to send drafts | Required |
| `poll_interval_hours` | How often to check | 6 |
| `response_tone` | friendly/formal/casual | friendly |
| `auto_post_positive` | Auto-post 4-5 star reviews | false |
| `min_stars_for_auto_post` | Min stars for auto-post | 4 |

---

## 📊 Activity Log (reviews.csv)

Every review is logged:

```csv
timestamp,reviewer_name,rating,review_text,response_draft,email_sent,posted,notes
2026-03-15 14:30:00,John Smith,5,"Great service!","Hi John, Thank you...",Yes,Pending,Review ID: test-123
```

---

## 🚀 Running Options

### Run Once (Test)
```bash
python review_pilot.py --config config.json --once
```

### Run Continuously (Production)
```bash
python review_pilot.py --config config.json
```

### Run with Test Mode (Simulated Review)
```bash
python review_pilot.py --config config.json --test --once
```

---

## 🔧 Troubleshooting

### "Config file not found"
```bash
# Make sure config.json exists
ls -la config.json

# If not, copy the example
cp config.example.json config.json
```

### "Google API error"
```bash
# Check your Google Cloud credentials
# Make sure Google Business Profile API is enabled
# Verify account ID is correct
```

### "Email not sending"
```bash
# Use Gmail app password, not regular password
# Generate at: https://myaccount.google.com/apppasswords
# Check SMTP settings in config.json
```

### "No reviews found"
```bash
# Normal if no new reviews since last poll
# Wait for next cycle (default: 6 hours)
# Or run with --test to simulate a review
```

---

## 📈 Next Steps (V2 Features)

- [ ] Auto-post positive reviews (no approval needed)
- [ ] SMS notifications for new reviews
- [ ] Response tone customization
- [ ] Multi-location support
- [ ] Web dashboard
- [ ] Analytics (response rate, avg rating trend)
- [ ] Integration with other review platforms (Yelp, Facebook)

---

## 💰 Pricing (If Selling as Service)

### Starter: £49/month
- 1 location
- Up to 50 reviews/month
- Email notifications
- Manual approval required

### Professional: £99/month ⭐
- Up to 5 locations
- Unlimited reviews
- SMS + email notifications
- Auto-post 4-5 star reviews
- Response tone customization

### Agency: £199/month
- Unlimited locations
- White-label dashboard
- Client access portals
- Priority support

---

## 🎯 Success Metrics

Track these in your reviews.csv:

| Metric | Target | Why It Matters |
|--------|--------|----------------|
| Response Rate | 100% | Google ranks you higher |
| Response Time | <24 hours | Shows you care |
| Avg Rating | 4.5+ stars | Social proof |
| Review Volume | Increasing | More customers = more reviews |

---

## 📞 Support

For issues or questions:
1. Check `reviewpilot.log` for errors
2. Review config.json settings
3. Test with `--test --once` flags

---

## 📄 License

MIT License - Use freely for personal or commercial projects.

---

**Built with ❤️ for local businesses**

Start responding to every review in 30 seconds! 🚀
