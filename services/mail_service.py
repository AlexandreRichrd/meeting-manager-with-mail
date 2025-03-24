import imaplib
import email
from email.header import decode_header
import os
from dotenv import load_dotenv

def load_env():
    load_dotenv()
    return (
        os.getenv("EMAIL_ACCOUNT"),
        os.getenv("PASSWORD"),
        os.getenv("IMAP_SERVER"),
    )

def connect_mail_server(imap_server, email_account, password):
    try:
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(email_account, password)
        print("✅ Connexion IMAP réussie.")
        return mail
    except Exception as e:
        print(f"❌ Erreur de connexion IMAP : {e}")
        return None

def decode_txt(text, encoding):
    if isinstance(text, bytes):
        return text.decode(encoding if encoding else 'utf-8', errors='ignore')
    return text

def fetch_unread_emails(mail, limit=5):
    emails = []
    try:
        mail.select("INBOX")
        status, messages = mail.search(None, "UNSEEN")
        email_ids = messages[0].split()

        if not email_ids:
            print("📭 Aucun e-mail non lu.")
            return emails

        for e_id in email_ids[:limit]:
            status, msg_data = mail.fetch(e_id, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject, encoding = decode_header(msg.get("Subject"))[0]
                    subject = decode_txt(subject, encoding)
                    from_ = msg.get("From")

                    body = ""
                    if msg.is_multipart():
                        for part in msg.walk():
                            if part.get_content_type() == "text/plain" and part.get("Content-Disposition") is None:
                                body = part.get_payload(decode=True).decode("utf-8", errors="ignore")
                                break
                    else:
                        body = msg.get_payload(decode=True).decode("utf-8", errors="ignore")

                    emails.append({
                        "from": from_,
                        "subject": subject,
                        "body": body.strip()
                    })
    except Exception as e:
        print(f"❌ Erreur pendant la récupération : {e}")
    return emails