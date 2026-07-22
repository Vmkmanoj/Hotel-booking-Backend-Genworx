from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.services.favorite_service import FavoriteService
from app.schema.favorite_schema import FavoriteResponse
from app.utils.security import get_current_user

favoriteRouter = APIRouter()


@favoriteRouter.post(
    "/{property_id}",
    response_model=FavoriteResponse
)
def add_to_favorite(
    property_id: UUID,
    db: Session = Depends(get_db),
    getUsers = Depends(get_current_user) 
):
  
    return FavoriteService.add_favorite(
        db = db,
        user_id = getUsers,
        property_id = property_id
    )