# Mail & Calendar Agent (LangChain + mail IMAP + Langfuse)

Un agent intelligent capable de :
- Lire les e-mails non lus depuis une boîte mail (via IMAP)
- Résumer leur contenu avec un LLM (Mistral via LangChain)
- Orchestrer les outils avec LangGraph
- Tracer toutes les interactions via Langfuse

---

## Stack technique

- LangChain + LangGraph
- imaplib pour la récupération des e-mails
- MistralAI (via langchain-mistralai)
- Langfuse pour l'observation des runs
- python-dotenv pour la gestion des secrets
- Python 3.10+

---

## Installation

### 1. Cloner le projet et créer un environnement virtuel

```bash
git clone <repo-url>
cd mail-calendar
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Remplir le fichier `.env`

```env
# Connexion email
EMAIL_ACCOUNT=ton.email@tondomaine.com
PASSWORD=ton_mot_de_passe
IMAP_SERVER=serveur imap du mail ex: imap.mail.ovh.net

# MistralAI
MISTRAL_API_KEY=ta_clé_api

# Langfuse (local ou cloud)
LANGFUSE_PUBLIC_KEY=ta_clé_publique
LANGFUSE_SECRET_KEY=ta_clé_secrète
LANGFUSE_HOST=http://localhost:3000
```

### 3. Lancer Langfuse en local (optionnel)

```bash
docker run -p 3000:3000 langfuse/langfuse:latest
```

---

## Utilisation

```bash
python config.py
```

Ce script :
- Crée un agent LangGraph
- Récupère les e-mails non lus
- Résume leur contenu
- Trace toute l'exécution dans Langfuse

---

## Structure du projet

```
mail-calendar/
├── agents/
│   └── read_mail_and_insert_calendar.py   # Création de l'agent LangGraph
├── services/
│   └── mail_service.py                    # Connexion et lecture des e-mails
├── tools/
│   └── mail_tool.py                       # Tool LangChain pour les mails
├── config.py                              # Script de lancement principal
├── .env                                   # Variables d’environnement (non versionné)
├── requirements.txt
└── README.md
```

---

## Prochaines fonctionnalités

- Détection de rendez-vous dans les mails
- Ajout automatique au calendrier (Google Calendar, Outlook)
- Mémoire longue durée (ex: vectorstore)
- Interface utilisateur (ex: Streamlit)

---

## Auteur

Développé par Alexandre RICHARD, propulsé par LangChain, Mistral et un peu de caffeine.
