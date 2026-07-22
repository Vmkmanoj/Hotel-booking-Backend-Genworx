<<<<<<< Updated upstream
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
=======
from sqlalchemy.orm import Session
>>>>>>> Stashed changes

from app.models.favorites import Favorite


class FavoriteRepository:

    @staticmethod
<<<<<<< Updated upstream
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
=======
    def get_by_user_and_property(
        db: Session,
        user_id,
        property_id
    ):
        return (
            db.query(Favorite)
            .filter(
                Favorite.user_id == user_id,
                Favorite.property_id == property_id
            )
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        favorite: Favorite
    ):
        db.add(favorite)
        db.commit()
        db.refresh(favorite)
>>>>>>> Stashed changes

        return favorite
    
    @staticmethod
<<<<<<< Updated upstream
    async def delete(
        db: AsyncSession,
        favorite: Favorite
    ):
        await db.delete(favorite)
        await db.commit()
=======
    def delete(
        db: Session,
        favorite: Favorite
    ):
        db.delete(favorite)
        db.commit()
>>>>>>> Stashed changes
