from fastapi import HTTPException
from app.services import task_service


def criar_task(task, db):
    return task_service.criar_task(task, db)


def listar_tasks(db):
    return task_service.listar_tasks(db)


def pegar_tarefa(task_id, db):
    task = task_service.buscar_por_id(task_id, db)

    if not task:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada!")

    return task


def atualizar_task(task_id, task_data, db):
    task = task_service.buscar_por_id(task_id, db)

    if not task:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada!")

    return task_service.atualizar_task(task, task_data, db)


def concluir_task(task_id, db):
    task = task_service.buscar_por_id(task_id, db)

    if not task:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada!")

    task_service.concluir_task(task, db)

    return {"message": "Tarefa completa!"}


def deletar_task(task_id, db):
    task = task_service.buscar_por_id(task_id, db)

    if not task:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada!")

    task_service.deletar_task(task, db)

    return {"message": "Tarefa deletada!"}