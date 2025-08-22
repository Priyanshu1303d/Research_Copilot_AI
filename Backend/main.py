from fastapi import FastAPI , UploadFile , File , Form
from fastapi.middleware.cors import CORSMiddleware
from Backend.schema import FileUploadResponse , ChatRequest , ChatResponse

app = FastAPI(title= "Research Copilot AI", 
              description="Backend API for chat, uploads, and RAG.",
              version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials  = True,
    allow_headers = ["*"],
    allow_methods = ["*"]
)


@app.get("/health")
def health_check():
    """Simple health check route."""
    return {"status" : "ok"}


@app.post("/chat", response_model = ChatResponse)
def chat(request : ChatRequest):
    """Dummy chat endpoint."""
    return ChatResponse(
        reply=f"Echo from {request.model_name}: {request.message}",
        session_id=request.session_id or "new-session-123"
    )

@app.post("/upload" , response_model = FileUploadResponse)
async def file_upload(file : UploadFile = File(...)):
    """Handle file upload (small image/video/pdf <= 50MB)."""

    contents = await file.read()

    size = len(contents)

    if size > 50*1024*1024 : 
        return {"error": "File too large!"}
    
    return FileUploadResponse(
        filename= file.filename,
        size = size ,
        type = file.content_type
    )
