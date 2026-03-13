from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.database import Base

class Task(Base):

        __tablename__ = "tasks"

        id = Column(Integer, primary_key=True, index=True)
        titulo = Column(String)
        descricao = Column(String)
        prioridade = Column(String)
        concluida = Column(Boolean, default=False)
        criado_em = Column(DateTime, default=datetime.utcnow)