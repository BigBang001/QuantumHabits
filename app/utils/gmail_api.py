# app/utils/gmail_api.py

import os
import base64
from google.oauth2 import service_account
from googleapiclient.discovery import build
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Google API credentials setup
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
SERVICE_ACCOUNT_FILE = 'path_to_your_service_account_json_file.json'  # Update with your service account file
EMAIL_ADDRESS = 'your_email@gmail.com'  # Update with your Gmail address

def create_service():
    """Creates a Google API service."""
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    delegated_credentials = credentials.with_subject(EMAIL_ADDRESS)
    service = build('gmail', 'v1', credentials=delegated_credentials)
    return service

def send_email(receiver_email, subject, message_text):
    """Sends an email using Gmail API."""
    service = create_service()
    email_msg = create_message(EMAIL_ADDRESS, receiver_email, subject, message_text)
    send_message(service, EMAIL_ADDRESS, email_msg)

def create_message(sender, to, subject, message_text):
    """Creates a message for sending."""
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    msg = MIMEText(message_text)
    message.attach(msg.as_string())
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw}

def send_message(service, user_id, message):
    """Sends a message."""
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()
        print(f"Message Id: {message['id']}")
        return message
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
if __name__ == '__main__':
    receiver_email = 'recipient@example.com'
    subject = 'Test Email'
    message_text = 'Hello, this is a test email sent from QuantumHabits!'
    send_email(receiver_email, subject, message_text)
