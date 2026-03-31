from app.models.task_model import Task


def criar_task(task_data, db):
    new_task = Task(**task_data.dict())

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