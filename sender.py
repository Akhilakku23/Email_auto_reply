
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from config import EMAIL, PASSWORD

def send_reply(to_email, reply_body, subject=None):
    """Send an email reply safely with UTF-8 encoding"""
    reply_subject = "Re: " + (subject if subject else "")
    
    # Create MIMEText object with UTF-8 encoding
    msg = MIMEText(reply_body, "plain", "utf-8")
    msg["From"] = EMAIL
    msg["To"] = to_email
    msg["Subject"] = Header(reply_subject, "utf-8")
    
    # Send via SMTP_SSL
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, to_email, msg.as_string())
        print(f"Replied to {to_email}")
