from fastapi import FastAPI
from app.database import Base, engine

from app.routes.task_routes import router as task_router
from app.routes.user_routes import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(task_router)
app.include_router(user_router)