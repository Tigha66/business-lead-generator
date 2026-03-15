# 🚀 ReviewPilot - Complete Build Plan

**Product:** Automated Google Review Response System  
**Goal:** £1,000/month in 30 days  
**Target:** 10 customers at £99/month

---

## 📋 PRODUCT OVERVIEW

### Product Name
**ReviewPilot** - Never Miss a Review Response Again

### Positioning
"Auto-respond to every Google review in 30 seconds. Boost local SEO and win more customers — on autopilot."

### Target Customer
- Local businesses with 20+ Google reviews
- Dentists, med spas, restaurants, salons, HVAC, plumbers
- Owner doesn't have time to respond to reviews manually
- Currently responding to <50% of reviews (or none at all)

### Core Value Proposition
- **Before:** Reviews pile up, owner forgets to respond, local SEO suffers, potential customers see unanswered reviews
- **After:** Every review gets a professional response within hours, local SEO improves, conversion rate increases

---

## 🎯 CORE FEATURES

### MVP (Week 1)
- [ ] Google Business Profile API integration
- [ ] Poll for new reviews every 6 hours
- [ ] AI-generated response drafts (Claude/OpenAI)
- [ ] Email drafts to owner for approval
- [ ] Manual post to Google (owner does this)
- [ ] Google Sheets log of all reviews/responses

### V2 (Week 3-4)
- [ ] Auto-post 4-5 star reviews (no approval needed)
- [ ] SMS notifications for new reviews
- [ ] Response tone customization (formal, friendly, etc.)
- [ ] Multi-location support

### V3 (Month 2)
- [ ] Web dashboard
- [ ] Analytics (response rate, avg rating trend)
- [ ] Team member access
- [ ] White-label for agencies

---

## 🔄 WORKFLOW DIAGRAM

```
┌─────────────────────────────────────────────────────────────┐
│                    ReviewPilot Workflow                      │
└─────────────────────────────────────────────────────────────┘

1. POLL (Every 6 hours)
   └─→ Google Business Profile API
       └─→ Check for new reviews

2. DETECT
   └─→ New review found?
       ├─→ YES: Extract (reviewer name, stars, text, date)
       └─→ NO: Wait for next poll

3. GENERATE RESPONSE
   └─→ Send to AI (Claude/OpenAI)
       └─→ Prompt: "Write a professional Google review response
                    for [BUSINESS NAME]. Review: [TEXT]. 
                    Rating: [STARS]. Keep it under 100 words."
       └─→ Receive drafted response

4. NOTIFY OWNER
   └─→ Email to business owner
       └─→ Subject: "New Google Review - Action Needed"
       └─→ Body: Review details + drafted response
       └─→ Button: "Approve & Post" (links to Google)

5. AUTO-POST (V2 feature)
   └─→ If 4-5 stars: Post directly via API
   └─→ If 1-3 stars: Flag for manual review

6. LOG
   └─→ Google Sheets row:
       └─→ Date, Business, Reviewer, Stars, Response Sent, Posted (Y/N)

7. REPORT (Monthly)
   └─→ Email summary:
       └─→ Reviews received, responses sent, avg rating, trend
```

---

## 🛠️ TECH STACK

### MVP Stack (Fastest to Build)
| Component | Tool | Cost |
|-----------|------|------|
| Backend | Python + FastAPI | Free |
| Google API | Google Business Profile | Free |
| AI | Claude API (Dashscope) | ~£0.01/response |
| Email | Gmail API or SMTP | Free |
| Database | Google Sheets | Free |
| Hosting | Railway/Render | £5-10/month |
| **Total Monthly** | | **~£10** |

### V2 Stack (Scaled)
| Component | Tool | Cost |
|-----------|------|------|
| Backend | Python + FastAPI | Free |
| Database | Supabase (PostgreSQL) | £25/month |
| Frontend | Next.js + Vercel | Free |
| Email | Resend | £15/month |
| SMS | Twilio | £0.0075/SMS |
| **Total Monthly** | | **~£50** |

