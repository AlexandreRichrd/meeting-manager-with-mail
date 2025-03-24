from agents.read_mail_and_insert_calendar import create_email_agent
from langchain_core.messages import HumanMessage
from uuid import uuid4
from langfuse.callback import CallbackHandler
from dotenv import load_dotenv
import os
from langchain_core.messages import AIMessage

load_dotenv()

# Initialisation du callback handler
langfuse_handler = CallbackHandler(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST")
)

# Création d'un agent
agent = create_email_agent()

# Initialisation des paramètres
initial_state = {
    "messages": [HumanMessage(content="Peux-tu lire me résumer mes mails non lus ?")]
}

# Paramètres supplémentaires pour Langfuse
config = {
    "configurable": {
        "thread_id": str(uuid4())
    },
    "callbacks": [langfuse_handler] # Callbacks pour Langfuse
}

# Exécution de l'agent
response = agent.invoke(initial_state, config=config)

# Affichage de la dernière réponse du LLM uniquement
messages = response["messages"]
final_response = next((m.content for m in reversed(messages) if isinstance(m, AIMessage)), None)

print("\nRéponse de l'agent :\n")
print(final_response)