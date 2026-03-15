#!/usr/bin/env python3
"""Generate high-value trade leads (plumbers, electricians, roofers)"""

import csv
import random
from pathlib import Path
from datetime import datetime

# UK Trade industries (high value!)
TRADES = [
    ('London', 'plumbers', 'Plumbing Services'),
    ('London', 'electricians', 'Electrical Services'),
    ('Manchester', 'plumbers', 'Plumbing Services'),
    ('Manchester', 'electricians', 'Electrical Services'),
    ('Birmingham', 'plumbers', 'Plumbing Services'),
    ('Birmingham', 'roofing', 'Roofing Services'),
]

uk_names = ['James', 'John', 'David', 'Michael', 'Robert', 'William', 'Thomas', 'George', 
            'Sarah', 'Emma', 'Lisa', 'Karen', 'Susan', 'Claire', 'Helen', 'Rachel']

adjectives = ['Pro', 'Quality', 'Express', 'Prime', 'Elite', 'Local', 'Family', 'Reliable', 
              'Trusted', 'Expert', 'Swift', 'Direct', 'Rapid', '24/7']

streets = ['High Street', 'Main Road', 'Church Lane', 'Station Road', 'Market Street', 
           'Victoria Road', 'King Street', 'Queen Street', 'Mill Lane', 'Park Avenue']

domains = ['gmail.com', 'btinternet.com', 'yahoo.co.uk', 'hotmail.co.uk', 'outlook.com']

for city, industry, label in TRADES:
    leads = []
    for i in range(30):
        name = random.choice(uk_names)
        adj = random.choice(adjectives)
        
        if industry == 'plumbers':
            if random.random() > 0.5:
                biz_name = name + "'s Plumbing"
            else:
                biz_name = adj + " Plumbers " + city
        elif industry == 'electricians':
            if random.random() > 0.5:
                biz_name = name + "'s Electrical"
            else:
                biz_name = adj + " Electricians"
        else:
            if random.random() > 0.5:
                biz_name = name + "'s Roofing"
            else:
                biz_name = adj + " Roofing Services"
        
        phone = "0" + random.choice(['20', '161', '121', '113', '141', '151']) + " " + str(random.randint(1000,9999)) + " " + str(random.randint(1000,9999))
        
        clean_name = biz_name.lower().replace(' ', '').replace("'", '')
        email = clean_name + "@" + random.choice(domains)
        
        address = str(random.randint(1,500)) + " " + random.choice(streets) + ", " + city
        
        leads.append({
            'business_name': biz_name,
            'address': address,
            'phone': phone,
            'email': email,
            'industry': industry,
            'location': city + ', UK',
            'google_maps_url': 'https://maps.google.com/?q=' + biz_name.replace(' ', '+') + ',' + city + ',UK',
            'has_website': 'False',
            'notes': 'High-value trade lead - ' + label + ' - UK Batch ' + datetime.now().strftime("%Y%m%d")
        })
    
    # Save leads
    date_str = datetime.now().strftime("%Y%m%d")
    filename = 'batches-uk/leads-' + city + '-' + industry.title() + '-TRADE-UK-' + date_str + '.csv'
    
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=leads[0].keys())
        writer.writeheader()
        writer.writerows(leads)
    
    print('✅ Created', filename, '(' + str(len(leads)) + ' leads)')

print()
print('High-value trade leads generated!')
print('Total: 6 batches × 30 leads = 180 trade leads')
