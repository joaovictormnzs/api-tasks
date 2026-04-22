from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum
from datetime import datetime
from app.database import Base
from app.enums.task_priority import TaskPriority
from sqlalchemy.orm import relationship

class Task(Base):

        __tablename__ = "tasks"

        id = Column(Integer, primary_key=True, index=True)
        title = Column(String)
        description = Column(String)
        priority = Column(Enum(TaskPriority), default=TaskPriority.BAIXA, nullable=False)
        completed = Column(Boolean, default=False)
        created_by_id = Column(Integer, ForeignKey("users.id"))
        assigned_to_id = Column(Integer, ForeignKey("users.id"))
        created_at = Column(DateTime, default=datetime.utcnow)

        created_by = relationship("User", foreign_keys=[created_by_id])
        assigned_to = relationship("User", foreign_keys=[assigned_to_id])