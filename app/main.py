from fastapi import FastAPI
from app.database import Base, engine
from app.routes import task_routes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(task_routes.router)