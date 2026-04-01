from app.models.user_model import User
from app.models.task_model import Task

def criar_user(user_data, db):

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
