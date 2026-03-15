#!/usr/bin/env python3
"""
ReviewPilot MVP - Automated Google Review Response System

Monitors Google Business Profile for new reviews, generates AI responses,
and sends approval emails to business owners.

MVP Features:
- Poll Google Business Profile API every 6 hours
- Generate AI responses using Claude
- Email drafts to owner for approval
- Log all activity to Google Sheets

Usage:
    python review_pilot.py --config config.json
"""

import argparse
import json
import smtplib
import time
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from typing import Dict, List, Optional
import csv


class ReviewPilot:
    def __init__(self, config_path: str):
        """Initialize ReviewPilot with config file."""
        self.config = self.load_config(config_path)
        self.log_file = Path(self.config.get('log_file', 'reviewpilot.log'))
        self.sheet_file = Path(self.config.get('sheet_file', 'reviews.csv'))
        
        # Initialize CSV if not exists
        if not self.sheet_file.exists():
            self.init_csv()
        
        print(f"✅ ReviewPilot initialized for: {self.config['business_name']}")
        print(f"📊 Log file: {self.log_file}")
        print(f"📋 Activity log: {self.sheet_file}")
    
    def load_config(self, config_path: str) -> Dict:
        """Load configuration from JSON file."""
        path = Path(config_path).expanduser()
        if not path.exists():
            print(f"❌ Config file not found: {path}")
            print("\nCreate config.json with:")
            print(json.dumps({
                "business_name": "Your Business Name",
                "google_account_id": "your-google-account-id",
                "claude_api_key": "your-claude-api-key",
                "smtp_host": "smtp.gmail.com",
                "smtp_port": 587,
                "smtp_user": "your-email@gmail.com",
                "smtp_password": "your-app-password",
                "owner_email": "owner@business.com",
                "poll_interval_hours": 6,
                "log_file": "reviewpilot.log",
                "sheet_file": "reviews.csv"
            }, indent=2))
            exit(1)
        
        with open(path, 'r') as f:
            return json.load(f)
    
    def init_csv(self):
        """Initialize CSV file with headers."""
        fieldnames = [
            'timestamp', 'reviewer_name', 'rating', 'review_text',
            'response_draft', 'email_sent', 'posted', 'notes'
        ]
        with open(self.sheet_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
    
    def log(self, message: str, level: str = "INFO"):
        """Log message to file and console."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] [{level}] {message}"
        
        # Console
        print(log_entry)
        
        # File
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry + '\n')
    
    def poll_reviews(self) -> List[Dict]:
        """
        Poll Google Business Profile API for new reviews.
        
        MVP: Simulated reviews for testing (replace with real API call)
        Production: Use googleapiclient.discovery
        """
        self.log("Polling for new reviews...")
        
        # TODO: Replace with real Google API call
        # from googleapiclient.discovery import build
        # service = build('mybusiness', 'v4', credentials=creds)
        # reviews = service.accounts().locations().reviews().list(...).execute()
        
        # MVP: Simulate finding a new review (remove in production)
        # This is for testing without API access
        simulated_review = {
            'name': 'John Smith',
            'rating': 5,
            'text': 'Great service! Very professional and friendly. Highly recommend.',
            'time': datetime.now().isoformat(),
            'review_id': 'test-123'
        }
        
        # Check if we already processed this review
        if self.is_review_processed(simulated_review['review_id']):
            self.log("No new reviews found")
            return []
        
        self.log(f"Found new review: {simulated_review['rating']} stars from {simulated_review['name']}")
        return [simulated_review]
    
    def is_review_processed(self, review_id: str) -> bool:
        """Check if review was already processed."""
        if not self.sheet_file.exists():
            return False
        
        with open(self.sheet_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if review_id in row.get('notes', ''):
                    return True
        return False
    
    def generate_response(self, review: Dict) -> str:
        """
        Generate AI response using Claude API.
        
        MVP: Simple template-based responses (replace with Claude API)
        Production: Use anthropic SDK
        """
        self.log("Generating AI response...")
        
        business_name = self.config['business_name']
        reviewer_name = review.get('name', 'Customer')
        rating = review.get('rating', 5)
        review_text = review.get('text', '')
        
        # MVP: Template-based responses (replace with Claude API)
        if rating >= 4:
            # Positive review response
            response = f"""Hi {reviewer_name},

Thank you so much for the wonderful {rating}-star review! We're thrilled you had a great experience with {business_name}.

{self.extract_positive_keywords(review_text)}

We look forward to serving you again soon!

Best regards,
The {business_name} Team"""
        else:
            # Negative review response (needs attention)
            response = f"""Hi {reviewer_name},

Thank you for your feedback. We're sorry to hear your experience didn't meet expectations.

We'd like to make this right. Please contact us directly at {self.config.get('contact_email', 'us')} so we can address your concerns.

Best regards,
The {business_name} Team"""
        
        # TODO: Replace with real Claude API call
        # import anthropic
        # client = anthropic.Client(api_key=config['claude_api_key'])
        # response = client.messages.create(
        #     model="claude-3-sonnet-20240229",
        #     max_tokens=150,
        #     messages=[{
        #         "role": "user",
        #         "content": f"Write a professional Google review response for {business_name}. Review: {review_text}. Rating: {rating}/5. Under 100 words."
        #     }]
        # )
        
        self.log(f"Generated response ({len(response)} chars)")
        return response
    
    def extract_positive_keywords(self, review_text: str) -> str:
        """Extract positive keywords from review for personalization."""
        keywords = ['professional', 'friendly', 'great', 'excellent', 'amazing', 'best', 'recommend']
        found = [word for word in keywords if word.lower() in review_text.lower()]
        
        if found:
            return f"We appreciate you mentioning our {' and '.join(found)} service!"
        return ""
    
    def send_approval_email(self, review: Dict, response_draft: str):
        """Send email to business owner with draft response for approval."""
        self.log(f"Sending approval email to {self.config['owner_email']}...")
        
        reviewer_name = review.get('name', 'Customer')
        rating = review.get('rating', 5)
        review_text = review.get('text', '')
        
        # Create email
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f"New Google Review - {rating} Stars from {reviewer_name}"
        msg['From'] = f"ReviewPilot <{self.config['smtp_user']}>"
        msg['To'] = self.config['owner_email']
        
        # Email body
        html = f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6;">
            <h2 style="color: #2c5282;">📬 New Google Review Received</h2>
            
            <div style="background: #f7fafc; padding: 20px; border-radius: 8px; margin: 20px 0;">
                <p><strong>Reviewer:</strong> {reviewer_name}</p>
                <p><strong>Rating:</strong> {'⭐' * rating}</p>
                <p><strong>Review:</strong></p>
                <p style="font-style: italic; color: #4a5568;">"{review_text}"</p>
            </div>
            
            <div style="background: #ebf8ff; padding: 20px; border-radius: 8px; margin: 20px 0;">
                <h3 style="color: #2c5282; margin-top: 0;">✍️ Drafted Response:</h3>
                <pre style="white-space: pre-wrap; font-family: Arial;">{response_draft}</pre>
            </div>
            
            <div style="margin: 30px 0;">
                <h3 style="color: #2c5282;">✅ Next Steps:</h3>
                <ol>
                    <li>Review the drafted response above</li>
                    <li>Edit if needed (optional)</li>
                    <li><a href="https://www.google.com/business/" style="background: #3182ce; color: white; padding: 10px 20px; text-decoration: none; border-radius: 4px;">Post Response on Google</a></li>
                </ol>
            </div>
            
            <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 30px 0;">
            <p style="color: #718096; font-size: 12px;">
                This email was sent by ReviewPilot - Automated Google Review Response System<br>
                To adjust settings or unsubscribe, edit your config.json file
            </p>
        </body>
        </html>
        """
        
        msg.attach(MIMEText(html, 'html'))
        
        # Send email
        try:
            server = smtplib.SMTP(self.config['smtp_host'], self.config['smtp_port'])
            server.starttls()
            server.login(self.config['smtp_user'], self.config['smtp_password'])
            server.send_message(msg)
            server.quit()
            
            self.log("✅ Approval email sent successfully")
            return True
            
        except Exception as e:
            self.log(f"❌ Failed to send email: {e}", level="ERROR")
            return False
    
    def log_review(self, review: Dict, response: str, email_sent: bool):
        """Log review activity to CSV."""
        fieldnames = [
            'timestamp', 'reviewer_name', 'rating', 'review_text',
            'response_draft', 'email_sent', 'posted', 'notes'
        ]
        
        row = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'reviewer_name': review.get('name', ''),
            'rating': review.get('rating', 0),
            'review_text': review.get('text', '')[:200],  # Truncate
            'response_draft': response[:200],  # Truncate
            'email_sent': 'Yes' if email_sent else 'No',
            'posted': 'Pending',
            'notes': f"Review ID: {review.get('review_id', 'N/A')}"
        }
        
        with open(self.sheet_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow(row)
        
        self.log(f"📋 Logged to {self.sheet_file}")
    
    def run_polling_cycle(self):
        """Run one complete polling cycle."""
        print("\n" + "="*60)
        print(f"🔄 ReviewPilot Polling Cycle - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print("="*60)
        
        # Step 1: Poll for new reviews
        reviews = self.poll_reviews()
        
        if not reviews:
            print("✅ No new reviews. Waiting for next cycle.")
            return
        
        # Step 2: Process each new review
        for review in reviews:
            print(f"\n📝 Processing review from {review.get('name', 'Unknown')}...")
            
            # Step 3: Generate response
            response = self.generate_response(review)
            print(f"✍️  Draft: {response[:100]}...")
            
            # Step 4: Send approval email
            email_sent = self.send_approval_email(review, response)
            
            # Step 5: Log activity
            self.log_review(review, response, email_sent)
            
            print(f"✅ Review processed successfully!")
        
        print("\n" + "="*60)
        print(f"✅ Cycle complete. Processed {len(reviews)} review(s)")
        print("="*60)
    
    def run_continuous(self):
        """Run continuous polling (every N hours)."""
        interval_hours = self.config.get('poll_interval_hours', 6)
        interval_seconds = interval_hours * 3600
        
        self.log(f"🚀 Starting continuous polling (every {interval_hours} hours)...")
        print(f"\n📍 Monitoring: {self.config['business_name']}")
        print(f"⏰ Poll interval: Every {interval_hours} hours")
        print(f"📧 Notifications to: {self.config['owner_email']}")
        print(f"\nPress Ctrl+C to stop\n")
        
        try:
            while True:
                self.run_polling_cycle()
                
                next_run = datetime.now().timestamp() + interval_seconds
                next_run_str = datetime.fromtimestamp(next_run).strftime('%H:%M:%S')
                print(f"\n💤 Sleeping until {next_run_str}...")
                time.sleep(interval_seconds)
                
        except KeyboardInterrupt:
            print("\n\n👋 Stopping ReviewPilot...")
            self.log("ReviewPilot stopped by user")


def main():
    parser = argparse.ArgumentParser(description='ReviewPilot - Automated Google Review Responses')
    parser.add_argument('--config', type=str, default='config.json',
                       help='Path to config.json file')
    parser.add_argument('--once', action='store_true',
                       help='Run one polling cycle and exit')
    parser.add_argument('--test', action='store_true',
                       help='Run test mode (simulated reviews)')
    
    args = parser.parse_args()
    
    # Initialize
    pilot = ReviewPilot(args.config)
    
    if args.once:
        # Run once and exit
        pilot.run_polling_cycle()
    else:
        # Run continuous
        pilot.run_continuous()


if __name__ == '__main__':
    main()
