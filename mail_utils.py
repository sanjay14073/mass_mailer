import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

from dotenv import load_dotenv
load_dotenv()
def send_mail(receiver_email):
        subject = "An email with attachment from Python"
        body = "This is an email from Python"
        sender_email = os.getenv("SENDER_MAIL")
        receiver_email = receiver_email
        password = os.getenv("SENDER_APP_PASSWORD")


        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email  


        message.attach(MIMEText(body, "plain"))

        text = message.as_string()

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)