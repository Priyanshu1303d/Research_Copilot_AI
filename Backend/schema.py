from pydantic import BaseModel , Field 
from typing import Annotated , Optional , Literal 


class ChatRequest(BaseModel):
    name_of_model : str
    message : str
    session_id : Optional[str] = None


class ChatResponse(BaseModel):
    reply: str
    session_id : str


class FileUploadResponse(BaseModel):
    filename : str
    type: str
    size : int