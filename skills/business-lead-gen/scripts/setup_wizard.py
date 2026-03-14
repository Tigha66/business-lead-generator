#!/usr/bin/env python3
"""
Setup wizard for business-lead-gen skill.
Guides user through configuration step-by-step.
"""

import json
import os
from pathlib import Path
from typing import Dict


def get_user_input(prompt: str, default: str = "") -> str:
    """Get user input with optional default."""
    if default:
        full_prompt = f"{prompt} [{default}]: "
    else:
        full_prompt = f"{prompt}: "
    
    try:
        value = input(full_prompt).strip()
        return value if value else default
    except KeyboardInterrupt:
        print("\n\nSetup cancelled.")
        exit(0)


def setup_sender_info() -> Dict:
    """Guide user through sender info setup."""
    print("\n" + "=" * 60)
    print("📝 STEP 1: Your Contact Information")
    print("=" * 60)
    print("\nThis information will appear in your emails.")
    print("IMPORTANT: Your physical address is REQUIRED by CAN-SPAM law.\n")
    
    sender_info = {
        "name": get_user_input("Your full name"),
        "email": get_user_input("Your email address"),
        "phone": get_user_input("Your phone number"),
        "address": get_user_input("Your physical address (street, city, state, zip, country)"),
        "company": get_user_input("Company name (optional)", "Your Web Services"),
        "website": get_user_input("Your website (optional)", "")
    }
    
    print(f"\n✅ Sender info saved!")
    return sender_info


def setup_smtp_config() -> Dict:
    """Guide user through SMTP setup."""
    print("\n" + "=" * 60)
    print("📧 STEP 2: Email Configuration (SMTP)")
    print("=" * 60)
    print("\nThis is how emails will be sent.")
    print("\n📌 GMAIL USERS:")
    print("   1. Go to: https://myaccount.google.com/apppasswords")
    print("   2. Create an app password for 'Mail'")
    print("   3. Use that password below (NOT your regular password)\n")
    
    print("Choose your email provider:")
    print("1. Gmail")
    print("2. Outlook/Hotmail")
    print("3. Custom SMTP")
    
    choice = get_user_input("Select [1]", "1")
    
    if choice == "1":
        host = "smtp.gmail.com"
        port = "587"
    elif choice == "2":
        host = "smtp-mail.outlook.com"
        port = "587"
    else:
        host = get_user_input("SMTP host", "smtp.example.com")
        port = get_user_input("SMTP port", "587")
    
    smtp_config = {
        "host": host,
        "port": int(port),
        "username": get_user_input("Your email address"),
        "password": get_user_input("Email password or app password"),
        "from_name": get_user_input("Sender name (how your name appears)", "Your Name")
    }
    
    print(f"\n✅ SMTP config saved!")
    return smtp_config


def setup_pricing() -> Dict:
    """Configure pricing packages."""
    print("\n" + "=" * 60)
    print("💰 STEP 3: Pricing Configuration")
    print("=" * 60)
    print("\nDefault pricing is in GBP (£). Change if needed.\n")
    
    pricing = {
        "one_time_amount": get_user_input("One-time package price", "397"),
        "one_time_currency": get_user_input("Currency symbol", "£"),
        "monthly_amount": get_user_input("Monthly package price", "39"),
        "monthly_currency": get_user_input("Currency symbol", "£")
    }
    
    print(f"\n✅ Pricing configured!")
    return pricing


def save_config(sender_info: Dict, smtp_config: Dict, pricing: Dict):
    """Save all configurations to files."""
    openclaw_dir = Path.home() / '.openclaw'
    openclaw_dir.mkdir(exist_ok=True)
    
    # Save sender info
    sender_path = openclaw_dir / 'sender_info.json'
    with open(sender_path, 'w') as f:
        json.dump(sender_info, f, indent=2)
    print(f"   ✓ Saved: {sender_path}")
    
    # Save SMTP config
    smtp_path = openclaw_dir / 'smtp.json'
    with open(smtp_path, 'w') as f:
        json.dump(smtp_config, f, indent=2)
    print(f"   ✓ Saved: {smtp_path}")
    
    # Save pricing
    pricing_path = openclaw_dir / 'pricing.json'
    with open(pricing_path, 'w') as f:
        json.dump(pricing, f, indent=2)
    print(f"   ✓ Saved: {pricing_path}")


def show_next_steps():
    """Display next steps for the user."""
    print("\n" + "=" * 60)
    print("🎉 SETUP COMPLETE!")
    print("=" * 60)
    print("\n✅ You're ready to start finding businesses and sending proposals!\n")
    
    print("📋 NEXT STEPS:")
    print("\n1. Find Businesses (Manual Method):")
    print("   cd ~/.openclaw/workspace/skills/business-lead-gen")
    print("   python scripts/find_businesses.py --location 'Your City' --industry 'restaurants' --method manual")
    print("\n2. Generate Proposals:")
    print("   python scripts/generate_proposals.py --input leads.csv --preview")
    print("\n3. Send Test Email:")
    print("   python scripts/send_emails.py --input proposals.csv --dry-run")
    print("\n4. Send Real Campaign:")
    print("   python scripts/send_emails.py --input proposals.csv")
    
    print("\n⚠️  REMEMBER:")
    print("   • Start with 10-20 emails (test batch)")
    print("   • Include your physical address in every email (legal requirement)")
    print("   • Honor unsubscribe requests immediately")
    print("   • Rate limit: max 50 emails/hour")
    
    print("\n📖 Full documentation: skills/business-lead-gen/SKILL.md")
    print("\n" + "=" * 60)


def main():
    print("\n" + "=" * 60)
    print("🦞 Business Lead Generator - Setup Wizard")
    print("=" * 60)
    print("\nThis will guide you through the initial setup.")
    print("Press Ctrl+C at any time to cancel.\n")
    
    input("Press Enter to start...")
    
    # Run setup steps
    sender_info = setup_sender_info()
    smtp_config = setup_smtp_config()
    pricing = setup_pricing()
    
    # Save configurations
    print("\n" + "=" * 60)
    print("💾 Saving configurations...")
    print("=" * 60)
    save_config(sender_info, smtp_config, pricing)
    
    # Show next steps
    show_next_steps()


if __name__ == '__main__':
    main()