---

## 💷 PRICING LADDER

### Tier 1: Starter - £49/month
- 1 location
- Up to 50 reviews/month
- Email notifications
- Manual approval required
- Monthly report

### Tier 2: Professional - £99/month ⭐ (RECOMMENDED)
- Up to 5 locations
- Unlimited reviews
- SMS + email notifications
- Auto-post 4-5 star reviews
- Response tone customization
- Monthly report + analytics

### Tier 3: Agency - £199/month
- Unlimited locations
- Everything in Professional
- White-label dashboard
- Client access portals
- Priority support

### Setup Fee: £297 (one-time)
- Google Business Profile connection
- Response tone setup
- Team training
- 30-day support

---

## 📄 LANDING PAGE COPY

### Headline
**"Auto-Respond to Every Google Review in 30 Seconds"**

### Subheadline
Boost local SEO and win more customers with professional review responses — completely automated.

### 5 Bullet Value Points
- ✅ **Never miss a review** — Get notified instantly when new reviews arrive
- ✅ **AI-powered responses** — Professional, personalized replies in seconds
- ✅ **Boost local SEO** — Google ranks businesses higher when they respond to reviews
- ✅ **Save 5+ hours/month** — No more manual review monitoring and writing
- ✅ **Convert more customers** — 89% of consumers read responses before choosing

### Product Description
```
Google reviews make or break local businesses. But responding to every review 
takes time you don't have.

ReviewPilot monitors your Google Business Profile 24/7. When a new review arrives, 
our AI drafts a professional, personalized response in seconds. You approve with 
one click (or let us auto-post positive reviews).

Result: Every review gets answered, your local SEO improves, and more customers 
choose you over competitors.

🎯 Perfect for: Dentists, med spas, restaurants, salons, HVAC, plumbers, 
and any local business with 20+ Google reviews.

⚡ Setup takes 15 minutes. Results start immediately.
```

### Social Proof Section (Add after first customers)
- "ReviewPilot saved me 3 hours/week. Our response rate went from 20% to 100%!" 
  — Sarah K., Dental Clinic Owner
- "Local SEO ranking improved within 2 weeks. Worth every penny."
  — Mike R., HVAC Business Owner

### CTA Section
**Start Your 14-Day Free Trial**
No credit card required. First 10 customers get 50% off for life.

[Get Started] [Book Demo]

---

## 🚀 LAUNCH STRATEGY

### Phase 1: Validation (Days 1-7)
**Goal:** 3 free trial customers

**Actions:**
1. Build MVP (2 days)
2. Create simple landing page (Carrd.co, 1 day)
3. Manual outreach to 50 businesses (2 days)
4. Onboard 3 trials (2 days)

**Outreach Script:**
```
Subject: Quick question about your Google reviews

Hi [Name],

I noticed [Business Name] has great Google reviews ([X] stars, [Y] reviews) 
but you're only responding to about [Z]% of them.

Research shows businesses that respond to reviews rank higher in local search 
and convert 23% more customers.

I built a tool that auto-responds to every review in 30 seconds. 
I'm looking for 3 businesses to test it free for 14 days.

Want me to send over the details?

Best,
[Your Name]
```

### Phase 2: Conversion (Days 8-14)
**Goal:** Convert 2 trials to paid

**Actions:**
1. Daily check-ins with trial users
2. Show them metrics (reviews responded to, time saved)
3. Offer 50% off for life if they convert in trial period
4. Collect testimonials

**Conversion Script:**
```
Subject: Your ReviewPilot trial results

Hi [Name],

Quick update on your first week with ReviewPilot:

📊 Reviews received: 8
✅ Responses sent: 8 (100% — up from 20%!)
⏱️ Time saved: ~2 hours

Your customers are now seeing professional responses to every review. 
This directly impacts your local SEO ranking and conversion rate.

Your trial ends in 7 days. As a founding customer, you're eligible for 
50% off for life (£49/month instead of £99).

Want to continue? Just reply "yes" and I'll send the invoice.

Best,
[Your Name]
```

