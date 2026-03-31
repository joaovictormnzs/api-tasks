from pydantic import BaseModel
from app.enums.user_role import UserRole

class UserCreate(BaseModel):
    name: str
    role: UserRole

class UserResponse(BaseModel):
    id: int
    name: str
    role: UserRole

    class Config:
        from_attributes = True
    
    
     