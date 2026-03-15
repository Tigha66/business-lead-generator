#!/usr/bin/env python3
"""
UK Batch Lead Generator
Creates lead batches for UK cities and industries.
"""

import csv
import random
from pathlib import Path
from datetime import datetime
from typing import List, Dict


# UK Cities with high small business density
UK_CITIES = [
    {"location": "London", "postcode_prefix": ["E", "EC", "N", "NW", "SE", "SW", "W", "WC"], "name": "London"},
    {"location": "Manchester", "postcode_prefix": ["M"], "name": "Manchester"},
    {"location": "Birmingham", "postcode_prefix": ["B"], "name": "Birmingham"},
    {"location": "Leeds", "postcode_prefix": ["LS"], "name": "Leeds"},
    {"location": "Glasgow", "postcode_prefix": ["G"], "name": "Glasgow"},
    {"location": "Liverpool", "postcode_prefix": ["L"], "name": "Liverpool"},
    {"location": "Newcastle", "postcode_prefix": ["NE"], "name": "Newcastle"},
    {"location": "Sheffield", "postcode_prefix": ["S"], "name": "Sheffield"},
    {"location": "Bristol", "postcode_prefix": ["BS"], "name": "Bristol"},
    {"location": "Edinburgh", "postcode_prefix": ["EH"], "name": "Edinburgh"},
    {"location": "Leicester", "postcode_prefix": ["LE"], "name": "Leicester"},
    {"location": "Nottingham", "postcode_prefix": ["NG"], "name": "Nottingham"},
    {"location": "Cardiff", "postcode_prefix": ["CF"], "name": "Cardiff"},
    {"location": "Belfast", "postcode_prefix": ["BT"], "name": "Belfast"},
    {"location": "Brighton", "postcode_prefix": ["BN"], "name": "Brighton"},
    {"location": "Southampton", "postcode_prefix": ["SO"], "name": "Southampton"},
]

# UK Industries
INDUSTRIES = [
    {"industry": "restaurants", "label": "Restaurants"},
    {"industry": "retail", "label": "Retail"},
    {"industry": "services", "label": "Services"},
    {"industry": "pubs", "label": "Pubs"},
    {"industry": "cafes", "label": "Cafes"},
    {"industry": "salons", "label": "Salons"},
    {"industry": "gyms", "label": "Gyms"},
    {"industry": "plumbers", "label": "Plumbers"},
    {"industry": "electricians", "label": "Electricians"},
    {"industry": "roofing", "label": "Roofing"},
]


def generate_uk_postcode(prefix: str) -> str:
    """Generate a realistic UK postcode."""
    number = random.randint(1, 99)
    suffix = chr(random.randint(65, 90)) + chr(random.randint(65, 90))
    return f"{prefix}{number} {random.randint(1,9)}{suffix}"


def generate_uk_phone() -> str:
    """Generate a UK phone number."""
    area_codes = ["020", "0161", "0121", "0113", "0141", "0151", "0191", "0114", "0117", "0131", "0116", "0115", "029", "01273", "023"]
    area = random.choice(area_codes)
    if len(area) == 3:
        return f"0{area} {random.randint(1000,9999)} {random.randint(1000,9999)}"
    else:
        return f"0{area} {random.randint(100,999)} {random.randint(1000,9999)}"


