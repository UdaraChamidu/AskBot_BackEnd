from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.langgraph_agent import agent

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add routes
app.include_router(agent.router)
