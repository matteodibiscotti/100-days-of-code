import smtplib
import os

sender_email = '<your email here>'
recipient_email = '<recipient email here>'
app_password = os.getenv('GMAIL_APP_PASSWORD')
smtp_server = 'smtp.gmail.com'
email_subject = ""
email_body = "content here"

connection = smtplib.SMTP(smtp_server)
connection.starttls()
connection.login(user=sender_email, password=app_password)


connection.sendmail(from_addr=sender_email, to_addrs=recipient_email, msg=email_body)
connection.close()


'''
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content('This is my message')

msg['Subject'] = 'Subject'
msg['From'] = "me@gmail.com"
msg['To'] = "you@gmail.com"

# Send the message via our own SMTP server.
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("me@gmail.com", "password")
server.send_message(msg)
server.quit()
'''