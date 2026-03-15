#!/usr/bin/env python3
"""
Automated Follow-Up System
Schedules and sends follow-up emails based on initial send dates.
"""

import csv
import json
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from send_emails import load_smtp_config, send_email


def load_proposals(input_path: str) -> list:
    """Load proposals from CSV."""
    proposals = []
    with open(input_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            proposals.append(row)
    return proposals


def load_template(template_name: str) -> str:
    """Load email template."""
    template_path = Path(__file__).parent / 'assets' / 'email-templates' / f'{template_name}.md'
    if not template_path.exists():
        print(f"❌ Template not found: {template_path}")
        return ""
    
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()


def personalize_template(template: str, business_name: str) -> str:
    """Replace template variables."""
    return template.replace('{{business_name}}', business_name)


def get_subject_from_template(template: str) -> str:
    """Extract subject line from template."""
    for line in template.split('\n'):
        if line.startswith('**Subject:**'):
            return line.replace('**Subject:**', '').strip()
    return "Following up"


def send_follow_ups(input_path: str, follow_up_number: int, dry_run: bool = False):
    """Send follow-up emails to businesses that haven't replied."""
    
    # Calculate target date based on follow-up number
    if follow_up_number == 1:
        days_ago = 3  # Send 3 days after initial email
        template_name = 'follow-up-1'
    elif follow_up_number == 2:
        days_ago = 10  # Send 10 days after initial email (7 days after follow-up 1)
        template_name = 'follow-up-2'
    else:
        print(f"❌ Invalid follow-up number: {follow_up_number}")
        return
    
    target_date = datetime.now() - timedelta(days=days_ago)
    
    print(f"🔔 Follow-Up #{follow_up_number} System")
    print("=" * 50)
    print(f"Looking for emails sent around: {target_date.strftime('%Y-%m-%d')}")
    print(f"Template: {template_name}")
    print()
    
    # Load proposals
    proposals = load_proposals(input_path)
    print(f"📥 Loaded {len(proposals)} proposals")
    
    # Filter: sent emails that need this follow-up
    candidates = []
    for p in proposals:
        if p.get('status') != 'sent':
            continue
        
        sent_date_str = p.get('sent_date', '')
        if not sent_date_str:
            continue
        
        try:
            sent_date = datetime.strptime(sent_date_str.split()[0], '%Y-%m-%d')
            days_since = (datetime.now() - sent_date).days
            
            # Check if this follow-up is due
            if follow_up_number == 1 and 2 <= days_since <= 4:
                if not p.get('follow_up_1') == 'sent':
                    candidates.append(p)
            elif follow_up_number == 2 and 9 <= days_since <= 12:
                if not p.get('follow_up_2') == 'sent' and p.get('follow_up_1') == 'sent':
                    candidates.append(p)
        except:
            continue
    
    print(f"📋 Found {len(candidates)} candidates for follow-up #{follow_up_number}")
    
    if not candidates:
        print("\n✅ No follow-ups needed right now")
        return
    
    # Load SMTP config
    smtp_config = load_smtp_config('~/.openclaw/smtp.json')
    if not smtp_config:
        print("\n❌ SMTP not configured")
        return
    
    # Load template
    template = load_template(template_name)
    if not template:
        return
    
    # Send follow-ups
    print(f"\n📧 Sending follow-up emails...")
    if dry_run:
        print("(DRY RUN - no emails will be sent)")
    print()
    
    sent_count = 0
    for i, p in enumerate(candidates, 1):
        business_name = p.get('business_name', 'Business')
        email_to = p.get('email_to', '')
        
        if not email_to:
            print(f"⚠️  Skipping {business_name} - no email")
            continue
        
        # Personalize template
        body = personalize_template(template, business_name)
        subject = get_subject_from_template(template)
        
        print(f"[{i}/{len(candidates)}] {business_name} -> {email_to}")
        
        if not dry_run:
            success = send_email(smtp_config, email_to, subject, body)
            if success:
                p[f'follow_up_{follow_up_number}'] = 'sent'
                p[f'follow_up_{follow_up_number}_date'] = datetime.now().strftime('%Y-%m-%d %H:%M')
                sent_count += 1
                print(f"   ✅ Sent")
            else:
                print(f"   ❌ Failed")
        else:
            print(f"   (would send)")
        
        # Small delay
        import time
        time.sleep(2)
    
    print()
    print("=" * 50)
    if dry_run:
        print(f"DRY RUN: Would send {len(candidates)} follow-up emails")
    else:
        print(f"✅ Sent {sent_count}/{len(candidates)} follow-up emails")
    
    # Save updated proposals
    if not dry_run:
        save_proposals(proposals, input_path)
        print(f"💾 Updated {input_path}")


def save_proposals(proposals: list, output_path: str):
    """Save proposals to CSV."""
    fieldnames = [
        'business_name', 'email_to', 'subject', 'body',
        'status', 'sent_date', 'notes',
        'follow_up_1', 'follow_up_1_date',
        'follow_up_2', 'follow_up_2_date'
    ]
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(proposals)


def main():
    parser = argparse.ArgumentParser(description='Automated follow-up system')
    parser.add_argument('--input', type=str, default='proposals-100.csv',
                       help='Input CSV with proposals')
    parser.add_argument('--follow-up', type=int, choices=[1, 2], required=True,
                       help='Which follow-up to send (1 or 2)')
    parser.add_argument('--dry-run', action='store_true',
                       help='Preview without sending')
    
    args = parser.parse_args()
    
    send_follow_ups(args.input, args.follow_up, args.dry_run)


if __name__ == '__main__':
    main()
