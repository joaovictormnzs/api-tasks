from sqlalchemy import Column, Integer, String
from app.database import Base 
from app.enums.user_role import UserRole

class User(Base):

    __tablename__="users" 

    id = Column(Integer, primary_key= True, index=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)