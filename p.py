import os
import requests
from dotenv import load_dotenv

load_dotenv()
STABILITY_API_KEY = os.getenv("STABILITY_API_KEY")

url = "https://api.stability.ai/v1/engines/list"
headers = {
    "Authorization": f"Bearer {STABILITY_API_KEY}"
}

response = requests.get(url, headers=headers)

if response.ok:
    engines = response.json()
    print("Available Engines:")
    for engine in engines:
        print("-", engine["id"])
else:
    print("Error:", response.status_code, response.text)
