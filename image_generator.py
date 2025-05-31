import os
import requests
import base64
from dotenv import load_dotenv

load_dotenv()
STABILITY_API_KEY = os.getenv("STABILITY_API_KEY")

def generate_image(prompt):
    engine_id = "stable-diffusion-v1-6"
    url = f"https://api.stability.ai/v1/generation/{engine_id}/text-to-image"

    headers = {
        "Authorization": f"Bearer {STABILITY_API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    json_data = {
        "text_prompts": [{"text": prompt}],
        "cfg_scale": 7,
        "height": 512,
        "width": 512,
        "samples": 1,
        "steps": 30
    }

    response = requests.post(url, headers=headers, json=json_data)

    if response.ok:
        data = response.json()
        image_data = data["artifacts"][0]["base64"]
        return f"data:image/png;base64,{image_data}"
    else:
        raise Exception(f"Stability AI Error: {response.status_code} {response.text}")
