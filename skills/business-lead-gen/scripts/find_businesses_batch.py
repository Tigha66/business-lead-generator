#!/usr/bin/env python3
"""
Batch Lead Generator
Creates lead batches for multiple cities and industries.
"""

import csv
import json
import random
from pathlib import Path
from datetime import datetime
from typing import List, Dict


# Target cities with high small business density
CITIES = [
    {"location": "Los Angeles, CA", "name": "LA"},
    {"location": "Chicago, IL", "name": "Chicago"},
    {"location": "Houston, TX", "name": "Houston"},
    {"location": "Phoenix, AZ", "name": "Phoenix"},
    {"location": "Philadelphia, PA", "name": "Philly"},
    {"location": "San Antonio, TX", "name": "SanAntonio"},
    {"location": "San Diego, CA", "name": "SanDiego"},
    {"location": "Dallas, TX", "name": "Dallas"},
    {"location": "San Jose, CA", "name": "SanJose"},
    {"location": "Austin, TX", "name": "Austin"},
    {"location": "Jacksonville, FL", "name": "Jacksonville"},
    {"location": "Fort Worth, TX", "name": "FortWorth"},
    {"location": "Columbus, OH", "name": "Columbus"},
    {"location": "Charlotte, NC", "name": "Charlotte"},
    {"location": "Seattle, WA", "name": "Seattle"},
    {"location": "Denver, CO", "name": "Denver"},
    {"location": "Boston, MA", "name": "Boston"},
    {"location": "Miami, FL", "name": "Miami"},
    {"location": "Atlanta, GA", "name": "Atlanta"},
    {"location": "Las Vegas, NV", "name": "Vegas"},
]

# High-value industries
INDUSTRIES = [
    {"industry": "restaurants", "label": "Restaurants"},
    {"industry": "retail", "label": "Retail"},
    {"industry": "services", "label": "Services"},
    {"industry": "plumbers", "label": "Plumbers"},
    {"industry": "electricians", "label": "Electricians"},
    {"industry": "roofing", "label": "Roofing"},
    {"industry": "landscaping", "label": "Landscaping"},
    {"industry": "auto repair", "label": "Auto Repair"},
    {"industry": "dentists", "label": "Dentists"},
    {"industry": "veterinarians", "label": "Vets"},
]


