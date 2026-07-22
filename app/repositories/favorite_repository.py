from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.favorites import Favorite


class FavoriteRepository:

    @staticmethod
    async def get_by_user_and_property(
        db: AsyncSession,
        user_id,
        property_id
    ):
        result = await db.execute(select(Favorite).where(
            Favorite.user_id == user_id,
            Favorite.property_id == property_id,
        ))
        return result.scalar_one_or_none()

    @staticmethod
    async def create(
        db: AsyncSession,
        favorite: Favorite
    ):
        db.add(favorite)
        await db.commit()
        await db.refresh(favorite)

        return favorite
    
    @staticmethod
    async def delete(
        db: AsyncSession,
        favorite: Favorite
    ):
        await db.delete(favorite)
        await db.commit()
