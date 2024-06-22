"""import requests

# Set the API key
api_key = "sk-0e744d4661ee49489792adb2f50be149"

# Set the authentication header
headers = {
    "Authorization": f"Bearer {api_key}"
}

# Make the API request
response = requests.get("https://api.deepseek.com/user/balance", headers=headers)

# Check the response status code
if response.status_code == 200:
    # Request was successful
    print(response.content)
else:
    # Request failed
    print(f"Error: {response.status_code} - {response.text}")
"""

import requests
import json

# Set the API key
api_key = "sk-0e744d4661ee49489792adb2f50be149"

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
