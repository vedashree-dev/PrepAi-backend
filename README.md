# 📚 PrepAi Backend

PrepAi is an AI-powered question paper generator built for students and teachers. This backend service allows teachers/trainers to upload academic material and generate structured question papers with customizable difficulty, marks, and formats — powered by Ollama and local LLMs.

---

## 🚀 Features

* 📄 Upload PDF, DOCX, TXT content
* 🔍 Extracts chapters/topics and subtopics
* 🧠 AI-generated questions (MCQ, Short, Long, HOTS)
* 📊 Control marks, difficulty, question types, language
* 📁 Save/load custom paper templates (Premium)
* 🧾 Export to PDF, DOCX, or plain text
* 🤖 Powered by local LLM via Ollama (Mistral, LLaMA3)
* ✅ Razorpay-ready premium gating

---

## 📦 Folder Structure

```
PrepAi/
├── main.py
├── config.py
├── .env
├── requirements.txt
├── templates.json
├── models/
├── routers/
├── services/
├── utils/
```

---

## ⚙️ Setup Instructions

### 1. Clone and Install Dependencies

```bash
git clone https://github.com/yourorg/prepai.git
cd prepai
pip install -r requirements.txt
```

### 2. Environment Variables

Create a `.env` file:

```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL_NAME=mistral
RAZORPAY_SECRET=YOUR_KEY
EXPORT_DIR=./exported
```

### 3. Run Ollama (in separate terminal)

```bash
ollama run mistral
```

### 4. Start Backend

```bash
uvicorn main:app --reload
```

Then visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Sample API Endpoints

### `POST /upload/file`

* Upload PDF/DOCX
* Returns cleaned text + chunked topics

### `POST /generate/generate-paper`

* Accepts chunks + settings
* Returns full generated paper

### `POST /export/generate-paper-file`

* Converts paper to PDF or DOCX

### `POST /premium/save-template`

* Stores a custom paper configuration

### `GET /premium/load-template?title=...`

* Load previously saved paper config

---

## ✨ Frontend Compatibility

Designed to work with:

* ✅ Vercel/React/Next.js frontend
* ✅ Razorpay payment buttons
* ✅ Copy-paste or upload inputs

---

## 🛠️ Deployment Options

* [ ] Railway (1-click deploy)
* [ ] Render (gunicorn + FastAPI)
* [ ] Docker container (optional)

---

## ❤️ Credits

* Built using FastAPI, Ollama, PyMuPDF, PDFKit, scikit-learn
* Inspired by teachers who deserve better tools

---

## 📬 Contact

Want help scaling PrepAi? Reach out: `team@prepai.ai` or [@buildwithgpt](https://instagram.com/buildwithgpt)
