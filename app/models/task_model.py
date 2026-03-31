from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

class Task(Base):

        __tablename__ = "tasks"

        id = Column(Integer, primary_key=True, index=True)
        title = Column(String)
        description = Column(String)
        priority = Column(String)
        completed = Column(Boolean, default=False)


        created_by_id = Column(Integer, ForeignKey("user.id"))
        assigned_to_id = Column(Integer, ForeignKey("user.id"))