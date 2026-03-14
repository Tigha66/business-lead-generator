# Lead Scoring Criteria

Score each lead from 1-100. Only process leads with score ≥70.

## Scoring Factors

### 1. Website Absence Confidence (0-30 points)
- **30 pts**: Explicitly listed as "no website" in listing
- **25 pts**: No website field in listing + no domain found via search
- **20 pts**: Website listed but domain doesn't resolve
- **15 pts**: Website listed but appears to be social media only (Facebook, Yelp)
- **0 pts**: Has active, functional website

### 2. Benefit Likelihood (0-25 points)
- **25 pts**: Service business with clear customer-facing need (plumber, electrician, roofer)
- **20 pts**: Professional service (dentist, chiropractor, tutor)
- **18 pts**: Retail/restaurant with menu/services to showcase
- **15 pts**: General local business
- **10 pts**: Unclear benefit from website
- **0 pts**: Business type doesn't need website

### 3. Data Quality (0-20 points)
- **20 pts**: Complete info (name, address, phone, hours, services, photos)
- **15 pts**: Most info present (missing 1-2 fields)
- **10 pts**: Basic info only (name, address, phone)
- **5 pts**: Sparse data
- **0 pts**: Critical fields missing (no phone or address)

### 4. Local Business Fit (0-15 points)
- **15 pts**: Independent local business, single location
- **12 pts**: Small local chain (2-5 locations)
- **10 pts**: Franchise location
- **5 pts**: Unclear ownership
- **0 pts**: National chain or corporate location (exclude)

### 5. Direct Mail Suitability (0-10 points)
- **10 pts**: Physical address verified, not PO box
- **8 pts**: Address appears valid (street address)
- **5 pts**: Address uncertain
- **0 pts**: PO box only or no address

## Automatic Exclusions

Exclude immediately if any of these apply:
- ❌ National chain (Starbucks, McDonald's, etc.)
- ❌ Permanently closed (per listing)
- ❌ PO box only (no physical address)
- ❌ Duplicate of existing lead
- ❌ Low confidence score (<50)
- ❌ Clearly has functional website
- ❌ Government/non-profit (different outreach approach)

## Scoring Examples

### Example A: Local Plumber
- No website listed: 25 pts
- Service business (plumber): 25 pts
- Complete info + photos: 20 pts
- Independent, single location: 15 pts
- Valid street address: 10 pts
- **Total: 95/100** ✅ QUALIFY

### Example B: Restaurant with Facebook Only
- Website is Facebook page: 15 pts
- Restaurant (benefit from site): 18 pts
- Good info, menu on Facebook: 18 pts
- Independent restaurant: 15 pts
- Valid address: 10 pts
- **Total: 76/100** ✅ QUALIFY

### Example C: National Chain Location
- No individual website: 20 pts
- Chain location: 10 pts
- Complete info: 20 pts
- National chain: 0 pts (EXCLUDE)
- Valid address: 10 pts
- **Total: 60/100** ❌ EXCLUDE (chain)

### Example D: Sparse Listing
- No website: 25 pts
- Unclear business type: 10 pts
- Only name + phone: 5 pts
- Unknown ownership: 5 pts
- Address uncertain: 5 pts
- **Total: 50/100** ❌ EXCLUDE (low confidence)

## Confidence Notes

For each lead, document:
- Why we believe they lack a website
- What data sources were checked
- Any uncertainties or flags
- Recommended personalization angles

---

**Threshold:** 70+ to qualify  
**Review:** Manual review recommended for scores 70-79  
**Auto-approve:** Scores 85+ with no flags
