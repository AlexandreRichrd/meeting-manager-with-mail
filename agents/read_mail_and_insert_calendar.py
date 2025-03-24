import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from tools.mail_tool import email_fetching


load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")

# Initialisation du model
chat_model = ChatMistralAI(
        model="mistral-large-latest",
        api_key=api_key,
        temperature=0.1
    )

# Enumération des tools pour l'agent
tools = [email_fetching]


# memory = MemorySaver()

# Fonction de création de l'agent
def create_email_agent():
    agent = create_react_agent(chat_model, tools)
    return agent

