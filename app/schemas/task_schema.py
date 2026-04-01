from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):
    title : str
    description: Optional[str]
    priority: str
    created_by_id: int
    assigned_to_id: Optional[int] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    priority: str
    completed: bool
    created_by_id: int
    assigned_to_id: int

    class Config:
        from_attributes = True