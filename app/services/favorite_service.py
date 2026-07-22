from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.favorites import Favorite
from app.models.property import Property, PropertyStatus

from app.repositories.favorite_repository import FavoriteRepository

from app.schema.favorite_schema import FavoriteResponse


class FavoriteService:

    @staticmethod
    async def add_favorite(
        db: AsyncSession,
        user_id,
        property_id
    ):
        property = (await db.execute(select(Property).where(
            Property.id == property_id,
            Property.is_deleted.is_(False),
            Property.status == PropertyStatus.APPROVED.value,
        ))).scalar_one_or_none()

        if not property:
            raise HTTPException(
                status_code=404,
                detail="Property not found."
            )

        favorite = await FavoriteRepository.get_by_user_and_property(
            db,
            user_id,
            property_id
        )

        if favorite:
            raise HTTPException(
                status_code=400,
                detail="Property already added to favorites."
            )

        favorite = Favorite(
            user_id=user_id,
            property_id=property_id,
            created_by=str(user_id),
            updated_by=str(user_id),
        )

        await FavoriteRepository.create(
            db,
            favorite
        )

        return FavoriteResponse(
            success=True,
            message="Property added to favorites."
        )
    

    @staticmethod
    async def remove_favorite(
        db: AsyncSession,
        user_id,
        property_id,
    ):
        favorite = await FavoriteRepository.get_by_user_and_property(
            db=db,
            user_id=user_id,
            property_id=property_id,
        )

        if not favorite:
            raise HTTPException(
                status_code=400,
                detail="Favorite not found."
            )

        await FavoriteRepository.delete(
            db=db,
            favorite=favorite
        )

        return {
            "success": True,
            "message": "Property removed from favorites."
        }
