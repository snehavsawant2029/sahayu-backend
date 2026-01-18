import os
import ssl
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
SMTP_TO = os.getenv("SMTP_TO") or SMTP_USER

def send_contact_email(name: str, email: str, subject: str, message: str):
    body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SMTP_USER
    msg['To'] = SMTP_TO

    context = ssl.create_default_context()

    # Use STARTTLS on port 587 instead of SSL on 465
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as server:
        server.starttls(context=context)  # Upgrade to secure TLS
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(SMTP_USER, SMTP_TO, msg.as_string())