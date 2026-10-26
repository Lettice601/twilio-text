from keys import acc_id, api_key
from twilio.rest import Client

client = Client(acc_id, api_key)

message = client.messages.create(
    body="sms_2fa",
    to = "+12508954841",
    from_="+17372508034"
    )

print(message.sid)