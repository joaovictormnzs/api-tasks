from fastapi import HTTPException, status
from app.models.user_model import User
from app.models.task_model import Task
from app.enums.user_role import UserRole

secret_key = "admin123"

def criar_user(user_data, db):

    if user_data.role == UserRole.lider:
        if user_data.access_key != secret_key:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Acesso negado: Chave de líder inválida.")

    new_user = User(
        name=user_data.name,
        role=user_data.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user 

def listar_users(db):
    return db.query(User).all()

def buscar_user(user_id, db):
    return db.query(User).filter(User.id == user_id).first()

def deletar_user(user, db):
    db.query(Task).filter(
        (Task.created_by_id == user.id) |
        (Task.assigned_to_id == user.id)
    ).delete()

    db.delete(user)
    db.commit()
