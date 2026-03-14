#!/usr/bin/env python3
"""
Generate personalized proposal emails for businesses without websites.
Reads leads from CSV and outputs personalized email drafts.
"""

import argparse
import csv
from pathlib import Path
from typing import List, Dict
from datetime import datetime


def load_leads(input_path: str) -> List[Dict]:
    """Load leads from CSV file."""
    leads = []
    with open(input_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            leads.append(row)
    return leads


def load_template(template_path: str) -> str:
    """Load email template from file."""
    path = Path(template_path)
    if not path.exists():
        # Use default template
        return get_default_template()
    return path.read_text(encoding='utf-8')


def get_default_template() -> str:
    """Return the default proposal email template."""
    return """Subject: Your New Professional Website – Enhance {{business_name}} Today

Hi {{owner_name}},

I noticed that {{business_name}} is thriving in {{location}}, but your online presence could be even better. I'm offering a one-time solution to create a stunning, fully functional website for your business.

Here's what you'll get:

✨ Professional 5-Page Website
• Fully responsive and mobile-friendly
• Contact forms and booking system
• Google Maps integration
• SEO optimization for better search rankings
• Stripe payment integration for seamless transactions
• 1-year hosting included

All for just £397 – One-Time Payment!

Perfect for businesses that want to own their website outright and have full control.

📅 Ongoing Support Option

If you prefer continuous support, I also offer a monthly package for only £39/month, which includes:
• Unlimited website edits
• 24/7 priority support (responses within 24 hours)
• Hosting always included
• Stripe maintenance and monthly analytics reports

Why Choose This Service?
✓ Fast and easy website creation
✓ Completely hands-off and automated
✓ Cancel anytime, no long-term commitment
✓ Professional design tailored to {{industry}}

Let's get started and elevate {{business_name}} with a professional website!

Best regards,
{{sender_name}}
{{sender_email}}
{{sender_phone}}

---
P.S. I specialize in helping {{industry}} businesses like yours establish a strong online presence. Recent clients have seen increased customer engagement and bookings after launching their new sites.

To unsubscribe from future emails, reply with "UNSUBSCRIBE".

{{sender_address}}
"""


def personalize_email(template: str, lead: Dict, sender_info: Dict) -> str:
    """Replace template variables with lead and sender information."""
    
    # Extract owner name from business name if not provided
    owner_name = lead.get('owner_name', '')
    if not owner_name:
        # Try to extract from business name (simple heuristic)
        business_name = lead.get('business_name', 'Your Business')
        owner_name = business_name.split()[0] if business_name else 'Business Owner'
    
    # Build replacement dictionary
    replacements = {
        '{{business_name}}': lead.get('business_name', 'Your Business'),
        '{{owner_name}}': owner_name,
        '{{location}}': lead.get('location', lead.get('address', 'your area')),
        '{{industry}}': lead.get('industry', 'your'),
        '{{sender_name}}': sender_info.get('name', 'Your Name'),
        '{{sender_email}}': sender_info.get('email', 'your@email.com'),
        '{{sender_phone}}': sender_info.get('phone', ''),
        '{{sender_address}}': sender_info.get('address', '')
    }
    
    # Replace all variables
    email = template
    for key, value in replacements.items():
        email = email.replace(key, value)
    
    return email


def save_proposals(proposals: List[Dict], output_path: str):
    """Save generated proposals to CSV."""
    if not proposals:
        print("⚠️  No proposals to save")
        return
    
    fieldnames = [
        'business_name', 'email_to', 'subject', 'body',
        'status', 'sent_date', 'notes'
    ]
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(proposals)
    
    print(f"\n✅ Saved {len(proposals)} proposals to: {output_path}")


def load_sender_info(config_path: str) -> Dict:
    """Load sender information from config file."""
    path = Path(config_path)
    if path.exists():
        import json
        return json.loads(path.read_text())
    
    # Return defaults
    return {
        'name': 'Your Name',
        'email': 'your@email.com',
        'phone': '',
        'address': ''
    }


def main():
    parser = argparse.ArgumentParser(description='Generate proposal emails for leads')
    parser.add_argument('--input', type=str, required=True, help='Input CSV with leads')
    parser.add_argument('--template', type=str, default='', help='Email template file')
    parser.add_argument('--output', type=str, default='proposals.csv', help='Output CSV file')
    parser.add_argument('--sender-config', type=str, default='~/.openclaw/sender_info.json', 
                       help='Sender info JSON file')
    parser.add_argument('--preview', action='store_true', help='Preview first email only')
    
    args = parser.parse_args()
    
    print("🦞 Proposal Generator")
    print("=" * 50)
    
    # Load leads
    print(f"\n📥 Loading leads from: {args.input}")
    leads = load_leads(args.input)
    print(f"   Found {len(leads)} leads")
    
    # Load template
    template_path = args.template if args.template else 'assets/email-templates/proposal.md'
    print(f"\n📝 Using template: {template_path}")
    template = load_template(template_path)
    
    # Load sender info
    sender_path = Path(args.sender_config).expanduser()
    sender_info = load_sender_info(str(sender_path))
    
    # Generate proposals
    proposals = []
    for i, lead in enumerate(leads):
        email_content = personalize_email(template, lead, sender_info)
        
        # Extract subject line
        lines = email_content.split('\n', 1)
        subject = lines[0].replace('Subject: ', '').strip() if lines[0].startswith('Subject:') else 'Website Proposal'
        body = lines[1] if len(lines) > 1 else email_content
        
        proposal = {
            'business_name': lead.get('business_name', ''),
            'email_to': lead.get('email', ''),
            'subject': subject,
            'body': body,
            'status': 'draft',
            'sent_date': '',
            'notes': ''
        }
        proposals.append(proposal)
        
        # Preview first email
        if args.preview and i == 0:
            print("\n" + "=" * 50)
            print("📧 PREVIEW:")
            print("=" * 50)
            print(f"To: {lead.get('email', 'N/A')}")
            print(f"Subject: {subject}")
            print("-" * 50)
            print(body[:1000] + "..." if len(body) > 1000 else body)
            print("=" * 50)
    
    # Save proposals
    if not args.preview:
        save_to_csv(proposals, args.output)
    else:
        print(f"\n⚠️  Preview mode - not saving. Remove --preview to save.")
    
    print(f"\n📊 Summary:")
    print(f"   Leads processed: {len(leads)}")
    print(f"   Proposals generated: {len(proposals)}")
    if not args.preview:
        print(f"   Output: {args.output}")


if __name__ == '__main__':
    main()
