from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ContentCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=5)
    tags: Optional[list[str]] = []

class ContentUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    tags: Optional[list[str]]

class ContentResponse(BaseModel):
    id: str
    title: str
    description: str
    tags: list[str]
    created_at: datetime
    updated_at: datetime