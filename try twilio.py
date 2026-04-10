from twilio.rest import Client

account_sid = "ACcef9cf6cf67303647a5a4fb19eae2250"
auth_token = "9731abb52d09a4e54d73c0ddea4e4316"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Test SMS from Twilio",
    from_="+17407574886",
    to="+918904636823"
)

print(message.sid)