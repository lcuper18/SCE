import requests
import json
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave API desde las variables de entorno
api_key = os.getenv("DEEPSEEK_TOKEN")

# Set the authentication header
headers = {
    "Authorization": f"Bearer {api_key}"
}

# Make the API request
response = requests.get("https://api.deepseek.com/user/balance", headers=headers)

# Check the response status code
if response.status_code == 200:
    # Request was successful
    data = json.loads(response.content)
    balance_info = data["balance_infos"][0]
    print(f"Moneda: {balance_info['currency']}")
    print(f"Total Saldo: {balance_info['total_balance']}")
else:
    # Request failed
    print(f"Error: {response.status_code} - {response.text}")
