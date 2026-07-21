from sqlalchemy.orm import Session

from app.models.address import Address
from app.schema.address import AddressCreate, AddressUpdate


class AddressRepository:

    @staticmethod
    def create(db: Session, address_data: AddressCreate):
        try:
            address = Address(**address_data.model_dump())

            db.add(address)
            db.commit()
            db.refresh(address)

            return address

        except Exception:
            db.rollback()
            raise

    @staticmethod
    def get_all(db: Session):
        try:
            return db.query(Address).all()

        except Exception:
            raise

    @staticmethod
    def get_by_id(db: Session, address_id):
        try:
            return (
                db.query(Address)
                .filter(Address.id == address_id)
                .first()
            )

        except Exception:
            raise

    @staticmethod
    def update(db: Session, address: Address, address_data: AddressUpdate):
        try:
            update_data = address_data.model_dump(exclude_unset=True)

            for key, value in update_data.items():
                setattr(address, key, value)

            db.commit()
            db.refresh(address)

            return address

        except Exception:
            db.rollback()
            raise

    @staticmethod
    def delete(db: Session, address: Address):
        try:
            db.delete(address)
            db.commit()

        except Exception:
            db.rollback()
            raise