🤖 AI API Integration Project
📌 Overview

This project demonstrates how to integrate and work with multiple Generative AI APIs using Python. The goal is to understand how different AI providers operate and how to interact with them programmatically.

The project includes implementations for:

Groq (Llama models)
Cohere (Command model)
Hugging Face (Inference API)
Google Gemini
Ollama (Local LLM)

🎯 Objectives
Learn how to use API keys securely
Integrate multiple AI services
Send prompts and receive responses
Handle API errors gracefully
Build modular Python programs
🛠️ Technologies Used
Python
REST APIs
VS Code
Git & GitHub

Libraries used:

groq
requests
google-generativeai / google-genai
cohere
python-dotenv
📂 Project Structure

ai-api-integration/
│
├── groq_example.py
├── ollama_example.py
├── huggingface_example.py
├── gemini_example.py
├── cohere_example.py
├── multi_api_query.py
├── requirements.txt
├── README.md
│
└── screenshots/
  ├── groq_output.png
  ├── cohere_output.png
  ├── huggingface_output.png
  ├── gemini_output.png
  └── ollama_output.png

⚙️ Setup Instructions
1. Clone the Repository

cd ai-api-integration

2. Install Dependencies

pip install -r requirements.txt

3. Set Up Environment Variables

Create a .env file and add your API keys:

GROQ_API_KEY=groq_key
HUGGINGFACE_API_KEY=hf_key
GOOGLE_API_KEY=gemini_key
COHERE_API_KEY=cohere_key


▶️ How to Run

Run any file using:

python groq_example.py
python cohere_example.py
python huggingface_example.py
python gemini_example.py
python ollama_example.py

Each program sends a prompt to the respective API and prints the response.

✨ Features
Multiple AI API integrations
Secure API key handling using .env
Error handling with try-except
Clean and modular code
Easy-to-run scripts
📸 Screenshots

Screenshots of outputs are included in the screenshots folder.

⚠️ Notes
API keys are not hardcoded
Free-tier limits may apply
Ollama requires local setup

🚀 Conclusion

This project demonstrates how to integrate different AI APIs and helps in building a strong foundation for real-world AI applications.

👨‍💻 Author

Prerana V.U.