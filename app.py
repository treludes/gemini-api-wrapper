from flask import Flask, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# ✅ Set up Gemini configuration (for v1)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ Explicitly create a Gemini model (v1)
model = genai.GenerativeModel(model_name="models/gemini-pro")

@app.route('/generate-content', methods=['POST'])
def generate_content():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "")

        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400

        response = model.generate_content(prompt)

        return jsonify({"response": response.text}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render sets $PORT automatically
    app.run(host='0.0.0.0', port=port)

