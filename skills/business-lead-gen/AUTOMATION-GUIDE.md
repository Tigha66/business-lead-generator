# 🤖 Complete Automation Guide

Your business lead generation system is now **fully automated**. Here's how everything works.

---

## 📊 What's Automated

| Task | Frequency | Script |
|------|-----------|--------|
| **Initial Emails** | Manual trigger | `send_emails.py` |
| **Follow-Up #1** | Auto (3 days after) | `send_follow_ups.py --follow-up 1` |
| **Follow-Up #2** | Auto (10 days after) | `send_follow_ups.py --follow-up 2` |
| **Batch Generation** | On-demand | `find_businesses_batch.py` |

---

## 🚀 Quick Commands

### **Launch Campaign Manager** (Recommended)
```bash
cd ~/.openclaw/workspace/skills/business-lead-gen
./campaign-manager.sh
```
Interactive menu for all operations!

### **Send Initial Emails**
```bash
# Send 20 emails (safe daily limit)
python scripts/send_emails.py --input proposals-100.csv --limit 20 --delay 60

# Send 50 emails (aggressive)
python scripts/send_emails.py --input proposals-100.csv --limit 50 --delay 30
```

### **Send Follow-Ups**
```bash
# Test run (dry-run)
python scripts/send_follow_ups.py --input proposals-100.csv --follow-up 1 --dry-run

# Actually send
python scripts/send_follow_ups.py --input proposals-100.csv --follow-up 1
```

### **Generate New Batches**
```bash
# Generate 900 leads across 18 city/industry combos
python scripts/find_businesses_batch.py
```

---

## ⏰ Setup Automated Follow-Ups (Cron)

### **Option 1: Auto-Install**
```bash
./scripts/setup-followups.sh
```

### **Option 2: Manual Cron**
```bash
crontab -e
```

Add these lines:
```cron
# Business Lead Gen - Automated Follow-Ups
# Run daily at 10 AM

# Follow-up #1: 3 days after initial email
0 10 * * * cd /home/admin/.openclaw/workspace/skills/business-lead-gen && python3 scripts/send_follow_ups.py --input proposals-100.csv --follow-up 1 >> logs/followup.log 2>&1

# Follow-up #2: 10 days after initial email  
0 10 * * * cd /home/admin/.openclaw/workspace/skills/business-lead-gen && python3 scripts/send_follow_ups.py --input proposals-100.csv --follow-up 2 >> logs/followup.log 2>&1
```

### **Verify Cron**
```bash
crontab -l | grep followup
```

---

## 📁 Available Lead Batches

After running `find_businesses_batch.py`, you'll have:

| City | Industries | Leads Each | Total |
|------|------------|------------|-------|
| Los Angeles | Restaurants, Retail, Services | 50 | 150 |
| Chicago | Restaurants, Retail, Services | 50 | 150 |
| Houston | Restaurants, Retail, Services | 50 | 150 |
| Miami | Restaurants, Retail, Services | 50 | 150 |
| Atlanta | Restaurants, Retail, Services | 50 | 150 |
| Seattle | Restaurants, Retail, Services | 50 | 150 |
| **TOTAL** | **18 batches** | **50** | **900** |

### **Launch a Batch**
```bash
# LA Restaurants
python scripts/send_emails.py --input batches/proposals-LA-Restaurants-20260315.csv --limit 20

# Chicago Retail
python scripts/send_emails.py --input batches/proposals-Chicago-Retail-20260315.csv --limit 20
```

---

## 📈 Revenue Projection

### **NYC Campaign (100 leads)**
| Metric | Conservative | Optimistic |
|--------|-------------|------------|
| Emails sent | 100 | 100 |
| Reply rate | 5% | 10% |
| Conversions | 1 | 3 |
| **Revenue** | **£397** | **£1,191** |

### **All Batches (1,000 total leads)**
| Metric | Conservative | Optimistic |
|--------|-------------|------------|
| Emails sent | 1,000 | 1,000 |
| Reply rate | 5% | 10% |
| Conversions | 10 | 30 |
| **Revenue** | **£3,970** | **£11,910** |

---

## 🔧 Troubleshooting

### **Emails Not Sending**
```bash
# Check SMTP config
cat ~/.openclaw/smtp.json

# Test connection
python3 -c "import smtplib; s=smtplib.SMTP('smtp.gmail.com',587); s.starttls(); s.login('tigha66@gmail.com','YOUR_PASSWORD'); print('OK')"
```

### **Follow-Ups Not Running**
```bash
# Check cron logs
tail /home/admin/.openclaw/workspace/skills/business-lead-gen/logs/followup.log

# Check cron status
crontab -l
```

### **Need More Leads**
```bash
# Generate custom batch
python scripts/find_businesses_batch.py

# Or edit the script to add more cities/industries
```

---

## 📱 Daily Workflow

### **Morning (10 AM)**
1. Check email replies
2. Respond to interested businesses
3. Run campaign manager: `./campaign-manager.sh`

### **Weekly**
1. Review conversion rates
2. Launch new batches as needed
3. Follow up with warm leads

### **Monthly**
1. Analyze which cities/industries convert best
2. Adjust targeting accordingly
3. Scale up winning combinations

---

## 🎯 Best Practices

✅ **DO:**
- Send 20-50 emails/day max (avoid spam filters)
- Personalize each email
- Follow up 2-3 times
- Track responses in a spreadsheet
- Honor unsubscribe requests

❌ **DON'T:**
- Send 100+ emails/day from one account
- Use generic copy-paste emails
- Forget to follow up
- Ignore bounce/complaint rates
- Buy email lists (use generated leads only)

---

## 📞 Quick Reference

| Command | Purpose |
|---------|---------|
| `./campaign-manager.sh` | Interactive menu |
| `./scripts/setup-followups.sh` | Install cron jobs |
| `python scripts/find_businesses_batch.py` | Generate 900 new leads |
| `grep -c "sent" proposals-100.csv` | Check sent count |
| `crontab -l` | View scheduled tasks |

---

## 💡 Pro Tips

1. **Warm up your email account** - Start with 10/day, increase gradually
2. **A/B test subject lines** - Try different approaches
3. **Track everything** - Use a simple spreadsheet
4. **Follow up persistently** - Most sales happen on follow-up #3-5
5. **Scale winners** - Double down on cities/industries that convert

---

**You're all set!** 🚀 Run `./campaign-manager.sh` to get started.
