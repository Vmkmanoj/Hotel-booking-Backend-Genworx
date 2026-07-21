from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

@router.post("/",response_model=RoomTypeResponse)
def create_room():
    pass