### Phase 3: Scale (Days 15-30)
**Goal:** 10 paying customers total

**Actions:**
1. Double down on what's working (which outreach channel converted best?)
2. Add content marketing (LinkedIn posts about local SEO + reviews)
3. Ask for referrals from happy customers
4. Consider paid ads (Google Ads targeting "google review management")

**Content Ideas:**
- "Why 80% of local businesses are losing customers to competitors (hint: it's their Google reviews)"
- "How responding to reviews improved our local SEO ranking by 40%"
- "The 30-second habit that adds £10k/year in revenue"

---

## 📅 30-DAY EXECUTION PLAN

### Week 1: Build & Validate
| Day | Task | Done? |
|-----|------|-------|
| 1 | Set up Google Business Profile API | ☐ |
| 2 | Build review polling + AI response | ☐ |
| 3 | Create landing page (Carrd) | ☐ |
| 4 | Write outreach scripts | ☐ |
| 5 | Send 50 outreach emails | ☐ |
| 6 | Onboard first trial customer | ☐ |
| 7 | Iterate based on feedback | ☐ |

### Week 2: Convert
| Day | Task | Done? |
|-----|------|-------|
| 8 | Check in with trial users | ☐ |
| 9 | Show metrics, offer discount | ☐ |
| 10 | Convert first paid customer | ☐ |
| 11 | Send 50 more outreach emails | ☐ |
| 12 | Onboard 2 more trials | ☐ |
| 13 | Collect testimonials | ☐ |
| 14 | Week review: what's working? | ☐ |

### Week 3: Scale
| Day | Task | Done? |
|-----|------|-------|
| 15 | Build auto-post feature (V2) | ☐ |
| 16 | Create LinkedIn content | ☐ |
| 17 | Send 100 outreach emails | ☐ |
| 18 | Onboard 3 more trials | ☐ |
| 19 | Convert 2 more paid | ☐ |
| 20 | Ask for referrals | ☐ |
| 21 | Week review | ☐ |

### Week 4: Optimize
| Day | Task | Done? |
|-----|------|-------|
| 22 | Improve landing page | ☐ |
| 23 | Create case study | ☐ |
| 24 | Test paid ads (£50 budget) | ☐ |
| 25 | Onboard more trials | ☐ |
| 26 | Convert more paid | ☐ |
| 27 | Build V3 features | ☐ |
| 28 | Month review: hit £1k? | ☐ |
| 29-30 | Plan Month 2 | ☐ |

---

## 📧 OUTREACH MESSAGES

### Cold Email Template #1 (Direct)
```
Subject: Your Google reviews

Hi [Name],

I was looking at [Business Name] on Google Maps and noticed you have 
[X] reviews but only responding to about [Y]%.

Businesses that respond to reviews rank higher in local search and 
convert 23% more customers.

I built a tool that auto-responds to every review in 30 seconds. 
Currently looking for 3 businesses to test it free for 14 days.

Interested?

Best,
[Your Name]
ReviewPilot
```

### Cold Email Template #2 (Value-First)
```
Subject: I wrote a response to your latest Google review

Hi [Name],

Your customer Sarah left a great 5-star review last week:
"[Review text]"

Here's a response I drafted for you:

"Hi Sarah, thank you so much for the wonderful review! We're thrilled 
you had a great experience. Looking forward to serving you again soon! 
- The [Business] Team"

Want me to handle all your review responses like this? 
I'm offering a free 14-day trial to 3 businesses this week.

Let me know!

Best,
[Your Name]
```

