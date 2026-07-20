from sqlalchemy.orm import Session
from app.models.users import User
from app.models.roles import Role
from app.models.property import Property


class DashboardRepository:

    def __init__(self, db: Session):
        self.db = db

    def total_users(self):
        return self.db.query(User).count()

    def total_customers(self):
        return (
            self.db.query(User)
            .join(Role)
            .filter(Role.name == "CUSTOMER")
            .count()
        )

    def total_property_owners(self):
        return (
            self.db.query(User)
            .join(Role)
            .filter(Role.name == "PROPERTY_OWNER")
            .count()
        )

    def total_admins(self):
        return (
            self.db.query(User)
            .join(Role)
            .filter(Role.name == "SUPER_ADMIN")
            .count()
        )

    def total_properties(self):
        return self.db.query(Property).count()

    def pending_properties(self):
        return (
            self.db.query(Property)
            .filter(Property.status == "PENDING")
            .count()
        )

    def approved_properties(self):
        return (
            self.db.query(Property)
            .filter(Property.status == "APPROVED")
            .count()
        )

    def rejected_properties(self):
        return (
            self.db.query(Property)
            .filter(Property.status == "REJECTED")
            .count()
        )