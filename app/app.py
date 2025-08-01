import os
from flask import Flask, request, jsonify
from openai import OpenAI      # NEW import
from dotenv import load_dotenv


load_dotenv(dotenv_path="./.env")  # explicitly load
print(f"OPENAI_API_KEY in container: '{os.getenv('OPENAI_API_KEY')}'")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"),base_url="https://api.openai.com/v1")

app = Flask(__name__)


@app.get("/")
def home():
    return "LLM Q&A chatbot is alive", 200


@app.post("/chat")
def chat():
    data = request.get_json(force=True)
    q = (data.get("question") or "").strip()
    if not q:
        return jsonify({"error": "field 'question' required"}), 400

    response = client.chat.completions.create(   # NEW style
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": q}],
        max_tokens=256,
        temperature=0.7,
    )
    return jsonify({"AI CHAT REPLY": response.choices[0].message.content.strip()}), 200

if __name__ == "__main__":
    # debug_mode = os.getenv("FLASK_ENV") == "development"
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)

