import imaplib
import email
from config import EMAIL, PASSWORD

def read_unread_emails():
    """Fetch unread emails from Gmail inbox"""
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")
    
    status, messages = mail.search(None, 'UNSEEN')
    email_ids = messages[0].split()
    
    unread_emails = []
    for e_id in email_ids:
        status, msg_data = mail.fetch(e_id, '(RFC822)')
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)
        sender = msg['From']
        subject = msg['Subject']
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    break
        else:
            body = msg.get_payload(decode=True).decode()
        
        unread_emails.append((sender, subject, body))
    
    mail.logout()
    return unread_emails
