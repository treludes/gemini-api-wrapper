# Gemini API Wrapper

A simple REST API that wraps the Google Gemini Generative AI model (`gemini-pro`) using Flask.

## 🚀 Quick Start

1. Clone the repo
2. Add your Gemini API key to `.env`:
   ```
   GEMINI_API_KEY=your_key_here
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the server:
   ```
   python app.py
   ```

## 🧪 Usage

POST to `/generate-content` with:
```json
{
  "prompt": "Give me a business idea involving AI and health"
}
```

## 📌 Notes

Free Gemini API keys available via: https://aistudio.google.com/app/apikey
