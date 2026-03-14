# Legal Compliance Guide

## CAN-SPAM Act (United States)

The CAN-SPAM Act sets rules for commercial email. Violations can result in fines up to $50,120 per email.

### Requirements

1. **Don't use false or misleading header information**
   - From, To, Reply-To must accurately identify the sender
   - Domain must be yours

2. **Don't use deceptive subject lines**
   - Subject must reflect the content of the message

3. **Identify the message as an ad**
   - Must be clear and conspicuous that this is advertising

4. **Include your physical postal address**
   - Must include a valid physical address
   - Can be street address, PO box, or registered CMRA

5. **Tell recipients how to opt-out**
   - Clear and conspicuous explanation of how to unsubscribe
   - Must be able to process opt-out requests for 30 days after sending

6. **Honor opt-out requests promptly**
   - Must process within 10 business days
   - Cannot charge a fee or require additional info beyond email address
   - Cannot make recipient go through anything other than a web page or email

### Best Practices

- Keep records of consent and opt-outs
- Use double opt-in when possible
- Monitor bounce rates (keep under 5%)
- Use email authentication (SPF, DKIM, DMARC)
- Warm up new email accounts gradually

## GDPR (European Union)

If contacting EU businesses, GDPR applies.

### Key Requirements

1. **Lawful basis for processing**
   - Legitimate interest may apply for B2B
   - Must document your lawful basis

2. **Right to be informed**
   - Privacy notice must be provided
   - Explain how you'll use their data

3. **Right to object**
   - Must honor opt-out immediately
   - Cannot continue processing after objection

4. **Data minimization**
   - Only collect what you need
   - Don't store longer than necessary

### B2B Exception

GDPR is more flexible for B2B communications:
- Can contact corporate email addresses (info@, sales@)
- Personal email addresses (name@company.com) require more care
- Always provide opt-out mechanism

## UK GDPR & PECR

Post-Brexit UK has similar rules:

- PECR requires consent for marketing emails to individuals
- B2B marketing to corporate subscribers is more flexible
- Still must provide opt-out mechanism

## Email Authentication

### SPF (Sender Policy Framework)
- DNS record listing authorized sending servers
- Prevents spoofing

### DKIM (DomainKeys Identified Mail)
- Cryptographic signature on emails
- Proves email wasn't tampered with

### DMARC
- Policy for handling SPF/DKIM failures
- Provides reporting on email authentication

## Practical Checklist

Before sending:

- [ ] Email account is properly authenticated (SPF, DKIM, DMARC)
- [ ] Physical address included in email footer
- [ ] Clear unsubscribe mechanism in every email
- [ ] Subject line accurately reflects content
- [ ] Recipient list is cleaned (remove bounces)
- [ ] Rate limiting is in place (max 50/hour for new accounts)
- [ ] Opt-out tracking system is working
- [ ] Privacy policy is accessible

## Sample Compliant Footer

```
---
{{Sender Name}}
{{Company Name}}
{{Street Address}}
{{City, State, ZIP}}
{{Country}}

To unsubscribe from future emails, reply with "UNSUBSCRIBE" or click here: [Unsubscribe Link]

Privacy Policy: [Link to Privacy Policy]
```

## Record Keeping

Maintain records of:
- When emails were sent
- To whom
- Content of emails
- Opt-out requests and when processed
- Bounce notifications

Retention: Minimum 3 years recommended

## Penalties

- CAN-SPAM: Up to $50,120 per violation
- GDPR: Up to €20 million or 4% of annual revenue
- UK GDPR: Similar to EU GDPR

## When in Doubt

1. Consult with a legal professional
2. Start with small test batches
3. Monitor complaint rates
4. Be transparent and honest
5. Respect opt-outs immediately

## Resources

- FTC CAN-SPAM Guide: https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business
- ICO B2B Marketing: https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-privacy-and-electronic-communications-regulations/direct-marketing/
- GDPR.eu: https://gdpr.eu/

---

**Disclaimer:** This is informational guidance, not legal advice. Consult with a qualified attorney for your specific situation.
