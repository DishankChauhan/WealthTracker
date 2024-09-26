import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

def send_notification(balance):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_number = os.getenv('TWILIO_FROM_NUMBER')
    your_number = os.getenv('YOUR_PHONE_NUMBER')

    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body=f"Your current HDFC account balance is ₹{balance:.2f}",
            from_=twilio_number,
            to=your_number
        )
        print(f"Notification sent successfully. SID: {message.sid}")
    except Exception as e:
        print(f"Error sending notification: {e}")