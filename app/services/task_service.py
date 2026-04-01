from fastapi import HTTPException
from app.models.task_model import Task
from app.models.user_model import User
from app.enums.user_role import UserRole

# controle global
ONLY_LEADER_CAN_CREATE = False


def criar_task(task_data, db):
    
    creator = db.query(User).filter(User.id == task_data.created_by_id).first()

    if not creator:
        raise HTTPException(status_code=404, detail="Criador nao encontrado")
    
    assigned = None
    if task_data.assigned_to_id:
        assigned = db.query(User).filter(User.id == task_data.assigned_to_id).first()

    if ONLY_LEADER_CAN_CREATE and creator.role != UserRole.lider:
        raise HTTPException(status_code=403, detail="Apenas lideres podem criar tarefas")
    
    if creator.role == UserRole.liderado and task_data.assigned_to_id:
        raise HTTPException(status_code=403, detail="Liderado nao pode atribuir tarefas")
    
    if creator.role == UserRole.liderado:
        task_data.assigned_to_id = creator.id

    if creator.role == UserRole.lider:
        if assigned.role != UserRole.liderado:
            raise HTTPException(status_code=400, detail="Lider so pode atribuir para liderados")
    
    new_task = Task(
        title = task_data.title,
        description = task_data.description,
        priority = task_data.priority,
        completed = False,
        created_by_id = task_data.created_by_id,
        assigned_to_id = task_data.assigned_to_id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

def listar_tasks(db):
    return db.query(Task).all()


def buscar_por_id(task_id, db):
    return db.query(Task).filter(Task.id == task_id).first()


def atualizar_task(task, task_data, db):
    task.title = task_data.title
    task.description = task_data.description
    task.priority = task_data.priority

    db.commit()
    db.refresh(task)

    return task


def concluir_task(task, db):
    task.completed = True
    db.commit()
    db.refresh(task)


def deletar_task(task, db):
    db.delete(task)
    db.commit()