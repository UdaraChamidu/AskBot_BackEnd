# 🔧 AskBot Backend (FastAPI + Gemini API)

This is the backend for the AskBot Chatbot project. It's built using **FastAPI** and serves as the core engine that handles chat messages, integrates with the Gemini API, and returns AI-generated responses.

## 🚀 Live API

👉 [AskBot Backend on Railway](https://askbotbackend-production.up.railway.app/)

You can test the live backend here:
- Swagger UI: [https://askbotbackend-production.up.railway.app/docs](https://askbotbackend-production.up.railway.app/docs)

---

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8+
- virtual environment

---

### 🔍 Installation

1. Navigate to the backend directory:

   ```bash
   cd backend
   ```
2. Create and activate virtual environment:

```bash
python -m venv venv
venv/bin/activate 
```
3. Install dependencies:

```bash
pip install -r requirements.txt
```
env
GEMINI_API_KEY=your_gemini_api_key

## ▶️ Run Locally
Run the FastAPI app with:

```bash
uvicorn app.main:app --reload
```