def generate_mock_leads(city: Dict, industry: Dict, limit: int = 50) -> List[Dict]:
    """Generate mock business leads for a city/industry combo."""
    leads = []
    
    # Sample business name patterns by industry
    name_patterns = {
        "restaurants": ["{name}'s {food}", "{adjective} {food} House", "The {adjective} {food}", "{name}'s Kitchen"],
        "retail": ["{name}'s {shop}", "{adjective} {product} Shop", "The {product} Store", "{name}'s Boutique"],
        "services": ["{name}'s {service}", "{adjective} {service} Co", "Pro {service}", "{name} {service} Services"],
        "plumbers": ["{name}'s Plumbing", "Quick Plumbing", "Pro Plumbers", "{name} Plumbing Services"],
        "electricians": ["{name}'s Electric", "Power Electric", "Pro Electricians", "{name} Electrical"],
        "roofing": ["{name}'s Roofing", "Quality Roofs", "Pro Roofing", "{name} Roof Services"],
        "landscaping": ["{name}'s Landscaping", "Green Gardens", "Pro Landscaping", "{name} Lawn Care"],
        "auto repair": ["{name}'s Auto", "Quick Auto Repair", "Pro Mechanics", "{name} Garage"],
        "dentists": ["{name} Dental", "Bright Smiles", "Family Dentistry", "{name} Dental Care"],
        "veterinarians": ["{name} Vet", "Pet Care Clinic", "Animal Hospital", "{name} Veterinary"],
    }
    
    names = ["Joe", "Mike", "Tony", "Sal", "Bob", "Jim", "Dan", "Tom", "Steve", "Rick", 
             "Maria", "Lisa", "Anna", "Sue", "Kate", "Jenny", "Linda", "Carol", "Nancy", "Diana"]
    
    adjectives = ["Best", "Top", "Quality", "Express", "Quick", "Prime", "Elite", "Pro", "Super", "Mega",
                  "Golden", "Silver", "Premium", "Select", "Choice", "First", "Main", "Central", "Local", "Neighborhood"]
    
    foods = ["Pizza", "Burger", "Taco", "Chinese", "Italian", "Mexican", "Thai", "Indian", "BBQ", "Steak"]
    
    shops = ["Store", "Shop", "Boutique", "Market", "Mart", "Place", "Center", "Hub", "Depot", "Outlet"]
    
    products = ["Fashion", "Electronics", "Home", "Garden", "Sports", "Beauty", "Pet", "Book", "Toy", "Gift"]
    
    services_list = ["Plumbing", "Electric", "Cleaning", "Repair", "Maintenance", "Installation", "Services", "Solutions", "Experts", "Pros"]
    
    for i in range(limit):
        pattern = random.choice(name_patterns.get(industry["industry"], ["{name}'s Business"]))
        
        name = random.choice(names)
        adj = random.choice(adjectives)
        
        # Generate business name based on industry
        if industry["industry"] == "restaurants":
            food = random.choice(foods)
            biz_name = pattern.format(name=name, food=food, adjective=adj)
        elif industry["industry"] == "retail":
            product = random.choice(products)
            shop = random.choice(shops)
            biz_name = pattern.format(name=name, product=product, shop=shop, adjective=adj)
        elif industry["industry"] == "services":
            service = random.choice(services_list)
            biz_name = pattern.format(name=name, service=service, adjective=adj)
        else:
            biz_name = pattern.format(name=name, adjective=adj)
        
        # Generate area code based on city
        area_codes = {
            "LA": ["213", "310", "323", "424", "626", "714", "818"],
            "Chicago": ["312", "773", "847", "630", "708"],
            "Houston": ["713", "281", "832", "346"],
            "Phoenix": ["602", "480", "623", "520"],
            "Philly": ["215", "267", "484", "610"],
            "SanAntonio": ["210", "830"],
            "SanDiego": ["619", "858", "760"],
            "Dallas": ["214", "972", "469", "817"],
            "SanJose": ["408", "669"],
            "Austin": ["512", "737"],
            "Jacksonville": ["904"],
            "FortWorth": ["817", "682"],
            "Columbus": ["614", "380"],
            "Charlotte": ["704", "980"],
            "Seattle": ["206", "425", "253"],
            "Denver": ["303", "720", "719"],
            "Boston": ["617", "857", "781", "978"],
            "Miami": ["305", "786", "954", "305"],
            "Atlanta": ["404", "678", "770", "470"],
            "Vegas": ["702", "725"],
            "NY": ["212", "347", "718", "646", "917"],
        }
        
        area = random.choice(area_codes.get(city.get("name", "NY"), ["555"]))
        phone = f"({area}) {random.randint(100,999)}-{random.randint(1000,9999)}"
        
        # Generate email
        email_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
        email_name = biz_name.lower().replace("'", "").replace(" ", "")[:20]
        email = f"{email_name}@{random.choice(email_domains)}"
        
        lead = {
            "business_name": biz_name,
            "address": f"{random.randint(100,9999)} {random.choice(['Main', 'First', 'Second', 'Third', 'Park', 'Oak', 'Maple', 'Cedar'])} {random.choice(['St', 'Ave', 'Blvd', 'Rd', 'Ln'])}, {city['location'].split(',')[0]} {random.choice(['CA', 'TX', 'NY', 'FL', 'IL', 'PA', 'AZ', 'WA', 'CO', 'GA', 'NC', 'OH', 'NV', 'MA'])}",
            "phone": phone,
            "email": email,
            "industry": industry["industry"],
            "location": city["location"],
            "google_maps_url": f"https://maps.google.com/?q={biz_name.replace(' ', '+')},{city['location'].replace(' ', '+')}",
            "has_website": "False",
            "notes": f"{random.choice(['Family-owned', 'Established', 'Local favorite', 'Highly rated', 'Growing business'])} - Batch {city['name']}-{industry['label']}"
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
    """Generate proposal emails from leads."""
    leads = []
    with open(leads_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            leads.append(row)
    
    proposals = []
    for lead in leads:
        biz_name = lead.get('business_name', 'Business')
        email = lead.get('email', '')
        location = lead.get('location', 'Your City')
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

**Special Launch Offer:**
First 10 customers get FREE domain name for 1 year (£15 value)

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
            "notes": f"Generated from {leads_path}"
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
    print("🏭 Batch Lead Generator")
    print("=" * 50)
    print()
    
    # Create output directory
    output_dir = Path(__file__).parent / 'batches'
    output_dir.mkdir(exist_ok=True)
    
    # Generate batches for top city/industry combos
    batches_created = []
    
    # Top combinations (city x industry = 50 leads each)
    top_combos = [
        (0, 0), (0, 1), (0, 2),  # LA: restaurants, retail, services
        (1, 0), (1, 1), (1, 2),  # Chicago: restaurants, retail, services
        (2, 0), (2, 1), (2, 2),  # Houston: restaurants, retail, services
        (17, 0), (17, 1), (17, 2),  # Miami: restaurants, retail, services
        (18, 0), (18, 1), (18, 2),  # Atlanta: restaurants, retail, services
        (14, 0), (14, 1), (14, 2),  # Seattle: restaurants, retail, services
    ]
    
    for city_idx, industry_idx in top_combos:
        city = CITIES[city_idx]
        industry = INDUSTRIES[industry_idx]
        
        timestamp = datetime.now().strftime('%Y%m%d')
        leads_file = output_dir / f"leads-{city['name']}-{industry['label']}-{timestamp}.csv"
        proposals_file = output_dir / f"proposals-{city['name']}-{industry['label']}-{timestamp}.csv"
        
        print(f"\n📍 Generating: {city['location']} - {industry['label']}")
        
        # Generate leads
        leads = generate_mock_leads(city, industry, limit=50)
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
    print("📊 BATCH SUMMARY")
    print("=" * 50)
    
    total_leads = sum(b['count'] for b in batches_created)
    print(f"\n✅ Created {len(batches_created)} batches")
    print(f"📈 Total leads: {total_leads}")
    print(f"📁 Location: {output_dir}")
    print()
    
    for b in batches_created:
        print(f"  • {b['city']} - {b['industry']}: {b['count']} leads")
    
    print()
    print("🚀 To send a batch:")
    print(f"   python scripts/send_emails.py --input batches/proposals-City-Industry-DATE.csv --limit 20")
    print()


if __name__ == '__main__':
    main()
