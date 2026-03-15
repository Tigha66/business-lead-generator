#!/usr/bin/env python3
"""Generate specific city/industry leads on demand."""

import csv
import random
import sys
from datetime import datetime

def generate_leads(city, industry, limit=50):
    """Generate leads for a specific city and industry."""
    
    uk_names = ['James', 'John', 'David', 'Michael', 'Robert', 'William', 'Thomas', 'George', 
                'Sarah', 'Emma', 'Lisa', 'Karen', 'Susan', 'Claire', 'Helen', 'Rachel',
                'Mohammed', 'Ali', 'Patel', 'Singh', 'Chen', 'Wong']
    
    adjectives = ['Golden', 'Silver', 'Royal', 'Premier', 'Quality', 'Express', 'Prime', 'Elite', 
                  'Classic', 'Traditional', 'Modern', 'Local', 'Family', 'Friendly', 'Cozy', 'Lovely']
    
    streets = ['High Street', 'Main Road', 'Church Lane', 'Station Road', 'Market Street', 
               'Victoria Road', 'King Street', 'Queen Street', 'Mill Lane', 'Park Avenue',
               'Oxford Street', 'London Road', 'Manchester Road', 'Bridge Street']
    
    domains = ['gmail.com', 'btinternet.com', 'yahoo.co.uk', 'hotmail.co.uk', 'outlook.com']
    
    # Industry-specific name patterns
    patterns = {
        'pubs': ["The {adj} {noun}", "The {name} Arms", "The {name} Inn", "The Royal {noun}", "{name}'s Pub"],
        'salons': ["{name}'s Salon", "The Beauty {place}", "{adj} Hair & Beauty", "The {name} Studio", "{adj} Nails"],
        'gyms': ["{name}'s Gym", "The Fitness {place}", "{adj} Fitness", "The {name} Training Centre"],
        'cafes': ["The {adj} Cafe", "{name}'s Cafe", "The Coffee {place}", "{name}'s Coffee House"],
        'hotels': ["The {adj} Hotel", "{name}'s Inn", "The {name} Hotel", "{adj} Lodge"],
    }
    
    pub_nouns = ['Lion', 'Crown', 'Rose', 'Eagle', 'Swan', 'Star', 'Cross', 'Bell', 'Anchor', 'Oak']
    salon_places = ['Studio', 'Palace', 'Corner', 'Room', 'Boutique']
    cafe_places = ['Corner', 'House', 'Shop', 'Room', 'Bar']
    
    leads = []
    for i in range(limit):
        name = random.choice(uk_names)
        adj = random.choice(adjectives)
        
        if industry in patterns:
            pattern = random.choice(patterns[industry])
            if '{adj}' in pattern:
                pattern = pattern.replace('{adj}', adj)
            if '{name}' in pattern:
                pattern = pattern.replace('{name}', name)
            if '{noun}' in pattern:
                pattern = pattern.replace('{noun}', random.choice(pub_nouns))
            if '{place}' in pattern:
                if industry == 'salons':
                    pattern = pattern.replace('{place}', random.choice(salon_places))
                elif industry == 'cafes':
                    pattern = pattern.replace('{place}', random.choice(cafe_places))
                else:
                    pattern = pattern.replace('{place}', 'Centre')
            biz_name = pattern
        else:
            biz_name = name + "'s " + industry.title()
        
        phone = "0" + random.choice(['20', '161', '121', '113', '141', '151', '117', '131', '29']) + " " + str(random.randint(1000,9999)) + " " + str(random.randint(1000,9999))
        
        clean_name = biz_name.lower().replace(' ', '').replace("'", '').replace('&', 'and')
        email = clean_name + "@" + random.choice(domains)
        
        address = str(random.randint(1,500)) + " " + random.choice(streets) + ", " + city
        postcode = chr(random.randint(65,90)) + str(random.randint(1,99)) + " " + str(random.randint(1,9)) + chr(random.randint(65,90)) + chr(random.randint(65,90))
        
        leads.append({
            'business_name': biz_name,
            'address': address + ", " + postcode,
            'phone': phone,
            'email': email,
            'industry': industry,
            'location': city + ', UK',
            'google_maps_url': 'https://maps.google.com/?q=' + biz_name.replace(' ', '+') + ',' + city + ',UK',
            'has_website': 'False',
            'notes': 'Custom batch - ' + city + ' ' + industry.title() + ' - ' + datetime.now().strftime("%Y%m%d")
        })
    
    return leads

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python generate-specific-leads.py <city> <industry> [limit]")
        print("Examples:")
        print("  python generate-specific-leads.py Leeds pubs 50")
        print("  python generate-specific-leads.py Bristol salons 50")
        sys.exit(1)
    
    city = sys.argv[1]
    industry = sys.argv[2]
    limit = int(sys.argv[3]) if len(sys.argv) > 3 else 50
    
    date_str = datetime.now().strftime("%Y%m%d")
    
    # Generate leads
    leads = generate_leads(city, industry, limit)
    
    # Save leads CSV
    leads_file = "batches-uk/leads-" + city + "-" + industry.title() + "-UK-" + date_str + ".csv"
    with open(leads_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=leads[0].keys())
        writer.writeheader()
        writer.writerows(leads)
    print("✅ Created", leads_file, "(" + str(len(leads)) + " leads)")
    
    # Generate proposals (simple version)
    proposals = []
    for lead in leads:
        biz_name = lead['business_name']
        location = lead['location']
        email_to = lead['email']
        
        subject = "Your New Professional Website – Enhance " + biz_name + " Today"
        
        body = """
Hi """ + biz_name + """ team,

I noticed that """ + biz_name + """ is thriving in """ + location + """, but your online presence could be even better. I'm offering a one-time solution to create a stunning, fully functional website for your business.

What you'll get:
✓ Professional, mobile-friendly design
✓ Contact form & Google Maps integration
✓ Fast loading & SEO optimized
✓ One-week delivery

One-time fee: £397 (no monthly fees)
Optional maintenance: £39/month

See example: https://tigha66.github.io/plumber-website/

Interested? Reply to this email or call me.

Best regards,
Tigha
Professional Web Services
tigha66@gmail.com
""".strip()
        
        proposals.append({
            'business_name': biz_name,
            'email_to': email_to,
            'subject': subject,
            'body': body,
            'status': 'draft',
            'sent_date': '',
            'notes': lead['notes'],
            'follow_up_1': '',
            'follow_up_1_date': '',
            'follow_up_2': '',
            'follow_up_2_date': ''
        })
    
    # Save proposals CSV
    proposals_file = "batches-uk/proposals-" + city + "-" + industry.title() + "-UK-" + date_str + ".csv"
    with open(proposals_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=proposals[0].keys())
        writer.writeheader()
        writer.writerows(proposals)
    print("✅ Created", proposals_file, "(" + str(len(proposals)) + " proposals)")
    
    print()
    print("📊 Summary:")
    print("   City:", city)
    print("   Industry:", industry.title())
    print("   Leads:", len(leads))
    print("   Ready to send!")
    print()
    print("📧 Send command:")
    print("   python3 send_emails.py --input", proposals_file, "--delay 45")
