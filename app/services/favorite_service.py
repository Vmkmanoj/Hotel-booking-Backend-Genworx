from fastapi import HTTPException

from app.models.favorites import Favorite
from app.models.property import Property

from app.repositories.favorite_repository import FavoriteRepository

from app.schema.favorite_schema import FavoriteResponse


class FavoriteService:

    @staticmethod
    def add_favorite(
        db,
        user_id,
        property_id
    ):

        property = (
            db.query(Property)
            .filter(
                Property.id == property_id,
                not Property.is_deleted,
                Property.status == "APPROVED"
            )
            .first()
        )

        if not property:
            raise HTTPException(
                status_code=404,
                detail="Property not found."
            )

        favorite = FavoriteRepository.get_by_user_and_property(
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

        FavoriteRepository.create(
            db,
            favorite
        )

        return FavoriteResponse(
            success=True,
            message="Property added to favorites."
        )