from fastapi import HTTPException
from app.services import user_service

def criar_user(user, db):
    return user_service.criar_user(user, db)

def listar_users(db):
    return user_service.listar_users(db)

def pegar_user(user_id, db):
    user = user_service.buscar_user(user_id, db)

    if not user:
        raise HTTPException(status_code=404, detail="User nao encontrado")
    
    return user

