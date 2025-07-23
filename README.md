# 🔧 AskBot Backend (FastAPI + Gemini API)

This is the backend for the AskBot Chatbot project. It's built using **FastAPI** and serves as the core engine that handles chat messages, integrates with the Gemini API, and returns AI-generated responses.

## 🚀 Live API

### ✅ AskBot FrontEnd (Vercel)
[![AskBot FrontEnd](https://img.shields.io/badge/AskBot-FrontEnd-000?style=for-the-badge&logo=vercel&logoColor=white)](https://ask-bot-front-end-git-main-udarachamidus-projects.vercel.app/)

### ✅ AskBot BackEnd (Railway)
[![AskBot BackEnd](https://img.shields.io/badge/AskBot-BackEnd-000?style=for-the-badge&logo=railway&logoColor=white)](https://railway.com/project/8c80da65-edde-4b47-bbc7-0b192d3f2e83/service/14b1a878-be2f-4d80-b481-8de56c8f9998?environmentId=a31d7c2a-1e3b-459e-9b1d-56dc5af1c3b9)

---

## Screenshots

<img width="1918" height="1078" alt="image" src="https://github.com/user-attachments/assets/b1f11d72-dd80-411d-9d11-1ae9a9640cad" />

### Vercel Frontend Screenshot

<img width="1918" height="1078" alt="image" src="https://github.com/user-attachments/assets/9b9158dd-ef45-4d6e-b951-219479537425" />

### Railway - Backend Screenshot

<img width="1918" height="1078" alt="image" src="https://github.com/user-attachments/assets/02916181-63a9-4a92-9998-1af07d8b7c11" />

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

---

## ▶️ Run Locally
Run the FastAPI app with:

```bash
uvicorn app.main:app --reload
```

---

## 📦 Deployment

The backend is deployed on Railway.
