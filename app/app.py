import os
from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path="./.env")

# Safely initialize OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key, base_url="https://api.openai.com/v1") if api_key else None

app = Flask(__name__)

@app.get("/")
def home():
    return "LLM Q&A chatbot is alive", 200

@app.post("/chat")
def chat():
    if not client:
        return jsonify({"error": "OpenAI API key not configured"}), 500

    data = request.get_json(force=True)
    q = (data.get("question") or "").strip()
    if not q:
        return jsonify({"error": "field 'question' required"}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": q}],
            max_tokens=256,
            temperature=0.7,
        )
        return jsonify({"AI CHAT REPLY": response.choices[0].message.content.strip()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_ENV") == "development"
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)  # nosec B104
