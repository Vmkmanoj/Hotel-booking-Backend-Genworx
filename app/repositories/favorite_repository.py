from sqlalchemy.orm import Session

from app.models.favorites import Favorite


class FavoriteRepository:

    @staticmethod
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

        return favorite
    
    @staticmethod
    def delete(
        db: Session,
        favorite: Favorite
    ):
        db.delete(favorite)
        db.commit()