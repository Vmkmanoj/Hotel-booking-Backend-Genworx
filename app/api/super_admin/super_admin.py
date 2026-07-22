from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from uuid import UUID
from app.database import get_db
from app.services.super_admin_service import SuperAdminPropertyService
from app.schema.super_admin_schema import PendingPropertyResponse, PropertyDetailResponse, MessageResponse, ApprovePropertyRequest
from app.schema.super_admin_property_schema import ActivatePropertyRequest, RejectPropertyRequest, SuspendPropertyRequest


superAdmin = APIRouter()


@superAdmin.get(
    "/property/pending",
    response_model=List[PendingPropertyResponse],
)
async def pending_properties(
    db: AsyncSession = Depends(get_db),
):
<<<<<<< Updated upstream
    return await SuperAdminPropertyService(db).get_pending_properties()
=======
    return await db.run_sync(lambda s: SuperAdminPropertyService(s).get_pending_properties())
>>>>>>> Stashed changes


@superAdmin.get(
    "/property/{property_id}",
    response_model=PropertyDetailResponse,
)
async def property_detail(
    property_id: UUID,
    db: AsyncSession = Depends(get_db),
):
<<<<<<< Updated upstream
    return await SuperAdminPropertyService(db).get_property(property_id)
=======
    return await db.run_sync(lambda s: SuperAdminPropertyService(s).get_property(property_id))
>>>>>>> Stashed changes


@superAdmin.patch(
    "/property/{property_id}/approve",
    response_model=MessageResponse,
)
async def approve_property(
    property_id: UUID,
    request: ApprovePropertyRequest,
    db: AsyncSession = Depends(get_db),
):
<<<<<<< Updated upstream
    return await SuperAdminPropertyService(db).approve_property(property_id, request)
=======
    return await db.run_sync(lambda s: SuperAdminPropertyService(s).approve_property(property_id, request))
>>>>>>> Stashed changes


@superAdmin.patch(
    "/property/{property_id}/reject",
    response_model=MessageResponse,
)
async def reject_property(
    property_id: UUID,
    request: RejectPropertyRequest,
    db: AsyncSession = Depends(get_db),
):
<<<<<<< Updated upstream
    return await SuperAdminPropertyService(db).reject_property(property_id, request)
=======
    return await db.run_sync(lambda s: SuperAdminPropertyService(s).reject_property(property_id, request))
>>>>>>> Stashed changes


@superAdmin.patch(
    "/property/{property_id}/suspend",
    response_model=MessageResponse,
)
async def suspend_property(
    property_id: UUID,
    request: SuspendPropertyRequest,
    db: AsyncSession = Depends(get_db),
):
<<<<<<< Updated upstream
    return await SuperAdminPropertyService(db).suspend_property(property_id, request)
=======
    return await db.run_sync(lambda s: SuperAdminPropertyService(s).suspend_property(property_id, request))
>>>>>>> Stashed changes


@superAdmin.patch(
    "/property/{property_id}/activate",
    response_model=MessageResponse,
)
async def activate_property(
    property_id: UUID,
    request: ActivatePropertyRequest,
    db: AsyncSession = Depends(get_db),
):
<<<<<<< Updated upstream
    return await SuperAdminPropertyService(db).activate_property(property_id, request)
=======
    return await db.run_sync(lambda s: SuperAdminPropertyService(s).activate_property(property_id, request))
>>>>>>> Stashed changes


# @superAdmin.delete(
#     "/property/{property_id}",
#     response_model=MessageResponse
# )
# def delete_property(
#     property_id: UUID,
#     db: Session = Depends(get_db)
# ):
#     service = SuperAdminPropertyService(db)
#
#     return service.delete_property(
#         property_id
#     )


@superAdmin.get(
    "/property/status/approved",
    # response_model=list[PropertyDetailResponse],
)
async def property_approved(
    db: AsyncSession = Depends(get_db),
):
<<<<<<< Updated upstream
    return await SuperAdminPropertyService(db).get_all_approved_property()
=======
    return await db.run_sync(lambda s: SuperAdminPropertyService(s).get_all_approved_property())
>>>>>>> Stashed changes
