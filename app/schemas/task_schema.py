from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):
    titulo : str
    descricao: Optional[str]
    prioridade: str

class TaskResponde(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str]
    prioridade: str
    concluida: bool
    criado_em: datetime

    class Config:
        orm_mode = True