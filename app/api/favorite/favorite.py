from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db

from app.services.favorite_service import FavoriteService
from app.schema.favorite_schema import FavoriteResponse
from app.utils.security import get_current_user

favoriteRouter = APIRouter()


@favoriteRouter.post(
    "/{property_id}",
    response_model=FavoriteResponse
)
async def add_to_favorite(
    property_id: UUID,
    db: AsyncSession = Depends(get_db),
    getUsers = Depends(get_current_user) 
):
    return await FavoriteService.add_favorite(
        db=db,
        user_id = getUsers,
        property_id = property_id
    )

@favoriteRouter.delete("/{property_id}")
async def remove_from_favorite(
    property_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user),
):
    return await FavoriteService.remove_favorite(
        db=db,
        user_id=current_user,
        property_id=property_id,
    )
