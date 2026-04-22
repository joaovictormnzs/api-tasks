from pydantic import BaseModel
from typing import Optional
from app.enums.user_role import UserRole

class UserCreate(BaseModel):
    name: str
    role: UserRole
    access_key: Optional[str] = None 

class UserResponse(BaseModel):
    id: int
    name: str
    role: UserRole

    class Config:
        from_attributes = True
    
    
      