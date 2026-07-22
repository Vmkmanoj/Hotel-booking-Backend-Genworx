from dotenv import load_dotenv
import os

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
)

from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# DATABASE_URL example:
# postgresql+asyncpg://postgres:password@localhost:5432/hotel_booking

engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)

async def get_db():
    async with SessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()