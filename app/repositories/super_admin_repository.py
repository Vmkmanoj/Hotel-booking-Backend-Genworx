from sqlalchemy.orm import Session
from app.models.property import Property
from app.models.users import User
from app.models.address import Address
from datetime import datetime


class SuperAdminPropertyRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_pending_properties(self):

        return (
            self.db.query(
                Property.id,
                Property.property_name,
                User.first_name.label("owner_name"),
                User.email.label("owner_email"),
                Address.city,
                Address.state,
                Property.status,
                Property.created_at,
            )
            .join(User, Property.owner_id == User.id)
            .join(Address, Property.address_id == Address.id)
            .filter(Property.status == "PENDING")
            .order_by(Property.created_at.desc())
            .all()
        )

    def get_property_by_id(self, property_id):

        return (
            self.db.query(
                Property.id,
                Property.property_name,
                Property.description,

                User.first_name.label("owner_name"),
                User.email.label("owner_email"),
                User.phone.label("owner_phone"),

                Address.address_line_1,
                Address.address_line_2,
                Address.city,
                Address.state,
                Address.country,
                Address.postal_code,

                Property.property_type,
                Property.status,
                Property.is_verified,
                Property.created_at,
            )
            .join(User, Property.owner_id == User.id)
            .join(Address, Property.address_id == Address.id)
            .filter(Property.id == property_id)
            .first()
        )

    def approve_property(self, property):

        property.status = "APPROVED"
        property.is_verified = True

        self.db.commit()
        self.db.refresh(property)

        return property
    
    def get_approve_property(self):
        return (
            self.db.query(Property)
            .filter(Property.status == "APPROVED")
            .all()
        )
    

    def reject_property(
        self,
        property,
        remarks,
        admin_id=None
    ):

        property.status = "REJECTED"
        property.is_verified = False
        property.approval_remarks = remarks
        property.approved_by = admin_id
        property.approved_at = datetime.utcnow()

        self.db.commit()
        self.db.refresh(property)

        return property


    def suspend_property(
        self,
        property,
        remarks,
        admin_id=None
    ):

        property.status = "SUSPENDED"
        property.approval_remarks = remarks
        property.approved_by = admin_id

        self.db.commit()
        self.db.refresh(property)

        return property


    def activate_property(
        self,
        property,
        remarks,
        admin_id=None
    ):

        property.status = "APPROVED"
        property.is_verified = True
        property.approval_remarks = remarks
        property.approved_by = admin_id

        self.db.commit()
        self.db.refresh(property)

        return property


    def delete_property(self, property):

        property.is_deleted = True

        self.db.commit()