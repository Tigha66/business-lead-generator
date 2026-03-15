#!/usr/bin/env python3
"""
Cold Email Sender for Never Miss A Call

Sends personalized outreach emails to local businesses.
"""

import csv
import smtplib
import json
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from datetime import datetime
import time

# Load SMTP config
smtp_config = {
    "host": "smtp.gmail.com",
    "port": 587,
    "username": "tigha66@gmail.com",
    "password": "wlbq bcso brtq kcgd",
    "from_name": "Never Miss A Call"
}

# Email config
FROM_EMAIL = "tigha66@gmail.com"
FROM_NAME = "Never Miss A Call Team"

# Email templates
EMAIL_SUBJECT_DENTAL = "Quick question about {business} missed calls"
EMAIL_SUBJECT_HVAC = "Quick question about {business} lost leads"

EMAIL_BODY_DENTAL = """Hi {first_name},

I noticed {business} might be missing calls during busy hours.

Here's the thing: most dental practices miss 20-40% of incoming calls, and 80% of patients don't leave voicemails. At your average ticket of $150+, that could be $3,000+ in lost revenue every month.

We built "Never Miss A Call" - an automated system that texts every caller back within 60 seconds, capturing their interest while it's hot. We've seen dental practices book 8-15 extra appointments/month from calls they would've missed.

Would it make sense to show you how it works? It's free, takes 10 minutes, and there's no obligation.

Best,
{from_name}

P.S. - If you're not the right person to talk to about operations, who should I connect with?
"""

EMAIL_BODY_HVAC = """Hi {first_name},

I noticed {business} might be missing service calls.

Here's the thing: most HVAC companies miss 20-40% of incoming calls, and 80% of callers don't leave voicemails. At your average service ticket of $200+, that could be $4,000+ in lost revenue every month.

We built "Never Miss A Call" - an automated system that texts every caller back within 60 seconds, capturing their interest while it's hot. We've seen HVAC companies book 10-20 extra jobs/month from calls they would've missed.

Would it make sense to show you how it works? It's free, takes 10 minutes, and there's no obligation.

Best,
{from_name}

P.S. - If you're not the right person to talk to about operations, who should I connect with?
"""


def load_leads(csv_path: str):
    """Load leads from CSV file."""
    leads = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            leads.append(row)
    return leads


def send_email(to_email: str, to_name: str, subject: str, body: str, smtp_config: dict):
    """Send email via SMTP."""
    try:
        # Create message
        msg = MIMEMultipart('alternative')
        msg['From'] = f"{FROM_NAME} <{FROM_EMAIL}>"
        msg['To'] = f"{to_name} <{to_email}>"
        msg['Subject'] = subject
        
        # Attach body
        msg.attach(MIMEText(body, 'plain'))
        
        # Send
        server = smtplib.SMTP(smtp_config['host'], smtp_config['port'])
        server.starttls()
        server.login(smtp_config['username'], smtp_config['password'].replace(' ', ''))
        server.sendmail(FROM_EMAIL, to_email, msg.as_string())
        server.quit()
        
        return True, "Sent"
    except Exception as e:
        return False, str(e)


def main():
    """Send cold emails to leads."""
    # Load leads
    csv_path = Path(__file__).parent / 'outreach-list.csv'
    leads = load_leads(csv_path)
    
    print(f"📧 Loaded {len(leads)} leads")
    print(f"📧 Sending emails from: {FROM_EMAIL}")
    print(f"📧 Using SMTP: {smtp_config['host']}")
    print()
    
    # Send emails
    sent = 0
    failed = 0
    rate_limit = 60  # 1 email per minute to avoid spam
    
    for i, lead in enumerate(leads):
        # Skip if no email
        if not lead.get('email') or lead['email'] == 'N/A':
            print(f"⏭️  Skipping {lead.get('name', 'Unknown')} - no email")
            continue
        
        # Get details
        name = lead['name']
        industry = lead.get('industry', 'Service')
        city = lead.get('city', '')
        
        # Get first name
        first_name = name.split()[0] if name else 'there'
        
        # Select template
        if 'dental' in industry.lower():
            subject = EMAIL_SUBJECT_DENTAL.format(business=name)
            body = EMAIL_BODY_DENTAL.format(
                first_name=first_name,
                business=name,
                from_name=FROM_NAME
            )
        else:
            subject = EMAIL_SUBJECT_HVAC.format(business=name)
            body = EMAIL_BODY_HVAC.format(
                first_name=first_name,
                business=name,
                from_name=FROM_NAME
            )
        
        to_email = lead['email'].strip()
        
        # Send email
        print(f"📧 Sending to {name} ({to_email})...")
        success, result = send_email(to_email, name, subject, body, smtp_config)
        
        if success:
            print(f"   ✅ Sent!")
            sent += 1
        else:
            print(f"   ❌ Failed: {result}")
            failed += 1
        
        # Rate limiting
        if i < len(leads) - 1:
            print(f"   ⏳ Waiting {rate_limit}s (rate limit)...")
            time.sleep(rate_limit)
    
    # Summary
    print()
    print("=" * 50)
    print(f"📊 SUMMARY")
    print(f"   ✅ Sent: {sent}")
    print(f"   ❌ Failed: {failed}")
    print(f"   📧 Total: {len(leads)}")
    print("=" * 50)


if __name__ == '__main__':
    main()