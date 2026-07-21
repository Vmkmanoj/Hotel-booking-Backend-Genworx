from uuid import UUID

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.models.property import Property
from app.schema.property_schema import PropertyUpdate
from app.models.address import Address


class PropertyRepository:

    @staticmethod
    def create(db: Session, address: Address, property_obj: Property):
        try:
            db.add(address)

            db.flush()

            property_obj.address_id = address.id

            db.add(property_obj)

            db.commit()

            db.refresh(address)
            db.refresh(property_obj)

            return property_obj

        except SQLAlchemyError:
            db.rollback()
            raise

        
    @staticmethod
    def get_all(db: Session):
        try:
            return db.query(Property).all()

        except SQLAlchemyError:
            raise

    @staticmethod
    def get_by_owner_id(db: Session, owner_id: UUID):
        try:
            return (
                db.query(Property)
                .filter(Property.owner_id == owner_id)
                .all()
            )

        except SQLAlchemyError:
            raise

    @staticmethod
    def get_by_id(db: Session, property_id: UUID):
        try:
            return (
                db.query(Property)
                .filter(Property.id == property_id)
                .first()
            )

        except SQLAlchemyError:
            raise

    @staticmethod
    def update(
        db: Session,
        property_obj: Property,
        property_data: PropertyUpdate
    ):
        try:

            update_data = property_data.model_dump(exclude_unset=True)

            for key, value in update_data.items():
                setattr(property_obj, key, value)

            db.commit()
            db.refresh(property_obj)

            return property_obj

        except SQLAlchemyError:
            db.rollback()
            raise

    @staticmethod
    def archive(db: Session, property_obj: Property):
        try:

            property_obj.status = "Archived"

            db.commit()
            db.refresh(property_obj)

            return property_obj

        except SQLAlchemyError:
            db.rollback()
            raise

    @staticmethod
    def submit_for_review(db: Session, property_obj: Property):
        try:

            property_obj.status = "Pending Review"

            db.commit()
            db.refresh(property_obj)

            return property_obj

        except SQLAlchemyError:
            db.rollback()
            raise

    @staticmethod
    def delete(db: Session, property_obj: Property):
        try:

            db.delete(property_obj)
            db.commit()

            return True

        except SQLAlchemyError:
            db.rollback()
            raise