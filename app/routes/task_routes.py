from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.controllers import task_controller
from app.schemas.task_schema import TaskCreate, TaskResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/tasks", response_model=TaskResponse)
def criar_task(task: TaskCreate, db: Session = Depends(get_db)):
    return task_controller.criar_task(task, db)


@router.get("/tasks", response_model=list[TaskResponse])
def listar_tasks(db: Session = Depends(get_db)):
    return task_controller.listar_tasks(db)


@router.get("/tasks/{task_id}", response_model=TaskResponse)
def pegar_tarefa(task_id: int, db: Session = Depends(get_db)):
    return task_controller.pegar_tarefa(task_id, db)


@router.put("/tasks/{task_id}")
def atualizar_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    return task_controller.atualizar_task(task_id, task, db)


@router.patch("/tasks/{task_id}/complete")
def concluida_task(task_id: int, db: Session = Depends(get_db)):
    return task_controller.concluir_task(task_id, db)


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return task_controller.deletar_task(task_id, db)

@router.post("/config/only-leader")
def set_mode(only_leader: bool):
    return task_controller.toggle_mode(only_leader)