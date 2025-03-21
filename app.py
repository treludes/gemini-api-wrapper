from flask import Flask, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os
import pkg_resources

# Load environment variables
load_dotenv()

app = Flask(__name__)

# ✅ Force the SDK to use v1 and REST
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY"),
    transport="rest",
    client_options={"api_endpoint": "https://generativelanguage.googleapis.com/v1"},
)
print("📦 google-generativeai version:", pkg_resources.get_distribution("google-generativeai").version)
print("Gemini configured. Using endpoint: https://generativelanguage.googleapis.com")

# ✅ Use full model name required for v1
model = genai.GenerativeModel(model_name="models/gemini-pro")

@app.route('/generate-content', methods=['POST'])
def generate_content():
    print("🛬 /generate-content endpoint hit!")

    try:
        data = request.get_json(force=True)  # <- force JSON parsing
        print("📥 Raw data:", data)

        prompt = data.get("prompt", "")

        if not prompt:
            print("⚠️ No prompt provided!")
            return jsonify({"error": "No prompt provided"}), 400

        print("🚀 Prompt sent to Gemini:", prompt)
        response = model.generate_content(prompt)
        print("✅ Gemini response:", response.text)

        return jsonify({"response": response.text}), 200

    except Exception as e:
        print("❌ Exception caught:", str(e))
        return jsonify({"error": str(e)}), 500


@app.route('/')
def home():
    return jsonify({"message": "Gemini API is live. Use POST /generate-content"})

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
