import os
import traceback
from dotenv import load_dotenv
from fastapi import APIRouter, Query
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import google.generativeai as genai

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use Gemini flash model
model = genai.GenerativeModel("gemini-2.5-flash")

router = APIRouter()

# Store sessions in memory
chat_sessions = {}  # { session_id: [ {"role": "user"/"assistant", "content": "..."} ] }

# Request and Response models
class ChatRequest(BaseModel):
    session_id: str
    user_message: str

class ChatResponse(BaseModel):
    reply: str

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # Start new session if needed
        if request.session_id not in chat_sessions:
            chat_sessions[request.session_id] = []

        # Save user message
        chat_sessions[request.session_id].append({
            "role": "user",
            "content": request.user_message
        })

        # Format full chat history for Gemini
        conversation = []
        for msg in chat_sessions[request.session_id]:
            prefix = "You: " if msg["role"] == "user" else "Bot: "
            conversation.append(prefix + msg["content"])

        prompt = "\n".join(conversation)

        # Generate response
        response = model.generate_content(prompt)
        reply_text = response.text.strip()

        # Save bot reply
        chat_sessions[request.session_id].append({
            "role": "assistant",
            "content": reply_text
        })

        return ChatResponse(reply=reply_text)

    except Exception as e:
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"error": str(e)})

# Endpoint to fetch full chat history
@router.get("/history")
async def get_history(session_id: str = Query(...)):
    return {
        "messages": chat_sessions.get(session_id, [])
    }
