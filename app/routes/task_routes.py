from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.task_model import Task
from app.schemas.task_schema import TaskCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Criar Tarefas
@router.post("/tasks")
def criar_task(task: TaskCreate, db: Session = Depends(get_db)):
    criar_task = Task(**task.dict())

    db.add(criar_task)
    db.commit()
    db.refresh(criar_task)

    return criar_task

#Listar Tarefas
@router.get("/tasks")
def listar_tasks(db: Session = Depends(get_db)):
    
    tasks = db.query(Task).all()

    return tasks


#Buscar Tarefa por ID
@router.get("/task")
def pegar_tarefa(task_id: int, db: Session = Depends(get_db)):

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code= 404, detail="Tarefa nao encontrada")
    
    return task

#Atualizar tarefa
@router.put("/tasks/{task_id}")
def atualizar_task(task_id: int, updated_task: TaskCreate, db: Session = Depends(get_db)):

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
    
    task.titulo = atualizar_task.titulo
    task.descricao = atualizar_task.descricao
    task.prioridade = atualizar_task.prioridade

    db.commit()
    db.refresh(task)

    return task


# Marcar como concluida
@router.patch("/tasks/{task_id}/complete")
def concluida_task(task_id: int, db: Session = Depends(get_db)):

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada")

    task.concluida = True

    db.commit()

    return {"message": "Tarefa concluida!"}


#Deletar tarefa
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada")

    db.delete(task)
    db.commit()

    return {"message": "Task deletada"}


            

