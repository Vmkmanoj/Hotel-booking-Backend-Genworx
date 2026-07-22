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
        print("userId",user_id)
        print("propertyId",property_id)

        property = (
        db.query(Property)
        .filter(
            Property.id == property_id,
            Property.is_deleted == False,
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
    

    @staticmethod
    def remove_favorite(
        db,
        user_id,
        property_id,
    ):
        favorite = FavoriteRepository.get_by_user_and_property(
            db=db,
            user_id=user_id,
            property_id=property_id,
        )

        if not favorite:
            raise HTTPException(
                status_code=400,
                detail="Favorite not found."
            )

        FavoriteRepository.delete(
            db=db,
            favorite=favorite
        )

        return {
            "success": True,
            "message": "Property removed from favorites."
        }