from firebase_admin import credentials, messaging
import os
from datetime import datetime, timedelta

cred = credentials.Certificate({
  "type": "service_account",
  "project_id": os.environ.get("PROJECT_ID"),
  "private_key_id": os.environ.get("PRIVATE_KEY_ID"),
  "private_key": os.environ.get("PRIVATE_KEY").replace("\\n", "\n"),
  "client_email": os.environ.get("CLIENT_EMAIL"),
  "client_id": os.environ.get("CLIENT_ID"),
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": os.environ.get("CLIENT_X509_CERT_URL"),
})

firebase_admin.initialize_app(cred)

def generate_notification_options():
    return messaging.AndroidConfig(
        priority='high',
        ttl=datetime.utcnow() + timedelta(days=1)
    )

def send_message_to_token(token, notification, options):
    message = messaging.Message(
        notification=notification,
        token=token,
        android=options
    )
    return messaging.send(message)

def send_message_to_topic(topic, notification, options):
    message = messaging.Message(
        notification=notification,
        topic=topic,
        android=options
    )
    return messaging.send(message)