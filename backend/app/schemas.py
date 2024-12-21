from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

class Token(BaseModel):
    access_token: str
    token_type: str

class ChatCreate(BaseModel):
    file_path: str

class ChatResponse(BaseModel):
    id: int
    analysis: Dict[str, Any]
    timestamp: datetime

class ChatListResponse(BaseModel):
    chats: List[ChatResponse]
