#!/usr/bin/env python3
"""
Never Miss A Call - SMS Sender

Simple script to send automated text responses to missed callers.
Can be triggered via Zapier webhook or called directly.
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path

# Try to import twilio, install if needed
try:
    from twilio.rest import Client
    from twilio.base.exceptions import TwilioRestException
except ImportError:
    print("Installing twilio...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "twilio"])
    from twilio.rest import Client
    from twilio.base.exceptions import TwilioRestException


class SMSSender:
    """Send automated SMS responses for missed calls."""
    
    def __init__(self, config_path: str = None):
        """Initialize with config or environment variables."""
        self.config = self.load_config(config_path)
        
        # Twilio credentials
        self.account_sid = os.environ.get('TWILIO_ACCOUNT_SID') or self.config.get('account_sid')
        self.auth_token = os.environ.get('TWILIO_AUTH_TOKEN') or self.config.get('auth_token')
        self.from_number = os.environ.get('TWILIO_PHONE_NUMBER') or self.config.get('from_number')
        
        # Business info
        self.business_name = self.config.get('business_name', 'Our Business')
        self.business_hours = self.config.get('business_hours', 'Mon-Fri 9am-5pm')
        
        # Initialize client
        if self.account_sid and self.auth_token:
            self.client = Client(self.account_sid, self.auth_token)
        else:
            self.client = None
    
    def load_config(self, config_path: str = None) -> dict:
        """Load configuration from file."""
        if config_path is None:
            config_path = Path(__file__).parent / 'config.json'
        
        config_file = Path(config_path)
        if config_file.exists():
            with open(config_file, 'r') as f:
                return json.load(f)
        return {}
    
    def load_template(self, template_name: str = 'default') -> str:
        """Load message template."""
        templates = {
            'default': "Thanks for calling {business}! We missed your call. Are you looking to schedule an appointment? Reply YES and we'll call you back within 10 minutes!",
            
            'dental': "Thanks for calling {business}! We missed your call. Looking to schedule an appointment? Reply YES and our team will call you back in 10 minutes! 🦷",
            
            'hvac': "Thanks for calling {business}! We missed your call. Need AC repair or heating service? Reply YES and we'll dispatch a technician to call you back within 10 minutes! ❄️",
            
            'plumbing': "Thanks for calling {business}! We missed your call. Have a leak or plumbing issue? Reply YES and our plumber will call you back within 10 minutes! 🔧",
            
            'spa': "Thanks for calling {business}! We missed your call. Looking to book a treatment? Reply YES and our team will call you back within 10 minutes! ✨",
            
            'general': "Thanks for calling {business}! We missed your call. How can we help you today? Reply with YES and we'll call you back ASAP!",
        }
        
        return templates.get(template_name, templates['default'])
    
    def format_message(self, template: str, caller_name: str = None) -> str:
        """Format message with business name and caller info."""
        message = template.format(
            business=self.business_name,
            caller=caller_name or 'there',
            date=datetime.now().strftime('%B %d'),
            time=datetime.now().strftime('%I:%M %p')
        )
        
        # Add compliance footer
        compliance = " Reply STOP to unsubscribe."
        if compliance not in message:
            message += compliance
        
        return message
    
    def send_sms(self, to_number: str, template: str = 'default', 
                 caller_name: str = None, log_file: str = None) -> dict:
        """
        Send SMS to caller.
        
        Args:
            to_number: Phone number to send to (E.164 format: +1234567890)
            template: Template name to use
            caller_name: Optional caller name
            log_file: Optional path to log file
        
        Returns:
            Dict with success status and message details
        """
        if not self.client:
            return {
                'success': False,
                'error': 'Twilio client not initialized. Check credentials.'
            }
        
        # Validate phone number
        if not to_number.startswith('+'):
            to_number = '+' + to_number.replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
        
        # Format message
        template_text = self.load_template(template)
        message = self.format_message(template_text, caller_name)
        
        try:
            # Send SMS
            result = self.client.messages.create(
                body=message,
                from_=self.from_number,
                to=to_number
            )
            
            response = {
                'success': True,
                'message_sid': result.sid,
                'to': to_number,
                'from': self.from_number,
                'status': result.status,
                'body': message[:50] + '...'
            }
            
            # Log if requested
            if log_file:
                self.log_message(log_file, response)
            
            return response
            
        except TwilioRestException as e:
            return {
                'success': False,
                'error': str(e),
                'code': e.code
            }
    
    def log_message(self, log_file: str, response: dict):
        """Log message to file."""
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().isoformat()
        with open(log_path, 'a') as f:
            f.write(f"[{timestamp}] {json.dumps(response)}\n")
    
    def test_connection(self) -> bool:
        """Test Twilio connection."""
        try:
            self.client.api.account.fetch()
            return True
        except Exception as e:
            print(f"Connection test failed: {e}")
            return False


def main():
    """CLI interface for sending SMS."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Never Miss A Call - SMS Sender')
    parser.add_argument('--to', required=True, help='Phone number to send to')
    parser.add_argument('--template', default='default', help='Template name')
    parser.add_argument('--name', help='Caller name')
    parser.add_argument('--config', help='Config file path')
    parser.add_argument('--log', help='Log file path')
    
    args = parser.parse_args()
    
    # Initialize sender
    sender = SMSSender(args.config)
    
    # Test connection
    print("🔄 Testing Twilio connection...")
    if not sender.test_connection():
        print("❌ Connection failed. Check credentials.")
        sys.exit(1)
    
    print("✅ Connected to Twilio!")
    
    # Send message
    print(f"📱 Sending SMS to {args.to}...")
    result = sender.send_sms(
        to_number=args.to,
        template=args.template,
        caller_name=args.name,
        log_file=args.log
    )
    
    if result['success']:
        print(f"✅ SMS sent successfully!")
        print(f"   SID: {result['message_sid']}")
        print(f"   Status: {result['status']}")
    else:
        print(f"❌ Failed: {result.get('error', 'Unknown error')}")
        sys.exit(1)


if __name__ == '__main__':
    main()