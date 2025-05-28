from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["10 per minute"]
)


# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/summarize", methods=["POST"])
@limiter.limit("5 per minute")

def summarize():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        # Stronger Gen Z Banglish prompt
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.7,
            messages=[
                {
                    "role": "system",
                    "content": (
    "You are a summarizer.\n"
    "You will receive long Facebook posts written in Bangla-English mix.\n"
    "Your job is to write a brief summary — 1 or 2 sentences — that clearly explains what the post is about.\n\n"
    "👉 Use natural Gen Z Banglish — mix English and Bengali like people in Dhaka do when texting.\n"
    "👉 Don’t write in first-person ('ami', 'amar') — you're not the poster.\n"
    "👉 No overexplaining, no full story — just the situation.\n\n"
    "✅ Examples:\n"
    "- 'GF AI chatbot er sathe weird sexting e ase. Vibe off, poster confused eta cheating kina.'\n"
    "- 'Relationship e ase but still onno meyeder niye comment kore — conflict ashche.'\n"
    "- 'Main kotha holo: trust niye issue hoise, karon ekjon onno manusher sathe closeness feel kortese.'\n\n"
    "Keep it chill, clean, and Banglish. Use words like: vibe off, onek confused, cheating-type situation, trust-er issue, etc."
)





                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )

        summary = response.choices[0].message.content.strip()

        # Fun BS score calculation
        drama_keywords = ["drama", "toxic", "cheated", "ghosted", "fake", "red flag", "gaslight", "lie", "cry"]
        drama_count = sum(text.lower().count(word) for word in drama_keywords)
        bs_score = min(100, len(text) // 10 + drama_count * 5)

        return jsonify({
            "summary": summary,
            "bs_score": bs_score
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
