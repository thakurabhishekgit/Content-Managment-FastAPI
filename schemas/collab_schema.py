from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class CollabCreate(BaseModel):
    title: str = Field(..., min_length=3)
    description: str = Field(..., min_length=5)
    owner_id: str   # user who created
    req_collabs: Optional[List[str]] = []

class CollabResponse(BaseModel):
    id: str
    title: str
    description: str
    owner_id: str
    req_collabs: List[str]
    created_at: datetime
    updated_at: datetime