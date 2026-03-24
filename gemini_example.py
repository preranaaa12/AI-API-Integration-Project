import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def query_gemini(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash-001",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    prompt = input("Enter the prompt: ")
    print("Response:")
    print(query_gemini(prompt))
