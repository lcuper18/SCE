from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variables
api_key = os.getenv("DEEPSEEK_TOKEN")
if not api_key:
    raise ValueError("DEEPSEEK_TOKEN no está configurado en el archivo .env")

def consulta_simple(consulta):
    try:
            # Initialize the ChatOpenAI model with the DeepSeek configuration
        llm = ChatOpenAI(
            model='deepseek-chat',
            openai_api_key=api_key,
            openai_api_base='https://api.deepseek.com',
            max_tokens=1024
    )

        # Invoke the model with the provided query
        response = llm.invoke(consulta)
        return response.content

    except Exception as e:
        # Handle any exceptions that occur during the API call
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    query = "Hola, como estas? que eres y como te llamas?"
    response = consulta_simple(query)
    if response:
        print(response)
    else:
        print("No se pudo obtener una respuesta.")
