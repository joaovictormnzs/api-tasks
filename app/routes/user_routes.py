from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.controllers import user_controller
from app.schemas.user_schema import UserCreate

router = APIRouter(prefix="/users", tags=["Users"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("")
def criar_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_controller.criar_user(user, db)


@router.get("/")
def listar_users(db: Session = Depends(get_db)):
    return user_controller.listar_users(db)


@router.get("/{user_id}")
def pegar_user(user_id: int, db: Session = Depends(get_db)):
    return user_controller.pegar_user(user_id, db)

@router.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user_controller.deletar_user(user_id, db)