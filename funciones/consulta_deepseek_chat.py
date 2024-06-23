from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave API desde las variables de entorno
api_key = os.getenv("DEEPSEEK_TOKEN")
from langchain_openai import ChatOpenAI

def consulta_simple(consulta):
    llm = ChatOpenAI(
        model='deepseek-chat', 
        openai_api_key=api_key, 
        openai_api_base='https://api.deepseek.com',
        max_tokens=1024
    )

    response = llm.invoke(consulta)
    return(response.content)

