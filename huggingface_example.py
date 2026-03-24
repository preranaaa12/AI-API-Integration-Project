import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

def query_hf(prompt):
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        return response.json()[0]["generated_text"]
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    prompt = input("Enter the prompt: ")
    print("Response:")
    print(query_hf(prompt))
