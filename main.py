from app.routers import router
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from app.database.base import Base
from app.database.engine import engine

Base.metadata.create_all(bind=engine)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)
