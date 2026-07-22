from app.routers import router
from contextlib import asynccontextmanager

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from app.database.engine import SessionLocal
from app.seed.seed_data import seed_database



@asynccontextmanager
async def lifespan(app: FastAPI):
    async with SessionLocal() as db:
        await seed_database(db)
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)
