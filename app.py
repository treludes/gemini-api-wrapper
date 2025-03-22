from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# v1beta endpoint for text-bison-001
API_KEY = os.getenv("GEMINI_API_KEY")
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/chat-bison-001:generateContent?key={API_KEY}"



HEADERS = {
    "Content-Type": "application/json"
}


@app.route("/generate-content", methods=["POST"])
def generate_content():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "")

        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400

        payload = {
            "contents": [
                {
                    "parts": [{"text": prompt}]
                }
            ]
        }

        print("🚀 Sending prompt:", prompt)

        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()

        result = response.json()
        print("✅ Gemini response:", result)

        # Extract response text safely
        text = result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
        return jsonify({"response": text})

    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return jsonify({"message": "Gemini v1beta (text-bison-001) API is live!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