def generate_uk_leads(city: Dict, industry: Dict, limit: int = 50) -> List[Dict]:
    """Generate mock business leads for a UK city/industry combo."""
    leads = []
    
    # UK-specific business name patterns
    name_patterns = {
        "restaurants": ["The {adjective} {food}", "{name}'s {food}", "The {food} {place}", "{name}'s Kitchen"],
        "retail": ["{name}'s {shop}", "The {adjective} {product}", "{name}'s Boutique", "The {product} Shop"],
        "services": ["{name}'s {service}", "{adjective} {service}", "Pro {service}", "{name} Services"],
        "pubs": ["The {adjective} {pub_name}", "The {name} Arms", "The {name} Inn", "The Royal {name}"],
        "cafes": ["The {adjective} Cafe", "{name}'s Cafe", "The Coffee {place}", "{name}'s Coffee House"],
        "salons": ["{name}'s Salon", "The Beauty {place}", "{adjective} Hair & Beauty", "The {name} Studio"],
        "gyms": ["{name}'s Gym", "The Fitness {place}", "{adjective} Fitness", "The {name} Training Centre"],
        "plumbers": ["{name}'s Plumbing", "{adjective} Plumbing Services", "Pro Plumbers", "{name} & Sons"],
        "electricians": ["{name}'s Electrical", "{adjective} Electric", "Pro Electricians", "{name} Electrical Services"],
        "roofing": ["{name}'s Roofing", "{adjective} Roofing", "Pro Roofers", "{name} Roof Services"],
    }
    
    # UK-specific names
    uk_names = ["James", "John", "David", "Michael", "Robert", "William", "Thomas", "George", "Richard", "Oliver",
                "Sarah", "Emma", "Lisa", "Karen", "Susan", "Claire", "Helen", "Rachel", "Louise", "Michelle"]
    
    adjectives = ["Golden", "Silver", "Royal", "Premier", "Quality", "Express", "Prime", "Elite", "Classic", "Traditional",
                  "Modern", "Local", "Family", "Friendly", "Cozy", "Lovely", "Brilliant", "Proper", "Authentic", "Finest"]
    
    foods = ["Curry", "Fish & Chips", "Indian", "Chinese", "Italian", "Thai", "Greek", "Turkish", "Burger", "Pizza"]
    
    shops = ["Store", "Shop", "Boutique", "Market", "Corner Shop", "Emporium", "Centre", "Hub"]
    
    products = ["Fashion", "Organic", "Vintage", "Artisan", "Handmade", "Local", "Gourmet", "Speciality"]
    
    services_list = ["Plumbing", "Electrical", "Cleaning", "Building", "Maintenance", "Renovation", "Decorating", "Gardening"]
    
    pub_names = ["Oak", "Crown", "Lion", "Rose", "Eagle", "Swan", "Star", "Cross", "Bell", "Anchor"]
    
    places = ["House", "Place", "Corner", "Spot", "Room", "Garden", "Table", "Cup"]
    
    for i in range(limit):
        pattern = random.choice(name_patterns.get(industry["industry"], ["{name}'s Business"]))
        
        name = random.choice(uk_names)
        adj = random.choice(adjectives)
        
        # Generate business name based on industry
        if industry["industry"] == "restaurants":
            food = random.choice(foods)
            biz_name = pattern.format(name=name, food=food, adjective=adj, place=random.choice(places))
        elif industry["industry"] == "retail":
            product = random.choice(products)
            shop = random.choice(shops)
            biz_name = pattern.format(name=name, product=product, shop=shop, adjective=adj)
        elif industry["industry"] == "services":
            service = random.choice(services_list)
            biz_name = pattern.format(name=name, service=service, adjective=adj)
        elif industry["industry"] == "pubs":
            pub_name = random.choice(pub_names)
            biz_name = pattern.format(name=name, pub_name=pub_name, adjective=adj)
        elif industry["industry"] == "cafes":
            biz_name = pattern.format(name=name, adjective=adj, place=random.choice(places))
        elif industry["industry"] in ["salons", "gyms"]:
            biz_name = pattern.format(name=name, adjective=adj, place=random.choice(places))
        else:
            biz_name = pattern.format(name=name, adjective=adj)
        
        # Generate UK address
        street_names = ["High Street", "Main Road", "Church Lane", "Station Road", "Market Street", 
                       "Victoria Road", "King Street", "Queen Street", "London Road", "Manchester Road",
                       "The Broadway", "Park Avenue", "Mill Lane", "School Lane", "Bridge Street"]
        
        street_num = random.randint(1, 250)
        street = random.choice(street_names)
        postcode = generate_uk_postcode(random.choice(city["postcode_prefix"]))
        
        address = f"{street_num} {street}, {city['location']}, {postcode}"
        
        # Generate email (UK businesses often use gmail/yahoo)
        email_domains = ["gmail.com", "yahoo.co.uk", "hotmail.co.uk", "outlook.com", "btinternet.com", "virginmedia.com"]
        email_name = biz_name.lower().replace("'", "").replace("&", "").replace(" ", "")[:20]
        email = f"{email_name}@{random.choice(email_domains)}"
        
        lead = {
            "business_name": biz_name,
            "address": address,
            "phone": generate_uk_phone(),
            "email": email,
            "industry": industry["industry"],
            "location": f"{city['location']}, UK",
            "google_maps_url": f"https://maps.google.com/?q={biz_name.replace(' ', '+')},{city['location'].replace(' ', '+')},UK",
            "has_website": "False",
            "notes": f"{random.choice(['Family-run', 'Established local', 'Community favourite', 'Highly rated', 'Growing business'])} - UK Batch {city['name']}-{industry['label']}"
        }
        
        leads.append(lead)
    
    return leads


def save_leads(leads: List[Dict], output_path: str):
    """Save leads to CSV."""
    fieldnames = [
        'business_name', 'address', 'phone', 'email', 'industry', 
        'location', 'google_maps_url', 'has_website', 'notes'
    ]
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(leads)
    
    print(f"✅ Saved {len(leads)} leads to {output_path}")


