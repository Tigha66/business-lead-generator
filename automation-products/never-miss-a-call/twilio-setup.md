# Twilio Setup Guide

## 1. Create Twilio Account

1. Go to: https://www.twilio.com/
2. Sign up with email (free trial includes $15 credit)
3. Verify phone number

## 2. Get Phone Number

1. Go to: https://console.twilio.com/us/develop/sms/phone-numbers
2. Click "Get a Twilio Phone Number"
3. Search for your area code
4. Select a number ($1/month)

## 3. Get Credentials

From Console: https://console.twilio.com/

```
Account SID: ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Auth Token: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Phone Number: +1234567890
```

## 4. Save Credentials

Save to `.env` file:
```bash
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=+1234567890
```

## 5. Test SMS

```python
from twilio.rest import Client

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Test message from Never Miss A Call!",
    from_='+1234567890',
    to='+1987654321'
)

print(message.sid)
```

## 6. SMS Costs

| Usage | Cost |
|-------|------|
| Incoming SMS | $0.0075 each |
| Outgoing US SMS | $0.0075 each |
| Outgoing International | $0.02-0.15 each |
| Phone Number | $1.00/month |

## 7. Compliance

- **TCPA**: Always include opt-out: "Reply STOP to unsubscribe"
- **Business Hours**: Don't send before 8am or after 9pm local time
- **Consent**: Get verbal/written consent before automating

---

## Troubleshooting

### "Message not delivered"
- Check phone number format (+1XXXXXXXXXX)
- Verify account balance
- Check Twilio console for errors

### "Number not verified"
- Verify your own number in Twilio console
- Trial accounts can only send to verified numbers

### Webhook not firing
- Check URL is HTTPS (required by Twilio)
- Verify webhook URL is accessible
- Check Twilio debugger for errors

---

*Guide created: 2026-03-15*