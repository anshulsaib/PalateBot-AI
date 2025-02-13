import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Retrieve the API key securely
HUGGING_FACE_API_KEY = os.getenv("API_KEY")

# Ensure the API key is not None
if HUGGING_FACE_API_KEY is None:
    raise ValueError("HUGGING_FACE_API_KEY is not set. Check your .env file.")

API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}

def generate_restaurant_name():
    prompt = "Suggest three unique and creative names for a fancy Indian restaurant."

    data = {
        "inputs": prompt,
        "parameters": {
            "temperature": 0.9,
            "top_p": 0.95,
            "max_new_tokens": 50,
            "do_sample": True
        }
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        print("Suggested Restaurant Names:", result[0]['generated_text'])
    else:
        print("Error:", response.json())

if __name__ == "__main__":
    generate_restaurant_name()
