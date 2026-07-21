from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from app.database import get_db
from app.services.super_admin_service import SuperAdminPropertyService
from app.schema.super_admin_schema import PendingPropertyResponse ,PropertyDetailResponse ,MessageResponse , ApprovePropertyRequest
from app.schema.super_admin_property_schema import ActivatePropertyRequest , RejectPropertyRequest , SuspendPropertyRequest



superAdmin = APIRouter()

@superAdmin.get(
    "/property/pending",
    response_model=List[PendingPropertyResponse],
)
def pending_properties(
    db: Session = Depends(get_db),
):
    service = SuperAdminPropertyService(db)
    return service.get_pending_properties()


@superAdmin.get(
    "/property/{property_id}",
    response_model=PropertyDetailResponse,
)
def property_detail(
    property_id: UUID,
    db: Session = Depends(get_db),
):
    service = SuperAdminPropertyService(db)
    return service.get_property(property_id)


@superAdmin.patch(
    "/property/{property_id}/approve",
    response_model=MessageResponse,
)
def approve_property(
    property_id: UUID,
    request: ApprovePropertyRequest,
    db: Session = Depends(get_db),
):
    service = SuperAdminPropertyService(db)
    return service.approve_property(property_id, request)


@superAdmin.patch(
    "/property/{property_id}/reject",
    response_model=MessageResponse,
)
def reject_property(
    property_id: UUID,
    request: RejectPropertyRequest,
    db: Session = Depends(get_db),
):
    service = SuperAdminPropertyService(db)
    return service.reject_property(property_id, request)


@superAdmin.patch(
    "/property/{property_id}/suspend",
    response_model=MessageResponse,
)
def suspend_property(
    property_id: UUID,
    request: SuspendPropertyRequest,
    db: Session = Depends(get_db),
):
    service = SuperAdminPropertyService(db)
    return service.suspend_property(property_id, request)


@superAdmin.patch(
    "/property/{property_id}/activate",
    response_model=MessageResponse,
)
def activate_property(
    property_id: UUID,
    request: ActivatePropertyRequest,
    db: Session = Depends(get_db),
):
    service = SuperAdminPropertyService(db)
    return service.activate_property(property_id, request)


# @superAdmin.delete(
#     "/property/{property_id}",
#     response_model=MessageResponse
# )
# def delete_property(
#     property_id: UUID,
#     db: Session = Depends(get_db)
# ):
#     service = SuperAdminPropertyService(db)

#     return service.delete_property(
#         property_id
#     )