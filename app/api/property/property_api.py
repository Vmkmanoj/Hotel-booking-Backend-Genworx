from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schema.property_schema import  PropertyCreate, PropertyUpdate
from app.services.property_service import PropertyService 


propertyRouter = APIRouter()


@propertyRouter.post("/create")
async def create_property(
    property_data: PropertyCreate,
    db: AsyncSession = Depends(get_db)
):
    return await PropertyService.create_property(
        db=db,
        property_data=property_data
    )


@propertyRouter.get("/owner/{owner_id}")
async def get_my_properties(
    owner_id: UUID,
    db: AsyncSession = Depends(get_db)
):
    return await PropertyService.get_my_properties(
        db=db,
        owner_id=owner_id
    )


@propertyRouter.get("/{property_id}")
async def get_property_details(
    property_id: UUID,
    db: AsyncSession = Depends(get_db)
):
    return await PropertyService.get_property_details(
        db=db,
        property_id=property_id
    )


@propertyRouter.patch("/{property_id}")
async def update_property(
    property_id: UUID,
    owner_id: UUID,
    property_data: PropertyUpdate,
    db: AsyncSession = Depends(get_db)
):
    return await PropertyService.update_property(
        db=db,
        property_id=property_id,
        owner_id=owner_id,
        property_data=property_data
    )


@propertyRouter.patch("/{property_id}/archive")
async def archive_property(
    property_id: UUID,
    owner_id: UUID,
    db: AsyncSession = Depends(get_db)
):
    return await PropertyService.archive_property(
        db=db,
        property_id=property_id,
        owner_id=owner_id
    )


@propertyRouter.patch("/{property_id}/submit-review")
async def submit_property_for_review(
    property_id: UUID,
    owner_id: UUID,
    db: AsyncSession = Depends(get_db)
):
    return await PropertyService.submit_property_for_review(
        db=db,
        property_id=property_id,
        owner_id=owner_id
    )


@propertyRouter.delete("/{property_id}")
async def delete_draft_property(
    property_id: UUID,
    owner_id: UUID,
    db: AsyncSession = Depends(get_db)
):
    return await PropertyService.delete_draft_property(
        db=db,
        property_id=property_id,
        owner_id=owner_id
    )
