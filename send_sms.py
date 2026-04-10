"""
SMS alert module using Twilio REST API.

Setup:
1. Sign up at https://www.twilio.com
2. Get your Account SID, Auth Token and a Twilio phone number
3. Replace the placeholder values below (or set as environment variables)
"""
import os
from twilio.rest import Client

# Load from environment variables or replace with your actual credentials
ACCOUNT_SID = "ACcef9cf6cf67303647a5a4fb19eae2250"
AUTH_TOKEN = "9731abb52d09a4e54d73c0ddea4e4316"


def send_sms(message: str) -> str:
    """
    Send an SMS via Twilio.

    Args:
        message: The message body to send

    Returns:
        Twilio message SID on success
    """
    if "YOUR_TWILIO" in ACCOUNT_SID:
        print(f"[send_sms] DEMO MODE — SMS would be sent: {message}")
        return "DEMO_SID"

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    msg = client.messages.create(
        body=message,
        from_="+17407574886",
        to="+918904636823"
    )
    print(f"[send_sms] SMS sent. SID: {msg.sid}")
    return msg.sid