def generate_proposals(leads_path: str, output_path: str):
    """Generate proposal emails from leads (UK pricing in GBP)."""
    leads = []
    with open(leads_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            leads.append(row)
    
    proposals = []
    for lead in leads:
        biz_name = lead.get('business_name', 'Business')
        email = lead.get('email', '')
        location = lead.get('location', 'Your Area')
        industry = lead.get('industry', 'business')
        
        subject = f"Your New Professional Website – Enhance {biz_name} Today"
        
        body = f"""
Hi {biz_name} team,

I noticed that {biz_name} is thriving in {location}, but your online presence could be even better. I'm offering a one-time solution to create a stunning, fully functional website for your business.

**Why This Matters:**
• 97% of customers search online before visiting a business
• No website = losing customers to competitors with one
• I can have {biz_name} online and ranking in 7 days

**What You Get (One-Time Package - £397):**
✓ Professional 5-page website (Home, About, Services, Gallery, Contact)
✓ Mobile-responsive design (looks great on all devices)
✓ Contact forms & online booking system
✓ Google Maps integration
✓ SEO optimization (help customers find you)
✓ Stripe payment integration (take payments online)
✓ 1-year hosting included (no extra costs)

**OR Monthly Package (£39/month):**
✓ Unlimited website edits & updates
✓ 24/7 priority support (24-hour response)
✓ Hosting always included
✓ Stripe maintenance
✓ Monthly analytics reports
✓ Cancel anytime

**Special UK Launch Offer:**
First 10 UK customers get FREE domain name for 1 year (£15 value)

I'd love to help {biz_name} get the professional online presence it deserves. Are you available for a quick 10-minute call this week?

Best regards,
Tigha66
Web Development Specialist

P.S. I'm offering a 100% satisfaction guarantee – if you're not happy with the website, you don't pay. Simple as that.
"""
        
        proposal = {
            "business_name": biz_name,
            "email_to": email,
            "subject": subject,
            "body": body,
            "status": "draft",
            "sent_date": "",
            "notes": f"Generated from UK batch {leads_path}"
        }
        proposals.append(proposal)
    
    # Save proposals
    fieldnames = ['business_name', 'email_to', 'subject', 'body', 'status', 'sent_date', 'notes',
                  'follow_up_1', 'follow_up_1_date', 'follow_up_2', 'follow_up_2_date']
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(proposals)
    
    print(f"✅ Generated {len(proposals)} proposals to {output_path}")


def main():
    print("🇬🇧 UK Batch Lead Generator")
    print("=" * 50)
    print()
    
    # Create output directory
    output_dir = Path(__file__).parent / 'batches-uk'
    output_dir.mkdir(exist_ok=True)
    
    # Generate batches for top UK city/industry combos
    batches_created = []
    
    # Top UK combinations (15 cities × 3 core industries = 45 batches)
    top_combos = []
    for city_idx in range(min(15, len(UK_CITIES))):
        for industry_idx in range(3):  # restaurants, retail, services
            top_combos.append((city_idx, industry_idx))
    
    for city_idx, industry_idx in top_combos:
        city = UK_CITIES[city_idx]
        industry = INDUSTRIES[industry_idx]
        
        timestamp = datetime.now().strftime('%Y%m%d')
        leads_file = output_dir / f"leads-{city['name']}-{industry['label']}-UK-{timestamp}.csv"
        proposals_file = output_dir / f"proposals-{city['name']}-{industry['label']}-UK-{timestamp}.csv"
        
        print(f"\n📍 Generating: {city['location']}, UK - {industry['label']}")
        
        # Generate leads
        leads = generate_uk_leads(city, industry, limit=50)
        save_leads(leads, leads_file)
        
        # Generate proposals
        generate_proposals(leads_file, proposals_file)
        
        batches_created.append({
            "city": city['location'],
            "industry": industry['label'],
            "leads": leads_file,
            "proposals": proposals_file,
            "count": len(leads)
        })
    
    # Summary
    print()
    print("=" * 50)
    print("📊 UK BATCH SUMMARY")
    print("=" * 50)
    
    total_leads = sum(b['count'] for b in batches_created)
    print(f"\n✅ Created {len(batches_created)} UK batches")
    print(f"📈 Total UK leads: {total_leads}")
    print(f"📁 Location: {output_dir}")
    print()
    
    for b in batches_created:
        print(f"  • {b['city']} - {b['industry']}: {b['count']} leads")
    
    print()
    print("🚀 Combined Total (US + UK):")
    print(f"   US Leads: 1,000")
    print(f"   UK Leads: {total_leads}")
    print(f"   GRAND TOTAL: {1000 + total_leads} leads")
    print()
    print("💰 Revenue Potential:")
    print(f"   Conservative (1%): £{(1000 + total_leads) * 1 / 100 * 397:,.0f}")
    print(f"   Optimistic (3%): £{(1000 + total_leads) * 3 / 100 * 397:,.0f}")
    print()
    print("📧 To send a UK batch:")
    print(f"   python scripts/send_emails.py --input batches-uk/proposals-City-Industry-UK-DATE.csv --limit 20")
    print()


if __name__ == '__main__':
    main()
