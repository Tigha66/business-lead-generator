#!/usr/bin/env python3
"""
Find local businesses without websites using Google Maps search.
Outputs a CSV file with business details for outreach.
"""

import argparse
import csv
import json
import time
import random
from pathlib import Path
from typing import List, Dict, Optional

# Try to import selenium for browser automation
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    HAS_SELENIUM = True
except ImportError:
    HAS_SELENIUM = False

# Try to import googlemaps for official API
try:
    import googlemaps
    HAS_GOOGLEMAPS = True
except ImportError:
    HAS_GOOGLEMAPS = False


def search_businesses_manual(location: str, industry: str, limit: int = 50) -> List[Dict]:
    """
    Manual search approach - user verifies results.
    This is a placeholder for manual data entry or copy-paste from Google Maps.
    """
    print(f"\n🔍 Searching for {industry} businesses in {location}")
    print(f"Target: {limit} businesses")
    print("\n📋 Manual Entry Mode:")
    print("Open Google Maps and search for: '{industry} in {location}'")
    print("Look for businesses WITHOUT a website link in their profile")
    print("Copy business details and paste below (empty line to finish):\n")
    
    businesses = []
    while len(businesses) < limit:
        try:
            line = input(f"Business {len(businesses) + 1}: ").strip()
            if not line:
                break
            
            # Simple parsing: name, address, phone
            parts = [p.strip() for p in line.split(',')]
            if len(parts) >= 2:
                business = {
                    'business_name': parts[0],
                    'address': parts[1] if len(parts) > 1 else '',
                    'phone': parts[2] if len(parts) > 2 else '',
                    'email': '',
                    'industry': industry,
                    'location': location,
                    'google_maps_url': '',
                    'has_website': False,
                    'notes': ''
                }
                businesses.append(business)
                print(f"  ✓ Added: {business['business_name']}")
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"  Error parsing: {e}")
    
    return businesses


def search_businesses_selenium(location: str, industry: str, limit: int = 50) -> List[Dict]:
    """
    Automated search using Selenium browser automation.
    Requires Chrome and chromedriver installed.
    """
    if not HAS_SELENIUM:
        print("❌ Selenium not installed. Run: pip install selenium")
        return []
    
    print(f"\n🔍 Automated search for {industry} in {location}...")
    
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
    
    businesses = []
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        wait = WebDriverWait(driver, 10)
        
        # Search Google Maps
        search_query = f"{industry} in {location}"
        url = f"https://www.google.com/maps/search/{search_query.replace(' ', '+')}"
        driver.get(url)
        
        time.sleep(3)  # Wait for page load
        
        # Find business listings (this selector may need updates)
        listings = driver.find_elements(By.CSS_SELECTOR, 'div[role="article"]')
        
        for listing in listings[:limit]:
            try:
                name_elem = listing.find_element(By.CSS_SELECTOR, 'div.fontHeadlineSmall')
                name = name_elem.text if name_elem else ''
                
                if not name:
                    continue
                
                business = {
                    'business_name': name,
                    'address': '',
                    'phone': '',
                    'email': '',
                    'industry': industry,
                    'location': location,
                    'google_maps_url': driver.current_url,
                    'has_website': False,  # Would need additional checking
                    'notes': ''
                }
                businesses.append(business)
                
                # Rate limiting
                time.sleep(random.uniform(2, 5))
                
            except Exception as e:
                continue
        
        driver.quit()
        
    except Exception as e:
        print(f"❌ Error: {e}")
    
    return businesses


def search_businesses_api(location: str, industry: str, limit: int = 50, api_key: Optional[str] = None) -> List[Dict]:
    """
    Search using official Google Maps API.
    Requires API key with Places API enabled.
    """
    if not HAS_GOOGLEMAPS:
        print("❌ googlemaps not installed. Run: pip install googlemaps")
        return []
    
    if not api_key:
        # Try to load from config
        config_path = Path.home() / '.openclaw' / 'google_maps_api_key.txt'
        if config_path.exists():
            api_key = config_path.read_text().strip()
        else:
            print("❌ No Google Maps API key found.")
            print("   Get one at: https://developers.google.com/maps/documentation/places/web-service/get-api-key")
            print("   Save to: ~/.openclaw/google_maps_api_key.txt")
            return []
    
    print(f"\n🔍 API search for {industry} in {location}...")
    
    gmaps = googlemaps.Client(key=api_key)
    businesses = []
    
    try:
        # Places API search
        places_result = gmaps.places(
            query=f"{industry} in {location}",
            type='establishment'
        )
        
        for place in places_result.get('results', [])[:limit]:
            place_id = place.get('place_id')
            
            # Get detailed info
            details = gmaps.place(place_id=place_id)
            result = details.get('result', {})
            
            # Check if website exists
            has_website = 'website' in result
            
            # Skip if has website (we want businesses WITHOUT websites)
            if has_website:
                continue
            
            business = {
                'business_name': result.get('name', ''),
                'address': result.get('formatted_address', ''),
                'phone': result.get('formatted_phone_number', ''),
                'email': '',  # Not available via Places API
                'industry': industry,
                'location': location,
                'google_maps_url': f"https://www.google.com/maps/place/?q=place_id:{place_id}",
                'has_website': False,
                'notes': ''
            }
            businesses.append(business)
            
            # Rate limiting (API limits)
            time.sleep(0.5)
        
    except Exception as e:
        print(f"❌ API Error: {e}")
    
    return businesses


def save_to_csv(businesses: List[Dict], output_path: str):
    """Save business list to CSV file."""
    if not businesses:
        print("⚠️  No businesses to save")
        return
    
    fieldnames = [
        'business_name', 'address', 'phone', 'email',
        'industry', 'location', 'google_maps_url', 'has_website', 'notes'
    ]
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(businesses)
    
    print(f"\n✅ Saved {len(businesses)} businesses to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description='Find local businesses without websites')
    parser.add_argument('--location', type=str, required=True, help='City/region to search')
    parser.add_argument('--industry', type=str, required=True, help='Business category')
    parser.add_argument('--limit', type=int, default=50, help='Max results')
    parser.add_argument('--output', type=str, default='leads.csv', help='Output CSV file')
    parser.add_argument('--method', type=str, choices=['manual', 'selenium', 'api'], 
                       default='manual', help='Search method')
    parser.add_argument('--api-key', type=str, help='Google Maps API key')
    
    args = parser.parse_args()
    
    print("🦞 Business Lead Generator")
    print("=" * 50)
    
    # Search based on method
    if args.method == 'manual':
        businesses = search_businesses_manual(args.location, args.industry, args.limit)
    elif args.method == 'selenium':
        businesses = search_businesses_selenium(args.location, args.industry, args.limit)
    elif args.method == 'api':
        businesses = search_businesses_api(args.location, args.industry, args.limit, args.api_key)
    else:
        businesses = []
    
    # Save results
    save_to_csv(businesses, args.output)
    
    print(f"\n📊 Summary:")
    print(f"   Location: {args.location}")
    print(f"   Industry: {args.industry}")
    print(f"   Found: {len(businesses)} businesses")
    print(f"   Output: {args.output}")


if __name__ == '__main__':
    main()
