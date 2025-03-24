from langchain_core.tools import tool
from services.mail_service import load_env, connect_mail_server, fetch_unread_emails

@tool
def email_fetching() -> str:
    """Fetch unread emails and return them"""
    email_account, password, imap_server = load_env()
    if not all([email_account, password, imap_server]):
        return "⚠️ Infos manquantes dans le fichier .env"

    mail = connect_mail_server(imap_server, email_account, password)
    if not mail:
        return "❌ Impossible de se connecter au serveur mail."

    emails = fetch_unread_emails(mail, limit=3)
    mail.logout()

    if not emails:
        return "📭 Aucun e-mail non lu."

    output = ""
    for i, e in enumerate(emails, 1):
        output += (
            f"📧 Email {i}\n"
            f"👤 De     : {e['from']}\n"
            f"📝 Sujet  : {e['subject']}\n"
            f"📄 Extrait:\n{e['body'][:300]}...\n\n"
        )

    return output