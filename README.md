# 🧠 BS Detector — Facebook Drama Summarizer in Gen Z Banglish

BS Detector is a fun and brutally honest Chrome extension that summarizes long, emotional Facebook group posts (like "Are We Dating the Same Guy?") into short, Gen Z-style Banglish summaries. It also gives each post a BS Meter 💩 score that reflects the drama level.

No more scrolling through ajaira post. Just read the vibe and bounce.

---

## 🧩 Features

- 🧠 One-click summary of long posts
- 🌍 Gen Z Banglish tone — casual, real, and local
- 💩 BS Meter: Detects overdrama, emotional chaos, and exaggeration
- ⚡ Works automatically on Facebook group posts
- 🔒 Powered by OpenAI GPT API (via your own key)

---

## 🧑‍💻 How to Use? For Chrome:

1. Download the latest release
2. Go to chrome://extensions
3. Turn on developer mode
4. click on load unpacked
5. Select the folder you have just downloaded
6. Done!

### 1. Clone the Project

bash
git clone https://github.com/shamratneero/bs-detector-AWDSGD.git
cd bs-detector-AWDSGD
`

---

### 2. Load the Chrome Extension

1. Go to `chrome://extensions`
2. Turn on Developer Mode
3. Click "Load unpacked"
4. Select the root folder (where `manifest.json` is)
5. Visit a Facebook group like "Are We Dating the Same Guy - Dhaka"
6. Scroll to any long post — you'll see a "🧠 Summarize BS?" button

---

### 3. Set Up the Flask Backend

#### 🔧 Requirements

* Python 3.9+
* OpenAI API key

#### 📦 Install Dependencies

bash
cd backend
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
pip install -r requirements.txt


#### 🔐 Create a `.env` file


OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx


> ⚠️ Never commit this file to GitHub!

#### ▶️ Run the Server


python app.py


Your Flask backend will run at `http://127.0.0.1:5000`.

---

### 4. Using the Extension

When browsing a Facebook group, long posts will automatically get a 🧠 Summarize BS? button below them.

Click it to get:

* A Banglish summary in 1–2 lines
* A BS Meter score (0–100 💩)

---

## 🔧 Optional: Deploy the Backend

If you want to make the extension work without `localhost`, deploy the backend using [Railway](https://railway.app) or [Render](https://render.com), then update the URL in `content.js`:

js
const API_URL = "https://your-deployed-backend.com/summarize";


---

## 💡 Example Output

Original Post:

> He said it’s not cheating because it’s just an AI chatbot...

Summary:

> GF AI chatbot er sathe sexting kortese silently. Poster confused if eita cheating. Vibe off fully.

BS Meter:

> 87% 💩

---

## 📁 Project Structure


bs-detector-AWDSGD/
├── manifest.json
├── content.js
├── icon.png
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── .env         (not committed)
│   ├── .gitignore
│   └── README.md
└── README.md


---

## 📦 Tech Stack

* ✅ Chrome Extension (Manifest V3)
* ✅ Vanilla JS
* ✅ Flask (Python)
* ✅ OpenAI GPT-3.5 API
* ✅ Gen Z Banglish Prompt Engineering 🔥

---

## 🙌 Credits

Made with coffee and sarcasm by [@shamratneero](https://github.com/shamratneero)

---

## 📄 License

[MIT](LICENSE)

---

## 🚀 TODOs

* [ ] Deploy backend to Render/Railway
* [ ] Add comment reply generator
* [ ] Submit to Chrome Web Store
* [ ] Add animated demo GIF



Keep Vibin!
