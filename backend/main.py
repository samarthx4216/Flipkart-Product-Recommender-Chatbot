from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from backend.rag_pipeline import chat
from backend.logger import setup_logger

logger = setup_logger("main")

app = FastAPI(title="Flipkart Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend
app.mount("/static", StaticFiles(directory="frontend"), name="static")

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    answer: str
    sources: list

@app.get("/")
def root():
    return FileResponse("frontend/index.html")

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    logger.info(f"Chat request: {request.message}")
    result = chat(request.message)
    return ChatResponse(
        answer=result["answer"],
        sources=result["sources"]
    )

@app.get("/health")
def health():
    return {"status": "healthy"}