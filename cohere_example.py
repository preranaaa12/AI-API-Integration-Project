import os
import cohere
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))

def query_cohere(prompt):
    try:
        response = co.generate(
            model="command",
            prompt=prompt,
            max_tokens=200
        )
        return response.generations[0].text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    prompt = input("Enter prompt: ")
    print(query_cohere(prompt))
