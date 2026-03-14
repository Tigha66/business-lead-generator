# Outreach Agent - Autonomous Lead Gen & Direct Mail System

## Mission

Find local US businesses without websites, generate custom demo website concepts, create direct-mail postcards with QR codes, and prepare outreach workflows that run continuously with minimal manual intervention.

## Core Workflow

```
Discovery → Qualification → Website Gen → Postcard Creation → Fulfillment Prep → Response Tracking
```

## Modules

### 1. Discovery (`discovery/`)
- Search public business listings (Google Maps, Yelp, Yellow Pages, etc.)
- Target service-based businesses: plumbers, electricians, landscapers, cleaners, roofers, auto shops, salons, tutors, pet groomers, restaurants, contractors, dentists, chiropractors
- Capture: name, category, address, phone, listing URL, reviews, rating, hours, photos, services, city/state
- Exclude: duplicates, chains, closed businesses, PO boxes, low-confidence records

### 2. Qualification (`discovery/scoring.md`)
- Score leads 1-100 based on:
  - Confidence they lack a real website
  - Likelihood they benefit from a website
  - Quality of available public data
  - Local business fit
  - Direct-mail suitability
- Only process leads above threshold (default: 70+)

### 3. Website Generation (`website-gen/`)
- Create custom starter websites using only public business info
- Include: homepage, headline, services, about, testimonials (if public), contact, CTA, local SEO copy
- Modern, tasteful design
- Label as preview/demo until claimed
- Output: live preview URL, screenshot, QR code, personalized summary

### 4. Postcard Creation (`postcard/`)
- Print-ready direct-mail postcard (4x6 or 6x9)
- Front: business name, website preview image, QR code, headline
- Back: personalized message, benefits explanation, CTA, contact details
- Tone: helpful, impressive, non-pushy, premium, trustworthy

### 5. Fulfillment (`fulfillment/`)
- Prepare mailing data: recipient name, address, postcard file, campaign ID, tracking ID, QR destination
- Validate all fields before export
- Integrate with mail APIs (Lob, PostcardMania, etc.)

### 6. Dashboard (`dashboard/`)
- Campaign stats: total found, qualified, websites generated, postcards prepared, duplicates removed
- Top niches, top cities
- Next-action queue
- Lead state tracking

## Legal & Ethical Constraints

- ✅ Follow all applicable laws, platform terms, privacy rules, direct-mail regulations
- ✅ Do not misrepresent affiliation with Google or business owner
- ✅ Do not fabricate reviews, credentials, or business facts
- ✅ Do not use copyrighted content outside lawful/public-use boundaries
- ✅ Mark all generated sites/materials as previews/demos until claimed
- ✅ Respect opt-outs, suppression lists, do-not-contact records
- ✅ Prefer accuracy over volume
- ✅ Flag uncertain leads instead of forcing through

## File Structure

```
skills/outreach-agent/
├── SKILL.md                 # This file
├── discovery/
│   ├── search.js            # Lead discovery logic
│   ├── scoring.md           # Scoring criteria
│   └── sources.md           # Data source documentation
├── website-gen/
│   ├── templates/           # HTML/CSS templates
│   ├── generator.md         # Site generation logic
│   └── qr-gen.md            # QR code generation
├── postcard/
│   ├── templates/           # Postcard design templates
│   └── copy.md              # Message/copy guidelines
├── fulfillment/
│   ├── mailing-prep.md      # Mailing data preparation
│   └── integrations.md      # Mail API integrations
├── dashboard/
│   ├── stats.md             # Dashboard metrics
│   └── queue.md             # Action queue management
├── configs/
│   ├── thresholds.json      # Scoring thresholds
│   └── templates.json       # Template configurations
├── data/
│   ├── leads-raw.json       # Raw discovered leads
│   ├── leads-qualified.json # Scored & qualified leads
│   └── suppression.json     # Do-not-contact list
└── output/
    ├── leads.csv            # Exportable lead table
    ├── postcards/           # Postcard preview files
    └── dashboard.json       # Campaign summary
```

## Usage

### Run Discovery
```bash
# Search for leads in specific categories/cities
node discovery/search.js --category=plumber --city=Austin --state=TX --limit=100
```

### Qualify Leads
```bash
# Score and filter leads
node discovery/score.js --input=data/leads-raw.json --threshold=70
```

### Generate Websites
```bash
# Create demo sites for qualified leads
node website-gen/generate.js --input=data/leads-qualified.json --batch=10
```

### Create Postcards
```bash
# Generate postcard assets
node postcard/create.js --input=output/websites.json --format=print-ready
```

### Export Campaign
```bash
# Prepare fulfillment data
node fulfillment/export.js --campaign=campaign-001
```

## Continuous Operation

Set up cron jobs for automated runs:
- Discovery: Daily at 2 AM
- Qualification: Daily at 3 AM
- Website gen: Daily at 4 AM
- Postcard creation: Daily at 5 AM
- Fulfillment export: Weekly on Monday at 6 AM

## API Integrations (Recommended)

| Service | Purpose | Config Key |
|---------|---------|------------|
| Google Places API | Business data | `GOOGLE_PLACES_KEY` |
| Yelp Fusion API | Business data | `YELP_API_KEY` |
| Lob | Postcard printing | `LOB_API_KEY` |
| Vercel/Netlify | Website hosting | `VERCEL_TOKEN` |
| Bitly | QR tracking | `BITLY_TOKEN` |

## Pilot Run Checklist

- [ ] Discover 100 leads
- [ ] Score and qualify (threshold 70+)
- [ ] Generate 10 website previews
- [ ] Create 10 postcard concepts
- [ ] Export CSV + dashboard
- [ ] Review and iterate

---

**Version:** 1.0  
**Created:** 2026-03-15  
**Status:** Active Development