### LinkedIn DM Template
```
Hi [Name], saw [Business] has [X] Google reviews — impressive!

Quick question: are you responding to all of them? Research shows 
businesses that do rank higher locally.

I built a tool that auto-responds in 30 seconds. Looking for 3 
businesses to test free for 14 days.

Worth a chat?
```

---

## 📱 CONTENT IDEAS

### LinkedIn Posts (Post 3x/week)

**Post 1: Problem Awareness**
```
80% of local businesses are losing customers to competitors.

Not because of bad service. Not because of high prices.

Because they don't respond to Google reviews.

Google's algorithm prioritizes businesses that engage with customers.
No responses = lower ranking = fewer customers.

The fix? Respond to every review within 24 hours.

Problem: Most business owners don't have time.

Solution: Automation.

[Link to ReviewPilot]
```

**Post 2: Social Proof**
```
"We went from responding to 20% of reviews to 100%.
Local SEO ranking improved by 40% in 2 weeks.
New customers up by 23%."

This is what happens when you automate review responses.

ReviewPilot handles it in 30 seconds per review.
No more forgetting. No more manual writing.

[Link to case study]
```

**Post 3: How-To**
```
How to respond to Google reviews (the right way):

1. Thank the reviewer by name
2. Mention something specific from their review
3. Invite them back
4. Keep it under 100 words

Example:
"Hi John, thanks for the 5 stars! So glad you enjoyed the 
[specific service]. See you next time! - The Team"

OR: Just use ReviewPilot and let AI write it for you. 
30 seconds vs 5 minutes. Your choice.

[Link to ReviewPilot]
```

---

## 🎯 SUCCESS METRICS

### Week 1 Goals
- [ ] MVP built and working
- [ ] Landing page live
- [ ] 50 outreach emails sent
- [ ] 3 trial customers onboarded

### Week 2 Goals
- [ ] 2 trial customers converted to paid
- [ ] 1 testimonial collected
- [ ] 100 total outreach emails sent

### Week 3 Goals
- [ ] 5 total paying customers
- [ ] £500/month recurring revenue
- [ ] V2 features launched

### Week 4 Goals
- [ ] 10 total paying customers
- [ ] £1,000/month recurring revenue ✅
- [ ] 3 case studies published

---

## ⚠️ RISKS & MITIGATION

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Google API changes | Low | High | Use official API only, monitor changelog |
| AI responses sound generic | Medium | Medium | Customize prompts, allow tone settings |
| Customers don't see value | Low | High | Show metrics weekly, prove ROI |
| Competitors copy idea | Medium | Low | First-mover advantage, focus on service |
| Churn after 3 months | Medium | Medium | Continuous value (analytics, reports) |

---

## 🏁 NEXT BUILD STEP

**Start with this (Day 1):**

1. Create Google Cloud Project
2. Enable Google Business Profile API
3. Get API credentials
4. Test polling for reviews manually

**Code skeleton:**
```python
# review_pilot.py
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def poll_reviews(account_id):
    service = build('mybusiness', 'v4', credentials=creds)
    reviews = service.accounts().locations().reviews().list(
        parent=f'accounts/{account_id}/locations/ALL'
    ).execute()
    return reviews

def generate_response(review_text, stars, business_name):
    # Call Claude API
    response = claude.generate(
        prompt=f"Write a professional Google review response for {business_name}. Review: {review_text}. Rating: {stars}/5. Under 100 words."
    )
    return response

def send_approval_email(customer_email, review, response_draft):
    # Send email via Gmail API
    pass

# Run every 6 hours
if __name__ == "__main__":
    reviews = poll_reviews(ACCOUNT_ID)
    for review in reviews['reviews']:
        if not review.get('responded'):
            draft = generate_response(review['text'], review['starRating'], BUSINESS_NAME)
            send_approval_email(CUSTOMER_EMAIL, review, draft)
```

---

**Ready to build?** Start with the MVP workflow above. First customer in 7 days. £1,000/month in 30 days. 🚀
