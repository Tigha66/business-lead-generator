#!/usr/bin/env python3
"""
Send proposal emails to businesses.
Reads proposals from CSV and sends via SMTP.
"""

import argparse
import csv
import smtplib
import time
import random
import json
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict, Optional
from datetime import datetime


def load_proposals(input_path: str) -> List[Dict]:
    """Load proposals from CSV file."""
    proposals = []
    with open(input_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            proposals.append(row)
    return proposals


def load_smtp_config(config_path: str) -> Dict:
    """Load SMTP configuration from JSON file."""
    path = Path(config_path).expanduser()
    if not path.exists():
        print(f"❌ Config file not found: {path}")
        print("\nCreate ~/.openclaw/smtp.json with:")
        print(json.dumps({
            "host": "smtp.gmail.com",
            "port": 587,
            "username": "your@email.com",
            "password": "your-app-password",
            "from_name": "Your Name"
        }, indent=2))
        return {}
    
    with open(path, 'r') as f:
        return json.load(f)


def send_email(smtp_config: Dict, to_email: str, subject: str, body: str) -> bool:
    """Send a single email via SMTP."""
    try:
        # Create message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = f"{smtp_config.get('from_name', 'Sender')} <{smtp_config.get('username', '')}>"
        msg['To'] = to_email
        
        # Attach body as plain text
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # Connect and send
        server = smtplib.SMTP(smtp_config['host'], smtp_config['port'])
        server.starttls()
        server.login(smtp_config['username'], smtp_config['password'])
        server.send_message(msg)
        server.quit()
        
        return True
        
    except Exception as e:
        print(f"❌ Error sending to {to_email}: {e}")
        return False


def update_proposals_csv(proposals: List[Dict], output_path: str):
    """Update proposals CSV with send status."""
    fieldnames = [
        'business_name', 'email_to', 'subject', 'body',
        'status', 'sent_date', 'notes'
    ]
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(proposals)


def main():
    parser = argparse.ArgumentParser(description='Send proposal emails')
    parser.add_argument('--input', type=str, required=True, help='Input CSV with proposals')
    parser.add_argument('--smtp-config', type=str, default='~/.openclaw/smtp.json',
                       help='SMTP config JSON file')
    parser.add_argument('--rate-limit', type=int, default=50, 
                       help='Max emails per hour')
    parser.add_argument('--delay', type=int, default=60,
                       help='Seconds between emails')
    parser.add_argument('--dry-run', action='store_true',
                       help='Preview without sending')
    parser.add_argument('--start-index', type=int, default=0,
                       help='Start from this index')
    
    args = parser.parse_args()
    
    print("🦞 Email Sender")
    print("=" * 50)
    
    # Load proposals
    print(f"\n📥 Loading proposals from: {args.input}")
    proposals = load_proposals(args.input)
    print(f"   Found {len(proposals)} proposals")
    
    # Filter to drafts only
    draft_proposals = [p for p in proposals if p.get('status') == 'draft']
    print(f"   Drafts to send: {len(draft_proposals)}")
    
    if not draft_proposals:
        print("\n⚠️  No draft proposals to send")
        return
    
    # Load SMTP config
    smtp_config = load_smtp_config(args.smtp_config)
    if not smtp_config:
        print("\n❌ Cannot proceed without SMTP configuration")
        return
    
    # Dry run preview
    if args.dry_run:
        print("\n🔍 DRY RUN - No emails will be sent")
        print("=" * 50)
        for i, proposal in enumerate(draft_proposals[:3]):
            print(f"\n{i+1}. To: {proposal.get('email_to', 'N/A')}")
            print(f"   Subject: {proposal.get('subject', 'N/A')}")
            body = proposal.get('body', '')
            print(f"   Preview: {body[:200]}...")
        print("\n" + "=" * 50)
        print(f"Total emails to send: {len(draft_proposals)}")
        print(f"Estimated time: {len(draft_proposals) * args.delay / 60:.1f} minutes")
        print("\nRemove --dry-run to actually send emails")
        return
    
    # Send emails
    print(f"\n📧 Starting email campaign...")
    print(f"   Rate limit: {args.rate_limit}/hour")
    print(f"   Delay: {args.delay}s between emails")
    
    sent_count = 0
    failed_count = 0
    start_time = datetime.now()
    
    for i, proposal in enumerate(draft_proposals[args.start_index:], start=args.start_index):
        to_email = proposal.get('email_to', '')
        
        # Skip if no email
        if not to_email:
            print(f"\n⚠️  [{i+1}] Skipping {proposal.get('business_name', 'Unknown')} - No email address")
            proposal['status'] = 'skipped'
            proposal['notes'] = 'No email address'
            continue
        
        # Send email
        print(f"\n📧 [{i+1}/{len(draft_proposals)}] Sending to {to_email}...")
        
        success = send_email(
            smtp_config,
            to_email,
            proposal.get('subject', ''),
            proposal.get('body', '')
        )
        
        if success:
            sent_count += 1
            proposal['status'] = 'sent'
            proposal['sent_date'] = datetime.now().isoformat()
            print(f"   ✓ Sent successfully")
        else:
            failed_count += 1
            proposal['status'] = 'failed'
            proposal['notes'] = 'Send failed'
            print(f"   ❌ Failed to send")
        
        # Update CSV after each email (for recovery)
        update_proposals_csv(proposals, args.input)
        
        # Rate limiting delay
        if i < len(draft_proposals) - 1:
            delay = args.delay + random.uniform(-5, 5)  # Add some randomness
            print(f"   ⏱️  Waiting {delay:.1f}s...")
            time.sleep(delay)
    
    # Summary
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    print("\n" + "=" * 50)
    print("📊 Campaign Summary")
    print("=" * 50)
    print(f"   Started: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"   Finished: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"   Duration: {duration/60:.1f} minutes")
    print(f"   Sent: {sent_count}")
    print(f"   Failed: {failed_count}")
    print(f"   Skipped: {len(draft_proposals) - sent_count - failed_count}")
    print(f"\n   Results saved to: {args.input}")


if __name__ == '__main__':
    main()
