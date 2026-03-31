from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):
    title : str
    description: Optional[str]
    priority: str

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    priority: str
    conmpleted: bool
    created_by: datetime

    class Config:
        from_attributes = True