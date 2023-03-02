import smtplib
from email.message import EmailMessage
import os

def send_email(price, item, price_direction):
    sender_email = '<your email here>'
    recipient_email = '<recipient email here>'
    app_password = os.getenv('GMAIL_APP_PASS')
    smtp_server = 'smtp.gmail.com'
    email_subject = "test"
    email_body = f'The price of {item} has {price_direction} to {price}'

    msg = EmailMessage()
    msg.set_content(email_body)

    msg['Subject'] = email_subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    connection = smtplib.SMTP(smtp_server)
    connection.starttls()
    connection.login(user=sender_email, password=app_password)

    connection.send_message(msg)
    connection.close()