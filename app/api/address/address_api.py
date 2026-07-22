from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.engine import get_db

from app.schema.address import (
    AddressCreate,
    AddressUpdate,
    AddressResponse,
)
from app.services.address_service import AddressService

addressRouter = APIRouter()


@addressRouter.post("/create", response_model=AddressResponse, status_code=201)
def create_address(
    address: AddressCreate,
    db: Session = Depends(get_db)
):
    return AddressService.create_address(db, address)


@addressRouter.get( "/", response_model=list[AddressResponse])
def get_all_addresses(
    db: Session = Depends(get_db)
):
    return AddressService.get_all_addresses(db)


@addressRouter.get("/{address_id}",response_model=AddressResponse)
def get_address(
    address_id: UUID,
    db: Session = Depends(get_db)
):
    return AddressService.get_address(db, address_id)


@addressRouter.patch(
    "/{address_id}",
    response_model=AddressResponse
)
def update_address(
    address_id: UUID,
    address: AddressUpdate,
    db: Session = Depends(get_db)
):
    return AddressService.update_address(
        db,
        address_id,
        address
    )


# @addressRouter.delete(
#     "/{address_id}"
# )
# def delete_address(
#     address_id: UUID,
#     db: Session = Depends(get_db)
# ):
#     return AddressService.delete_address(
#         db,
#         address_id
#     )